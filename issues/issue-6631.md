---
title: monerod only maintains an i2p outbound connection if --add-priority-node is
  used
source_url: https://github.com/monero-project/monero/issues/6631
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-06-06T11:31:21+00:00'
updated_at: '2022-07-20T22:59:55+00:00'
type: issue
status: closed
closed_at: '2022-07-20T22:59:55+00:00'
---

# Original Description
Basically what it says on the tin.

If I use the --add-peer flag, or no flag, I'm basically never able to maintain an outbound i2p connection. Sometimes it will successfully establish one, but it always drops after about a minute, give or take. It will try to establish new connections, but so many i2p addresses in my peer list are offline that it fails like 98% of the time. This is an even bigger issue than it would be because of #6590 where, when a tx is sent and there are no available i2p connections, it can get stuck in the local mempool even after an i2p connection is established.

The workaround I have found is to add a known working node as a priority node. The outbound connections still gets dropped just as often, but this way it immediately tries to re-establish a connection to a known working peer, as opposed to cycling through a list of offline peers.

I am including my [bitmonero.log](https://github.com/monero-project/monero/files/4739886/bitmonero.log.txt), which is split into two main sections. At the beginning, the log without a priority node. Then later, logs WITH a priority node. Sections of the log are labeled.

Not sure what the "real" issue is here -- maybe that offline nodes stay in the peer list for so long. Maybe that i2p connections only last ~1 minute. Maybe both. Maybe neither. But for me, --tx-proxy with i2p is essentially non-functional without taking this step of adding a priority node.

# Discussion History
## MoneroArbo | 2020-06-08T15:48:39+00:00
My [daemon log](https://github.com/monero-project/monero/files/4747047/bitmonero.log.txt) (with log level 0) over the past ~2 days, to give an idea of just how often outbound i2p connections fail. This is WITH --add-priority-node option using the dsc* address at https://github.com/i2p-zero/i2p-zero/blob/master/mipseed.md.

Without the option I actually see the error less often, I suppose because connections are rarely established to begin with.

## knaccc | 2020-06-13T21:50:34+00:00
I'm having similar issues. @selsta and niocbrrrrrr kindly set up mipseeds in the last few hours, and I've added their new seed nodes to the list in this doc: https://github.com/i2p-zero/i2p-zero/blob/master/mipseed.md (Note that the `core5....` address is not currently active).

I'm using this command to monitor I2P connections: `watch 'curl -H "Content-Type: application/json" --data "{\"public_only\":false}" http://127.0.0.1:18081/get_peer_list 2>/dev/null | grep -A 8 "i2p" | grep "i2p\|last_seen"'`

I then deleted the `.bitmonero/p2pstate.bin` file, started monerod and watched the output from the command I mentioned above. At first, I saw 10 I2P peers listed, all with `"last_seen": 0`. The only way it could have obtained this list of 10 I2P peers would have been if it had connected to an I2P peer, and so it's odd that that I2P peer it connected to was not listed with a recent `last_seen` timestamp.

A few minutes later, the list reduced to only 4 entries, with `"last_seen": 0` on all of them except for one peer (which was snbrpdeug2vuojer6ql6ozcbdzddxbdbi3yiv7avchwnzzocrlaq.b32.i2p).

niocbrrrrrr also noted he was seeing the error in monerod: `Lost all outbound connections to anonymity network - currently unable to send transaction(s)`.

Edit: a few minutes after I posted this comment, the list expanded to 5 entires. Strangely, the new addition still has `"last_seen": 0`

I also suddenly saw a strange entry `"last_seen": 0,9`:
````
"host": "sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p:18080",
    "last_seen": 0,9
````

It's also strange that there are port numbers (e.g. `:18080`) appended to I2P addresses, since I2P addresses are not supposed to have port numbers.

## MoneroArbo | 2020-06-14T11:31:56+00:00
>It's also strange that there are port numbers (e.g. :18080) appended to I2P addresses, since I2P addresses are not supposed to have port numbers.

I think i2p (not i2p zero) can map specific ports on addresses? Not sure about that. But if so, it makes sense to include the port number. I will say though, I sometimes see my daemon trying to connect its own i2p address in the log and there's always a port number, even though I don't list one in my --anonymous-inbound flag. So, it's getting added on somewhere along the way. Could explain why, in some cases, I see the same address listed with two different ports.

Anyway, here's the current output of that command for me:

```
    "host": "oryrzlz3ymti6v543x4juu6jhgzsxohafftn6ajli5v5eh7f5iqa.b32.i2p:18080",
    "last_seen": 0,
    "host": "rmy5sqcoob4zdeqstjn6qgrvxqbk4ackrync77m437klegmqcitq.b32.i2p:18080",
    "last_seen": 0,
    "host": "sygqvtafzqvk3zmwmuiaihrjtjghcfqwgrdxypjpnbhc4qmsraoq.b32.i2p:18080",
    "last_seen": 0,
    "host": "dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p:18080",
    "last_seen": 0,
    "host": "dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p:38080",
    "last_seen": 1591444885,
    "host": "io2tn2fjzz2cfsm3plichw2sn4jyrq7lo5mfzuqgtsdcqytpgcka.b32.i2p:18080",
    "last_seen": 0,9
    "host": "moneroti7lckp4hjrqckoq5cfi2apuyxia42sp5x7tkbzjfwqfiq.b32.i2p:18080",
    "last_seen": 0,9
    "host": "p4m3hm3usjgfc7gj2usdbu5xvkgqfsf723qvzfqozqmi7eprutqq.b32.i2p:18080",
    "last_seen": 0,
    "host": "sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p:18080",
    "last_seen": 1592085756,
    "host": "snbrpdeug2vuojer6ql6ozcbdzddxbdbi3yiv7avchwnzzocrlaq.b32.i2p:18080",
    "last_seen": 1592127539,
    "host": "snbrpdeug2vuojer6ql6ozcbdzddxbdbi3yiv7avchwnzzocrlaq.b32.i2p:28082",
    "last_seen": 0,9
    "host": "y3hxuiaotzamn5s36yb3yjhwr4q5zryfz4bnfkixz6seg4paji7q.b32.i2p:18080",
    "last_seen": 0,9
    "host": "yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p:18080",
    "last_seen": 1592078995,
```

**edit:**

I just cleared my p2p state, added the new seed nodes, now the output of that command looks like:

```
    "host": "aakazsmlk27gjit2wcleguduhb3af77fj3ofyigeffkrc2rtd56q.b32.i2p",
    "last_seen": 0,
    "host": "dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p",
    "last_seen": 0,
    "host": "dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p:38080",
    "last_seen": 0,
    "host": "nqussuztpeyrbtxz7j6fc32lugwm4ajincm5emqueihlbxq2rtza.b32.i2p",
    "last_seen": 0,
    "host": "nqussuztpeyrbtxz7j6fc32lugwm4ajincm5emqueihlbxq2rtza.b32.i2p:18080",
    "last_seen": 0,
    "host": "nqussuztpeyrbtxz7j6fc32lugwm4ajincm5emqueihlbxq2rtza.b32.i2p:38080",
    "last_seen": 0,
    "host": "snbrpdeug2vuojer6ql6ozcbdzddxbdbi3yiv7avchwnzzocrlaq.b32.i2p:28082",
    "last_seen": 0,
    "host": "y3hxuiaotzamn5s36yb3yjhwr4q5zryfz4bnfkixz6seg4paji7q.b32.i2p",
    "last_seen": 0,
    "host": "y3hxuiaotzamn5s36yb3yjhwr4q5zryfz4bnfkixz6seg4paji7q.b32.i2p:18080",
    "last_seen": 0,
    "host": "dsc7fyzzultm7y6pmx2avu6tze3usc7d27nkbzs5qwuujplxcmzq.b32.i2p:18080",
    "last_seen": 1592135340,
    "host": "sel36x6fibfzujwvt4hf5gxolz6kd3jpvbjqg6o3ud2xtionyl2q.b32.i2p:18080",
    "last_seen": 1592135395,
    "host": "snbrpdeug2vuojer6ql6ozcbdzddxbdbi3yiv7avchwnzzocrlaq.b32.i2p:18080",
    "last_seen": 1592135374,
    "host": "yht4tm2slhyue42zy5p2dn3sft2ffjjrpuy7oc2lpbhifcidml4q.b32.i2p:18080",
    "last_seen": 1592135427,
```

I added the peers without ports, but as you can see they were re-added to my list basically immediately, but with port numbers. The entries with port numbers are also the only ones with a last_seed != 0.

**edit2:** The dsc* address is now showing up in my peer list twice again, one with port 38080 and one with18080. Three times if you count the original entry with no port #.

Also starting to see some of the `"last_seen": 0,9` entries again.

## knaccc | 2020-06-14T12:36:07+00:00
I have access to dsc's node, and it does not specify port 38080 anywhere, and is not listening on that port via IPv4. 

## MoneroArbo | 2020-06-14T20:26:47+00:00
On the plus side, after adding the new peers from [mipseed.md](https://github.com/i2p-zero/i2p-zero/blob/master/mipseed.md) as priority nodes, I've gone ~8 hours with zero `Lost all outbound connections to anonymity network` errors. Outbound connections are lasting up to 5 minutes and I'm consistently connecting to all the listed addresses except core*.i2p, which I haven't seen.

That's, you know, usable.

## xanoni | 2021-08-17T23:13:00+00:00
Could someone share their (sanitized) daemon `.conf` file please? I think I'm screwing something up, I can't get inbound connections despite `anonymous-inbound` (neither I2P nor Tor). Thank you.

See my ticket here: https://github.com/monero-project/monero/issues/7863

## deutrino | 2022-06-10T02:31:47+00:00
> The workaround I have found is to add a known working node as a priority node. The outbound connections still gets dropped just as often, but this way it immediately tries to re-establish a connection to a known working peer, as opposed to cycling through a list of offline peers.

I'm experiencing this exact same behavior on Tor, BTW, with the exact same workaround of adding priority nodes.

I've found one needs about 6 to 8 vetted (as in, looked up on node lists which list uptime and how long active) and fairly reliable priority Tor nodes to eliminate 99% of the "unable to send transactions" messages in the logs.

## selsta | 2022-07-20T22:59:55+00:00
Should be solved in v0.18.0.0

# Action History
- Created by: MoneroArbo | 2020-06-06T11:31:21+00:00
- Closed at: 2022-07-20T22:59:55+00:00
