#!/bin/bash
# comment text
$ curl -s -I "$1" | grep -i Content-Length | awk '{print $2}'
