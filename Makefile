.PHONY: help clean lint test run up down

help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@echo "  clean       Remove Python cache files and build artifacts"
	@echo "  lint        Lint the Python code using flake8"
	@echo "  test        Run unit tests using pytest"
	@echo "  run         Start the FastAPI application using uvicorn"
	@echo "  stop        Stop the running FastAPI application"
	@echo ""

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf dist

lint:
	flake8 app

test:
	pytest

run:
	uvicorn app.main:app --reload

up:
	docker-compose up -d

down:
	docker-compose down
