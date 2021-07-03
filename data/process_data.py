import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """load_data fucntion
    
    This function loads disaster message data and disaster categories data and merge them
    
    Args:
        messages_filepath (str): disaster message data path.
        categories_filepath (str): disaster categories data path .

    Returns:
        merged disaster dataframe of messsage data and categories data
    
    """
    # load messages dataset and categories dataset
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # merge datasets
    df = categories.merge(messages, how='inner', on = ["id"])

    return df


def clean_data(df):
    """clean_data fucntion
    
    This function cleans the disaster dataframe
    
    Args:
        df (panda dataframe): disaster dataframe.

    Returns:
        Cleaned disaster dataframe
    
    """
    # create a dataframe of the 36 individual category columns
    categories = df['categories'].str.split(pat=';', expand = True)

    # select the first row of the categories dataframe and extract category names
    row = categories.iloc[0]
    category_colnames = row.apply(lambda x: x[:-2])

    # rename the columns of `categories`
    categories.columns = category_colnames

    # extract category values (0 or 1)
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1]
        categories[column] = pd.to_numeric(categories[column])

    # replace categories column in df with new category columns
    df = df.drop(columns=['categories'])
    df = pd.concat([df,categories],axis=1)

    # remove duplicates
    df = df.drop_duplicates()

    return df


def save_data(df, database_filename):
    """save_data fucntion
    
    This function saves dataframe into database
    
    Args:
        df (panda dataframe): dataframe
        database_filename: database file path
        
    Returns:
        None
    
    """
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql('DisasterResponse', engine, index=False, if_exists = 'replace')

def main():
    """main function
    
    The funtion loads and clean disaster data and save into database
        
    """

    if len(sys.argv) == 4:
        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()