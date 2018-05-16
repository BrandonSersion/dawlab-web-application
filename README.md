# DAWLAB WEB APPLICATION
<p>
Full stack web application built for a small technology company with the framework Python Django. Bootstrap4 user interface. Has a functional test suite built with Selenium Webdriver and a unit test suite built with Unittest. Uses a Sqlite database. Uses django-allauth for user authentication. Allows you to create an account or log in with your GitHub account.
</p>

## SECURITY WARNINGS

    Superuser credentials are public.
    Delete that superuser and create a new one before setting up a real production server.

    Database key in settings.py is public.
    Change database key before setting up a real production server.

    Debug mode in settings.py is active.
    Deactivate debug mode before setting up a real production server.


## CONSOLE COMMANDS 

### SET UP DJANGO SERVER
        *Install python3*
        *Install pip*

        Use Python3 core package Venv to create virtual environment.
            python -m venv 'name virtual environment'

        Activate Virtual Environment.
            cd 'folder containing virtual environment name'
            source 'virtual environment name'/bin/activate
            
        Install DAWLAB_SITE Dependencies in virtual environment.
            pip install -r requirements/local.txt 
            OR
            pip install -r requirements/production.txt

### RUN SERVER
        cd 'folder containing virtual environment folder'
        source 'virtual environment folder'/bin/activate
        cd 'folder containing DAWLAB_SITE manage.py'
        python manage.py runserver

### RUN FUNCTIONAL TESTS
        python manage.py test functional_tests

### RUN UNIT TESTS
        python manage.py test content

#### *more info in the requirements folder*


## HOW TO LOG IN TO HIDDEN ADMIN PAGE

    url: 'host_url'/admin/
    admin credentials:
        username: brandon
        email: s@s.com
        password: brandonsersion
