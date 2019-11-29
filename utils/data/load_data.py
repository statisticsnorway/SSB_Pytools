#!/bin/env python3
# -*- coding: utf-8 -*-
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


def load_raw_data (DF_Name, File_name, sep=',', PATH=PATH):
    '''
    Loads the data, sorts the columns alphabetically.
    And sores a copy of the sorted frame in the processed folder, 
    with a timestamp.
    
    :param DF_Name:
    :type DF_Name:
    :param File_name:
    :type File_name
    :param sep:
    :type sep:
    :param PATH:
    :type PATH:
    '''
    timestamp = time.strftime('%S')
    DF_Name = pd.read_csv(PATH+File_name, sep)
    DF_Name = DF_Name.reindex(sorted(DF_Name.columns), axis=1)
    DF_Name.to_csv(PATH+'data/processed/'+DF_Name+timestamp+'.csv')
    print('/nLoaded data: ',File_name, 'as', DF_Name)
    return DF_Name



def store_unitsize_data(filename, df=df, size_treshold=0.0,PATH=PATH):
    timestamp = time.strftime('%S')
    
    below_treshold=df.loc[df[unit_area]< size_treshold]
    below_treshold.to_csv(PATH+'data/interim/below_treshold'\
                          +filename+timestamp+'.csv')
    above_treshold=df.loc[df[unit_area]< size_treshold]
    above_treshold.to_csv(PATH+'data/interim/above_treshold'\
                          +filename+timestamp+'.csv')


    
        
def Parse_text_archive_to_df(file_path, schema, encoding = 'utf-8', null_marker = '.'):
    '''
    A function that takes a position based .txt file and parses into a pandas DataFrame
    
    :param file_path: Location of archive file
    :type file_path: Str
    :param schema: A schema providing the position for the columns. 
    :type schema: Dict, {col_name : [start:stop]} on a index 1 system 
    :param encoding: What encoding system is used on the file
    :type encoding: Str, Optional *Default: utf-8*
    :param null_marker: symbol used to indicate empty column in position file
    :type null_marker: Str, Optional *Default: .*
    '''
    with codecs.open(file_path, 'r', encoding=encoding,
                 errors='ignore') as f:
        archive_text = f.readlines()
     
    d = []
    for entry in archive_text:
        col={}
        for k, v in schema.items():
            rows = (entry[v[0]-1:v[0]+v[1]-1]).strip()
            col.update({k:rows})
         
        d.append(col)
      
    data_df = pd.DataFrame()
    
    for i in d:
        data_df = data_df.append(i,ignore_index=True)
       
    data_df = data_df.replace(null_marker, np.nan)
    
    return data_df