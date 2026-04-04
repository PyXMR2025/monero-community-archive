---
title: Cannot connect to remote node over Tor using monero-wallet-gui on macOS (connecting
  to node using cURL works)
source_url: https://github.com/monero-project/monero-gui/issues/3552
author: sunknudsen
assignees: []
labels: []
created_at: '2021-06-10T20:37:13+00:00'
updated_at: '2022-11-14T10:37:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hey guys,

Experimenting with Monero (amazing project btw)… running my own remote node over Tor (using client auth).

When I try to connect to my node on macOS running `/Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui --disable-check-updates --socks5-proxy 127.0.0.1:9050` (using advanced mode configuring onion address and port in settings), following error is thrown and connection fails.

```shell
2021-06-10 20:27:18.620	E error: resolve: Host not found (authoritative)
```

That said, running following on same computer works which appears to reveal issue is related to Monero app vs my node or network (onion address has been redacted).

```console
$ curl --socks5-hostname 127.0.0.1:9050 --digest -X POST http://***.onion:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    …
  }
}
```

I am also able to connect to my node on Tails.

Any ideas what I might be doing wrong?

Thanks for helping out!

# Discussion History
## rating89us | 2021-07-16T06:54:28+00:00
Monero GUI doesn't include a bundled Tor, so you need to start standalone Tor (use SOCKS5 port 9050) or Tor Browser (use SOCK5 port 9150) before trying to connect to your .onion remote node.

# Action History
- Created by: sunknudsen | 2021-06-10T20:37:13+00:00
