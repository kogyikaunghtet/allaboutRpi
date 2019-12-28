#!/bin/bash
gpio mode 25 out
while [ 1 ];do
gpio write 25 1
sleep 1
gpio write 25 0
sleep 1
done
