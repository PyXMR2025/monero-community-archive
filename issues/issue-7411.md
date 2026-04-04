---
title: Daemon RPC Connection Failure
source_url: https://github.com/monero-project/monero/issues/7411
author: downystreet
assignees: []
labels: []
created_at: '2021-03-01T03:08:36+00:00'
updated_at: '2023-08-09T00:17:57+00:00'
type: issue
status: closed
closed_at: '2023-08-09T00:17:56+00:00'
---

# Original Description
I'm still getting connection timeouts when mining to the daemon. Today I started up two machines that had been shut down and started xmrig and they would not get any new jobs even when there was no connection error in the proxy. Restarting the Monero Daemon temporarily solved the problem. The connection errors I get when connected to the Monero Daemon are happening very often throughout the day. At this point I am wondering, am I even mining anything because there are so many connect errors to the daemon. There is something seriously wrong here that needs to be addressed and I haven't heard hide nor hair of the Monero team about this. Ten days after submitting my first report about this problem it would be nice to hear at least "we're looking into it", "we're working on it" or "it's a bug" instead of radio silence. Show some respect for the people that are trying to help the Monero project instead of completely ignoring them.

# Discussion History
## vdero133 | 2021-03-01T03:26:40+00:00
Could you run monerod with `--log-level 4` and post the logs?  (or point me to where you posted them, did not see them elsewhere), I only saw the ones from xmrig.

## downystreet | 2021-03-01T16:30:07+00:00
I ran log level 4 however when I go to find the log file that corresponds to the time when the connection timeout occurred it seems that it doesn't exist. I have several new log files in the .bitmonero directory but they only span a 3 hour period while log level 4 has been running for more than 10 hours. I am assuming that the Monero daemon uses Universal Time (UTC) and calculated the times accordingly. I am also assuming that the numbers of the bitmonero.log file correspond to bitmonero.log-year-month-day-hour-minute-second. Do you want to see the logs from when there is no connection timeout? Is there something I'm skipping over?

## moneromooo-monero | 2021-03-01T17:41:40+00:00
monerod only keeps 50 log files by default, it'll delete the oldest ones when it reaches that many.
There's a monerod command line option to change this.

## downystreet | 2021-03-01T18:16:10+00:00
Daemon RPC connect error occurred in xmrig proxy from 17:28-17:30 UTC. The Monero daemon log is available from the zip file.
[monerodlog.zip](https://github.com/monero-project/monero/files/6063591/monerodlog.zip)



## mrx23dot | 2021-03-08T17:19:01+00:00
For me RPC is unresponsive when it's syncing:
https://github.com/monero-project/monero/issues/7431

## selsta | 2021-10-06T02:32:54+00:00
#7760 should help with RPC becoming unresponsive.

## selsta | 2023-08-09T00:17:56+00:00
There have been larger monerod code changes in the last 2 years, if this issue persists in the latest version please open a new issue.

# Action History
- Created by: downystreet | 2021-03-01T03:08:36+00:00
- Closed at: 2023-08-09T00:17:56+00:00
