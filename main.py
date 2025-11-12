from dotenv import load_dotenv
from datetime import datetime
import time
import requests
import json
import boto3
import os
import sys

from exrtact_bike_point_api import extract
from load import load

# url for the Tfl Bike Point API
url = 'https://api.tfl.gov.uk/BikePoint'

print('running extract')
extract(url)
print('extract done')

print('running load')
load()
print('load successful')



