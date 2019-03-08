# Web-Crawler
Web crawler to scrap website such as Olx and Wikipedia. Monitoring competitors’ prices and product lineups can help online retailers win pricing battles; optimize sales and special offers; and track product trends over time. For many small ecommerce businesses, however, keeping tabs on the competition is a painful, manual process. So with the use of Scrapy framework,we can create a web spider to crawl competitors’ websites and collect pricing data.

## Getting Started

### Prerequisites
To use the Python-powered Scrapy application framework, you need to ensure that you have the following services, packages, and software loaded on your computer or server.

* Python 2.7 or greater version
* The pip package manager
* Python setuptools
* The lxml Python Library
* The OpenSSL Library

You’ll find a copy of the pip package manager at https://bootstrap.pypa.io/get-pip.py.

Once downloaded, open your Mac’s terminal, navigate to the directory you downloaded the get-pip.py file to, and run the following commands.
```
sudo python get-pip.py
```
```
sudo pip install Scrapy
```

Windows requires a couple of extra steps, which are outlined on the Scrapy website at http://doc.scrapy.org/en/1.0/intro/install.html.

## Running the tests
For scrapping mobile phones, tablets and accessories prices from Olx website, run- 
```
scrapy crawl mobiles -o results.csv
```
For scrapping from Wikipedia website, run- 
```
scrapy crawl wi -o results.csv
```

