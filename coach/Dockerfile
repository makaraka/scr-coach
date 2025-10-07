FROM python:3.11-slim
# openai>=1.51.0 ships the updated HTTP client wrapper that uses the new
# ``proxy`` keyword compatible with httpx 0.28+. Keeping the SDK at or above
# this version prevents the ``proxies`` TypeError that surfaced with newer
# httpx releases while still allowing upstream bugfixes.
RUN pip install --no-cache-dir \
    "openai>=1.51.0,<2"
WORKDIR /app
COPY run_coach.py .
CMD ["python","run_coach.py"]
