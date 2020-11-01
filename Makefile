serve:
	#python manage.py runserver
	python manage.py runserver

migrate:
	python manage.py migrate

migrations:
	python manage.py makemigrations $(app)

collectstatic:
	python manage.py collectstatic

app:
	#django-admin startapp <name>
	python manage.py startapp $(name)

check:
	python manage.py check

test:

	coverage run ./manage.py test

report:
	coverage html

superuser:
	./manage.py createsuperuser --username $(name)
