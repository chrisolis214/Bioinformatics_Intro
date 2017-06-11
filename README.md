# Bioinformatics_Intro
Repo used to track Bioinformatics progress

## How To use Container

This container is serverless and only meant to be executed for the life of
the expected function.

I test my containers on a windows machine.

## Creating the containers

` docker build -t python_alpine .`

## Running the containers

`docker run -it --rm python_alpine:latest "<pattern>" "<text">`
