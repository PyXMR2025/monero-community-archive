---
title: 'Linux: Ledger documentation improvements'
source_url: https://github.com/monero-project/monero/issues/4930
author: EmbeddedAndroid
assignees: []
labels: []
created_at: '2018-12-02T20:39:27+00:00'
updated_at: '2018-12-02T21:06:15+00:00'
type: issue
status: closed
closed_at: '2018-12-02T21:06:15+00:00'
---

# Original Description
Perhaps I missed the relevant documentation, but I ran through setting up a Ledger with the statically linked prebuilt v13.0.4 release binaries on Linux, and ran into a few issues which caused me to google for various solutions. I was a bit surprised this wasn't documented in this repo somewhere, and to help I'd be willing to add this information to the README if there is interest. 

When running ```./monero-wallet-gui or ./start-gui.sh``` I get the following error

```
error while loading shared libraries: libhidapi-libusb.so.0
```

Google led me to this thread: https://monero.stackexchange.com/questions/10361/gui-monerod-v0-13-0-3-does-not-start-on-linux-because-of-monero-wallet-gui 

Then I tried to setup a new ledger wallet and hit a problem with the wallet unable to access the Ledger. Turns out it was the lack of udev rules as documented here: https://github.com/LedgerHQ/ledger-nano-s/issues/38

Simple to fix these issues, but this answer would be helpful IMO if this was in the README somewhere for all us Linux users.



# Discussion History
## moneromooo-monero | 2018-12-02T20:57:09+00:00
The 

> error while loading shared libraries: libhidapi-libusb.so.0

error seems like some misconfiguration on your system. Maybe you installeda libhidapi-libusb on some custom path ? In that case you need to set LD_LIBRARY_PATH. In any case, this is not the GUI repo, you want https://github.com/monero-project/monero-core.

For the udev stuff, feel free to add it to the README if it's not there.


## EmbeddedAndroid | 2018-12-02T21:06:15+00:00
I don't recall installing libhidapi-libusb to a custom location (just the Debian packager manager) but I suppose it's possible.  Thanks for the feedback I'll open a PR to update the documentation in the monero-core project.

# Action History
- Created by: EmbeddedAndroid | 2018-12-02T20:39:27+00:00
- Closed at: 2018-12-02T21:06:15+00:00
