# Django social network project

## This is project for Hillel's Python course

### Structure of the project

``` bash
├── .github/workflows
│   └──ci.yml
├── config
│   ├── __init__.py
|   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core
|   ├── migrations
|   |   └── __init__.py
|   ├── __init__.py
|   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static
│  └── css
│        └── style.css
├── templates 
│   ├── core
│   │    ├── base.html
│   │    └── posts.html
│   └── users
├── users
|   ├── migrations
|   |   └── __init__.py
|   ├── __init__.py
|   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── Pipfile
└── Pipfile.lock
```

## Details

\
Continious Integration with `GitHub actions`.

``` bash
├── .github/workflows
│   └──ci.yml
```

\
Within `config` directiry are five files:

```bash
├── config
│   ├── __init__.py
|   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
```

- `__init__.py` indicates that the files in the folder are part of a Python package.
- `asgi.py` allows for an optional Asynchronous Server Gateway Interface to be run.
- `settings.py` controls our Django project’s overall settings.
- `urls.py` tells Django which pages to build in response to a browser or URL request.
- `wsgi.py` stands for Web Server Gateway Interface which helps Django serve our eventual web pages.

\
Within `core` directiry are and six files and `migrates` directory within `__init__.py` file :

```bash
├── core
|   └── migrations
|   |   └── __init__.py
|   ├── __init__.py
|   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py 
```

- `migrations` folder is where Django stores migrations, or changes to the database.
- `__init__.py` indicates that the files in the folder are part of a Python package.
- `admin.py` file is used to display  models in the Django admin panel.
- `apps.py` is a configuration file.
- `models.py` is where the models for the app are located.
- `tests.py` contains test procedures.
- `views.py` is where the views for the app are located.

\
`Static` derictory stores static files such as styles

```bash
├── static
│  └── css
│        └── style.css
```

\
`Templates` derictory stores `html` templates for all apps

```bash
├── templates 
│   ├── core
│   │    ├── base.html
│   │    └── posts.html
│   └── users
```

\
`Users` derictory repeats the structure of `core`.

\
**_Database_** is located in:

```bash
├── db.sqlite3
```

\
**_The manage.py_** file is used to execute various Django commands such as running the local web server or creating a new app.

```bash
├── manage.py
```

\
`Pipfile` and `Pipfile.lock`  are files created with virtual environment and contains required libraries.

```bash
├── Pipfile
└── Pipfile.lock
```
