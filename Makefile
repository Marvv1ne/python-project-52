build:
		./build.sh

runserver:
		python manage.py runserver

render-start:
		gunicorn task_manager.wsgi

test:
	    uv run manage.py test

lint:
	    uv run flake8

migrate:
		poetry run python manage.py makemigrations
		poetry run python manage.py migrate

check:
		uv pip check

PORT ?= 8000
start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi
		