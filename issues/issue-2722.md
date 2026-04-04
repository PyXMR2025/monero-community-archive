---
title: Expected memory usage of monerod
source_url: https://github.com/monero-project/monero/issues/2722
author: svenha
assignees: []
labels: []
created_at: '2017-10-24T11:39:42+00:00'
updated_at: '2017-10-24T15:24:51+00:00'
type: issue
status: closed
closed_at: '2017-10-24T12:44:42+00:00'
---

# Original Description
Hi.
I freshly installed monero from the source file monero-0.11.1.0.tar.gz (worked nicely on Ubuntu 17.04). If I start monerod, it will synchronize up to 90 %, but than it requests an mmap size that exceeds my
32 GB RAM and stops. What RAM size is required by monerod?
Sven


# Discussion History
## moneromooo-monero | 2017-10-24T11:43:46+00:00
32 GB should be way more than enough. I run monerod with at most 2GB free. mmap size may reach terabytes, it doesn't really matter.

Run monerod with "--log-level 1" and see if you get more info on the stop.

## svenha | 2017-10-24T11:52:50+00:00
Thanks for your help.
I had to increase the ulimit -v (virtual memory) from
ulimit -S -v 32000000
ulimit -S -v 64000000
Now, monerod continues the synchronization.


## hyc | 2017-10-24T15:24:51+00:00
You'll be better off running monerod with unlimited virtual memory. The mapsize is always set larger than the space in use.

# Action History
- Created by: svenha | 2017-10-24T11:39:42+00:00
- Closed at: 2017-10-24T12:44:42+00:00
