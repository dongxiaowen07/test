# Version: 0.0.2
FROM docker.io/ubuntu
MAINTAINER Andy Dong "dongxiaowen07@163.com"
ENV REFRESHED_AT 2019-02-12
RUN apt-get update
RUN apt-get install -y -q nginx
RUN mkdir -p /var/www/html
ADD nginx/global.conf /etc/nginx/conf.d/
ADD nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80

