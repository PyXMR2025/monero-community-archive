---
title: Remove "Copy" Button Next to QR Code
source_url: https://github.com/monero-project/monero-gui/issues/3243
author: needmoney90
assignees: []
labels: []
created_at: '2020-11-20T19:40:36+00:00'
updated_at: '2021-04-19T05:29:30+00:00'
type: issue
status: closed
closed_at: '2021-01-21T03:39:53+00:00'
---

# Original Description
After some discussion with Selsta in #monero-dev (and with an affected user), I propose that we remove the "Copy to Clipboard" button that appears next to the scannable QR code, due to it being both redundant and confusing.

![gui_copy](https://user-images.githubusercontent.com/3836500/99842258-592efa00-2b24-11eb-9ceb-14a53ca067d8.png)

The first button copies the wallet address as expected (437KEQM2VQYjbkbCZk1UWpBo5RsdpawhudDVSzsYK31rSxYnTdQWq6dTno7wrejs2p8yN1hChGxHbEcBUTKZ16GbDedGa2w), whereas the second button copies the  QR-ified version of the address (monero:437KEQM2VQYjbkbCZk1UWpBo5RsdpawhudDVSzsYK31rSxYnTdQWq6dTno7wrejs2p8yN1hChGxHbEcBUTKZ16GbDedGa2w). 

The QR-ified version of the wallet address apparently causes errors when entered into exchanges which don't sanity-check wallet addresses in the browser (bitfinex specifically in this case). It is not immediately apparent to the user that the copied address contains an extra prefix (that isn't even useful if you aren't scanning a QR), which is a UX concern.

# Discussion History
## needmoney90 | 2020-11-20T19:46:06+00:00
Alternatively, removing the prefix would be acceptable as well. The buttons are still kind of redundant, but at least we won't have users with stuck exchange withdrawals.

## AlpineVibrations | 2021-02-18T07:08:17+00:00
having the copy button right next to the qr code is really nice for new users. its very direct. the little clipboard icon is not clear whats going on. the problem is just that the copy to clipboard button copies in the "monero:" text. I think the copy button should remain next to the qr image and the "monero:" text should be removed from the copied text.

## selsta | 2021-04-19T05:29:30+00:00
@lucas-wade see #3415

# Action History
- Created by: needmoney90 | 2020-11-20T19:40:36+00:00
- Closed at: 2021-01-21T03:39:53+00:00
