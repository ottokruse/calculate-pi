FROM python:alpine

WORKDIR /app
COPY pi.py .

ENTRYPOINT ["python", "pi.py"]