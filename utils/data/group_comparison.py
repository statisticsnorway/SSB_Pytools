#!/usr/bin/env python

import pandas as pd
import numpy as np

def GroupComparison(df, group_col, label_1, label_2):
    '''
    Function for checking for grouped identifiers
    
    given a grouping vlaue this function will investigate 
    if there is a idenfying label. All values with this
    identifying label  are given the same value in label_1.
    
    :param df: DataFrame  to perform comparison
    :type df: DataFrame
    :param group_col: the column containing the grouping column
    :type group_col: str
    :param label_1: column containing value to be transfered to the entire group
    :type label_1: str
    :param label_2: Column containing the subgroup identifying labels
    :type label_2: str
    '''
    d=df
    d[label_1+"_new"] = d[label_1]
    # grouping by group_col and label2 will identify groups to be assigned label1_new values.
    g = d.groupby(by=[group_col, label_2])
    for key, df_grp in g:
        label1_new = df_grp.iloc[0,2]

        #I didn't understand how to use the Pandas group to update in place.
        #Therefore I made a copy to hold new label1_new values.
        #Then updated the original data frame.
        cp = df_grp.copy()
        cp[label_1+"_new"] = label1_new
        d.update(cp)
    return d