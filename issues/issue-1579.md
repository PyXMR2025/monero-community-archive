---
title: Using the GUI 12.3 requires entire wallet resync each time closed\opened. Using
  NANO S
source_url: https://github.com/monero-project/monero-gui/issues/1579
author: usmarine2141
assignees: []
labels:
- resolved
created_at: '2018-10-01T20:47:57+00:00'
updated_at: '2018-12-17T16:36:30+00:00'
type: issue
status: closed
closed_at: '2018-12-17T16:36:30+00:00'
---

# Original Description
Every time the GUI closes, and reopens have to resync the ENTIRE wallet blocks, not just what was missed. I have read there is a save button, but do not see a save button anywhere in the wallet GUI. 


NOTE: Created wallet using the GUI, by selecting the Ledger option. 

# Discussion History
## sanderfoobar | 2018-10-13T20:59:14+00:00
possibly related #1565

## dEBRUYNE-1 | 2018-12-17T08:03:20+00:00
@usmarine2141 - Did you manage to resolve this issue? If not, have you looked at the `It's imperative that the closing process of your Ledger Monero wallet is done in this specific consecutive order:` part of this guide?

https://monero.stackexchange.com/questions/9901/how-do-i-generate-a-ledger-monero-wallet-with-the-gui-monero-wallet-gui

## usmarine2141 | 2018-12-17T16:31:41+00:00
Yes i thought i had closed this issue.

On Mon, Dec 17, 2018 at 2:03 AM dEBRUYNE-1 <notifications@github.com> wrote:

> @usmarine2141 <https://github.com/usmarine2141> - Did you manage to
> resolve this issue? If not, have you looked at the It's imperative that
> the closing process of your Ledger Monero wallet is done in this specific
> consecutive order: part of this guide?
>
>
> https://monero.stackexchange.com/questions/9901/how-do-i-generate-a-ledger-monero-wallet-with-the-gui-monero-wallet-gui
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1579#issuecomment-447755049>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/ATwSo2wJLYaF5qJVWnp8FJ-hq1sHpsviks5u50_LgaJpZM4XC3AM>
> .
>


## dEBRUYNE-1 | 2018-12-17T16:34:34+00:00
All right, will close then.

## dEBRUYNE-1 | 2018-12-17T16:34:38+00:00
+resolved

# Action History
- Created by: usmarine2141 | 2018-10-01T20:47:57+00:00
- Closed at: 2018-12-17T16:36:30+00:00
