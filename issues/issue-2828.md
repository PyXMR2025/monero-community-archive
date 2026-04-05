---
title: XMRIG Web API not starting when using wireless connection
source_url: https://github.com/xmrig/xmrig/issues/2828
author: toxicroadkill
assignees: []
labels:
- bug
created_at: '2021-12-22T01:29:49+00:00'
updated_at: '2025-06-16T20:25:56+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:25:55+00:00'
---

# Original Description
I am running xmrig on a machine that uses a wireless connection, debian 10, when the machine boots, it takes it a short time to connect to the wifi hotspot. XMRIG is set to auto start using the @reboot in crontab, and specifying cli options to connect to the xmrig-proxy.

The problem arises, when it reboots/starts up, it runs xmrig, and all is good, with the exception of the web api interface, the web server does not start up. (xmrig is mining, just no web api) I tried starting xmrig manually using the same exact command in crontab, and it works great, starting xmrig along with the web api

Added  sleep 60 && before the crontab command, and poof, it works fine.

It appears that if there is no network connection, the web api wont start up, even if the web connection appears after a short connection time. Is there a solution that can be put into xmrig to have it try again to start the api, or put in a cli option to wait a short time to start to give the network time to come alive?

the wireless connection is set up using a static ip for the machine, so it knows what IP address it should have when it starts up.

# Discussion History
## Spudz76 | 2021-12-22T05:21:17+00:00
Stop (ab)using cron and make a real systemd service.

Put this in `/lib/systemd/system/xmrig.service`:
```
[Unit]
Description=xmrig
After=network-online.target systemd-modules-load.service
Wants=network-online.target systemd-modules-load.service
AssertFileNotEmpty=/opt/xmrig/config.json

[Service]
Type=simple
User=root
Group=root
Restart=always
KillSignal=SIGINT
LimitMEMLOCK=8G
WorkingDirectory=/opt/xmrig
SyslogIdentifier=xmrig
TimeoutStartSec=30s
TimeoutStopSec=15s
ExecStart=/opt/xmrig/xmrig

[Install]
WantedBy=multi-user.target
```

Then `systemctl daemon-reload` and then `systemctl restart xmrig` and then `journalctl -n50 -xafu xmrig` will show what's happening.

The first couple lines tell it not to launch before network-online status.

## Spudz76 | 2021-12-22T05:22:46+00:00
Oh and obviously if your install folder is not `/opt/xmrig` then mass replace with wherever.

## toxicroadkill | 2021-12-22T05:23:16+00:00
i wouldn't call it abusing cron, making it run as a service would be a royal pita to set up (im running 170+ machines), crontab is the simple solution to launching it.

> On Dec 21, 2021, at 11:21 PM, Tony Butler ***@***.***> wrote:
> 
> 
> Stop (ab)using cron and make a real systemd service.
> 
> Put this in /lib/systemd/system/xmrig.service:
> 
> [Unit]
> Description=xmrig
> After=network-online.target systemd-modules-load.service
> Wants=network-online.target systemd-modules-load.service
> AssertFileNotEmpty=/opt/xmrig/config.json
> 
> [Service]
> Type=simple
> User=root
> Group=root
> Restart=always
> KillSignal=SIGINT
> LimitMEMLOCK=8G
> WorkingDirectory=/opt/xmrig
> SyslogIdentifier=xmrig
> TimeoutStartSec=30s
> TimeoutStopSec=15s
> ExecStart=/opt/xmrig/xmrig
> 
> [Install]
> WantedBy=multi-user.target
> Then systemctl daemon-reload and then systemctl restart xmrig and then journalctl -n50 -xafu xmrig will show what's happening.
> 
> The first couple lines tell it not to launch before network-online status.
> 
> —
> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/2828#issuecomment-999295590>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ASD5O3YC2YEYZGRHOV4VL4LUSFN5PANCNFSM5KROEUWQ>.
> Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675> or Android <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>. 
> You are receiving this because you authored the thread.
> 



## toxicroadkill | 2021-12-22T06:48:38+00:00
the real issue is a problem with xmrig, not in how it's launched, whether or not it is connected to the net, it still should start up the api, or at least retry startup if it fails for whatever reason
the miner works great, it's just the api, i think a fix for that issue would be in order, not making a user jump through hoops to launch it differently

just my opinion



> On Dec 21, 2021, at 11:23 PM, postmaster_toxicroadkill ***@***.***> wrote:
> 
> i wouldn't call it abusing cron, making it run as a service would be a royal pita to set up (im running 170+ machines), crontab is the simple solution to launching it.
> 
>> On Dec 21, 2021, at 11:21 PM, Tony Butler ***@***.*** ***@***.***>> wrote:
>> 
>> 
>> Stop (ab)using cron and make a real systemd service.
>> 
>> Put this in /lib/systemd/system/xmrig.service:
>> 
>> [Unit]
>> Description=xmrig
>> After=network-online.target systemd-modules-load.service
>> Wants=network-online.target systemd-modules-load.service
>> AssertFileNotEmpty=/opt/xmrig/config.json
>> 
>> [Service]
>> Type=simple
>> User=root
>> Group=root
>> Restart=always
>> KillSignal=SIGINT
>> LimitMEMLOCK=8G
>> WorkingDirectory=/opt/xmrig
>> SyslogIdentifier=xmrig
>> TimeoutStartSec=30s
>> TimeoutStopSec=15s
>> ExecStart=/opt/xmrig/xmrig
>> 
>> [Install]
>> WantedBy=multi-user.target
>> Then systemctl daemon-reload and then systemctl restart xmrig and then journalctl -n50 -xafu xmrig will show what's happening.
>> 
>> The first couple lines tell it not to launch before network-online status.
>> 
>> —
>> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/2828#issuecomment-999295590>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ASD5O3YC2YEYZGRHOV4VL4LUSFN5PANCNFSM5KROEUWQ>.
>> Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675> or Android <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>. 
>> You are receiving this because you authored the thread.
>> 
> 



## Spudz76 | 2021-12-22T07:03:27+00:00
It's reeeeeeeeeeealy hard to scp one file to everywhere, yeah.

## toxicroadkill | 2021-12-22T07:11:41+00:00
running it as a service is just needlessly complicating things, when a relatively simple fix to the program would solve the issue

simple is better and running it with @reboot, and a few cli options is the ultra simple way to do it, it's certainly **not** abusing cron whatsoever


simple is better, and in this case simple is fix the issue with the program



> On Dec 22, 2021, at 1:03 AM, Tony Butler ***@***.***> wrote:
> 
> 
> It's reeeeeeeeeeealy hard to scp one file to everywhere, yeah.
> 
> —
> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/2828#issuecomment-999334579>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ASD5O3Y26MIC3KZFIQCSYG3USFZ4TANCNFSM5KROEUWQ>.
> Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675> or Android <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>. 
> You are receiving this because you authored the thread.
> 



# Action History
- Created by: toxicroadkill | 2021-12-22T01:29:49+00:00
- Closed at: 2025-06-16T20:25:55+00:00
