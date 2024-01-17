#!/usr/bin/node
const requestSettings = {
    url: process.argv[2];
};
request(requestSettings, function(error, response, body) {
    console.log(response.statusCode);
});
