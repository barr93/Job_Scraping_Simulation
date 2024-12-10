import pandas as pd
import matplotlib.pyplot as plt

# Load the scraped data
df = pd.read_csv('sample_output/scraped_jobs.csv')

# Count of jobs by company
company_counts = df['company'].value_counts()
plt.bar(company_counts.index, company_counts.values)
plt.title('Number of Jobs by Company')
plt.xlabel('Company')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Count of jobs by location
location_counts = df['location'].value_counts()
plt.bar(location_counts.index, location_counts.values)
plt.title('Number of Jobs by Location')
plt.xlabel('Location')
plt.ylabel('Number of Jobs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
