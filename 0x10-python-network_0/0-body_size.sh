#!/bin/bash
# comment text
$ curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
