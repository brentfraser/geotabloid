#!/usr/bin/env bash
# A script to load the geotabloid demo data to a RESTful server
# such as https://github.com/geoanalytic/cookiecutter-geopaparazzi-server
#
# see https://geoanalytic.github.io/a-reference-server-for-geopaparazzi-cloud-profiles/
#
# uses cUrl (https://curl.haxx.se/)
# be sure to replace user:password with your username and password
# the upload url assumes a local server but you can replace localhost:8000 with your specific server address
#
# the path parameters below have a space intentionally placed at the start due to some weird behaviour on Windows
curl -u user:password -v -F path=" /geotabloid/geotabloid_demo.gpap" -F url=@geotabloid_demo.gpap http://localhost:8000/profiles/projects/
curl -u user:password -v -F path=" /geotabloid/mapnik.mapurl" -F url=@mapnik.mapurl http://localhost:8000/profiles/basemaps/
curl -u user:password -v -F path=" /geotabloid/tags.json" -F url=@tags.json http://localhost:8000/profiles/tags/
