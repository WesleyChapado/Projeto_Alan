<<<<<<< HEAD
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
=======
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
>>>>>>> 4c1e03151ce5a177d1c8621d1a5dd57a435c6ed5
COPY . /code/