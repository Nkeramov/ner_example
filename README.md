# Name Entity Recognition (NER) example

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![license](https://img.shields.io/badge/licence-MIT-green.svg)](https://opensource.org/licenses/MIT)

This project is a simple example for NER tagging task in NLP. Based on Natasha library. 

You can enter text and get text with tagged entities. Standart named entities are extracted: names, locations, organizations.

The web server is based on Flask framework. By default the application will run on port 5000.

## Setting up and running the project
Clone repository:
```bash 
git clone https://github.com/Nkeramov/ner_example.git
```
Switch to repo directory
```bash 
cd ner_example
```
Сreate new virtual environment:
```bash 
python -m venv .venv 
```
If you are using Linux or Mac activate the virtual environment with the command:
```bash 
source .venv/bin/activate
```
or if you are using Windows use the command:
```bash 
./env/Scripts/activate
```
Install dependencies from the requirements file:
```bash
pip install -r requirements.txt
```
Run with command:
```bash
python3 main.py
```
