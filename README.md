# Overview
This tool is a fork of a respository from Ben Edwards. The original repository has not been updated since 2017 and includes deprecated code. Thereforce, DCS has created its own copy of the code and will maintain it within this repo. The decision whether to share our changes has not been made yet, so until then this code is private to DCS only.


# Salesforce Switch

Django application designed to run on Heroku for disabling and enabling Salesforce automations (Workflows, Process Flows, Validation Rules and Triggers)

## Setup

To set this up on your own Heroku account, this app does require some knowledge of deploying Django apps. The following Heroku apps are required:
- Heroku Postgres (or alternative database)
- Redis To Go (or Heroku Redis - but might require some minor changes)

Local computers must have:
- Homebrew
- PostgreSQL 9.4+

This app uses a common web framework called Django. Django allows us to easily create models and views. It is similar to Rails for Ruby or Play for Java. Commands below are run in the terminal or shell.

Note: As of Jan 2021, this code uses Python 2.7, which is deprecated. Since it has open security issues but is not longer maintained, we must upgrade this app to use Python 3 before allowing other users. Moreover, we will upgrade Django and take advantage of many new features instroduced after version 1.6.

## Running Locally
### Install Requirements
#### Virtual Environments
First, ensure you have a tool for managing virtual environments. If not, we recommend running:
```brew install pyenv-virtualenv```

[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) is a pyenv plugin that provides features to manage virtualenvs and conda environments for Python on UNIX-like systems.

List all available virtual environments.
```pyenv virtualenvs```

Check that the virtual environment you want to use exits. If not, create it.

To create or activate a virtual environment, run:
```pyenv activate <name of environment>```

For example
```pyenv activate 2.7.14/envs/my-virtual-env-2.7.14```

#### Proxy Connection for OAuth
OAuth requires a callback URL that is reachable by the Salesforce server. Thus, we need to open a connection on the local computer for the server to the webserver to use. A simple way is to use a proxy that will create a web accessible URL for the local web server and forward all requests to it.

Run: 
```brew cask install ngrok```

#### Celery
[Celery](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html) is a distributed task queue that allows long-running processes to be executed in the background, asynchronously. Celery should be installed automatically when other dependencies are installed

Note: While the web server automatically restarts if you make changes, Celery does not. Be sure to restart Celery after making any changes to the tasks.py file or Celery configuration.

#### Install Redis
[Redis](https://redis.io/download) acts as a broker between the web app and Celery, which processes background tasks. Tasks are created by the web server, then sent to Redis. Celery pulls tasks from Redis for execution as worker processes become available. In production, Redis runs on a server separate from the web app or Celery but it can be on the same machine for local development.

#### Update Local Connection Details
The project must connect to a database. Update credentials for a PostgreSQL server in `settings.py`.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<REPLACE_WITH_DB_NAME>',
        'USER': '<REPLACE_WITH_DB_USERNAME_>',
        'PASSWORD': '<REPLACE_WITH_DB_PASSWORD>',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
#### Install Project Dependencies
Install all the dependencies in the virtual environment
```pip install -r requirements.txt```

### Create Tables in Database
For Python 2.7.x ONLY:

Create all the tables in the database by running:
```python manage.py syncdb```

For Python 3+ ONLY:
Create all the tables in the database by running:
```python manage.py migrate```

### Start the Local Web Server, Celery, and Redis
Start the proxy connection:
```ngrok http 8000```

Copy the URL and paste it in the LOCAL_PROXY_URL field in `settings.py`.

Start the web server:

```python manage.py runserver```

Start Redis:
```redis-server```

Start Celery:
```celery -A enable_disable.tasks worker```






# Production
TODO


# License
This repository does not have an explicit license but other features in the Cloud Toolkit project have been released under http://unlicense.org/