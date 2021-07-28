# syntax=docker/dockerfile:1
FROM python:3.9
WORKDIR /code

ENV FLASK_APP=${FLASK_APP}
ENV FLASK_RUN_HOST=${FLASK_RUN_HOST}

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]