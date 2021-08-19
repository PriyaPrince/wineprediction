# Wine Quality Prediction
# Data Analysis and Machine Learning Project


## Project Overview
The aim of this project is to predict the quality of wine on the basis of its chemical composition. Wine quality dataset taken from Kaggle has been used to do the analysis to find out the impact of the chemical attributes in deciding  the quality of wine and to build various classification models to predict the wine is of good quality or not. 
Each wine data in this dataset is given a quality score ranging from 3 to 9. As part of analysis I converted the dependent variable into a binary type where each wine is either good quality(a score of 6 or higer) or not (a score below 6).
## Summary of Dataset 
Input variables:
1 - Fixed acidity
2 - Volatile acidity
3 - Citric acid
4 - Residual sugar
5 - Chlorides
6 - Free sulfur dioxide
7 - Total sulfur dioxide
8 - Density
9 - PH
10 - Sulphates
11 - Alcohol 

Output variable 
Quality of wine (Score between 2 and 9)

## Understanding Data
The dataset looks very clean with 1143 rows , 12 features and no missing values.
## Preprocessing
As mentioned earlier, the quality attribute has been regrouped into 0 and 1, representing bad and good respectively. Map function is used assign new labels to the attribute.
## Feature Selection
As we can see, density, pH,free sulphar dioxide attributes do not have any impact on the qulaity. Though removing only density and free suphar dioxide considering extratree regressor and partial correlation results.

<img width="940" alt="p1" src="https://user-images.githubusercontent.com/82373435/130103992-62f7f019-eb82-4c23-a1af-8c7434fdab42.png">






## Exploratory Data Analysis
Detailed EDA of the dataset is given [here](/WineQualityPrediction.ipynb)
The below bar plot shows count of data which is good or bad. It is clear that 55% of the data is classified with bad wine quality and 45 % is classified with good quality.




This bar plot shows a directly proportional relation between volatile acidity and quality. As the quality of wine increases the value of volatile acidity also increases which shows that volatile acidity is an important feature on which quality of wine depends.





Citric acid is another important feature which is greatly contributing to the quality of wine.

## Model Creation and Pipelining
Algorithms used for model creation and classification.

RandomForest Classifier
XGBoost Classifier
Support Vector Machine
K- Nearest Neighbour
Hyper parameter tuning of the parameters is done using GridSearchCV and RandomozedSearchCV for finding out the optimal accuracy.
RandomForest Classifer showed comparitively greater Cross validation Score - 74%
Pipeline of the ML model created(Algorithm used - RandomForest Classifer )

## Model Deployment 
Deployment of the model is done using Python DJANGO Framework.The same is deployed in Heroku.
Heroku Link to launch predictor :-  https://wineprediction012.herokuapp.com/

## Conclusion 










