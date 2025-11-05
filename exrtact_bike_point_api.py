from datetime import datetime
import time as t
import requests
import json

url = 'https://api.tfl.gov.uk/BikePoint'

response = requests.get(url, timeout=10)

print(response.status_code)

data = response.json()

# print(data)

extract_time =  datetime.now()

for bp in data:
    bp['extract_time'] = str(extract_time)

# print(data[0])

filepath = 'data/' +  extract_time.strftime('%Y-%m-%dT%H-%M-%S') + '.json'

with open(filepath, 'w') as file:
    json.dump(data, file)


