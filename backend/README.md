# Backend Services & Projects

This directory contains Python backend implementations developed with **Flask** and **Django**, ranging from foundational HTTP handling and authentication to database-backed CRUD applications and production-ready blog platforms.

---

## Architecture & Directory Overview

```text
backend/
├── 01_flask_basics/               # Core Flask: routes, URL variable rules, HTTP methods
├── 02_flask_sqlite_auth/          # Session-based authentication with raw SQLite3 & Werkzeug
├── 03_flask_template_routing/     # Jinja2 template inheritance, dynamic routes, layout base
├── 04_flask_crud_app/             # Full CRUD operations with Flask-SQLAlchemy
├── 05_flask_sqlalchemy_auth/      # Secure user authentication with Flask-SQLAlchemy & Bcrypt
├── 06_django_basics/              # Django core architecture, apps, models, admin, views
├── 07_django_blog/                # Full-featured Django blog application
├── 08_django_blog_deployment/     # Production-configured Django blog with Render deployment
├── python_notebooks/              # Python recap & reference Jupyter notebooks
├── django_exam_prep/              # Practice projects (Forms, ORM, Auth, Storefront)
├── Procfile                       # Gunicorn web process definition
└── requirements.txt               # Backend dependencies
```

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- `pip` (Python package manager)

### 2. Environment Setup
Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running Applications

### Flask Applications
Navigate to the desired Flask module and run the entry file:

```bash
# Example: Running the CRUD app
cd 04_flask_crud_app
python app.py
```
By default, Flask applications run on `http://127.0.0.1:5000` (or the port defined in `app.run()`).

### Django Applications
Navigate to the Django project root (containing `manage.py`):

```bash
# Example: Running the 07_django_blog app
cd 07_django_blog

# Apply database migrations
python manage.py migrate

# Create an administrator account (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```
The Django application will be accessible at `http://127.0.0.1:8000`.
