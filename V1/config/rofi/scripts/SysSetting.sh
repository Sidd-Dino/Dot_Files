#!/bin/bash



Wallpaper="nitrogen"
Volume="pavucontrol"
Power="xfce4-power-manager"
Cancel="exit"
GtkTheme="lxappearance"
Network="nm-connection-editor"

# you can customise the rofi command all you want ...
rofi_command="rofi -config $HOME/.dotfiles/config/rofi/themes/default.rasi "

options=$'Wallpaper\nVolume\nPower\nGtkTheme\nNetwork\nCancel'

# ... because the essential options (-dmenu and -p) are added here
eval \$"$(echo "$options" | $rofi_command -dmenu -p "System Settings")"
