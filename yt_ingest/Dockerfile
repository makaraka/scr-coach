FROM python:3.11-slim
RUN pip install --no-cache-dir youtube-transcript-api==0.6.2 google-api-python-client==2.143.0
WORKDIR /app
COPY ingest_playlist.py .
CMD ["python","ingest_playlist.py","PLWQeRMoEALvo17hR-OBfldEN6gCFcA1wy"]
