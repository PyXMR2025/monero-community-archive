---
title: '"Unsupported transaction" error on v7 when restoring from seed'
source_url: https://github.com/monero-project/monero/issues/2943
author: ghost
assignees: []
labels:
- duplicate
created_at: '2017-12-16T20:31:56+00:00'
updated_at: '2017-12-16T23:32:24+00:00'
type: issue
status: closed
closed_at: '2017-12-16T23:32:24+00:00'
---

# Original Description
Starting at line 377: https://paste.fedoraproject.org/paste/ojDZ7eTU5t4DYKbx5AJN-Q

I also have the log-level 2 of the wallet log, but it's over 70MB, so let me know what portion of that you might need and I'll fpaste it.

# Discussion History
## ghost | 2017-12-16T20:39:38+00:00
I looked up one of those "unsupported" errors in the monero-wallet-cli.log file. When it's syncing blocks the log file says this:

2017-12-16 20:21:24.289	    7f47800c9740	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1311	Processed block: <e072be6c40a2482c4289436a0cd7bcdc6ea69ddeb856178ccf6203357da67bff>, height 995436, 0(0/0)ms
2017-12-16 20:21:24.290	    7f47800c9740	INFO 	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:293	failed to deserialize extra field. extra = 020054686973207478207761732067656e65726174656420627920436f696e6f6d6901a9f72ba7a9170d0e40ad0d9c22233b476517945ae33ddc29a2d8bcdb2e4309af
2017-12-16 20:21:24.290	    7f47800c9740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:875	Transaction extra has unsupported format: <93278cde512ceeb6d2a8f102d3014c7253d9208de2c63362e37d4a92ee520a7e>
2017-12-16 20:21:24.290	    7f47800c9740	WARN 	wallet.wallet2	src/wallet/wallet2.cpp:890	Public key wasn't found in the transaction extra. Skipping transaction <93278cde512ceeb6d2a8f102d3014c7253d9208de2c63362e37d4a92ee520a7e>
2017-12-16 20:21:24.290	    7f47800c9740	INFO 	msgwriter	src/common/scoped_message_writer.h:102	
Height 995437, transaction <93278cde512ceeb6d2a8f102d3014c7253d9208de2c63362e37d4a92ee520a7e>, unsupported transaction format
2017-12-16 20:21:24.290	    7f47800c9740	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:1311	Processed block: <9160dc28d0236622fbc57c772ce26c81239bdb9500832347f7aef6397a4fbead>, height 995437, 1(0/1)ms

## moneromooo-monero | 2017-12-16T23:31:25+00:00
See 2875

+duplicate


# Action History
- Created by: ghost | 2017-12-16T20:31:56+00:00
- Closed at: 2017-12-16T23:32:24+00:00
