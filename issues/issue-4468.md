---
title: 'v0.13.0.1-RC1 + Whonix: no peers without torsocks'
source_url: https://github.com/monero-project/monero/issues/4468
author: qubenix
assignees: []
labels: []
created_at: '2018-09-29T19:20:06+00:00'
updated_at: '2018-10-15T13:43:44+00:00'
type: issue
status: closed
closed_at: '2018-10-15T13:43:44+00:00'
---

# Original Description
OS: Qubes r4.0 + Whonix 14 (Debian Stretch)

Up until the upgrade to the current RC there was no need to use `torsocks` on Whonix. Now using `torsocks` is the only way to get connections.

log-level 1, without `torsocks`: http://termbin.com/vxm4
log-level 4, without `torsocks`: http://termbin.com/ysrw

# Discussion History
## qubenix | 2018-10-14T23:19:00+00:00
I'm going to close this because I'm not 100% sure if this is an issue in Monero, Whonix, or the way I was using them. Some new stream isolation things are happening transparently on Whonix recently, but it's most likely my fault as I haven't seen anyone else mentioning this or commenting here.

I was able to solve this on Whonix 14 by running `monerod` with `systemd` like this:

```
[Unit]
Description=Monero Full Node Mainnet
                                                                                               
[Service]                                                                                      
User=monerod                                                                                   
Group=monerod                                                                                  
Type=simple                                                                                    
ExecStart=/usr/bin/torsocks /usr/local/bin/monerod --no-igd --non-interactive                                              
ExecStop=/usr/local/bin/monerod exit
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## xiphon | 2018-10-14T23:35:02+00:00
@qubenix could you check if the patch #4578 helps?

## qubenix | 2018-10-15T02:03:55+00:00
Yeah, 4578 does seem to help. I still get stacktrace spam, but I don't need to use `torsocks` any more to get connections. Reopening. I'll report on that pull after 12 hours have passed with feedback.

May have solved #4469 too, been running for 24 minutes without stalling. I'll reopen that issue too if there's no stall in 12 hours.

Thanks for catching @xiphon.

## qubenix | 2018-10-15T13:43:44+00:00
#4578 was merged, so no point commenting there. This and #4469 are fixed by it (so no point reopening that issue). Doesn't run smooth but runs. False warnings like this pop up:

`No incoming connections - check firewalls/routers allow port 18080`

and over 12 hours not printing `SYNCHRONIZED OK` ever. Although `print_height` and `status` both show increasing block height and 8 connections (which is correct according to `netstat`). [Here](https://paste.debian.net/plainh/6543845e) is 4 hours worth of logs for the curious.

Running with the `systemd` unit above or same on cli (with or without `--non-interactive`) is the best user experience I've had from Monero on Whonix. Runs smooth, prints accurate information in the log, and doesn't stall.

# Action History
- Created by: qubenix | 2018-09-29T19:20:06+00:00
- Closed at: 2018-10-15T13:43:44+00:00
