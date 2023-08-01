[![tests-and-linter-check](https://github.com/Acemore/YLab_University_python_intensive_project_tests/actions/workflows/tests_and_linter.yml/badge.svg?branch=main)](https://github.com/Acemore/YLab_University_python_intensive_project_tests/actions/workflows/tests_and_linter.yml)

### To run tests for [**Menu app**](https://github.com/Acemore/YLab_University_python_intensive_project)

[Run Menu app](https://github.com/Acemore/YLab_University_python_intensive_project#to-run-menu-app) 

Clone repo

```bash
git clone git@github.com:Acemore/YLab_University_python_intensive_project_tests.git
```

Create .env file in root project dir and add the following line

```
LOCAL_URL='http://127.0.0.1:8000'
```

Install dependencies

```bash
python -m pip install poetry
poetry install
```

Run tests

```bash
poetry run pytest tests/*
```

