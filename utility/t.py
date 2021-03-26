import requests
import json
r = requests.get("http://www.wookieware.com")
print(r.text)
