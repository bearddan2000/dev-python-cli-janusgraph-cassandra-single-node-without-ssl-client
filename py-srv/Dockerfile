FROM python:3.8-slim

WORKDIR /code

COPY bin/ .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
