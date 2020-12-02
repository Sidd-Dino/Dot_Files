#!/bin/bash

APPS_PATH="$HOME/Documents/SyncLibs/Docs/CheatSheets/"
rofi_command="rofi -config ~/.dotfiles/config/rofi/themes/Switch.rasi "


eval \$"$(ls "$APPS_PATH" | $rofi_command -dmenu -p "")"

eval \$"$()"
