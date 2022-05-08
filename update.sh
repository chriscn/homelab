#!/bin/sh
echo "Running at $(date -R)"

git pull --ff--only

docker-compose up -d
