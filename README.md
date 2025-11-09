# qa_automation_challenge
Automation test framework for the QA Engineer technical challenge.

---

## Project Description

This project contains automated tests for the FashionHub demo website.  
It covers functional and UI tests, supports cross-browser testing, and allows running tests in multiple environments (local, staging, production).  
Additionally, it includes a script to fetch open pull requests from a GitHub repository and save them in CSV format.

---

## Prerequisites

- Python 3.10+
- Git
- Virtual environment (venv)
- Browsers supported by Playwright: Chromium, Firefox, WebKit
- Internet connection (for GitHub PR API script)

---

## Setup Instructions

1. **Clone the repository** – Download the project to your local machine:

```bash
git clone https://github.com/your-username/qa_automation_challenge.git
cd qa_automation_challenge

```
2. **Create and activate a virtual environment** – This isolates dependencies for this project:

```bash
python3 -m venv myenv
source myenv/bin/activate   # macOS/Linux
myenv\Scripts\activate      # Windows
```

# 3. Install dependencies – Install Python packages required for Playwright and the tests
```bash
pip install -r requirements.txt
playwright install
```

# 4. Run a single test file – Example: Run the *About Page* test in *production* on *Chromium* browser
```bash
pytest tests/test_about.py --env=production --browser=chromium -v
```
# 5. Run all tests – Example: Run *all* tests in *production* on *Chromium* browser
```bash
pytest tests/ --env=production --browser=chromium -v
```

# 6. Run the GitHub PR CSV script – Fetch all open PRs from a repository and save to CSV
```bash
python api_testing/github_pr_to_csv.py
```

# 7. Running in different browsers – Supported browsers: chromium, firefox, webkit

```bash
pytest tests/test_about.py --env=production --browser=firefox -v
```

# 8. Running in different environments – Supported environments: local, staging, production
```bash
pytest tests/test_home.py --env=staging --browser=chromium -v
```
