#!/usr/bin/node

const fs = require('node:fs');

const writer = fs.createWriteStream(process.argv[2]);

writer.write(process.argv[3]);
