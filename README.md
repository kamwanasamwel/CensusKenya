# Getting Started

The steps outlined have been adopted from [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04).
The project is based on Python 3.6 so it's recommended that your environment is set to that to maintain consistency

## Install the Packages from the Ubuntu Repositories
To begin the process, we'll download and install all of the items we need from the Ubuntu repositories. We will use the Python package manager `pip` to install additional components a bit later.
Since we are using Django with Python 3, type:

```
sudo apt-get update

sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
```
This will install pip, the Python development files needed to build Gunicorn later, the Postgres database system and the libraries needed to interact with it, and the Nginx web server.

## Create the PostgreSQL Database and User
Log into an interactive Postgres session by typing:
```
sudo -u postgres psql
```
You will be given a PostgreSQL prompt where we can set up our requirements.

First, create a database for our project:
```
CREATE DATABASE censuskenya;
```
Next, create a database user for our project. Make sure to select a secure password:

```
CREATE USER censususer WITH PASSWORD 'amcountingall';
```

We are going to set the default encoding to `UTF-8`, which Django expects. We are also setting the default transaction isolation scheme to "read committed", which blocks reads from uncommitted transactions. Lastly, we are setting the timezone. Our Django projects will be modified to use `Africa/Nairobi`:

```
ALTER ROLE censususer SET client_encoding TO 'utf8';
ALTER ROLE censususer SET default_transaction_isolation TO 'read committed';
ALTER ROLE censususer SET timezone TO 'Africa/Nairobi';
```

Now, we can give our new user access to administer our new database:
```
GRANT ALL PRIVILEGES ON DATABASE censuskenya TO censususer;
```

When you are finished, exit out of the PostgreSQL prompt by typing:
```
\q
```

## Create a Python Virtual Environment for our Project
Since we are using Python 3, create a virtual environment called `censuskenya_venv` by typing:
```
virtualenv -p python3 censuskenya_venv
```
Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:
```
source censuskenya_venv/bin/activate
```

## Clone and Configure a New Django Project
Login into your bitbucket account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:
```
git clone https://github.com/kamwanasamwel/CensusKenya
```
Next, install the requirements by typing:
```
pip install -r requirements.txt
```

## Complete Initial Project Setup
Now, we can migrate the initial database schema to our PostgreSQL database using the management script:
```
./manage.py makemigrations
./manage.py migrate
```

Create an administrative user for the project by typing:
```
./manage.py createsuperuser
```

Finally test that the project is running:
```
./manage.py runserver
```

