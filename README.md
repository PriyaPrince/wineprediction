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
![p3](https://user-images.githubusercontent.com/82373435/130211568-92f0ae6e-d6c6-4c3d-867f-db3edfba2953.jpg)
## Exploratory Data Analysis
**Detailed EDA of the dataset is given [here]**(/WineQualityPrediction.ipynb)  

The below bar plot shows count of data which is good or bad.  It is clear that 55% of the data is classified with bad wine quality and 45 % is classified with good quality.  
<img width="257" alt="p4" src="https://user-images.githubusercontent.com/82373435/130212186-a2d0b53b-e2d1-47b5-a467-9ac164105d12.png">  
This bar plot shows an inversely proportional relation between volatile acidity and quality. As the quality of wine increases the value of volatile acidity decreases which shows that volatile acidity is an important feature on which quality of wine depends.
![image](https://user-images.githubusercontent.com/82373435/130212950-79167a8c-6f3a-4e30-830d-3ad803eb0b40.png)  
Citric acid is another important feature which is greatly contributing to the quality of wine.

## Model Creation and Pipelining
Algorithms used for model creation and classification.

RandomForest Classifier  
XGBoost Classifier  
Support Vector Machine  
K- Nearest Neighbour  
Hyper parameter tuning of the parameters is done using GridSearchCV and RandomozedSearchCV for finding out the optimal accuracy.
RandomForest Classifer showed comparitively greater Cross validation Score - 74%. 
Pipeline of the ML model created(Algorithm used - RandomForest Classifer )

## Model Deployment 
Deployment of the model is done using Python DJANGO Framework.The same is deployed in Heroku.  
Heroku Link to launch predictor :-  https://wineprediction012.herokuapp.com/

## Future Scope 
 In recent years, interest has increased in the wine industry, which is demanding growth in this market. The companies are also investing in new technology to increase wine quality and sales. Wine quality certification plays a significant role in all processes in this direction, and it needs human experts to test wine.An automatic predictive system can be integrated to enhance the speed and quality of the process.Furthermore, a feature selection process can help to analyze the impact of the various analytical
tests.
  
In the future, broad data set may be used for experiments and other machine learning techniques may be explored for prediction of wine quality, and can expand this analysis to include feature development methods to test whether or not the model's predictive power may be increased.











