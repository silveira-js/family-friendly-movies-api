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

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

-  After create superuser, retrieve the token, passing the body to the request:

```
{
    "username": <username>,
    "password"": <password>
}
```


[POST]  ```/api/auth-token/```  



### Running tests with pytest

    $ pytest


