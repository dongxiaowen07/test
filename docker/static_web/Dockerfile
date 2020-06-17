# Version: 0.0.1
FROM docker.io/ubuntu
MAINTAINER Andy Dong "dongxiaowen07@163.com"
RUN apt-get update
RUN apt-get install -y nginx
RUN echo 'Hi, I am in your container' \
    > /usr/share/nginx/html/index.html
EXPOSE 80

