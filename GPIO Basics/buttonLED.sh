#!/bin/bash
gpio mode 25 out
gpio mode 24 up
while [ 1 ];do
button="$(gpio read 24)"
        if [[ $button == 0 ]]; then
                gpio write 25 1
                echo "LED on"
        else
                gpio write 25 0
                echo "LED off"
        fi
done

