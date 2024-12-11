import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('sample_output/scraped_jobs.csv')

# Job counts by company
company_counts = df['company'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(company_counts.index, company_counts.values)
plt.title('Job Counts by Company')
plt.xlabel('Company')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.tight_layout()
# Save the plot
plt.savefig('images/job_counts_by_company.png')
plt.show()

# Job counts by location
location_counts = df['location'].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(location_counts.index, location_counts.values)
plt.title('Job Counts by Location')
plt.xlabel('Location')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.tight_layout()
# Save the plot
plt.savefig('images/job_counts_by_location.png')
plt.show()
