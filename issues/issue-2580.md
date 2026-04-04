---
title: cryptonote::OUTPUT_DNE error flooding logs
source_url: https://github.com/monero-project/monero/issues/2580
author: emesik
assignees: []
labels: []
created_at: '2017-10-04T21:50:39+00:00'
updated_at: '2017-10-07T01:08:23+00:00'
type: issue
status: closed
closed_at: '2017-10-07T01:08:23+00:00'
---

# Original Description
I have my monerod logs being flooded by stack traces of _cryptonote::OUTPUT_DNE_ error.

The log: [monero-bug.log](https://github.com/monero-project/monero/files/1357427/monero-bug.log)

By function names (_tx_memory_pool_, _check_tx_inputs_, _get_output_key_) I guess this is somebody trying to broadcast invalid transactions.

However, if this is something serious, a more user-friendly message would be nice and the log level could be perhaps higher (ERROR ?)

If this is not important, perhaps demoting it to loglevel DEBUG would be a good idea?

# Discussion History
## moneromooo-monero | 2017-10-04T22:04:44+00:00
Please restart with --log-level 1,\*pool\*:DEBUG,*msg:INFO
Then paste a new log with the extra info.

## emesik | 2017-10-07T01:08:23+00:00
The messages stopped appearing. Perhaps it was someone trying to publish invalid transactions. If that happens again and I'm able to provide more details, I'll reopen.

# Action History
- Created by: emesik | 2017-10-04T21:50:39+00:00
- Closed at: 2017-10-07T01:08:23+00:00
