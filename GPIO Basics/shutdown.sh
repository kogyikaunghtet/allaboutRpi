#!/bin/bash
gpio mode 25 up
while [ 1 ];do
button="$(gpio read 25)"
        if [[ $button == 0 ]]; then
                echo$(sudo halt -h)
        fi
done

