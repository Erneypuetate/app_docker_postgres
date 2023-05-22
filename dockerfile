FROM python:3.9-slim-buster

WORKDIR /code

COPY requirements.txt .

RUN apt-get update && apt-get install -y freetds-dev build-essential

RUN pip install --no-cache-dir -r requirements.txt

#COPY crear_tabla.py .
#
#RUN chmod +x crear_tabla.py
#RUN ./crear_tabla.py

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
