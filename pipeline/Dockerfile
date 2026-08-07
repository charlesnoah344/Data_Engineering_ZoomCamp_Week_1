FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked --no-install-project

COPY ingest_data.py .

ENTRYPOINT ["/code/.venv/bin/python", "/code/ingest_data.py"]