---
title: Enhancement request - more granular export_outputs options
source_url: https://github.com/monero-project/monero/issues/6664
author: Adreik
assignees: []
labels: []
created_at: '2020-06-18T06:12:11+00:00'
updated_at: '2020-06-19T00:23:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Currently the export_outputs command for both RPC and CLI exports either every output, including ones that have been spent, or all outputs that were not included in the last output export.

Consider the case of a wallet service similar where a high-availability server holds a private view key on the user's behalf, where bit rate is relatively low (For example, if it's transmitting data to the user's phone via SMS, where the user's private spend key is stored and transactions would be signed, key images computed and so on).

Due to bit rate constraint it would be preferable to be able to export a single owned output or only a few rather than all, especially considering that the number of outputs and therefore the size of the output export file for a regularly used wallet can get very large.

Criteria for selecting what outputs to export could include block ranges, a list of the outputs' pubkeys, key images, specific subaddress indices, filtering on only exporting outputs that are spent/unspent etc etc. 

There might also be a configuration option to exclude frozen outputs from appearing in export_outputs files.

An alternative could be if instead of an unstructured hex blob there was an option to export or import a list of outputs without encryption (where you could then apply your own encryption scheme after extracting the data you want).

# Discussion History
# Action History
- Created by: Adreik | 2020-06-18T06:12:11+00:00
