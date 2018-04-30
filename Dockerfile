FROM python:3.6-alpine

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && apk add curl

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/

RUN pip install -r /app/requirements.txt

RUN apk del build-deps

ADD . /app/
RUN chmod 0755 /app/run.sh
RUN chmod 0755 /app/healthcheck.sh

#HEALTHCHECK --interval=5s --timeout=3s CMD curl -f http://localhost:8111/ || exit 1
ENTRYPOINT ["/bin/sh", "run.sh"]
#ENTRYPOINT ["python", "web.py"]