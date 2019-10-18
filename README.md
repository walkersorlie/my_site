## Installing the project on a Unix machine
Follow instructions on https://devcenter.heroku.com/articles/getting-started-with-python through the section "Setup" (this guide can be helpful if you forget certain steps of the deploy process, as I often do). Hint: installing the Heroku CLI system-wide (_i.e._ not installed in a virtual environment) is easier.


### Create a project folder and a virtual environment folder within
```
mkdir PROJECT_NAME
cd PROJECT_NAME
python3 -m venv VIRTUALENV_NAME
```
If you don't have the virtual environment package installed, you can install it with this: `sudo apt-get install python3-venv`.

Then, use git to clone the application into the project folder created

#### Activate the virtual environment
`. VIRTUALENV_NAME/bin/activate`


### Install project requirements
Make sure the virtual environment is activated before installing project requirements!!!

#### Install requirements from requirements.txt
`pip3 install -r requirements.txt`

##### If you get errors, you might have to install/upgrade packages such as:
```
pip3 install --upgrade setuptools
pip3 install wheel
sudo apt-get install python-dev (probably not necessary because this is not for python3. Could perhaps uninstall if installed)
sudo apt-get install python3-dev
sudo apt-get install snapd
```
You might need to install other link files for libc as well


### Running the Heroku project locally
To run the app locally, Heroku looks for a ".env" file that lists any config variables associated with the project. This file should never be committed to version control!!!!

Now, in the root project folder (where the Procfile, requirements.txt, and .git directory are), create the ".env" file and add all config variables at the same time with this command:
* `heroku config -a NAME_OF_APP -s >> .env`

The "-a" option specifies the name of the Heroku application, and the "-s" option converts the output to a string

Now, while still in the root project folder, use the `heroku local` command to run the application:
* `heroku local:run python my_site/manage.py runserver`
or
* `heroku local web`

The first command uses Django's built-in web server to run the project, while the second command uses Gunicorn to run the application (specified in Procfile)


### Running with different settings files
You can use different settings files to run the app. To use different settings files, change which file is specified in:
* my_site/manage.py
or
* my_site/my_site/wsgi.py

The first file is if you are running the app with Django's built-in server, and the second file is for running the app with Gunicorn


### Deploying the project to Heroku
Use the command `git push heroku master` to push Heroku's git branch to their servers
After this is completed, it might be necessary to run this command to allocate a Heroku dyno to the application: `heroku ps:scale web=1`

If you get this error:
> fatal: 'heroku' does not appear to be a git repository
> fatal: Could not read from remote repository.
>
> Please make sure you have the correct access rights
> and the repository exists.

the problem could be that you don't have a remote branch created for Heroku becuase you cloned an already existing repository instead of creating a new one. To solve the issue, follow these steps:
1. Run `get remote -v` to list git remotes and make sure there are no Heroku remotes
2. If there are no Heroku remotes, run this command to create a remote: `heroku git:remote -a APP_NAME_HERE`
More info can be found here: https://devcenter.heroku.com/articles/git



#### Problems with viewing static files or running collectstatic
There can be some weirdness with static files with Gunicorn and Django. For starters, the command to run "collectstatic" from the root directory is:
* `heroku local:run python my_site/manage.py collectstatic`

Do this before you run the application to instantiate the static files in the "staticfiles" directory.

If you run the application using Gunicorn and none of the static files seem to work on the website, read below:

In the "production_settings.py" file, are different "STATICFILES_STORAGE" engines, depending on if you are running the project locally or not. If you are running the project locally for the first time, you might need to uncomment this line:
* # STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

and comment out this line:
* STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

and then proceed with running the application.

There is also a comment that briefly explains what to do:
> For local development, need this:
> STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
> and whenever changes made in any static file, need to run collectstatic:
> heroku local:run python my_site/manage.py collectstatic

After you've done this, you can revert the commented lines to their previous comment state and things should work. But still, if you change a static file, you must run "collectstatic" again (at least if you are running the application with Gunicorn and not Django's built-in server).

A reason you might need to do this before the first time you run the application locally is because the static files are not added to the "staticfiles" directory automatically. There is some weirdness with the interaction between Gunicorn, Django, and the different STATICFILES_STORAGE engines that I have yet to fully understand.


#### Remove .pyc files
If, for whatever reason, you find it necessary to delete all .pyc files, this command will find and delete all of them:
`find . -type f -name *.pyc -delete`


### Helpful links
* https://devcenter.heroku.com/articles/getting-started-with-python
* https://devcenter.heroku.com/articles/deploying-python
