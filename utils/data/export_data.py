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

def create_statbank_tables_complex(df, groupings_name, counter_col, math_func, path):
    '''
    Creates and exports tables that need unstacking ready to be uploaded to Statestikkbanken
    '''
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
        
def create_statbank_tables_simple(df, groupings_name, counter_col, math_func, path):
    '''
    Creates and exports tables ready to be uploaded to Statestikkbanken
    '''
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