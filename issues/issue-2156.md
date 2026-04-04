---
title: Extraneous characters on daemon output
source_url: https://github.com/monero-project/monero/issues/2156
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-07-06T13:14:53+00:00'
updated_at: '2017-08-08T17:48:23+00:00'
type: issue
status: closed
closed_at: '2017-08-08T17:44:03+00:00'
---

# Original Description
There are some weird extra characters sometimes popping up on messages. I'd never seen that before, and I'm in a mind to blame the readline patches, but I do not have clear evidence they're related:

�T�Height: 4401/947885 (0.5%) on testnet, not mining, net hash 340 H/s, v1, up to date, 2(out)+0(in) connections, uptime 0d 0h 2m 16s�

Usually, I only see the one extra char at the end. I'd never seen them at start of line before. Maybe it's the readline prompt getting printed at the same time as the actual output ?

# Discussion History
## jtgrassie | 2017-07-08T19:32:23+00:00
Can you test with #2159 please?


## moneromooo-monero | 2017-07-08T22:12:31+00:00
I still got it to happen (running "status" in monerod till it happens while it syncs).

## jtgrassie | 2017-07-09T13:43:57+00:00
Hmm. If this is readline related, I'm sure it would be to do with the terminal color sequences.
The extra characters are hex EF BF BD.
https://codingrigour.wordpress.com/2011/02/17/the-case-of-the-mysterious-characters/

The only time our readline code adds readline color sequences is in the wallet cli which prints a color prompt. However you are in the daemon, which doesn't get a color prompt. Plus, the status message which is getting these extra chars is actually not touching libreadline, just our streambuf which simply gets synced to stdout.

All this said, a quick test on the theory:

> Maybe it's the readline prompt getting printed at the same time as the actual output ?

Would be to place a lock at the start of `readline_buffer::set_prompt`
  
```diff
void rdln::readline_buffer::set_prompt(const std::string& prompt)
{
+  std::lock_guard<std::mutex> lock(sync_mutex);
```
which I think it should have anyway.


## jtgrassie | 2017-07-09T13:53:20+00:00
I have added the synchronization lock to #2159 

## moneromooo-monero | 2017-07-09T13:55:27+00:00
<s>Annoyingly, I can't reproduce that without your patch in the first place right now, so it's hard to tell whether it'd fix it. I'll continue on and off trying to find a good way to repro.</s> I got it without the patch, but it's rare-ish. I'll run with the lock for a while and see if I see it again.

## jtgrassie | 2017-07-09T14:01:24+00:00
Annoyingly I have never managed to produce it but there are soo many variables with term setup mixed in.

That sync lock was needed anyway.

Hope you're enjoying the tab completion as much as I am btw ;)

## moneromooo-monero | 2017-07-09T14:04:01+00:00
After a few minutes of trying to repro this with the lock, I've not seen it happen again yet.
And yes, tab works well here :)

## moneromooo-monero | 2017-07-10T10:44:43+00:00
BTW, my TERM is xterm-256color, and wider than 80.

## moneromooo-monero | 2017-08-08T17:44:03+00:00
I've not seen it happen in a while now. I'll reopen if I see it again.

+resolved

# Action History
- Created by: moneromooo-monero | 2017-07-06T13:14:53+00:00
- Closed at: 2017-08-08T17:44:03+00:00
