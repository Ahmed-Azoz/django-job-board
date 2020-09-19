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

migrations :
        python manage.py makemigrations
        python manage.py migrate


relations in django :
        - One to many  [author - posts] Forginkey
        - Many to many [user - groups] Many to many
        - One to one   [user - profile] One to one




static files : [frontend] image, css, javascript
media files : [upload] images





-- Function Based View
        - simple
        - customiz
        - complex

-- Class Based View
        - fast development
        - not complex

-- Viewsets
        - api [model + url] [CRUD]
        - hard customiz