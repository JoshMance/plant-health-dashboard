const express = require('express');
const cors = require('cors');
const http = require('http');
const https = require('https');
const path = require('path');


const server = express();
server.use(cors());
server.options('*', cors());


const port = 4000;

const buffer_size  = 1000
const buffer       = []
var   buffer_index = 0 

server.get('/', (req, res) => {
      try {
            res.sendFile(path.join(__dirname, 'index.html'))

      } catch (error) {
            res.sendStatus(404);
      }
})

server.get('/data', async (req, res) => {
      try {
          res.send(`${buffer.at(-1)}`)

      } catch (error) {
          res.sendStatus(404);
      }
  });

const options = {
      host: 'localhost',
      port: 3000,
      path: '/data',
      method: 'GET',
      // headers: {
      //   'Content-Type': 'application/json'
      // }
};

function getData(options) {
      const port = options.port == 443 ? https : http;
      let output = '';

      const req = port.request(options, (res) => {
            res.setEncoding('utf8');
            res.on('data', (chunk) => {
                  output += chunk;
            });
      
            res.on('end', () => {
                  buffer[buffer_index] = output;
                  buffer_index = (buffer_index + 1) % buffer_size;
            });
      });

      req.on('error', (err) => {console.log(err)});
      req.end();
};


server.listen(port, () => {
      var intervalID = setInterval(function() {
            getData(options);
      }, 2000);
})