"""
   Main module for Competitor web scraper
   (https://www.hallon.se/mobilabonnemang)
"""

import logging
from comviq import Comviq
from hallon import Hallon
from halebop import Halebop
from tele2 import Tele2
from tre import Tre
import pandas as pd

logging.basicConfig(level=logging.ERROR)

# Initialize
competitors = []
pricelist = []

# Create Competitors
competitors.append(Comviq("Comviq"))
competitors.append(Hallon("Hallon"))
competitors.append(Halebop("Halebop"))
competitors.append(Tele2("Tele2"))
competitors.append(Tre("Tre"))

# Create priceplans for each competitor and append to a common dataframe
for competitor in competitors:
    try:
        priceplan = competitor.get_dataframe()
        prices = competitor.process_dataframe(priceplan)
        pricelist.append(prices)
    except:
        logging.error("Error getting prices for for %s", competitor.name)    

# Format pricelist into dataframe
Large_df = pd.concat(pricelist, ignore_index=True)
print(Large_df)
