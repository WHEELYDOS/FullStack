# FullStack Development Repository

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20.svg?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-v4-38B2AC.svg?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-F7DF1E.svg?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A structured, full-stack software engineering repository containing frontend UI architectures, backend web services, relational database integrations, and end-to-end applications built with modern web technologies.

---

## Repository Architecture

```text
.
├── backend/
│   ├── 01_flask_basics/               # Routing, URL variable rules, and HTTP method dispatch
│   ├── 02_flask_sqlite_auth/          # Session authentication with SQLite3 and Werkzeug hashing
│   ├── 03_flask_template_routing/     # Jinja2 templating, layout inheritance, and error handling
│   ├── 04_flask_crud_app/             # Database-driven CRUD application with Flask-SQLAlchemy
│   ├── 05_flask_sqlalchemy_auth/      # User authentication system with Flask-SQLAlchemy & Bcrypt
│   ├── 06_django_basics/              # Django application fundamentals, models, admin, and views
│   ├── 07_django_blog/                # Full-featured Django blog platform
│   ├── 08_django_blog_deployment/     # Production-ready Django app configured for Render deployment
│   ├── python_notebooks/              # Python programming notebooks and reference material
│   ├── django_exam_prep/              # Practice projects (Forms, ORM, Auth, Storefront)
│   ├── Procfile                       # Production web process declaration
│   ├── requirements.txt               # Backend Python dependencies
│   └── README.md                      # Backend documentation & run instructions
│
├── frontend/
│   ├── css/                           # Core CSS3 modules
│   │   ├── bem_methodology/           # BEM class naming conventions
│   │   ├── blog_card/                 # Responsive blog component
│   │   ├── box_model/                 # Box model mechanics (margins, padding, borders)
│   │   ├── box_shadow/                # Elevation and drop shadow styling
│   │   ├── css_variables/             # Custom properties and theming
│   │   ├── dashboard_ui/              # Multi-panel administrative dashboard layout
│   │   ├── forms/                     # Form styling and state pseudo-classes
│   │   ├── gradients/                 # Linear/radial gradients and progress bars
│   │   ├── grid/                      # CSS Grid, Subgrid, areas, and dynamic templates
│   │   ├── login_page/                # Centered login form UI
│   │   ├── mustache_art/              # Pure CSS vector drawing
│   │   ├── navbar/                    # Responsive navigation header
│   │   ├── practice_layouts/          # Flexbox container and wrapping practice
│   │   ├── product_card/              # E-commerce card component
│   │   ├── selectors/                 # Combinators, pseudo-classes, and pseudo-elements
│   │   ├── specificity/               # Specificity calculations and inheritance
│   │   └── typography/                # Web fonts (@font-face) and text hierarchy
│   ├── javascript/                    # JavaScript fundamentals & scripts
│   ├── saas_dashboard/                # Modern SaaS dashboard project workspace
│   ├── tailwind/                      # Tailwind CSS v4 implementations
│   │   ├── intro/                     # Utility-first introductory templates
│   │   ├── tailwind_starter/          # PostCSS build pipeline starter
│   │   └── tailwind_components/       # Reusable card and UI components
│   └── README.md                      # Frontend documentation & build instructions
│
├── .gitignore                         # Comprehensive Git ignore rules
└── README.md                          # Repository documentation
```

---

## Tech Stack Overview

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 (Flexbox, Grid, Subgrid, BEM), Tailwind CSS v4, JavaScript (ES6+) |
| **Backend** | Python 3.10+, Flask, Django, Jinja2, Django REST Framework |
| **Database & ORM** | SQLite3, SQLAlchemy, Flask-SQLAlchemy, Django ORM |
| **Security & Auth** | Werkzeug Security, Bcrypt, Flask Session Management, Django Auth |
| **Deployment & Ops** | Gunicorn, Render (`render.yaml`), Git |

---
