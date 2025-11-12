# url for the Tfl Bike Point API
url = 'https://api.tfl.gov.uk/BikePoint'

def extract (url):
    response = requests.get(url, timeout=10) # call the API
    retry_these_status_codes = [429, 500] # list of error codes where the api can be called again

    count = 0 # start of the count for the while loop
    max_count = 3 # the max number of times the while loop can run

    while count < max_count:
        if response.status_code == 200:
            # if the conneciton is good, test if the file being called is a json
            try:
                data = response.json()
            # if the file is not a json print the error and break the loop
            except Exception as e:
                print(e)
                break
            
            extract_time =  datetime.now() # adding to json to keep track of snapshot in time

            # add the extract time to each instance in the json
            for bp in data:
                bp['extract_time'] = str(extract_time)

            # specify the file path to save json to local drive
            filepath = 'data/' +  extract_time.strftime('%Y-%m-%dT%H-%M') + '.json'

            # save to local drive
            with open(filepath, 'w') as file:
                json.dump(data, file)
            break
        
        # if the status code is in the list of codes to retry call the API again but only max three times
        elif response.status_codes in  retry_these_status_codes:
            time.sleep(20)
            print(f"Error code: {response.status_code}, {response.reason}")
            count += 1

        # if the status code is anything else print the error code and break the loop
        else:
            print(f"Error code: {response.status_code}, {response.reason}")
            break