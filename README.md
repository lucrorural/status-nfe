# status-nfe


* `docker-compose up -d --build`
* `docker-compose exec web python manage.py migrate`
* `docker-compose up`

* Monitor do cache: `docker exec -it container_id redis-cli monitor`
