#!/usr/bin/env python # coding: utf-8 
import pandas as pd
import numpy as np
import time

def ColumnComparison (data_set1, data_set2, output ='yes', log = None):
    '''
    Function to compare the columns in two data setts
    '''
    a = set(data_set1.columns)
    b = set(data_set2.columns)
    timestr = time.strftime("%Y%m%d")
    
    if output == 'yes':
        print('These Datasets have the following common columns:')
        for elem in (a & b):
            print('* ', elem)
        print('These columns exist only in the first dataset:')
        for elem in (a-b):
            print('* ', elem)
        print('These columns exist only in the second datasett:')
        for elem in (b - a):
            print('* ', elem)
    elif output == 'no':
        print('No output printed to screen')
    
    if log != None:
        with open(log+timestr+'.log', 'w') as f:
            f.write('** Column comparison betweeen**')
            if (a&b):
                f.write('\n\nThese Datasets have the following common columns:')
                for elem in (a & b):
                    f.write('\n* %s' % elem)
            if (a-b):
                f.write('\n\nThese columns exist only in the first dataset:')
                for elem in (a-b):
                    f.write('\n* %s' % elem)
            if (b-a):
                f.write('\n\nThese columns exist only in the second datasett:')
                for elem in (b - a):
                    f.write('\n* %s'% elem)
    elif log == None:
        print('No Log created')

    return

def correctionDetection(start_data, comparison_data,output='yes', log=None):
    
    if start_data.equals(comparison_data)==True:
        print('No differneces detected, data considderes equal')
    elif start_data.equals(comparison_data)==False:
        print('Differences detected')
        diff = start_data != comparison_data
        for col in comparison_data.columns:
            changes = comparison_data.loc[diff[col]]
            original = start_data.loc[diff[col]]
            if output == 'yes':
                if len(changes) > 0:
                    print('Column ',str(col),' is changed!')
                    print(len(changes),' Changes detected')
                    for i in changes.reset_index().index:
                        print('\nChange nr: ',i+1)
                        print('Changes: ',changes.iloc[[i]].to_string(header=False))
                        print('Original: ',original.iloc[[i]].to_string(header=False))
            if output == 'no':
                print('No detaild output printed to screen')
        
        
    if log != None:
        timestr = time.strftime("%Y%m%d")
        with open(log+timestr+'.log', 'w') as f:
            if start_data.equals(comparison_data)==True:
                f.write('\n\nNo differneces detected, data considderes equal')
            elif start_data.equals(comparison_data)==False:
                f.write('\n\nDifferences detected')
                diff = start_data != comparison_data
                for col in comparison_data.columns:
                    changes = comparison_data.loc[diff[col]]
                    original = start_data.loc[diff[col]]

                    if len(changes) > 0:

                        f.write('\n\nColumn %s is changed!' % str(col))
                        f.write('\n%s Changes detected' % len(changes),)
                        for i in changes.reset_index().index:
                            f.write('\n\nChange nr: %s' % str(i+1))
                            f.write('\nChanges: %s' % changes.iloc[[i]].to_string(header=False))
                            f.write('\nOriginal: %s' % original.iloc[[i]].to_string(header=False))