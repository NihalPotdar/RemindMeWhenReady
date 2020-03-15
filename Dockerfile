FROM python:3.8

COPY ./GetData /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]