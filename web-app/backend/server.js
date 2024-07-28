const express = require('express');
 
const app = express();
const port = 4000;

var intervalID = setInterval(function() {
   console.log('hello world!')
}, 5000);