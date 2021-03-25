# Competitor campaign_price Scraping

An application for scraping the subscription prices from competitors. The classes for each competitor is in the .py file with the competitors name

### To install all dependencies
```pip install -r requirements.txt```  

### To run the application   
```python3 scraper_main.py ```


### To run tests
From the competitor campaign_price scraping folder:  
```pytest ```

### To run tests with code coverage
From the competitor campaign_price scraping folder:  
```pytest --cov=../competitor_price_scraping ```

### To update requirements
install pipreqs (if not installed)  
(```pip3 install pipreqs```  )  
then to generate the requirements  
```pipreqs ../competitor_price_scraping --force```

### To build the docker image
```docker image build -t price-scraper .```

### To run the docker image
```docker run -d --rm -p 80:5000 --name price-scraper-service price-scraper```  
