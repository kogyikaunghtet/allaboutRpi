#!/bin/bash
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
gpio mode 19 out
gpio write 19 0

