"""
   Comviq Class
   (https://webbutik.comviq.se/abonnemang)
"""

from datetime import date
import logging
import re
import pandas as pd

from competitor import Competitor

logging.basicConfig(level=logging.ERROR)
class Comviq(Competitor):
    """Comviq class, subclass of Competitor"""

    website = "https://webbutik.comviq.se/abonnemang"

    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def process_dataframe(self, dataframe):
        logging.info("Processing dataframe from %s", self.website)
        priceplans = dataframe

        # Create dataframes
        df_priceplans = pd.DataFrame(columns=['volume', 'campaign_price', 'full_price', 'campaign_months', 'campaign_data'])
        print(df_priceplans)

        # for each campaign_price segment, extract prices and volumes and append to dataframe
        for priceplan in priceplans:
            campaign_price = priceplan.find('div', {'class' : 'price-plan-card__price'})
            try:
                campaign_price = campaign_price.get_text()
                campaign_price = re.search("[0-9]+", campaign_price)[0]
            except AttributeError:
                logging.error("Error scraping for campaign_price for %s", self.name)
                campaign_price = 'NA'

            volume = priceplan.find('div', {'class' : 'price-plan-card__surf'})
            try:
                volume = volume.get_text()
                volume = re.search("[0-9]+", volume)[0]
            except AttributeError:
                logging.error("Error scraping for volume for %s", self.name)
                volume = 'NA'

            # No campaign_price campaigns at comviq for the moment, so set campaign_price=campaign_price
            full_price = campaign_price
            campaign_months = '1'

            campaign_data = priceplan.find('div', {'class' : 'ribbon ribbon-topright'}).text
            campaign_data = campaign_data.strip(' GBextra')

            data = {'volume' : [volume],
                'campaign_price' : [campaign_price],
                'full_price' : [full_price],
                'campaign_months' : [campaign_months],
                'campaign_data' : [campaign_data]}

            df_priceplans = df_priceplans.append(pd.DataFrame(data))

        # Add operator
        df_priceplans['operator'] = 'comviq'
        df_priceplans =  df_priceplans[df_priceplans.campaign_price != 'NA']
        today = date.today()
        df_priceplans['date'] = today.strftime("%Y%m%d")        

        logging.info("Finished processing dataframe from %s", self.website)
        return df_priceplans
