---
title: Different address on Ledger and on monero-gui
source_url: https://github.com/monero-project/monero-gui/issues/3708
author: klinki
assignees: []
labels: []
created_at: '2021-09-22T17:00:13+00:00'
updated_at: '2021-09-22T17:05:48+00:00'
type: issue
status: closed
closed_at: '2021-09-22T17:01:20+00:00'
---

# Original Description
Hello,

I have noticed there is a different address displayed in monero-gui and in Ledger Nano S.
At first, I was worried there is something suspicious going on, but then I googled little bit and found out there are 2 formats for the same address and it is possible to use this page: https://xmr.llcoins.net/addresstests.html to transform address from one format to another. (By entering the original address into   `8. Public Address:`   field, clicking `Check address` button and verifying address from   `15. Standard XMR: ` field with address on Ledger).

I'm not sure whose fault it is, if it is wrong in monero-gui, or in Ledger, but it would be really nice to show the same address.
Maybe you could add the Standard XMR address and allow user to see both? Or add some sort of switch and toggle between them?

That would be really nice.
Thank you

 

# Discussion History
## selsta | 2021-09-22T17:01:20+00:00
It's an issue on the Ledger firmware side. See https://github.com/LedgerHQ/app-monero/issues/66

Not much we can do on the Monero side :/

## klinki | 2021-09-22T17:05:47+00:00
I see. I know it is inconvenient, but could you maybe add some configuration option to show the embedded real addresses instead of the integrated one? Or, as I suggested in first post, maybe allow user to see both or toggle between them?

I know it is not your fault that Ledger is doing it wrong, but this is very confusing for users.

# Action History
- Created by: klinki | 2021-09-22T17:00:13+00:00
- Closed at: 2021-09-22T17:01:20+00:00
