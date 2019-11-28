#!/bin/env python3
# -*- coding: utf-8 -*-

def load_raw_data (DF_Name, File_name, sep=',', PATH=PATH):
    '''
    Loads the data, sorts the columns alphabetically.
    And sores a copy of the sorted frame in the processed folder, 
    with a timestamp.
    
    DF_Name:
    File_name:
    sep:
    PATH:
    '''
    timestamp = time.strftime('%S')
    DF_Name = pd.read_csv(PATH+File_name, sep)
    DF_Name = DF_Name.reindex(sorted(DF_Name.columns), axis=1)
    DF_Name.to_csv(PATH+'data/processed/'+DF_Name+timestamp+'.csv')
    print('/nLoaded data: ',File_name, 'as', DF_Name)
    return DF_Name



def store_unitsize_data(filename, df=df, size_treshold=0.0,PATH=PATH):
    timestamp = time.strftime('%S')
    
    below_treshold=df.loc[df[unit_area]< size_treshold]
    below_treshold.to_csv(PATH+'data/interim/below_treshold'\
                          +filename+timestamp+'.csv')
    above_treshold=df.loc[df[unit_area]< size_treshold]
    above_treshold.to_csv(PATH+'data/interim/above_treshold'\
                          +filename+timestamp+'.csv')


    
def load_geo_variables(name_file):
    '''
    '''
    df_list = []
    for k, v in name_file.item():
        k = pd.read_csv(PATH+'data/raw/'+v+'.csv', sep=';')
        df_list.append(k)
        
    geo_df = join_df_2_one('geo_df',
                              old_dfs=df_list,
                              join_on = GEO_BYGGNINGNR
                             )
    return geo_df


def create_statbank_tables_simple(df, groupings_name, counter_col, math_func, path):
    for k, v in groupings_name.items():
        if math_func == 'sum':
            table = df.groupby(v)[counter_col].sum().fillna(0)
        elif math_func == 'mean':
            table = df.groupby(v)[counter_col].mean().fillna(0)
        elif math_func == 'count':
            table = df.groupby(v)[counter_col].count().fillna(0)
        else:
            print('please spessify aggregation type')
            
        table.to_csv(path+k+'.csv', sep=';')

        return 'Statbank table created'
    
def create_statbank_tables_complex(df, groupings_name, counter_col, math_func, path):
    for k, v in groupings_name.items():
        if math_func == 'sum':
            table = df.groupby(v)[counter_col]\
                      .sum()\
                      .unstack()\
                      .reset_index()\
                      .fillna(0)
        elif math_func == 'mean':
            table = df.groupby(v)[counter_col]\
                      .mean()\
                      .unstack()\
                      .reset_index()\
                      .fillna(0)
        elif math_func == 'count':
            table = df.groupby(v)[counter_col]\
                      .count()\
                      .unstack()\
                      .reset_index()\
                      .fillna(0)
        else:
            print('please spessify aggregation type')
            
        table.to_csv(path+k+'.csv', sep=';')