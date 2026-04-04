---
title: Update of the help documentation of monero-wallet-cli
source_url: https://github.com/monero-project/monero/issues/2643
author: 1337tester
assignees: []
labels: []
created_at: '2017-10-13T12:47:34+00:00'
updated_at: '2017-12-02T07:22:50+00:00'
type: issue
status: closed
closed_at: '2017-12-02T07:22:50+00:00'
---

# Original Description
There are some missing parameters + some small improvements in the help provided, listed as follows:

* "check_tx_key"
  * <txid> mandatory, but not mentioned in help
* "check_tx_proof "
  * <txid> mandatory, but not mentioned in help
* "export_key_images"
  * <filename> mandatory, but not mentioned in help
* "export_outputs"
  * <filename> mandatory, but not mentioned in help
* "import_key_images"
  * <filename> mandatory, but not mentioned in help
* "import_outputs"
  * <filename> mandatory, but not mentioned in help
* "set_tx_note"
  * [txid] and [free text note] needed, but not mentioned  in help + would be beneficial to mention how to prepare a tx for this tx_note, the 'transfer' command sends the tx immediately as far I understand 
* "show_transfer"
  * <txid> mandatory, but not mentioned in help
* "show_transfers"
  * Would be nice to provide also the column names in this list
* "sign"
  * <filename> mandatory, but not mentioned in help
* "sign_transfer"
  * parameters mandatory, but not mentioned in help
* "submit_transfer"
  * parameters mandatory, but not mentioned in help
* "verify"
  * parameters <filename> <address> <signature> mandatory, but not mentioned in help

# Discussion History
## moneromooo-monero | 2017-11-24T17:41:54+00:00
See https://github.com/monero-project/monero/pull/2832

# Action History
- Created by: 1337tester | 2017-10-13T12:47:34+00:00
- Closed at: 2017-12-02T07:22:50+00:00
