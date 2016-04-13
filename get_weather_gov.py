import sys
import requests
import re
from bs4 import BeautifulSoup as bs
url = 'http://forecast.weather.gov/MapClick.php?lat=40.71326027124559&lon=-74.00710399075575#.Vw7PjjZh2cw'
r = requests.get(url)
if(r.status_code != 200):
    sys.exit(1)

text=r.text
s=bs(text)
temp_string=s.select('.temp-high')[0].text
temp=re.sub('[^0-9]', '', temp_string)
print temp






