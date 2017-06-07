Charcoal
========

Just another site of mine.

Based on
========

Charcoal is developed on Django web framework and Wagtail CMS system.
It is now deployed by the power of gunicorn and supervisor behind a nginx server.
Other dependencies could be found in ``Pipfile``.

Modules
=======

This is the main structure of Charcoal project::

    .
    ├── charcoal
    ├── custom
    ├── home
    ├── posts
    ├── search
    └── tags

* ``charcoal`` contains the main settings and url configurations.
* ``custom`` contains custom model defination based on Wagtail.
* ``posts`` is the implementation of Wagtail Pages.
* ``home`` contains higher layer pages than ``posts`` which is mainly ``*ListPage``.
* ``search`` provides a basic search service for Charcoal.
* ``tags`` is only used for displaying tagged figures for now.

Development
===========

Using ``./manage.py shell_plus`` for development serving.

No test is provided for now.

Deployment
==========

1. Create a ``prod.py`` setting file under directory ``charcoal/settings``.
2. Collect static dependecies by running ``./manage.py collectstatic``.
3. Run a static server for collected static files.
4. Deploy Charcoal by runngin a WSGI server: ``gunicorn charcoal.wsgi:application``.

Demo
====

You can find a demo here: `http://cc.home.windrunner.me:14000/ <http://cc.home.windrunner.me:14000/>`__.

