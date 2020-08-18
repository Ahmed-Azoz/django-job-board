Create virtualenv :
        virtualenv -p python3.8 VIRTUAL_NAME

Activate :
        on ubintu => source bin/activate
        on windows => source .scripts/activate

Make requirements :
        pip freeze > requirements.txt

Deactivate : 
        deactivate

Add Git :
        git add .

Commit :
        git commit -m "COMMIT_NAME"

Push :
        git Push

Install django :
        pip install django

Super Admin:
        django-admin startproject PROJECT_NAME(always 'project')

Runserver : 
        python manage.py runserver

url => Path
view => logic
model => DB
templates => Frontend
