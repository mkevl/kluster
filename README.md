# On windows
1. install python and add it to path
2. install pip (pip usually comes with python)
3. python should also come with venv, which is used for creating virtual environments
4. go to project directory and create virtual environment: execute `python -m venv env`
5. activate virtual environment: execute `env\Scripts\activate` (you should see 'env' at the beginning of cmd line)
6. run `pip install -r requirements.txt`
7. copy values from .env.example to .env file and assign appropriate values
8. run `python manage.py migrate`
