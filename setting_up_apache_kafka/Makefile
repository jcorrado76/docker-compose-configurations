up:
	docker compose up -d

down:
	docker compose down

test:
	@echo "Testing 22181"
	nc -z localhost 22181
	@echo "Testing 29092"
	nc -z localhost 29092

logs:
	docker compose logs kafka | grep -i started

.PHONY: up down test logs