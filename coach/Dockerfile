FROM python:3.11-slim
# Pin httpx below 0.28 because openai==1.45.0 still relies on the legacy
# "proxies" keyword argument that was removed in httpx 0.28. Installing both
# packages together keeps the runtime client compatible with the OpenAI SDK.
RUN pip install --no-cache-dir \
    "httpx==0.27.2" \
    "openai==1.45.0"
WORKDIR /app
COPY run_coach.py .
CMD ["python","run_coach.py"]
