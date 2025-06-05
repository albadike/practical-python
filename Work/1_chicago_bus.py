import urllib.request
from bs4 import BeautifulSoup

# 1. Fetch the page (HTML)
url = "https://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22&format=xml"
resp = urllib.request.urlopen(url)
html = resp.read().decode("utf-8", errors="ignore")

# 2. Parse it with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# 3. Now you can find tags just like in XML, e.g. all <pt> elements:
for pt in soup.find_all("meta"):
    print(pt)