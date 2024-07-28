# Fetching the minified node image on apline linux
FROM node:slim

# Declaring env
ENV NODE_ENV production

WORKDIR /web-app

# Copying all the files
COPY . .

# Installing dependencies
RUN npm install

# Starting our application
CMD node server.js

# Exposing server port
EXPOSE 4000
