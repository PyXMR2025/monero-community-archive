---
title: Probably not a "Bug" per se, but this really bugs me.....
source_url: https://github.com/xmrig/xmrig/issues/2072
author: fwet
assignees: []
labels:
- av
created_at: '2021-01-30T22:23:08+00:00'
updated_at: '2021-11-12T07:05:57+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:18:15+00:00'
---

# Original Description
Click the "Build from Source" link on certain public wireless nets using Cisco Umbrella nanny software, and you will be redirected to a page telling you xmrig.com is malware
![Screenshot from 2021-01-30 17-19-34](https://user-images.githubusercontent.com/76499781/106369471-bc58bc00-631f-11eb-8dfe-807504437309.png)

Going to assume this is politically motivated and not actual malware, but I figured I would mention it


# Discussion History
## toy1111 | 2021-01-31T17:01:44+00:00
Hi - I think this is pretty typical for any mining software, not just xmrig. Unfortunately there are cases where someone takes the mining software code and includes it in a bot to spread onto unsuspecting users. So downloading with Chrome or Firefox will be block as possible virus and most virus scanners flag crypto mining software as malware. On my computer I always need to click the "allow access/not a virus" or what ever you need to do so that the mining software is allowed.

## Spudz76 | 2021-02-05T21:22:53+00:00
Yep, nothing we can do about that.  Identical to getting socially cancelled on networks, based upon whims, with no path to reverse.

## fwet | 2021-11-12T06:33:47+00:00
> Unfortunately there are cases where someone takes the mining software code and includes it in a bot 

Guilt by association then. Cisco umbrella censors plenty of other content for ideological reasons, not just security.    Malware researchers should remove false positive results like this, or disclose what malware is on the xmrig site so it can be fixed. Otherwise it should be fairly obvious they have ulterior motives.

## Spudz76 | 2021-11-12T07:05:57+00:00
Definitely not just Cisco.  ISPs are now black-holing DNS records for known mining sites.  Some are slapping closed any connection to any port with any protocol (SSL or not) to known mining IPs.

Essentially if you intend to mine on purpose you should be smart enough to get around the issues they have created to protect the majority part of society (most people, who don't even know what mining is).

# Action History
- Created by: fwet | 2021-01-30T22:23:08+00:00
- Closed at: 2021-04-12T14:18:15+00:00
