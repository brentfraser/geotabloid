#!/bin/bash
# A script to load the geotabloid demo data to a RESTful server
# such as https://github.com/geoanalytic/cookiecutter-geopaparazzi-server
#
# see https://geoanalytic.github.io/a-reference-server-for-geopaparazzi-cloud-profiles/
#
# uses Httpie (https://httpie.org/)
# be sure to replace user:password with your username and password
# the upload url assumes a local server but you can replace localhost:8000 with your specific server address
#
# the path parameters below have a space intentionally placed at the start due to some weird behaviour on Windows
http -a user:password -f POST http://localhost:8000/profiles/projects/ path=" /geotabloid/geotabloid_demo.gpap" url@./geotabloid_demo.gpap
http -a user:password -f POST http://localhost:8000/profiles/basemaps/ path=" /geotabloid/mapnik.mapurl"  url@./mapnik.mapurl
http -a user:password -f POST http://localhost:8000/profiles/tags/ path=" /geotabloid/tags.json"  url@./tags.json
