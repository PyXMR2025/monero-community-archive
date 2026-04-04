---
title: 'SOLVED  Couldn''t open wallet: std::bad_alloc  Monero Gui v0.13.0.4 Beryllium
  Bullet and Windows 10'
source_url: https://github.com/monero-project/monero-gui/issues/1730
author: fouadr
assignees: []
labels:
- resolved
created_at: '2018-11-07T11:27:40+00:00'
updated_at: '2018-11-08T09:27:25+00:00'
type: issue
status: closed
closed_at: '2018-11-08T09:27:25+00:00'
---

# Original Description
Hi there,

Just downloaded, extracted and opened Monero Gui v0.13.0.4 Beryllium Bullet in Windows 10, after opening I used my seed to restore the wallet ( to create new wallet/cache files) and this went fine.
Once the wallet was synchronised I closed the Monero Wallet Gui and a few minutes later I tried to open the wallet file, right after providing my passphrase the dreaded isse that I was hoping not to see appered:

"Couldn't open wallet: std::bad_alloc" 

Are these builds not tested on the different platforms for where they are build for??
Guys, after opening the wallet also close and open it again after build!

And yes, deleting the cache file is a work around, just wait a long time to download the whole blockchain again... but this is not a desired situation.



# Discussion History
## dEBRUYNE-1 | 2018-11-07T14:04:30+00:00
Are you absolutely certain you downloaded GUI v0.13.0.4? Because that particular issue has been resolved in v0.13.0.4 (you may have to delete the wallet cache once though). If not, please use the direct download link from here:

https://reddit.com/r/Monero/comments/9ti2on/gui_v01304_beryllium_bullet_released/

## fouadr | 2018-11-07T20:12:09+00:00
Thanks, I'll try that..

## fouadr | 2018-11-07T20:45:02+00:00
I had downloaded the right version ( build date of monero-wallet-gui is:  ‎31 ‎oktober ‎2018, ‏‎13:24:30).
I deleted the cache file and restarted.
At the moment it is downloading the Blocks.... will take a while, even through a remote node...


## fouadr | 2018-11-08T08:40:03+00:00
Solved by deleting the cache file again.

## dEBRUYNE-1 | 2018-11-08T09:26:25+00:00
+resolved

## dEBRUYNE-1 | 2018-11-08T09:26:31+00:00
Good to hear!

# Action History
- Created by: fouadr | 2018-11-07T11:27:40+00:00
- Closed at: 2018-11-08T09:27:25+00:00
