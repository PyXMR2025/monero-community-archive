---
title: 'Client_loop: send disconnect Broken pipe'
source_url: https://github.com/xmrig/xmrig/issues/3406
author: schmidtBalint
assignees: []
labels: []
created_at: '2024-01-23T00:24:39+00:00'
updated_at: '2024-09-28T17:48:51+00:00'
type: issue
status: closed
closed_at: '2024-09-28T17:48:51+00:00'
---

# Original Description
I'm getting this ssh disconnection. I'm trying to run xmrig on my pi4. I'm connected to it via ssh. I run the program it gets a job etc but it seems to hang up and when I press a command such as h to see the hashrate I get the broken pipe.

# Discussion History
## geekwilliams | 2024-01-25T03:27:58+00:00
Are you able to plug in a monitor and run the app to see what's happening?

## schmidtBalint | 2024-01-25T07:46:53+00:00
Not really that's why I use ssh. I don't have a micro hdmi with me now. 

## geekwilliams | 2024-01-25T07:52:06+00:00
What version and what OS are you running on the pi? Are you able to log back in using ssh without rebooting the pi? 

## schmidtBalint | 2024-01-25T07:53:21+00:00
Im using the 64 bit version pi OS lite. Yes I'm able to log back in without a reboot 

## geekwilliams | 2024-01-25T08:08:55+00:00
You may be having an issue with your ssh client not sending keep-alive messages as soon as the server on the pi is expecting. Please add the following to the command you use to log in to the pi 

```
-o ServerAliveInterval=60
```

If this works, you can update your ssh client's settings to fix this. 

Also, if you intend to run xmrig long-term on the pi you may want to look into a utility like Unix's Screen.  That way xmrig doesn't automatically stop when the ssh session is disconnected. 

## SChernykh | 2024-01-25T08:23:09+00:00
Also, this is not an XMRig issue.

## Anaphylaxis | 2024-01-25T15:19:52+00:00
Most likely it's either OOM killing ssh or hanging due to the cpu. Did you try --cpu-priority 1 and --cpu-max-threads-hint=90 to limit xmrig to use less processing power (or alternatively the `nice` command) 
Use `--log-file xmrig.log` in xmrig to see what xmrig is doing, you can `tail -f xmrig.log` to follow the file. Use a different ssh session or tmux/screen with the CPU limiting command flags

# Action History
- Created by: schmidtBalint | 2024-01-23T00:24:39+00:00
- Closed at: 2024-09-28T17:48:51+00:00
