import requests
import json
from bs4 import BeautifulSoup
# URL to create an organization
org_url = 'https://www.wikileaf.com/strains'
r = requests.get(org_url)
# r = json.loads(r.text)
print(type(r))

data = BeautifulSoup(r.text, 'html.parser')
# print(data.prettify())
print(data.name)

# strain_data = data.find_all('div', attrs={'class', 'name disp-title'})

# print(type(strain_data))


fi = open("wikileaf3.txt", 'w')

# fi.write(r.content.decode("utf-8"))
fi.close
