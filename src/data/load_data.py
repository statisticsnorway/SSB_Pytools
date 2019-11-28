#!/bin/env python3
# -*- coding: utf-8 -*-

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