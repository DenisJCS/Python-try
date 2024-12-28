import requests
from bs4 import BeautifulSoup

DOLLAR_SOM = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%81%D0%BE%D0%BC%D1%83&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%81%D0%BE%D0%BC%D1%83&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhGGIICGIAEMgcIARAAGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEINzIxMWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

full_page = requests.get(DOLLAR_SOM, headers)

soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span",{"class":"MWvIVe"})
print(convert) 

