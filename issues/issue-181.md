---
title: Best configuration for 4x cpu, E7-4850
source_url: https://github.com/xmrig/xmrig/issues/181
author: xtrojan1
assignees: []
labels:
- NUMA
created_at: '2017-10-29T13:19:02+00:00'
updated_at: '2019-08-02T12:38:03+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:38:03+00:00'
---

# Original Description
Hi,

I do not know what and the best configuration for E7-4850., i have 4 cpu(Processor) in the server.
Performance
of Cores 10,     10 x 4cpu =40 core
of Threads 20,     20 x 4cpu = 80 threads
Processor Base Frequency 2.00 GHz
Max Turbo Frequency 2.40 GHz
Cache 24 MB SmartCache
I do not know how to compute the (cpu inffinty) for my 4x, E7-4850.

I also think that if I put too many hearts sela works less well.

Is there a best practice for windows OS servers 2012R2?

do you have an answer or a link to my questions.

thank you in advance

# Discussion History
## NmxMilk | 2017-10-29T18:30:40+00:00
the bottleneck being cache size (2M = 1 thread), you should go for 12 threads per CPU.
CPU affinity is a bitwise mask for your logical cores:
1 cpu = 20 threads = 20 bit mask
mask = 1111 1111 1111 1111 1111
use   = 1010 1010 10 10 1010 1010   =  use 10 out of the twenty
hexa affinity = 0xAAAAA

For a double socket this will be 0xAAAAAAAAAA
and for a quad socket : 0xAAAAAAAAAAAAAAAAAAAA



## xtrojan1 | 2017-10-30T08:18:27+00:00
thanks a lot, i will try it..

## angel12 | 2017-10-30T16:32:34+00:00
I have 4x e7 4860, and currently I can only get about 40% - 50% cpu usage, even when max cpu set at 100. I also see this in my xmrig window:

CPU: Intel(R) Xeon(R) CPU E7- 4860 @ 2.27GHz (2) x64 AES-NI

Does this mean it is only using (2) of the 4 CPU's?

## NmxMilk | 2017-10-30T19:08:19+00:00
You should have a look at the NUMA issue #86.
Maybe your case too.

## xtrojan1 | 2017-11-01T12:28:38+00:00
start /node 0 xmrig.exe --threads=11
start /node 1 xmrig.exe --threads=11
start /node 2 xmrig.exe --threads=11
start /node 3 xmrig.exe --threads=11

for all i have 1.360 h/s
https://drive.google.com/file/d/0B4yy8QDExEZ1anNxQVlvRjBIeTQ/view

but i do not use cpu affinity,

how to add cpu affinity on my configure?
do you have an answer or a link to my questions.

thank you in advance

## xmrig | 2019-07-29T02:19:20+00:00
If this issue still actual, please check v2.99.2-beta release #1077.
Thank you.

# Action History
- Created by: xtrojan1 | 2017-10-29T13:19:02+00:00
- Closed at: 2019-08-02T12:38:03+00:00
