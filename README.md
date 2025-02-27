# Student-Report-Card-Management-System
A Django-based student report system managing 210 students across 5 departments with 5-6 subjects each. Features search, ranking automation, clickable student profiles, and bulk report card generation via admin panel.

#Student Report Card Management System

#Description

A Django-based student report system managing 210 students across 5 departments with 5-6 subjects each. Features search, ranking automation, clickable student profiles, and bulk report card generation via the admin panel.

#Tech Stack

-Backend: Django, Python

-Frontend: HTML, CSS, Bootstrap

-Database: Django’s built-in SQLite

#Features

✅ Admin dashboard for bulk report card generation
✅ Search & filter students by ID or department
✅ Clickable student profiles displaying marks, total score, rank, and creation date
✅ Pagination for efficient browsing
✅ Department-wise categorization

#Installation Guide

Clone the repository:

git clone <repo-link>
cd student-report-card

#Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate

#Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

#Start the development server:

python manage.py runserver

Open in browser: http://127.0.0.1:8000/

