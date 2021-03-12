#!/bin/bash

container_name=${1:-demodb}
volume_name=${2:-demodb_data}

docker run -d --name $container_name \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=demodb \
    -e MYSQL_USER=demo \
    -e MYSQL_PASSWORD=secret \
    -v $volume_name:/var/lib/mysql \
    -p 3307:3306 \
    mysql:5.7

