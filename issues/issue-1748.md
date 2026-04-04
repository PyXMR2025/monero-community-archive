---
title: I downloaded the gui wallet but I can't get Daemon to run
source_url: https://github.com/monero-project/monero-gui/issues/1748
author: freddrums
assignees: []
labels:
- resolved
created_at: '2018-11-22T21:11:58+00:00'
updated_at: '2018-12-17T08:00:31+00:00'
type: issue
status: closed
closed_at: '2018-12-17T08:00:31+00:00'
---

# Original Description
I have now been able to download the new Gui wallet but I can't get daemon to sync. Any ideas, I keep getting an error and it says to monerod manually? How do I do that? Also, it says to check my wallet and daemon log for errors.
any ideas how to get the daemon to connect?

thanks,
Fred

# Discussion History
## dEBRUYNE-1 | 2018-11-23T15:28:52+00:00
Did you upgrade from a 0.12 version? Because then the following applies:

>This version, if using your own (local) node, requires a database conversion, which may take a few hours and the GUI may show that it's Disconnected (or unable to connect) from the daemon (monerod). I'd advise to simply let it run and after the database conversion has completed the GUI will connect back to the daemon (monerod).



## dEBRUYNE-1 | 2018-11-26T11:01:34+00:00
Ping @freddrums - did you manage to resolve your issue? 

## freddrums | 2018-11-26T18:47:01+00:00
I have't had a chance to run it for a few hours, I'll try today and keep you posted, thanks for checking in! really appreciate it,
all the best!
Fred

## dEBRUYNE-1 | 2018-11-29T08:13:15+00:00
@freddrums - All right, hopefully you will be able to resolve your issue! 

## freddrums | 2018-11-30T20:44:53+00:00
thanks for checking in! really appreciate it. I let daemon run for a few days, I think it eventually did sync once. It seems like it syncs very slowly!! I think my computer is old and really slow. I'll try to sync it again and see if it can do it quicker. Definitely time for a nex MAc. mine is almost 6 yrs old.
Thnx much!!

## dEBRUYNE-1 | 2018-12-02T10:33:06+00:00
@freddrums - Thanks for your report. Note that the sync performs best when all other resource intensive processes (e.g. a browser) are closed.

P.S. Can this issue be closed? 

## dEBRUYNE-1 | 2018-12-17T07:57:33+00:00
Author has not responded in ~2 weeks. I therefore am going to close this issue. 

## dEBRUYNE-1 | 2018-12-17T07:57:37+00:00
+resolved

# Action History
- Created by: freddrums | 2018-11-22T21:11:58+00:00
- Closed at: 2018-12-17T08:00:31+00:00
