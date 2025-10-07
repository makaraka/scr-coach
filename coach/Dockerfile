FROM python:3.11-slim
RUN pip install --no-cache-dir openai==1.45.0
WORKDIR /app
COPY run_coach.py .
CMD ["python","run_coach.py"]
