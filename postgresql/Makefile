up:
	docker compose up -d

down:
	docker compose down --volumes

download-docker-compose:
	curl -sSL https://raw.githubusercontent.com/bitnami/containers/main/bitnami/postgresql/docker-compose.yml > docker-compose.yml

read-data:
	docker exec -it postgresql-postgresql-1 psql -U postgres -d postgres -c "SELECT * FROM sample_table;"

.PHONY: download-docker-compose up down read-data