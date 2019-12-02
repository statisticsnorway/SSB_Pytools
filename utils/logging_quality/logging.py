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