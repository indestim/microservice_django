# Microservices with Django

In this example we have two microservices.

A microservice `Writers` and another microservice `Books`.

Also, the `Writers` microservice will work as API Gateway.

### Install environment

**For API Writers:**

`$ cd api_writers`

`$ virtualenv env_gw`

`$ . env_gw/bin/activate`

**For API Books:**

`$ cd api_books`

`$ virtualenv env_m1`

`$ . env_m1/bin/activate`

### Configure URL microservice

in the API Writers settings file: `api_writers/settings.py`, edit the value of the `MICROSERVICE` dictionary with the `BooksMicroservice` key

### Run Microservices

**For API Books:**

`$ python manage.py runserver 127.0.0.1:8081`

It is **important** that the domain and port of this microservice matches what is written in the configuration

**For API Writers:**

`$ python manage.py runserver 127.0.0.1:8080`