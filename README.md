# Selenium with Python E-Commerce Framework (Study Pack)

This is a cleaned study version of your GitHub project, organized so you can revise quickly.

## What it includes
- **pytest** test runner
- **Page Object Model**: `pageObjects/`
- **Test data**: `data/test_e2eTestFramework.json`
- **Screenshot on failure** + **HTML report** (pytest-html)

## Quick start
```bash
pip install -r requirements.txt
pytest -m smoke --html=Reports/report.html --self-contained-html
```

## Folder map
- `tests/` – test cases + `conftest.py` fixture
- `pageObjects/` – Login, Shop, Checkout Confirmation pages
- `utils/` – small helper (`BrowserUtils`)
- `data/` – JSON test data
- `Reports/` – HTML report + screenshots
