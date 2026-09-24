# Sticky Notes Application

A Django-based web application for creating, editing, and managing sticky notes.

## Features
- Create, read, update, and delete sticky notes
- Clean and simple user interface
- SQLite database storage
- Fully documented with Sphinx
- Docker containerized for easy deployment

## Installation

### Option 1: Virtual Environment
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`
7. Visit http://localhost:8000

### Option 2: Docker
1. Build image: `docker build -t sticky-notes-app .`
2. Run container: `docker run -p 8000:8000 sticky-notes-app`
3. Visit http://localhost:8000

## Documentation
Sphinx docs are in `docs/_build/html/`.

## Technologies
- Python 3.12
- Django 5.1
- SQLite
- Sphinx
- Docker