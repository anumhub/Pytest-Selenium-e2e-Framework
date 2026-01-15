# Selenium + Python E-Commerce Automation Framework (pytest + POM)

This repository demonstrates an end-to-end UI automation framework built using **Selenium WebDriver**, **Python**, and **pytest**.
The framework follows the **Page Object Model (POM)** to keep tests readable, maintainable, and scalable.

## What this project covers
Automated workflow (e-commerce style):
- Login
- Browse products
- Add product(s) to cart
- Checkout flow
- Validate order confirmation

## Framework Highlights
- **pytest** test runner + fixtures
- **Page Object Model (POM)** (separate page classes for UI actions/locators)
- **Test data externalized** via JSON
- **HTML reporting** via pytest-html
- **Screenshot capture on failure** for debugging

## Repository Structure
- tests/ # pytest test cases + conftest.py (fixtures)
-pageObjects/ # Page Object classes (Login, Shop, Checkout/Confirmation)
- data/ # JSON test data
- utils/ # helper utilities
- Reports/ # HTML reports + failure screenshots
- pytest.ini # pytest configuration
- requirements.txt # dependencies


## Setup
### Prerequisites
- Python 3.8+
- Google Chrome installed

### Install dependencies
```bash
pip install -r requirements.txt
```
## Run Tests
1. Run all tests: ```pytest```
2. Run a single test: ```pytest tests/test_e2eTestFramework.py```
3. Generate HTML report: ```pytest --html=Reports/report.html --self-contained-html```
