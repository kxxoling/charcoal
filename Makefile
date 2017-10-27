all: install install-dep format docker-image statics

install:
	pipenv install --ignore-pipfile
	pipenv install --dev --ignore-pipfile
	wget https://cdnjs.cloudflare.com/ajax/libs/bulma/0.5.0/css/bulma.min.css -O charcoal/static/css/bulma.min.css

install-dep:
	sudo apt-get install libxml2-dev libxslt1-dev lib-pq libmagickwand-dev
	curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
	sudo install -y nodejs
	npm install -g stylus

format:
	yapf -irp -e "./.venv/**" -e "**/migrations/**" **/**.py

statics:
	rm -rf static/*
	pipenv run ./manage.py collectstatic
	pipenv run ./manage.py compress -f

docker-image: statics
	docker build -t charcoal -f ./docker/app/Dockerfile .
