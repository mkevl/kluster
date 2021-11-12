1. install python and add it to path
2. install pip (pip usually comes with python)
3. python should also come with venv, which is used for creating virtual environments
4. go to project directory and create virtual environment: execute `python -m venv venv`

# On windows
5. activate virtual environment: execute `venv\Scripts\activate.bat` (you should see 'venv' at the beginning of cmd line)

# On linux
5. activate virtual environment: source venv/bin/activate

6. run `pip install -r requirements.txt`
7. copy values from .env.example to .env file and assign appropriate values
8. run `python manage.py migrate`
9. create super user to access django admin panel: python manage.py createsuperuser
10. use newly created user account to access django admin at domain.com/admin and create or update data