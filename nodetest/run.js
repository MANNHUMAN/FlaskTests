//Require is unique to Node.
//use '../' to refer to parent folder.
const logger = require('./nodejs.js');
const path = require('path');
const os = require('os');
const fs = require('fs');
const EventEmitter = require('events');

const emitter = new EventEmitter();

emitter.on('messageLogged',(args)=>{
    console.log('Listener called.',args);
});

emitter.emit('messageLogged',{id: 1, url: 'http://'});

fs.readdir('./',function(err,files){
    if (err) console.log('Error',err);
    else console.log('Result',files);
})

var pathObj = path.parse(__filename);

var totalMemory = os.totalmem();
var freeMemory = os.freemem();

console.log('Total Memory: '+totalMemory+'... Free Memory: '+freeMemory);
//is the same as
console.log(`Total Memory: ${totalMemory}... Free Memory: ${freeMemory}`);
console.log(pathObj);
console.log(logger);
logger.log('message');
