#!/bin/bash
SERVICE="polybar"
if pgrep -x "$SERVICE" >/dev/null
then
	killall "$SERVICE"
	killall blueman-applet
	killall nm-applet
	killall pamac-tray
else
	polybar bottom  &
	nm-applet &
	blueman-applet &
	pamac-tray &	
fi


#exec --no-startup-id /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1
#exec --no-startup-id nitrogen --restore; sleep 1; compton -b
#exec --no-startup-id manjaro-hello
#exec --no-startup-id nm-applet
#exec --no-startup-id xfce4-power-manager
#exec --no-startup-id pamac-tray
#exec --no-startup-id clipit
#exec --no-startup-id blueman-applet
#exec_always --no-startup-id sbxkb
#exec --no-startup-id start_conky_maia
#exec --no-startup-id start_conky_green
#exec --no-startup-id xautolock -time 10 -locker blurlock
#exec_always --no-startup-id ff-theme-util
#exec_always --no-startup-id fix_xcursor
#exec_always --no-startup-id /home/sidd-dino/.config/polybar/launch.sh
