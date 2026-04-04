---
title: incoming connections swings +-30 connections in ~10min cycles, since upgrade
  to v0.17.1.7
source_url: https://github.com/monero-project/monero/issues/7158
author: sacrelege
assignees: []
labels: []
created_at: '2020-12-15T21:08:57+00:00'
updated_at: '2021-01-09T01:33:26+00:00'
type: issue
status: closed
closed_at: '2021-01-09T01:33:26+00:00'
---

# Original Description
Incoming connection swings (+- 30 connections) after upgrade from v0.17.1.6 to v0.17.1.7.
No configuration change done. Node running on ubuntu 20.04.1 LTS. Pretty much default settings.
Nothing special in logs, cpu utilization low (as before).
![monero_inc_connections](https://user-images.githubusercontent.com/7289595/102272376-f3664000-3f20-11eb-9476-82cae4d55ccf.png)

Is this okayish / expected behavior?


# Discussion History
## moneromooo-monero | 2020-12-15T22:06:37+00:00
It's not an expected change.
Run "set_log 1" for a while, paste the resulting logs.

## sacrelege | 2020-12-15T23:36:13+00:00
running with "set_log 1" now, gonna report back soon...

## sacrelege | 2020-12-16T22:34:50+00:00
incoming connection graph in grafana looks pretty much the same as above.
here the last 2000 lines of my log. if you need more, just let me know.

[monerod_2000.log](https://github.com/monero-project/monero/files/5705825/monerod_2000.log)


## moneromooo-monero | 2020-12-16T23:40:16+00:00
This shows a differnce of max 6 connections over the lifetime of the log. It's also only about one minute long. Your graph shows about 30 for that same time period ?

grep INC monerod_2000.log | awk '/NEW CONNECTION/{++C;print C}/CLOSE CONNECTION/{--C;print C}'

## sacrelege | 2020-12-17T01:16:26+00:00
Sorry, my bad. Here the output of your grep over ~2.5h log (a 200k lines monerod.log with set_log 1)
[2h.log](https://github.com/monero-project/monero/files/5706374/2h.log)



## moneromooo-monero | 2020-12-17T11:46:39+00:00
OK, that one shows ~42. Can I see the log ?

## moneromooo-monero | 2020-12-17T11:47:16+00:00
You can upload it to your github repo if it's too large. Or compress it and base64 it.


## sacrelege | 2020-12-17T12:48:54+00:00
just gnuzipped, 200k lines. sorry its not exactly the same time range, but I guess you can run your grep again. grafana still shows similar pattern/swings.
[monerod_200k.log.gz](https://github.com/monero-project/monero/files/5709494/monerod_200k.log.gz)

PS: and sorry for my long response time (busy times) and I'm also not used to report issues on github - your input really helps a lot. thx!

## moneromooo-monero | 2020-12-17T14:51:14+00:00
I see no errors before most disconnections, so it looks like either network issues or the peers disconnecting. This happening right after updating would be a weird coincidence though. Does it revert to the previous behaviour if you run .6 again ? Logs about peers disconnecting or related network errors will appear with log-level 1,net:TRACE  (but this will be spammy).

## sacrelege | 2020-12-17T14:53:54+00:00
running now .6 gonna report back with chart...

## sacrelege | 2020-12-17T22:04:47+00:00
overview a couple of days:
![monero_days](https://user-images.githubusercontent.com/7289595/102549028-ca2de700-40bb-11eb-8fc3-f89ead05d41a.png)
it seems the amplification decreased a bit towards the end of .7 session.

close up of last few hours running with .6.
![monero_6_closeup](https://user-images.githubusercontent.com/7289595/102549043-ce5a0480-40bb-11eb-9dd4-c36f4c73e482.png)

it seems now more pronounced on .6 as well, can't tell if the amplification is getting bigger if there are more connections (over time).. it just seems very strange to have such a regular pattern.. compared to what I had at the very start.

## sacrelege | 2020-12-18T08:43:17+00:00
@moneromooo-monero do you have a node where you can run your grep to check if the behavior is the same? I would like to exclude that this is only happening on my node.

the following is a comparison to my bitcoin core node, which is running on the same network.

![xmr_btc](https://user-images.githubusercontent.com/7289595/102593647-6a642a00-4115-11eb-8c32-3251c4b1d5fa.png)


## moneromooo-monero | 2020-12-18T13:27:42+00:00
I have a node, but I suspect it's missing some connection/disconection events so I'd trust your graph more than the log. Mine shows some of these spike like things, but less pronounced.

## moneromooo-monero | 2020-12-18T13:34:27+00:00
As a data point, does the behviour change markedly if you download https://gui.xmr.pm/files/block.txt and run with: --ban-list block.txt

## sacrelege | 2020-12-19T01:40:23+00:00
yes!
![ban](https://user-images.githubusercontent.com/7289595/102677612-80b8c700-41a3-11eb-815f-1b4f30291fc4.png)


## moneromooo-monero | 2020-12-19T13:33:00+00:00
Alright, chalk it up to the look-at-me then. Thanks for the quick turnaround in testing.


## moneromooo-monero | 2021-01-09T01:33:26+00:00
Solved.

# Action History
- Created by: sacrelege | 2020-12-15T21:08:57+00:00
- Closed at: 2021-01-09T01:33:26+00:00
