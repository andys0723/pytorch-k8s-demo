#!/bin/bash
# build_push.sh
# Usage: ./build_push.sh <dockerhub-username> <image-name> <tag>
# Example: ./build_push.sh aaadys pytorch-distributed-demo latest

set -e  # exit if any command fails

# --- Parameters ---
DOCKER_USER=$1
IMAGE_NAME=$2
TAG=${3:-latest}  # default tag is 'latest'

if [ -z "$DOCKER_USER" ] || [ -z "$IMAGE_NAME" ]; then
    echo "Usage: $0 <dockerhub-username> <image-name> [tag]"
    exit 1
fi

FULL_IMAGE="$DOCKER_USER/$IMAGE_NAME:$TAG"

echo "Building Docker image: $FULL_IMAGE"
docker build -t $FULL_IMAGE .

echo "Logging into Docker Hub..."
docker login

echo "Pushing Docker image: $FULL_IMAGE"
docker push $FULL_IMAGE

echo "✅ Image pushed successfully!"
