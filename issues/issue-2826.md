---
title: Is there a graceful way to stop the miner?
source_url: https://github.com/xmrig/xmrig/issues/2826
author: deostroll
assignees: []
labels: []
created_at: '2021-12-20T09:27:21+00:00'
updated_at: '2022-09-30T05:54:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I checked the http api and came to the conclusion that the controls there are mainly for config reload, pause, and, resume. Please let me know if I missed anything here.

Any suggestion on linux how I can run xmrig for a specified duration?

# Discussion History
## Spudz76 | 2021-12-20T10:20:47+00:00
You can send SIGINT (2) to the process and it does what normal exit does (ctrl-c from controlling terminal)

`kill -2 <main xmrig pid>`

## deostroll | 2021-12-20T17:45:47+00:00
So is there a script-based solution for this? So I figure xmrig must run in background. If so, how do I see the miner stats? (accepts, hashrate, etc)? And, will setting `"background" : true` in the `config.json` output pid?

## Fast-T | 2021-12-20T20:31:51+00:00
CTRL+C should shut down the miner


## Spudz76 | 2021-12-20T21:14:48+00:00
Enable API, hit `/2/backends` or `/2/summary` for JSON report.

## busyboredom | 2022-06-03T22:48:27+00:00
Something in the HTTP API for this would be really welcome (or even just a CLI `quit` command).

If XMRig is run as root, the SIGINT caller must also be running as root. This is really unfortunate when the SIGINT caller is a GUI application that really should not be run as root, and doubly frustrating when that GUI application has to start other child processes which should similarly _not_ be root (I know `setuid()` exists, but if your GUI is GTK-based you're out of luck there too).

## Spudz76 | 2022-06-03T23:58:27+00:00
I run all mine under systemd and as such can allow regular users to start/stop the service while the process still runs as root.

You could also enable API with a secret and then:
```
curl -v --data '{"method":"pause","id":1}' -H "Content-Type: application/json" -H "Authorization: Bearer SECRET" http://127.0.0.1:44444/json_rpc
```
(replace `SECRET` with it, and replace `44444` with your port)

There are only `pause`, `resume`, or `stop`.  But, stop doesn't exit and there is no `start` lol.  Probably this could be fixed up to have a `quit`, I've already got a pull request going that adds `start`.

## busyboredom | 2022-06-04T00:39:23+00:00
Makes sense, I think most people are in your boat :) 

I'm working on a GUI that bundles monerod, p2pool and xmrig into a 1-click mining solution, so I'm a little constrained in how I run things. So far I've tried:
1. Just run the GUI as root (technically this works lol).
2. Run the GUI as root and use `setuid()` to drop privileges when not needed (does not work, 'cause GTK doesn't like this).
3. Set the `setuid` bit on xmrig during installation (gave up on this because it felt too insecure).
4. Start XMRig with `pkexec()` (this works beautifully, but the GUI can't _stop_ XMRig now)

For now, I've just temporarily forked XMRig locally and added:

```
if (command == 'q' || command == 'Q') {
        LOG_INFO("%s " YELLOW_BOLD("quit"), Tags::miner());
        close();
}
```

Which is letting me keep moving with (4) for now. 

## DeeDeeRanged | 2022-09-30T05:54:00+00:00
> You can send SIGINT (2) to the process and it does what normal exit does (ctrl-c from controlling terminal)
> 
> `kill -2 <main xmrig pid>`

Or use sudo killall xmrig

# Action History
- Created by: deostroll | 2021-12-20T09:27:21+00:00
