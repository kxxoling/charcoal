FROM python:3.6

RUN apt update && apt upgrade
RUN apt install -y libmagickwand-dev
RUN mkdir /web/
RUN mkdir /mediavol/
WORKDIR /web/
RUN pip install pipenv
ADD ./Pipfile.lock /web/
RUN pipenv install --ignore-pipfile
RUN mkdir /db/
EXPOSE 8333
VOLUME /db/
VOLUME /mediavol/
ENV DJANGO_SETTINGS_MODULE charcoal.settings.docker
ADD . /web/
CMD pipenv run gunicorn charcoal.wsgi:application --name charcoal --workers 8 --timeout 120 --graceful-timeout 20 --bind 0.0.0.0:8333 --log-level warn
