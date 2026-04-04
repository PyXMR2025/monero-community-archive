---
title: '[Add ASAP/URGENT] Limiting Disk Cache / Memory Usage / Access Speeds'
source_url: https://github.com/monero-project/monero-gui/issues/1862
author: SBSeed
assignees: []
labels:
- invalid
created_at: '2018-12-25T18:07:14+00:00'
updated_at: '2019-02-08T14:45:33+00:00'
type: issue
status: closed
closed_at: '2019-02-08T14:45:33+00:00'
---

# Original Description
massive issue which is causing 75% of the issues people are having...
this is leading to memory leaks, disk pagefile/cache freezing and more.
(information here is relative and percentages are not completely accurate since there is no current way to monitor every detail, or even with any accuracy, of monero hardware usages)

sadly most (if not all) of the problems that people are having with the crashing/freezing or partial of same of their systems no matter the OS or Hardware used, this also is not repeat NOT from physical hardware breakdowns (such as disk sector degradation)...

this is basically a false-positive of looking at logs and why ibdm blockchain data is/can become corrupted...

this type of uncontrolled usage of cache/memory is causing computers/servers to disconnect from the internet mid or late download as well as corruption of blockchain through partial or full freezing of OS and system because monerod.exe/monero-GUI/monero-blockchain-import.exe etc. ALL have this same problem (why this has never been addressed is beyond me) within the coding of the programs/apps.

because the programs/apps do not limit cache/memory/page file usage and clear/purge old information  as the program runs it overloads the cache/memory/page files and causes hell with any OS... currently the only way to clear/purge this information is by completely restarting the computer, this is a huge problem that needs to be fixed NOW!

there has to be hardcoding for limiting usage by setting a maximum percentage that the programs/apps use... this has been a misdiagnosis for YEARS and apparently no one even considered this as a potential issue or cause of most of the symptoms that people have been dealing with or complaining about connect-ability/blockchain data/etc.
through looking through old issues/bugs researching commands for CMD/console commands and personal investigation i have been able to find this and seeing how the programs work (especially on Win7 OS-PC) uses hardware...

if you use any webbrowsers or similar internet software at the same time as downloading/processing the blockchain through monero programs this is magnified by 50%, and is exponential in usage beyond this...
compairing downloading of usage's between just running the programs/apps with the blockchain and using browsers/etc. the time to crash/freeze is halved, the next program/browser used causes crashing/freeze down to 1/4 and so on...
this is also the case with using blockchain.raw (much MUCH less of a problem) when importing to imdb for monero programs to use to sync etc., using blockchain.raw is probably 75% (probably much higher) less problematic and less likely to cause these issues than downloading blockchain directly.

it has taken a week or so of looking into this (probably only a 2-3 days total) to notice this, the only reason i did notice is because of how i am able to view/process information in a completely different way to most people but it still surprises me to see no one else caught onto this before....

bottom line: these has to be addressed now or this will create worse problem with connecting and using monero in the future (this already effects the blockchain information and therefore effects recieving/sending of monero)

i would suggest adding controls for controlling usages of application of hardware and software...
- cache usage min 10% to max 75% (i think this would be good for most PCs that are not dedicated to monero usage)
- memory usage proper purging of information from physical memory and page files/virtual memory
- limitation on disk access speeds similar to cache usage (possible to do this for network interfacing as well)

# Discussion History
## xiphon | 2018-12-25T18:56:08+00:00
You must be kidding, but in the case you are serious:

> cache usage min 10% to max 75% (i think this would be good for most PCs that are not dedicated to monero usage)
> memory usage proper purging of information from physical memory and page files/virtual memory

That is what any OS and hardware are doing. Read OS docs to find out whether it supports per-process cache limiting and how to configure it.

> limitation on disk access speeds similar to cache usage (possible to do this for network interfacing as well)

Yep, disk access throttling might be implemented. 
But it won't resolve any problems if the underlying hardware doesn't provide enough disk I/O bandwidth and Monero daemon hits the limit.

## pazos | 2018-12-27T22:22:29+00:00
> sadly most (if not all) of the problems that people are having with the crashing/freezing or partial of same of their systems no matter the OS or Hardware used, this also is not repeat NOT from physical hardware breakdowns (such as disk sector degradation)...

IMO problems in the GUI are related to the deattached start of monerod and further communications when it is busy because we (the gui) don't know that is busy until we do a request and then we need to wait for a response (in most cases blocking the UI thread). This will throw a warning on most OSes saying that the program is frozen. More info on issue #1522 

> this type of uncontrolled usage of cache/memory is causing computers/servers to disconnect from the internet mid or late download as well as corruption of blockchain through partial or full freezing of OS and system because monerod.exe/monero-GUI/monero-blockchain-import.exe etc. ALL have this same problem (why this has never been addressed is beyond me) within the coding of the programs/apps.

monerod is beautiful as-is and shouldn't be artificially limited. I know it is cpu intensive to download and verify the blockchain but setting a limit just make the things worse, not better.

> massive issue which is causing 75% of the issues people are having...

75% of statics are wrong :smile: 

> if you use any webbrowsers or similar internet software at the same time as downloading/processing the blockchain through monero programs this is magnified by 50%, and is exponential in usage beyond this...
compairing downloading of usage's between just running the programs/apps with the blockchain and using browsers/etc. the time to crash/freeze is halved, the next program/browser used causes crashing/freeze down to 1/4 and so on...
this is also the case with using blockchain.raw (much MUCH less of a problem) when importing to imdb for monero programs to use to sync etc., using blockchain.raw is probably 75% (probably much higher) less problematic and less likely to cause these issues than downloading blockchain directly.

Please leave the GUI alone while downloading and verifying. Please do use other programs as much as you want. You will see that monerod is using most cpu time but you can't change that since monerod is actually working on the background and the browser can stay idle once a page is rendered (if you run other cpu-heavy programs like video renders you'll see that cpu time is distributed almost equally between them).

>  this is a huge problem that needs to be fixed NOW!

You have a few options:

1. fix the issues you find yourself
2. contract a developer to fix some issues.
3. open a bounty for enhacements at https://www.bountysource.com/
4. contribute to a FFS
5. reward current contributors with words of wisdom and hope that somebody, in his/her free time, fix that for you.

## SBSeed | 2018-12-28T00:09:22+00:00
@xiphon: why would you think i was joking?

@pazos:
- its not the CPU usage that is the issue, this can be limited by command settings before you run monerod with or without the GUI...
- monero-GUI and monerod ALREADY have a limit set on how much CPU usage happens
- WHEN the hardware caching and speeds are maxed this creates a idle cascade effect that causes issues and plays havoc with other programs
- the caching and accessing speeds will and DO top out and cause freezing since they are not controlled this can cause multiple issues to accure over time including creating what would appear to be a memory leak (this can easily be recreated on any PC)
- the same can and does happen with physical memory, the OS does a dump to physical memory and causes false reporting on physical memory usage which then causes further problems with operations and halts on the OS and hardware which causes total system freeze and you have to physically force shutdown

i might try a bountysource thing, however as things currently stand i have no money to donate (i am completely dependent on the state/gov because i am disabled) this is part of why i am even bothering to post anything (i would rather NOT waste my time and efforts) in the first place...
i am hoping that the Developers/programmers take this information into account and fix or add to monero project so that it becomes more stable, and so that more people can use it (or becomes more widely usable to laymen)...

it is becoming more and more essential to have alternatives to paper money as it is consistently losing value because it is made from air and is not finite.

-edit-
also, let me rephrase the percentages thing:
this CAN BE ATTRIBUTED TO MOST BUGS/FREEZING/MEMORY LEAKS/HARD DRIVE BAD CLUSTERS/PHYSICAL MEMORY MAXING OUT/ETC. as a cascade type of effect.

## sanderfoobar | 2019-02-08T14:18:53+00:00
I am certain #1920 will 'fix' some performance issues some are seeing. I am going to close this issue for now and if there is any doubt about the inner workings of blockchain syncing, I suggest opening a PR on the [main repository](https://github.com/monero-project/monero), not the GUI repository. We are strictly for GUI related issues.

I thank you for the investigations. Please be aware you can also choose to fix the complaints you have yourself by submitting a pull request.

+invalid

# Action History
- Created by: SBSeed | 2018-12-25T18:07:14+00:00
- Closed at: 2019-02-08T14:45:33+00:00
