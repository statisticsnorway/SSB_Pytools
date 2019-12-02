#!/usr/bin/env python

import pandas as pd
import numpy as np

from itertools import groupby, chain

import sys
import random
import string
import datetime
from collections import defaultdict

__author__ = "Simen Svenkerud"
__copyright__ = "Statistics Norway 2019, Seksjon 426"
__credits__ = ['na']

__licence__ = 'n/a'
__version__ = 
__maintainer__ = 'Simen Svenkerud'
__ email__ = 'ssv@ssb.no'
__status__ = 'Development'


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