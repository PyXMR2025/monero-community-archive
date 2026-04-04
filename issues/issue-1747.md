---
title: Some anti-viruses flag the GUI as malware, let's contact them - Call for action
source_url: https://github.com/monero-project/monero-gui/issues/1747
author: erciccione
assignees: []
labels: []
created_at: '2018-11-21T13:30:50+00:00'
updated_at: '2022-10-20T01:14:34+00:00'
type: issue
status: closed
closed_at: '2019-04-23T17:47:03+00:00'
---

# Original Description
The GUI wallet is often flagged as malware by many ant-iviruses. This is probably because of the integrated miner.
The problem could get worse in time and it's alread causing some minor troubles to windows users. Some anti-viruses even appear to quarantine or deletes files of the wallet without even prompting a warning (see #1742 ), this is causing a poor user experience.

There isn't much we can do except contact the companies and let them know of the issue. Some of them allow to report false positives using a module on their website and some others need to be contacted by email. I'm opening this issue because **i intend to contact them all and let them know of the issue**. I will update this thread with the results. If somebody wants to help, please do.

I uploaded the last GUI wallet (0.13.0.4) on VirusTotal, the results are:
+ **monero-gui-win-x64-v0.13.0.4.zip** flagged as potential malware by **16** of 55 anti-viruses.
https://www.virustotal.com/#/file/ff1b1467dc6252462e5e7818485857ad2ee253712670ff7f5716aa57241577c7/detection
+ **monerod.exe** flagged as potential malwatre by **23** of 66 anti-viruses.
https://www.virustotal.com/#/file/aabfc1a8d4f303721ae64ffb7ad91fbc992da2d774327b740d8c2082023793eb/detection

We have reports of other anti-viruses flagging the GUI as malware, but they are not reported by VirusTotal (like Avira and Malwarebytes). So, **if you are aware of an antivirus not in this list, but that does flag the GUI as malware, please report it here**.

This issue is also related to the CLI wallet, but most of the reports are about the GUI, that's why i'm opening here and not on monero-project/monero.

Anti-viruses:
*(The one i already contacted are checked, i will update this thread with eventual answers. If you wish to help with this, please contact the anti-viruses that are not checked yet)*

- [x] Avira
- [x] Malwarebytes
- [ ] AhnLab-V3
- [ ] Cyren
- [ ] Fortinet
- [ ] Endgame
- [ ] K7AntiVirus
- [ ] Kaspersky
- [x] McAfee-GW-Edition
- [x] McAfee
- [ ] Palo Alto Networks
- [ ] Qihoo-360
- [ ] Sophos AV
- [ ] Sophos ML
- [x] Symantec
- [ ] ZoneAlarm
- [ ] CAT-QuickHeal
- [ ] ESET-NOD32
- [ ] GData
- [ ] K7GW
- [x] Microsoft - https://www.microsoft.com/en-us/wdsi/submission/9db5c5c0-5f43-419a-bf93-452f06341a8f
- [ ] Panda
- [ ] Rising
- [ ] TrendMicro-HouseCall

# Discussion History
## sanderfoobar | 2018-11-21T19:15:23+00:00
Perhaps we should get rid of the integrated miner, for the GUI at least. The miner is meant as a tool to strengthen the network which is a honorable cause, however I fear that only a small percentage of users actually use this feature.

In addition, contacting these companies will probably prove to be futile.

## erciccione | 2018-11-22T13:11:16+00:00
> Perhaps we should get rid of the integrated miner, for the GUI at least

Isn't the miner in the monerod binary? The wallet .exe come out clean from all AV.

> In addition, contacting these companies will probably prove to be futile.

Possible, but the autenticity of the official wallet can be determined by the sha256 hash. I thought they could whitelist the binary with that specific hash after they checked it's autenticity. The problem would remain for self-built binaries, but that's a very small portion of Windows user.
Don't know if they are willing to help with this, but this is becoming a issue from many users and can just be worse with time

## erciccione | 2018-11-22T13:14:22+00:00
From Avira:

> We will update our detection database once the result of the technical analysis is ready. 

That sounds good.

## cryptochangements34 | 2018-11-26T03:09:45+00:00
I'm not sure how anti virus actually works but monerod still needs to be able to hash cryptonight in order to verify blocks and iirc the wallet uses it too for things like KDF so the actual cryptonight code can't be removed or avoided

## xloem | 2019-02-12T14:07:57+00:00
Norton 360 is detecting https://dlsrc.getmonero.org/gui/monero-gui-win-x64-v0.13.0.4.zip as OSX.Trojan.Gen

## CoinAnt | 2019-03-19T03:12:55+00:00
Both Avast and Malwarebytes detect monerod.exe and sometimes even monero-wallet-gui as malware.

## erciccione | 2019-04-23T17:47:02+00:00
Closing after discussion during today's GUI meeting. Please read logs on getmonero.org when they will be available (i will try to remember to update this issue :P)

Edit: Logs https://repo.getmonero.org/monero-project/monero-site/blob/bc2d7e6691bb47e6e3fc09f25ffa7fba67360035/_posts/2019-04-23-logs-for-the-GUI-meeting-held-on-2019-04-23.md

## phil-79 | 2020-09-29T19:39:25+00:00
Kaspersky total security detects 6 files of monero gui wllet incl. monero-ellet-cli.exe.

## Furiouz84 | 2020-10-20T09:38:46+00:00
got 6 hits on oxygen orion install client, Presenokertrojan etc. and some other proved from web als malware. ill check hash, and clean comp now... be warned to always proof hash

## Furiouz84 | 2020-10-20T09:40:07+00:00
Got these 6 hits from Windows internal anti vir(Microsoft)

## matronator | 2021-04-20T08:56:56+00:00
CleanMyMac X's Malware Removal (by MacPaw) tool now also flags the Miner as a threat.

<img width="1103" alt="Snímek obrazovky 2021-04-20 v 10 54 53" src="https://user-images.githubusercontent.com/5470780/115367866-d8eded00-a1c6-11eb-9d2b-0005cc96467b.png">

## jcolson | 2021-07-07T09:11:14+00:00
Bitdefender flags monerod and monero-wallet-gui on MacOS - and REMOVES them

![image](https://user-images.githubusercontent.com/2362647/124732952-a0c79200-df0b-11eb-8345-820d6705dc47.png)


## ebonit | 2021-07-20T09:28:22+00:00
> Bitdefender flags monerod and monero-wallet-gui on MacOS - and REMOVES them
> 

Turn off Bitdefender Shield
unpack and copy the monero gui to a directory outside the Apps directory for instance ~/Monero
drag the gui from ~/Monero to the Dock
add ~/Monero to the safe files in Bitdefender
add ~/Monero to Security->Exceptions to except from scanning
turn on Bitdefender Shield
run the monerogui from the Dock
when you get a warning from Bitdefender choose 'Trust the application'


## richardforrestbarker | 2022-10-19T20:46:31+00:00
Malwarebytes recently reported a couple trojan or compromised IP addresses.

145.239.64.167
165.227.211.106
209.222.252.92

This is after pulling the zip file from https://downloads.getmonero.org/gui/win64

I'm not sure if this is the best place for this, but the malwarebytes did block the attempt. just adding here in case there's something malicious going on 


```
![image](https://user-images.githubusercontent.com/22085800/196797694-a080260e-ba00-4ad5-aca4-426142004787.png)
![image](https://user-images.githubusercontent.com/22085800/196798136-7988e384-77c3-4a22-8901-59a6fdb62b47.png)
![image](https://user-images.githubusercontent.com/22085800/196798313-49c27231-0f62-408f-9653-aeeab3f45b85.png)
```



## selsta | 2022-10-19T23:59:04+00:00
@richardforrestbarker it's a false positive, not much we can do

## richardforrestbarker | 2022-10-20T01:07:15+00:00
@selsta sure - except maybe document where these IPs come from and why they're accessed by the deamon..? 

## selsta | 2022-10-20T01:14:34+00:00
monero is a p2p network, these are just other peers in the network.

Now why are these IP flagged? I don't know. It's possible that someone did malicious things using these IPs in the past and someone else has this IP assigned now.

# Action History
- Created by: erciccione | 2018-11-21T13:30:50+00:00
- Closed at: 2019-04-23T17:47:03+00:00
