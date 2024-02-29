#!/bin/bash
# Sends a request to the URL passed and displays response's status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
