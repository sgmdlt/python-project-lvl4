MANAGE := poetry run python manage.py

install:
	@poetry install

lint:
	@poetry run flake8

test:
	@poetry run pytest

test-coverage:
	@poetry run pytest --cov=. --cov-report xml

check: test lint


dev-run:
	@$(MANAGE) runserver

make-migration:
	@$(MANAGE) makemigrations

migrate: make-migration
	@$(MANAGE) migrate

repl:
	@$(MANAGE) shell_plus  --ipython

requirements.txt:
	@poetry export -f requirements.txt -o requirements.txt

.PHONY: install test lint selfcheck check build
