#!/usr/bin/node

const fs = require('fs');

const passedArgs = process.argv;

const fileContentA = fs.readFileSync(passedArgs[2], 'utf8');
const fileContentB = fs.readFileSync(passedArgs[3], 'utf8');

const newContent = fileContentA + fileContentB;

fs.writeFileSync(passedArgs[4], newContent, 'utf8');
