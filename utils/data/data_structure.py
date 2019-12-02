#!/usr/bin/env python

import pandas as pd
import numpy as np

__author__ = "Simen Svenkerud"
__copyright__ = "Statistics Norway 2019, Seksjon 426"
__credits__ = ['na']

__licence__ = 'n/a'
__version__ = 
__maintainer__ = 'Simen Svenkerud'
__ email__ = 'ssv@ssb.no'
__status__ = 'Development'



def join_df_2_one(old_dfs, join_on):
    '''
    Function that coins a list of Data Frames to a singel frame
    
    Takes a list of dataframes and kombines them into a singel dataframe, 
    given they share a joining key.
    The join is perfored using a standard left outer join
    

    :param old_dfs: List of 2 dataframes to be merged
    :type old_dfs: list, dataframes
    :param join_on: join key for the join process
    :type join_on: Str
    
    '''
    new_df = old_dfs[0]
    for i in old_dfs[1:]:
        new_df = pd.merge(new_df, i, on=join_on)

    return new_df

def seperate_by_value(df, split_col, split_value, new_df):
    '''
    Split a Data frame in two by a value
    
    :param df: The dataframe to perform the split on
    :type df: DataFrame
    :param split_col: The name of the column to use as split basis
    :type split_col: Str, Column name
    :param split_value: The treshold for the split
    :type split_value: Int or Float
    :param new_df: list of new empty DataFrames
    :type new_df: list
    '''
    new_df[0] = df.loc[(df[split_col]<split_value)==False]
    new_df[1] = df.loc[(df[split_col]<split_value)]
    
    return  new_df[0], new_df[1]


def groupby_count(i, key=None, force_keys=None):
    """
    Example::
        [1,1,1,2,3] -> [(1,3),(2,1),(3,1)]
    """
    counter = defaultdict(lambda: 0)
    if not key:
        key = lambda o: o

    for k in i:
        counter[key(k)] += 1

    if force_keys:
        for k in force_keys:
            counter[k] += 0

    return counter.items()


def groupby_dict(i, keyfunc=None):
    return dict((k, list(v)) for k,v in groupby(sorted(i, key=keyfunc), keyfunc))
