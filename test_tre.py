"""
   comviq.py unit tests
"""

import requests
from tre import Tre


tre = Tre("Tre")
df = tre.get_dataframe()
function_returns_list = tre.process_dataframe(df)

def test_site_availability():
    """Test site availability"""
    site = Tre.website
    req = requests.head(site)
    assert req.status_code == 200

def test_getting_dataframe():
    """Test that dataframe is returning something"""
    assert len(df) != 0

def test_processing_dataframe():
    """Test that dataframe is correctly processed"""
    assert len(function_returns_list) != 0

def test_number_of_rows():
    """Test that dataframe rows is more than 5"""
    total_rows = len(function_returns_list)
    assert total_rows > 3

def test_number_of_rows_failed():
    """Test that dataframe rows is more than 5"""
    total_rows = len(function_returns_list)
    assert total_rows > 3   

def test_column_names():
    """Test that column names are correct"""
    assert set(function_returns_list.columns) == {'volume', 'campaign_price', 'full_price', 'campaign_months', 'campaign_data', 'operator', 'date'}