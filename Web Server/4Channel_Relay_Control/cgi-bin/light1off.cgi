#!/bin/bash
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
gpio mode 6 out
gpio write 6 1

