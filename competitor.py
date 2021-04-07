"""
   Competitor class
   (https://www.hallon.se/mobilabonnemang)
"""

import logging
from urllib import request
import time
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

class Competitor:
    """Competitor class"""

    # Set website adress
    website = "https://www.hallon.se/mobilabonnemang"

    def __init__(self, name):
        self.name = name

    def get_dataframe(self):
        """Code to get dataframe from website"""
        logging.info("Getting dataframe for %s", self.name)
        logging.debug("self.website value: %s", self.website)

        try:
            page = request.urlopen(self.website).read()
            soup = BeautifulSoup(page, "html5lib")
        except ValueError:
            logging.error("Problems getting data from the website at %s", self.website)

        # Extract part of website with prices
        if self.name=="Comviq":
            priceplans = soup.find_all('div', {'class' : 'col-xs-6 col-md-3'})
        elif self.name=="Fello":
            priceplans = soup.find_all('div', {'class' : 'css-iek43z el95idj0'})
            print(priceplans)
        elif self.name=="Hallon":
            priceplans = soup.find_all('li', {'class' : ['OfferCard__Card-sc-17ymwty-0 wIHrn', 'OfferCard__Card-sc-17ymwty-0 PDwUD'] })
        elif self.name=="Halebop":
            priceplans = soup.find_all('div', {'class' : 'plan-item__inner'})
        elif self.name=="Tele2":
            priceplans = soup.find_all('article', {'class' : 't2-js-data-card-subscription'})
        elif self.name=="Telia":
            priceplans = soup.find_all('div', {'class':'product-cards-list__card layout-4-col'})
        elif self.name=="Tre":
            priceplans = soup.find_all('div', {'class' : 'FormLabelWithRecurringPrice__Wrapper-sc-100lnzr-0 fhGGQ'})
        else:
            priceplans = []
            logging.error("Priceplan not found")

        #browser.close()

        if priceplans == []:
            logging.debug("Dataframe empty")
            raise Exception('The dataframe is empty')

        logging.info("Finished getting dataframe for %s", self.name)
        return priceplans

    def process_dataframe(self, dataframe):
        """Code to process the dataframe"""
        logging.info("Processing dataframe from %s", self.website)
        priceplans = dataframe
        priceplans = []

        logging.info("Finished processing dataframe from %s", self.website)
        return priceplans
