# Start tmux https://wiki.archlinux.org/index.php/Tmux#Start_tmux_on_every_shell_login
# If not running interactively, do not do anything
[[ $- != *i* ]] && return
[[ -z "$TMUX" ]] && exec tmux

alias open="xdg-open"
