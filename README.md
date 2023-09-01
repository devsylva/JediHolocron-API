# JediHolocron-API
Welcome to the documentation for JediHolocron API! This guide provides developers with necessary information on how to interact with our API and integrate it into their applications.

# Overview
The JediHolocron API is built with Django Rest Framework (DRF) and provides awesome features for fetching films from the Star Wars open API and also performs other CRUD operations and background tasks.


# Tech Stack
- Language: Python 3.11.3
- Framework: django
- Database: PostgreSQL
- Version Control: Git
- Hosting/Deployment: Heroku
- Authentication and Authorization: JSON Web Token (JWT)


# System Architecture
![Untitled Diagram drawio](https://github.com/devsylva/JediHolocron-API/assets/67736638/f2b770ba-9b48-435f-ab52-fdf7d089e429)


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

on macOS and Linux
```
source venv/bin/activate
```

on windows
```
venv\Scripts\activate
```

4. Install dependecies.

```
pip install -r requirements.txt
```

5. Change `.env.templates` in the jediholocron directory to `.env`. Then provide the requierd data specifiedd.

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


## User Authentication
Authentication is required for most endpoints in the API. To authenticate, include an access token in the `Authorization` header of your request. The access token can be obtained by logging into your account.

The following endpoints are available in the API:

-   `api/auth/signup/` (POST): to allow users register an account.  
-   `api/auth/login/` (POST): to allow users to log in into their account.
-   `api/auth/login/refresh/` (POST): to allow user refresh to get their access token after it expires.
-   `api/auth/logout/` (POST): to allow users to log out of their account.
-   `api/auth/change_password/` (POST): to allow users change there account password.


## Core Application Endpoints
Kindly note that all the endpoints provided below requires authentication, hence kindly provided your access token generated during your login  and include the token in the `Authorization` header of your request. e.g `Authorization: Bearer <your_access_token>` 

The following endpoints are available in the API:

-   `api/films/` (GET):  allows authenticated users view all films.
-   `api/film/<int:id>/` (GET): allows authenticated users view a particular film with a valid id.
-   `api/comments/` (GET):  allows authenticated users view comments for all films.
-   `api/comment/<int:id>/` (GET): allow authenticated users view a particular comment with a valid id.
-   `api/comments/` (POST): allow authenticated users create a comment for a partifular film.
-   `api/comment/<int:id>/` (PUT): allows authenticated users to update their comment.
-   `api/comment/<int:id>/` (DELETE): allows authenticated users delete their comment.



## Automatic Film Data Update from External API

In this section, we will cover how i implemented a function to automatically update film data from the Star Wars API using Django's `django-crontab` package. This feature ensures that your film database stays up-to-date with the latest information from the external source.

### Background

Maintaining accurate and current film data is crucial for this application. To achieve this, i had to integrate a mechanism to periodically fetch and update film records from the Star Wars API.

### Updating Function: `update_film_data`

The `update_film_data` function is responsible for fetching film data from the external API and updating your database accordingly. This function is designed to be executed at specified intervals, ensuring that your film records remain current.

#### Implementation Details

Here's an overview of how the `update_film_data` function works:

1. The function sends an HTTP request to the external API to fetch the latest film data.
2. It receives the API response, which typically contains a list of film records.
3. The function iterates through the fetched film records and processes each entry.
4. For each film, it checks whether the film already exists in your local database based on a unique identifier `ID`.
5. If the film exists, the function updates the relevant fields (e.g., release date, title, etc) to reflect the latest information.
6. If the film is not found, the function creates a new film record using the fetched data.

#### Scheduling the Update

i configured the `update_film_data` function to run automatically using Django's `django-crontab` package. The function is scheduled to run every midnight, ensuring that your film database is updated daily.


#### Extracting Film ID from URL

To smartly retrieve the film's ID from the URL provided by the external API, you have employed a parsing strategy. You iterated over the URL to extract the necessary ID component, which uniquely identifies the film. This clever approach allows you to match external film data with your local records efficiently.

```
def handle(self, *args, **options):
        response = requests.get('https://swapi.dev/api/films') 
        data = response.json()
        film_data = data["results"]
        for i in film_data:
            film, created = Film.objects.update_or_create(
                # get film id from the url endpoint
                id=int(i['url'][28:-1]),
                defaults={
                    'title': i['title'],
                    'release_date': i['release_date'],
                }
            )
```


## Conclusion

The automatic film data update functionality, scheduled to run every midnight using `django-crontab`, is a valuable addition to the Film API. This ensures that the application's film records are always up-to-date with the latest information from the external API. By periodically fetching and processing new data, i enhanced the accuracy and reliability of the film database.

# License

This project is licensed under the MIT License - [LICENSE](LICENSE) file for details.
