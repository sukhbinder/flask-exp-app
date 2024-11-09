# flask-expense-app

[![PyPI](https://img.shields.io/pypi/v/flask-expense-app.svg)](https://pypi.org/project/flask-expense-app/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/flask-expense-app?include_prereleases&label=changelog)](https://github.com/sukhbinder/flask-expense-app/releases)
[![Tests](https://github.com/sukhbinder/flask-expense-app/actions/workflows/test.yml/badge.svg)](https://github.com/sukhbinder/flask-expense-app/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/flask-expense-app/blob/master/LICENSE)

Flask expense app 

## Installation

Install this tool using `pip`:
```bash
pip install flask-expense-app
```
## Usage

For help, run:
```bash
flask-expense-app --help
```
You can also use:
```bash
python -m flask_expense_app --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd flask-expense-app
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
