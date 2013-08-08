#mongo-migrate

a python lib for mongo migration

based on pymongo

usage:

    mongration -H localhost -P 27017 -d test -l ./migrations cmd

-H: mongodb server ip

-P: mongodb server port

-d: which databases will be migrate

-l: migration file location

cmd: command, include up, down, list, new


for django:

    python manage.py mongration up


