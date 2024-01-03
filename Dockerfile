FROM python:3.12-slim

# app deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app
WORKDIR /opt/app
COPY . .

EXPOSE 8080
CMD uvicorn python_api_template.main:app --port 8080 --host 0.0.0.0
