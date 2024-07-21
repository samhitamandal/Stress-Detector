# Stress-Detector
This is a stress detector application which uses various lifestyle and physiological data to predict stress levels of an individual.
I used the Kaggle dataset: https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset for this project. 
It is a stress level predictor application which takes parameters such as age,gender,occupation,sleep duration,sleep quality,physical activity level,BMI Category,daily steps and blood pressure to make the prediction.
I have used streamlit to make it into an application. The code ffor the same is in the stress_detector.py file in this repository.
The original data had values of stress level ranging from 0 to 10 which i divided into 3 categories of low, medium and high stress levels. 
I used 4 classification models to find the best fit.The models are: XGBoost,Random Forest, K Nearest Neighbours and Decision Tree Classifier. The models had the following accuracies on train and test data respectively:
1.XGBoost: 99.107 and 98.667
2.Random Forest: 96.42 and 98.00
3.K Nearest Neighbours: 94.19 and 96.667
4.Decision Tree Classifier: 97.76 and 93.33

In conclusion I used XGBoost because of its high accuracy to best fit the model.
