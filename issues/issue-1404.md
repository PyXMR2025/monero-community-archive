---
title: CPU threads not working after system reboot
source_url: https://github.com/xmrig/xmrig/issues/1404
author: Bathmat
assignees: []
labels: []
created_at: '2019-12-11T19:50:58+00:00'
updated_at: '2019-12-12T22:58:36+00:00'
type: issue
status: closed
closed_at: '2019-12-12T14:35:33+00:00'
---

# Original Description
After a system reboot and starting the miner, one (or more) threads will stop working. Occasionally, the whole cpu slowly loses hashrate until it's near zero. Restarting the miner usually fixes the issue, but sometimes requires more than one restart to get consistent hashrate without threads dying.

Here is the threads data for dual E5-2670v2 taken from the API showing thread 2 dead:

```
threads: [
[
431.21, 431.01, 431.12
],
[
null, null, 0.21
],
[
430.81, 423.37, 424.17
],
[
431.91, 432.03, 431.5
],
[
437.35, 438.14, 437.81
],
[
437.4, 433.92, 436.87
],
[
435.89, 436.38, 436.26
],
[
436.37, 434.92, 435.71
],
[
431.16, 432.03, 431.3
],
[
435.93, 436.61, 436.56
],
[
427.54, 430.66, 430.64
],
[
429.71, 429.99, 429.17
],
[
429.71, 429.76, 428.33
],
[
431.21, 430.61, 430.46
],
[
436.64, 436.43, 436.4
],
[
429.71, 426.78, 425.85
],
[
431.16, 430.66, 430.55
],
[
179.91, 138.13, 125.51
],
[
335.41, 372.28, 386.32
],
[
433.37, 432.14, 431.71
]
]
```
 - OS: Win10 1903
 - Algo: RandomX
 - Version: 5.2.0

Same issue when compiled with both GCC and MSVC and on different machines.

# Discussion History
## xmrig | 2019-12-12T06:20:13+00:00
Can you check is restart only CPU threads (instead of whole miner) revert hashrate back or not?
It can be done by setting `"enabled": false,` in `cpu` object and then `"enabled": true,` in config file.
Thank you.

## Bathmat | 2019-12-12T13:56:08+00:00
CPU `enabled:` `true` -> `false` -> `true` restarted full hashrate briefly, but behavior returned after a short bit (within a few minutes).

More strange behavior: When I log into the machine using Chrome Remote Desktop, hashrate returns as with the above CPU enable behavior, but dies again after I log out.

I've noticed this behavior since RandomX was introduced and it was definitely present in version 3.x.x (beta and dev too). I've wondered if it's something on my end since I launch the miner in a shell using a javascript program, and previously, restarting the whole javascript program seemed to be the only way to get full hashrate to work correctly.

I may have fixed the issue by changing `Priority` from `Below normal` to `High` in Windows Task Manager. (It's possible that even setting `Normal` might fix the issue). I'm unsure why the task has such low priority after a reboot, but I'll keep investigating and see if I can change the default settings/behavior.

Here is another example of a Ryzen 1700 showing all threads dead a few minutes after system reboot and miner start:
```
hashrate: {
	total: [ null, 1887.01, null ],
	highest: 4786.8,
	threads: [
		[ null, 201.68, null ],
		[ null, 232.09, null ],
		[ null, 239.54, null ],
		[ null, 269.15, null ],
		[ null, 258.65, null ],
		[ null, 232.18, null ],
		[ null, 261.72, null ],
		[ null, 191.99, null ]
	]
},
```

## Bathmat | 2019-12-12T14:35:33+00:00
I believe this is fixed by changing Windows Task Scheduler priority. Not sure exactly when that started affecting the miner's behavior (or possibly a Windows Update changed a setting), or perhaps it's been the case all along but I never noticed it. I'll close the issue for now.

Resources in case others have the same problem: 
[Microsoft Docs](https://docs.microsoft.com/en-us/windows/win32/taskschd/tasksettings-priority)
[Stack Overflow](https://stackoverflow.com/questions/2427142/is-there-any-way-for-a-win2k8-scheduled-task-to-have-normal-priority-io)
[Cognition](https://www.cognition.us/_pvt_wiki/index.php/Making_a_Scheduled_Task_Run_with_Normal_Priority)

## xmrig | 2019-12-12T16:57:25+00:00
Can you also check `priority` option https://github.com/xmrig/xmrig/blob/master/src/config.json#L27 ? for example `2` or `3`, possible values for this option is range from `0` (idle) to `5` 0 idle (highest). Default `null` value means miner don't change priority at all.
Thank you.

## Bathmat | 2019-12-12T17:01:19+00:00
Changing priority in the config did not change the `Base priority` in Task Manager, so I don't think that solves the issue.

## xmrig | 2019-12-12T17:05:32+00:00
It change priority of main thread and mining threads, but thank you anyway I will check about `Base priority` little later.

## Bathmat | 2019-12-12T21:46:58+00:00
I tried testing priority a little more, and it appears that `priority: 5` also might solve the issue even with Base priority `Below normal`.

Update: It appears that `priority: 4` also works, but `3` does not. Difficult to say for sure since the behavior can be random.

# Action History
- Created by: Bathmat | 2019-12-11T19:50:58+00:00
- Closed at: 2019-12-12T14:35:33+00:00
