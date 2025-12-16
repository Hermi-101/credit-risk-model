import pytest
import pandas as pd
import numpy as np
# Assuming your actual feature engineering script is named 'data_processor.py'
# and contains a function like 'engineer_rfm_features'.

# --- Helper function we are testing (Mimic the logic used earlier) ---
def mock_engineer_features(df):
    """Mock feature engineering function that aggregates data."""
    # Assuming df has 'Customer_ID', 'Date', and 'Revenue' for this test
    # Mock aggregation similar to RFM calculation
    rfm_df = df.groupby('Customer_ID').agg(
        Recency_Days=('Date', lambda x: (pd.to_datetime('2024-01-01') - x.max()).days),
        Frequency_Mean=('Date', 'count'),
        Monetary_Mean=('Revenue', 'mean')
    ).reset_index()
    return rfm_df

@pytest.fixture
def sample_raw_data():
    """Fixture to provide sample raw data."""
    data = {
        'Customer_ID': [1, 1, 2, 3, 3],
        'Date': ['2023-12-01', '2023-11-01', '2023-12-25', '2023-10-01', '2023-10-05'],
        'Revenue': [100, 50, 200, 30, 40]
    }
    return pd.DataFrame(data)

def test_feature_engineering_returns_expected_columns(sample_raw_data):
    """Test 1: Check that the RFM feature columns are present."""
    processed_df = mock_engineer_features(sample_raw_data)
    expected_columns = ['Customer_ID', 'Recency_Days', 'Frequency_Mean', 'Monetary_Mean']
    
    # Assert that all expected columns are in the output
    assert all(col in processed_df.columns for col in expected_columns)
    assert processed_df.shape[1] == len(expected_columns)

def test_rfm_calculation_accuracy(sample_raw_data):
    """Test 2: Check if Recency and Monetary values are calculated correctly for a known customer."""
    processed_df = mock_engineer_features(sample_raw_data)
    
    # Customer 1: Recency = (2024-01-01 - 2023-12-01) = 31 days. Monetary = (100+50)/2 = 75.0
    customer_1_data = processed_df[processed_df['Customer_ID'] == 1].iloc[0]
    
    # Check Recency
    assert customer_1_data['Recency_Days'] == 31
    
    # Check Monetary Mean
    assert customer_1_data['Monetary_Mean'] == 75.0
    
    # Check Frequency (count of 2)
    assert customer_1_data['Frequency_Mean'] == 2

# You would run the tests in your terminal:
# pytest tests/test_data_processing.py