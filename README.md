# site template
Base template for client websites. Everything is configured and ready to go with the exception of Gunicorn/Nginx/SSL cert configuration, and .env files for backend and frontend app that will need to be generated manually and tailored to specific client's needs


# Setup
IMPORTANT: Django is expecting `lctec_project` as the project name for the backend. So if you want to change the project name, then you need to rename all instances of `lctec_project` found in this project to `your_project_name`, including renaming the `lctec_project` main project folder. Otherwise if you rename the project and try to run the server it will crash. 
- clone this project to your local machine somewhere, like your Desktop under a folder called `tmp`. It doesn't matter where, we can delete this after setup.
- create a new git repo in GitHub or any git platform with a simple README.md file for your new website and clone it to a new folder on your local machine where this new website will live, maybe also in your desktop in a folder called `my_new_website` 
- Copy/paste this template's project folders and files (backned/, frontend/, LICENSE, README.md, servers_ssl_db_setup/, .gitignore) to the `my_new_website` folder you created so that your new website code won't be apart of this repo's source, as this is just a template to get things started quickly.
- You can now delete this template repo from your local computer i.e. delete the `tmp` folder. You can keep it on your local machine if you want for future use reference so you don't have to keep re-cloning it
- within the parent folder `my_new_website`, create a python environment so that it won't be added to source as well as preventing it from being deployed to production in the CI/CD pipeline.
- So the directory will look like this where this template's code will be in `my_new_website/`:
`my_new_website/` ----> `python_env/` `my_new_website/`
- now within the child `my_new_website/` folder is this template's source code that you can begin to alter to build your website. Make sure you add a Django backend `.env` file within this directory: `my_new_website/`, and add the VueJS frontend `.env` file here: `my_new_website/frontend`. Don't worry, this template is already set up to look at these specific locations for the .env files

- read the frontend and backend `README.md` files for setup guides as well as the guides found in `servers_ssl_db_setup` for web server and SSL cert config

# running Django dev server
- Make sure you have setup and activated the python env, as well as creating the .env file for the backend Django project. cd to `backend/` where the manage.py file is and run this command to start the Django built-in dev server (replace `lctec_project` with your project name if you renamed the project):
`DJANGO_SETTINGS_MODULE=lctec_project.dev_settings python manage.py runserver`

# running VueJS dev server
- Make sure you have nodejs installed as well as creating the .env file for the frontend VueJS project, cd to `frontend/` and run:
`npm run serve`


That's it! Happy Coding 🤠