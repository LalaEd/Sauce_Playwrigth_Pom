# Sauce_Playwright_POM

A Python QA automation project using Playwright, pytest, and the Page Object Model (POM) pattern for testing the Sauce Demo web application.

## Features
- Page Object Model for maintainable test code
- Pytest for test execution and fixtures
- Playwright for browser automation
- Allure and HTML reporting
- CI/CD with GitHub Actions
- Code quality tools: black, isort, pylint, ruff

## Project Structure
```
sauce_demo/
  src/pages/      # Page Object Model classes
  src/utils/      # Utilities
  tests/          # Test cases organized by feature
  tests/test_data # Test data
```

## Getting Started

### Prerequisites
- Python 3.11+
- [Playwright browsers](https://playwright.dev/python/docs/browsers)

### Installation
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install --with-deps
```

### Running Tests
```bash
pytest --html=reports/report.html --self-contained-html
pytest --alluredir=allure-results
```

### Viewing Allure Report
```bash
allure serve allure-results
```

### Linting & Formatting
```bash
black .
isort .
ruff .
pylint sauce_demo/
```

## Contributing
- Fork the repo and create a feature branch
- Use pre-commit hooks for linting/formatting
- Add/modify tests and submit a pull request

## License
See [LICENSE](LICENSE). 