---
title: P2pool miner not working shows Connected+Mining(Linux Pop!_OS 22.04 LTS)
source_url: https://github.com/monero-project/monero-gui/issues/4022
author: XOverMindX
assignees: []
labels: []
created_at: '2022-09-05T09:59:08+00:00'
updated_at: '2022-12-10T15:29:06+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Fresh install full chain all default settings no start up flags works when solo mining
Hangs on Starting P2Pool while showing a Connected+Mining for network status but no hash rate is displayed and no CPU activity

![image](https://user-images.githubusercontent.com/96671852/188422488-e9d42221-93cd-4029-89f0-9ec4adfdb335.png)


# Discussion History
## selsta | 2022-09-05T10:00:44+00:00
How did you install monero-gui?

## XOverMindX | 2022-09-05T10:01:14+00:00
through the pop store

## selsta | 2022-09-05T10:02:24+00:00
Quite sure p2pool only works when downloading from getmonero.org, getting it to work with package managers will be complicated.

## XOverMindX | 2022-09-05T10:07:34+00:00
copy if i get it to work i'll post a Pop user how to here.  

## selsta | 2022-09-05T10:09:00+00:00
monero-gui downloads the p2pool binary into the same dir as the monero-gui binary. So check if it is there and also check if the permission/owner is set correctly.

## q7nm | 2022-09-05T14:45:37+00:00
I think, you installed monero-gui via flatpak (pop store), so you should use `--data-api` option in the p2pool startup flags.

## hsmalley | 2022-12-10T14:19:51+00:00
> I think, you installed monero-gui via flatpak (pop store), so you should use `--data-api` option in the p2pool startup flags.

I'm using the flatpak version installed from flathub. Having the same problem as OP. According to the mouse over it says path to the p2pool JSON file?  I can't seem to find the json to point --data-api at.  Maybe I'm just missing something in the documentation? When I use the solo option everything works correctly

EDIT_1: I saw a closed issue (#4001) and tried doing the suggested user override to a folder in my home. So I created the path. After doing `--data-api "/home/MYUSER/monero/api"` on the p2pool startup flags. I didn't get anywhere with that. Looking over the monero documentation on the website relating to p2pool I did not see that option listed. Again, I could be missing something completely obvious.

EDIT_2: I gave the flatpak full access to my home. It started using $HOME/.bitmonero in my home rather than the flatpak. I symlinked the it to the flatpak path. Not sure if that's desired behavior or not. 

I also set log level to 4 and I've been tailing the logs watching it come up. I 've also had a tail piped into grep looking for "p2p|fail|err|war" and I'm not seeing anything that would indicate a problem. If you want/need the logs let me know what level you want it set to and I'll upload them.

EDIT_3: Running p2pool manually seems works correctly. I tried the version bundled with the flatpak and downloading the latest version. I'm not seeing any logs produced for it when trying to start it from the monero gui though. 

# Action History
- Created by: XOverMindX | 2022-09-05T09:59:08+00:00
