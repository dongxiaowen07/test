'use strict';
const server = require('net').createServer(connection => {
    console.log('Subscriber connected.');
    const firstChunk = '{"type":"changed","timesta';
    const secondChunk = 'mp":1450694370094}\n';

    connection.write(firstChunk);

    const timer = setTimeout(() => {
        connection.write(secondChunk);
        connection.end();
    }, 100);

    connection.on('end', () => {
        clearTimeout(timer);
        console.log('Subscriber disconnected.');
    });

});

server.listen(60300, () => {
    console.log('Test server listening for subscribers...');
});
// const fs = require('fs');
// const net = require('net');
// const filename = process.argv[2];

// if (!filename) {
//     throw Error('Error: No filename specified!');
// }

// net.createServer(connection => {
//     console.log('Subscriber connected.');
//     //connection.write(`Now watching "${filename}" for changes...\n`);
//     connection.write(JSON.stringify({type: 'watching', file: filename}) + '\n');
//     // const watcher = fs.watch(filename, () => connection.write(`File changed: ${new Date()}\n`));
//     const watcher = fs.watch(filename, () => connection.write(JSON.stringify({type: 'changed', timestamp: Date.now()}) + '\n'));
//     connection.on('close', () => {
//         console.log('Subscriber disconnected.');
//         watcher.close();
//     });
// }).listen(60300, () => console.log('Listening for subscribers...'));