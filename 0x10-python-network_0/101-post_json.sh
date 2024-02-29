#!/bin/bash
# Sends a request to the URL passed and displays response's status code.
curl -sH "Content-Type: application/json" --data "@$2" "$1"
