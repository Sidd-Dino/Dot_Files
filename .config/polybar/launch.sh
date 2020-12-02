#!/bin/bash

# Terminate already running bar instances
killall -q polybar

#ps -ax | grep polybar | awk '{system("kill " $1)}'
# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null;do sleep 1; done

# Launch bar1 and bar2
#polybar top &
polybar bottom &

