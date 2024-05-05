.PHONY: help clean lint test up down

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  clean         Remove Python cache files and build artifacts"
	@echo "  lint          Lint the Python code using flake8"
	@echo "  test          Run unit tests using pytest"
	@echo "  up            Start the FastAPI application and associated services using docker-compose"
	@echo "  down          Stop the running FastAPI application and associated services using docker-compose"
	@echo ""

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf dist

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
