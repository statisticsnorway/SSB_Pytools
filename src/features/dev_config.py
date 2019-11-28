#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:19:46 2019

@author: ssv
"""
{}
[]

PATH = '/ssb/bruker/ssv/jupyter/Fritidsbygg/'

RAW_DATA = {'data/raw/BRUKSENHET_OG_BYGG.csv': 'bruksenhet_og_bygg',
            'data/raw/BYGG_UTEN_BRUKSENHET.csv': 'uten_bruksenhet',
            'data/raw/BRUKSENHET_UTEN_FRIBYGG.csv': 'uten_fritidsbygg',
            'data/raw/FRITIDSBYGG_BRUKSENHET.csv': 'full_liste',
            'data/raw/BYGGEAAR_BYGGA.csv': 'byggaar'
            }

DATA_TO_CONCATENATE = [bruksenhet_og_bygg, uten_bruksenhet]

VALUES_TO_REPLACE = {'ANTALL_BOLIGER':1.0,
                     'ANTALL_ROM':1.0,
                     'ANTALL_ETASJER':1.0,
                     'ANTALL_BAD':1.0
                     }

AREA_COL = ['BRUKSAREAL',
            'BRUKSAREAL_BOLIG',
            'BRUKSAREAL_TOTALT'
            ]

BYGGE_AAR_COL = ['ID', 'byggeaar_ssb', 'opprinnelseskode_ssb']
BYGGE_AAR_JOIN_COL = ['ID']

BRUKSAREAL = 'BRUKSAREAL_SSB'
BRUKSAREAL_TOTALT = 'BRUKSAREAL_TOTALT_SSB'
ANTALL_FRIBOLIG = 'ANTALL_FRIBOLIG'
BYGNINGSNR='BYGNINGSNR'
BRUKSENHETID = 'bruksenhetid'

CLEANED_TRAINING_DATA = 'Fritidsbolig_trening'