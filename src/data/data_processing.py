#!/usr/bin/env python

import pandas as pd
import numpy as np

def set_min_value(df, col, min_value):
    '''
    '''
    for col in col:
        df[col+'_adj'] = df[col].where(df[col]>min_value, min_value)
        
    return df


def Collect_area_from_prioritised_3variables(df,prioritised_col,new_col, treshold_value, math_index = None, math_col= None, mathtype= None):
    '''
    '''
    for col in prioritised_col:
        for cell in df[col]:
            try:
                val = int(cell)
            except ValueError:
                df[col] = df[col].replace(cell, np.nan)
        
    for col in prioritised_col:
        df[col] = pd.to_numeric(df[col])
        df[col] = df[col].mask(df[col] < treshold_value)
    
    if math_index is not None:
        if mathtype == 'div':
            df[prioritised_col[math_index]] = df[prioritised_col[math_index]]/df[math_col]
        
            print('Dividing:' + str(prioritised_col[math_index]) +' by ' + str(math_col))
        elif mathtype == 'mult':
            df[prioritised_col[math_index]] = df[prioritised_col[math_index]]*df[math_col]
        
            print('multiplying:' + str(prioritised_col[math_index]) +' by ' + str(math_col))
        else:
            print('Please provide a math function to employ on the variables')
            
        df[new_col] = df[prioritised_col[0]]\
        .combine_first(df[prioritised_col[1]])\
        .combine_first(df[prioritised_col[2]])\
        .fillna(0)
    
    else:    
        df[new_col] = df[prioritised_col[0]]\
        .combine_first(df[prioritised_col[1]])\
        .combine_first(df[prioritised_col[2]])\
        .fillna(0)
    
    return df

def add_counter_col(df, grouping_col, counting_col, new_col_name):
    counter = df.groupby(grouping_col)[counting_col].count().reset_index()
    counter.columns = [grouping_col, new_col_name]
    df = pd.merge(df, counter, on=grouping_col, how ='left')
    
    return df

def conditional_area_adjustments(df, unit_area, total_area, counter_col, min_treshold=1, max_treshold=1000):
    '''
    This is a highly custom function for this script only, 
    it aims to make sure that unit size i not larger than total size,
    and that in the case of missing unit size we can take a proportion of 
    the total area, instead. 
    
    * This should possibly be improoved upon later*
    '''
    tot = np.array(df[total_area].values.tolist())
    a = np.array(df[unit_area].values.tolist())
    ant = np.array(df[counter_col].values.tolist()) 
    
    df[unit_area] = np.where((a>tot)&(a<min_treshold), a, a).tolist()
    df[unit_area] = np.where((a>tot)&(a>min_treshold),tot, a).tolist()
    df[unit_area] = np.where(((a==0.0)|(a>max_treshold)|(a>tot)),(tot/ant), a).tolist()
    df[total_area] = np.where((tot<a)&(tot<min_treshold),a, tot).tolist()
    
    return df

def total_area_unit_area_adjustments(df, unit_area, total_area,min_treshold):
    '''
    This is a highly custom function for this script only, 
    it aims to make sure that unit size i not larger than total size,
    and that in the case of missing unit size we can take a proportion of 
    the total area, instead. 
    
    * This should possibly be improoved upon later*
    '''
    tot = np.array(df[total_area].values.tolist())
    a = np.array(df[unit_area].values.tolist())
    
    df[total_area] = np.where((tot<a)&(tot<min_treshold),a, tot).tolist()
    
    return df

def join_df_2_one(new_df, old_dfs, join_on):
    '''
    Function that coins a list of Data Frames to a singel frame
    '''
    new_df = old_dfs[0]
    for i in old_dfs[1:]:
        new_df = pd.merge(new_df, i, on=join_on)

    return new_df

def seperate_by_value(df, split_col, split_value, new_df):
    '''
    Split a Data frame in to by a value
    '''
    new_df[0] = df.loc[(df[split_col]<split_value)==False]
    new_df[1] = df.loc[(df[split_col]<split_value)]
    
    return  new_df[0], new_df[1]
    
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













               