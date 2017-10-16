all: install install-dep format docker-image

install:
	pipenv install --ignore-pipfile
	pipenv install --dev --ignore-pipfile

install-dep:
	sudo apt-get install libxml2-dev libxslt1-dev lib-pq libmagickwand-dev
	curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
	sudo install -y nodejs
	npm install -g stylus

format:
	yapf -irp -e "./.venv/**" -e "**/migrations/**" **/**.py

docker-image:
	rm -r static/*
	pipenv run ./manage.py collectstatic
	pipenv run ./manage.py compress -f
	docker build -t charcoal -f ./docker/app/Dockerfile .

