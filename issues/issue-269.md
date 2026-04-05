---
title: Find and remove xmrig
source_url: https://github.com/xmrig/xmrig/issues/269
author: codeh4nter
assignees: []
labels: []
created_at: '2017-12-16T23:40:08+00:00'
updated_at: '2025-12-15T19:26:11+00:00'
type: issue
status: closed
closed_at: '2018-03-14T23:39:45+00:00'
---

# Original Description
Today i left my terminal opened for some hours and found it with the message "xmrig[18611]: no active pools, stop mining". I am sure that i didn't install the software so i guess somebody got access to my computer and installed it. I need to find it and remove. I use Ubuntu 16.04. I tried to find the software location by name but no successed.

Help me please

# Discussion History
## QwertyJack | 2017-12-18T09:21:30+00:00
@ilyasavitski maybe I can help u.
There are several ways to find out the cracker and stop him:
* First check out the login record via `last -a`, to see if there is something wrong
* The process' pid is `18611`, you can easily find where the miner is via `sudo ls -l /proc/18611/exe`
* Using network traffic sniffing tools such as `tcpdump` to find out his address
* If mining is OK for you, you can redirect his address to yours ( lol ); otherwise close the miner immediately
* Do not forget change your password after everything is fine, in case he will come again

Good luck ~

## tarreislam | 2020-12-18T09:08:13+00:00
Hi, I have a similar "issue" but xmrig is running under www-data (nginx default user). So I figure this guy found some vulnerability on some site that I host, or that I somehow installed this while under www-data permissions.

`/proc/xxxxx/exe: symbolic link to /tmp/xmrig-upx-v0.2.0-lin64/xmrig`

My server is only available via port 80and 443 


## QwertyJack | 2020-12-18T10:20:16+00:00
There must be some vulnerability on your site. Usually nobody operates under `www-data`.

## ahmanPg | 2023-08-07T12:47:34+00:00
Mine happened through Cudo Miner. It was a headache since couldn't find the entry in crontab, as the process was relaunching with root access. Just after the removal of Cudo faded away with its trojan!

## 0xDeve | 2023-08-17T02:14:36+00:00
> 

Have you found out a way to remove it? I cant seem to find any entry nor task in crontab, can't find the instance anywhere in my cloud server to remove besides the folder .xmrig that basically respawns every 8 hours or so. End up running a script that kills the miner every time it appears in processes lol

## ahmanPg | 2023-08-27T16:31:25+00:00
I think you installed a software that incubated it. Mine was Cudos Etherium miner. Removed it and everything worked out 

## brahimrizqHireme | 2025-12-15T19:26:11+00:00
If you're using docker check all containers that runs in background some images like Umami ghcr.io/umami-software/umami:postgresql-v2.15.0 uses xmrig

run this to scan for any use

`sudo find / -name '*xmrig*' 2>/dev/null`

```text
/var/lib/docker/overlay2/d60543da130e5894cca0823b131a6896722048d5f6cb5e54e9fa2bd04e7d89a3/diff/tmp/xmrig-6.24.0
/var/lib/docker/overlay2/d60543da130e5894cca0823b131a6896722048d5f6cb5e54e9fa2bd04e7d89a3/diff/tmp/xmrig-6.24.0/xmrig
/var/lib/docker/overlay2/d60543da130e5894cca0823b131a6896722048d5f6cb5e54e9fa2bd04e7d89a3/diff/var/tmp/xmrig-6.24.0
/var/lib/docker/overlay2/d60543da130e5894cca0823b131a6896722048d5f6cb5e54e9fa2bd04e7d89a3/diff/var/tmp/xmrig-6.24.0/xmrig
```
and then run this to get the container id 

```bash
for c in $(docker ps -aq); do
  docker inspect "$c" --format '{{.Id}} {{.GraphDriver.Data.MergedDir}}'
done | grep d60543da130e5894cca0823b
```
once you get the container id run this to identify the image
``docker inspect 698340a9fb0a --format 'Image: {{.Config.Image}}'``

Image: ghcr.io/umami-software/umami:postgresql-v2.15.0


# Action History
- Created by: codeh4nter | 2017-12-16T23:40:08+00:00
- Closed at: 2018-03-14T23:39:45+00:00
