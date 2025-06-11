# Name Entity Recognition (NER) example

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![license](https://img.shields.io/badge/licence-MIT-green.svg)](https://opensource.org/licenses/MIT)

This project is a simple example for NER tagging task in NLP. Based on Natasha library. 

You can enter text and get text with tagged entities. Standart named entities are extracted: names, locations, organizations.

The web server is based on Flask framework. By default the application will run on port 5000.

## Setting up project

Сreate a virtual environment, activate it and install dependencies from the requirements file.
```bash
        python -m venv .venv
        source .venv/bin/activate           # for Linux and Mac
        ./env/Scripts/activate              # for Windows
        pip install -r requirements.txt
```

Run with command: `python3 main.py`
