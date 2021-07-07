# Disaster-Response-Pipeline

## Table of Contents
1. [Description](#Description)
2. [Getting Started](#gettingstarted)
    1. [Software and Libraries](#libraries)
    2. [](#)
    3. Executing Program
    4. Additional Material
3. Authors
4. License
5. Acknowledgement
6. Screenshots

## Description <a name="Description"></a>
This project is completed as a part of Udacity Data Scientist Nanodegree Program.

The goal of the project is to build an application that classifies disaster messages. The project consists of three parts:

- ETL Pipeline
    - Load and merge two raw disaster datasets (messages and classification categories)
    - Clean data and store it in a SQLite database
- ML Pipeline
    - Load data from the SQLite database
    - Splits data into training and test sets
    - Build, train, evaluate ML model 
    - Export the final models as a pickle file
- Flask Web App
    - Load data from the SQLite database
    - Load the trained the model 
    - Run an application that visualises database data and classfies a new meesage into multiple disaster categories.

## Getting Started <a name="gettingstarted"></a>
### Software and Libraries<a name="libraries"></a>
Python 3.8.3 is used for the project with following libraries
- pandas
- sqlalchemy
- numpy
- re
- nltk
- sklearn
- pickle
- plotly
- flask
