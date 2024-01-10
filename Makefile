### Actions
usage:
	@poetry run python -B src usage

test:
	@poetry run python -B src test

gen:
	@poetry run python -B src generate

base:
	@poetry run python -B src base


### Develop
pytest:
	poetry run pytest tests/

log:
	@cat logs/latest.log

clean:
	cd target_project/tdd-sample/ && git restore .
	rm logs/latest.log || :

catdd:
	source .env


### Docker
docker-setup:
ifdef OPENAI_API_KEY
	docker build --build-arg OPENAI_API_KEY=$(OPENAI_API_KEY) -t catdd-image .
	docker run -d --name catdd-container catdd-image
else
	@echo "Please input a argument \"OPENAI_API_KEY\""
	@echo " $$ make docker-setup OPENAI_API_KEY=YOUR_API_KEY"
endif

docker-bash:
	docker exec -it catdd-container bash

docker-start:
	docker start catdd-container

docker-stop:
	docker stop catdd-container