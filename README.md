## Installing the project on a Unix machine
Follow instructions on https://devcenter.heroku.com/articles/getting-started-with-python through the section "Setup" (this guide can be helpful if you forget certain steps of the deploy process, as I often do)
Hint: installing the Heroku CLI system-wide (_i.e._ not installed in a virtual environment) is easier


### Create a project folder and a virtual environment folder within
```
mkdir PROJECT_NAME
cd PROJECT_NAME
python3 -m venv VIRTUALENV_NAME
```
Then, clone the application into the project folder created

#### Activate the virtual environment
`. VIRTUALENV_NAME/bin/activate`


### Install project requirements
Make sure the virtual environment is activated before installing project requirements

#### Install requirements from requirements.txt
`pip3 install -r requirements.txt`

#### Might have to install/upgrade packages such as:
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

Now, in the root project folder (where the Procfile and requirements.txt are), create the ".env" file and add all config variables at the same time with this command:
`heroku config -a NAME_OF_APP -s >> .env`
The "-a" option specifies the name of the Heroku application, and the "-s" option converts the output to a string

Now, while still in the root project folder, use the `heroku local` command to run the application:
* `heroku local:run python my_site/manage.py runserver`
or
* `heroku local web`
The first command uses Django's built-in web server to run the project, while the second command uses Gunicorn to run the application (specified in Procfile)


### Running with different settings staticfiles
You can use different settings files to run the app. To use different settings files, change which file is specified in:
* my_site/my_site/wsgi.py
or
* my_site/manage.py
depending on which method of running the app you are using (Django or Gunicorn, respectively)


### Deploying the project to Heroku
Use the command `git push heroku master` to push Heroku's git branch to their servers
After this is completed, it might be necessary to run this command to allocate a Heroku dyno to the application: `heroku ps:scale web=1`

#### Remove .pyc files
If, for whatever reason, you find it necessary to delete all .pyc files, this command will find and delete all of them:
`find . -type f -name *.pyc -delete`
