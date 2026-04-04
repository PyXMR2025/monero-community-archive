---
title: Wallet GUI stucks on Block 1788047 but it says "synchronized". Last scheduled
  hard fork time shows a daemon update is needed soon.
source_url: https://github.com/monero-project/monero/issues/5268
author: kinza1509
assignees: []
labels: []
created_at: '2019-03-12T00:40:54+00:00'
updated_at: '2019-03-15T22:28:42+00:00'
type: issue
status: closed
closed_at: '2019-03-15T22:28:42+00:00'
---

# Original Description
Wallet GUI stucks on Block 1788047 but it says "synchronized". Last scheduled hard fork time shows a daemon update is needed soon.
What should i do?


# Discussion History
## moneromooo-monero | 2019-03-12T01:21:31+00:00
Are you running 0.14.0.x ? If you're running a 0.13.x.y series, you need to update, 0.13 is too old and will not be able to follow the network.

## kinza1509 | 2019-03-12T01:29:48+00:00
How do i get 0.14.0? I downloaded the latest version one week ago on the monero Page. 
But if i download it now in getmonero.org, then i get also the 0.13.0 folder.?

## kinza1509 | 2019-03-12T06:36:47+00:00
What can i do? And how can i do this?

## el00ruobuob | 2019-03-12T06:46:28+00:00
Your browser may had caching issue as the 0.14 has been on the website for more than a week. Go to the release tab on monero-gui repository to download the latest 0.14. After you start it, it will resync correctly and you'll be fine.  

## kinza1509 | 2019-03-12T06:53:41+00:00
When i download it form getmonero.com it seems to be the old version 0.13.0
![Unbenannt](https://user-images.githubusercontent.com/48460347/54180444-f0146980-449b-11e9-8332-049c6870e66e.JPG)


## mmbyday | 2019-03-12T08:04:26+00:00
@kinza1509 https://www.reddit.com/r/Monero/comments/ayshug/gui_v01400_boron_butterfly_released/

## dEBRUYNE-1 | 2019-03-12T08:18:36+00:00
@kinza1509 - Upgrading to GUI v0.14.0.0 should solve your issue. Please take notice of the following though:

>This version, if using your own (local) node, requires a database conversion, which may take 5-10 minutes and the GUI will show that it's Disconnected (or unable to connect) from the daemon (monerod). I'd advise to simply let it run and after the database conversion has completed the GUI will connect back to the daemon (monerod).



# Action History
- Created by: kinza1509 | 2019-03-12T00:40:54+00:00
- Closed at: 2019-03-15T22:28:42+00:00
