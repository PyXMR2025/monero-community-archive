---
title: looking for advice
source_url: https://github.com/xmrig/xmrig/issues/3543
author: realyukii
assignees: []
labels: []
created_at: '2024-08-31T10:55:14+00:00'
updated_at: '2024-09-19T09:22:14+00:00'
type: issue
status: closed
closed_at: '2024-09-19T09:20:35+00:00'
---

# Original Description
I'm seeking advice on how to use my old notebook, which I want to keep running 24/7. I don't have a specific reason for doing this, but I would like to put it to work on some computations. While it would be great if these computation are profitable, my main goal is to make it useful in any way, profit are just optional. Will xmrig help with this? I have an internet connection but lack the capability to act as a server since I don't have a public IP.


# Discussion History
## realyukii | 2024-09-19T09:20:35+00:00
Alright, currently I have several use cases for my personal use (tunneling ssh, playing around with telegram bot, etc..):

```
[user@server ~]$ # cockpit and cloudflared are runnnig on the background too                                                 
[user@server ~]$  jobs
[1]   Running                 mpv --no-video genshin.webm --loop-file=inf &
[2]   Running                 sudo -u thelounge thelounge start &
[4]   Running                 ./start-service.js &> /tmp/start-service.log &  (wd: ~/control-center)
[5]-  Running                 sudo python -m http.server 80 &  (wd: ~/personal-web)
[6]+  Running                 ngrok start --all > /dev/null &  (wd: ~/personal-web)
```


## realyukii | 2024-09-19T09:22:12+00:00
After being on for several days, the battery is still in great condition! ^^

```
[user@server ~]$ uptime
 16:18:21 up 18 days,  3:19,  3 users,  load average: 0.48, 0.45, 0.39
```

# Action History
- Created by: realyukii | 2024-08-31T10:55:14+00:00
- Closed at: 2024-09-19T09:20:35+00:00
