---
title: Usage of `std::get_time`
source_url: https://github.com/monero-project/monero/issues/2984
author: arnuschky
assignees: []
labels: []
created_at: '2017-12-21T14:54:29+00:00'
updated_at: '2018-01-18T23:48:29+00:00'
type: issue
status: closed
closed_at: '2018-01-18T23:48:29+00:00'
---

# Original Description
Current master uses `std::get_time` in `contrib/epee/include/storages/portable_storage_val_converters.h`. This isn't available in GCC 4.x, which should be sufficient as per the requirements. Do you want to update the requirements or shall we replace that method?

# Discussion History
## moneromooo-monero | 2017-12-21T15:48:55+00:00
If it's the only thing that's borked there, I'd rather we fix it. strptime should do the trick.
Can you confirm it's the only thing (or list others if not) ?

## moneromooo-monero | 2017-12-21T16:06:35+00:00
https://github.com/monero-project/monero/pull/2986

## arnuschky | 2017-12-21T21:07:12+00:00
:+1:  Worked great, thanks. Managed to build it with gcc 4.8.4

## moneromooo-monero | 2018-01-18T23:34:00+00:00
+resolved

# Action History
- Created by: arnuschky | 2017-12-21T14:54:29+00:00
- Closed at: 2018-01-18T23:48:29+00:00
