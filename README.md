# Django To-Do Application

## Project Description
This is a simple To-Do web application built with Django. Users can create, view, complete and delete tasks.

## Features
- Add new tasks
- View all tasks
- Mark tasks as completed
- Delete tasks
- Form validation
- CSRF protection

## Technologies
- Python
- Django
- HTML
- SQLite
- python-dotenv
- Git and GitHub

## Installation

1. Clone the GitHub repository.
2. Create and activate a virtual environment.
3. Install dependencies:

   `pip install -r requirements.txt`

4. Create a `.env` file with `SECRET_KEY` and `DEBUG` variables.
5. Run database migrations:

   `python manage.py migrate`

6. Start the development server:

   `python manage.py runserver`

## Testing

The following checks were completed:

- Django system check — PASS
- Application startup — PASS
- CRUD operations — PASS
- Form validation — PASS
- CSRF protection — PASS
- HTML templates — PASS

## Security

- Secret settings are stored in environment variables.
- The `.env` file is excluded from Git.
- CSRF protection is enabled in POST forms.
- Production security settings require final verification before deployment.

## Deployment

The project is being prepared for deployment on PythonAnywhere.