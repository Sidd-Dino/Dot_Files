#!/usr/bin/env python3

import json
import os
import datetime

#===================================================================================
##TIME
x = datetime.datetime.now()
print(x.strftime("[  DATE  ] %a %d %b"))
print(x.strftime("[  TIME  ] %H:%M")) 

#===================================================================================
##BATTERY
BAT_CAP_STR = os.popen('cat /sys/class/power_supply/BAT0/capacity').read()[:-1]
BAT_STAT =  os.popen('cat /sys/class/power_supply/BAT0/status').read()[:1]

print("[  BATT  ]",BAT_CAP_STR,BAT_STAT)

#===================================================================================
##WORKSPACE DATA

WORKSPACE_INPUT = os.popen('i3-msg -t get_workspaces').read()
WORKSPACE_DICT_LIST  = json.loads( WORKSPACE_INPUT )
WRK_SPC_STR = ""

DISPLAYS = []
for DICT in WORKSPACE_DICT_LIST :
	if not DICT['output'] in DISPLAYS:
		if WRK_SPC_STR != "" :
			WRK_SPC_STR += "\n"
		DISPLAYS.append( DICT['output'] )
		WRK_SPC_STR += "[" + DICT['output'][:8].center(8) + "] "

	if DICT['focused'] :
		WRK_SPC_STR += ">" + str(DICT['num']) + "<"
	elif DICT['urgent'] :
		WRK_SPC_STR += "!" + str(DICT['num']) + "!"
	else:
		WRK_SPC_STR += " " + str(DICT['num']) + " "

print( WRK_SPC_STR )