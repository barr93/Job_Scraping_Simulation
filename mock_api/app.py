from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load job data from the mock JSON file
with open('mock_jobs_data.json', 'r') as f:
    jobs = json.load(f)

@app.route('/jobs', methods=['GET'])
def get_jobs():
    """
    Fetch job listings with optional filters for title and location.
    """
    title_filter = request.args.get('title')
    location_filter = request.args.get('location')

    # Apply filters
    filtered_jobs = jobs
    if title_filter:
        filtered_jobs = [
            job for job in filtered_jobs
            if title_filter.lower() in job['title'].lower()
        ]
    if location_filter:
        filtered_jobs = [
            job for job in filtered_jobs
            if location_filter.lower() in job['location'].lower()
        ]

    return jsonify(filtered_jobs)

if __name__ == '__main__':
    app.run(debug=True)
