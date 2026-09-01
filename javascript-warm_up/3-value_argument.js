#!/usr/bin/node
const argument = process.argv[2];

console.log(argument === undefined ? 'No argument' : argument);
