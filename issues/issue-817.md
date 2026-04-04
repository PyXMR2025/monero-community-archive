---
title: Monero daemon process should be @ lowest possible priority
source_url: https://github.com/monero-project/monero-gui/issues/817
author: walsall
assignees: []
labels: []
created_at: '2017-08-11T13:17:43+00:00'
updated_at: '2023-08-14T12:44:35+00:00'
type: issue
status: closed
closed_at: '2023-08-13T23:59:57+00:00'
---

# Original Description
Monerod on Windows: Process priority is "Normal" which causes user response lags in browsers etc.; process priority should be "Low" instead (to run Monerod only when computer would otherwise be idle). 

An example of proper process priority is the BOINC scientific computing software, which correctly uses "Low" process priority in order to avoid interfering with any other computer usage. For no apparent reason, Monerod is running at "Normal" priority (same priority as browsers, spreadsheets, etc.) which means the user will encounter poor interactive response time. Workaround is to manually set the priority of the Monerod process to "Low", but many users will not know how to do that, and even those who are that knowledgeable will have to perform the workaround manually after each reboot (a PITA). 

Unless your computer is also running another low-priority CPU-bound task (such as BOINC), it spends the vast majority of its time running a special "Idle" task which exists only to waste time. That idle time is what the category of software which includes scientific computing, coin mining, etc. is designed to put to productive use. During night hours, PCs are nearly 100% idle. And during casual use such as browsers and spreadsheets, the idle time is typically 50 to 75%. There's plenty of CPU left for Monerod to use at "Low" priority.

New Monero installations immediately generate complaints from non-technical users about the sudden appearance of browser lags, etc. immediately after Monero installation, and after the Monerod process priority is set to to "Low" those complaints go away.

The same process priority fix should also be applied to other platforms (Linux, Mac, etc.).


# Discussion History
## Hueristic | 2017-08-22T15:57:29+00:00
I agree when used on a winblows system as a background process just downloading the chain effect performance across all cores and hogs disk activity. 

I personally lower priority to below normal and set affinity to one core as well as lowering IO operations to idle with Process explorer.

But this should be the default IMO.

## ghost | 2017-09-11T12:09:16+00:00
I would like to endorse this viewpoint.

From time to time, monerod.exe causes small lag spikes for a fraction of a second, for example in audio or video output. This happens on multiple systems, running Windows 10.
For now, when gaming, watching video, or listening to music, it's better to shut down monerod.exe. I would prefer to be able to keep it running all the time to support the network. I hope this can be improved in a future update.

## SleepswithGators | 2018-02-22T00:59:00+00:00
Do we open "Resource Monitor" to complete this action?


## Hueristic | 2018-02-22T18:08:05+00:00
TaskManager -> Processes -> Set Priority

Or there is a nice program that I love called  Process Lasso That will allow you to set all the priority and core affinities and have them stay set after a reboot.

## ghost | 2018-02-22T23:08:08+00:00
I know there are ways to set processes at the lowest priority, but if we want to improve usability of the Monero software, it would be a plus if the deamon could run in the background without causing lag. Even at --max-concurrency 1, the deamon still causes lag spikes from time to time. I'm using an eight-core Ryzen at the moment, but this also happens on Intel CPUs. It sucks. No other heavy computation process, game, running multiple VMs, or compressing a file with 16 threads, does this. Monerod.exe is the only process I have ever encountered that causes the keyboard to hang, or the sound to hang. Setting priority or affinity seems to have no effect whatsoever. Once every few minutes, you get a few-second lag spike.

## Hueristic | 2018-02-23T04:03:26+00:00
Lower the I/O priority to below avg. 
But yes it should be addressed.

## ghost | 2018-02-23T12:55:53+00:00
By the way it is most easily reproducible to get his lag spike by typing exit in the deamon. During the shutdown process you get a short mouse/keyboard/sound hang.

## selsta | 2023-08-13T23:59:57+00:00
There haven't been complaints like this in a while, I don't think setting priority to lowest possible is necessary at this point.

## mmortal03 | 2023-08-14T01:14:36+00:00
@selsta , I don't think it should be the default, so no issues with closing the issue, but like @Hueristic said regarding Windows, a person can lower the priority and affinity by putting something like the following in a batch file (it's what I do on my very low-end Windows machine that I use as a server, to make it less likely to use enough of the CPU to interfere with another process):
start "" /low /affinity 2 monerod.exe

## Hueristic | 2023-08-14T12:44:35+00:00
> There haven't been complaints like this in a while, I don't think setting priority to lowest possible is necessary at this point.

Translation: I've ignored this long enough I consider it moot.

# Action History
- Created by: walsall | 2017-08-11T13:17:43+00:00
- Closed at: 2023-08-13T23:59:57+00:00
