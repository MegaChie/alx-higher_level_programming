#!/bin/bash
# comment text
curl -sI OPTIONS "$1" | grep "Allow: " | sed 's/Allow: //'
