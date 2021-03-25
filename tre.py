"""
   Tre Class
   (https://www.tre.se/privat/webshop/abonnemang)
"""

from datetime import date
import logging
import re
import pandas as pd

from competitor import Competitor

logging.basicConfig(level=logging.ERROR)

class Tre(Competitor):
    """Tre class, subclass of Competitor"""

    website = "https://www.tre.se/handla/abonnemang?pricePlanId=X8Q9djchE5wWbmpOhNOMeg%3D%3D"

    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def process_dataframe(self, dataframe):
        logging.info("Processing dataframe from %s", self.website)
        priceplans = dataframe
        print(priceplans)
        # Create dataframe
        df_priceplans = pd.DataFrame(columns=['volume', 'campaign_price', 'full_price', 'campaign_months', 'campaign_data'])

        for priceplan in priceplans:
            volume = priceplan.find('span').text
            volume = volume.replace(' GB/mån','').strip()

            if volume == 'Obegränsat':
                volume = 'unlimited'

            campaign_price = priceplan.find('span', {'class' : 'InformativePrice__Price-sc-9ubzau-0'}).text
            campaign_price = campaign_price.replace(' kr/mån','').strip()

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
        df_priceplans['operator'] = 'tre'
        today = date.today()
        df_priceplans['date'] = today.strftime("%Y%m%d")                
            
        logging.info("Finished processing dataframe from %s", self.website)
        return df_priceplans
