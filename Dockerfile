FROM python:3.12-slim

WORKDIR /opt/app

# app deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# app
COPY . .

# entrypoint
EXPOSE 8080
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
