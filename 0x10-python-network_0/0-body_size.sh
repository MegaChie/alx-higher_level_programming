#!/bin/bash
# comment text
$ curl -sI $1 | grep -i Content-Length | awk '{print $2}'
