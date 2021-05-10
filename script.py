import requests
import os


r = requests.get("https://google.es")
print(r.status_code)
