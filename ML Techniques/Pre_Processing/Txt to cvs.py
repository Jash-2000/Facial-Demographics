# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 05:39:07 2020

@author: bhargav Pandya
"""

import pandas as pd

read_file = pd.read_csv (r'E:\Second year\PS-1 - Facial Demographics\data.txt')
read_file.to_csv (r'E:\Second year\PS-1 - Facial Demographics\data.csv', index=None)

df = pd.read_csv('E:\Second year\PS-1 - Facial Demographics\data.csv')
print(df.head())