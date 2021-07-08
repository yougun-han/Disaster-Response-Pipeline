# Disaster-Response-Pipeline

## Table of Contents
1. [Description](#Description)
2. [Getting Started](#gettingstarted)
    1. [Software and Libraries](#libraries)
    2. [File Description](#FileDescription)
    3. [Run Program](#RunProgram)
3. [Output(WebApp)](#Output)
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

More informations in requirements.txt which details my python environment at the time of project completion. I have used "python -m pip freeze > requirements.txt" to create the requirement.txt file.

### File Description <a name="FileDescription"></a>
<pre>
- disaster_response_pipeline
|- app
|   |- template
|   |   |- master.html  # main page of web app
|   |   |- go.html      # classification result page of web app
|   |- run.py           # Flask file that runs app
|    
|- data
|   |- DisasterResponse.db          # databased created by running process_data.py
|   |- process_data.py              # python file that processes data and create DisasterResponse.db
|   |- disaster_categories.csv      # data to process by process_data.py
|   |- disaster_messages.csv        # data to process by process_data.py
|
|- classifier
|   |- train_classifier.py          # python file that build models
|   |- trained_classifier.pkl       # model created by train_classifier.py (Not in repo, but will be created upon running train_classifier.py) 
|
|- ETL Pipeline Preparation.ipynb   # Notebook file prior to buiding process_data.py 
|- ML Pipeline Preparation.ipynb    # Notebook file prior to building train_classifier.py
|- README.md
|- requirements.txt
|- LICENSE
</pre>

### Run Program <a name="RunProgram"></a>
- Run ETL pipeline that cleans data and stores in database
 
    `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`

- Run ML pipeline that trains classifier and saves

    `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
- Run Flask Web App
    
    `python run.py`
    
## Output(WebApp) <a name="Output"></a>
