# Fetching the minified node image on apline linux
FROM node:slim

# Declaring env
ENV NODE_ENV production

# Setting up the work directory
WORKDIR /sensor-server

# Copying all the files in the sensor-server
COPY . .

# Installing dependencies
RUN npm install

# Starting our application
CMD node server.js

# Exposing server port
EXPOSE 3000