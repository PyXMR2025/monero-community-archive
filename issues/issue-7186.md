---
title: '[Big Problem?] Monerod memory leak'
source_url: https://github.com/monero-project/monero/issues/7186
author: setuidroot
assignees: []
labels: []
created_at: '2020-12-25T08:36:44+00:00'
updated_at: '2021-01-09T01:35:06+00:00'
type: issue
status: closed
closed_at: '2021-01-09T01:35:06+00:00'
---

# Original Description
I had my monerod node running fine (without any ban list) since the v0.17.1.7 release.  It crashed on my server earlier today and when I went to restart it *monerod* starting eating up all my RAM and eventually it was OOM killed after it ate ~7 GB of RAM and ~13 GiB of swap space.  I can't even run my node now because every time I restart it, it starts eating my RAM until it's OOM killed.  I tried adding the popular ban list (https://gui.xmr.pm/files/block.txt) and this seemed to help (it took longer for monerod to start eating all my RAM.)  So I'm thinking this is something brought about by the malicious nodes.  This is pretty serious I think.  I'm too tired to even really think about it now, but this is a problem.  I can't run my monerod node anymore because it just eats all my RAM until it gets OOM killed.

Is this a known problem?  I mean... this seems like it could crash the entire network.  I'm not sure how it's being done... but my node barely downloads *anything* (like ~20 MiB) downloaded trying to resynchronize the blockchain when it starts eating all my RAM.

I'm running the v0.17.1.7 release that I compiled myself on my server.  I've never had this problem at all until today.  I will try to get more information later... too tired to think right now.  I just thought somebody should know about this.

==== Update (3 days later) ====

Just an update: I have my node working now.  I'm still using the same binary build of the v0.17.1.7-release branch that I compiled when v0.17.1.7 was first tagged.  It's working fine for me since I've applied selsta's block_tor.txt list.  Just add --ban-list /path/to/block_tor.txt when starting monerod.  I recommend using the *full* path to the block list. Example:

````
./monerod --ban-list /home/monero/banlist/block_tor.txt
````

You should also use the *full* path for monerod.  Always good to give the system the full path to a file.

Keep in mind that this ban list is constantly updated thanks to selsta and community members.  I think when you update block.txt, you'll have to restart monerod.  I might be wrong about this, but restarting it makes sure the updated list is applied.

As for the resource exhaustion... how was this done?  It seems like a very serious vulnerability... good thing we can patch it now.  I hope Monero does a postmortem on this.



# Discussion History
## armerpunkt | 2020-12-25T09:15:16+00:00
I had the same thing happen, it was running fine until about 11 hours ago at the time of this post when it crashed and I had an out of memory error.  Running the official v0.17.1.7 Windows 64-bit release. Just noticed now and restarted monerod, and the memory use keeps climbing (in 20 minutes it was up to around 4 GB of RAM).  Another thing I've just noticed, though not sure if it's related, is that it's constantly 2 blocks behind in syncing (so right now it says 2259812/2259814)

## setuidroot | 2020-12-25T09:28:07+00:00
> I had the same thing happen about 11 hours ago at the time of this post. Running the official v0.17.1.7 Windows 64-bit release. Just noticed now and restarted monerod, and the memory use keeps climbing (in 20 minutes it was up to around 4 GB of RAM). Another thing I've just noticed, though not sure if it's related, is that it's constantly 2 blocks behind in syncing (so right now it says 2259812/2259814)

The 2 blocks behind has to do with the malicious nodes that are falsely reporting 2 blocks ahead of where the blockchain is really at.  It'll help if you apply the ban list I referenced before.  Add --ban-list */path/to/ban/list/block.txt*  They have some better explanations of how to do this on the Monero subreddit.

As for the memory leak... 11 hours for us both?  I wonder if it's possible we got some kind of maliciously tainted block from the malicious nodes.  I'm just guessing here.  Maybe popping blocks by ~12+ hours and resynchronizing the chain would help?  I don't know... I need sleep before I can do much else.  It's good to know I'm not alone with this issue 🤔 but also kind of bad to know that because this could be serious for the network.

I forgot to say I run Ubuntu 20.04.  I compiled mine from source and you are having the same problem with the official release... that's not encouraging :/ I was hoping the official release might fix it lol.  I can't really think well now so I'm just going to leave my node off for now.  If you find a fix or something let me know.


## bgmastermind | 2020-12-25T10:34:30+00:00
I'm on v0.17.1.6 and in the last 24 hours I've had the monerod killed from OOM killer 5 rimes. At first the machine was running with 4 GB RAM. It was perfectly fine. When that happened I increased it to 8. It got killed again. Now it's running with 16GB and still getting killed. Something is indeed wrong. I'm running the release, not compiled.

## selsta | 2020-12-25T10:36:30+00:00
Please see: https://reddit.com/r/Monero/comments/kjrub1/_/ggyiids/?context=1

The linked comment includes a workaround. We should have a new release out hopefully soon.

## dwjorgeb | 2020-12-25T11:07:16+00:00
I was running v0.17.1.5 and around 12h ago it started giving RPC errors and eventually ran OOM, while using 110GB (!) of RAM!

Something very fishy is going on.

Meanwhile, I've updated to .7 and now it is kinda holding, but I'm still getting some RPC errors

## selsta | 2020-12-25T11:09:32+00:00
Please apply the following ban list as a temporary mitigation: https://gui.xmr.pm/files/block_tor.txt

There is a large network DoS going on, we are working on a fix and new version.

## armerpunkt | 2020-12-25T11:24:57+00:00
Thanks for the tip, selsta. Using the new block_tor list seems to have mitigated the problem.  It's holding steady at around 300 MB of RAM now and no longer 2 blocks behind. Though I am getting a ton of "SYNCHRONIZED OK" messages.

## moneromooo-monero | 2020-12-26T03:25:36+00:00
https://github.com/monero-project/monero/pull/7190 should fix this particular memory exhaustion

## ghost | 2020-12-27T01:15:41+00:00
I'm having the same issue running v0.17.1.7 on a Debian 10.6 server. The server is used only as a node with 8GB of RAM and 8GB of swap. Monerod still managed to consume all of it. I restarted the server and the daemon crashed again.

## bill-mcgonigle | 2020-12-27T14:48:22+00:00
[workaround]
I'm still seeing memory spikes even with the Tor blocklist.

Rather than wait for the machine to swap to death and count on OOM to do something sensible, I have monit keeping an eye on it:

```
# cat /etc/monit/monitrc.d/monerod   
check process monerod with pidfile /path/to/my/monerod.pid
 start program = "/bin/systemctl start monerod"
 stop program  = "/bin/systemctl stop monerod"
 if total memory usage > 2.4 GB for 5 cycles then restart

```
(adjust for your service name and pid location)

It seems to run for about 50 minutes then need a restart. At least it's up 90% of the time.



## cvandesande | 2020-12-27T15:01:47+00:00
> #7190 should fix this particular memory exhaustion

I rebuilt off master because the Raspberry 4 8GB would not be able to sync the blockchain without running out of memory for the last few days. Running (v0.17.0.0-7438617bb) it's up to 90% and holding at 1.8G of memory in use. Much better now. 


## hyc | 2020-12-27T20:46:03+00:00
@bill-mcgonigle You shouldn't be triggering off total memory usage. You should be using total memory minus shared memory usage. Otherwise you'll be killing a normally operating daemon most of the time.

## setuidroot | 2020-12-28T05:28:10+00:00
> I'm still seeing memory spikes even with the Tor blocklist.

I like that you're trying to find better ways of containing this memory leak.  I recommend you try updating the block_tor.txt list.  Selsta is very active constantly updating this list and I haven't had a problem using the latest list.  You could set a cronjob to check for updates of the list and restart monerod if new IPs have been added to it. 

> It seems to run for about 50 minutes then need a restart. At least it's up 90% of the time.

You could limit monerod's memory usage by using a control group (cgroup.)  You can create a cgroup with a memory limit and then add the user that you run monerod as to this cgroup.  I'm not going to try to explain this in detail... you'll find better explanations online.  Like [here](https://unix.stackexchange.com/a/125024) and some more info about using ulimit (another option) and cgroups [here.](https://stackoverflow.com/q/26860822)

If you would like me to go into more detail, just let me know.  I'm happy to help.

It would be cool to have a flag for limiting memory usage in future Monero release versions.  Kind of like the **--limit-rate** flag for limiting bitrate/bandwidth usage.  We could have a **--limit-memory** flag for capping monerod's maximum memory usage.


## undeath | 2020-12-28T09:32:46+00:00
> You could limit monerod's memory usage by using a control group (cgroup.)

If you're using systemd it's as easy as adding to your `[Service]` block.

```
Restart=always
MemoryAccounting=yes
MemoryHigh=4G
MemoryMax=4G
```

replace `4G` with a sensible limit for your server

## selsta | 2020-12-30T23:01:40+00:00
v0.17.1.8 is out: https://www.getmonero.org/downloads/

## selsta | 2020-12-31T13:48:15+00:00
New attack, seems like the tor block list is required again: https://gui.xmr.pm/files/block_tor.txt

This does not seem related to the attack fixed in v0.17.1.8

## dwjorgeb | 2020-12-31T14:21:06+00:00
> 
> 
> New attack, seems like the tor block list is required again: https://gui.xmr.pm/files/block_tor.txt
> 
> This does not seem related to the attack fixed in v0.17.1.8

has the list been updated, or can I use the same one I downloaded last week?

## selsta | 2020-12-31T14:21:39+00:00
Same list.

## guedressel | 2021-01-08T19:35:15+00:00
v0.17.1.9 is out: https://github.com/monero-project/monero/releases/tag/v0.17.1.9

## moneromooo-monero | 2021-01-09T01:35:06+00:00
Fixed. Please open a new one should another crafted packet do that again.

# Action History
- Created by: setuidroot | 2020-12-25T08:36:44+00:00
- Closed at: 2021-01-09T01:35:06+00:00
