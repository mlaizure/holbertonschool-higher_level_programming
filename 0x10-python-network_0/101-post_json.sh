#!/bin/bash
# sends JSON POST request and displays the body of the response
curl -sH "Content-Type: application/json" -X POST -d @"$2" "$1"
