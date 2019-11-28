#!/usr/bin/env python

import pandas as pd
import numpy as np

__author__ = "Simen Svenkerud"
__copyright__ = "Statistics Norway 2019, Seksjon 426"
__credits__ = ['na']

__licence__ = 'n/a'
__version__ = '
__maintainer__ = 'Simen Svenkerud'
__ email__ = 'ssv@ssb.no'
__status__ = 'Development'

def set_min_value(df, col, min_value):
    '''
    Function to copy a column, but setting a floor for the possible values
    
    This function takes the given input column and makes a copy.
    This copy is then checked if it is belov a given treshold. 
    If the value is belov a treshold, it replaces the value with the treshold set.
    
    :param df: The Dataframe to perform this function on 
    :type df: Data frame
    :param col: The column to impse floor on
    :type col: Numerical array
    :param min_value: Lowest possible value treshold
    :type min_value: Int or float
    :return: A copy of input dataframe with new column
    :rtype: Data frame
    '''
    for col in col:
        df[col+'_adj'] = df[col].where(df[col]>min_value, min_value)
        
    return df


def Collect_value_from_prioritised_3variables(df,prioritised_col,new_col, treshold_value, math_index = None, math_col= None, mathtype= None):
    '''
    A function to collect a value form a prioritised list of three variables
    
    This function was created for a spessifik task, possibly not sufficently generalized.
    Given you have a prioritised list of 3 columns this function will collect the value from he first value found.
    It functuions simmilarly to coalece in SQL. 
    However it also performs a multiplication or division with one of the prioritised columns.
    Was originally created for fritidsbolig statistikken.
    
    :param df: DataFram to perform function on
    :type df: DataFrame
    :param prioritised_col: These are the columns in prioritised order that contain the values to look for 
    :type prioritised_col: List of column names
    :param new_col: Name of the resulting column
    :type new_col: string
    :param treshold_value: Lower treshold for possible values
    :type treshold_value: int or float
    :param math_index: the index position within the prioritised_col that is to be multiplied or divided
    :type math_index: Int
    :param math_col: The name of the collum to be used as counter part in the calculation
    :type math_col: Str
    :param mathtype: div or mult
    :type mathtype: Str
    :return: Returns Copy of Dataframe with additional column
    :rtype: DataFrame
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
    '''
    Adds a counter column based on a given grouping variable to a DataFrame
    
    :param df: DataFrame to perform calculation on
    :type df: DataFrame
    :param grouping_col: The name of the column to use as grouping variable in counting
    :type grouping_col: Str, column name 
    :param counting_col: The name of the column to count
    :type counting_col: Str, columnname
    :param new_col_name: The name of the new counting column
    :type new_col_name: Str, columnname
    :return: A copy of the dataframe with a counting column attached
    :rtypes: DataFrame
    '''
    counter = df.groupby(grouping_col)[counting_col].count().reset_index()
    counter.columns = [grouping_col, new_col_name]
    df = pd.merge(df, counter, on=grouping_col, how ='left')
    
    return df

def conditional_area_adjustments(df, unit_area, total_area, counter_col, min_treshold=1, max_treshold=1000):
    '''
    Adjust value in col a, to make sure it is not greater than col b
    
    This is a highly custom function buildt for "fritidsbolig statistikken" 
    it aims to make sure that unit size i not larger than total size,
    and that in the case of missing unit size we can take a proportion of 
    the total area, instead. 
    *This should possibly be improoved upon later*
    
    :param df:
    :type df:
    :param unit_area:
    :type unit_area:
    :param total_area:
    :type total_area:
    :param counter_col:
    :type counter_col: 
    :param min_treshold:
    :type min_treshold:
    :param max_treshold:
    :type max_treshold:
    :return:
    :rtype:
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











               