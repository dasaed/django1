# Crash Course in DJANGO

### Steps to setup
0. Go to the folder where you want to create your project
1. Create virtual environmnet
  * virtualenv -p python3 .

2. Activate the virtual environment 
  * source ./bin/activate

3. Install the django version we are going to use
  * pip install django=2.0.7
  * This isn't the latest version, but it's the one I'm going to use. I will update this version later on


### Creating a sample project

1. Create a source folder within your virtual environment, to keep your django packages

2. mkdir src && cd src

3. django-admin startproject oilgashackathonpractice . 

4. Start the django server
   python manage.py runserver


### Checking out the settings file
When you create a new project, django will automatically import the os library as it works with any OS
BASE\_DIR = The directory where the manage.py script for the project is
SECRET\_KEY = It's a private key, don't share in production servers
DEBUG = True # In production servers, you will want to set this to false

INSTALLED\_APPS = List of products that you might have for your project, but this refers more to the components in your project.
MIDDLEWARE = This has to do with how your requests and security is handle.
ROOT\_URLCONF = This is how django knows how to route any URL
TEMPLATES = templates that django work with. Basically where your html code will essentially go

WSGI\_APPLICATION = how your server works

DATABASES = django maps realy well to databases, and django by default creates a sqllite database

AUTH\_PASSWORD\_VALIDATORS = checks that passwords are good according to django's standards

STATIC\_URL = where you store your CSS and javascript. 

Side Note 
*  To prevent the initial error when running the server for the first time (i.e.  python manage.py runserver), run:
  *  python manage.py migrate
  *  This will sync django and the database

