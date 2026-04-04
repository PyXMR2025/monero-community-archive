---
title: Monero GUI (Flatpak) falsely appears to create a wallet despite having no access
  to the wallet file directory.
source_url: https://github.com/monero-project/monero/issues/8429
author: ForeverNooob
assignees: []
labels: []
created_at: '2022-07-11T20:06:43+00:00'
updated_at: '2022-07-11T20:06:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Flatpak (`org.getmonero.Monero` app to be exact) has sandboxed access to the filesystem. Currently, in this particular case, the app only has file creation and read access inside `~/Monero/`.

Here's the dangerous part:
When creating a new wallet, if you specify a path _outside_ of the allowed directory, then the app creates the wallet just fine, but if you look inside the specified path, no actual wallet files are created.

This means that when the app is closed, the wallet which was supposedly had been created is gone. So all created wallets using this method are essentially temporary.

This is obviously dangerous since the app lets the user falsely assume that the wallet is created normally and will persist across app launches.


Additional observations:
* Specifying a relative path, even an allowed one, evokes similar behavior as described above.
* During the wallet creation process, when selecting a path using "Browse" dialog (using a file manager), even if a path in the allowed directory is selected, the UI complains ("Wallet location is empty")


Flatpak version: `Monero 'Oxygen Orion' (v0.17.3.2-unknown)`
OS version: Ubuntu 18.04

# Discussion History
# Action History
- Created by: ForeverNooob | 2022-07-11T20:06:43+00:00
