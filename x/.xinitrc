#!/bin/sh

[[ -f ~/.Xresources ]] &&\
	xrdb -merge -I$HOME ~/.Xresources

# fix to allow dunst to start
systemctl --user import-environment DISPLAY

wllppr &

# killall battify scripts 
pgrep -f "battify" | awk '{system("kill " $2)}'

#launch battify
battify &

urxvtd -q -f -o

sxhkd -c "$HOME"/.config/berry/sxhkdrc &

#wm
exec berry
