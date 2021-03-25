"""
   Halebop Class
   (https://shop.halebop.se/mobilabonnemang)
"""

from datetime import date
import logging
import re
import pandas as pd

from competitor import Competitor

logging.basicConfig(level=logging.ERROR)

class Halebop(Competitor):
    """Halebop class, subclass of Competitor"""

    website = "https://shop.halebop.se/mobilabonnemang"

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
            campaign_price = priceplan.find('p', {'class' : 'plan-item__price'})
            campaign_price = campaign_price.get_text()
            campaign_price = re.search("[0-9]+", campaign_price)[0]

            volume = priceplan.find('strong')
            volume = volume.get_text()
            volume = re.search("[0-9]+", volume)[0]

            # For now, add this manually
            campaign_months = '3'

            searchstring = priceplan.find('p', {'class' : 'plan-item__strike-through'}).text
            regexp = re.search('(.+?) kr/mån', searchstring)
            if regexp:
                full_price = regexp.group(1).strip()
            else:
                full_price = campaign_price

            campaign_data = 0    

            data = {'volume' : [volume],
                'campaign_price' : [campaign_price],
                'full_price' : [full_price],
                'campaign_months' : [campaign_months],
                'campaign_data' : [campaign_data]}

            df_priceplans = df_priceplans.append(pd.DataFrame(data))

        df_priceplans['campaign_price'] = df_priceplans['campaign_price'].astype('int')
        df_priceplans.sort_values('campaign_price', ascending=False)
        df_priceplans = df_priceplans.drop_duplicates(subset='volume', keep = 'last')

        # Add operator
        df_priceplans['operator'] = 'halebop'
        today = date.today()
        df_priceplans['date'] = today.strftime("%Y%m%d")        

        logging.info("Finished processing dataframe from %s", self.website)
        return df_priceplans
