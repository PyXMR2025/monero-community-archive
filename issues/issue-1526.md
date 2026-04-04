---
title: 'balance is zero  '
source_url: https://github.com/monero-project/monero-gui/issues/1526
author: whenswineflu
assignees: []
labels:
- resolved
created_at: '2018-07-27T22:46:14+00:00'
updated_at: '2018-12-17T09:00:35+00:00'
type: issue
status: closed
closed_at: '2018-12-17T09:00:35+00:00'
---

# Original Description
no log ?

# Discussion History
## dEBRUYNE-1 | 2018-07-28T09:00:19+00:00
Use:

https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance

## whenswineflu | 2018-07-28T22:09:12+00:00
ahh I thought would be hearing from you yeah I tried that few times my issue been on going and did start at the fork I am new monero not crypto  so that did work and my funds show up as I was learning wallet got closer to sum  eg first time was 3 /56  I sync with remote node would go back to 0 so start over from mnemonic seed 25 word and my .bitmonero added up with new gui wallet names each time  balance got closer to the sum same wouldent let me send out  and remote node 0 out so del the .bitmonero folders   I started with gui 0.12.1.0  didnt have much luck when 0.12.2.0  came out started  and I got all my funds started having probs with hdd  old  and full hdd I didnt like was taking to long    bought new and sdd  and hdd  i,m running windows 10 insiders build ![screenshot 128](https://user-images.githubusercontent.com/25366386/43360954-ace2d02e-9277-11e8-92ae-db23c6bf06c6.png)  

## dEBRUYNE-1 | 2018-07-29T16:23:48+00:00
Have you tried using GUI v0.12.3.0? 

## whenswineflu | 2018-07-30T18:27:58+00:00
yes right now nothing working Win32/CoinMiner  flag as trojan 


## dEBRUYNE-1 | 2018-07-31T10:22:00+00:00
You have to add an exception for the GUI v0.12.3.0 directory / folder and take executables out of quarantine in case they were quarantined by your AV (AntiVirus). 

## whenswineflu | 2018-08-03T23:33:40+00:00
went back to 0.12.0 same no coins 


## whenswineflu | 2018-08-03T23:35:11+00:00
going to read the log see whats up 


## stevesbrain | 2018-08-04T08:44:16+00:00
So did you ever add an exception for 0.12.3 and run that, or not?

## dEBRUYNE-1 | 2018-08-04T15:20:44+00:00
@whenswineflu - I am wondering, why is your screenshot displaying a balance, whereas you state there is no balance? 

## stevesbrain | 2018-08-05T10:23:37+00:00
Screenshot posted looks to have likely been taken in June, but was posted here in July. Just guessing, of course, but I'm thinking it's an old photo as "proof" they had the balance at that point in time?

## whenswineflu | 2018-08-11T10:49:39+00:00
yes  for proof date 6/16/2018 June ur right well went though troubleshooting steps and possibly resyncs wallets when I stated I used hdd took 4-5 days each time did that 3-4 times upgraded to ssd takes 30hrs I'm usually able to solve my own problem's im not new to crypto have good understanding now I new to monero that took time for me to learn then I hit forums  dEBRUYNE  was very helpful then one day in July finely gave up kind of embarrassing for me had to be done wasn't to worried about time  lol balance in that pic is about half the sum pic was before issue  had to take a break so I could regroup and be here now did a fresh resync 0.12.3 is at  1572437/1636509 trying log level 2 post log 

## whenswineflu | 2018-08-12T12:06:20+00:00
![screenshot 149](https://user-images.githubusercontent.com/25366386/44001797-3396f82c-9ded-11e8-8469-363d76daa248.png)
![screenshot 151](https://user-images.githubusercontent.com/25366386/44001803-44098198-9ded-11e8-8606-edeb0eb5130c.png)
![screenshot 150](https://user-images.githubusercontent.com/25366386/44001808-55343dbe-9ded-11e8-8e4d-05abc49de51a.png)


## whenswineflu | 2018-08-12T12:12:25+00:00
<img width="960" alt="2018-06-16" src="https://user-images.githubusercontent.com/25366386/44001840-20c1d478-9dee-11e8-88e3-f66179045a20.png">


## whenswineflu | 2018-08-12T12:27:23+00:00
the last pic is old  refence/proof 

## whenswineflu | 2018-08-12T12:29:50+00:00
whats best way I can post log ? 


## whenswineflu | 2018-08-12T13:11:31+00:00
![screenshot 152](https://user-images.githubusercontent.com/25366386/44002388-8833917a-9df6-11e8-8cb4-48d51ada368f.png)


## whenswineflu | 2018-08-16T18:13:44+00:00
![screenshot 154](https://user-images.githubusercontent.com/25366386/44220115-911f8980-a132-11e8-8c87-1ebdf555e1c4.png)
  what should I do with p2p .bin  should remove or use my windows-insiders ability to run Subsystem for Linux 
 

## dEBRUYNE-1 | 2018-08-26T12:48:43+00:00
@whenswineflu - Apologies for the late response. Did you perhaps manage to resolve your issue in the meantime? 

## whenswineflu | 2018-08-27T15:26:23+00:00
unfortunately no haven't given up lol was using cmdlets got some different moderod responses along few hello world tinkering thought had something  so went to visual studio not aloud wouldent let me was funny 

## whenswineflu | 2018-08-27T19:19:04+00:00
ok so I did each step 
 Exit the GUI, but keep the daemon running.
Browse to the directory your wallet files are located (Documents\Monero on Windows | ~/Monero on Linux and Mac OS X). 
Rename <wallet-name> (the file without extension) to <wallet-name>-old.
Restart the GUI. This will trigger a wallet refresh from scratch, which shouldn't take longer than 30 minutes. 
Once it states Connected (in the left bottom) you should see funds.

didnt work done it 2 different ways same thing ground zero opens back to  whats  Language and keys my guess renaming simple like that moves it thats not good   

starting  outside the box ideas lot of your command are mixed that is easy to do when covering different shells is fine i get it is cached .keys and like .NET stuff have to remove key when do that will say need a admin funny when user is the admin and even if  simply del hidden file some how saves it agents admin and user wish   after sync up this time around want do it right in powershell  this cmdlet in the ballpark 

  [ https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/rename-item?view=powershell-6 ](url) 






## whenswineflu | 2018-08-27T19:24:44+00:00
[https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-6
](url) maybe that one too

## dEBRUYNE-1 | 2018-08-29T14:36:43+00:00
@whenswineflu - Have you tried restoring from the 25 word mnemonic seed in conjunction with a remote node (instead of your own (local) node)? It could be that (part of) your blockchain is corrupted. Make sure to set a proper restore height:

https://monero.stackexchange.com/questions/7581/what-is-the-relevance-of-the-restore-height

In addition, you can use `node.moneroworld.com` with port `18089` as remote node. 

## dEBRUYNE-1 | 2018-12-17T08:13:09+00:00
Author has not responded to my last question / suggestion. I therefore am going to close this issue.



## dEBRUYNE-1 | 2018-12-17T08:13:13+00:00
+resolved

# Action History
- Created by: whenswineflu | 2018-07-27T22:46:14+00:00
- Closed at: 2018-12-17T09:00:35+00:00
