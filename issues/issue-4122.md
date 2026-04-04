---
title: 'monerod runs as dbus.service '
source_url: https://github.com/monero-project/monero-gui/issues/4122
author: plowsof
assignees: []
labels: []
created_at: '2023-02-20T05:45:41+00:00'
updated_at: '2023-03-16T09:46:08+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
the goal is to detect if monerod is 'running as a service'

i hope its an issue on my end because sanity checks earlier did not show this behaviour with release. edit* i did not 'double click the binary' 
to check this: (when monerod is running)
`ps -eo pid,cgroup | grep $(pgrep monerod)`

running as ./monerod
8742 0::/user.slice/user-1000.slice/user@1000.service/app.slice/app-org.gnome.Terminal.slice/vte-spawn-67ffb31d-2952-4656-94a4-1dc3a46b

after monerod gets restarted by the gui or started by gui normally
9017 0::/user.slice/user-1000.slice/user@1000.service/app.slice/dbus.service

actual service
10492 0::/system.slice/monerod.service

the gui checks if it ends in .service 

will look at this tomorrow but the fix to ignore "dbus.service" will work

issue happens when i start monero-gui by clicking the appimage / or binary - instead of `./monero-wallet-gui` 

### pstree ?
`pstree -s $(pgrep monerod)`
./monerod ran from terminal
systemd---systemd---gnome-terminal----bash---monerod---34*[{monerod}]
monerod actual systemd service
systemd---monerod---25*[{monerod}]
monerod from gui 
systemd───systemd───monerod───28*[{monerod}]

if there is only one occurrence of systemd then return true?

# Discussion History
# Action History
- Created by: plowsof | 2023-02-20T05:45:41+00:00
