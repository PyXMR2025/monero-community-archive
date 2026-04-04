---
title: local stagenet node can not connect
source_url: https://github.com/monero-project/monero-gui/issues/3962
author: plowsof
assignees: []
labels: []
created_at: '2022-07-09T01:26:10+00:00'
updated_at: '2022-07-11T03:07:33+00:00'
type: issue
status: closed
closed_at: '2022-07-11T03:07:33+00:00'
---

# Original Description
[in my version of reality] when you start gui and open a stagenet wallet with a `./monerod --stagenet` already running, it is unable to connect. however if you select `Remote node` and input `localhost:38081` it connects fine.. clicking on `Local` again to double check and yes unable to connect.

looking around in the source, i decided to hardcode the default port of testnet and 'default' to 38081 https://github.com/monero-project/monero-gui/blob/b26f38d37ed81e84e51199425a633bc517f7bec2/main.qml#L2255
```C++
    function getDefaultDaemonRpcPort(networkType) {
        switch (networkType) {
            case NetworkType.STAGENET:
                console.log("[DEBUG]: STAGENET");
                return 38081;
            case NetworkType.TESTNET:
                console.log("[DEBUG]: TESTNET");
                return 38081;
            default:
                console.log("[DEBUG]: DEFAULT");
                return 38081; //<-- we always end up here for stagenet wallet.. nettype == 2 and persistant settings == 2 
                //perhaps NetworkType.STAGENET is not set correctly?
        }
    }
```
I was unable to see these console.log messages but through process of elimination , when opening a stagenet wallet the networktype is neither stagenet or testnet, it uses default (18081) so unable to connect.

the correct value should be read from here but apparently not:
https://github.com/monero-project/monero-gui/blob/b26f38d37ed81e84e51199425a633bc517f7bec2/main.qml#L94

this looked weird how mainnet is set but the others not?

https://github.com/monero-project/monero/blob/424e4de16b98506170db7b0d7d87a79ccf541744/src/wallet/api/wallet2_api.h#L45

now i can review #3734 with a local stagenet node :smile: 

# Discussion History
# Action History
- Created by: plowsof | 2022-07-09T01:26:10+00:00
- Closed at: 2022-07-11T03:07:33+00:00
