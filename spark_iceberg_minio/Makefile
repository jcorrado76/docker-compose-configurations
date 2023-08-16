up:
	docker compose up -d

down:
	docker compose down

pyspark:
	docker exec -it spark-iceberg pyspark

write-job:
	docker exec -it spark-iceberg spark-submit jobs/write_job.py

read-job:
	docker exec -it spark-iceberg spark-submit jobs/read_job.py


.PHONY: up down pyspark write-job read-job