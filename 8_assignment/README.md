# Django Blog Assignment

A simple blog application built with Django. Users can sign up, log in, create posts with optional images, and view post details. The admin user can view all posts, while regular users see only their own posts on the home page.

## Features

- User registration and authentication
- Create blog posts with optional images
- Post list and detail views
- Django admin for content management

## Tech Stack

- Python 3.10+
- Django 5.1
- SQLite (local development)

## Getting Started

### 1) Create and activate a virtual environment

```bash
py -3.10 -m venv .venv
```

```bash
.venv\Scripts\activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Apply migrations

```bash
python manage.py migrate
```

### 4) (Optional) Create a superuser

```bash
python manage.py createsuperuser
```

### 5) Run the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Live Demo

- https://django-assignment-3-rsxl.onrender.com

## Useful Routes

- Home: `/`
- Sign up: `/signup/`
- Log in: `/accounts/login/`
- Create post: `/create/`
- Admin: `/admin/`

## Environment Variables (Optional)

- `SECRET_KEY`: Django secret key (defaults to a local value if not set)
- `DEBUG`: `True` or `False` (defaults to `True`)
- `PERSISTENT_DISK`: Path for persistent storage (used for Render deployments)

## Notes

- Uploaded images are stored in `media/post_images/` during local development.
- SQLite database file is `db.sqlite3` in the project root.
