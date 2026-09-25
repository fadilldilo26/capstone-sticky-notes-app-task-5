# Sticky Notes Application

A Django-based web application for creating, editing, and managing sticky notes.

## Features

- Create, read, update, and delete sticky notes
- Clean and simple user interface
- SQLite database storage
- Fully documented with Sphinx
- Docker containerized for easy deployment

## Installation

You can run this project using a standard Python environment or via Docker.

### Option 1: Virtual Environment (Local)

1. Clone the repository:
```bash
   git clone <your-repo-url>
   cd capstone-sticky-notes-app
```

2. Create a virtual environment:
```bash
   python -m venv venv
```

3. Activate the environment:
   - **Windows:** `venv\Scripts\activate`
   - **Mac/Linux:** `source venv/bin/activate`

4. Install dependencies:
```bash
   pip install -r requirements.txt
```

5. Run migrations:
```bash
   python manage.py migrate
```

6. Start the server:
```bash
   python manage.py runserver
```

7. Visit [http://localhost:8000](http://localhost:8000)

### Option 2: Docker (Recommended)

This method ensures all system dependencies (like `mysqlclient`) are handled automatically.

1. **Build the Docker image:**
```bash
   docker build -t sticky-notes-app .
```

2. **Run the container:**
```bash
   docker run -p 8000:8000 sticky-notes-app
```
   *(Note: If you need to run migrations inside the container, use: `docker run sticky-notes-app python manage.py migrate`)*

3. **Visit the app:**
   Open your browser and go to [http://localhost:8000](http://localhost:8000)

## Documentation

This project uses Sphinx for API documentation.

- **Source files:** Located in the `/docs` folder.
- **Generated HTML:** After running `make html` inside the `/docs` folder, the output is available at `docs/_build/html/index.html`.

## Technologies

- **Python** 3.12
- **Django** 5.1
- **SQLite**
- **Sphinx** (Documentation)
- **Docker** (Containerization)