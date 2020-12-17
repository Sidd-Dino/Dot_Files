#
# ~/.bashrc
#_______________________________________________________________________________
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
#_______________________________________________________________________________
HISTSIZE=500000
HISTFILESIZE=100000


alias ls='ls --color=auto'


source ~/.key-binding.bash


[[ -r "/usr/share/z/z.sh" ]] && source /usr/share/z/z.sh

. ~/.fishPS1


