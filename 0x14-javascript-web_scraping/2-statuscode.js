#!/usr/bin/node
const url = process.argv[2];
request(url, function (response) {
  console.log('statusCode:', response && response.statusCode);
});
