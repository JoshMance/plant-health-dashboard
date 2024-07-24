const express = require('express');
const { spawn } = require('child_process');
 
const app = express();
const port = 3000;
const read_data_script = 'backend/read_moisture_sensor.py';

function runPythonScript(scriptPath) {
    var data = '';
    const child = spawn('python', [scriptPath]);
    child.stdout.on('data', (data) => {
        console.log(data.toString(), Date(Date.now()))
    })
};

var intervalID = setInterval(function() {
    runPythonScript(read_data_script)
}, 5000);