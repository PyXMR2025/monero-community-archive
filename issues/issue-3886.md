---
title: Adding new address book entry corrupts previous entries (bug)
source_url: https://github.com/monero-project/monero-gui/issues/3886
author: edisondotme
assignees: []
labels: []
created_at: '2022-04-13T00:22:42+00:00'
updated_at: '2022-04-13T00:32:44+00:00'
type: issue
status: closed
closed_at: '2022-04-13T00:24:35+00:00'
---

# Original Description
I encountered a serious bug with the address book today that cost me $100 in XMR
My steps to reproduce:

1. Have a few entries in the address book (4 in my case)
2. Click "Add address"
3. Fill out address information
4. Monero GUI adds the new entry to the bottom, but OVERWRITES the first address label with the newly created address book entry label while leaving the alphanumeric address intact.

I accidentally sent some XMR to the wrong address this way. Luckily the recipient was contactable and he was nice enough to send it back, but this could have gone much worse!

# Discussion History
## selsta | 2022-04-13T00:24:35+00:00
Hello, thank you for the bug report. We have it already fixed in code and it will be included in the next release, which I hope will be released in 2 weeks or so.

## edisondotme | 2022-04-13T00:32:44+00:00
Excellent! Sorry to leave a possible duplicate bug report. Thanks!

# Action History
- Created by: edisondotme | 2022-04-13T00:22:42+00:00
- Closed at: 2022-04-13T00:24:35+00:00
