---
title: Installing Monero via Snap - Unknown Connections
source_url: https://github.com/monero-project/monero/issues/3237
author: TimeTravelersHackedMe
assignees: []
labels:
- invalid
created_at: '2018-02-06T20:24:59+00:00'
updated_at: '2018-06-18T15:17:18+00:00'
type: issue
status: closed
closed_at: '2018-06-18T15:17:18+00:00'
---

# Original Description
Hey, I installed Monero via the snap package and when I check out connections via netstat I see a bunch of a connections that the client makes even when it's not running... one of them is to:

echomike.de:18080 for instance

Is the Snap package mining on my server? Why is it running even before I run it?

# Discussion History
## moneromooo-monero | 2018-02-07T13:08:26+00:00
Monero makes connections when it's not running ? I'm sure you don't mean this. Please explain.

## lh1008 | 2018-02-07T13:19:25+00:00
I have not been able to run monero from a snap package. I´m using ubuntu 16.04.3 LTS. I´m able to see the monero snap package in terminal but can´t find the repository or which command to open monero. Sorry if this is not the correct post, but saw the title and thought someone could help. 

## juliavi | 2018-02-08T09:30:57+00:00
running 
`sudo snap start monero`
Doesn't start syncing, and doesn't allow to add the --testnet flag.
What would be the right way to run a testnet node from the snap?

## TimeTravelersHackedMe | 2018-02-08T15:02:35+00:00
The Snap package is named monero.monero-wallet-cli (and
monero.monero-wallet-rpc)

- Brian

On Feb 8, 2018 4:31 AM, "Julia Vishnevsky" <notifications@github.com> wrote:

> running
> sudo snap start monero
> Doesn't start syncing, and doesn't allow to add the --testnet flag.
> What would be the right way to run a testnet node from the snap?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3237#issuecomment-364053268>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AFaOlhbYHFWpn4oIq7OiqMrcG8AaXu-oks5tSr7agaJpZM4R7rX1>
> .
>


## juliavi | 2018-02-11T08:56:35+00:00
So snap doesn't support the latest build of monerod?
monerod replaced the former wallet-cli

## moneromooo-monero | 2018-06-18T14:52:28+00:00
I'm confused by the above.
The connection in the first post looks like a normal P2P connection at first glance. I'll assume that monerod is running and it's the user being confused. If monerod wasn't running, then it's something else that's connecting there, and thus not our problem in the first place :P

+invalid


# Action History
- Created by: TimeTravelersHackedMe | 2018-02-06T20:24:59+00:00
- Closed at: 2018-06-18T15:17:18+00:00
