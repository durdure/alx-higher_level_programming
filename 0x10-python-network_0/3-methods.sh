#!/bin/bash
# Show html methods allowed by the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
