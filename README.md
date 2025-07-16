# TodoApp

A modern, user-friendly Django application for managing personal todos and tasks.  
Features include user authentication, CRUD for tasks, Bootstrap dashboard UI, and filtering/search.

---

## Features

- User registration and login (Django built-in authentication)
- Create, read, update, and delete your own todos
- Responsive Bootstrap dashboard with stats and filters
- Task search, status toggle, and due dates
- Admin interface for managing users and tasks

---

## Getting Started

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd <project-folder>
```



### 2. Install Dependencies


```sh
pip install django django-crispy-forms crispy-bootstrap4
```

### 3. Apply Migrations

```sh
python manage.py migrate
```

### 4. Create a Superuser (Admin)

```sh
python manage.py createsuperuser
```

### 5. Run the Development Server

```sh
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## Usage

- Register a new user or log in with your superuser account.
- Create, update, and manage your todos from the dashboard.
- Use the admin panel at `/admin/` for advanced management.

---

## Project Structure

```
todoapp/           # Django project config
main/              # Main app (tasks, dashboard)
authentication/    # User registration and login
templates/         # HTML templates
static/            # Static files (CSS, JS)
manage.py
db.sqlite3
requirements.txt
```




