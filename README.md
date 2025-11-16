# Name Entity Recognition (NER) analyzer

![Python](https://img.shields.io/badge/python-3.11-blue.svg)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![license](https://img.shields.io/badge/licence-MIT-green.svg)](https://opensource.org/licenses/MIT)

This project is a simple example for NER tagging task in NLP. Based on Natasha library. 

You can enter text and get text with tagged entities. Standart named entities are extracted: names, locations, organizations.

The web server is based on Flask framework. By default the application will run on port 5000.

## Setting up and running the project 🚀

### Prerequisites
Clone repository:
```bash 
git clone https://github.com/Nkeramov/ner_analyzer.git
```
Switch to repo directory:
```bash 
cd ner_analyzer
```
### Traditional method with venv and pip
Create and activate virtual environment:
```bash 
python -m venv .venv 
source .venv/bin/activate       # Linux/Mac
# or
./venv/Scripts/activate         # Windows
```
Install dependencies and run:
```bash
pip install -r requirements.txt
python main.py
```
### Modern method with uv
Install dependencies and create virtual environment automatically:
```bash
uv sync
```
Run the project (virtual environment is handled automatically):
```bash
uv run python main.py
```
Or with explicit activation:
```bash
source .venv/bin/activate       # After uv sync
python main.py
```
