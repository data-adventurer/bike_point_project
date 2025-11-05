from datetime import datetime
import time as t
import requests

url = 'https://api.tfl.gov.uk/BikePoint'

response = requests.get(url, timeout=10)

print(response.status_code)

