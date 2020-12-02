#!/usr/bin/env bash

# Terminate already running bar instances
#pgrep -u $UID -x conky | awk '{system("kill " $1) }'
killall conky

# Wait until the processes have been shut down
while pgrep -u $UID -x conky >/dev/null;
do
#pgrep -u $UID -x conky | awk '{system("kill " $1) }'
sleep 1;
done

conky -c ~/.config/conky/conky.conf
conky -c ~/.config/conky/conky_cowsay.conf 
