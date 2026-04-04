---
title: 'Monero GUI wallet Access issues '
source_url: https://github.com/monero-project/monero-gui/issues/4127
author: IntheLimelight
assignees: []
labels: []
created_at: '2023-03-11T00:56:27+00:00'
updated_at: '2023-03-12T05:11:54+00:00'
type: issue
status: closed
closed_at: '2023-03-12T04:44:22+00:00'
---

# Original Description
I need help. Trying to access my wallet with my Ledger Device attached and getting this message. 


Couldn’t open wallet: Wrong Device Status: 0x6a30 (UNKNOWN), EXSPECTED 0x9000 (SW_OK), MASK 0xffff

Have no idea what to do

# Discussion History
## selsta | 2023-03-11T01:16:50+00:00
Which operating system are you using? Can you post your ledger firmware, ledger monero app and monero-gui version?

Also did you make sure your Ledger is unlocked and the monero app is opened? It also doesn't like when multiple programs interact with the Ledger at the same time, so make sure to have Ledger Live closed.

## IntheLimelight | 2023-03-11T01:19:58+00:00
On Fri, Mar 10, 2023 at 5:17 PM selsta ***@***.***> wrote:

> Which operating system are you using? Can you post your ledger firmware,
> ledger monero app and monero-gui version?
>
> Also did you make sure your Ledger is unlocked and the monero app is
> opened? It also doesn't like when multiple programs interact with the
> Ledger at the same time, so make sure to have Ledger Live closed.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/4127#issuecomment-1464739575>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A6NJEKY3GTGJVMMTVRH6GK3W3PHA3ANCNFSM6AAAAAAVXDOLLY>
> .
> You are receiving this because you authored the thread.Hello, thank you
> so much for your email. I am not very advanced in this technology and doing
> transactions but I am using a regular Windows computer and I did have
> ledger live open at the time on my ledger device. I did have the Manero app
> open, but I can see you can toggle through different options or versions or
> something like that which I know nothing about.
>
I will try again and try to get a little more information here

> Message ID: ***@***.***>
>
-- 
Rick J Neff


## IntheLimelight | 2023-03-11T01:37:54+00:00
Sorry let me try this again. I will update. Best Regards,Rick NeffOn Mar 10, 2023, at 5:19 PM, Rick Neff ***@***.***> wrote:﻿On Fri, Mar 10, 2023 at 5:17 PM selsta ***@***.***> wrote:
Which operating system are you using? Can you post your ledger firmware, ledger monero app and monero-gui version?
Also did you make sure your Ledger is unlocked and the monero app is opened? It also doesn't like when multiple programs interact with the Ledger at the same time, so make sure to have Ledger Live closed.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Hello, thank you so much for your email. I am not very advanced in this technology and doing transactions but I am using a regular Windows computer and I did have ledger live open at the time on my ledger device. I did have the Manero app open, but I can see you can toggle through different options or versions or something like that which I know nothing about. I will try again and try to get a little more information hereMessage ID: ***@***.***>
-- Rick J Neff

## IntheLimelight | 2023-03-11T01:59:17+00:00
The first attempt to Log-in I had Ledger Live open and just tried again with it closed and same issue. 
Operating system: Windows 11
Ledger Firmware: 2.1.0 
Monero Ledger App: on Ledger when open reads;
XMR/0 43ZR2..GSpCa 


## selsta | 2023-03-11T02:03:28+00:00
Please also post the monero-gui version and the monero ledger app version. I suspect something is outdated.

Do you know where to find them?

## IntheLimelight | 2023-03-11T02:26:03+00:00
I tried to find that and could not. The GUI was created in 1/19 but do not see how to find the version or for the App. Best Regards,Rick NeffOn Mar 10, 2023, at 6:03 PM, selsta ***@***.***> wrote:﻿
Please also post the monero-gui version and the monero ledger app version.
Do you know where to find them?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2023-03-11T02:32:03+00:00
For the GUI please download the latest version from here: https://www.getmonero.org/downloads/

To get the monero ledger app version, you have to open Ledger Live and click on "My Ledger", and then look at installed apps. It should show monero app being installed and the exact version.

## IntheLimelight | 2023-03-11T03:22:48+00:00
Ok. Thank you! I will try this ASAP. Really appreciate the help!Best Regards,Rick NeffOn Mar 10, 2023, at 6:32 PM, selsta ***@***.***> wrote:﻿
For the GUI please download the latest version from here: https://www.getmonero.org/downloads/
To get the monero ledger app version, you have to open Ledger Live and click on "My Ledger", and then look at installed apps. It should show monero app and the exact version.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## IntheLimelight | 2023-03-11T05:02:02+00:00
Ok. I downloaded the other version of GUI not sure if it installed. For the Monero App on Ledger it is;1.8.0 Best Regards,Rick NeffOn Mar 10, 2023, at 6:32 PM, selsta ***@***.***> wrote:﻿
For the GUI please download the latest version from here: https://www.getmonero.org/downloads/
To get the monero ledger app version, you have to open Ledger Live and click on "My Ledger", and then look at installed apps. It should show monero app and the exact version.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## IntheLimelight | 2023-03-11T05:02:02+00:00
I downloaded the Newest version of the GUI still in Process. Also the Monero App On Ledger is the 1.8.0Best Regards,Rick NeffOn Mar 10, 2023, at 7:22 PM, Rick Neff ***@***.***> wrote:﻿Ok. Thank you! I will try this ASAP. Really appreciate the help!Best Regards,Rick NeffOn Mar 10, 2023, at 6:32 PM, selsta ***@***.***> wrote:﻿
For the GUI please download the latest version from here: https://www.getmonero.org/downloads/
To get the monero ledger app version, you have to open Ledger Live and click on "My Ledger", and then look at installed apps. It should show monero app and the exact version.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## IntheLimelight | 2023-03-11T05:03:18+00:00
Ok. I’m downloading the latest version of GUI in progress Also the Monero App on Ledger is 1.8.0Best Regards,Rick NeffOn Mar 10, 2023, at 7:22 PM, Rick Neff ***@***.***> wrote:﻿Ok. Thank you! I will try this ASAP. Really appreciate the help!Best Regards,Rick NeffOn Mar 10, 2023, at 6:32 PM, selsta ***@***.***> wrote:﻿
For the GUI please download the latest version from here: https://www.getmonero.org/downloads/
To get the monero ledger app version, you have to open Ledger Live and click on "My Ledger", and then look at installed apps. It should show monero app and the exact version.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## IntheLimelight | 2023-03-11T20:41:09+00:00
Following up, I see the downloads but can’t tell if it’s installed. Should I delete the old Icon on my desktop and try to install the newer version? Is this what we are trying to do? 

## selsta | 2023-03-11T22:28:14+00:00
Did you download the installer or the zip?

## IntheLimelight | 2023-03-11T22:31:49+00:00
I believe both but on the Zip now. Was able to access the wallet 🙏 but now says “ Please check daemon log for errors, you can also try to start moderod.EXE manually.  Seems like it is in the process of updating the daemon blocksBest Regards,Rick NeffOn Mar 11, 2023, at 2:28 PM, selsta ***@***.***> wrote:﻿
Did you download the installer or the zip?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2023-03-11T22:32:54+00:00
Good, that means you can open the wallet again.

Can you post your "wallet mode" in Settings -> Info?

## IntheLimelight | 2023-03-11T22:34:40+00:00
Sorry, Post wallet mode in settings. Not sure what that meansBest Regards,Rick NeffOn Mar 11, 2023, at 2:33 PM, selsta ***@***.***> wrote:﻿
Good, that means you can open the wallet again.
Can you post your "wallet mode" in Settings -> Info?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2023-03-11T22:35:37+00:00
What does it say under "wallet mode" in Settings -> Info?

Simple mode?
Advanced mode?

Please write the exact text.

## IntheLimelight | 2023-03-11T22:40:01+00:00
Simple modeBest Regards,Rick NeffOn Mar 11, 2023, at 2:35 PM, selsta ***@***.***> wrote:﻿
What does it say under "wallet mode" in Settings -> Info?
Simple mode?
Advanced mode?
Please write the exact text.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## IntheLimelight | 2023-03-11T22:42:11+00:00
The wallet window keeps closing and defaults the the Daemon failed to start message So I have to hit ok at the bottom and the wallet gives me like 2 seconds to read or select something Best Regards,Rick NeffOn Mar 11, 2023, at 2:35 PM, selsta ***@***.***> wrote:﻿
What does it say under "wallet mode" in Settings -> Info?
Simple mode?
Advanced mode?
Please write the exact text.

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2023-03-11T22:44:20+00:00
Are you sure that your anti anti virus isn't blocking monerod.exe ?

## IntheLimelight | 2023-03-11T22:46:51+00:00
That could be possible. Unfortunately I’m not really good with computers so can’t tell or not sure what to checkFeel like an idiot now.  Lol Best Regards,Rick NeffOn Mar 11, 2023, at 2:44 PM, selsta ***@***.***> wrote:﻿
Are you sure that your anti anti virus isn't blocking monerod.exe ?

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## IntheLimelight | 2023-03-12T00:05:38+00:00
Whatever is happening I can’t seem to get the most current GUI Wallet up on my Computer desktop 
Trying to download again. What version do i download? For Windows? 

## selsta | 2023-03-12T00:12:53+00:00
Let me try one more thing so that you can connect to a remote node:

Open the latest version and then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `selsta2.featherwallet.net`
port: `18081`

This should resolve your issue for now. No extra hard disk space required and no issues with monerod not starting.

----------

Other remote node in case the above has issues:

address: `node.supportxmr.com`
port: `18081`

address: `selsta1.featherwallet.net `
port: `18081`

address: `node.community.rino.io`
port: `18081`

More nodes: nodes.monero.com

## IntheLimelight | 2023-03-12T00:30:45+00:00
I think I may have got the updated wallet to install. Logging in and wallet is up just says “ synchronizing” And now “ Connected “ WowBest Regards,Rick NeffOn Mar 11, 2023, at 4:13 PM, selsta ***@***.***> wrote:﻿
Let me try one more thing so that you can connect to a remote node:
Open the latest version and then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:
address: selsta2.featherwallet.net
port: 18081
This should resolve your issue for now. No extra hard disk space required and no issues with monerod not starting.

Other remote node in case the above has issues:
address: node.supportxmr.com
port: 18081
address: selsta1.featherwallet.net 
port: 18081
address: node.community.rino.io
port: 18081
More nodes: nodes.monero.com

—Reply to this email directly, view it on GitHub, or unsubscribe.You are receiving this because you authored the thread.Message ID: ***@***.***>

## selsta | 2023-03-12T04:44:22+00:00
Seems the issue is resolved :)

## IntheLimelight | 2023-03-12T05:11:54+00:00
Thank you.

On Sat, Mar 11, 2023 at 8:44 PM selsta ***@***.***> wrote:

> Closed #4127 <https://github.com/monero-project/monero-gui/issues/4127>
> as completed.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/4127#event-8725049038>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A6NJEKYYIZD5DCKJU7JV7B3W3VIDFANCNFSM6AAAAAAVXDOLLY>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>
-- 
Rick J Neff


# Action History
- Created by: IntheLimelight | 2023-03-11T00:56:27+00:00
- Closed at: 2023-03-12T04:44:22+00:00
