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
* GitHub access token to use GitHub API ('MY_SITE_GITHUB_ACCESS_TOKEN')
* Django secret key ('DJANGO_SECRET_KEY')


### Running with different settings staticfiles


### Remove .pyc files
`find . -type f -name *.pyc -delete`

You might need to install other link files for libc (I know I did)
