---
title: '"Export all History" CSV: output should be sorted by date'
source_url: https://github.com/monero-project/monero-gui/issues/3907
author: molecular
assignees: []
labels: []
created_at: '2022-05-01T06:31:34+00:00'
updated_at: '2022-05-05T13:32:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I hope this is correct repo for "monero-wallet-gui".

I use the "Export all History" function to import tx data into a self-made accounting database. 

For the import itself the order in the CSV file is not important, but I usually look at a diff vs. an older version of the export to see what changed and if the order is seemingly random and changes (at least I observe this when connecting to a different node), the diff will just say "everything changed", which is not helpful.

Expectation: rows in export CSV are sorted by date
Status quo: rows in export CSV are in some order unknown to me


# Discussion History
## selsta | 2022-05-01T06:48:25+00:00
As a workaround you could use the `sort` command before creating a diff.

## plowsof | 2022-05-05T13:32:01+00:00
@molecular i recently made a crude python json-RPC script which interacts with the monero-wallet-rpc to '[get_transactions](https://monerodocs.org/interacting/monero-wallet-rpc-reference/#get_transfers') -> 'make a csv file' [here](https://github.com/plowsof/check-monero-bounties-subad/blob/bcf9a16be2092d579111aec9577cc0d2196e8371/bounties-parser.py#L38) if you would like something similar to this let me know :)

# Action History
- Created by: molecular | 2022-05-01T06:31:34+00:00
