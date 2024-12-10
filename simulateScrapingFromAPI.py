import requests
import pandas as pd

# URL for the mock API
url = 'http://127.0.0.1:5000/jobs'

# Fetch data from the API
response = requests.get(url)
if response.status_code == 200:
    print("Data fetched successfully!")
    jobs = response.json()
    
    # Convert to a DataFrame
    df = pd.DataFrame(jobs)
    print(f"Number of records fetched: {len(df)}")
    print(df.head())

    # Save the data to a CSV file
    df.to_csv('sample_output/scraped_jobs.csv', index=False)
    print("Data saved to 'sample_output/scraped_jobs.csv'")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
