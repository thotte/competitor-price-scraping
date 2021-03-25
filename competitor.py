"""
   Competitor class
   (https://www.hallon.se/mobilabonnemang)
"""

import logging
from urllib import request
import urllib
from lxml import html
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
            options = Options()
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            #browser = webdriver.Chrome(options=options)
            #browser.get(self.website)
            time.sleep(1)
            page = request.urlopen(self.website)
            page = page.read()
            page = html.fromstring(page)
            text = urllib.request.urlopen(self.website).read().decode('utf8')
            htmltree = html.fromstring(text)
            print(htmltree)
            
            #print(page)
            soup = BeautifulSoup(page, "lxml")
            # Extract website
            #soup = BeautifulSoup(browser.page_source, "html5lib")
            time.sleep(1)
        except ValueError:
            logging.error("Problems getting data from the website at %s", self.website)

        # Extract part of website with prices
        if self.name=="Comviq":
            priceplans = soup.find_all('div', {'class' : 'col-xs-6 col-md-3'})
        elif self.name=="Fello":
            priceplans = soup.find_all('div', {'class' : 'css-iek43z el95idj0'})
            print(priceplans)
        elif self.name=="Hallon":
            priceplans = soup.find_all('li', {'class' : 'expandable-product-card expandable-product-card--no-upsale js-expandable-productcard' })
        elif self.name=="Halebop":
            priceplans = soup.find_all('div', {'class' : 'plan-item__inner'})
        elif self.name=="Tele2":
            priceplans = soup.find_all('article', {'class' : 't2-js-data-card-subscription'})
        elif self.name=="Telia":
            priceplans = soup.find_all('div', {'class':'product-cards-list__card layout-4-col'})
        elif self.name=="Tre":
            priceplans = soup.find_all('div', {'class' : 'FormLabelWithRecurringPrice__Wrapper-sc-100lnzr-0 bDFTGy'})
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
