# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 21:11:32 2021

@author: Tommy
"""
#%%
###Set-up
import os
from os import path
import sys


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%

#Set up files paths

proj_dir = os.path.abspath(os.path.join(os.path.dirname('abundance_stoolsubset.csv'), os.pardir,))
sys.path.append(proj_dir)

#%%

#Load the data

data = pd.read_csv(path.join(proj_dir,'Analysis', 'data', 'abundance_stoolsubset.csv'))

data.head()

print(data.shape)

print(data.info)

#%%

#Get the IBD subset

ibd = data[data["dataset_name"]=='metahit']

#%% Explore IBD

print(ibd.shape)

ibd.head()

#%%Set up data for classification of disease

ibd.disease.unique()

ibd.loc[:,'disease'] = ibd.disease.map({'n':0, 'ibd_ulcerative_colitis':1, 'ibd_crohn_disease':1}) #Map no diesease to 0 and all others to 1

#%% Cleaning up the data, eliminate nuisance variables

ibd.loc[:, (ibd != 0).any(axis=0)] #Eliminate bacteria that are 0 in all rows.

ibd = ibd.loc[:, (ibd != 0).any(axis=0)]
#%% Set up Random Forest

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 500, max_depth=None, min_samples_split=2, random_state=5523)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(ibd.iloc[:,211:], ibd['disease'] #211 is where the bacteria start
                                                    ,test_size=0.20, random_state=5523)

rf.fit(X_train, y_train)

from sklearn import metrics

rf_pred = rf.predict(X_test)

fpr, tpr, thresholds = metrics.roc_curve(y_test, rf_pred, pos_label=1)

metrics.auc(fpr, tpr)

#%% Naive Bayes

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

gnb_pred = gnb.fit(X_train, y_train).predict(X_test)

gnb_pred

#%% Neural Net

from sklearn.neural_network import MLPClassifier

NN = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=5523)

NN.fit(X_train, y_train)

NN.predict(X_test)

NN_pred = NN.fit(X_train, y_train).predict(X_test)







