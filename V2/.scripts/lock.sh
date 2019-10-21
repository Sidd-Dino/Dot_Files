#!/usr/bin/env bash

WALLPAPERLOCK() {
	#'betterlockscreeen CODE'
	#betterlockscreen -u ~/.lockscreen.* -b 2
	betterlockscreen -l blur
}

PXLLOCK() {

	#I3LOCK LOCKSCREEN CODE
	icon="$HOME/.lockscreen_icon.png"
	tmpbg='/tmp/screen.png'
	pixelated='/tmp/pixelated_screen.png'
	
	rm -f /tmp/screen.png	

	scrot "$tmpbg"
	#convert -scale 20% -scale 500% "$tmpbg" "$pixelated"
	#convert "$pixelated" "$icon" -gravity center -composite -matte "$pixelated"
	#betterlockscreen -u "$pixelated"
	#xset dpms force off &&
	betterlockscreen -u "$tmpbg"
	betterlockscreen -l
}

I3LOCKNXT() {
	i3lock-next
}

#WALLPAPERLOCK

#PXLLOCK

I3LOCKNXT



