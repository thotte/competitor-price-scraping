"""
   Telia Class
   (https://www.telia.se/privat/telefoni/abonnemang-kontantkort)
"""

from datetime import date
import logging
import pandas as pd

from competitor import Competitor

logging.basicConfig(level=logging.ERROR)

class Telia(Competitor):
    """Telia class, subclass of Competitor"""

    website = "https://www.telia.se/privat/telefoni/abonnemang-kontantkort"

    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def process_dataframe(self, dataframe):
        logging.info("Processing dataframe from %s", self.website)
        priceplans = dataframe

        # Create dataframe
        df_priceplans = pd.DataFrame(columns=['volume', 'campaign_price', 'full_price', 'campaign_months', 'campaign_data'])

        # for each campaign_price segment, extract prices and volumes and append to dataframe
        for priceplan in priceplans:
            volume = priceplan.find('p',{'class':['nf-product-poster__image-heading nf-product-poster__image-heading--middle']}).text
            volume = volume.replace('GB','').strip()

            campaign_price = priceplan.find('p', {'class':'nf-product-poster__details-pitch-price with-out-secondary'}).text
            campaign_price = campaign_price[0:6].strip()

            if volume == '' and campaign_price != '':
                volume = 'unlimited'

            if volume == 'OBEGRÄNSAD':
                volume = 'unlimited'

            full_price = campaign_price
            campaign_months = '1'

            campaign_data = 0

            data = {'volume' : [volume],
                'campaign_price' : [campaign_price],
                'full_price' : [full_price],
                'campaign_months' : [campaign_months],
                'campaign_data' : [campaign_data]}

            df_priceplans = df_priceplans.append(pd.DataFrame(data))

        # Add operator
        df_priceplans['operator'] = 'telia'
        today = date.today()
        df_priceplans['date'] = today.strftime("%Y%m%d")

        logging.info("Finished processing dataframe from %s", self.website)
        return df_priceplans
