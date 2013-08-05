#mongo-migrate

a python lib for mongo migration

based on pymongo

usage:

    mongration -h localhost -p 27017 -d test -l ./migrations up target

-h: mongodb server ip
-p: mongodb server port
-d: which databases will be migrate
-l: migration file location
up: action
target: migration version

for django:

    python manage.py mongration up target


