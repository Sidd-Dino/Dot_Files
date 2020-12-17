#!/bin/sh

[[ -f ~/.Xresources ]] &&\
	xrdb -merge -I$HOME ~/.Xresources

# fix to allow dunst to start
systemctl --user import-environment DISPLAY

# killall battify script 
ps aux |\
grep battify |\
head -n-1 |\
awk '{system("kill " $2)}'

#launch battify
battify &

urxvtd -q -f -o

# start wm
siddwm
