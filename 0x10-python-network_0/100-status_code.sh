#!/bin/bash
# comment text
curl -s -o /dev/null -w "%{http_code}" "$1"
