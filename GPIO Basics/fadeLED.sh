#!/bin/bash
gpio mode 23 pwm
while [ 1 ]
do
        for ((i=0; i<=1023; i+=15));do
                gpio pwm 23 $i
                sleep 0.01
        done
        for ((i=1023; i>=0; i-=15));do
                gpio pwm 23 $i
                sleep 0.01
        done
done
