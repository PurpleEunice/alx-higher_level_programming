#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
