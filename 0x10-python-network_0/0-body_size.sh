#!/bin/bash
# comment text
$ curl -s -I "$1" | grep -i Content-Length | cut -d ' ' -f 2
