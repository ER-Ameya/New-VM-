1. Open a terminal and navigate to the project directory.

2. Create a new virtual environment using the command python -m venv env.

3. Activate the virtual environment using the command source env/bin/activate on Linux or env\Scripts\activate on Windows.

4. add project from the git to the folder 

5. Install the required dependencies using the command pip install -r requirements.txt 

6. Create the database tables by running the command python manage.py makemigrations / migrate.

7. Create a superuser by running the command python manage.py createsuperuser and following the prompts.

8. Start the development server using the command python manage.py runserver.

9. Open a web browser and navigate to http://127.0.0.1:8000/admin/.

10. Log in with the superuser account you just created.

11. In the admin interface, you should see three groups: Super Admin, Admin, and User. You can add users to these groups and assign permissions as needed.
