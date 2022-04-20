def loading_data():
    path = 'data/df_listings_revenue_total.csv'
    return pd.read_csv(path)



def descriptive_statistics(df1):
    #separte data in numerical and categorical attributes
    num_attributes = df1.select_dtypes(include=['int64', 'float64'])
    cat_attributes = df1.select_dtypes(exclude=['int64', 'float64', 'datetime64[ns]'])

    # Central tendency - mean, median
    ct1 = pd.DataFrame(num_attributes.apply(np.mean)).T
    ct2 = pd.DataFrame(num_attributes.apply(np.median)).T

    # Dispersion - std, min, max, range, skew, kurtosis
    d1 = pd.DataFrame(num_attributes.apply(np.std)).T
    d2 = pd.DataFrame(num_attributes.apply(min)).T
    d3 = pd.DataFrame(num_attributes.apply(max)).T
    d4 = pd.DataFrame(num_attributes.apply(lambda x: x.max() - x.min())).T
    d5 = pd.DataFrame(num_attributes.apply(lambda x: x.skew())).T
    d6 = pd.DataFrame(num_attributes.apply(lambda x: x.kurtosis())).T

    # concatenate
    m = pd.concat([d2, d3, d4, ct1, ct2, d1, d5, d6]).T.reset_index()
    m.columns = ['attributes', 'min', 'max', 'range', 'mean', 'median', 'std', 'skew', 'kurtosis']
    print(m)
    m.to_csv('data/statistics/df_num_statistics.csv', index=False)

    print('===========================================')
    print('Statistics Numerical Atributes:\n')





if __name__ == '__main__':
    # IMPORT LIBRIES
    import pandas as pd
    import numpy  as np
    import math
    import seaborn as sns
    import matplotlib.pyplot as plt

    import sweetviz as sv

    import warnings
    warnings.filterwarnings('ignore')

    #Loading Data
    df_raw = loading_data()

    #Plot Estatistics Analysis
    descriptive_statistics(df_raw)

    #Generate Plots Univariate Analysis using analyze
    my_report = sv.analyze(df_raw)

    my_report.show_html()