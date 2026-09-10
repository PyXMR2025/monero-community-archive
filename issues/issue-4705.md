---
title: GUI socks5 proxy setting actually defaults to socks4
source_url: https://github.com/monero-project/monero-gui/issues/4705
author: EntropyHoover
assignees: []
labels: []
created_at: '2026-09-09T06:11:59+00:00'
updated_at: '2026-09-09T07:41:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The GUI settings proxy is stated as : "Socks 5 proxy (updates downloading, fetching price sources)", but if the user did not explicitly state flag socks5:// , for example using 127.0.0.1 directly as ip address and port 9050 , the connection is actually defaulted to socks4.

tcpdump log for kraken api access

IP 127.0.0.1.49442 > 127.0.0.1.9050: Flags [P.], seq 1:25, ack 1, win 64, length 24
	0x0000:  0000 0000 0000 0000 0000 0000 0800 4500  ..............E.
	0x0010:  0040 c152 4000 4006 7b63 7f00 0001 7f00  .@.R@.@.{c......
	0x0020:  0001 c122 235a 13f4 f798 dfbd 3c8f 5018  ..."#Z......<.P.
	0x0030:  0040 fe34 0000 0401 01bb 0000 0001 0061  .@.4...........a
	0x0040:  7069 2e6b 7261 6b65 6e2e 636f 6d00       pi.kraken.com.
```
0x0030:  0040 fe34 0000 0401 01bb 0000 0001 0061 
                        ^here the 04 indicates the connection is socks4
```



# Discussion History
## nahuhh | 2026-09-09T07:41:09+00:00
Yea, it has said socks5 since before we had socks5 support 🙃

# Action History
- Created by: EntropyHoover | 2026-09-09T06:11:59+00:00
