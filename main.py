from exrtact_bike_point_api import extract
from load import load

# url for the Tfl Bike Point API
url = 'https://api.tfl.gov.uk/BikePoint'

extract(url)

load()