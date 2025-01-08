FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app/main.py main.py

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir temp

EXPOSE 5000

CMD ["python", "main.py"]
