FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /opt/app

# app deps
COPY pyproject.toml uv.lock ./
RUN uv export --no-hashes --no-dev --no-emit-project --output-file=requirements.txt && \
  pip install --no-cache-dir -r requirements.txt

# app
COPY . .

# entrypoint
EXPOSE 8080
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
