# fathom-test 

Interview test for Fathom Privacy.  

**The challenge**: We would like for you to develop a Python Django code base. When the root of that codebase is called '/', it should return a webpage built with React. When that request is received, Django should save some information about that request to a database. You can email the codebase, but delivery over GitHub is preferred.

# Dependencies

## Backend ##

- Django
- djangorestframework

## Frontend ##

- React
- axios

# Running the project

1. Create the database schema in the project root with `python manage.py makemigrations && python manage.py migrate`.
2. Build the frontend with the command `yarn relocate` inside the /ui directory.
3. Run de development server with `python manage.py runserver` and it's good to go.
