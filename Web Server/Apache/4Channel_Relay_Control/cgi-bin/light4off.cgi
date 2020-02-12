#!/bin/bash
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
gpio mode 26 out
gpio write 26 1

