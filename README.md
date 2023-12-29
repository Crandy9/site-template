# site template
Base template for client websites. Everything is configured and ready to go with the exception of Gunicorn/Nginx/SSL cert configuration, and .env files for backend and frontend app that will need to be generated manually and tailored to specific client's needs

# Setup
- clone this project to your local machine somewhere, like your Desktop under a folder called `tmp`. It doesn't matter where, we are going to delete this after setup.
- create a new git repo with a simple README.md file for your new website and clone that repo to a new folder on your local machine where this new website will live, maybe also in your desktop in a folder called `my_new_website` and put the `my_new_website` folder in a parent folder, maybe called `parent_dir`
- Copy/paste this template project that you initially cloned to your local computer within the `my_new_website` folder you created so that your new website code won't be apart of this repo's source, as this is just a template to get things started quickly.
- You can now delete this template repo from your local computer i.e. delete the `tmp` folder. You can keep it on your local machine if you want it for reference and don't want to keep re-cloning it
- within the parent folder `parent_dir`, create a python environment so that it won't be added to source as well as preventing it from being deployed to production in the CI/CD pipeline.
- So the directory will look like this where this template's code will be in `my_new_website/`:
`parent_dir/` ----> `python_env/` `my_new_website/`
- now within `my_new_website/` is this template's source that you can begin to alter to build your website. Make sure you add a Django backend `.env` file within this directory: `my_new_website/`, and add the VueJS frontend `.env` file here: `my_new_website/frontend`. Don't worry, this template is already set up to look at these specific locations for the .env files

- read the frontend and backend `README.md` files for setup guides as well as the guides found in `servers_ssl_db_setup` for web server and SSL cert config

That's it! Happy Coding 🤠
