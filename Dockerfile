from python

RUN apt-get update
RUN apt-get install vim sqlite3 -y
RUN pip install cookiecutter

COPY . /app

