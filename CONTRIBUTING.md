# Contributing to Sauce_Playwrigth_Pom

Thank you for considering contributing to this QA automation project! Please follow these guidelines to ensure a smooth workflow and high code quality.

## Branching Strategy

- **main**: Always stable and production-ready. Only merge tested and reviewed code.
- **feature/xyz**: For new features, test cases, or POMs. Example: `feature/add-login-tests`
- **bugfix/xyz**: For fixing bugs or test failures. Example: `bugfix/fix-login-error-message`
- **hotfix/xyz**: For urgent fixes to the main branch. Example: `hotfix/fix-broken-ci`
- **develop** (optional): For pre-release integration if the team is large.

### Workflow
1. **Create a branch** for your work:
   ```bash
   git checkout -b feature/your-feature
   ```
2. **Commit and push** your changes to your branch.
3. **Open a Pull Request (PR)** to `main` on GitHub.
4. **Request a review** from a maintainer.
5. Ensure all **CI checks pass** before merging.
6. **Do not push directly to `main`**.

## Pull Requests & Code Review
- All changes must go through a PR and be reviewed.
- PRs should have a clear description of the change.
- Link related issues if applicable.
- Ensure tests pass and code is linted (see pre-commit hooks).

## Coding Standards
- Use the Page Object Model (POM) for maintainable test code.
- Follow linting and formatting rules (black, isort, ruff, pylint).
- Add/modify tests as needed for your change.
- Add docstrings and type hints to new code.

## Running Tests & Linting
- Run tests locally before pushing:
  ```bash
  pytest --html=reports/report.html --self-contained-html
  pytest --alluredir=allure-results
  ```
- Run linting/formatting:
  ```bash
  black .
  isort .
  ruff .
  pylint sauce_demo/
  ```
- Use pre-commit hooks:
  ```bash
  pre-commit run --all-files
  ```

## Branch Protection (Recommended)
- Enable branch protection rules for `main` in GitHub settings:
  - Require PR review before merging
  - Require status checks to pass (CI)
  - (Optional) Require linear history

---

Thank you for helping make this project better! 