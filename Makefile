all: install install-dep

install:
	pip install -r requirements.txt
	pip install gunicorn
	npm install -g stylus

install-dep:
	sudo apt-get install libxml2-dev libxslt1-dev lib-pq libmagickwand-dev
	curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
	sudo install -y nodejs

dev:
	./manage.py runserver

serve:
	gunicorn --workers=4 -D charcoal.wsgi:application
