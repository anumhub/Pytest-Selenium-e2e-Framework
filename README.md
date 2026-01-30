# Pytest Selenium E2E Framework

An end-to-end Selenium automation framework built with **Python, Pytest, and Page Object Model (POM)**.
This project demonstrates **data-driven testing, reusable page objects, pytest fixtures, and HTML reporting**, designed to be easily runnable by anyone cloning the repository.

## What this project covers
Automated workflow (e-commerce style):
- Login
- Browse products
- Add product(s) to cart
- Checkout flow
- Validate order confirmation

## Tech Stack

* Python 3.x
* Selenium WebDriver
* Pytest - test runner + fixtures
* Pytest-HTML (reporting)
* Page Object Model (POM) (separate page classes for UI actions/locators)
* Test data externalized** via JSON

##  Quick Start 

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
open Reports/report.html
# more run options
pytest --browser_name=chrome
pytest --browser_name=chrome --headless
````

## Project Structure

```text
Pytest-Selenium-e2e-Framework
│
├── data/
│   └── test_e2eTestFramework.json      # Test data (credentials + product names)
│
├── pageObjects/
│   ├── login.py                        # Login page actions
│   ├── shop.py                         # Product selection & cart actions
│   └── checkout_confirmation.py        # Checkout & validation logic
│
├── tests/
│   ├── conftest.py                     # Pytest fixtures (browser setup/teardown)
│   ├── test_e2eTestFramework.py         # End-to-end data-driven test
│   └── test_SortingTables.py            # UI sorting validation test
│
├── Reports/
│   └── report.html                     # Auto-generated HTML report
│
├── pytest.ini                          # Pytest configuration
├── requirements.txt                    # Project dependencies
├── README.md                           # Project documentation
```



## How to Run Locally

You can run this project using **PyCharm (recommended)** or **Terminal only**.

### Option A: Run Using PyCharm (Recommended)

#### 1️⃣ Clone the repository


git clone https://github.com/anumhub/Pytest-Selenium-e2e-Framework.git


#### 2️⃣ Open the project in PyCharm

* Open **PyCharm**
* Click **File → Open**
* Select the cloned folder: `Pytest-Selenium-e2e-Framework`
* Click **Trust Project** when prompted

 This folder is the **project root**.

---

#### 3️⃣ Create & select Python virtual environment (one-time)

* Go to **Settings → Python Interpreter**
* Click **Add Interpreter → Virtualenv**
* Location: `.venv`
* Python version: **Python 3.x**
* Click **OK**

PyCharm will automatically activate the virtual environment.

---

#### 4️⃣ Install dependencies

Open **PyCharm Terminal** and run:

```bash
pip install -r requirements.txt
```

---

#### 5️⃣ Run tests

```bash
pytest
```

---

#### 6️⃣ Open HTML report (Mac)

```bash
open Reports/report.html
```

---

###  Option B: Run Using Terminal Only

#### 1️⃣ Navigate to desired location

```bash
cd ~/Downloads
```

#### 2️⃣ Clone the repository

```bash
git clone https://github.com/anumhub/Pytest-Selenium-e2e-Framework.git
cd Pytest-Selenium-e2e-Framework
```

 Ensure you are inside the **project root**.

---

#### 3️⃣ Create & activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

#### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

#### 5️⃣ Run tests

```bash
pytest
```

---

#### 6️⃣ Open HTML report (Mac)

```bash
open Reports/report.html
```

---

## Test Execution Flow (High Level)

1. Pytest starts execution using `pytest.ini`
2. Tests are discovered inside the `/tests` folder
3. Browser setup happens via `conftest.py` fixture
4. E2E test reads data from JSON file
5. Test runs once per dataset (parameterized)
6. Page Object flow:

   * LoginPage → ShopPage → CheckoutConfirmation
7. Assertions validate successful order placement
8. Browser closes after each test
9. HTML report is generated automatically



## Reporting

* Reports are generated using **pytest-html**
* Output location: `Reports/report.html`
* Includes:

  * Test status (Pass/Fail)
  * Execution time
  * Environment details



## Important Notes

* Always run commands from the **project root folder**
* `.venv` is local and should **not** be committed to GitHub
* Each test launches a **fresh browser session** by design
* `Reports/.gitkeep` exists only to track the empty folder in Git


## Future Enhancements

* Parallel execution (pytest-xdist)
* CI/CD integration (GitHub Actions / Jenkins)
* Browser cross-compatibility
