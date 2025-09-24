import pandas as pd

def preprocess(df,region_df):
    #filitering for summer olympics
    df =  df[df['Season'] == 'Summer']
    #merge with region_df
    df = df.merge(region_df, how='left', on='NOC')
    #dropping duplicates
    df.drop_duplicates(inplace=True)
    # encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df