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

### Built-in Apps and some more setup steps you should definately do
Apps here are basically components of the general django project. You would add them in the INTALLED\_APPS variable inside the settings file. 
*  Create the admin user
    * Double-check that "python manage.py migrate" runs without errors
    * python manage.py createsuperuser

### My first custom app(django component) 
Remember that apps should be very narrow and focus on specific components. An app shouldn't have to handle too many things, and for example a car app should have nothing to do with the sales app.
Creating your new app:
1. python manage.py startapp [name]
    1.1  python manage.py startapp ogreporting
2. Go to the projects folder and edit the models.py file
    2.1  cd [name]
    2.2  vi models.py
        This is what models.py looks like at this point
        from django.db import models
        
        \# Create your models here.
        class Report(models.Model):
            title = models.TextField()
            description = models.TextField()
            severity = models.TextField()

3. Go to settings.py and add your new app, so that the INSTALLED\_APPS variable should look like this:
        INSTALLED\_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        
            # Third party apps
        
            # My own apps
            'ogreporting'
        ]

4. Run the following commands to save the changes to your project 
        python manage.py makemigrations
        python manage.py migrate

5. Register your models in the admin.py
        vi django1/src/ogreporting/admin.py 
        from django.contrib import admin
        
        # Register your models here.
        from .models import Report

        admin.site.register(Report)

### At this point, we basically got a very basic product working :D

### Create Product Objects in the Python Shell

1. We go back to our product root directory(ie. where the manage.py file is) and run:
    python manage.py shell
And now we can run commands like:
    from ogreporting.models import Report



















