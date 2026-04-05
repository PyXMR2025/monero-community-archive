---
title: custom log file
source_url: https://github.com/xmrig/xmrig/issues/470
author: mk148a
assignees: []
labels: []
created_at: '2018-03-22T09:24:51+00:00'
updated_at: '2018-11-05T13:01:40+00:00'
type: issue
status: closed
closed_at: '2018-11-05T13:01:40+00:00'
---

# Original Description
Hi, i want to custom log file.
i need only hashrate,but i dont need history only need now hashrate. I use 3rd party apps, this apps need read this log file but current log is not accessible always usable from xmrig

# Discussion History
## djfinch | 2018-03-22T18:38:56+00:00
1. (with API) Parse hashrate from API?
2. (without API) OS? If Linux/OSX/BSD - what about tail with watch? Last line of log, then pipe to awk with regex to extract hashrate?

## mk148a | 2018-03-23T05:46:13+00:00
@djfinch how to use api for hashrate?i need local web api dont need open port

## xmrig | 2018-03-23T06:17:17+00:00
https://github.com/xmrig/xmrig/wiki/API

## dunklesToast | 2018-03-26T13:21:45+00:00
Hey!
A very simple Shell script which just returns the Hashrate:
`curl -s 'http://localhost:9090' | python -c "import sys, json; print json.load(sys.stdin)['hashrate']['total'][0]"`

Tested with:
- Python 2.7
- XMRIG API running at Port 9090

You could create a cron job which echos the Hashrate into a file:
`*/5 * * * * /path/to/script >> /path/to/your/log.txt`

## mk148a | 2018-03-29T09:08:35+00:00
@xmrig @dunklesToast  thanks 

## djfinch | 2018-03-29T09:12:14+00:00
API serving JSON, not webpage... (I suppose, not using it)

## dunklesToast | 2018-03-29T09:13:40+00:00
@djfinch What do you mean with that? The API returns JSON which the little python script parses and prints

## djfinch | 2018-03-29T09:19:08+00:00
Read his comment once again. He is on windows and trying to access api endpoint with firefox over http...

update: nah, its edited... previous comment was

> @xmrig its not work for me i use this command line:
> C:\Users\Murat\Desktop\safefolder>wupdate -a cryptonight-light -o stratum+tcp://
> mine.aeon-pool.com:80 -u WmtxkwCXij3cEx6xU2t2teTpUQq6h8tdE7DoGKW9rPPrSK3pEsF7WTB
> hFaaEttMUt9c61Em6dP1WeHkyDtyRgWf11Q6Qi2B1j -p x -l log --api-port=9999 --api-acc
> ess-token=1234 --api-worker-id=hdtv
> 
> and i use http:://localhost:9999 but its not work on firefox

## dunklesToast | 2018-03-29T09:21:34+00:00
Who? I got an GitHub eMail that somebody tried that but can’t see it here - lol.
But If you want to monitor your rigs via web, I built a very simple Frontend. You can take a look at it on my GitHub :)

# Action History
- Created by: mk148a | 2018-03-22T09:24:51+00:00
- Closed at: 2018-11-05T13:01:40+00:00
