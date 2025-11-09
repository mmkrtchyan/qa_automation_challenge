import requests
import csv
import os

# Fetch all open pull requests from a GitHub repository
def get_all_prs(api_url: str, max_page: int = 100) -> list:
    all_prs = []
    page = 1
    while True:
        params = {"state": "open", "per_page": max_page, "page": page}
        response = requests.get(api_url, params=params)
        prs = response.json()
        if not prs:
            break
        all_prs.extend(prs)
        page += 1
    return all_prs


# Format PR data for CSV output
def format_data(all_prs: list):
    result = []
    for pr in all_prs:
        pr_name = pr["title"]
        created_date = pr["created_at"]
        author = pr["user"]["login"]
        result.append([pr_name, created_date, author])
    return result


# Write PR data into a CSV file
def collect_prs_csv(out_file: str, api_url: str):
    all_prs = get_all_prs(api_url)
    with open(out_file, mode="w", encoding="utf-8") as f:
        for pr in all_prs:
            f.write(f"PR Name: {pr['title']}\n")
            f.write(f"Created Date: {pr['created_at']}\n")
            f.write(f"Author: {pr['user']['login']}\n\n")


# Main entry point
if __name__ == "__main__":
    repo_url = os.getenv(
        "GITHUB_REPO_URL", "https://api.github.com/repos/appwrite/appwrite/pulls"
    )
    output_file = os.getenv("OUTPUT_FILE", "open_pull_requests.csv")

    collect_prs_csv(output_file, repo_url)