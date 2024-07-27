import pytest
from dotenv import load_dotenv
import numpy as np
import string
import os
from ml_utils import load_ranking_model, make_recommendation, json_to_df

load_dotenv()

n_rows = 100
data = {
    'all_session_actions_feature': np.random.uniform(0, 1, n_rows).tolist(),
    'all_session_actions_feature_lag_1': np.random.uniform(0, 1, n_rows).tolist(),
    'all_session_actions_feature_lag_1_rolling_3_mean': np.random.uniform(0, 1, n_rows).tolist(),
    'session_page_views_feature': np.random.uniform(0, 1, n_rows).tolist(),
    'session_page_views_feature_lag_1': np.random.uniform(0, 1, n_rows).tolist(),
    'session_page_views_feature_lag_1_rolling_3_mean': np.random.uniform(0, 1, n_rows).tolist(),
    'session_success_feature': np.random.uniform(0, 1, n_rows).tolist(),
    'session_success_feature_lag_1': np.random.uniform(0, 1, n_rows).tolist(),
    'session_success_feature_lag_1_rolling_3_mean': np.random.uniform(0, 1, n_rows).tolist(),
    'session_cart_feature': np.random.uniform(0, 1, n_rows).tolist(),
    'session_cart_feature_lag_1': np.random.uniform(0, 1, n_rows).tolist(),
    'session_cart_feature_lag_1_rolling_3_mean': np.random.uniform(0, 1, n_rows).tolist(),
    'session_cost_change_feature': np.random.uniform(0, 1, n_rows).tolist(),
    'session_cost_change_feature_lag_1': np.random.uniform(0, 1, n_rows).tolist(),
    'session_cost_change_feature_lag_1_rolling_3_mean': np.random.uniform(0, 1, n_rows).tolist(),
    'sessionId': np.full(n_rows, 1).tolist(),  # Same session ID for all rows
    'category': np.random.choice(list(string.ascii_lowercase), n_rows).tolist()  # Random letters for category
}


# Test the load_ranking_model function
def test_load_ranking_model():
    model = load_ranking_model()
    assert model is not None  # Assumes the environment and file are correctly set

# Test the json_to_df function with a simple JSON input
def test_json_to_df():
    
    df = json_to_df(data)
    assert not df.empty

# Integration test for make_recommendation assuming all dependencies work
def test_make_recommendation():
    recommendations = make_recommendation(data)
    assert len(recommendations) <= int(os.getenv('NUMBER_OF_RECOMMENDATIONS'))
    assert isinstance(recommendations, list)