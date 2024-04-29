# Family Friendly API

Assists parents in finding suitable movies for children.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Local Setup
DISCLAIMER: This local setup was tested on MacOS, it should work on most Unix systems as well.

### Requirements
- [Visual Studio Code](https://code.visualstudio.com/) editor
- [Docker](https://www.docker.com/get-started/) for your operating system
- [Git](https://git-scm.com/downloads)

### Remote Container

The project is intended to be developed inside a containerized development environment using Visual Studio Code [Remote - Containers extension](https://code.visualstudio.com/docs/remote/containers). More information on how to develop using containers is available [here](https://www.youtube.com/watch?v=KFyRLxiRKAc).

To use the development IDE, open the project folder with VS Code and press 'F1', then search for: 'Remote-Containers: Rebuild and Reopen in Container'.
VS Code should reopen your IDE inside the dev container, which should make you ready to start developing!

Tests should be available in the Testing tab (troubleshooting below).

Rebuild and Reopen in Container should create:

- A Django service on [localhost:8000](http://localhost:8000/)

## Basic Commands

### Setting Up Your User
- To connect with the TMDb API, an API KEY is needed and loaded as an environment variable. For practicality, you will find a working key in .envs/.local/.django;
  
- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

## API
-  After create superuser, retrieve the token, passing the body to the request:

[POST]  ```/api/auth-token/```  

```
{
    "username": <username>,
    "password"": <password>
}
```

### Access API Documentation
- For further information about all endpoints, afger building, a swagger page will be available at:
```
http://localhost:8000/api/docs/
```

### You must add token authorization to every request:  

```
{
    "Authorization": "Token <token>"
}
```


### Running tests with pytest

    $ pytest


