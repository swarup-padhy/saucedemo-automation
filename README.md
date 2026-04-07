# 🛒 SauceDemo — Selenium Automation Framework

> A production-grade UI test automation framework built with Selenium WebDriver, pytest, and Allure Reports. Covers the complete e-commerce purchase flow using the Page Object Model (POM) architecture.

---

![Python](https://img.shields.io/badge/Python-3.14.3-blue?style=flat-square&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.41.0-green?style=flat-square&logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-9.0.2-orange?style=flat-square&logo=pytest)
![Allure](https://img.shields.io/badge/Allure-2.15.3-yellow?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-21%20Passed-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)

---

## 📌 Project Overview

| Field | Detail |
| :--- | :--- |
| **Application Under Test** | [SauceDemo](https://www.saucedemo.com) — E-commerce practice site |
| **Framework** | Selenium WebDriver + pytest + POM |
| **Reporting** | Allure Reports |
| **Language** | Python 3.14.3 |
| **Architecture** | Page Object Model (POM) |
| **Test Types** | Functional · Negative · End-to-End |

---

## ✅ Test Coverage

| Module | Test Cases | Markers |
| :--- | :---: | :--- |
| 🔐 Login | 5 | smoke + regression |
| 📦 Inventory | 3 | smoke + regression |
| 🛒 Cart | 4 | smoke + regression |
| 📋 Checkout Form | 6 | smoke + regression |
| 🔄 End-to-End Flow | 3 | smoke + regression |
| **Total** | **21** | |

---

## 🏗️ Framework Architecture

```
saucedemo-automation/
│
├── pages/                          ← Page Object Model layer
│   ├── login_page.py               ← Login page actions and locators
│   ├── inventory_page.py           ← Product listing page
│   ├── cart_page.py                ← Shopping cart page
│   ├── checkout_page.py            ← Checkout form page
│   ├── checkout_overview_page.py   ← Order summary page
│   └── checkout_complete_page.py   ← Order confirmation page
│
├── tests/                          ← Test suites
│   ├── test_login.py               ← Login functional + negative tests
│   ├── test_inventory.py           ← Product and cart badge tests
│   ├── test_cart.py                ← Cart management tests
│   ├── test_checkout.py            ← Form validation tests
│   └── test_complete_flow.py       ← Full e2e purchase flow
│
├── utils/
│   └── test_data.py                ← Centralized test data
│
├── conftest.py                     ← Fixtures: driver, logged_in_driver
├── pytest.ini                      ← pytest config + markers
└── requirements.txt                ← Project dependencies
```

---

## 🔗 How the Framework Connects

```
conftest.py          → Creates browser, manages setup/teardown
     │
     ▼
tests/               → Imports page objects, calls actions, asserts results
     │
     ▼
pages/               → Finds elements, performs actions (never asserts)
     │
     ▼
utils/test_data.py   → Supplies test credentials and form data
```

---

## ⚡ Quick Start

**1. Clone the repository**
```bash
git clone https://github.com/swarup-padhy/saucedemo-automation.git
cd saucedemo-automation
```

**2. Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run tests**
```bash
# Full suite
python -m pytest tests/ -v

# Smoke tests only
python -m pytest -m smoke -v

# Regression tests only
python -m pytest -m regression -v
```

**5. Generate Allure report**
```bash
allure serve reports
```

---

## 📊 Test Markers

| Marker | Purpose | Count |
| :--- | :--- | :---: |
| `smoke` | Critical path — run first, fast feedback | 8 |
| `regression` | Full coverage — run after smoke passes | 13 |

```bash
python -m pytest -m smoke -v       # 8 tests — ~37 seconds
python -m pytest -m regression -v  # 13 tests — ~61 seconds
python -m pytest tests/ -v         # 21 tests — ~98 seconds
```

---

## 🧰 Key Design Decisions

**Page Object Model**
Every page has its own class. Locators and actions live in the page file. Tests only call methods and assert — they never contain locators.

**Fixture Layering**
Two fixtures in `conftest.py`:
- `driver` — fresh browser for tests that start from scratch (login tests)
- `logged_in_driver` — pre-authenticated browser for tests that start after login

**Centralized Test Data**
All usernames, passwords, and form data live in `utils/test_data.py`. One change updates every test that uses it.

**DRY Principle**
Repeated setup steps extracted into fixtures. No test contains more code than it needs.

---

## 🌐 Test Users

SauceDemo provides built-in test users — all use the same password `secret_sauce`:

| Username | Behaviour |
| :--- | :--- |
| `standard_user` | Normal user — full access |
| `locked_out_user` | Blocked — cannot login |
| `problem_user` | UI bugs present |
| `performance_glitch_user` | Slow page loads |
