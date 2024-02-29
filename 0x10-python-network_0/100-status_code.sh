#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me
# that causes the server to respond with a message containing "You got me!"
curl -X PUT 0.0.0.0:5000/catch_me
   -H "Content-Type: text/html; charset=UTF-8" 
   -d "You got me!"
curl -sL 0.0.0.0:5000/catch_me
