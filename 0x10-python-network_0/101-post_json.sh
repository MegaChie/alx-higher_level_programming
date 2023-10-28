#!/bin/bash
# comment text
curl -sH "Content-Type: application/json" --data "@$2" "$1"
