FROM python:3.11-slim
RUN apt-get update && apt-get install -y tesseract-ocr libgl1 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir opencv-python-headless==4.10.0.84 pytesseract==0.3.10
WORKDIR /app
COPY vision_stream_tesseract.py .
CMD ["python","vision_stream_tesseract.py"]
