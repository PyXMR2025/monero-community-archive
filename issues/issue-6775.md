---
title: --txpool-notify propsal
source_url: https://github.com/monero-project/monero/issues/6775
author: wojtasss
assignees: []
labels: []
created_at: '2020-08-23T15:45:34+00:00'
updated_at: '2020-08-26T17:04:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It would be nice to have similar notify as --tx-notify in wallet but wtih new pending transactions in txpool, is possible to implement it?

# Discussion History
## ndorf | 2020-08-24T19:41:08+00:00
I agree this could be convenient. 

You could also try the [new ZeroMQ pub/sub feature](https://github.com/monero-project/monero/pull/6418/files) (just merged a couple of weeks ago), and subscribe to `txpool_add`.

ZeroMQ has binding for most popular languages, so you could easily write a script in Python, NodeJS, or whatever language you prefer.

## wojtasss | 2020-08-24T20:09:29+00:00
@ndorf sounds great! Need I use bindings for ZeroMQ for particular language or can just connect websockets to this ZeroMQ on Monero full node?

## ndorf | 2020-08-24T20:25:09+00:00
WebSockets are unrelated to ZeroMQ. You would need to use a ZeroMQ binding. It's not hard; here's a simplistic example in Python:

```
import zmq

ctx = zmq.Context()
sock = ctx.socket(zmq.SUB)

sock.connect("ipc:///var/run/monero/zmqpub.sock")
print("Connected to daemon")

sock.subscribe("json-minimal-txpool_add")
print("Subscribed")

while True:
    msg = sock.recv()
    print("Received message: %s" % msg)
```

Now run `monerod` with the `--zmq-pub ipc:///var/run/monero/zmqpub.sock` option, and this script. Output: 
```

Connected to daemon
Subscribed
Received message: b'json-minimal-txpool_add:[{"id":"713499fd605d99d01db6d2cc47af04dee7984006ac440c23add6e16cb1800992","blob_size":2589}]'
Received message: b'json-minimal-txpool_add:[{"id":"cbd20fe6764582dc66d398e2f92561cf4035015fa25a960c0a4823bbd36e7780","blob_size":1768}]'

```

## wojtasss | 2020-08-24T20:35:17+00:00
Ok, I just was wonderng if I don't need add more layers to my project (game engine Godot with GDscript language that supports websockets) but probably I will stay with just download current txpool from monerod :) anyway thanks!

## moneromooo-monero | 2020-08-25T11:30:46+00:00
--tx-notify tells you about txes in the pool (if they are for you).

## wojtasss | 2020-08-26T17:04:11+00:00
@moneromooo-monero yup I know that, but need notify when transaction arrived to txpool so want to get info about all transactions in txpool not only mine 

# Action History
- Created by: wojtasss | 2020-08-23T15:45:34+00:00
