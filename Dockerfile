# syntax=docker/dockerfile:1

FROM node:latest

COPY . .

RUN npm install
