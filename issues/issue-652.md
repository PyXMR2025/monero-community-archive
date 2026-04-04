---
title: 'Feature Request: Daemon rate limits'
source_url: https://github.com/monero-project/monero-gui/issues/652
author: Gingeropolous
assignees: []
labels: []
created_at: '2017-03-30T21:11:24+00:00'
updated_at: '2018-11-18T13:48:11+00:00'
type: issue
status: closed
closed_at: '2018-11-18T13:48:11+00:00'
---

# Original Description
would be helpful to encourage users running nodes if they could modulate how much bandwidth it uses. 

# Discussion History
## KanoczTomas | 2017-03-30T21:18:33+00:00
fully agree! One of cool features I like in the daemon.

## yonderblue | 2017-11-04T06:33:02+00:00
I can't get the limit GUI command or daemono startup option --limit 100 (set in GUI) to do anything. Are they unimplemented?

## Jaqueeee | 2017-11-04T06:49:14+00:00
@gaillard Limit is not a valid flag. Try any of these instead:
```
  --limit-rate-up arg (=-1)             set limit-rate-up [kB/s]
  --limit-rate-down arg (=-1)           set limit-rate-down [kB/s]
  --limit-rate arg (=-1)                set limit-rate [kB/s]
```

## yonderblue | 2017-11-04T21:27:48+00:00
Even doing --limit-rate 100, and restarting daemon in the gui daemon log command entry, if I type limit I still get back zero. Perhaps its a bug in the gui and the daemon really is limited. Anyway to verify?

## Jaqueeee | 2017-11-05T15:42:56+00:00
@gaillard that's because of a bug in the daemon. See #805. You'll have to start the daemon manually too see the output from `limit`

## erciccione | 2018-11-18T13:26:23+00:00
@Gingeropolous can this be closed?

## Gingeropolous | 2018-11-18T13:48:11+00:00
yeah, I guess it can. I introduced another issue about hard data caps, but this is fundamentally different I guess. 

# Action History
- Created by: Gingeropolous | 2017-03-30T21:11:24+00:00
- Closed at: 2018-11-18T13:48:11+00:00
