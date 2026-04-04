---
title: Support allowed SSL fingerprints
source_url: https://github.com/monero-project/monero-gui/issues/3387
author: jluttine
assignees: []
labels: []
created_at: '2021-04-11T16:31:00+00:00'
updated_at: '2021-04-11T16:33:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero CLI wallet has the following option: `--daemon-ssl-allowed-fingerprints`

How can similarly set allowed daemon SSL certificates in the GUI wallet? Otherwise, I cannot securely connect to the daemon.

Also, would it then make sense to auto-accept CA-signed certificates in addition to manually entered fingerprints? I don't know. Manually entering the fingerprint(s) would suffice for me.

EDIT: Also, it would be nice if one could force SSL. That is, the client wouldn't connect unless SSL connection can be established and the fingerprint is ok. Otherwise, there's a risk of leaking the username and password. At the moment, I cannot use username+password authentication because there's no way I can be sure that the wallet has connected to the node securely.

# Discussion History
# Action History
- Created by: jluttine | 2021-04-11T16:31:00+00:00
