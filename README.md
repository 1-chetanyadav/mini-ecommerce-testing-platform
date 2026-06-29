# Mini E-Commerce Testing Platform v1.0.0

## Overview

Mini E-Commerce Testing Platform is a Python-based automation testing project developed to demonstrate API and UI automation skills using industry-standard tools and frameworks.

The project simulates a simple e-commerce application with login and product modules and includes automated test coverage for both backend APIs and frontend user interfaces.

---

## Features

* API Automation using **Pytest** and **Requests**
* UI Automation using **Playwright**
* Reusable **Pytest Fixtures**
* **Parameterized Test Cases**
* Shared configuration using **conftest.py**
* API Helper Functions
* HTML Test Reports
* Modular and scalable test structure

---

## Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Programming Language      |
| Flask        | Web Application Framework |
| Pytest       | Test Framework            |
| Requests     | API Testing               |
| Playwright   | UI Automation             |
| HTML Reports | Test Reporting            |
| Git & GitHub | Version Control           |

---

## Project Structure

```text
mini-ecommerce-testing-platform/
│
├── app.py
├── main.py
│
├── data/
│   ├── users.json
│   ├── product.json
│   └── orders.json
│
├── tests/
│   ├── conftest.py
│   ├── test_login_api.py
│   ├── test_product.py
│   ├── test_order.py
│   ├── test_login_ui.py
│   └── test_product_ui.py
│
├── utilities/
│   ├── __init__.py
│   └── api_helper.py
│
├── templates/
│   ├── login.html
│   └── product.html
│
├── reports/
│
└── README.md
```

---

## Modules Covered

### Login Module

#### API Test Scenarios

* Valid Login
* Invalid Username
* Invalid Password
* Empty Username
* Empty Password

#### UI Test Scenarios

* Successful Login
* Invalid Login Validation

---

### Product Module

#### API Test Scenarios

* Valid Product Retrieval
* Invalid Product ID Validation

#### UI Test Scenarios

* Product Search Validation
* Invalid Product Validation

---

## Framework Concepts Implemented

### Pytest Fixtures

Reusable test setup and test data management.

Example:

```python
@pytest.fixture
def app_url():
    return "http://127.0.0.1:5000"
```

---

### Parametrization

Execute a single test with multiple datasets.

```python
@pytest.mark.parametrize(
    "username,password,status_code",
    [
        ("", "rocky123", 400),
        ("rocky", "", 400)
    ]
)
```

---

### Helper Functions

Reusable API request methods to reduce code duplication and improve maintainability.

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd mini-ecommerce-testing-platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

Application runs on:

```text
http://127.0.0.1:5000
```

---

## Running Tests

Run all tests:

```bash
pytest -v
```

Run API tests:

```bash
pytest tests/test_login_api.py -v
```

Generate HTML Report:

```bash
pytest --html=reports/report.html
```

---

## Sample Report

The project supports HTML-based execution reports for easier analysis and debugging.

---

## Future Improvements

* Logging Integration
* Database Validation
* CI/CD Integration using GitHub Actions
* Advanced Automation Framework Design
* Page Object Model (POM)
* API Schema Validation

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

* REST API Testing
* UI Automation
* Test Framework Design
* Pytest Advanced Features
* Browser Automation
* Debugging Automation Failures
* Test Data Management
* Reusable Automation Architecture

---

## Author

**Chetan Yadav**

BCA (Artificial Intelligence & Data Science)

Aspiring QA Automation Engineer | Python | Pytest | Playwright | API Testing
