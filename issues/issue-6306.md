---
title: 'Feature request: add editable sender/receiver fields for past incoming/outgoing
  transactions'
source_url: https://github.com/monero-project/monero/issues/6306
author: rating89us
assignees: []
labels: []
created_at: '2020-01-26T14:45:02+00:00'
updated_at: '2020-01-26T19:09:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In Monero, the sender and the destination addresses are impossible to know just by watching the blockchain data. This can be a problem when you receive a lot of transactions and want to track them years later (how much did I receive from Bob in the period of 2019-2023?)

Currently users can track senders by giving a different receiving address (subaddress) for each sender. This is useful for merchants, because they automatically generate a subaddresses for each purchase, but you can't expect common users will do this for every transaction they receive.

To track receivers, the monero wallet saves the destination address of all outgoing transactions (the receiver's name is not saved). Alternatively, users can add a note with the sender/receiver's name in description field.

Instead of using the above described methods, I suggest we add an editable field for every transaction: 
- Sender's name (of an incoming transaction)
- Receiver's name (of an outgoing transaction)

Some ideas:
- These fields should be editable and should only be used for internal control (not for auditing).
- They should be integrated with the contacts in address book. So when I send 1 XMR to John's address, the receiver's name field should automatically be set to "John". Also, after I received 2 XMR from Bob, I should be able to go to Transactions history (in Monero GUI) and select Bob from a dropdown list.
- When the wallet detects a new incoming transaction, a message could be displayed: "You received a new transaction with 1 XMR! If you want, you can store who was the sender (dropdown list with address book contacts) or add a note (description field with free text)".

# Discussion History
## moneromooo-monero | 2020-01-26T15:49:16+00:00
wallet2 (and simplewallet, I don't know about the GUI) can already attach a user defined text to any transaction. See set_tx_note and get_tx_note. This is free text, so you can your own comments, which could include the name of the other party, the reason for the tx, etc.

## rating89us | 2020-01-26T16:56:12+00:00
The idea is to create an additional field for each transaction that is used exclusively to store sender or receiver name, which is linked (or not) to a contact in address book.



## moneromooo-monero | 2020-01-26T19:09:42+00:00
Why would you want that ? Are there any advantages you can see ?

# Action History
- Created by: rating89us | 2020-01-26T14:45:02+00:00
