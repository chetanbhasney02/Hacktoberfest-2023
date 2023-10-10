#web scraping the stock prices from a finance website

import requests
from bs4 import BeautifulSoup

def scraper(url):
    res = requests.get(url) # sending the request to the website and waiting for response
    html = res.text
    if res.status_code == 200:
        soupRes = BeautifulSoup(html, 'lxml') 
    else:
        print('Failed to retrieve the web page. Try again.')

    table = soupRes.find('table', {'class':'table-striped'}) # DOM element where the stock prices are stored

    if table:
        rows = table.find_all('tr') #Finding all the rows

        for row in rows:
            try:
                stock_name_tag = row.find('td').find('a').find('strong')
                stock_price_tag = row.find_all('td')[1].find('span')

                if stock_name_tag and stock_price_tag:
                    stock_name = stock_name_tag.text.strip()
                    stock_price = stock_price_tag.text.strip()
                    print('Stock Name:', stock_name)
                    print('Stock Price:', stock_price)
                    print('--------------------------------------')
            except AttributeError as e:
                pass #For the row which does not follow the provided structure
    else:
        print('Table not found.')

if __name__ == '__main__':
    url = 'https://www.etmoney.com/stocks/list-of-stocks'
    scraper(url)