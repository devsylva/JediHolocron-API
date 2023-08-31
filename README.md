# JediHolocron-API
Welcome to the documentation for JediHolocron API! This guide provides developers with necessary information on how to interact with our API and integrate it into their applications.

# Overview
The JediHolocron API is built with Django Rest Framework (DRF) and provides awesome features for fetching films from the Star Wars open API and also performs other CRUD operations and background tasks.


# Tech Stack
- Language: Python 3.11.3
- Framework: Django and Django Rest Framework 
- Database: PostgreSQL



# ER-Diagram
![Jediholocron](https://github.com/devsylva/JediHolocron-API/assets/67736638/51210bae-3e4a-4750-9f6d-8a34d3525839)


# Getting Started

To run the API locally, follow these steps:

1. Clone this repository.

```
git clone https://github.com/devsylva/JediHolocron-API.git
```

2. Create a virtual environment inside the project directory.

```
python -m venv venv
```

3. Activate the virtual environment.

```
source venv/bin/activate
```

4. Install dependecies.

```
pip install -r requirements.txt
```

5. Change `.env.templates` in the `jediholocron` directory to `.env`. Then provide the requierd data specifiedd.

6. Set up the database.

```
python manage.py migrate
```

7. Create a superuser/admin account.

```
python manage.py createsuperuser
```

8. Start the development server.

```
python manage.py runserver
```


# Running tests

Here's how to run tests.

- To run all the tests, use the following command

```
python manage.py test
```


# Functional Requirements Definition

Functional requirements specify the actions that a software system or application should take to satisf the user's needs and business objectives. They describe the system's functions, features, and capabilites, as well as how it should respond under different circumstances

### User Authentication
The API should provide a user registration and login including password recovery features. We'll ensure that passwords are securely stored and hashed using Django's built-in Authentication system.

### Film Storage and Organization
The API should provide an effective pattern for fetching Film data from the provided Star Wars API endpoint in other to store the film's id, title, release date and comment count in our database. Films should be sorted in ascending order with respect to their release date, Also users shouldbe able to comment on film(s), hence provide endpoint for listing comments made to film(s) also in ascending order with respect to their creation time.