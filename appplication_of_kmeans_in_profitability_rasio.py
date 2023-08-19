# -*- coding: utf-8 -*-
"""Appplication of KMeans in Profitability Rasio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IC8UgIjvK62hBd5u7uXNfzlSqtJa3Go7
"""

#  APPLICATION OF K-MEANS IN PYTHON
#--------------------------------------
#   "Data Rasio Kinerja Keuangan"

#Edited by: Mutia Yollanda & Muhardiansyah
#4th Meeting
#Tuesday, November 8th 2022
#Introduction of Artificial Intelligence

#Reading data
import pandas as pd
# import files
from google.colab import files
uploaded = files.upload()

mydata=pd.read_excel("Data Rasio Kinerja Keuangan.xlsx")
mydata

mydata.iloc[40]

#Import Library/Package
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

import plotly as py
import plotly.graph_objs as go

from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings('ignore')

plt.figure(1 , figsize = (20 , 12))
n = 0 
for x in ['EPS', 'PER', 'DER', 'ROA', 'ROE','NPM']:
    n += 1
    plt.subplot(2 , 3 , n)
    plt.subplots_adjust(hspace = 0.5 , wspace = 0.5)
    sns.distplot(mydata[x] , bins = 15)
    plt.title('Distplot of {}'.format(x))
plt.show()

mydataolah=mydata.loc[:,'EPS':'NPM']
mydataolah

# Data Scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(mydataolah)
scaled = scaler.transform(mydataolah) #in array
scaled

#Transform "scaling_value" to DataFrame
df_scaled = pd.DataFrame(scaled, columns=['EPS', 'PER', 'DER', 'ROA', 'ROE','NPM'])
df_scaled

# K-Means
from sklearn.cluster import KMeans

km = KMeans(n_clusters=3) 
y_predicted = km.fit_predict(df_scaled[['EPS', 'PER', 'DER', 'ROA', 'ROE','NPM']])

#Add new column "tipePenghasilan" in mydata
mydata['Kluster'] = y_predicted
y_predicted

import plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter3d(
    x= mydata['EPS'],
    y= mydata['PER'],
    z= mydata['ROE'],
    mode='markers',
     marker=dict(
        color = mydata['Kluster'], 
        size= 6,
        line=dict(
            color= mydata['Kluster'],
            width= 12
        ),
        opacity=0.8
     )
)
data = [trace1]
layout = go.Layout(
    title= 'Clusters EPS, PER, DER, ROA, ROE,NPM',
    scene = dict(
            xaxis = dict(title  = 'EPS'),
            yaxis = dict(title  = 'PER'),
            zaxis = dict(title  = 'ROA')
        )
)
fig = go.Figure(data=data, layout=layout)
py.offline.iplot(fig)

conditions = [
    (mydata['Kluster']==0),
    (mydata['Kluster']==1),
    (mydata['Kluster']==2)]
choices = ['Kluster 1','Kluster 2','Kluster 3']
mydata['Kluster'] = np.select(conditions, choices)
mydata