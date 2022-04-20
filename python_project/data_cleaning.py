def loading_data():
    path = 'data/df_listings_revenue_1.csv'
    return pd.read_csv(path)

def data_cleaning(df1):
    #Change strings to 0
    df1['cama_casal'] = df1['cama_casal'].apply(lambda x: 0 if x == 'Quantidade de Camas Casal' else x)
    df1['cama_solteiro'] = df1['cama_solteiro'].apply(lambda x: 0 if x == 'Quantidade de Camas Solteiro' else x)
    df1['cama_queen'] = df1['cama_queen'].apply(lambda x: 0 if x == 'Quantidade de Camas Queen' else x)
    df1['cama_king'] = df1['cama_king'].apply(lambda x: 0 if x == 'Quantidade de Camas King' else x)
    df1['sofa_cama_solteiro'] = df1['sofa_cama_solteiro'].apply(
        lambda x: 0 if x == 'Quantidade de Sofás Cama Solteiro' else x)
    df1['banheiros'] = df1['banheiros'].apply(lambda x: 0 if x == 'Banheiros' else x)

    # Change 'endereco' Nan to 'não consta'
    df1['endereco'] = df1[['endereco']].fillna('none')

    # Change Nan in registers to 0
    df1['cama_casal'] = df1['cama_casal'].apply(lambda x: 0 if math.isnan(x) else x)
    df1['cama_solteiro'] = df1['cama_solteiro'].apply(lambda x: 0 if math.isnan(x) else x)
    df1['cama_queen'] = df1['cama_queen'].apply(lambda x: 0 if math.isnan(x) else x)
    df1['cama_king'] = df1['cama_king'].apply(lambda x: 0 if math.isnan(x) else x)
    df1['sofa_cama_solteiro'] = df1['sofa_cama_solteiro'].apply(lambda x: 0 if math.isnan(x) else x)
    df1['travesseiros'] = df1['travesseiros'].apply(lambda x: 0 if math.isnan(x) else x)
    df1['banheiros'] = df1['banheiros'].apply(lambda x: 0 if math.isnan(x) else x)
    df1['taxa_limpeza'] = df1['taxa_limpeza'].apply(lambda x: 0 if math.isnan(x) else x)
    df1['capacidade'] = df1['capacidade'].apply(lambda x: 0 if math.isnan(x) else x)
    #df1['creation_date'] = df1['creation_date'].apply(lambda x: '0000-00-00 00:00:00' if pd.isnull(x) else x)

    # change occupancy 2 to 1
    df1['occupancy'] = df1['occupancy'].apply(lambda x: 1 if x == 2 else x)

    # drop id= TST001, this listing no data about revenue or especifics data
    df1 = df1[~df1['id'].isin(['TST001'])]

    # Check NA
    print('===========================================')
    print('Numbers of NaNs:\n')
    print(df1.isna().sum())

    return df1

def change_types(df1):
    # Chage type data df daily revanue and Listings
    df1['date'] = pd.to_datetime(df1['date'])
    df1['creation_date'] = pd.to_datetime(df1['creation_date'])

    df1['data_inicial_contrato'] = pd.to_datetime(df1['data_inicial_contrato'], dayfirst = True)

    # Change type to float df listings
    df1.comissao.astype(float)
    df1.cama_casal = df1.cama_casal.astype(float)
    df1.cama_solteiro = df1.cama_solteiro.astype(float)
    df1.cama_queen = df1.cama_queen.astype(float)
    df1.cama_king = df1.cama_king.astype(float)
    df1.sofa_cama_solteiro = df1.sofa_cama_solteiro.astype(float)
    df1.banheiros = df1.banheiros.astype(float)
    df1.capacidade = df1.capacidade.astype(float)
    df1.occupancy = df1.occupancy.astype(int)


    # Data Types
    print('===========================================')
    print('Columns Data Types:\n')
    print(df1.dtypes)

    #Features Engeneering:

    #New columns, year, month and day
    df1['year'] = pd.DatetimeIndex(df1['date']).year
    df1['month'] = pd.DatetimeIndex(df1['date']).month
    df1['day'] = pd.DatetimeIndex(df1['date']).day

    #New columns seasons
    df1['season'] = 'season'
    df1['season'] = df1['month'].apply(lambda x: 'summer' if (x >= 1) & (x <= 3)
    else 'fall' if (x >= 4) & (x <= 6)
    else 'spring' if (x >= 10) & (x <= 12)
    else 'winter')



    # Print sample dataframe
    print('\n===========================================')
    print('News Features: year, month, day and season\n')
    print(df1[['date', 'year', 'month', 'day', 'season']].sample(5))

    # df only listings occupancy = 1
    df2 = df1.loc[(df1['occupancy'] == 1) & (df1['blocked'] == 0) ]

    # Check NA
    print('===========================================')
    print('Numbers of NaNs in listings occupancy = 1 \n')
    print(df2.isna().sum())

    #Check date > creation_date
    df2['lead_time'] =  (df2.date - df2.creation_date).dt.days
    dfaux = df2.loc[df2.lead_time < 0 ]
    print(f'Number of listings with creation_date > date:{len(dfaux)} ')

    #export new data
    df1.to_csv('data/df_listings_revenue_total.csv', index=False)
    df2.to_csv('data/df_listings_revenue_occupancy.csv', index=False)

if __name__ == '__main__':
    # IMPORT LIBRIES
    import pandas as pd
    import numpy as np
    import math
    import warnings
    warnings.filterwarnings('ignore')

    df_raw = loading_data()
    df1 = data_cleaning(df_raw )
    change_types(df1)
