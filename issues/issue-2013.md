---
title: v0.14.0.0 GUI in task manager runs betwin 50 and 100% CPU
source_url: https://github.com/monero-project/monero-gui/issues/2013
author: xhums1
assignees: []
labels:
- resolved
created_at: '2019-03-12T13:21:42+00:00'
updated_at: '2019-09-18T21:38:33+00:00'
type: issue
status: closed
closed_at: '2019-07-12T16:09:44+00:00'
---

# Original Description

![Untitled](https://user-images.githubusercontent.com/9310833/54207536-3be20580-44d2-11e9-91d5-657f84fbbdb5.png)
runs at 50 - 100% CPU all the time, even after sync finished

# Discussion History
## dEBRUYNE-1 | 2019-03-12T16:02:44+00:00
Could you run the GUI via the `start-low-graphics-mode.bat` batch file that is included?


## xhums1 | 2019-03-12T18:52:00+00:00
Yes, tried it. Same thing
![Untitled](https://user-images.githubusercontent.com/9310833/54227446-d6a10b00-44f7-11e9-9e8a-5578888cd2e2.png)


## mmbyday | 2019-03-13T02:12:51+00:00
Just wondering, can you create a new blank wallet and see if the CPU is just as high? Trying to narrow down what the issue could be. Also, could try opening the wallet in simple mode. 

## xhums1 | 2019-03-13T08:14:36+00:00
So I made a new wallet in simple mode and it is the same, immediately after I start it it goes to full cpu usage. 
![simple mode](https://user-images.githubusercontent.com/9310833/54263108-f243fa00-4567-11e9-9736-e9e4822a492f.png)


## xhums1 | 2019-03-13T08:28:24+00:00
what is upsetting for me is that it seams I'm the only one with this problem. I want to specify that the windows is clean (no programs other then windows update installed), the system also used the v0.13 of monero and it was working fine. Also this is a virtualbox windows

## sanderfoobar | 2019-03-13T14:28:19+00:00
Did you enable AMD-V or Intel VT in the bios? Is your VM using hardware virtualization? This should speed things up a bit. Even then - running inside a VM has a performance loss. What is your host CPU?

## xhums1 | 2019-03-13T16:23:14+00:00
Virtualization is not a problem. Again, v0.13.0.4 worked perfectly, cpu is i7-7700hq and yes virtualization is enabled and working perfectly.

## dEBRUYNE-1 | 2019-03-14T07:04:56+00:00
@xhums1 - Are you using the GUI in conjunction with a Ledger device? Also, would you be able to try it outside of a VM environment? 

## dEBRUYNE-1 | 2019-03-14T16:35:10+00:00
@xhums1 - Also, could you try this:

>1. Click the Start button, right-click the Computer option in the Start menu, and select Properties.

>2. Click the Advanced System Settings link in the left column.

>3. In the System Properties window, click on the Advanced tab, then click the Environment Variables button near the bottom of that tab.

>4. In the Environment Variables window you can now add a new User Environment Variable. Name=MONERO_USE_CNV4_JIT / Value=1

## xhums1 | 2019-03-14T21:29:50+00:00
Did not try in host windows, only on guest windows on wirtualbox.
I did what you asked and it is the same. look
![Untitled](https://user-images.githubusercontent.com/9310833/54392716-4225dc80-46a0-11e9-955c-9ee44a59a9ba.png)


## dEBRUYNE-1 | 2019-03-15T07:28:31+00:00
Odd, it worked for someone else. Could you perhaps try on host Windows? 

## sanderfoobar | 2019-03-15T16:17:37+00:00
Runs fine in VM here.

![https://i.imgur.com/BelnHne.png](https://i.imgur.com/BelnHne.png)

## sanderfoobar | 2019-03-15T16:18:21+00:00
@xhums1 Does your wallet contain a lot of transactions?

## xhums1 | 2019-03-15T16:27:16+00:00
no, only 16

## xhums1 | 2019-03-15T16:28:52+00:00
Did you update windows to the latest version? patch and all, windows update. I thing the last cumulative update screwed things up

## xhums1 | 2019-03-15T16:32:04+00:00
Don't get me wrong, it is not that bad, because I only need it when I do a transaction or generate an address, so it is not pain, but just wondering what did go wrong.
If I try again the v0.13.0.4 will this screw things up? Just to see if it uses high cpu like v0.14 . Don't want to make a big mistake

## dEBRUYNE-1 | 2019-07-03T17:35:02+00:00
@xhums1 - Can you check whether this is still an issue with GUI v0.14.1.0? 

## dEBRUYNE-1 | 2019-07-12T16:05:17+00:00
I am going to close this as (i) the author did not respond and (ii) xiphon addressed a lot of potential freezing issues in GUI v0.14.1.0. 

## dEBRUYNE-1 | 2019-07-12T16:05:21+00:00
+resolved

## xhums1 | 2019-09-17T18:16:57+00:00
Yes, I know what was the problem.
At virtualbox - guest settings - display - I had VBoxVGA (this is no longer supported) and that is why monero gui always used full CPU. I changed it now to VBoxSVGA and it is working perfectly
![Untitled](https://user-images.githubusercontent.com/9310833/65067979-3ed51b80-d977-11e9-86dc-68d5316d736e.png)


## xiphon | 2019-09-17T22:50:37+00:00
@xhums1 

Did you try low graphic mode? Might resolve the issue as well.

## xhums1 | 2019-09-18T21:38:33+00:00
Tried that and did not work. The only solution was to set the Graphics Controller to VBoxSVGA

# Action History
- Created by: xhums1 | 2019-03-12T13:21:42+00:00
- Closed at: 2019-07-12T16:09:44+00:00
