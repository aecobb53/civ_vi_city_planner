FROM python:3
# https://testdriven.io/courses/tdd-fastapi/docker-config/

# Sets the working directory and copies the working directory in
WORKDIR /usr/src
COPY . .

# set environment varibles for python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
LABEL project="Civ-VI"
LABEL color=blue

# install requirements file
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
