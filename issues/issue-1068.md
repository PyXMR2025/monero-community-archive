---
title: GUI displays unexpected path to wallet log file
source_url: https://github.com/monero-project/monero-gui/issues/1068
author: ordtrogen
assignees: []
labels:
- resolved
created_at: '2018-01-09T22:09:18+00:00'
updated_at: '2018-12-17T11:54:30+00:00'
type: issue
status: closed
closed_at: '2018-12-17T11:54:30+00:00'
---

# Original Description
Why does it point to 
/usr/bin/monero-wallet-gui.log

(see screenshot)

System:

OS: Manjaro Linux i686
Model: Compaq Mini 110c-1000 03A81000000000001000
Kernel: 4.9.74-2-MANJARO
Packages: 976
Shell: bash 4.4.12
CPU: Intel Atom N270 (2) @ 1.600GHz
GPU: Intel Integrated Graphics
GPU: Intel Integrated Graphics
Memory: 298MiB / 995MiB

Daemon installed from https://aur.archlinux.org/monero.git
I typically keep it running continuously 

Recently installed GUI to begin testing:

GUI installed from https://aur.archlinux.org/monero-wallet-qt.git

First time I ran it, decided to create a wallet on testnet
When I start GUI now, it displays this:

![skarmbild_2018-01-09_23-01-43](https://user-images.githubusercontent.com/15184875/34745818-14039f1e-f592-11e7-8ffc-524c24163cc3.png)





# Discussion History
## ordtrogen | 2018-01-09T22:14:43+00:00
Maybe worth mentioning these errors displayed on console on startup:

![skarmbild_2018-01-09_23-13-07](https://user-images.githubusercontent.com/15184875/34746022-dd70f6d0-f592-11e7-918e-a6b86c211d33.png)


## medusadigital | 2018-01-11T12:54:51+00:00
that looks like a potential bug to me.

however, please check permissioning on the file here too: https://monero.stackexchange.com/questions/2866/where-are-the-monero-core-configuration-parameters-stored



## ordtrogen | 2018-01-11T18:33:55+00:00
I found the config file but its location is different from what the SE question mentions. I have it

~/.config/monero-project/monero-core.conf

Are you suggesting that the properties mentioned in the console output (daemonLogPath et al) should be mentioned in the .conf file?




## mmbyday | 2018-12-17T08:58:46+00:00
+resolved 
by #1800

## dEBRUYNE-1 | 2018-12-17T11:52:10+00:00
+resolved

# Action History
- Created by: ordtrogen | 2018-01-09T22:09:18+00:00
- Closed at: 2018-12-17T11:54:30+00:00
