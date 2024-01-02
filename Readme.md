## Python version 3.10

### Install dependencies
`pip install -r requirements.txt`

### Adding migrations for db
`python manage.py migrate`

### Run server
`python manage.py runserver`

### Run Celery
- on windows
`celery -A config worker -l info -P eventlet` 
- on unix os
`celery -A config worker -l info -P` 
### Run celery beat
- ``celery -A config beat -l info``

### Environment variables
- create `.env` file
- add
  - DB_USERNAME
  - DB_PASSWORD
  - DB_DATABASE
  - DB_HOST
  - DB_PORT
  - REDIS_HOST
  - REDIS_PORT
  - SECRET_KEY

## Docker-compose
### run project
`docker-compose up`