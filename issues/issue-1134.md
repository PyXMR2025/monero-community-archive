---
title: Testnet daemon says I'm synchronized with the network, but status stuck on
  99.2%.  Never shows 100%.
source_url: https://github.com/monero-project/monero/issues/1134
author: phloatingman
assignees: []
labels: []
created_at: '2016-09-25T18:52:23+00:00'
updated_at: '2017-10-03T11:36:22+00:00'
type: issue
status: closed
closed_at: '2017-10-03T11:36:22+00:00'
---

# Original Description
![](https://ipfs.pics/ipfs/QmVqZq8GdLim4UbKnayaYMYP57BAdxh5VU6ZM4cNky3PRJ)

I'm still able to transfer testnet coins between wallets.  The unlocked balance reports everything fine even though the daemon says 99.2%.


# Discussion History
## moneroexamples | 2016-09-26T05:04:41+00:00
It happens sometimes. Dont know exactly why, but my guess is that its due to lack of up-to-date  peers to synchronise with. 


## moneromooo-monero | 2016-09-26T07:01:37+00:00
Does https://github.com/monero-project/monero/pull/1133 help ?


## moneromooo-monero | 2016-10-01T09:17:49+00:00
On testnet, it might be because we rolled back testnet to allow a change in the rct signature encoding. This would have meant that for a while, the "real" chain would have been shorter than the longest (since the longest would have had invalid blocks due to the change).


## ElLamparto | 2016-10-10T10:32:29+00:00
monerod reached 100% and then fall to 99%,, 98% though being connected all the time.
Currently it shows "3 days behind" (first entry from the top), while the client shows "synced".

![moneroblocks](https://cloud.githubusercontent.com/assets/9163437/19233377/71365ede-8ee5-11e6-98b5-89be56a98af6.png)

Debian Jessie 32bit, monero Wolfram Warptangent.


## ElLamparto | 2016-10-14T10:18:54+00:00
UPDATE: It looks like my database is no longer updated, I am many days behing (though online).

Debian Jessie 32bit, monero Wolfram Warptangent.


## ElLamparto | 2016-11-21T10:56:08+00:00
Should I open a new ticket for this? Since my db is not updated, **I can no longer use Monero**.
Is there anything that I can do to change it?

## ghost | 2016-12-05T00:18:26+00:00
@ElLamparto What do you mean by not updated? I would recommend closing this issue if solved and opening a new one to address the new specific issue you've discovered.

## ElLamparto | 2016-12-06T09:46:47+00:00
@NanoAkron, This issue is not solved. Please see my previous entries in this ticket (especially the one of 10 Oct. with screenshots). It should be clear.

## ElLamparto | 2017-01-01T17:34:00+00:00
Shortly again. At certain moment, monerod stops syncing, all I get are entries like:
2017-Jan-01 09:37:26.798813 [P2P1][193.70.8.151:18080 OUT]Sync data returned a new top block candidate: 1017006 -> 1214096 [Your node is 197090 blocks (273 days) behind]

I NO LONGER get:
2016-Dec-31 02:42:34.072885 [P2P9][195.154.207.151:18090 OUT]Synced 1009806/1213156

I've possibly found a workaround: setting the throttle correctly. If too high or too low, at certain height monerod stops syncing.

The below settings seem to work:
./monerod --limit-rate-up 10 --limit-rate-down 500

Attached is a level 1 log covering about 30 minutes, with throttle by default (too high vs my Internet connection speed). Please have a look at it.
[bitmonero.log.zip](https://github.com/monero-project/monero/files/680100/bitmonero.log.zip)

I keep testing. If OK, I will close this ticket one week from now.

Monero 'Wolfram Warptangent' (v0.10.1.0-release)
Debian Jessie 32bit, SSD


## moneromooo-monero | 2017-01-29T14:41:44+00:00
That log shows blocks being added. Maybe it just got a lot slower ?

## ElLamparto | 2017-02-14T10:41:42+00:00
@moneromooo-monero, maybe. There is no doubts about one thing: adding blocks slows down dramatically when approching 100%. Shutting down monerod for 24 hours (fully synchronized) will require 2-3 days to get to 100% again.

On the other hand, once 100% synchronized, it remains synchronized without problems.

Bitcoin and Litecoin (Core) synchronize at a steady rate until synchronized. It would be great if monerod were able to do the same.

## moneromooo-monero | 2017-02-18T17:29:42+00:00
It can sync at a steady rate if you use --fast-block-sync 0. That'll slow it down though.
Current master should be a good bit faster for HDDs (the tester reported about 4 times as fast). That might help.

## moneromooo-monero | 2017-10-03T11:31:00+00:00
That all seems to be fixed. The original problem (stuck 99.2%) should be fixed by the recent target height updating.

+resolved

# Action History
- Created by: phloatingman | 2016-09-25T18:52:23+00:00
- Closed at: 2017-10-03T11:36:22+00:00
