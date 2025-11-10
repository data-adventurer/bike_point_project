# TfL BikePoint Data Extractor

This Python script retrieves live data from Transport for London’s (TfL) **BikePoint API**, validates the response, and saves the results as timestamped JSON files for historical or analytical use.

It includes error handling, retry logic for specific HTTP response codes, and embeds a snapshot timestamp in each record to track when the data was extracted.

---

## Overview

# Extract:

1. Connects to the [TfL BikePoint API](https://api.tfl.gov.uk/BikePoint).
2. Checks if the API response is valid and in JSON format.
3. Adds an extraction timestamp (`extract_time`) to each BikePoint record.
4. Saves the data locally in a `data/` directory as a timestamped JSON file.
5. Retries failed API calls (for `429` or `500` status codes) up to three times with a 20-second delay between attempts.

---

# Load:

This script automates the process of uploading `.json` files from a local `data` directory to an AWS S3 bucket.

1. Establishes a connection to S3 using the `boto3` library.
2. Verifies that the configured S3 bucket can be accessed. If access is denied, the script stops running.
3. Searches the local `data` folder for any files ending with `.json`.
4. If a `.json` file is found, it uploads the first one to the specified S3 bucket.
5. Once uploaded, the local file is deleted to prevent duplicate uploads.

---

## Requirements

Before running the script, make sure you have the following installed:

```bash
pip install requests
```

Python version **3.8+** is recommended.

---

## How to Use

1. Clone or download the script into your working directory.

2. Create a folder named `data` in the same directory (for storing output files).

3. Run the script in your terminal:

   ```bash
   python bikepoint_extractor.py
   ```

4. If successful, a new JSON file will appear in the `data/` folder with a name like:

   ```
   2025-11-05T16-30-12.json
   ```

5. Once you have JSON files in the data/ folder, run the upload script to send them to your AWS S3 bucket

6. If no .json files are found, you’ll see the message:

   ```
   No files to upload
   ```

7. If AWS credentials are invalid or bucket access is denied, the script will print:

   ```
   Access denied
   ```

---

## Output Format

Each output file is a JSON array where each object represents a TfL BikePoint location, for example:

```json
[
  {
    "id": "BikePoints_1",
    "commonName": "River Street , Clerkenwell",
    "lat": 51.529163,
    "lon": -0.10997,
    "extract_time": "2025-11-05 16:30:12.123456"
  },
  ...
]
```

The added `extract_time` field records when the data snapshot was taken.

---

## Error Handling and Retries

### API Extraction Script

- If the response returns a **200 OK**, the script proceeds normally.
- If the response returns **429 (Too Many Requests)** or **500 (Internal Server Error)**, the script:

  - Waits 20 seconds.
  - Retries up to 3 times before giving up.

- Any other status code or JSON decoding error will terminate the script with an error message.

### AWS S3 Upload Script

- If S3 access is denied or credentials are invalid, the script prints:

  ```
  Access denied
  ```

  and exits without attempting uploads.

- If no `.json` files are found in the `data` folder, the script prints:

  ```
  No files to upload
  ```

- Any other unexpected error (e.g., network interruption, missing environment variables, etc.) is printed to the console, and the script stops execution safely.

---

## Testing

To test error handling, you can temporarily replace the API URL with a non-JSON endpoint such as:

```python
url = 'https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll'
```

This will intentionally raise a JSON decode error to verify the exception handling logic.

---

## License

This project is provided for educational and analytical use. Data is sourced from the public TfL API under their [Open Data Licence](https://tfl.gov.uk/corporate/terms-and-conditions/transport-data-service).

---
