---
title: 'monero-wallet-cli: do not use UTC time, or at least be clear thats what''s
  being used'
source_url: https://github.com/monero-project/monero/issues/8669
author: imfiesh
assignees: []
labels: []
created_at: '2022-12-05T00:39:19+00:00'
updated_at: '2024-07-31T23:16:57+00:00'
type: issue
status: closed
closed_at: '2024-07-31T23:16:57+00:00'
---

# Original Description
Both ```show_transfer``` and ```show_transfers``` displays the transaction timestamp using UTC time. This is different from the norm for UNIX based (or at least Linux based) software which normally use the localtime call which respects the TZ environment variable. If there is a good reason for using UTC, it should at least be clearly labeled as such, for example by adding the string "UTC" at the end. As it is now it can be confusing and potentially misleading in some situations, especially if you are in a timezone that is very close to UTC. If you are waiting for a incoming transaction and aren't careful you could potentially mistake a new transaction for an old one or vice versa. It gets extra confusing when combined with #8667

# Discussion History
## moneromooo-monero | 2023-01-01T10:28:30+00:00
For privacy reasons, time functions use GMT. It'd make sense to explicitely use local time on wallet info though.


## moneromooo-monero | 2023-01-01T10:37:19+00:00
It's unclear whether things like block timestamp in monerod should also use local time. It would be consistent, but the daemon logs by default, and GMT was used so that log sharing does not leak timezones. For now, I'll just add a "Z" suffix.

## moneromooo-monero | 2023-01-01T10:44:33+00:00
https://github.com/monero-project/monero/pull/8694

# Action History
- Created by: imfiesh | 2022-12-05T00:39:19+00:00
- Closed at: 2024-07-31T23:16:57+00:00
