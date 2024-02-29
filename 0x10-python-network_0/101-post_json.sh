#!/bin/bash
# Sends a JSON POST request to URL passed and displays the response's body
curl -sH "Content-Type: application/json" --data "@$2" "$1"
