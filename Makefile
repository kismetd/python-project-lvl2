install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff tests/

format:
	poetry run isort --profile black gendiff tests
	poetry run black gendiff tests

bandit:
	poetry run bandit -r gendiff tests

safety:
	poetry run safety check

selfcheck:
	poetry check

check: selfcheck test format lint

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: install test lint selfcheck check build