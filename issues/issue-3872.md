---
title: Bug in Address book when adding entries
source_url: https://github.com/monero-project/monero-gui/issues/3872
author: JRB202
assignees: []
labels: []
created_at: '2022-03-25T10:51:32+00:00'
updated_at: '2022-03-25T11:29:14+00:00'
type: issue
status: closed
closed_at: '2022-03-25T11:29:13+00:00'
---

# Original Description
To reproduce :

Install monero gui latest march 2022 version on windows 10

Create a wallet

Create a 1rst entry in Address book with name and XMR address.

Then Add other entries

The bug :

After each add of a new entry (IP and Name)  the name of entry of the first entry (zero index) is overwritten 
with the name of of the last created entry.

Apparently, xmr address is left untouched in the first entry, only the name is lost






# Discussion History
## JRB202 | 2022-03-25T11:00:02+00:00
Problem still here with V0.17.3.1

## selsta | 2022-03-25T11:29:13+00:00
Thanks for the report, this is already fixed in the codebase. The next release will solve this.

# Action History
- Created by: JRB202 | 2022-03-25T10:51:32+00:00
- Closed at: 2022-03-25T11:29:13+00:00
