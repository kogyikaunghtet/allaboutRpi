#!/bin/bash
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
gpio mode 13 out
gpio write 13 0

