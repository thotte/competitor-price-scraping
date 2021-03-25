"""
   competitor.py unit tests
   (https://www.hallon.se/mobilabonnemang)
"""

import requests
from competitor import Competitor

def test_site_availability():
    """Test site availability"""
    site = Competitor.website
    req = requests.head(site)
    assert req.status_code == 200

def test_getting_dataframe():
    """Test that dataframe is returning something"""
    hallon = Competitor("Hallon")
    function_returns_list = hallon.get_dataframe()
    assert len(function_returns_list) != 0

def test_processing_dataframe():
    """Test that dataframe is correctly processed"""
    hallon = Competitor("Hallon")
    function_returns_list = hallon.process_dataframe(hallon.get_dataframe())
    assert len(function_returns_list) == 0
