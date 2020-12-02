#!/usr/bin/env python3

import json
import os

#===================================================================================
##TIME DATA
T_S=os.popen('date +"%H:%M" ').read()

ASCII_NUMS = [
		['     ',' ▄▄▄ ','█  ▄█','█ █ █','█▀  █',' ▀▀▀ ','     '],#0
		['     ',' ▄▄  ','  █  ','  █  ','  █  ',' ▀▀▀ ','     '],#1
		['     ',' ▄▄▄ ','█   █',' ▄▄▄▀','█    ','▀▀▀▀▀','     '],#2
		['     ',' ▄▄▄ ','▀   █','  ▀▀▄','▄   █',' ▀▀▀ ','     '],#3
		['     ','▄   ▄','█   █','▀▀▀▀█','    █','    ▀','     '],#4
		['     ','▄▄▄▄▄','█    ','▀▀▀▀▄','█   █',' ▀▀▀ ','     '],#5
		['     ',' ▄▄▄ ','█   ▀','█▀▀▀▄','█   █',' ▀▀▀ ','     '],#6
		['     ','▄▄▄▄▄','▀  ▄▀','  █  ','  █  ','  ▀  ','     '],#7
		['     ',' ▄▄▄ ','█   █','▄▀▀▀▄','█   █',' ▀▀▀ ','     '],#8
		['     ',' ▄▄▄ ','█   █','▀▄▄▄█','▄   █',' ▀▀▀ ','     '],#9
		['     ','     ','  ■  ','     ','  ■  ','     ','     ']
]


# █ ▄ ▀ ■

TIME_STR = [ '┌ ┐' , '│ │' , '│ │', '│ │' , '│ │' , '│ │' , '└ ┘' ]

for D in range(0,7):
	Nn=0
	for N in T_S :
		if N == ':':
			TIME_STR[D] = TIME_STR[D][:-1] + ASCII_NUMS[10][D] + TIME_STR[D][-1:]
			TIME_STR[D] = TIME_STR[D][:-1] + " " + TIME_STR[D][-1:]
			continue
		if N == '\n':
			break
		Nn+=1
		TIME_STR[D] = TIME_STR[D][:-1] + ASCII_NUMS[int(N)][D] + TIME_STR[D][-1:]
		TIME_STR[D] = TIME_STR[D][:-1] + " " + TIME_STR[D][-1:]

#===================================================================================
##BATERY BAR
BAT_CAP_STR = os.popen('cat /sys/class/power_supply/BAT0/capacity').read()[:-1]
BAT_STAT =  os.popen('cat /sys/class/power_supply/BAT0/status').read()[:1]
BAT_CAP_INT = int(BAT_CAP_STR)

if BAT_STAT == 'C' :
	STAT_CHAR = ""
else:
	STAT_CHAR = "┊"

BAT_BAR_COUNT = (BAT_CAP_INT/100)*( 40-len(BAT_CAP_STR)-3 )
BAT_BAR = "[  BAT   ] "

for BARS in range(0, ( 40-len(BAT_CAP_STR)-3 ) ):
	if BARS <= BAT_BAR_COUNT :
		BAT_BAR += STAT_CHAR
	else:
		BAT_BAR += " "
BAT_BAR += " " + BAT_CAP_STR + "%"

#===================================================================================
##BATERY SYMBOL

BAT_STAT_ICON = [ '' , '' , '' , '' , '' ]

if BAT_STAT == 'C' :
	BAT_STAT_ICON = [
		'   /  ' ,
		'  /__ ' ,
		'    / ' ,
		'   /  ' ,
		'  /   '
	]
elif BAT_CAP_INT <= 15 :
	BAT_STAT_ICON = [
		'  ██  ' ,
		'  ██  ' ,
		'  ██  ' ,
		'  ▀▀  ' ,
		'  ██  '
	]
else:
	BAT_STAT_ICON = [
		'      ' ,
		' +  - ' ,
		'▄█▄▄█▄' ,
		'█▟▄▄▙█' ,
		'      '
	]

#===================================================================================
##BATERY CAP

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
	['█▀█','▀▀█','▀▀▀'],#9
	['   ','   ','   '] #E
]

BAT_CAP_STR = os.popen('cat /sys/class/power_supply/BAT0/capacity').read()[:-1]

#BAT_STR = [ '█▀▄ ▄ ' , '█▀▄ ▄ ' , '▀▀▀   '  ]
BAT_CAP = [ '' , '' , '' ]
for D in range(0,3):
	cnt=0
	for N in BAT_CAP_STR  :
		if N == '\n':
			break
		BAT_CAP[D] += BAT_NUMS[int(N)][D]
		if cnt < len(BAT_CAP_STR)-1:
			BAT_CAP[D] += ' '
		cnt+=1

if( len(BAT_CAP_STR) == 2 ):
	for D in range(0,3):
		BAT_CAP[D] = BAT_NUMS[10][D] + BAT_CAP[D]

#===================================================================================
##VOLUME BAR

VOL_STR=os.popen('pamixer --get-volume').read()[:-1]
VOL_INT=int(float(VOL_STR))
VOL_MUTE=os.popen("pamixer --get-mute").read()
VOL_BAR_COUNT = (40-len(VOL_STR)-2) if( VOL_INT >= 100 ) else (VOL_INT/100)*( 40-len(VOL_STR)-2 ) 
VOL_BAR = "[ VOLUME ] "

if "true" in VOL_MUTE:
    VOL_BAR += "muted"
else:
    for BARS in range(0, ( 40-len(VOL_STR)-2 ) ):
            if BARS <= VOL_BAR_COUNT :
                    VOL_BAR += "-"
            else:
                    VOL_BAR += " "

    VOL_BAR += " " + VOL_STR

#===================================================================================
##BRIGHTNESS BAR

BRGH_STR=os.popen('xbacklight -get').read()[:-5]
BRGH_INT=int(float(BRGH_STR))

BRGH_BAR_COUNT = (BRGH_INT/100)*( 40-len(BRGH_STR)-2 )
BRGH_BAR = "[ BKLGHT ] "

for BARS in range(0, ( 40-len(BRGH_STR)-2 ) ):
	if BARS <= BRGH_BAR_COUNT :
		BRGH_BAR += "█"
	else:
		BRGH_BAR += " "
BRGH_BAR += " " + BRGH_STR

#===================================================================================
##WORKSPACE DATA

WORKSPACE_INPUT = os.popen('i3-msg -t get_workspaces').read()
WORKSPACE_DICT_LIST  = json.loads( WORKSPACE_INPUT )
WRK_SPC_STR = "[ WRKSPC ]\n"

DISPLAYS = []
for DICT in WORKSPACE_DICT_LIST :

	if not DICT['output'] in DISPLAYS:
		DISPLAYS.append( DICT['output'] )
		WRK_SPC_STR += DICT['output'][:9].center(9) + "●"

	WRK_SPC_STR += " " + str(DICT['num'])
	if DICT['focused'] :
		WRK_SPC_STR += "<"
	else:
		WRK_SPC_STR += " "

	if DICT['urgent'] :
		WRK_SPC_STR += "!"
	else:
		WRK_SPC_STR += " "


#===================================================================================
##MISC INFO

DATE_S=os.popen('date +"%d" ').read()[:-1]
DAY_S =os.popen('date +"%a" ').read()[:-1]
YEAR_S=os.popen('date +"%b"').read()[:-1]

DATE= [ '' , '' ,'' ]

DATE_NUM = [
	['▛▜','▌▐','▙▟'],
	[' ▌',' ▌',' ▌'],
	['▀▜','▄▟','▙▄'],
	['▀▜','▄▟','▄▟'],
	['▌▐','▙▟',' ▐'],
	['▛▀','▙▄','▄▟'],
	['▌ ','▙▄','▙▟'],
	['▀▜',' ▌',' ▌'],
	['▛▜','▙▟','▙▟'],
	['▛▜','▙▟',' ▐']
]
for D in range(0,3):
	for N in DATE_S:
		DATE[D] = DATE[D] + DATE_NUM[int(N)][D] + " "
	DATE[D] = DATE[D][:-1]

#===================================================================================
##PRINT

print("┌        ┐" , TIME_STR[0] , "┌     ┐" , sep='')
print("│ " , BAT_STAT_ICON[0] , " │" , TIME_STR[1] , "│",DATE[0],"│" , sep='')
print("│ " , BAT_STAT_ICON[1] , " │" , TIME_STR[2] , "│",DATE[1],"│" , sep='')
print("│ " , BAT_STAT_ICON[2] , " │" , TIME_STR[3] , "│",DATE[2],"│" , sep='')
print("│ " , BAT_STAT_ICON[3] , " │" , TIME_STR[4] , "│",DAY_S,"  │" , sep='')
print("│ " , BAT_STAT_ICON[4] , " │" , TIME_STR[5] , "│",YEAR_S,"  │" , sep='')
print("└        ┘" , TIME_STR[6] , "└     ┘" , sep='')
#print("12345678901234567890123456789012345678901234567890")
#print( "     " , DATE_S , YEAR_S , sep='')
print( BAT_BAR )
print( VOL_BAR )
print( BRGH_BAR )
print( WRK_SPC_STR )

'''
print("\
●* 0* 1* 2* 3* 4* 5* 6* 7* 8* 9*\n\
╳*12*12*12*12*12*12*12*12*12*12*\n\
1*▛▜* ▌*▀▜*▀▜*▌▐*▛▀*▌ *▀▜*▛▜*▛▜*\n\
2*▌▐* ▌*▄▟*▄▟*▙▟*▙▄*▙▄* ▌*▙▟*▙▟*\n\
3*▙▟* ▌*▙▄*▄▟* ▐*▄▟*▙▟* ▌*▙▟* ▐*\n\
█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ \n\
")

# █ ▄ ▀ ■

#│ ─
#┌ ┐ └ ┘
#┴  ┤ ├
#┼

# ╔ ╗ ╚ ╝
# ╩ ╦ ╣ ╠
# ═ ║

╭ ╮ ╯ ╰ ╱ ╲ ╳
╴ ╵ ●

#── ── ── ── ── ──

# ▄  █
#   █
#  █  ▀

#  ║ ║
# █████
#  ███

#['█▀█','█ █','▀▀▀'],#0
#[' █ ',' █ ',' ▀ '],#1
#['▀▀█','█▀▀','▀▀▀'],#2
#['▀▀█',' ▀█','▀▀▀'],#3
#['█ █','▀▀█','  ▀'],#4
#['█▀▀','▀▀█','▀▀▀'],#5
#['█▀▀','█▀█','▀▀▀'],#6
#['▀▀█',' █ ',' ▀ '],#7
#['█▀█','█▀█','▀▀▀'],#8
#['█▀█','▀▀█','▀▀▀'] #9

['█▀█','█ █','▀▀▀'],#0
[' █ ',' █ ',' ▀ '],#1
['▀▀█','█▀▀','▀▀▀'],#2
['▀▀█',' ▀█','▀▀▀'],#3
['█ █','▀▀█','  ▀'],#4
['█▀▀','▀▀█','▀▀▀'],#5
['█▀▀','█▀█','▀▀▀'],#6
['▀▀█',' █ ',' ▀ '],#7
['█▀█','█▀█','▀▀▀'],#8
['█▀█','▀▀█','▀▀▀'],#9
[' ■ ','   ',' ■ '], #E

['   ','▄▄▄','█ █','█▄█','   '],#0
['   ',' ▄ ',' █ ',' █ ','   '],#1
['   ','▄▄▄','▄▄█','█▄▄','   '],#2
['   ','▄▄▄',' ▄█','▄▄█','   '],#3
['   ','▄ ▄','█▄█','  █','   '],#4
['   ','▄▄▄','█▄▄','▄▄█','   '],#5
['   ','▄▄▄','█▄▄','█▄█','   '],#6
['   ','▄▄▄',' █ ',' █ ','   '],#7
['   ','▄▄▄','█▄█','█▄█','   '],#8
['   ','▄▄▄','█▄█','▄▄█','   '],#9
['   ',' ▄ ','   ',' ▀ ','   '], #E

[' ▄▄▄ ','█  ▄█','█ █ █','█▀  █',' ▀▀▀ '],#0
[' ▄▄  ','  █  ','  █  ','  █  ',' ▀▀▀ '],#1
[' ▄▄▄ ','█   █',' ▄▄▄▀','█    ','▀▀▀▀▀'],#2
[' ▄▄▄ ','▀   █','  ▀▀▄','▄   █',' ▀▀▀ '],#3
['▄   ▄','█   █','▀▀▀▀█','    █','    ▀'],#4
['▄▄▄▄▄','█    ','▀▀▀▀▄','█   █',' ▀▀▀ '],#5
[' ▄▄▄ ','█   ▀','█▀▀▀▄','█   █',' ▀▀▀ '],#6
['▄▄▄▄▄','▀  ▄▀','  █  ','  █  ','  ▀  '],#7
[' ▄▄▄ ','█   █','▄▀▀▀▄','█   █',' ▀▀▀ '],#8
[' ▄▄▄ ','█   █','▀▄▄▄█','▄   █',' ▀▀▀ '],#9
['     ','  ■  ','     ','  ■  ','     ']

●* 0* 1* 2* 3* 4* 5* 6* 7* 8* 9*
╳*12*12*12*12*12*12*12*12*12*12*
1*▛▜* ▌*▀▜*▀▜*▌▐*▛▀*▌ *▀▜*▛▜*▛▜*
2*▌▐* ▌*▄▟*▄▟*▙▟*▙▄*▙▄* ▌*▙▟*▙▟*
3*▙▟* ▌*▙▄*▄▟* ▐*▄▟*▙▟* ▌*▙▟* ▐*
█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █

[
	['▛▜','▌▐','▙▟'],
	[' ▌',' ▌',' ▌'],
	['▀▜','▄▟','▙▄'],
	['▀▜','▄▟','▄▟'],
	['▌▐','▙▟',' ▐'],
	['▛▀','▙▄','▄▟'],
	['▌ ','▙▄','▙▟'],
	['▀▜',' ▌',' ▌'],
	['▛▜','▙▟','▙▟'],
	['▛▜','▙▟',' ▐']
]

'''
