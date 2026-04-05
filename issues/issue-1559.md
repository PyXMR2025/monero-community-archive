---
title: 'Feature Request: '
source_url: https://github.com/xmrig/xmrig/issues/1559
author: kio3i0j9024vkoenio
assignees: []
labels: []
created_at: '2020-02-20T18:13:14+00:00'
updated_at: '2020-02-24T19:58:03+00:00'
type: issue
status: closed
closed_at: '2020-02-24T19:58:03+00:00'
---

# Original Description
A feature request to have the miner use one or two less cores (per NUMA node) while users are busy using the system for other important work. But then reuse those cores when system is basically idle.

My reason for this request is that on my primary system (Dell T5500 with dual X5670 Xeons) using all 12 cores and all of the L2 cache results in a very slow responsive system. The only way to have a responsive system while mining was to not use one core in each X5670 Xeon which resulted in five cores and 10MB L2 cache used for each of the two X5670 Xeons. That gave my system two free idle cores (one per NUMA node) and freed up 4MB L2 cache. The system was again responsive and useful for everyday work even while mining.

To do the above I had to manually edit the config.json file to exclude one core from each NUMA node. This was time consuming and error prone.

My feature request would be for some way to do the removing (and re-adding them back) one or two cores from each node easily (for all the algorithims). That way when needing to be productive on the system remove the one or two cores from mining but when going to lunch, or for the night or just stepping away then add them back in for better mining hash rates.

During initial running of XMRig the core count for mining usage is just as it was. In my system of dual X5670 Xeons that would be 12 cores total or 6 for each NUMA node. There needs to be no changes to how XMRig determines this.

My system has cores [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] available for mining.
NUMA NODE 0: [0, 1, 2, 3, 4, 5]
NUMA NODE 1: [6, 7, 8, 9, 10, 11]

Maybe this feature could be implemented as an option to the config.json file as a number field and function as follows:

// Use all the cores
Mining_Core_Reduction: 0

// Remove one core from each NUMA node from mining, I suggest the first one in the NUMA node
Mining_Core_Reduction: 1

// Remove two cores from each NUMA node from mining, I suggest the first ones in the NUMA node
Mining_Core_Reduction: 2

Then in the XMRig application when running a single keystroke to either use all the defined core or reduce the cores for mining by the Mining_Core_Reduction value.

In Use on my system I would set "Mining_Core_Reduction" to the value of 1 and in the running XMRig would toggle a key (maybe - minus key) to reduce the available mining cores from 12 to 10 when needing the system to be productive and then toggle a key (maybe + plus key) to go back to full out mining on all 12 cores when I step away from my system.

So as an example for having this on my system:

Initial running of XMRig configures config.json with all twelve cores [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and has the "Mining_Core_Reduction" option set to 0.

Stop XMRig and then edit config.json and set "Mining_Core_Reduction" option to 1.

Run XMRig and it will be using 10 cores [1, 2, 3, 4, 5] and [7, 8, 9, 10, 11]. Then when I want to step away I hit the "+" key in XMRig and the system is back to full out mining on all 12 cores [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and again when I want to be productive I hit the "-" key and XMRig would then only use 10 cores [1, 2, 3, 4, 5] and [7, 8, 9, 10, 11].






# Discussion History
## DocDrydenn | 2020-02-20T19:01:16+00:00
Seems like that feature would have such a small use-case for a developer to even want to mess with... Majority of mining is being done on non-production machines. 

I'm not trying to be negative here... it is a good idea, just not very realistic to implement. Who knows, maybe the devs will add it. In the meantime, consider the below workaround.

Most OS's offer task management in some form or another... Have you considered using that to control your mining?

On Windows, the Windows Task Scheduler has idle triggers that would do exactly what you want. You could have the Scheduler run XMRig with a config specific to your "In-Use" desires and another task that stops the "In-Use" task and fires off a new XMRig with a config specific to your "Idle" desires. These tasks would just toggle back and forth depending on if the machine is idle or In-Use. 

I know this works because I've done it on multiple home desktop computers. It takes learning how the Scheduler works, but it is completely doable.

Good luck.

## kio3i0j9024vkoenio | 2020-02-20T21:09:50+00:00
Quote: Seems like that feature would have such a small use-case for a developer to even want to mess with... Majority of mining is being done on non-production machines.

I'm not sure that the Majority of mining is being done on non-production machines. A lot of the posts in the Welcome to the world of Monero mining! forum are filled with individuals who are using their own machines to mine on while still using their machine for other tasks.

Quote: Most OS's offer task management in some form or another... Have you considered using that to control your mining?

There really is none that would work as I described as they would not free up the L2 cache and thus the system would still a very slow responsive system.

The only way to have a responsive system is to either not mine or do as I currently do by disabling 2 cores from mining.

As for the difficulty in implementing this feature I really don't see it as taking much time. I am even willing to try to implement it if I could be given some pointers.



## DocDrydenn | 2020-02-21T00:34:05+00:00
Did you even read what I wrote? Did you even attempt to do what I suggested? How are you telling me it can't be done when I'm doing exactly what you are asking?

Windows Task Scheduler. Two tasks. Two XMRig config files.

Task 1: Computer is not Idle (i.e. In-Use)
Description: This task launches XMRig with ConfigA.
ConfigA: XMRig config setup to only use 10 cores.
Task Trigger/Start: When computer is not Idle.
Task Exit: When computer becomes Idle.
.
Task 2: Computer is Idle (i.e. not In-Use)
Description: This task launches XMRig with ConfigB.
ConfigB: XMRig config setup use all 12 cores.
Task Trigger/Start: When computer is Idle.
Task Exit: When Computer is not Idle.

Your request isn't the first of its kind I've see, yet I haven't seen one mainstream miner implement anything close to it and I explained why. 

This is a working fix/solution for what you want. Enjoy... or don't. Whatever.

## SChernykh | 2020-02-21T08:59:51+00:00
> My system has cores [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] available for mining.
NUMA NODE 0: [0, 1, 2, 3, 4, 5]
NUMA NODE 1: [6, 7, 8, 9, 10, 11]

Do you have HT disabled? Enable HT, set priority to 0 and yield to true in config to have a responsive system.

## BlankerL | 2020-02-23T08:33:32+00:00
It is just a priority issue, you can directly set the priority with Task Manager or Process Lasso or something else. 

# Action History
- Created by: kio3i0j9024vkoenio | 2020-02-20T18:13:14+00:00
- Closed at: 2020-02-24T19:58:03+00:00
