*** DJANGO PROJECT SETUP (installing libraries/dependencies) *** 


- install ffmpeg for audio file processing on your system:
sudo apt-get inst- net tools
sudo apt-get install net-tools
- install postgres
sudo apt install libpq-dev
sudo apt install postgresql
sudo apt install postgresql-contrib

- make sure python is installed (should come with ubuntu):
python (or python3) --version
 Django setup (Using Python -v 3.10.6 and Django -v 4.2 as of April, 29, 2023):

- make dir on local machine where this project will be located

- clone this repo from github (ssh or https, see top level servers_ssl_db_setup digitalocean_server.txt)

- install venv:
sudo apt install python3.10-venv

- Create python virtual environment on local machine: 

python3 -m venv env

- Activate python virtual environment on local machine: 

. env/bin/activate 
(you'll see '(env)' on the left-most side the terminal signature when activated)

- Once your env is activated, install Django and other dependencies (see requirements.txt):

install pgadmin4 desktop tool for DB management (https://www.pgadmin.org/download/)

*** Note: You need to create empty DB in either psql shell or pgadmin tool before running python manage.py makemigrations and python manage.py migrate (If you want to use custom user model, DO NOT RUN python manage.py makemigrations/migrate until you have created your custom user model, otherwise Django will revert to its default User Model. Changing from Django's default user model to a custom user model is possible, but unsupported and prone to many errors. Do this first before anything else if that's what you want for your app)
- activate env
(linux) . env/bin.activate
- create new Django project (make sure you are in dir you want project to be created):
django-admin startproject yourprojectname
- run python manage.py runserver to start django backend development server on localhost:8000
- create app (sub projects; make sure you are in project root directory)
python manage.py startapp my app name



*** DEV SERVER (using Django's and npm's development servers over http) ***

To run vs code debugger:
In top level directory, add this launch.json file:

```

{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Django",
            "type": "python",
            "request": "launch",
            "program": "/your/path/to/manage.py",
            "args": [
                "runserver"
            ],
            "django": true,
            "env": {
                "DJANGO_SETTINGS_MODULE": "sheriff_crandy_project.dev_settings"
            },
            "justMyCode": true
        }
    ]
}
```

In sheriff_crandy_project folder, create .env file
add these env vars:

DOMAIN=https://sheriffcrandymusic.local:9443/api
DEV_DOMAIN=http://127.0.0.1:8000
DEV_MODE=True

Should be it. Activate your python env:
. env/bin/activate
And start Django's dev server with the dev settings:

start dev server using dev mode settings:
DJANGO_SETTINGS_MODULE=sheriff_crandy_project.dev_settings python manage.py runserver


Now go to an API endpoint and verify the dev site is running:
http://127.0.0.1:8000/api/sc/v1/tracks/

Go to vuejs setup and run the frontend to make sure the vue app is successfully fetching the dev url data over http

If you were preveiously in production mode, stop all nginx and gunicorn servers and open 
your browser's dev tools and clear all cache and cookie data:

sudo systemctl stop nginx
sudo systemctl stop gunicorn
sudo systemctl stop gunicorn.socket


*** PRODUCTION SIMULATION SERVER (https self-signed SSL certs) ***

TO START SIMULATED PROD SERVER 
access site over https with self-signed ssl certs 
(see servers_ssl_db_setup folder and comlete those steps first if you haven't set up the serves yet):
set backend env DEV_MODE var:
DEV_MODE=False


restart nginx and gunicorn
sudo systemctl restart nginx
sudo systemctl restart gunicorn.socket
sudo systemctl restart gunicorn

access the backend API/admin page at:

https://sheriffcrandymusic.local:9443/api/sheriffcrandyadmin-6A6573757363687269737469736B696E67/

or whatever you named your hosts name in nginx/gnicorn ssl setup


After everything is working, to begin developing and making changes to code.
After you have made a code change, restart servers to see updates:

reset nginx and gunicorn 

sudo systemctl restart nginx
sudo systemctl restart gunicorn

Do not need to use Django's development servers anymore. Hosted by Nginx and Gunicorn servers
