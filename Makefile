.PHONY: help lint test up down

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  lint          Lint the Python code using flake8"
	@echo "  test          Run unit tests using pytest"
	@echo "  up            Start the FastAPI application and associated services using docker-compose"
	@echo "  down          Stop the running FastAPI application and associated services using docker-compose"
	@echo ""

lint:
	flake8 app

test:
	pytest --cov=app tests/

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down
