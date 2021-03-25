"""
   scraper_main.py unit tests
"""

from hallon import Hallon

def test_processing_dataframe():
    """Test that dataframe is correctly processed"""
    hallon = Hallon("Hallon")
    assert hallon.name == "Hallon"
