from bs4 import BeautifulSoup
import pandas as pd

# Load the mock HTML file
def scrape_static_page(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    jobs = []
    job_elements = soup.find_all('div', class_='job')
    for job in job_elements:
        title = job.find('h2', class_='title').text
        company = job.find('p', class_='company').text.split(": ")[1]
        location = job.find('p', class_='location').text.split(": ")[1]
        description = job.find('p', class_='description').text
        jobs.append({'Title': title, 'Company': company, 'Location': location, 'Description': description})
    
    # Convert to DataFrame and save as CSV
    df = pd.DataFrame(jobs)
    output_path = './sample_output/simulated_scraped_data.csv'
    df.to_csv(output_path, index=False)
    print(f"Scraped data saved to {output_path}")

# Run the scraper
scrape_static_page('./mock_job_page.html')
