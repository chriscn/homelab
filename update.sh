#!/bin/sh

# A simple script that perodicially 
echo "Running at $(date -R)"

git pull

docker-compose up -d
