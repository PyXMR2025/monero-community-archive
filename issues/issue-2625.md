---
title: Set -DWITH_EMBEDDED_CONFIG=ON, Switching algorithm problem
source_url: https://github.com/xmrig/xmrig/issues/2625
author: JieSinTime
assignees: []
labels: []
created_at: '2021-10-11T18:39:39+00:00'
updated_at: '2021-10-16T15:39:38+00:00'
type: issue
status: closed
closed_at: '2021-10-16T15:39:38+00:00'
---

# Original Description
After setting the built-in configuration file, using the moneroocean mining pool, every time you switch the algorithm, you need to STARTING ALGO PERFORMANCE CALIBRATION (with 20 seconds round)

# Discussion History
## Spudz76 | 2021-10-11T20:52:25+00:00
MO-xmrig support is over on the [MO fork](https://github.com/MoneroOcean/xmrig/issues)

The bug doesn't exist here since there is no algo-perf feature.

## Spudz76 | 2021-10-11T21:46:00+00:00
Possibly related: https://github.com/MoneroOcean/xmrig/issues/70

Something definitely unexpected occurs when using the API config features with MO-fork.

## Spudz76 | 2021-10-11T21:47:31+00:00
Oh actually if your embedded config file actually had the algo-perf section in it, probably it would not do that.

Of course then you need to embed a custom config for each individual rig which is harder than just having the normal external config.json file.  Not really much way around this.

## Spudz76 | 2021-10-11T21:49:54+00:00
Guess it could cache the algo-perf section and when it re-loads from embedded just always insert the algo-perf regardless.

Then it should run once every time you launch cold instead and maybe persist the algo-switches (which apparently trigger a config-reread when embedded?)

## JieSinTime | 2021-10-11T23:36:46+00:00
Everything is normal for external files. Every time the mining pool changes the algorithm, the built-in configuration file will start to test again

## JieSinTime | 2021-10-11T23:56:57+00:00
![image](https://user-images.githubusercontent.com/86323541/136868666-0dff752f-27c6-4f53-8fc4-0de2a8c4f00c.png)


## JieSinTime | 2021-10-12T00:13:21+00:00
![image](https://user-images.githubusercontent.com/86323541/136869662-30a5d803-3264-4a43-b1bf-2e3aaf66e403.png)
Yes, the built-in does not need to update these data, which leads to the test every time, and everything is normal on the external

## JieSinTime | 2021-10-12T00:14:37+00:00
@xmrig 

## Spudz76 | 2021-10-12T01:53:14+00:00
You mean to flag @MoneroOcean because all of this code is completely theirs.

But you're already talking to one of the top contributors to both projects.  You should post this on the correct Issues page instead of here.

# Action History
- Created by: JieSinTime | 2021-10-11T18:39:39+00:00
- Closed at: 2021-10-16T15:39:38+00:00
