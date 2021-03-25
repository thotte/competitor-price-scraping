"""
   Fello Class
   (https://www.fello.se/mobilabonnemang/)
"""

from datetime import date
import logging
import re
import pandas as pd

from competitor import Competitor

logging.basicConfig(level=logging.ERROR)

class Fello(Competitor):
    """Fello class, subclass of Competitor"""

    website = "https://www.fello.se/mobilabonnemang/"

    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def process_dataframe(self, dataframe):
        logging.info("Processing dataframe from %s", self.website)
        priceplans = dataframe
        #print(priceplans)
        # Create dataframe
        df_priceplans = pd.DataFrame(columns=['volume', 'campaign_price', 'full_price', 'campaign_months', 'campaign_data'])

        # for each campaign_price segment, extract prices and volumes and append to dataframe
        for priceplan in priceplans:
            if "css-z5r2tn" in str(priceplan):
                volume = priceplan.find('div', {'class' : 'css-z5r2tn'}).text
            else:
                volume = priceplan.find('div', {'class' : 'css-166mfs1'}).text
            volume = volume.replace('GB','').strip()
            campaign_price = priceplan.find('span', {'class' : 'css-vpdphh'}).text
            campaign_price = campaign_price.replace(' kr/mån','').strip()

            searchstring = priceplan.find('div', {'class' : 'css-1m9v747'}).text
            regexp = re.search('Månad 1-(.+?) därefter', searchstring)
            if regexp:
                campaign_months = regexp.group(1).strip()
            else:
                campaign_months = '1'

            regexp = re.search('därefter (.+?) kr/mån', searchstring)
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

        # Add operator
        df_priceplans['operator'] = 'fello'
        today = date.today()
        df_priceplans['date'] = today.strftime("%Y%m%d")        

        logging.info("Finished processing dataframe from %s", self.website)
        return df_priceplans
