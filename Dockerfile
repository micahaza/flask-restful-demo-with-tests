FROM python:alpine

VOLUME ./src

EXPOSE 5000

COPY ./src /opt/myapp
COPY requirements.txt /opt/myapp

WORKDIR /opt/myapp

RUN pip install -r requirements.txt

CMD python app.py
