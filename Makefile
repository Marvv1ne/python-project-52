build:
		./build.sh

runserver:
		python manage.py runserver

render-start:
		gunicorn task_manager.wsgi

test:
	    uv run manage.py test

lint:
	    uv run flake8 task_manager --exclude settings.py