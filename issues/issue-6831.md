---
title: RPC connection failure due to SSL fingerprint mismatch does not produce a helpful
  error message
source_url: https://github.com/monero-project/monero/issues/6831
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-09-19T22:09:37+00:00'
updated_at: '2020-10-05T16:26:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When utilizing the "--daemon-ssl-allowed-fingerprints" option of the CLI wallet, fingerprint mismatches result in the Error: wallet failed to connect to daemon: http://ipaddress:18081. Daemon either is not started or wrong port was passed. Please make sure the daemon is running or change the daemon address using the 'set_daemon' command.

Suggest adding a warning specifically regarding SSL fingerprint failure.

# Discussion History
# Action History
- Created by: MoneroArbo | 2020-09-19T22:09:37+00:00
