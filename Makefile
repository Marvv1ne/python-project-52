build:
		./build.sh

runserver:
		python manage.py runserver

render-start:
		gunicorn task_manager.wsgi