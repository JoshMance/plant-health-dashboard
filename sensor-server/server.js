const express  = require("express")
const cors = require('cors');
const  cron  = require("node-cron");
const { exec } = require("child_process");
const  querystring  = require("querystring"); 

const server = express()
server.use(cors());
server.options('*', cors());

const port = 3000

const buffer_size  = 1000
const buffer       = []
var   buffer_index = 0

function run_measurement() {
    return new Promise((resolve, reject) => {
        exec("python3 measurement_script.py", (error, stdout, stderr) => {
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
cron.schedule('*/2 * * * * *', async () => {
    try {
        const data = await run_measurement();
        buffer[buffer_index] = data;
        buffer_index = (buffer_index + 1) % buffer_size;

    } catch (error) {
        console.error(error);
    }
});

server.get('/data', async (req, res) => {
    try {
        console.log(`Sending: ${buffer.at(-1)}`)
        res.send(`${buffer.at(-1)}`)

    } catch (error) {
        res.sendStatus(404);
    }
});



server.listen(port, () => {
  console.log(`Sensor server listening on port ${port}`)
})
