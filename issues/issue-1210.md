---
title: Provide an easier way to export signed transaction data
source_url: https://github.com/monero-project/monero-gui/issues/1210
author: leafcutterant
assignees: []
labels: []
created_at: '2018-03-30T20:30:35+00:00'
updated_at: '2018-03-31T23:47:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For now, if one wants to extract signed transaction data, ~~they have to first create a watch-only wallet, wait until it finishes scanning the blockchain, create an unsigned transaction in that, export it, import it to the real wallet, sign it, and export that.~~ they can only do so in CLI, by starting it with --do-not-relay, making the transfer and then open the tx file.

~~This is a huge amount of hassle. Could there be an automated process? An option something like "Create signed tx file", which would be accessible in the real wallet, and would output the signed transaction data after entering the password.~~

Could this be streamlined in the GUI so that the transaction data can be accessed by the push of a button? E.g. having a `Generate transaction data` button on the Send tab, which would, similarly to sending, would ask for a confirmation and then the password, but instead of broadcasting the transaction, it would display the transaction data in raw hex and optionally in base64.



# Discussion History
# Action History
- Created by: leafcutterant | 2018-03-30T20:30:35+00:00
