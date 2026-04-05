---
title: freebsd service
source_url: https://github.com/xmrig/xmrig/issues/3640
author: sec13b
assignees: []
labels: []
created_at: '2025-02-28T10:44:47+00:00'
updated_at: '2025-05-18T18:03:55+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In Ubuntu is easy to create this  permanent service : 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/etc/systemd/system/xmrig.service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
example:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[Unit]
Description=XMRIG Service
[Service]
ExecStart=/home/test/xmrig-c /home/test/config.json
Restart=always
Nice=10
[Install]
WantedBy=multi-user.target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

But in FreeBSD.
can someone give a example ?







# Discussion History
## geekwilliams | 2025-03-01T02:01:02+00:00
FreeBSD uses rc scripts for system services.  You can read about how to assemble your own start script on this site: [https://docs.freebsd.org/en/articles/rc-scripting/]{https://docs.freebsd.org/en/articles/rc-scripting/}

A simple script to run xmrig at a certain part of system start should be pretty straightforward 



## laffer1 | 2025-05-18T18:03:54+00:00
FreeBSD ports already has a script for this

```sh
#!/bin/sh

# PROVIDE: xmrig
# REQUIRE: LOGIN
# KEYWORD: shutdown
#
# Add the following lines to /etc/rc.conf.local or /etc/rc.conf
# to enable this service:
#
# xmrig_enable (bool):	Set to NO by default.
#			Set it to YES to enable it.
# xmrig_user:		The user account the XMRig daemon runs as.
#			It uses '%%USERS%%' user by default.
#			Do not sets it as empty or it will run as root.
# xmrig_conf:		The configuration file XMRig uses.    
#			Default: %%ETCDIR%%/config.json
# xmrig_flags:		Additional runtime flags.

. /etc/rc.subr
name="%%PORTNAME%%"
rcvar="${name}_enable"
load_rc_config ${name}

: ${xmrig_enable:="NO"}
: ${xmrig_user:="%%USERS%%"}
: ${xmrig_conf:="%%ETCDIR%%/config.json"}
: ${xmrig_flags:=""}

command="/usr/sbin/daemon"
procname="%%PREFIX%%/bin/xmrig"
command_args="-f ${procname} --config=${xmrig_conf} ${xmrig_flags}"

run_rc_command "$1"
```

# Action History
- Created by: sec13b | 2025-02-28T10:44:47+00:00
