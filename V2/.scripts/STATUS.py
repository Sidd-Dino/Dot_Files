#!/usr/bin/env python3

import json
import os

#===================================================================================
##TIME DATA
T_S=os.popen('date +"%H%M" ').read()
DAY_S=os.popen('date +"%a" ').read()[:-1]
DATE_S=os.popen('date +"%a %d " ').read()[:-1]
YEAR_S=os.popen('date +"%b %y" ').read()[:-1]
#FORTUNE=os.popen('fortune -s').read()

ASCII_NUMS = [
	[' ▄▄▄ ','█  ▄█','█ █ █','█▀  █',' ▀▀▀ '],#0
	[' ▄▄  ','  █  ','  █  ','  █  ',' ▀▀▀ '],#1
	[' ▄▄▄ ','█   █',' ▄▄▄▀','█    ','▀▀▀▀▀'],#2
	[' ▄▄▄ ','▀   █','  ▀▀▄','▄   █',' ▀▀▀ '],#3
	['▄   ▄','█   █','▀▀▀▀█','    █','    ▀'],#4
    ['▄▄▄▄▄','█    ','▀▀▀▀▄','█   █',' ▀▀▀ '],#5
	[' ▄▄▄ ','█   ▀','█▀▀▀▄','█   █',' ▀▀▀ '],#6
    ['▄▄▄▄▄','▀  ▄▀','  █  ','  █  ','  ▀  '],#7
    [' ▄▄▄ ','█   █','▄▀▀▀▄','█   █',' ▀▀▀ '],#8
    [' ▄▄▄ ','█   █','▀▄▄▄█','▄   █',' ▀▀▀ '] #9
]


TIME_STR = [ '' , '' , '' , '' , '' ]

for D in range(0,5):
	Nn=0
	for N in T_S :
		if Nn == 2 and D in [0,2,4]:
			TIME_STR[D] += '  '
		if Nn == 2 and D in [1,3]:
			TIME_STR[D] += '■ '
		if N == '\n':
			break
		Nn+=1
		TIME_STR[D] += ASCII_NUMS[int(N)][D]
		TIME_STR[D] += ' '
'''
ASCII_DAYS = {
	'a': ['┌─┐' , '┌─┤' , '└─┘'],
	'd': ['  │' , '┌─┤' , '└─┘'],
	'e': ['┌─┐' , '├─┘' , '└─┘'],
	'F': ['┌─┐' , '├─ ' , '┴  '],
	'h': ['┌  ' , '├─┐' , '┴ ┴'],
	'i': ['┌┬┐' , ' │ ' , '└┴┘'],
	'M': ['┌┬┐' , '│││' , '└ ┘'],
	'n': ['   ' , '┌─┐' , '└ ┘'],
	'o': ['   ' , '┌─┐' , '└─┘'],
	'r': ['   ' , '┌─┐' , '┴  '],
	'S': ['┌─┐' , '└─┐' , '└─┘'],
	'T': ['┌┬┐' , ' │ ' , ' ┴ '],
	't': ['─┼─' , ' │ ' , ' └ '],
	'u': ['   ' , '│ │' , '└─┘'],
	'W': ['┌ ┐' , '│││' , '└┴┘']
}

for D in range(0,3):
	for N in DAY_S :
		if N == '\n':
			break

		TIME_STR[D] += ASCII_DAYS[N][D]
'''

#===================================================================================
##BATERY DATA

BAT_NUMS = [
	['█▀█','█ █','▀▀▀'],#0
	[' █ ',' █ ',' ▀ '],#1
	['▀▀█','█▀▀','▀▀▀'],#2
	['▀▀█',' ▀█','▀▀▀'],#3
	['█ █','▀▀█','  ▀'],#4
    ['█▀▀','▀▀█','▀▀▀'],#5
	['█▀▀','█▀█','▀▀▀'],#6
    ['▀▀█',' █ ',' ▀ '],#7
    ['█▀█','█▀█','▀▀▀'],#8
    ['█▀█','▀▀█','▀▀▀'] #9
]

BATTERY_CAP = os.popen('cat /sys/class/power_supply/BAT0/capacity').read()[:-1]
BATTERY_STAT =  os.popen('cat /sys/class/power_supply/BAT0/status').read()

# █ ▄ ▀ ■

#BAT_STR = [ '█▀▄ ▄ ' , '█▀▄ ▄ ' , '▀▀▀   '  ]
BAT_STR = [ '' , '' , ''  ]
for D in range(0,3):
	for N in BATTERY_CAP  :
		if N == '\n':
			break
		BAT_STR[D] += BAT_NUMS[int(N)][D]
		BAT_STR[D] += ' '

if BATTERY_STAT[0] == 'C' :
	BAT_STR[0] += ' ▄█▄ '
	BAT_STR[1] += '▀ █ ▀'
	BAT_STR[2] += '  ▀  '
else:
	BAT_STR[0] += '  █  '
	BAT_STR[1] += '▀▄█▄▀'
	BAT_STR[2] += '  ▀  '
#===================================================================================
##WORKSPACE DATA

WORKSPACE_INPUT = os.popen('i3-msg -t get_workspaces').read()
WORKSPACE_DICT_LIST  = json.loads( WORKSPACE_INPUT )

WRK_SPC_STR = ""

for DICT in WORKSPACE_DICT_LIST :
	if DICT['focused'] :
		if DICT['urgent'] :
			WRK_SPC_STR += "#" + str(DICT['num']) + "# "
		else:
			WRK_SPC_STR += "│" + str(DICT['num']) + "│ "
		continue
	else :
		if DICT['urgent'] :
			WRK_SPC_STR += "#" + str(DICT['num']) + "# "
		else:
			WRK_SPC_STR += str(DICT['num']) + " "
		continue

#===================================================================================
##WEATHER INFO

#WTHR = os.popen('wget -qO- --no-check- https://wttr.in/Delhi\?0T').read().replace( "\n\n" , "\n" )

#===================================================================================
##PRINT
print("")
print(TIME_STR[0] , DATE_S )
print(TIME_STR[1] , YEAR_S )
print(TIME_STR[2] , BAT_STR[0] )
print(TIME_STR[3] , BAT_STR[1] )
print(TIME_STR[4] , BAT_STR[2] )

print( WRK_SPC_STR )

#print(FORTUNE)

# █ ▄ ▀ ■

#│ ─
#┌ ┐ └ ┘
#┴  ┤ ├
#┼

# ╔ ╗ ╚ ╝
# ╩ ╦ ╣ ╠
# ═ ║

#── ── ── ── ── ──
