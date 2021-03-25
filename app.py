"""
   Flask API for Competitor web scraper
"""

from flask import Response
from flask import Flask
from comviq import Comviq
from fello import Fello
from halebop import Halebop
from hallon import Hallon
from tele2 import Tele2
from telia import Telia
from tre import Tre
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    """Return API info"""
    return 'Price scraper API v0.1'

@app.route('/all')
def getall():
    """Return all prices"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    competitors.append(Fello("Fello"))
    competitors.append(Hallon("Hallon"))
    competitors.append(Halebop("Halebop"))
    competitors.append(Tele2("Tele2"))
    competitors.append(Telia("Telia"))
    competitors.append(Tre("Tre"))
    result = get_data(competitors)
    Large_df = pd.concat(result, ignore_index=True)
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

@app.route("/dfjson")
def dfjson():
    """return a json representation of the dataframe"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    prices = get_data(competitors)
    Large_df = pd.concat(prices, ignore_index=True)  
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

@app.route('/comviq')
def getcomviq():
    """Return Comviq prices"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    prices = get_data(competitors)
    Large_df = pd.concat(prices, ignore_index=True)  
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

@app.route('/fello')
def getfello():
    """Return Fello prices"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    prices = get_data(competitors)
    Large_df = pd.concat(prices, ignore_index=True)  
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

@app.route('/halebop')
def gethalebop():
    """Return Halebop prices"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    prices = get_data(competitors)
    Large_df = pd.concat(prices, ignore_index=True)  
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

@app.route('/hallon')
def gethallon():
    """Return Hallon prices"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    prices = get_data(competitors)
    Large_df = pd.concat(prices, ignore_index=True)  
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

@app.route('/tele2')
def gettele2():
    """Return Tele2 prices"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    prices = get_data(competitors)
    Large_df = pd.concat(prices, ignore_index=True)  
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

@app.route('/telia')
def gettelia():
    """Return Telia prices"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    prices = get_data(competitors)
    Large_df = pd.concat(prices, ignore_index=True)  
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

@app.route('/tre')
def gettre():
    """Return Tre prices"""
    competitors = []
    competitors.append(Comviq("Comviq"))
    prices = get_data(competitors)
    Large_df = pd.concat(prices, ignore_index=True)  
    return Response(Large_df.to_json(orient="records"), mimetype='application/json')

def get_data(comp):
    """Create a list with prices"""
    pricelist = []
    for competitor in comp:
        priceplan = competitor.get_dataframe()
        prices = competitor.process_dataframe(priceplan)
        pricelist.append(prices)
    return pricelist