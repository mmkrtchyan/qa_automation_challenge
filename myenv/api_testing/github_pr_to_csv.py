import requests
import csv

# GitHub repository pull requests URL (open PRs only)
api_url = "https://api.github.com/repos/appwrite/appwrite/pulls"

# Send GET request
response = requests.get(api_url)
response.raise_for_status()  # Raise exception if request failed

pull_requests = response.json()

# File to save the PR data
output_file = "open_pull_requests.csv"

with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    # Write CSV header
    writer.writerow(["PR Name", "Created Date", "Author"])

    # Write each pull request info
    for pr in pull_requests:
        pr_name = pr["title"]
        created_date = pr["created_at"]
        author = pr["user"]["login"]
        writer.writerow([pr_name, created_date, author])

print(f"Successfully saved {len(pull_requests)} open PRs to {output_file}")