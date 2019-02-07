# Installing the project on a Unix machine


### Using virtualenv
#### Create a project folder and a `venv` folder within
```
mkdir PROJECT_NAME
cd PROJECT_NAME
python3 -m venv VIRTUALENV_NAME
```
#### Activate the Environment
`. VIRTUALENV_NAME/bin/activate`

### Installing Django 

### I use environment variables to read-in:
* Database password ('MY_SITE_DATABASE_PASSWORD')
* Database endpoint ('MY_SITE_ENDPOINT')
* GitHub access token to use GitHub API ('MY_SITE_GITHUB_ACCESS_TOKEN')
* Django secret key ('DJANGO_SECRET_KEY')

### Installed packages in virtual environment:
* Django==2.1.3
* djangorestframework==3.9.1
* Markdown==3.0.1 (helps style web output on REST api)
* mysqlclient==1.3.13
* pytz==2018.7
* requests==2.21.0

You might need to install other link files for libc (I know I did)
