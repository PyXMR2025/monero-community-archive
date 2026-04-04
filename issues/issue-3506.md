---
title: '[feature] Accounts tab: view address on hardware wallet'
source_url: https://github.com/monero-project/monero-gui/issues/3506
author: jonathancross
assignees: []
labels: []
created_at: '2021-05-26T10:52:50+00:00'
updated_at: '2021-05-26T20:56:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It would be great if the user had a small eyeball icon on each address / subaddress allowing them to view the address on their hardware wallet.

The "View on hardware wallet" option would not be there for non-hardware wallets.


# Discussion History
## rating89us | 2021-05-26T11:40:47+00:00
This is already supported on Trezor, but on Receive page (#2221). Maybe you're refering to Ledger?

Also, I think that Account page shouldn't display any receiving address (#3128).



## jonathancross | 2021-05-26T13:36:51+00:00
> supported on Trezor, but on Receive page

Also supported by the Ledger Nano X as well on the Receive page.

I was referring to this feature being available for both hardware wallets on the **_Accounts_** tab/page (next to "copy to clipboard").

But I now see we are going in different directions as you believe addresses and "copy to clipboard" should be removed from that page entirely.  Personally I am not a fan of having to go to the **_Receive_** page for all of these functions.

## rating89us | 2021-05-26T20:56:25+00:00
I'm not against displaying an address on Accounts page, but IMO it should display an unused address every time the page is opened, to avoid address reusing.

# Action History
- Created by: jonathancross | 2021-05-26T10:52:50+00:00
