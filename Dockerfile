FROM python:3.9-slim-bullseye


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /todo_service

WORKDIR /todo_service

ADD . /todo_service/

# Install any needed packages specified in requirements.txt
ADD requirements.txt /todo_service/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -Ur /todo_service/requirements.txt


CMD ["/todo_service/start.sh"]
