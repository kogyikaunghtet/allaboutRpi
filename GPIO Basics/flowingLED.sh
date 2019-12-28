#!/bin/bash
for ((pin=0; pin<=9; pin++));do
        gpio mode $pin out
        gpio write $pin 0
done
while [ 1 ]
do
        for ((pin=0; pin<=9; pin++));do
                gpio write $pin 1
                sleep 0.03
        done
        for ((pin=0; pin<=9; pin++));do
                gpio write $pin 0
                sleep 0.03
        done
done
