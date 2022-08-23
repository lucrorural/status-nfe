# status-nfe

`status-nfe` é um serviço que consulta como estão os status dos Webservices da Sefaz de todos os Estados do Brasil através do Portal NFe (http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx)

## Como funciona

* A consulta ao site do Portal NFe é feita a cada 10 minutos com os serviços do Celery e Celery Beat.
* O resultado da consulta é enviada para a fila de processamento do Redis.
* O status de cada serviço e de cada UF é gravada no banco de dados Postgres.
* Após a consulta e gravação é criado ou atualizado o cache dos dados no Redis.
* O endpoint da consulta: `api/v1/statusnfe`

## Iniciando os serviços 

* Constroe as imagens de todos os serviços envolvidos: `docker-compose up -d --build`
* Atualiza os modelos do banco de dados: `docker-compose exec web python manage.py migrate`
* Inicia todos os serviços: `docker-compose up`
* Monitoramento do cache: `docker exec -it container_id redis-cli monitor`
