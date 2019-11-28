# -*- coding: utf-8 -*-
#!/usr/bin/env python
'''
Feature Engenering for Imputation of user unit sizes.

'''
import pandas as pd
import numpy as np
import os
import datetime


__author__ = "Simen Svenkerud"
__copyright__ = "Statistics Norway 2019, Seksjon 426"
__credits__ = ['na']

__licence__ = 'n/a'
__version__ = '0.0.3'
__maintainer__ = 'Simen Svenkerud'
__ email__ = 'ssv@ssb.no'
__status__ = 'Development'

%reload_ext autoreload 
%autoreload 2

for k,v in RAW_DATA.items():
    k = load_raw_data(v,k)

bruksenhet_og_bygg = pd.read_csv(PATH+'data/raw/BRUKSENHET_OG_BYGG.csv', sep=';')
uten_fritidsbygg = pd.read_csv(PATH+'data/raw/BRUKSENHET_UTEN_FRIBYGG.csv', sep=';')

df = pd.concat(DATA_TO_CONCATENATE, axis = 0, ignore_index=True)

for k,v in VALUES_TO_REPLACE.items():
    df = replace_values(col=k, value=v)
    df = replace_values(col=k, to_replace= 0.0, value=v)
    
#replace_values(col='ANTALL_BOLIGER', value=1)

for i in AREA_COL:
    replace_values(col=i, to_replace= 0.0, value=np.nan)
    
df = create_counter_col(new_col= ANTALL_FRIBOLIG, 
                   group_col=BYGNINGSNR, 
                   counting_col=BRUKSENHETID)
    
df = get_building_area_divide(BRUKSAREAL, 
                         AREA_COL[0], 
                         AREA_COL[1], 
                         AREA_COL[2], 
                         ANTALL_FRIBOLIG)
df = get_building_area_multiply(BRUKSAREAL_TOTALT, 
                           AREA_COL[2], 
                           AREA_COL[0], 
                           AREA_COL[1], 
                           ANTALL_FRIBOLIG)

for i in [BRUKSAREAL, BRUKSAREAL_TOTALT]:
    df = replace_values(col=i, value=0.0)

df = adjust_extreme_values(total_area = BRUKSAREAL_TOTALT, 
                      unit_area = BRUKSAREAL_TOTALT, 
                      counting_col = ANTALL_FRIBOLIG)

df = df.merge(byggaar[BYGGE_AAR_COL], 
              how = 'inner',
              left_on=BYGGE_AAR_JOIN_COL, 
              right_on=BYGGE_AAR_JOIN_COL)

store_unitsize_data(filename = CLEANED_TRAINING_DATA)

    
