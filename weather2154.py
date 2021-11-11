import sys
import stdio
from instream import InStream
from outstream import OutStream

"""
Find a website that publishes the current 
temperature in your area, andwrite a 
screen-scraper program weather.py 
so that typing python weather.py followed 
by your ZIP code will give you a weather forecast.
"""


def _readHTML():
     WEBSITE = 'https://www.9news.com.au/weather/nsw/castle-hill'
     page = InStream(WEBSITE)
     html = page.readAll()
     outstream = OutStream('outFile123')
     outstream.write(html)
     return html

def weather():
     html = _readHTML()
     findstr = html.find('weather-temperature"', 0)
     beg = html.find('>', findstr)
     end = html.find('</span>', beg)
     temp = html[beg + 1:end]

     findstr1 = html.find('aria-label=', 0)
     beg1 = html.find('"', findstr1)
     end1 = html.find('" title=', beg1)
     temp2 = html[beg1 + 1:end1]


     return str(temp+" "+temp2)

def main():
     print(weather())
     # stdio.writef('%.2f\n', price)
if __name__ == '__main__': main()