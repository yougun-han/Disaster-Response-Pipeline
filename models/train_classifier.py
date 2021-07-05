# import libraries
import sys
import numpy as np
import pandas as pd
from sqlalchemy import  create_engine, inspect

import re
import nltk
nltk.download(['punkt','wordnet','stopwords','averaged_perceptron_tagger'])

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report 
from sklearn.model_selection import GridSearchCV
import pickle

def load_data(database_filepath):
    """load_data fucntion
    
    This function loads disaster data from SQL database
    
    Args:
        database_filepath (str): filepath of disaster database.

    Returns:
        X (table) : disaster massage table
        Y (table) : disaster category table
        category_names (array) : list of category names
    """

    # Assess database and extract DisasterResponse table
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql(
        "SELECT * FROM DisasterResponse",
        con=engine
    )

    # Extract X, Y, Categories from the table
    X = df["message"]
    Y = df.drop(columns=["id", "message", "original", "genre"]).astype('bool')
    category_names = Y.columns.values

    return X, Y, category_names


def tokenize(text):
    """tokenize fucntion
    
    This function tokenize test
    
    Args:
        text (str): test message

    Returns:
        clean_tokens (list) : list of cleaned tokens
    """

    #remove non-text/numbers from text and normalize 
    text = re.sub(r'[^a-zA-Z0-9]',' ',text.lower())
    
    # tokenize and remove stop words
    words = word_tokenize(text)
    tokens = [w for w in words if w not in stopwords.words("english")]
    
    # lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).strip()
        clean_tokens.append(clean_tok)
    
    return clean_tokens 


def build_model():  
    """build_model fucntion
    This function defines a ML model

    Returns:
        clean_tokens (list) : list of cleaned tokens
    """ 
    #define ML pipeline
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer = tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
        ])

    return pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    """evaluate_model fucntion
    
    This prints out the performance of model using test data
    
    Args:
        model : trained model
        X_test : test data 
        Y_test : test data
        category_names : list of categories

    Returns:
        None
    """
    # forcast using model and print out performance
    y_pred = model.predict(X_test)
    print(classification_report(Y_test, y_pred, target_names=category_names))
    return None


def save_model(model, model_filepath):
    """save_model fucntion
    
    This save the model into pickle file
    
    Args:
        model : trained model
        model_filepath : filename for trained model

    Returns:
        None
    """
    pickle.dump(model, open(model_filepath, 'wb'))
    return None


def main():
    """main function
    
    The funtion does followings
        - Read the disaster table from database
        - Build, train, evaluate, and save the model
        
    """
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()