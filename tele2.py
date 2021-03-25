"""
   Tele2 Class
   (https://www.tele2.se/handla/mobilabonnemang)
"""

from datetime import date
import logging
import re
import pandas as pd

from competitor import Competitor

logging.basicConfig(level=logging.ERROR)

class Tele2(Competitor):
    """Tele2 class, subclass of Competitor"""
    website = "https://www.tele2.se/handla/mobilabonnemang"

    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def process_dataframe(self, dataframe):
        logging.info("Processing dataframe from %s", self.website)
        priceplans = dataframe

        # Create dataframe
        df_priceplans = pd.DataFrame(columns=['volume', 'campaign_price', 'full_price', 'campaign_months', 'campaign_data'])

        # For each campaign_price segment, extract prices and volumes and append to dataframe
        for priceplan in priceplans:
            campaign_price = priceplan.get('data-card-subscription-price')
            volume = priceplan.get('data-card-subscription-name')

            try:
                volume = re.search("[0-9]+", volume)[0]
            except:
                volume = 'unlimited'

            full_price = campaign_price
            campaign_months = 1

            campaign_data = 0

            data = {'volume' : [volume],
                'campaign_price' : [campaign_price],
                'full_price' : [full_price],
                'campaign_months' : [campaign_months],
                'campaign_data' : [campaign_data]}

            df_priceplans = df_priceplans.append(pd.DataFrame(data))

        # Add operator
        df_priceplans['operator'] = 'tele2'
        today = date.today()
        df_priceplans['date'] = today.strftime("%Y%m%d")

        logging.info("Finished processing dataframe from %s", self.website)
        return df_priceplans
