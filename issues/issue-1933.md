---
title: monerod.exe causing high hard pagefaults
source_url: https://github.com/monero-project/monero/issues/1933
author: exemar
assignees: []
labels: []
created_at: '2017-03-27T18:14:10+00:00'
updated_at: '2017-03-27T19:00:10+00:00'
type: issue
status: closed
closed_at: '2017-03-27T19:00:10+00:00'
---

# Original Description
Posted this to the gui repo and told to post here instead with more system info.
Discovered this because I was trying to find the cause of audio glitches/stutters so ran LatencyMon. 
I've attached the text of the processes page in LatencyMon, aswell as the report where it highlights monerod.exe as the highest pagefault count.
Was asked to include also the process size - not too sure what that means but the monerod.exe process seems to be using around 65,000K memory according to task manager. 
System info:
AMD fx-4300
Nvidia GeForce GTX 1060
Gigabyte GA-78LMT-USB3 motherboard
8gb DDR3 ram
[report.txt](https://github.com/monero-project/monero/files/873358/report.txt)
[Processes.txt](https://github.com/monero-project/monero/files/873359/Processes.txt)

I don't know if this is relevant but I noticed that if I close the gui client I do not encounter any audio stutters and the latencymon report says then that my system is capable of handling real time audio. 
Please let me know if there's any additional information I can provide.



# Discussion History
## hyc | 2017-03-27T18:44:58+00:00
It doesn't seem that monerod is the source of the problems. Your report shows:

> Highest measured interrupt to process latency (µs):   460335.609794
> Average measured interrupt to process latency (µs):   7.911126

> Highest measured interrupt to DPC latency (µs):       402544.491853
> Average measured interrupt to DPC latency (µs):       2.544042

Meanwhile for page faults
> Highest hard pagefault resolution time (µs):          12091.117370

A 12ms max pagefault time is consistent for a hard disk drive. It still doesn't add up to a 460ms latency though.

Note that the pagefault count for monerod is expected, since the blockchain DB uses a memory mapped file. But that activity in itself isn't enough to slow down the system.

## exemar | 2017-03-27T19:00:10+00:00
Ok thanks for your help, guess I'll continue to look for the real cause then. 

# Action History
- Created by: exemar | 2017-03-27T18:14:10+00:00
- Closed at: 2017-03-27T19:00:10+00:00
