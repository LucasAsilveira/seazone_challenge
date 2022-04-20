def loading_data():
    #paths to datas
    path_daily_revenue = 'data/daily_revenue_1.csv'
    path_listings      = 'data/listings-challenge_3.csv'

    #loading datas
    df_daily_revenue = pd.read_csv(path_daily_revenue)
    df_listings = pd.read_csv(path_listings)

    #reanamen key columns
    df_listings = df_listings.rename(columns={"Código": "id"})
    df_daily_revenue = df_daily_revenue.rename(columns={"listing": "id"})

    #merge dataframes
    df_raw = pd.merge(df_daily_revenue, df_listings, on='id', how='left')
    return df_raw

def data_description(df):
    #create copy df
    df1 = df_raw.copy()


    #rename columns:
    #rename columns to facilitate data manipulation
    cols_news = ['id', 'date', 'last_offered_price', 'occupancy', 'revenue', 'blocked',
                 'creation_date', 'localizacao', 'categoria', 'comissao', 'endereco',
                 'cama_casal', 'cama_solteiro', 'cama_queen', 'cama_king',
                 'sofa_cama_solteiro', 'travesseiros', 'banheiros', 'taxa_limpeza',
                 'capacidade', 'hotel', 'data_inicial_contrato', 'status', 'tipo']
    df1.columns = cols_news

    # Data Dimensions:
    # Dimension df daily revenue
    print('===========================================')
    print('Dimensions Dataframe:\n')
    print('Number of Rows: {}'.format(df1.shape[0]))
    print('Number of cols: {}\n'.format(df1.shape[1]))

    # Data Types
    print('===========================================')
    print('Columns Data Types:\n')
    print(df1.dtypes)


    # Check NA
    print('===========================================')
    print('Numbers of NaNs:\n')
    print(df1.isna().sum())
    df1.to_csv('data/df_listings_revenue_1.csv', index=False)

if __name__ == '__main__':
    # IMPORT LIBRIES
    import pandas as pd

    df_raw = loading_data()

    data_description(df_raw)


