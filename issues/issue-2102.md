---
title: Jason Error need help please.
source_url: https://github.com/xmrig/xmrig/issues/2102
author: Talos11
assignees: []
labels: []
created_at: '2021-02-14T07:08:25+00:00'
updated_at: '2021-04-12T14:14:03+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:14:03+00:00'
---

# Original Description
Hrello,
I need help with this error. 
![XMR_ERROR](https://user-images.githubusercontent.com/32502521/107870740-53616000-6e58-11eb-9a1e-e01d780271b0.PNG)
I do not know why this has happened, it happened all of a sudden.  I did just upgrade my internet but don't think that has anything to do with it but i could be wrong.  It was mining fine after the install.  I am at a loss.  Please someone help.
Thank you



# Discussion History
## snipeTR | 2021-02-14T07:12:39+00:00
https://xmrig.com/wizard

## xmrig | 2021-02-14T08:11:51+00:00
Please make sure you enable tls. If it is enabled but still not working, try another port, for example 9000. Likely your ISP somehow affected traffic between the miner and pool.
Page https://pool.supportxmr.com/ should show text `Mining Pool Online` after you allow insecure TLS connection in your browser.
Thank you.

## Talos11 | 2021-02-14T15:53:52+00:00
Thank you for responding so quickly.  Well it seems it was the tls setting.  Very strange, I didn’t change anything but the modem.  I upgraded to 80Mbps from 20.  Would changing the modem and upgrading be the cause of this?  That was the only thing that changed.  I didn’t change anything in my .bat file.  I have now added the tls setting and it works.  Just really odd that it worked after my service was installed but then just decided to not.
Thanks again for helping me out.  I have to say that over the years of mining I have met some good people and projects, and XMR and the XMRING TEAM are among the nicest and coolest people.
Thanks again,
Dan  :0)

Sent from Mail<https://go.microsoft.com/fwlink/?LinkId=550986> for Windows 10

From: xmrig<mailto:notifications@github.com>
Sent: Sunday, February 14, 2021 1:12 AM
To: xmrig/xmrig<mailto:xmrig@noreply.github.com>
Cc: Talos11<mailto:madr8b@msn.com>; Author<mailto:author@noreply.github.com>
Subject: Re: [xmrig/xmrig] Jason Error need help please. (#2102)


Please make sure you enable tls. If it is enabled but still not working, try another port, for example 9000. Likely your ISP somehow affected traffic between the miner and pool.
Page https://pool.supportxmr.com/ should show text Mining Pool Online after you allow insecure TLS connection in your browser.
Thank you.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/2102#issuecomment-778743704>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AHX7F6PUIAFBCASL732RVDDS66AVVANCNFSM4XS6H2MA>.



## Talos11 | 2021-02-14T16:15:49+00:00
Need help again.  So after I go and do the setup wizard all is good.  I can mine with no problem.  However after I shut the miner down and try to restart it it will not work and I get the same error message.  I am at my wits end.  I can not figure out what is going on here.  It must be something in my modem.  Are there settings in the modem that I need to change?
Dan

Sent from Mail<https://go.microsoft.com/fwlink/?LinkId=550986> for Windows 10

From: xmrig<mailto:notifications@github.com>
Sent: Sunday, February 14, 2021 1:12 AM
To: xmrig/xmrig<mailto:xmrig@noreply.github.com>
Cc: Talos11<mailto:madr8b@msn.com>; Author<mailto:author@noreply.github.com>
Subject: Re: [xmrig/xmrig] Jason Error need help please. (#2102)


Please make sure you enable tls. If it is enabled but still not working, try another port, for example 9000. Likely your ISP somehow affected traffic between the miner and pool.
Page https://pool.supportxmr.com/ should show text Mining Pool Online after you allow insecure TLS connection in your browser.
Thank you.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/xmrig/xmrig/issues/2102#issuecomment-778743704>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/AHX7F6PUIAFBCASL732RVDDS66AVVANCNFSM4XS6H2MA>.



## Spudz76 | 2021-02-17T04:50:06+00:00
The pool is sending garbage, or unrecognized fields.  Pool communication is JSON-RPC therefore this JSON parse error has nothing to do with the JSON config file, but what is coming from the pool packets.

You can switch to non-SSL and tcpdump the pool traffic to see what garbage it's sending - OR - recompile with debugging enabled to dump the packets inside the xmrig (you can't sniff SSL traffic).

Ask pool support why their JSON is invalid.

# Action History
- Created by: Talos11 | 2021-02-14T07:08:25+00:00
- Closed at: 2021-04-12T14:14:03+00:00
