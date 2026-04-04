---
title: GUI 12.3 change Wallet hight
source_url: https://github.com/monero-project/monero-gui/issues/1565
author: AlexAnarcho
assignees: []
labels:
- resolved
created_at: '2018-09-19T08:35:37+00:00'
updated_at: '2018-12-27T15:27:28+00:00'
type: issue
status: closed
closed_at: '2018-12-27T15:27:28+00:00'
---

# Original Description
When I want to retroactively change the Wallet hight in the Monero GUI (12.3.) to start the sync of the Blockchain not from 0, the change is not accepted and the number is set back to 0. 

Wallet cache seems to be wiped though, since the sync starts again from 0. 

Kinda annoying...

# Discussion History
## dEBRUYNE-1 | 2018-09-19T16:26:32+00:00
Are you using the GUI in conjunction with a Ledger device? If so, it's fixed in #1446. 

## AlexAnarcho | 2018-09-20T07:31:27+00:00
No, I am not working with a Ledger, just using the GUI as is. 

Problem does not seem to be fixed - no big big deal, just a small thing I noticed. May be helpful to revisit when the time is rife. 

Cheers,

## dEBRUYNE-1 | 2018-09-20T15:18:45+00:00
I see. I'll try to reproduce this behavior then. 

## Laurentiu-Andronache | 2018-09-21T16:43:38+00:00
It happens to me too, in .12.3, with a Ledger.

## dEBRUYNE-1 | 2018-09-21T18:04:01+00:00
@Laurentiu-Andronache - If you use a Ledger, please see #1446. To utilize the fix, you ought to compile master. 

## usmarine2141 | 2018-10-01T21:32:21+00:00
im having similar problems, using the ledger. However... It makes me resync the entire damn thing every freaking time, and doesnt work half the time. Utilized the GUI to create the ledger wallet. I dont want to reset because i sent some xmr to my wallet on there. 

## Laurentiu-Andronache | 2018-10-02T00:06:02+00:00
It's not like your XMR will disappear if you reset the GUI... Just don't reset your Ledger Nano unless you have that seed written down... 

## dEBRUYNE-1 | 2018-12-17T08:06:12+00:00
@Laurentiu-Andronache, @AlexAnarcho: Are you still experiencing this behavior in the most recent version? 

## usmarine2141 | 2018-12-17T16:32:12+00:00
Please close. I thought i had closed this. Sorry for the lingering ticket.

On Mon, Dec 17, 2018 at 2:06 AM dEBRUYNE-1 <notifications@github.com> wrote:

> @Laurentiu-Andronache <https://github.com/Laurentiu-Andronache>,
> @AlexAnarcho <https://github.com/AlexAnarcho>: Are you still experiencing
> this behavior in the most recent version?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1565#issuecomment-447755713>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ATwSox2vzZeXcJMG42orzh4UT5hk-Xtdks5u51B3gaJpZM4WvrMv>
> .
>


## dEBRUYNE-1 | 2018-12-17T16:34:53+00:00
Will close in a few days if I don't hear anything from the other commenters. 

## dEBRUYNE-1 | 2018-12-27T15:09:36+00:00
Author has not responded and therefore I am going to close this issue. 

## dEBRUYNE-1 | 2018-12-27T15:09:40+00:00
+resolved

# Action History
- Created by: AlexAnarcho | 2018-09-19T08:35:37+00:00
- Closed at: 2018-12-27T15:27:28+00:00
