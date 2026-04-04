---
title: Monero GUI froze/crashed ubuntu 22
source_url: https://github.com/monero-project/monero-gui/issues/4089
author: Gingeropolous
assignees: []
labels: []
created_at: '2022-12-24T05:53:46+00:00'
updated_at: '2023-02-27T22:57:41+00:00'
type: issue
status: closed
closed_at: '2023-02-27T22:57:41+00:00'
---

# Original Description
as documented on IRC, I decided to use the GUI for a new account. 

```
<gingeropolous> aaaight im gonna do it! i got a fresh ubuntu 22 and gonna use the GUI to manage this monero account
<gingeropolous> hrm. the appimage icon or the one without appimage
<gingeropolous> ooh theres a guide
<gingeropolous> ok. looks like i click on the one thats not appimage
<gingeropolous> ah screw it. im goin appimage. 
<gingeropolous> hrm, double clicked... started to doubt things were happening
<gingeropolous> register GUI desktop entry?
<gingeropolous> gah, i wanna try easy / bootstrap but i don't wanna connect to a random node. :( i guess advanced it is
<gingeropolous> hrm. too many negative words in the seed. i wonder if I hit back to menu if i can create another
<gingeropolous> wait. Bootstrap node, and then a button to connect to a remote node?
<gingeropolous> ooooh, clicking that button was not what i wanted
<gingeropolous> methinks there needs to be a visual separation of that menu hiearchy
<gingeropolous> heirarchy
<gingeropolous> damnit
 
* Loaded log from Fri Dec 23 08:22:17 2022
 
* Now talking on #monero
* Topic for #monero is: [XMR] Be excellent to each other and welcoming to newcomers || getmonero.org || Dev: #monero-dev || Pool related: #monero-pools || Price chat: #monero-markets || People can & do log this channel
* Topic for #monero set by binaryFate!~binaryFat@monero/binaryFate (Thu Jul 21 20:33:10 2022)
<gingeropolous> well thats great
<gingeropolous> computer froze. I gave it 2 minutes with no change. couldn't even do the ctr-alt F1 or F2 or whatever to get to the console
<gingeropolous> had to give it a hard power cycle
```

But yeah. Brand new ubuntu 22 install, and downloaded the GUI from getmonero.org and double clicked on the appimage version in the folder. 

I write froze/crashed in the title because everything on screen was frozen, however my HDD light was still goin at it, so I summise the daemon was still active. 

I'm gonna try and clean slate the .bitmonero folder again and try and re-create. Are there any other files to nuke so I can best re-create the first launch experience?  

# Discussion History
## selsta | 2022-12-24T10:00:00+00:00
What kind of hardware do you have? It's definitely not normal that your whole operating system freezes.

When did the freeze happen? If it happened after starting the local daemon this should be a CLI bug report.

## Gingeropolous | 2022-12-24T13:19:16+00:00
its a thinkpad P50 with i7-6820HQ CPU @ 2.70GHz and 64 GB RAM and a new SSD. 

I mean, it's old. But its not bad. 

Yeah, I think it happened when the node started. 

## selsta | 2023-02-27T22:57:41+00:00
It seems this issue is related to the daemon + your hardware, I don't think there's anything that I can fix on the GUI side here, also there's no way to reproduce it in the first place. If  you continue to have issue like this it would be best to open them on the CLI repo.

# Action History
- Created by: Gingeropolous | 2022-12-24T05:53:46+00:00
- Closed at: 2023-02-27T22:57:41+00:00
