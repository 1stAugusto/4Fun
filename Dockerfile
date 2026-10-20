FROM python:3.14-slim

LABEL org.opencontainers.image.source="https://github.com/1stAugusto/4Fun"

WORKDIR /app
RUN addgroup --system app && adduser --system --ingroup app app

ENV APP_VERSION=0.1.0 \
    APP_ENV=container

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app app ./app

USER app
EXPOSE 8000 10000

HEALTHCHECK --interval=5s --timeout=3s --start-period=3s --retries=3 CMD ["python", "-c", "import os, urllib.request; port=os.getenv('PORT', '8000'); urllib.request.urlopen(f'http://127.0.0.1:{port}/health', timeout=2)"]

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
