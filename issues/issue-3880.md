---
title: Had bluescreen while syncing blocks MONERO GUI (blockchain on pc)
source_url: https://github.com/monero-project/monero-gui/issues/3880
author: Kekko93
assignees: []
labels: []
created_at: '2022-04-06T15:38:28+00:00'
updated_at: '2022-04-07T13:26:14+00:00'
type: issue
status: closed
closed_at: '2022-04-07T07:06:08+00:00'
---

# Original Description
Hi , i  had bluescreen on windows 10 while syncing blocks like 6000 only (i havent used monero gui for a week or so) , when i had bluescreen i have reseted pc on power button and didnt wait for it to go to 0 - 100% , now my monero gui daemon cant sync. im so stupid.

![image](https://user-images.githubusercontent.com/100800917/162013111-bf0c3ddf-0405-4190-a819-6353d0098704.png)


im using Advanced mode (Local node) - blockchain downloaded on pc. 
HOW CAN I FIX THIS so i dont need to redownload blockchain , last time i downloaded blockchain it took 7 days since i have shitty hdd and atm i cant upgrade to ssd. 

# Discussion History
## Kekko93 | 2022-04-06T15:39:33+00:00
![image](https://user-images.githubusercontent.com/100800917/162013580-ed7d9b8e-c8a5-4604-961c-a12b7e7a003c.png)


## Kekko93 | 2022-04-06T16:20:41+00:00
i opened monerod.exe manually as it says and this happened 
![image](https://user-images.githubusercontent.com/100800917/162021196-4197546c-dcfa-4d32-b399-69bb80f936f0.png)

ITS DOWNLOADING BLOCKCHAIN FROM SCRATCH? , should i even continue this or just delete and go from 0% so it doesnt corrupt something again? here we go 7days more to download it .. jesus

## Kekko93 | 2022-04-06T22:24:21+00:00
Anyone?

## selsta | 2022-04-07T07:03:34+00:00
If you set a custom blockchain location in the GUI and then start monerod.exe from explorer the custom location isn't set, that's why it's resyncing from scratch. It will sync to the default location. A bluescreen will mean that your blockchain is corrupted and you have to delete it.

I would probably recommend you to use a remote node, if you got a bluescreen once during sync it's possible that you will get one again. Is your computer stable during high loads?

## selsta | 2022-04-07T07:06:08+00:00
I will close this as a bluescreen isn't something we can fix on our side. If you continue to have questions just reply here.

## Kekko93 | 2022-04-07T13:18:01+00:00
i started download again after i deleted blockchain and i had bluescreen while syncing again jesus.. turned on pc its corrupted again , cant beleave this is happening. i ordered 3k / 3k speed m2 SSD , think this is gona fix the issue . remote node? is that cloud node? i need it on my pc since i want maximum privacy

## selsta | 2022-04-07T13:25:20+00:00
In general a bluescreen is a hardware issue or a driver / OS issue. A program like monero should in the worst case crash but never produce a bluescreen.

Yes, a remote node is a "cloud node", basically it's a publicly available node that is hosted by someone else.

Do you have a different computer where you could test syncing?

## selsta | 2022-04-07T13:26:14+00:00
One more thing you can do is run e.g. Prime95 to check if your computer is stable under high load or if it also bluescreens.

# Action History
- Created by: Kekko93 | 2022-04-06T15:38:28+00:00
- Closed at: 2022-04-07T07:06:08+00:00
