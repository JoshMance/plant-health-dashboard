const express  = require("express")
const  cron  = require("node-cron");
const { exec } = require("child_process");
const  querystring  = require("querystring"); 
// const redis = require('redis');

const server = express()
const port = 3000
const measurement_script = "measurement_script_mock.py"

const buffer_size  = 1000
const buffer       = []
var   buffer_index = 0

function run_measurement() {
    return new Promise((resolve, reject) => {
        exec("python3 measurement_script_mock.py", (error, stdout, stderr) => {
            if (error) {
                reject(`Error: ${error.message}`);
            } else if (stderr) {
                reject(`Stderr: ${stderr}`);
            } else {
                resolve(stdout);
            }
        });
    });
}

// Schedule the script to run every second 
cron.schedule('*/1 * * * * *', async () => {
    try {
        const data = await run_measurement();
        buffer[buffer_index] = JSON.parse(data);
        buffer_index = (buffer_index + 1) % buffer_size;

    } catch (error) {
        console.error(error);
    }
});

server.get('/data', async (req, res) => {
    try {
        res.send(`${buffer.at(-1)["mean"]}`)

    } catch (error) {
        res.sendStatus(404);
    }
});



server.listen(port, () => {
  console.log(`Sensor server listening on port ${port}`)
})
