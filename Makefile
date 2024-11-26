start:
	uv run uvicorn python_api_template.main:app --port 8080 --reload
test:
	uv run pytest tests/single.py
test-full:
	uv run pytest -n 8 tests/full.py
codecov:
	uv run pytest --cov=python_api_template tests/single.py
