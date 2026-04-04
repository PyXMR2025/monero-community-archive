---
title: 'monerod: "Error: Unsuccessful -- json_rpc_request:" when using print_coinbase_tx_sum. '
source_url: https://github.com/monero-project/monero/issues/7425
author: YonatanBL
assignees: []
labels: []
created_at: '2021-03-04T17:02:37+00:00'
updated_at: '2022-02-19T00:25:24+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:25:23+00:00'
---

# Original Description
About a minute after running 
`monerod print_coinbase_tx_sum 0 2309751 ` in my terminal I get `"Error: Unsuccessful -- json_rpc_request:"`.

Software: Ubuntu 20.04.2 LTS, running monerod 0.17.1.9-release.
Hardware: Intel i5-9500, 8GB DDR4 RAM, 250GB M.2 SSD.


# Discussion History
## moneromooo-monero | 2021-03-04T17:19:33+00:00
Run with --log-level 2, see if any interesting message pops out of monerod shortly before the end.

## YonatanBL | 2021-03-04T17:53:13+00:00
Output:
`2021-03-04 17:45:06.747 W SSL peer has not been verified
2021-03-04 17:45:06.748 W SSL peer has not been verified
2021-03-04 17:45:06.779 D SSL handshake success
2021-03-04 17:48:36.780 D Problems at read: Operation canceled
2021-03-04 17:48:36.780 E Unexpected recv fail
2021-03-04 17:48:36.780 I Failed to invoke http request to  /json_rpc
Error: Unsuccessful -- json_rpc_request:
2021-03-04 17:48:36.793 D Problems at cancel: Bad file descriptor
2021-03-04 17:48:36.793 D Problems at shutdown: Bad file descriptor`

## sethforprivacy | 2021-03-04T18:52:37+00:00
Tested on ThreadRipper 3950X, 32GB RAM, 1TB Intel 660p NVMe SSD with the following results:

* IO usage is ~80% of my NVMe drive while running, at ~25MB/s read
* CPU/RAM usage seem nominal

Error:

```
docker exec monerod monerod print_coinbase_tx_sum 0 2309751
2021-03-04 18:47:51.658 I Monero 'Oxygen Orion' (v0.17.1.9-release)
Error: Unsuccessful -- json_rpc_request: 
```

IO usage remains high after the command errors out.

Will re-test with log-level 2 later.

## moneromooo-monero | 2021-03-04T19:53:33+00:00
Ah, that must be just the RPC timing out because you're running it not from the console. Last I tried, it took an hour.

## ndorf | 2021-03-05T05:22:26+00:00
Aside from the client timing out, it seems the daemon itself will drop the connection after 20 minutes:

```
% time curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_coinbase_tx_sum","params":{"height":0,"count":2310084}}' -H 'Content-Type: application/json'
curl: (52) Empty reply from server
curl http://127.0.0.1:18081/json_rpc -d  -H 'Content-Type: application/json'  0.04s user 0.08s system 0% cpu 20:00.07 total
%
```

I/O and CPU usage stays elevated for some time afterwards.

## flolu | 2022-01-15T19:58:14+00:00
I'm also running into
```
Error: Unsuccessful -- json_rpc_request
```
What could be going wrong?

## selsta | 2022-02-19T00:25:23+00:00
This command has to be run from `monerod` console to avoid any timeouts.

# Action History
- Created by: YonatanBL | 2021-03-04T17:02:37+00:00
- Closed at: 2022-02-19T00:25:23+00:00
