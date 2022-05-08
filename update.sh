#!/bin/sh
cd "$(dirname "$0")"
echo "Running at $(date -R)"

git pull --ff-only
docker-compose up -d --remove-orphans
