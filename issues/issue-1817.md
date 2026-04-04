---
title: date / time formatting in show_transfers
source_url: https://github.com/monero-project/monero/issues/1817
author: assylias
assignees: []
labels: []
created_at: '2017-02-27T19:16:49+00:00'
updated_at: '2018-03-25T13:08:40+00:00'
type: issue
status: closed
closed_at: '2017-03-02T17:39:04+00:00'
---

# Original Description
When calling `show_transfers` in the wallet, I get inconsistent formatting for the date column (third column). All entries up to 2017-02-23 are in a "yyyy-mm-dd" format but more recent entries are in "hh:mm:ss AM/PM" format. It looks like this:

Entries up to 23rd of Feb:

    1252318     out       2017-02-23       xxxxxx

More recent entry:

    1254774    out      08:01:11 PM     xxxxx

# Discussion History
## assylias | 2017-02-27T19:26:54+00:00
OK the code uses a different formatting when the transfer occurred less than 24 hours ago. See [`get_human_readable_timestamp`](https://github.com/monero-project/monero/blob/0e7722ff40fe0b27c225a53777543bf772389b19/src/simplewallet/simplewallet.cpp#L3377)

If one wants to extract the data and import it into a third party software (say Excel), it is going to cause issues. Is it possible to have a consistent formatting (maybe one column for the date and one for the time, or just a date/time column)?

## moneromooo-monero | 2017-02-27T20:33:42+00:00
That was on purpose (more granularity for recent txes). I did not think it was going to cause trouble.
If you want to automate things, you might be better off using RPC, and these will not call get_human_readable_timestamp. Is that a suitable alternative ?

## assylias | 2017-02-28T09:16:13+00:00
Yes sure - I suppose people who are less tech savvy will use the GUI anyway.

## lunacrypt | 2018-03-25T13:04:41+00:00
Excuse me replying to an closed issue, but I don't feel like it should be closed, yet.
I'm using the CLI in an automated environment and have many wallets open at the same time to execute various commands and parsing the output. Using RPC on top would add a lot overhead and tech dept just to get a accurate date / time.
I'm fine with the human readable format in the `show transfers` summary. But querying information specific to a transaction, I would expect a full timestamp in what ever reusable format.
I don't see any value for a user to have that valuable information stripped from every possible output.

# Action History
- Created by: assylias | 2017-02-27T19:16:49+00:00
- Closed at: 2017-03-02T17:39:04+00:00
