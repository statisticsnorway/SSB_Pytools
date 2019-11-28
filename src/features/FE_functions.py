#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 09:46:29 2019

@author: ssv
"""

 
import pandas as pd
import numpy as np
import os
import datetime
import time

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

def replace_values(col, value, to_replace = np.nan, df=df):
    '''
    Replaces values in the given columns.
    
    df
    col
    to_replace
    value
    '''
    df[col]=df[col].replace(to_replace, value)
    return df

def coalece_columns(new_col, old_col, coalece_col, df=df):
    '''
    Coaleces a series of collumns into a new column
    
    df
    new_col
    old_col
    coalece_col
    '''
    df[new_col] = df[old_col].combine_first(df[coalece_col])
    return df
    
def create_counter_col(new_col, group_col, counting_col, df=df):
    '''
    Creates a column that counts entries given a grouping column,
    and adds it back to the data frame.
    
    df
    new_col
    group_col
    counting_col
    '''
    a = df.groupby(group_col)[counting_col].count().reset_index()
    a.columns = [group_col, new_col]
    df= pd.merge(df, a, on=group_col, how= 'left')
    return df
    
def get_building_area_divide(new_col, col1, col2, col3, counting_col, df=df):
    '''
    Custom function for getting the building area from other columns.
    '''
    df[new_col] = df[col1].combine_first(df[col2])\
                            .combine_first(df[col3]/df[counting_col])
    return df

def get_building_area_multiply(new_col, col1, col2, col3, counting_col, df=df):
    '''
    Custom function for getting the building area from other columns.
    '''
    df[new_col] = df[col1].combine_first(df[col2]*df[counting_col])\
                            .combine_first(df[col3])
    return df
    
def adjust_extreme_values(total_area, unit_area, counting_col, df=df):
    '''
    Custom function that adjusts the extream values of housing units.
    '''
    
    tot = np.array(df[total_area].values.tolist())
    a = np.array(df[unit_area].values.tolist())
    ant = np.array(df[counting_col].values.tolist())

    #need to add values to config file
    df[unit_area] = np.where((a>tot)&(a<20), a, a).tolist()
    df[unit_area] = np.where((a>tot)&(a>20),tot, a).tolist()

    df[unit_area] = np.where(((a==0.0)|(a>300)|(a>tot)),(tot/ant), a).tolist()

    f = np.array(df[total_area].values.tolist())
    df[total_area] = np.where((f<a)&(f<20),a, f).tolist()
    
    df=df.loc[df[unit_area]< 1000.0]
    return df

def store_unitsize_data(filename, df=df, size_treshold=0.0,PATH=PATH):
    timestamp = time.strftime('%S')
    
    below_treshold=df.loc[df[unit_area]< size_treshold]
    below_treshold.to_csv(PATH+'data/interim/below_treshold'\
                          +filename+timestamp+'.csv')
    above_treshold=df.loc[df[unit_area]< size_treshold]
    above_treshold.to_csv(PATH+'data/interim/above_treshold'\
                          +filename+timestamp+'.csv')