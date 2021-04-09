#!/bin/bash
# displays http code only
curl -s -o /dev/null -w "%{http_code}" "$1"
