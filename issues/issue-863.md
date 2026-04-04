---
title: Monero Research Lab Meeting - Wed 12 July 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/863
author: Rucknium
assignees: []
labels: []
created_at: '2023-07-11T23:31:23+00:00'
updated_at: '2023-08-02T19:14:01+00:00'
type: issue
status: closed
closed_at: '2023-07-17T05:44:30+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#859 

# Discussion History
## plowsof | 2023-08-02T19:14:01+00:00
Logs 
```
17:03:58 <xmrack[m]> Meeting today?

17:04:43 <rbrunner> Wondering the same :) Last week UkoeHB said for a meeting somebody ready to manage it
would have to be found.

17:05:02 <rbrunner> And people not on holidays anyway of course

17:09:00 <xmrack[m]> I have a small update. Collected data from 11 and 12 output transactions on-chain over
the last 4 months trying to see if there was an obvious fingerprint of users with monerujo pocket change.
Neither myself nor rucknium could identify anything obvious at first glance.

17:10:08 <rbrunner> Already 4 months that this is in the hand of users? Time flies. No obvious fingerprint
sounds like good news, right?

17:11:08 <xmrack[m]> Pocketchange came out May 5 IIRC. I collected extra data to compare before/after its
existence

17:11:28 <rbrunner> Ah, ok

17:12:49 * xmrack[m] posted a file: (205KiB) <
https://libera.ems.host/_matrix/media/v3/download/matrix.org/aVDDSRfZjRvSJrSEhlCOeXdB/pocketchange11.csv >

17:12:50 * xmrack[m] posted a file: (102KiB) <
https://libera.ems.host/_matrix/media/v3/download/matrix.org/YdaTvLpXfUOsHTgeNHvzIPyd/pocketchange12.csv >

17:13:21 <xmrack[m]> Everyone, feel free to take a look for yourself and see if we missed something

17:14:40 <xmrack[m]> https://paste.debian.net/1285721/

17:15:02 <xmrack[m]> Here is my code if anyone wants to sanity check

17:17:59 <rbrunner> Wondering who was doing 12-out txs before Pocket Change, and why ...

17:18:35 <rbrunner> Pocket changing "by hand" perhaps

17:18:59 <xmrack[m]> I also noticed that if you turn off pocket change all of your outputs will be combined
back together which is an obvious true spend

17:19:26 <xmrack[m]> yea 12 is a weird number

17:22:00 <rbrunner> I recently saw an estimate somewhere that Monero currently may have around a million
users, and with so many you probably get almost everything sooner or later

17:37:33 <xmrack[m]> I take it back

17:37:37 * xmrack[m] uploaded an image: (21KiB) <
https://libera.ems.host/_matrix/media/v3/download/matrix.org/oksHZttIAqoKfEyiQNKotrSE/image.png >

17:38:04 <xmrack[m]> Clear indication of when pocketchange was released

17:38:59 <xmrack[m]> y-axis is the number of 12 output transactions within a block

17:45:00 * xmrack[m] posted a file: (857KiB) < https://libera.ems.host/_matrix/media/v3/download/matrix.org/xu
NFFvnJEascXgsjefpSGDlj/updated%20-%20pocketchange12.csv >

17:45:53 <xmrack[m]> The original spreadsheet was difficult to view the data. Here is an updated copy that
should make it a lot easier

17:51:20 <xmrack[m]> https://xmrchain.net/search?value=2884485

17:51:34 <xmrack[m]> This block had 13 transactions with 12 outputs


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-07-11T23:31:23+00:00
- Closed at: 2023-07-17T05:44:30+00:00
