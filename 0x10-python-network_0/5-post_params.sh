#!/bin/bash
# sends header vaiable and displays the body of the response
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
