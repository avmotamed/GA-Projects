# GA Capstone Project - Predicting User Click Through

The goal of this project was to try to predict what recommended content a user would select. The data was provided by Outbrain via this [Kaggle competition](https://www.kaggle.com/c/outbrain-click-prediction) that aimed to improve the recommendation engine.

The analysis is split into six notebooks:
  •	Book 1: Data cleaning
  •	Book 2: Exploratory Data Analysis (EDA)
  •	Books 3 – 6: Modeling and analysis
    o	Random Forest
    o	Logistic Regression
    o	Gradient Boost
    o	Decision Tree

The original competition was very data intensive, so as a proof of concept that I could run locally, a small subset of data was used (10,000 clicks out of 17 million).

Using local resources, I could predict the correct selection 39% of the time versus a baseline of 19%. The next step is to move onto larger platforms (e.g. AWS) to run larger sets of data and to add the use of behavioral profiles based off a larger data set of user browsing histories.
