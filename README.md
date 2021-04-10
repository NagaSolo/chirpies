### Description
    - A pseudo-twitter app/service
    - First prototype is online @ [Cheapies](http://cheapies.herokuapp.com)

### Tech Stack
    1st Phase
    - Django
    - SQL
    - Bootstrap4
    - Email transaction service

    2nd Phase
    - ELK stack

### Development
    @main branch
    - test integration with Postal

### Containerization
- At `containerization` directory:
    1. build related containers:
        - `docker-compose up` -> to start the application with postgresql db
    2. run migrations:
        - `docker exec containerization_web_1 python ./chirpies/manage.py makemigrations`
        - `docker exec containerization_web_1 python ./chirpies/manage.py migrate`

- To tear down instances:
    1. bring network down:
        - `docker-compose down`
    2. remove volume:
        - `docker volume rm containerization_postgres_data`

### Deployment
    - First deployment @heroku [Cheapies](http://cheapies.herokuapp.com)
    - Prototype is deployed at: http://cheapies.herokuapp.com
