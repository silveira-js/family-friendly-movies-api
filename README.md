# Family Friendly API

Assists parents in finding suitable movies for children.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

This API provides access to a collection of family-friendly movies sourced from The Movie Database (TMDb). It allows users to retrieve a list of family-friendly movies and paginate through the results.

## Features

- Retrieve a list of family-friendly movies
- Pagination support for navigating through the movie list
- Integration with The Movie Database (TMDb) API
- Endpoint to create and manage movies and watchlists

## Installation
DISCLAIMER: This local setup was tested on MacOS, it should work on most Unix systems as well.

#### Requirements
- [Visual Studio Code](https://code.visualstudio.com/) editor
- [Docker](https://www.docker.com/get-started/) for your operating system
- [Git](https://git-scm.com/downloads)

#### 1. Remote Container

- The project is intended to be developed inside a containerized development environment using Visual Studio Code [Remote - Containers extension](https://code.visualstudio.com/docs/remote/containers). More information on how to develop using containers is available [here](https://www.youtube.com/watch?v=KFyRLxiRKAc).

- To use the development IDE, open the project folder with VS Code and press 'F1', then search for: 'Remote-Containers: Rebuild and Reopen in Container'.
VS Code should reopen your IDE inside the dev container, which should make you ready to start developing!

- Rebuild and Reopen in Container should create a Django service on [localhost:8000](http://localhost:8000/)

#### 2. Set up your TMDb API key:

- Obtain an API key from [TMDb](https://www.themoviedb.org/documentation/api)
- Add your API key to the `TMDB_API_KEY` variable in `settings.py`

** For practicality, you will find a working key in .envs/.local/.django;

#### 3. Setting Up Your User
  
- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

## API
-  After create superuser, retrieve the token, passing the body to the request:

POST  ```/api/auth-token/```  

```
{
    "username": <username>,
    "password"": <password>
}
```

-  You must add token authorization to every request:  

```
{
    "Authorization": "Token <token>"
}
```

### 1. Retrieving Family Friendly Movies
To retrieve a list of family-friendly movies, send a GET request to the following endpoint:

GET ```/api/movies/family_friendly/```


#### Pagination

Pagination is supported for navigating through the movie list. You can specify the page number as a query parameter:

GET ```/api/movies/family_friendly/?page=<page_number>```

### 2. Watchlist

Users can add or remove movies to their watchlist by sending a POST request to the following endpoint:

POST ```/api/watchlists/<list_id>/add_movie/<tmdb_id>```

POST ```/api/watchlists/<list_id>/remove_movie/<tmdb_id>```


### 3. Access API Documentation
- For further information about all endpoints, a swagger page will be available at:
```
http://localhost:8000/api/docs/
```




## Future Improvements

- Implement filtering options based on movie attributes such as genre, release year, and rating.
- Add authentication and authorization mechanisms to restrict access to certain endpoints.
- Improve error handling and provide informative error messages to API consumers.
- Implement caching mechanisms to improve performance and reduce the number of requests to TMDb API.
