mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

pip:
	pip freeze > requirements.txt

flush:
	python3 manage.py flush --no-input

migdel:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete

install:
	pip install -r requirements.txt

user:
	python3 manage.py createsuperuser --email admin@gmail.com
