FROM python:3.8.3-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev git

RUN git clone https://github.com/ogurliev02/user_service.git .
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]