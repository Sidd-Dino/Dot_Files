#!/bin/sh

TIME=$(date +"%H:%M")
DATE=$(date +"%a %d")
YEAR=$(date +"    %b %y")
SPC="      "
BATCAP=$(su -c cat /sys/class/power_supply/battery/capacity)
BATSTA=$(su -c cat /sys/class/power_supply/battery/status)
STAT="${BATSTA:0:1}"


T0=(' ▄▄▄  ' '█   █ ' '█   █ ' '█   █ ' ' ▀▀▀  ')
T1=(' ▄▄   ' '  █   ' '  █   ' '  █   ' '▀▀▀▀▀ ')
T2=(' ▄▄▄  ' '█   █ ' ' ▄▄▄▀ ' '█   ▄ ' '▀▀▀▀▀ ')
T3=(' ▄▄▄  ' '▀   █ ' '  ▀▀▄ ' '▄   █ ' ' ▀▀▀  ')
T4=('▄   ▄ ' '█   █ ' '▀▀▀▀█ ' '    █ ' '    ▀ ')
T5=('▄▄▄▄▄ ' '█   ▀ ' '▀▀▀▀▄ ' '█   █ ' ' ▀▀▀  ')
T6=(' ▄▄▄  ' '█   ▀ ' '█▀▀▀▄ ' '█   █ ' ' ▀▀▀  ')
T7=('▄▄▄▄▄ ' '▀  ▄▀ ' '  █   ' '  █   ' '  ▀   ')
T8=(' ▄▄▄  ' '█   █ ' '▄▀▀▀▄ ' '█   █ ' ' ▀▀▀  ')
T9=(' ▄▄▄  ' '█   █ ' '▀▄▄▄█ ' '▄   █ ' ' ▀▀▀  ')
TC=('  ' '▄ ' '  ' '▀ ' '  ')

TS=('' '' '' '' '')
Q=$(expr ${#TIME} - 1)
for i in $( seq 0 $Q) 
do
  #echo "${TIME:$i:1}"
  for index in ${!TS[*]}; do
    case "${TIME:$i:1}" in
    "1")
        TS[$index]=${TS[$index]}${T1[$index]}
        ;;
    "2")
        TS[$index]=${TS[$index]}${T2[$index]}
        ;;
    "3")
        TS[$index]=${TS[$index]}${T3[$index]}
        ;;
    "4")
        TS[$index]=${TS[$index]}${T4[$index]}
        ;;
    "5")
        TS[$index]=${TS[$index]}${T5[$index]}
        ;;
    "6")
        TS[$index]=${TS[$index]}${T6[$index]}
        ;;
    "7")
        TS[$index]=${TS[$index]}${T7[$index]}
        ;;
    "8")
        TS[$index]=${TS[$index]}${T8[$index]}
        ;;
    "9")
        TS[$index]=${TS[$index]}${T9[$index]}
        ;;
    "0")
        TS[$index]=${TS[$index]}${T0[$index]}
        ;;
    ":")
        TS[$index]=${TS[$index]}${TC[$index]}
        ;;
    *)
        echo "${TIME:$i:1}"
        ;;
    esac
  done
done

#================================================
B0=( '█▀█ ' '█ █ ' '▀▀▀ ' )
B1=( ' █  ' ' █  ' ' ▀  ' )
B2=( '▀▀█ ' '█▀▀ ' '▀▀▀ ' )
B3=( '▀▀█ ' ' ▀█ ' '▀▀▀ ' )
B4=( '█ █ ' '▀▀█ ' '  ▀ ' )
B5=( '█▀▀ ' '▀▀█ ' '▀▀▀ ' )
B6=( '█▀▀ ' '█▀█ ' '▀▀▀ ' )
B7=( '▀▀█ ' ' █  ' ' ▀  ' )
B8=( '█▀█ ' '█▀█ ' '▀▀▀ ' )
B9=( '█▀█ ' '▀▀█ ' '▀▀▀ ' )

BS=( '' '' '' )

Q=$(expr ${#BATCAP} - 1)
for i in $( seq 0  $Q) 
do
  #echo "${TIME:$i:1}"
  for index in ${!BS[*]}; do
    case "${BATCAP:$i:1}" in
    "1")
        BS[$index]=${BS[$index]}${B1[$index]}
        ;;
    "2")
        BS[$index]=${BS[$index]}${B2[$index]}
        ;;
    "3")
        BS[$index]=${BS[$index]}${B3[$index]}
        ;;
    "4")
        BS[$index]=${BS[$index]}${B4[$index]}
        ;;
    "5")
        BS[$index]=${BS[$index]}${B5[$index]}
        ;;
    "6")
        BS[$index]=${BS[$index]}${B6[$index]}
        ;;
    "7")
        BS[$index]=${BS[$index]}${B7[$index]}
        ;;
    "8")
        BS[$index]=${BS[$index]}${B8[$index]}
        ;;
    "9")
        BS[$index]=${BS[$index]}${B9[$index]}
        ;;
    "0")
        BS[$index]=${BS[$index]}${B0[$index]}
        ;;
    *)
        echo "${BATCAP:$i:1}"
        ;;
    esac
  done
done
#================================================
BD=( '  █  ' '▀▄█▄▀' '  ▀  ' )
BI=( ' ▄█▄ ' '▀ █ ▀' '  ▀  ' )
if [ $STAT == 'C' ]
then
  BS[0]=${BS[0]}${BI[0]}
  BS[1]=${BS[1]}${BI[1]}
  BS[2]=${BS[2]}${BI[2]}
fi
if [ $STAT == 'D' ]
then
  BS[0]=${BS[0]}${BD[0]}
  BS[1]=${BS[1]}${BD[1]}
  BS[2]=${BS[2]}${BD[2]}
fi
#================================================

printf "%s │ %s\n" "${TS[0]}" "$DATE"
printf "%s │ %s\n" "${TS[1]}" "$YEAR"
printf "%s │ %s\n" "${TS[2]}" "${BS[0]}"
printf "%s │ %s\n" "${TS[3]}" "${BS[1]}"
printf "%s │ %s\n" "${TS[4]}" "${BS[2]}" 
printf "───────────────────────────┴\n"
