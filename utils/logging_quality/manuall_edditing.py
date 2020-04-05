#!/usr/bin/env python # coding: utf-8 
import pandas as pd
import numpy as np
import time


def manualEdditing(df, id_column):
    user = input('Enter username')
    n_changes = input('How many changes do you want to make?:')
    change = 1
    change_log = {}
    while change <= int(n_changes):
        timestr = time.strftime("%Y%m%d%H%M%S")
        print('Change nr: ',change)
        col = input('Enter what column you want to change:')
        row_identifier = input('Enter row identificator for the value you want to change:')
        
        Reason = input('Enter reason for change:')
        change = change+1
        original = df.loc[df[id_column]==row_identifier, col]
        if len(original)>0:
            print(original)
        else:
            print('No value found, retry')
            break
            
        eddit = input('is this the value you want to change? y/n:')
        
        if eddit == 'y':
            new_value = input('Enter the new value:')
            df.loc[df[id_column]==row_identifier, col] = new_value
            print(df.loc[df[id_column]==row_identifier, col])
            c = [id_column, row_identifier, col, [str(original)], [new_value], Reason ]
            change_log[user+timestr]= c
        
        elif eddit == 'n':
            print('Pleas rerun funktion to restart edditing process')
            break
    return df, change_log