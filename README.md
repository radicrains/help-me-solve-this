# MATHS HEROS

## ABOUT THE APPLICATION
This app is intended for the student community to help each other out with their maths questions. It's a place for students to understand the step-by-step approach in solving your maths problem, as well as learning from your peers! One gets to learn, Another gets to practise their maths skills. It's a win-win for everyone!

[Application Link - MathsHero](https://mathshero.herokuapp.com/)


## INSTALLATION

*Pre-requisites to run this app locally:*
- *Python (v3.6 & higher)*
- *Virtual Environment*
- *Pip*

1. Clone this repo: ```git clone git@github.com:radicrains/help-me-solve-this.git```

2. Open up the repo in VS Code / type ```code .``` in the terminal

3. Create your own .env file  and include your own value for each of the following key:
    - SECRET_KEY
    - DB_NAME
    - DB_USER
    - DB_PASSWORD
    - DB_HOST
    - DB_PORT
    - cloudinary_cloud_name
    - cloudinary_api_key
    - cloudinary_api_secret

4. Run these following commands:
    - pipenv shell
    - pipenv install
    - pipenv run python manange.py makemigrations
    - pipenv run python manage.py migrate
    - pipenv run python manage.py runserver

## TECH STACK
This application is built with Django, Html, PostgreSQL and Materialize

## NEW TECHNOLOGY USED
- Cloudinary
- Materialize

## PROJECT MANAGEMENT, WIREFRAME & SCREENSHOTS
- [Project To-do](https://mathshero.herokuapp.com/)
- [Wireframe](https://mathshero.herokuapp.com/)
- [Screenshots](https://mathshero.herokuapp.com/)

## FUTURE DEVELOPMENTS
- Fix Like Model
- Have user filter see their post
- Allow groups/roles for teacher/students
- Teachers able to pin model answers
- Level up student's badge for their contributions in answering the questions.
