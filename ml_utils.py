
import lightgbm as lgb
import logging
import os
from dotenv import load_dotenv
import pickle

# Load the environment variables from the .env file
load_dotenv()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_ranking_model():
    try:
        model_path = os.getenv('MODEL_PATH')
        if model_path is None:
            logging.error("MODEL_PATH environment variable is not set.")
            return None
        #model = lgb.Booster(model_file=model_path)
        


        # Load the model using pickle
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        logging.info("Model loaded successfully.")
        return model
    except Exception as e:
        logging.error(f"An error occurred while loading the model: {e}")
        return None
    
import pandas as pd
from pandas import json_normalize

def json_to_df(data):
    """
    Convert JSON data to a pandas DataFrame, handling nested structures.

    Parameters:
    data (str or list of dicts): JSON data in string or list of dictionaries format.

    Returns:
    DataFrame: A pandas DataFrame.
    """
    try:
        # Convert JSON string to DataFrame
        df = pd.DataFrame(data)
        logging.info("JSON converted to DataFrame successfully.")
        return df
    except Exception as e:
        logging.warning(f"Error converting JSON to DataFrame: {e}")
        return None

def make_recommendation(data):
    model = load_ranking_model()
    if model is None:
        logging.error("Failed to load model.")
        return None
    
    df = json_to_df(data)
    if df is None:
        logging.error("Failed to convert data to DataFrame.")
        return None

    try:
        df['predictions'] = model.predict(df[model.feature_name()])
        df = df.sort_values(['predictions'], ascending=False, ignore_index=True)
        number_of_recommendations = int(os.getenv('NUMBER_OF_RECOMMENDATIONS'))
        recommendations = df.head(number_of_recommendations)['category'].to_list()
        return recommendations
    except Exception as e:
        logging.error(f"Error making recommendations: {e}")
        return None
