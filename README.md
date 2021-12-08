
# Adult Census Income Prediction

## Overview

The prominent inequality of wealth and income is a huge concern especially in the United States. The likelihood of diminishing poverty is one valid reason to reduce the world's surging level of economic inequality. The principle of universal moral equality ensures sustainable development and improves the economic stability of a nation. Governments in different countries have been trying their best to address this problem and provide an optimal solution. This study aims to show the usage of machine learning and data mining techniques in providing a solution to the income equality problem. The UCI Adult Dataset has been used for the purpose. Classification has been done to predict whether a person's yearly income in US falls in the income category of either greater than 50K Dollars or less equal to 50K Dollars category based on a certain set of attributes.

This application goal is to predict whether a person has an income of more than 50K a year or not.
This is basically a binary classification problem where a person is classified into the >50K group or <=50K group.

### Approach

#### Data Collection
I have dataset of 32562 rows which includes all the parameters required to predict the income. The data is available in a CSV file format and it’s collected from the link as per provided in the project description

#### Data Insertion into Database
a.	Database Creation and connection - Create a database with Cassandra cloud version and connect to the database.

b.	Insert the user input in data base and store it database is work as a hidden
API in entire project.  

#### Export Data from Database
Take the user input and store in Cassandra database.

#### Data Cleaning
In order to fit the data to the model I need to identify incomplete, incorrect, inaccurate or irrelevant parts of the data and then replacing, modifying, or deleting the dirty or coarse data

#### Feature Engineering
In this section I try to take care of validating or replacing values with other values in the dataset. Additionally, I also take care of converting the categorical columns to numerical columns by one hot encoding and apply label encoding on label data.

#### Sampling
Here dataset is unbalanced so I try random oversampling to balance the data.

#### Model Building
After the completion of the above process I split the dataset into test and train. I use various classification algorithm like Decision trees, Random Forest, K-NN, Bagging, XgBoost, ExtraTree classifier and validate the accuracy. Finally I select the best algorithm and check the accuracy on train and test data. I used the metrics which validates the variance from model prediction to ground truth.

#### Hyperparameter Tuning
Here I have used Randomized Search CV for selection of the best parameters to reduce overfitting criteria. Along with this I have used k fold cross validation technique for training of the model and finally got 84% accuracy.

#### Model Dump with pkl file
I have saved the model using pickle.

#### Creation of front end
As per the required parameters for the user to predict the income I have created the front end in order to link with the Flask App. Here the styling and formatting of the html page is taken care with the CSS file.

#### Flask Web App
I have created a Flask Web App where I read the contents from the pickle file and made sure it linked to the html file to predict the income.

#### Dockerize
I have used dockerize technique here which helps the application to run within a docker container. It is useful to take care of the environmental variables and helps the app to run in all the platforms.

#### Deployment
I have deployed the app on Heroku platform but I have prepared a deck to help user in order to deploy on other platforms as well.

## Tools

Python, Amazon EC2, Cassandra, Flask, Html, CSS, Docker, Vscode






## Heroku

https://income-predictions.herokuapp.com/

## Docker

https://hub.docker.com/repository/docker/sonupal/inr_api




## Documentation

[HLD](https://github.com/sonupal77/income-prediction/blob/main/HLD.pdf)

[LLD](https://github.com/sonupal77/income-prediction/blob/main/LLD.pdf)

[Architecture](https://github.com/sonupal77/income-prediction/blob/main/Architecture.pdf)

[Wireframe](https://github.com/sonupal77/income-prediction/blob/main/Wireframe.pdf)

## Bug / Feature Request

If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue]

