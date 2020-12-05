#!/usr/bin/env bash

read_sleep() {
    # Usage: read_sleep 1
    #        read_sleep 0.2
    read -rt "$1" <> <(:) || :
}

feh --randomize --bg-fill ~/Pictures/wallpapers
for((;;)){
        read_sleep 120
        feh --randomize --bg-fill ~/Pictures/wallpapers
}
