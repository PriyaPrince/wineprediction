import pandas as pd
import numpy as np

from sklearn import pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer 
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import dill as pickle
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import cross_val_predict
from defs import log_transform
import joblib

df = pd.read_csv("wine_train.csv")

def quality_finder(row):
    
    if (row.quality == 8 or row.quality == 6 or row.quality == 7):
        return 1
    elif(row.quality == 3 or row.quality == 4 or row.quality == 5):
        return 0
    
df['quality'] = df.apply(quality_finder,axis = 1)

X = df.drop(['density','free sulfur dioxide','quality','Id'],axis = 1)
y = df.loc[:,'quality']

clog = ColumnTransformer(transformers =[('clog', FunctionTransformer(log_transform),[2,3,4,5,8])],remainder ='passthrough')
x2 = clog.fit_transform(X)

 
cnull = ColumnTransformer(transformers =[
    ('cat', SimpleImputer(strategy ='median'), list(range(9)))])  
x1 = cnull.fit_transform(X)    



scale =  ColumnTransformer(transformers =[('scale',StandardScaler(),list(range(9)))])
x4 = scale.fit_transform(X)


winepipe = pipeline.Pipeline([('cnull',cnull),('clog',clog),('scale', scale),('model',RandomForestClassifier(n_estimators= 400,min_samples_leaf= 1,max_features= 'sqrt',max_depth= None,criterion= 'gini',bootstrap= True))])

winepipe.fit(X,y)

joblib.dump(winepipe,'WineModelPickle.sav')

ypred = winepipe.predict([[10.3,0.32,0.45,6.4,0.073,13,3.23,0.83,12.6]])  #1 Good

ypred1 = winepipe.predict([[7.3,0.98,0.05,2.1,0.061,49,3.31,0.55,9.7]]) #0  Bad

ypred1 = winepipe.predict([[7.3,0.05,2.1,0.061,49,3.31,0.55,9.7]]) # Error




ypredc = cross_val_predict(winepipe, X, y,cv=10)









