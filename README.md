## Overview

A full-stack E-commerce web application built using Django (Python) for the backend and HTML, CSS, and JavaScript for the frontend.

The system allows users to browse products, view details, add items to a shopping cart, register/login, and place orders. An admin panel is included for product and order management.

## Features

Product listing and detail pages

Shopping cart (session-based)

User registration & authentication

Order processing system

Django admin panel

SQLite database integration

## Tech Stack

Backend: Django (Python)

Frontend: HTML, CSS, JavaScript

Database: SQLite

## Project Architecture
ecommerce_project/
│
├── ecommerce_app/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── ecommerce_project/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── db.sqlite3

## Setup Instructions
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

## Visit:
http://127.0.0.1:8000/
Admin: http://127.0.0.1:8000/admin/

## Future Enhancements

--> Payment gateway integration (Stripe / Khalti / eSewa)

--> Product categories & filtering

--> Search functionality

--> Order history dashboard

--> REST API integration

--> Deployment using Docker

--> Cloud hosting (Render / PythonAnywhere / AWS)
