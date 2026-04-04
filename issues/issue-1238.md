---
title: Dynamic embedded version recognition
source_url: https://github.com/monero-project/monero-gui/issues/1238
author: leafcutterant
assignees: []
labels:
- resolved
created_at: '2018-04-01T00:36:23+00:00'
updated_at: '2018-04-04T05:54:18+00:00'
type: issue
status: closed
closed_at: '2018-04-04T05:54:18+00:00'
---

# Original Description
I updated the Monero binaries used by the GUI to 0.12, but it still displays the old version number in Settings -> Debug info.

I propose it not to be a static piece of text but actually checking the Monero version in the background and display the version properly.

# Discussion History
## pazos | 2018-04-01T23:29:53+00:00
I think you're mixing monerod version with the api version . Replacing monerod does not affect the gui, since it was built against a specific api and this api does not change until you replace monero-wallet-gui too. The api is part of the main monero repo.

This is debug info obtained at build time. monero version matches the api & monerod bundled with the software, so it's ok for me.

## leafcutterant | 2018-04-02T00:15:47+00:00
GUI releases are very sparse in time, so manually updating monerod used by the GUI makes sense.

If indeed this doesn't change the functioning of the GUI client, then feel free to close the issue.

## sanderfoobar | 2018-04-04T05:49:00+00:00
+resolved

# Action History
- Created by: leafcutterant | 2018-04-01T00:36:23+00:00
- Closed at: 2018-04-04T05:54:18+00:00
