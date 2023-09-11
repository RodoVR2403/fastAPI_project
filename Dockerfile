
FROM python:3.8-slim-buster

WORKDIR /app

COPY ["main.py", "models.py"]

RUN pip install --no-cache-dir fastapi uvicorn

COPY main.py /app/
COPY models.py /app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
