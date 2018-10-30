GeoTabloid
==========

A demonstration server for GeoPaparazzi users

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT

Getting Started With A Local Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Prerequisites
-------------

Docker_ and Docker-compose_ (Linux) or Docker-desktop (Windows or Mac)
Httpie_ or cUrl_

.. _Docker: https://www.docker.com/products
.. _Docker-compose: https://docs.docker.com/compose/install/
.. _Httpie: https://httpie.org/
.. _cUrl: https://curl.haxx.se/


Clone the repo and build the docker containers
---------------------------------------------

::
    $ git clone https://github.com/geoanalytic/geotabloid.git
    $ cd geotabloid
    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml up -d
    $ docker-compose -f local.yml ps

Depending on how you have installed docker, you may need to preface the docker-compose commands with sudo.
The ps command should result in a report like this.

::
                  Name                         Command               State           Ports
    -------------------------------------------------------------------------------------------
    geotabloid_celerybeat_1     /entrypoint /start-celerybeat    Up
    geotabloid_celeryworker_1   /entrypoint /start-celeryw ...   Up
    geotabloid_django_1         /entrypoint /start               Up      0.0.0.0:8000->8000/tcp
    geotabloid_flower_1         /entrypoint /start-flower        Up      0.0.0.0:5555->5555/tcp
    geotabloid_postgres_1       /bin/sh -c /docker-entrypo ...   Up      5432/tcp
    geotabloid_redis_1          docker-entrypoint.sh redis ...   Up      6379/tcp

So long as the state of all the containers is Up, we are good to go.

Create a superuser and run the tests
------------------------------------

::
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py collectstatic
    > y
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
    > username
    > email
    > password
    > repeat the password
    $ docker-compose -f local.yml run --rm django py.test

The py.test command should result in a report like this:

::
    Starting geotabloid_postgres_1 ... done
    PostgreSQL is available
    Test session starts (platform: linux, Python 3.6.5, pytest 3.8.0, pytest-sugar 0.9.1)
    Django settings: config.settings.test (from ini file)
    rootdir: /app, inifile: pytest.ini
    plugins: sugar-0.9.1, django-3.4.3, celery-4.2.1

     geotabloid/users/tests/test_forms.py ✓                                                                                       2% ▎
     geotabloid/users/tests/test_models.py ✓                                                                                      4% ▍
     geotabloid/users/tests/test_urls.py ✓✓✓✓                                                                                    11% █▏
     geotabloid/users/tests/test_views.py ✓✓✓                                                                                    16% █▋
     gp_projects/tests/test_models.py ✓✓✓                                                                                        21% ██▏
     profiles/tests/test_api.py ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓                                                                          61% ██████▎
     profiles/tests/test_models.py ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓                                                                       100% ██████████

    Results (6.27s):
          57 passed

Load the demo data
------------------

First load the demo data files, which are in the profiles/fixtures folder.  There are shell scripts there to use either Httpie or cUrl, you only need to execute one ot these. but before you begin, edit the file and replace user:password with the username and password you supplied for the superuser.
Execute this command from the fixtures folder.

::
    $ ./load_httpie.sh

Returning to the main GeoTabloid folder, load the fixture data to connect up the demo data to the superuser account.

::
    $ docker-compose -f local.yml run --rm django python manage.py loaddata profiles/fixtures/minimal.json

Now, open your browser and point it to http://localhost:8000/profiles/myprofiles/
You should see a page like this:

::
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept

    {
        "formatVersion": 1.1,
        "profiles": [
            {
                "name": "GeoTabloid",
                "description": "demo geotabloid cloud profile",
                "creationdate": "2018-10-30T18:31:25.841000Z",
                "modifieddate": "2018-10-30T18:31:25.841000Z",
                "color": "#FBC02D",
                "active": true,
                "sdcardPath": "MAINSTORAGE",
                "mapView": "52.02025604248047,-115.70208740234375,10.0",
                "project": {
                    "path": "/geotabloid/geotabloid_demo.gpap",
                    "modifieddate": "2018-10-30T18:28:37.511619Z",
                    "url": "http://localhost:8000/media/projects/geotabloid_demo.gpap",
                    "uploadurl": "/profiles/userprojects/",
                    "size": "110592"
                },
                "tags": {
                    "path": "/geotabloid/tags.json",
                    "modifieddate": "2018-10-30T18:28:37.628130Z",
                    "url": "http://localhost:8000/media/dave/tags/tags.json",
                    "size": "2702",
                    "owner": 1
                },
                "basemaps": [
                    {
                        "path": "/geotabloid/mapnik.mapurl",
                        "modifieddate": "2018-10-30T18:28:37.572963Z",
                        "url": "http://localhost:8000/media/basemaps/mapnik.mapurl",
                        "size": "323"
                    }
                ],
                "spatialitedbs": [],
                "otherfiles": []
            }
        ]
    }

Success!

