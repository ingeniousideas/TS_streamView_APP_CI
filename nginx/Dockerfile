ARG NGINX_VERSION=1.27.1
FROM docker.io/nginx:${NGINX_VERSION}

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/