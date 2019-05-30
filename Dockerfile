FROM python:3.7-alpine3.8

EXPOSE 8081

RUN apk add --no-cache nginx uwsgi gcc libc-dev linux-headers bash
RUN pip install uwsgi

ADD nginx.conf /etc/nginx/conf.d
RUN mkdir /run/nginx

WORKDIR /usr/local/src

ADD ./requirements.txt ./
RUN pip install -r requirements.txt

ADD ./domain ./domain
ADD ./infrastructure ./infrastructure
ADD ./service ./service
ADD ./utils ./utils
ADD ./uwsgi.ini ./
ADD ./start.sh ./

CMD ["bash", "start.sh"]
