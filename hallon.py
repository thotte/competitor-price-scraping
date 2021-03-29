"""
   hallon Class
   (https://www.hallon.se/mobilabonnemang)
"""

from datetime import date
import logging
import re
import pandas as pd

from competitor import Competitor

logging.basicConfig(level=logging.ERROR)

class Hallon(Competitor):
    """Hallon class, subclass of Competitor"""

    website = "https://www.hallon.se/mobilabonnemang"

    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def process_dataframe(self, dataframe):
        logging.info("Processing dataframe from %s", self.website)
        priceplans = dataframe

        df_priceplans = pd.DataFrame(columns=['volume',
                                        'campaign_price', 'full_price', 'campaign_months', 'campaign_data'])

        # For each campaign_price segment, extract prices and volumes and append to dataframe
        for priceplan in priceplans:
            volume = priceplan.find('p', {'class' : 'Display__StyledDisplayMedium-sc-1i1vwyk-1 bredrt OfferCard__Name-sc-17ymwty-4 hqRmNd'}).text
            volume = volume.strip(' GB')

            campaign_price = priceplan.find('p', {'class' : 'Display__StyledDisplayMedium-sc-1i1vwyk-1 bredrt OfferCard__Price-sc-17ymwty-5 bkHRNi'}).text
            campaign_price = campaign_price.strip(' kr/mån')
            print(campaign_price)
            
            searchstring = priceplan.find('p', {'class' : 'Detail__StyledDetailRegular-sc-1wrousk-2 exNjRY OfferCard__FinePrint-sc-17ymwty-10 eCSpPK'}).text

            regexp = re.search('Priset gäller i (.+?) mån', searchstring)
            if regexp:
                campaign_months = regexp.group(1).strip()
            else:
                campaign_months = '1'


            full_price = searchstring
            if 'per 30 dagar' in full_price:
                full_price = campaign_price
            else:
                regexp = re.search('därefter(.+?)kr/mån', full_price)
                if regexp:
                    full_price = regexp.group(1).strip()

            searchstring = priceplan.find('p', {'class' : 'Detail__StyledDetailRegular-sc-1wrousk-2 exNjRY OfferCard__UspText-sc-17ymwty-14 lejUQQ'}).text

            regexp = re.search(r'\+(.+?)GB extra surf', searchstring)
            if regexp:
                campaign_data = regexp.group(1).strip()
            else:
                campaign_data = '0'

            data = {'volume' : [volume],
                'campaign_price' : [campaign_price],
                'full_price' : [full_price],
                'campaign_months' : [campaign_months],
                'campaign_data' : [campaign_data]}

            df_priceplans = df_priceplans.append(pd.DataFrame(data))

        df_priceplans['campaign_price'] = df_priceplans['campaign_price'].astype('int')
        df_priceplans.sort_values('campaign_price', ascending=False)
        df_priceplans = df_priceplans.drop_duplicates(subset='volume', keep = 'last')
        df_priceplans = df_priceplans[~df_priceplans['volume'].isin(['10', '6'])]
        df_priceplans['volume'] = df_priceplans['volume'].astype('int')

        # Add operator
        df_priceplans['operator'] = 'hallon'
        today = date.today()
        df_priceplans['date'] = today.strftime("%Y%m%d")
        
        logging.info("Finished processing dataframe from %s", self.website)
        return df_priceplans
