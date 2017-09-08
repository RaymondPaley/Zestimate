# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 10:46:20 2017

@author: Neel Tiruviluamala
"""

import os
import pandas as pd

base_path = "C:/Users/Neel Tiruviluamala/Desktop/Zillow" #Set your basepath to be the Zillow folder
data_path = base_path + os.sep + 'Data' + os.sep

properties_2016 = pd.read_csv(data_path + 'properties_2016.csv')