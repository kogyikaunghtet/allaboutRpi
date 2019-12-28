#!/bin/bash
greeting() {
	echo "Hello, $USER. Let's update this system."
}
update() {
        sudo apt-get update;
        sudo apt-get upgrade -y;
}
leave() {
	echo "--------------------"
	echo "- Update Complete! -"
	echo "--------------------"
	exit
}

greeting
update
leave
