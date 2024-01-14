#!/usr/bin/node
const response = await fetch(process.argv[2]);
  console.log('response.status: ', response.status);
  console.log(response);
