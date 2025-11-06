# 🧩 Selenium UI Automation – SauceDemo (Allure)

Automated UI tests for the demo e-commerce site [SauceDemo](https://www.saucedemo.com/)  
This repository demonstrates Selenium tests written in **Python** with **Pytest** and **Allure** reporting.

---

## 🚀 TL;DR

- Tests: Selenium + Pytest
- Reporting: Allure (allure-pytest + Allure CLI)

---

## 🔧 Prerequisites

- Python 3.8+ (recommended)
- Chrome (compatible with chromedriver)
- (local) Allure Commandline to generate/serve the HTML report
- Recommended: use a virtual environment

---

## 🧰 Tech stack

- Python
- Selenium WebDriver
- Pytest
- allure-pytest (plugin)
- webdriver-manager (automatic driver download)
- Allure Commandline (for generating/serving the report)

`requirements.txt`:
```
selenium
pytest
allure-pytest
webdriver-manager
```

---

## 📁 Project structure

```
selenium-tests-saucedemo/
├── tests/
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   ├── test_remove_button.py
│   ├── test_logout.py
│   └── test_cart_total.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

Example `pytest.ini` used in this repo:
```ini
[pytest]
addopts = -v --alluredir=allure-results
testpaths = tests
python_files = test_*.py
python_functions = test_*
```

---

## ⚙️ Local setup (step by step)

1. Clone repository:
```bash
git clone https://github.com/<your-username>/selenium-tests-saucedemo.git
cd selenium-tests-saucedemo
```

2. Create & activate virtual environment:

**Windows (PowerShell)**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. (Optional but recommended) run a single test to verify:
```bash
pytest tests/test_login.py -q
```

---

## ▶️ Run all tests and collect Allure results

Run tests (pytest is configured to save results to `allure-results` by default):
```bash
pytest
```

After the run you should have an `allure-results/` directory with JSON files, attachments, etc.

---

## 📊 Generate and view Allure report locally

### Option A — if you have Allure CLI installed

1. Install Allure CLI:

- **Windows (Chocolatey)**:
  ```powershell
  choco install allure
  ```

- **Manual (any OS)**:
  - Download a release zip from: https://github.com/allure-framework/allure2/releases
  - Unzip and add `<allure-folder>/bin` to your PATH

2. Serve the report:
```bash
allure serve allure-results
```
This command builds a temporary report and opens it in the browser.

3. Or generate static report:
```bash
allure generate allure-results -o allure-report --clean
# then open the generated folder (open index.html)
```

> If `allure` is not recognized, either add it to PATH or use the manual download method above.

---

## ✅ What this repo demonstrates

- Practical UI test cases with Selenium and Pytest  
- Fixture-based setup/teardown (clean code)  
- Allure reporting with attachments (screenshots) 

---

## Screenshots
<img width="1919" height="958" alt="image" src="https://github.com/user-attachments/assets/ad3af291-be19-477a-a967-8b35ef612a9d" />
<img width="1918" height="956" alt="image" src="https://github.com/user-attachments/assets/5a4f34c6-6057-4597-b837-789e14145b67" />
<img width="1917" height="958" alt="image" src="https://github.com/user-attachments/assets/0b816287-951e-458d-98b4-7fe6f9f5301a" />

