# status-nfe


docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose up

ToDo:
 * criar no .env de variaveis do settings
 * criar no .env o tempo para rodar cada task
