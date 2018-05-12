SECURITY WARNINGS

    BEWARE admin credentials are public.
    Delete that admin and create a new one before setting up a real production server.

    BEWARE database key in settings.py is public.
    Change database key before setting up real production server.

    BEWARE debug mode in settings.py is active.
    Deactivate debug mode before setting up real production server.


CONSOLE COMMANDS 

    SET UP DJANGO SERVER
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

    RUN SERVER
        cd 'folder containing virtual environment name'
        source 'virtual environment name'/bin/activate
        cd 'folder containing DAWLAB_SITE manage.py'
        python manage.py runserver

    RUN FUNCTIONAL TESTS
        python manage.py test functional_tests

    RUN UNIT TESTS
        python manage.py test content

    *more info in the requirements folder*


HOW TO LOG IN TO HIDDEN ADMIN PAGE

    url: 'host_url'/admin/
    admin credentials:
        username: brandon
        email: s@s.com
        password: brandonsersion