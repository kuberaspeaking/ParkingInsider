#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:55:45 2017

@author: abdulliaqat
"""

import pandas as pd
import numpy as np

import os


cwd = os.getcwd()

file_path = os.path.abspath(cwd+"/../data_cleaned.csv")

data2 = pd.read_csv(file_path)


data = data2[data2.columns[[1,2,3,6,7,8]]]


from sklearn.cluster import KMeans


### Find out the false parking point
#cluster = [3,4,5,6,7,8,9,10]
cluster = [3,4,5]
inertia = []
centers = []    
for n in cluster:
    k = KMeans(n_clusters = n, random_state = 5).fit(data["duration(s)"].reshape(-1,1))
    inertia.append(k.inertia_)
    centers.append(k.cluster_centers_)


### 3 Cluster centere is the knee area

center = centers[2]

cluster = KMeans(n_clusters = 2,).fit(data["duration(s)"].reshape(-1,1))

data["combined_original"] = data.apply(lambda x:str(x[0])+str(x[1]))

