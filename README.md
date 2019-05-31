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
