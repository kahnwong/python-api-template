start:
	uvicorn python_api_template.main:app --port 8080 --reload
test:
	pytest tests/single.py
test-full:
	pytest -n 8 tests/full.py
codecov:
	pytest --cov=python_api_template tests/single.py
