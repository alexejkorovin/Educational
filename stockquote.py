#-----------------------------------------------------------------------
# stockquote.py
#-----------------------------------------------------------------------

import sys
import stdio
from instream import InStream
# import base64
import requests
#-----------------------------------------------------------------------

# Return the raw HTML from the website http://finance.yahoo.com

def _readHTML(stockSymbol):
    WEBSITE = "https://finance.yahoo.com/quote/" +"?p="+ stockSymbol
    resp = requests.get(WEBSITE)
    html = resp.json()
    # WEBSITE = 'https://finance.yahoo.com/quote/'
    # page = InStream(WEBSITE + stockSymbol)
    # page = base64.b64encode(page.encode('utf-8',errors = 'strict'))
    return html

#-----------------------------------------------------------------------

# Extract the current stock price of the stock whose symbol is 
# stockSymbol from the HTML and return it.

def priceOf(stockSymbol):
    html  = _readHTML(stockSymbol)
    trade = html.find('{"raw",', 0)
    beg   = html.find('"fmt":"', trade)
    end   = html.find('"},"', beg)
    price = html[beg+1:end]
    price = price.replace(',', '')
    return float(price)

#-----------------------------------------------------------------------

# Accept string stockSymbol as a command-line argument. Write to
# standard output the current stock price for stockSymbol, as reported
# by the website http://finance.yahoo.com/.

def main():
    stockSymbol = sys.argv[1]
    price = priceOf(stockSymbol)
    stdio.writef('%.2f\n', price)

if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python stockquote.py goog
# 540.48

# python stockquote.py adbe
# 83.55

