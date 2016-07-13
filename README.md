
* docker-compose -f docker-compose.yml build
* docker-compose -f docker-compose.yml up -d
* docker-compose run web python ip_rest/manage.py migrate 

Run tests:

* docker-compose run web python ip_rest/manage.py test ip_app.tests
