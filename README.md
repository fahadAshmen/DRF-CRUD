
# DRF-CRUD
REST API CRUD with Custom User Model and Django Rest Knox

This project is a REST API CRUD (Create, Read, Update, Delete) implementation using Django and Django Rest Framework (DRF).
It includes a custom user model with roles for Manager, Doctor, and Patient, user authentication using Django Rest Knox,
and the ability for authenticated users to create and manage their to-do tasks. Generic views and customized permissions from DRF are also utilized in this project.

Features
* Custom User Model: The project features a custom user model with roles for Manager, Doctor, and Patient, allowing for role-based access control.
* Authentication: User authentication is handled using Django Rest Knox, providing token-based authentication for secure API access.
* CRUD Operations: The API supports CRUD operations, allowing users to create, read, update, and delete their to-do tasks.
* Generic Views: Generic views from Django Rest Framework are leveraged to simplify API endpoints for common operations.
* Customized Permissions: Permissions in DRF are customized to control access to different API endpoints based on user roles.
* Have used PostgreSQL for database operations
* Testing with Postman: You can use Postman to test the API endpoints. Import the provided Postman collection to get started with testing.## Acknowledgements

* Django
* Django Rest Framework
* Django Rest Knox
## Deployment

To clone this project run

```bash
  git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

Create a virtual environment (optional but recommended)

```bash
python -m venv env
env/bin/activate  # On Windows
```

Install the project dependencies:
```bash

pip install -r requirements.txt
```

Migrate the database:
```bash
python manage.py makemigrations
python manage.py migrate
```
Create a superuser account to access the admin panel:

```bash
python manage.py createsuperuser
```
Start the development server:
```bash
python manage.py runserver
```




## API Reference

#### For Create-user or update-user

```http
  locatlhost/api/create-user/
  locatlhost/api/update-user/<int:pk>/
```
#### For Authentication
```http
  locatlhost/api/login/
  locatlhost/api/logout/
  locatlhost/api/logout-all/
```
#### For To-do

```http
  locatlhost/api/todo/
  locatlhost/api/todo-details/<int:pk>/
 ```



