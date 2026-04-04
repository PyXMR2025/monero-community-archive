---
title: 'Bug: Monerod crashes on Docker for no reason'
source_url: https://github.com/monero-project/monero/issues/9101
author: arhue
assignees: []
labels:
- bug
- reproduction needed
created_at: '2023-12-24T22:10:49+00:00'
updated_at: '2024-02-26T15:20:02+00:00'
type: issue
status: closed
closed_at: '2023-12-30T21:28:43+00:00'
---

# Original Description
Monerod crashes on Docker for no reason, with no warning and anything useful in logs. I am trying to host a public node on my Docker Swarm infrastructure.

Examples of log outputs:

```2023-12-24 03:13:36.400	I Synced 1224020/3046366 (40%, 1822346 left)
2023-12-24 03:13:36.402	I [batch] DB resize needed
2023-12-24 03:15:39.304	I LMDB Mapsize increased.  Old: 10613MiB, New: 12070MiB
2023-12-24 03:15:40.489	I Synced 1224120/3046366 (40%, 1822246 left, 8% of total synced, estimated 19.3 hours left)
2023-12-24 03:15:40.833	I Synced 1224220/3046366 (40%, 1822146 left)
2023-12-24 03:15:41.074	I Synced 1224320/3046366 (40%, 1822046 left)
2023-12-24 03:15:41.549	I Synced 1224420/3046366 (40%, 1821946 left)
2023-12-24 03:15:42.012	I Synced 1224520/3046366 (40%, 1821846 left)
2023-12-24 03:15:42.258	I Synced 1224620/3046366 (40%, 1821746 left)
2023-12-24 03:15:42.762	I Synced 1224720/3046366 (40%, 1821646 left)
2023-12-24 03:15:43.287	I Synced 1224820/3046366 (40%, 1821546 left)
2023-12-24 03:15:43.347	I Synced 1224840/3046366 (40%, 1821526 left)
2023-12-24 03:15:43.400	I Synced 1224860/3046366 (40%, 1821506 left)
2023-12-24 03:15:43.448	I Synced 1224880/3046366 (40%, 1821486 left)
2023-12-24 03:15:43.500	I Synced 1224900/3046366 (40%, 1821466 left)
2023-12-24 03:15:43.545	I Synced 1224920/3046366 (40%, 1821446 left)
2023-12-24 03:15:43.783	I Synced 1224940/3046366 (40%, 1821426 left)
2023-12-24 03:15:43.843	I Synced 1224960/3046366 (40%, 1821406 left)
2023-12-24 03:15:44.114	I p2p net loop stopped
2023-12-24 03:15:46.235	I Stopping core RPC server...
2023-12-24 03:15:46.309	I Stopping restricted RPC server...
2023-12-24 03:15:46.309	I Node stopped.
2023-12-24 03:15:46.409	I Deinitializing core RPC server...
2023-12-24 03:15:51.718	I Deinitializing restricted RPC server...
2023-12-24 03:15:51.982	I Deinitializing p2p...
2023-12-24 03:15:52.593	I Deinitializing core...
```

Then it starts again from 0. I've also seen something like this:

```
2023-12-24 21:26:20.599	I Synced 3014544/3046895 (98%, 32351 left, 63% of total synced, estimated 54.6 minutes left)
2023-12-24 21:26:24.455	I Synced 3014564/3046895 (98%, 32331 left)
2023-12-24 21:26:28.785	I Synced 3014584/3046895 (98%, 32311 left)
2023-12-24 21:26:30.740	I Synced 3014604/3046895 (98%, 32291 left)
2023-12-24 21:26:35.716	I Synced 3014624/3046895 (98%, 32271 left)
2023-12-24 21:26:38.341	I Synced 3014644/3046895 (98%, 32251 left)
2023-12-24 21:26:38.465	E Error in handle_invoke_map: boost::bad_get: failed value get using boost::get
```

I first thought it was something to do with gluster FS or one of Docker Swarm nodes. So I ran it on local disk and pinned to a particular VM. The VM has 2 cores on pretty unused 7700x VM and disk on 980 Pro NVMe SSD, with lots of capacity free. I also tried running it on a node with 8 GB RAM and almost all of 6 core CPU.

This is my Docker Compose file:

```
version: '3.3'

services:
  monerod:
    image: sethsimmons/simple-monerod:latest
    user: 0:0
    volumes:
      - /home/varun/monero/bitmonero:/home/monero/.bitmonero
    deploy:
      labels:
        homepage.group: Services
        homepage.name: Monero
        homepage.description: Monero Public Node
        homepage.icon: monero.png
        homepage.href: https://monero.ca.varunpriolkar.com
        homepage.server: docker
        homepage.statusStyle: dot
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.hostname == docker-4
    networks:
      - monero
    ports:
      - target: 18080
        published: 18080
        protocol: tcp
        mode: host
      - target: 18089
        published: 18089
        protocol: tcp
        mode: host
    expose:
      - "18080"
      - "18081"
      - "18089"
    command:
      - "--rpc-restricted-bind-ip=0.0.0.0"
      - "--rpc-restricted-bind-port=18089"
      - "--rpc-bind-ip=0.0.0.0"
      - "--confirm-external-bind"
      - "--public-node"
      - "--no-igd"
      - "--enable-dns-blocklist"
      - "--prune-blockchain"
  tor:
    image: goldy/tor-hidden-service:latest
    environment:
        MONEROD_TOR_SERVICE_HOSTS: 18089:monerod:18089
        MONEROD_TOR_SERVICE_VERSION: '3'
    volumes:
      - /mnt/vol1/monero/tor:/var/lib/tor/hidden_service/
    networks: 
      - monero
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.hostname != rpi
  gui:
    image: hvalev/monero-dashboard:latest
    networks:
      - monero
      - caddy
    environment:
      MONERO_HOST: monerod
      MONERO_PORT: 18081
      TICKER: "true"
      PORT: 3333
    deploy:
      mode: replicated
      replicas: 1
      labels:
        caddy: "monero.ca.varunpriolkar.com"
        caddy.reverse_proxy.to: "{{upstreams 3333}}"
        caddy.tls.dns: "route53"
        caddy.tls.dns.access_key_id: "{env.AWS_ACCESS_KEY}"
        caddy.tls.dns.secret_access_key: "{env.AWS_SECRET_KEY}"
 
networks:
  caddy:
    external: true
  monero:
    driver: overlay
    attachable: true
   ```

I first thought it could be something to do with the specific Docker image I am using, but I came across something similar: https://stackoverflow.com/questions/77603054/monero-daemon-in-docker-container-exits-for-no-reason

If you need any more information, let me know.

# Discussion History
## selsta | 2023-12-24T22:14:26+00:00
Can you increase the log level? Maybe it prints why monerod stops.

## arhue | 2023-12-24T22:47:39+00:00
@selsta Thanks for the prompt response. Running it with log level 1. It's hard to know where the logs are because they are in containers that exit and go away so I made it log to systemd journal in the absence of a good Docker logging solution.

```
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.295        I Transaction added to pool: txid <24caa8002250be735a05b4d9f541b0c47f9931eac58416f2930bc635d286d551> weight: 4811 fee/byte: 1.66286e+06, count: 2
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.296        I +++++ BLOCK SUCCESSFULLY ADDED
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.296        I id:        <9221aab8bfa969c9116cdb7ec0e31306f06178c1f0dcd8a4278b598bdb4926be>
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.296        I PoW:        <ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff>
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.296        I HEIGHT 178984, difficulty:        1192258429
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.296        I block reward: 14.883554550025(14.865554550025 + 0.018000000000), coinbase_weight: 249, cumulative weight: 9036, 0(0/0)ms
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.296        I Transaction added to pool: txid <fb4752b0b652e5434489915a3640bb9f36d8575a69e1a88dc61cef36f28a3b36> weight: 1689 fee/byte: 5.92066e+06, count: 1
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.296        I Transaction added to pool: txid <9099715cd7dc61208a7c95189c0d5f3ec1946a6fe5e99e2488328ed06a749ea0> weight: 2200 fee/byte: 3.58258e+06, count: 2
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.297        I +++++ BLOCK SUCCESSFULLY ADDED
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.297        I id:        <2a1bdacbb4df45000a9d9e678869383b510244c8686b3d86f76f0b4c7052aaf6>
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.297        I PoW:        <ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff>
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.297        I HEIGHT 178985, difficulty:        1194901506
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.297        I block reward: 14.883422038805(14.865540373127 + 0.017881665678), coinbase_weight: 249, cumulative weight: 4138, 0(0/0)ms
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I +++++ BLOCK SUCCESSFULLY ADDED
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I id:        <91798433ee64cf3c9cde15b788c939c0794d7856e9a41c061c9ada324929dc2d>
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I PoW:        <ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff>
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I HEIGHT 178986, difficulty:        1189731679
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I block reward: 14.865526196243(14.865526196243 + 0.000000000000), coinbase_weight: 287, cumulative weight: 287, 0(0/0)ms
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I Transaction added to pool: txid <6e864d7187597c263ee13006ae75ed0699ab4b59619afd16fcea9b558dd6e451> weight: 905 fee/byte: 5.81593e+06, count: 1
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I Transaction added to pool: txid <9fba7cccf583d83f158a7493b6c5aff79f534a578814cee73c8b8624a9c5f5ad> weight: 864 fee/byte: 9.33926e+06, count: 2
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I Transaction added to pool: txid <b61a5e00cb1ee6bef0bcae15b6250dcd2e74bf04dcfe73bfc62ce9eb0e44150a> weight: 1947 fee/byte: 4.7051e+06, count: 3
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I Transaction added to pool: txid <6bcb8f2faf0a959c40e99b12f4aaa71ef0a568175903dea673f6bf0ab4755362> weight: 3170 fee/byte: 2.7335e+06, count: 4
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I Transaction added to pool: txid <9442872647983b07781f241eebf4fdd7e43166a47b338d1ac5c4b3a6bfecf3a1> weight: 456 fee/byte: 1.09649e+07, count: 5
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I Transaction added to pool: txid <f0acbec71874ca551cffce18c2c8074d4b100413c1325885de3ca93c0a184fcf> weight: 1026 fee/byte: 1.8046e+07, count: 6
Dec 24 22:42:17 docker-4 3026041b80e6[768]: 2023-12-24 22:42:17.298        I Transaction added to pool: txid <ca5c8fdc395133736b1bcafd93edde57379fa15b3b270779447ce5e48b85e5e1> weight: 832 fee/byte: 1.20192e+07, count: 7
```

Looks like it's at 11% now. It's a lot of logs that it's generating. Need to scroll up few pages for every 1/10th of second of log. 

## selsta | 2023-12-25T00:32:10+00:00
There is no crash visible in your logs, it seems monerod gets an external exit signal and correctly stops. Now why it gets the exit signal, I'm not sure. I'm not familiar enough with Docker to debug this.

## arhue | 2023-12-25T00:34:44+00:00
Yea, it hasn't crashed yet. Apologies if I wasn't clear enough. It was just a sample of the normal journalctl log. Currently at 54%. I'm keeping an eye on it.

## arhue | 2023-12-25T07:33:36+00:00
Ok, it happened again. I couldn't find a good place to upload the debug log so I just created a public repo on Github with the content.

https://github.com/arhue/monerod-debug

Both are text files. 10 minute file should be enough but I also provided the 30 minute file just incase. These logs should also have the docker daemon log, along with the container log incase you need either of them. The timestamp where it restarted should be around Dec 25 02:10:13 docker-4 3026041b80e6[768]: 2023-12-25 07:10:13.959. 02:10 is local time, 07:10 is the UTC time.

```
Dec 25 02:10:02 docker-4 3026041b80e6[768]: 2023-12-25 07:10:02.522        I Synced 3040382/3047197 (99%, 6815 left) (5.069976 sec, 3.944792 blocks/sec), 548.906616 MB queued in 239 spans, stripe 7 -> 7
Dec 25 02:10:08 docker-4 3026041b80e6[768]: 2023-12-25 07:10:08.874        I Synced 3040402/3047197 (99%, 6795 left) (6.325051 sec, 3.162030 blocks/sec), 547.269165 MB queued in 238 spans, stripe 7 -> 7
Dec 25 02:10:13 docker-4 3026041b80e6[768]: 2023-12-25 07:10:13.959        I Synced 3040422/3047197 (99%, 6775 left) (5.066600 sec, 3.947420 blocks/sec), 545.507080 MB queued in 237 spans, stripe 7 -> 7
Dec 25 02:10:33 docker-4 a36a629e7a87[768]: 2023-12-25 07:10:33.574        I Synced 101/3047198 (0%, 3047097 left) (0.015882 sec, 6296.436217 blocks/sec), 0.000000 MB queued in 0 spans, stripe 1 -> 1
Dec 25 02:10:33 docker-4 a36a629e7a87[768]: 2023-12-25 07:10:33.701        I Synced 201/3047198 (0%, 3046997 left) (0.012266 sec, 8152.616990 blocks/sec), 0.000000 MB queued in 0 spans, stripe 1 -> 1
```

Problematic part of log?

```
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.369        I block reward: 0.600089460000(0.600000000000 + 0.000089460000), coinbase_weight: 106, cumulative weight: 4579, 4(0/4)ms
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.378        I [94.75.232.164:44910 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.378        I [82.66.187.193:48070 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.378        I [97.148.142.44:63509 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.378        I [76.132.108.9:22108 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [24.145.120.167:65186 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [45.83.5.80:32968 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [80.219.65.129:12286 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [82.66.187.193:48070 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [94.130.9.215:18080 OUT] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [80.219.65.129:12286 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [185.159.157.9:45352 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [97.148.142.44:63509 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [93.227.184.108:39668 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [198.251.87.50:39054 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [24.145.120.167:65186 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [34.124.182.107:49904 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [76.132.108.9:22108 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [95.84.137.181:34996 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [94.75.232.164:44910 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [172.59.124.209:25350 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [34.124.182.107:49904 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [27.32.37.206:18080 OUT] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [94.130.9.215:18080 OUT] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [172.59.124.209:25350 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [98.116.240.168:47380 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [139.99.123.196:18080 OUT] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [98.116.240.168:47380 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [35.229.149.89:52800 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [31.15.171.128:38822 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [95.84.137.181:34996 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [51.195.62.81:62408 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [93.227.184.108:39668 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [95.211.199.137:51064 INC] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [31.15.171.128:38822 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [92.206.32.47:18080 OUT] Failed to lock m_sync_lock, going back to download
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [198.251.87.50:39054 INC] [182] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [45.83.5.80:32968 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [92.206.32.47:18080 OUT] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [51.195.62.81:62408 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.379        I [185.159.157.9:45352 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.380        I [95.211.199.137:51064 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.380        I [27.32.37.206:18080 OUT] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.380        I [139.99.123.196:18080 OUT] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.380        I [35.229.149.89:52800 INC] [0] state: pausing in state standby
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.385        I Transaction added to pool: txid <ce996c37a60ec22c3bd68aab010c7012f7887ce63d2f8a13a69a786603000eb3> weight: 1532 fee/byte: 80000, count: 1
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.389        I Transaction added to pool: txid <70efe85c2bd44259817c5b115a871cead432fc79bb0eed4115b1ce9533b5e086> weight: 1525 fee/byte: 20039.3, count: 2
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.393        I Transaction added to pool: txid <07025905090cedd88c160fe6dcc5ca1d77cb060c3ceafde7a808d3b7135e9c4d> weight: 1528 fee/byte: 20000, count: 3
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.398        I Transaction added to pool: txid <2737a9971782d7dde8bc13f4b4a56d1c3d1aa1fc80f46e42dd261e90df7cf91d> weight: 1534 fee/byte: 20000, count: 4
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.405        I Transaction added to pool: txid <7e3e266c909d4269518f3f69489e3bc20769977675dd6648c6a28bdf4f11383f> weight: 2218 fee/byte: 20000, count: 5
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.408        I Transaction added to pool: txid <063c0309f6695b759dfffd2eaabb9b6a3d4a65d33a671309fef339009a3499c5> weight: 1535 fee/byte: 20000, count: 6
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.413        I Transaction added to pool: txid <e4f5505e50a98aab91c5f1a427e3f83d133d3bf0b32a643d71bfc14fcf30a224> weight: 2221 fee/byte: 20000, count: 7
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.416        I Transaction added to pool: txid <9e56bdc139ccfcdbb564e32df3537e6135b2996a0186272f20c948d58dec2b53> weight: 1529 fee/byte: 20000, count: 8
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.419        I Transaction added to pool: txid <6de6bf2151734b9545f9090fbf1a797293e19fe14c6a11db50cebf71101e3e5a> weight: 1535 fee/byte: 20000, count: 9
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.424        I Transaction added to pool: txid <0937ca695b48d1f5eea5a5a990a0b1b1e360ea5c10a7efa997d5050e5a01f13a> weight: 1530 fee/byte: 20000, count: 10
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.426        I +++++ BLOCK SUCCESSFULLY ADDED
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.426        I id:        <acaab98cc87aac4cd91d5cbf80a4f0a0cea04a675587b9115c02cabe63fa9a03>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.426        I PoW:        <f3f83c7d13972605af13b103c011625dc62dcde8e2c4a4f6d454370100000000>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.426        I HEIGHT 3040430, difficulty:        271836128286
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.426        I block reward: 0.600425720000(0.600000000000 + 0.000425720000), coinbase_weight: 97, cumulative weight: 16784, 4(0/4)ms
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.447        I Transaction added to pool: txid <b09dfc5e207db46e9a22f4f23084195b9c6c5ff7097c94fd738c93921b07797d> weight: 1534 fee/byte: 516949, count: 1
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.450        I [82.66.187.193:48070 INC] 5835 bytes received for category command-2002 initiated by peer
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.450        I [82.66.187.193:48070 INC] Received NOTIFY_NEW_TRANSACTIONS (2 txes)
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.450        I Including transaction <701c4df16d715698e28e5b925b13374d0e3bdfeff8f988bc879d1cfd8fadc564>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.450        I Including transaction <1837605897cee22a1f8c06d7cce5bace6e2755fe94cd1d3365074ebd8e3200d7>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.453        I Transaction added to pool: txid <db3c47c9fa7c147be8aed6869d6839044c8a798fb5fad897e27b501297517ef3> weight: 2219 fee/byte: 320000, count: 2
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.456        I Transaction added to pool: txid <907479be3eb9504ce28b930897f718eeea1d8e1ccc1e3be7917c89d45725e404> weight: 2218 fee/byte: 80000, count: 3
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.460        I Transaction added to pool: txid <0a92be7cdb42c0ca26c0bf6d8a8517fdf9d4cc5b1427189c378cf27c5ec2e9d6> weight: 1530 fee/byte: 80000, count: 4
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.463        I Transaction added to pool: txid <62f76948e4eec05b37f383aff2870e284d23d69fb9aebc339c0796d4459e5b28> weight: 1526 fee/byte: 20026.2, count: 5
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.467        I Transaction added to pool: txid <f58eed0593abd75d97afc186aba3bd403b9401a79b431479efb6330cfca127a1> weight: 3592 fee/byte: 20000, count: 6
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.470        I Transaction added to pool: txid <1cd56c49692aab044862b30398db4d60323dcc5bad81ca981b7913ea2a56f842> weight: 2215 fee/byte: 20000, count: 7
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.474        I Transaction added to pool: txid <5f66891a666fc228693e00065df691f058703847f1c11db88300c2a8970a5dae> weight: 1534 fee/byte: 20000, count: 8
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.477        I Transaction added to pool: txid <0121acd8864677f49c98c549dbd77a9cd027190bfbee4542206fedf691af44bb> weight: 2222 fee/byte: 20000, count: 9
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.480        I Transaction added to pool: txid <6fd82c0e42dc37f181aa045117de42568df707241e3f1fa0c73358db69ba88f1> weight: 1530 fee/byte: 20000, count: 10
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.484        I Transaction added to pool: txid <98de0bf16abeb3981581736d4f5aeba70628982989a432aad85b906d80e90cbe> weight: 1536 fee/byte: 20000, count: 11
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.485        I +++++ BLOCK SUCCESSFULLY ADDED
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.485        I id:        <53cb782524eed039cd3abd224c8c7691a8f5e2c3e89db89fa37437e42438b1e8>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.485        I PoW:        <b15425b5be94ce6e706323304c6e5e73d9bfdbcd7cb63c92fab1360300000000>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.485        I HEIGHT 3040431, difficulty:        271288341237
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.485        I block reward: 0.602086060000(0.600000000000 + 0.002086060000), coinbase_weight: 97, cumulative weight: 21753, 5(1/4)ms
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.498        I [31.15.171.128:38822 INC] 3620 bytes received for category command-2002 initiated by peer
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.498        I [31.15.171.128:38822 INC] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.498        I Including transaction <1837605897cee22a1f8c06d7cce5bace6e2755fe94cd1d3365074ebd8e3200d7>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.546        I Transaction added to pool: txid <41efb121657f7a21d29a634d4227e8fbe4ab2619e326129f4ef358d122ee7e69> weight: 1536 fee/byte: 516276, count: 1
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.550        I Transaction added to pool: txid <69b3cc4fe2b8fb3e28b5fee23599d5ca9ea19d0b38bc6b4c0cedc6c177a8be8d> weight: 2223 fee/byte: 320000, count: 2
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.553        I Transaction added to pool: txid <5aefdfdb777d01dac7146b2509bf834e4347063f8ebb09b8ea2cb8e2408bf909> weight: 2215 fee/byte: 320000, count: 3
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.557        I Transaction added to pool: txid <dd82af78d7a25078678714cc2ff879c405678e6c3f289f3d9ac56be90b4caf51> weight: 2224 fee/byte: 320000, count: 4
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.560        I Transaction added to pool: txid <7bceae27fa5686c01d000408e836bfc4c94fab60e85cf3e0da85edb45b161d03> weight: 1533 fee/byte: 156947, count: 5
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.564        I Transaction added to pool: txid <030b6ee8fafab47ce3ab8b0795f2248f1a6b9e85a26b73275612d9658406e726> weight: 2204 fee/byte: 80072.6, count: 6
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.567        I Transaction added to pool: txid <9b02b513455e7db1fc00cc64f86208325ea4cfed8b201bfa9a8a2aa970938e2a> weight: 1534 fee/byte: 80000, count: 7
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.571        I Transaction added to pool: txid <70cc62f6464697777fbcfd3eacc6dad33d876185f3fc760223f7aa4c78a848e7> weight: 2215 fee/byte: 80000, count: 8
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.574        I Transaction added to pool: txid <d5b62c60078eb6b955d876fc330d95be6b707b79892afbd9568b09f53af063c6> weight: 2214 fee/byte: 80000, count: 9
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.577        I Transaction added to pool: txid <c5faa9e0f02703e4d2d167127b8e7b76e87955c770782c2e0d6f87be468e03d5> weight: 2221 fee/byte: 80000, count: 10
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.581        I Transaction added to pool: txid <6bea097c40b8645d09ed9b7becc04e97075eb34117dbb17823e779e83d53aea6> weight: 1535 fee/byte: 80000, count: 11
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.584        I Transaction added to pool: txid <742e4556dc0c1594f1f5362be14cd696f31006edaa94913062a8e6409bcdd53a> weight: 1535 fee/byte: 80000, count: 12
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.587        I Transaction added to pool: txid <9a853509664a2cb5fc5a33a102755d2853e7783f934853262b16e199cb57b8ca> weight: 1532 fee/byte: 80000, count: 13
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.591        I Transaction added to pool: txid <9abc3dd7e0b137be875bd860c844ace991792938ffc0a7dd10d569be9818c1d4> weight: 2214 fee/byte: 80000, count: 14
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.594        I Transaction added to pool: txid <582916ddb5e2548f08d7273bf13caae5ea79efe1d030d818206c2bc016adbb43> weight: 2224 fee/byte: 80000, count: 15
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.598        I Transaction added to pool: txid <3b75161f80cec17baf4ff7bfe249c552043a0822214a8769c077174d3fa6a272> weight: 1534 fee/byte: 20678, count: 16
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.601        I Transaction added to pool: txid <e2987b32b5bd12ba57c7443c6f9c1d202546e091c918a83e9c1b5b07da60502a> weight: 1536 fee/byte: 20039.1, count: 17
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.604        I Transaction added to pool: txid <e762a04a2a89a8fe0aaf8483b28429879b47007e5e14bb360971a81a98f56fa1> weight: 1533 fee/byte: 20013, count: 18
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.608        I Transaction added to pool: txid <f8e46fca4ee344ee3b18d2026c7699c2c037c66dafc833fac7d54601723b2fb5> weight: 2212 fee/byte: 20000, count: 19
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.611        I Transaction added to pool: txid <c8ea054824d247bceeff654127e73be0981e3bdfc060fc4af894a98d084b8648> weight: 1534 fee/byte: 20000, count: 20
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.614        I Transaction added to pool: txid <6aabee2433351b4d154d9007a773c0578554fce81be548e825ea0d313718be41> weight: 1531 fee/byte: 20000, count: 21
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.618        I Transaction added to pool: txid <22badf40b6a73c8eacc92f208f68dadd71a03494d2581fc95940268f626cfb5d> weight: 1536 fee/byte: 20000, count: 22
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.621        I Transaction added to pool: txid <3f7a3235735cf90e51b8858926a44a99cd3f44a8ce50253db983b520a8dc1b4a> weight: 2224 fee/byte: 20000, count: 23
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.624        I Transaction added to pool: txid <611fce3ab9d1251ae3e64f8b77efe16951d8c92733d795fb0fded4f3840df44e> weight: 1532 fee/byte: 20000, count: 24
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.628        I Transaction added to pool: txid <c40ffe0b22a8b78e907af7e100469aadcd5d742968f24ca08a61c377f4f6665f> weight: 1531 fee/byte: 20000, count: 25
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.631        I Transaction added to pool: txid <5324a413fe7559b15762bf420b17024c5621d3c1cc0ca13fe2ff4a900bed5685> weight: 7400 fee/byte: 20000, count: 26
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.635        I Transaction added to pool: txid <a69467ace3c9349710b8657dcc315d4252ae103dc594c907e0f62229a9f273ea> weight: 1531 fee/byte: 20000, count: 27
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.638        I Transaction added to pool: txid <2dbc35af8e5ae30f8a44dc65db6e2c9446b9b90bfe6f038da8f16aca65e40c99> weight: 1535 fee/byte: 20000, count: 28
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.641        I Transaction added to pool: txid <31c305064134687a53157b8f8339ec76b5adeb052324c3c4e6e7dec8fbfe4845> weight: 1534 fee/byte: 20000, count: 29
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.645        I Transaction added to pool: txid <4b916dda6029676fcc93523e99efbf79d0ab3db0de1776681e7171641f1e0dea> weight: 1529 fee/byte: 20000, count: 30
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.648        I Transaction added to pool: txid <759590ebf6c55acbaef0c913091f1157caff98141fddc32c3146eec3226ebffa> weight: 2221 fee/byte: 20000, count: 31
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.652        I Transaction added to pool: txid <1461bcf6e425cd51d994b120c66dd14818206c08677ff2962c6323011c178748> weight: 1534 fee/byte: 20000, count: 32
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.655        I Transaction added to pool: txid <81b66a3b710b86f65ace2ede095b39bf2ff9eec0a0c186a2933ce0185d8f5d25> weight: 1535 fee/byte: 20000, count: 33
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.659        I Transaction added to pool: txid <2bb30c7e3b9737c24a64ea9da96b3fd289c406a5ccedce83beedf9edfbe10af8> weight: 2220 fee/byte: 20000, count: 34
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.662        I Transaction added to pool: txid <a84e93d4d7a325bc270fe126a953e98942eab8670bfdd9a9bc227edd8f4fe820> weight: 2799 fee/byte: 20000, count: 35
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.666        I Transaction added to pool: txid <1469bff637bdf91ca9aa64165eea85e3e893a708e0d9f1c5a0093c1700648740> weight: 2223 fee/byte: 20000, count: 36
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.670        I Transaction added to pool: txid <65a426dd4167e39f9f962efea62bbdbdbdce634ef8a46b1105e4b225c11ea39d> weight: 4167 fee/byte: 20000, count: 37
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.673        I Transaction added to pool: txid <388777b951b6fe60952949212eed55e557f5199f05e0968d715ac6de622571f1> weight: 1531 fee/byte: 20000, count: 38
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.676        I Transaction added to pool: txid <8f96ee7b5ce7f1ca013786969ab777c84b9b454e527922eb50451552c7b37270> weight: 1532 fee/byte: 20000, count: 39
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.680        I Transaction added to pool: txid <63eec5fd9992be2037a9339df5cedb39fcabf3fb748edcc96fdb254000abf188> weight: 1530 fee/byte: 20000, count: 40
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.683        I Transaction added to pool: txid <9658297532728112bcdf643cb345e68b30a471e50e0aa9c868787635194036c5> weight: 1532 fee/byte: 20000, count: 41
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.687        I Transaction added to pool: txid <add45f8c18b50fd013540047b852913b6586459739dfc2d4730ec7fb74a7483e> weight: 2219 fee/byte: 20000, count: 42
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.689        I +++++ BLOCK SUCCESSFULLY ADDED
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.689        I id:        <af69b3b7c4182cd00bdffbf851bd64cdbaee815f01acfd502deaff3c2ca27a9f>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.689        I PoW:        <586acd4f73f01281f3d3c8e7589064cbadc14aa5eb52f38b67449d0300000000>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.689        I HEIGHT 3040432, difficulty:        271535419204
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.689        I block reward: 0.605826460000(0.600000000000 + 0.005826460000), coinbase_weight: 106, cumulative weight: 84540, 6(0/4)ms
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.790        I [172.59.124.209:25350 INC] 3620 bytes received for category command-2002 initiated by peer
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.790        I [172.59.124.209:25350 INC] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.790        I Including transaction <1837605897cee22a1f8c06d7cce5bace6e2755fe94cd1d3365074ebd8e3200d7>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.831        I Transaction added to pool: txid <5579c8037e26f290b21ab8566f7d33c7cb78cb3cc74cb38f65be437f0ffa05e7> weight: 1535 fee/byte: 2.06645e+07, count: 1
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.834        I Transaction added to pool: txid <c2526f17b363ea139f0794e93f31523c462dacf904b80228db1f8c4d762fb99c> weight: 1538 fee/byte: 2.06242e+07, count: 2
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.838        I Transaction added to pool: txid <49bf3e81e06baf0aae9d1f2d02297a48032baa99bcbaf62be6a23231511d0bbf> weight: 1530 fee/byte: 4e+06, count: 3
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.843        I Transaction added to pool: txid <87a58463f305ec72ba2b8876bd2314c0c81f60ad91ec5d7bf74b3a53770165eb> weight: 2212 fee/byte: 320000, count: 4
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.846        I Transaction added to pool: txid <fe02c23a7f163b60a084012ebc87be5f7e6972e08e72f85df21ba383c02b1200> weight: 1535 fee/byte: 320000, count: 5
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.850        I Transaction added to pool: txid <3962dee743136a8d5ab266f5306b317db2e5b961d373ff5dc49e0fa881309b3b> weight: 2222 fee/byte: 320000, count: 6
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.853        I Transaction added to pool: txid <958eff54937cefe71bd2981d23928d1098e20ec13803082cb22167bb7b7bcaf1> weight: 2213 fee/byte: 320000, count: 7
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.856        I Transaction added to pool: txid <73f7de307c31efd93ed0b7cb916fa6cd24bdaad25519089c12ba6e25a7f6ae61> weight: 1533 fee/byte: 320000, count: 8
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.860        I Transaction added to pool: txid <9e0d54b7e9735986b0f89db99c8f0410e0e524b216638a4a9c5afb7b74844423> weight: 2218 fee/byte: 320000, count: 9
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.863        I [93.227.184.108:39668 INC] 3620 bytes received for category command-2002 initiated by peer
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.863        I [93.227.184.108:39668 INC] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.864        I Including transaction <1837605897cee22a1f8c06d7cce5bace6e2755fe94cd1d3365074ebd8e3200d7>
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.864        I Transaction added to pool: txid <71a702b6f3345d0ce1c12d3aa112946c31f6959ee50101d2bd9a22dcc890b3fc> weight: 2221 fee/byte: 320000, count: 10
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.867        I Transaction added to pool: txid <e1789cd503bb8a007fe18d1e728ff81e5908f1f8012f012dad96fcbf0fca8c0d> weight: 1538 fee/byte: 320000, count: 11
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.871        I Transaction added to pool: txid <4a91822f1a94776481ebcabb326571cd8f3e71dbb5a15d8484c2d0dee2d3f62c> weight: 2217 fee/byte: 320000, count: 12
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.874        I Transaction added to pool: txid <3558390ad4224f5ea912b931670c6a2994ea5919491d888390e1300357deb248> weight: 2219 fee/byte: 320000, count: 13
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.878        I Transaction added to pool: txid <a482a3cfa4225b8c187a4e20500d2e31f0cfed4952288b0dbd6c28030ee6a043> weight: 2219 fee/byte: 320000, count: 14
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.881        I Transaction added to pool: txid <e770104d34200645a956843a81f41b0b2a0ceba2acd0a41078edac32dbbbdafc> weight: 1520 fee/byte: 111928, count: 15
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.885        I Transaction added to pool: txid <6c134c99bbb82f15cc112c185f258dcb1faedb3a084d18caeee1e8800784401b> weight: 1530 fee/byte: 104837, count: 16
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.888        I Transaction added to pool: txid <1e7961b496c76deaa5967a802371659ca12a5858e5ceef4966f696e9e09d220d> weight: 1531 fee/byte: 103592, count: 17
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.892        I Transaction added to pool: txid <1078019d799c43c9d303a94845dad92016a2aeb9375e404cdbef710c18dc4399> weight: 1535 fee/byte: 103322, count: 18
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.895        I Transaction added to pool: txid <4178b948d72d2aae4be24334930e2f45c774af560ce257463a8198d586f5084a> weight: 1536 fee/byte: 103255, count: 19
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.898        I Transaction added to pool: txid <220ee3b91e5977256c01c5e8396b59ab710eac4736f5e44ac12545bcb7bacd79> weight: 1533 fee/byte: 80000, count: 20
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.902        I Transaction added to pool: txid <5b6e089717c0621304d112d3fb4bfe95b92cbff1ae2d3842ef29f2aa5a3b8ce8> weight: 2903 fee/byte: 80000, count: 21
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.906        I Transaction added to pool: txid <cde23109353cf467d1148591f93484ec39db1f53815376ff4190eaa6b06d36cf> weight: 1529 fee/byte: 80000, count: 22
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.909        I Transaction added to pool: txid <c707522b00028685d079bf82232b866a798d3b7cc338f0c581502a5f3a5425a0> weight: 1537 fee/byte: 80000, count: 23
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.912        I Transaction added to pool: txid <3f904e984e5b0b783c3faee0b71c5bae2c7aa1b20fc34e29962409828bcd4cb9> weight: 1535 fee/byte: 80000, count: 24
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.916        I Transaction added to pool: txid <0dc91ed6a7f94b13172d6fd6f4d84cec2a1fcc3f1a450537033eb26aed0f62c8> weight: 1539 fee/byte: 30916.2, count: 25
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.919        I Transaction added to pool: txid <c3c1bb07ff2ce8703a5f1914982dde6decf8b81ec458277cb16c223a694216bd> weight: 1532 fee/byte: 20705, count: 26
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.922        I Transaction added to pool: txid <00a9624e3ac7d99c2d2cbec414679cd5ecaaa6a576c56e85d510de190fe9ec1f> weight: 1534 fee/byte: 20678, count: 27
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.926        I Transaction added to pool: txid <276fdaa958121d97b2f4063d826d226735e1f30bc45d2e2677285a64e7ef61b8> weight: 1536 fee/byte: 20651, count: 28
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.933        I Transaction added to pool: txid <1ca23257b13ffaccb8285478fea8bb8da17ba5c894f9bf935bf08aecf3cd15d9> weight: 3593 fee/byte: 20167, count: 29
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.936        I Transaction added to pool: txid <4d313da601a8c9d27b9ed9b500c835e4b9c8afc432dbe1b71d5d4e1bd0bf4248> weight: 1529 fee/byte: 20078.5, count: 30
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.939        I Transaction added to pool: txid <95b55fc96d4a1f53d49881978b75d1e0e621eceac30f29f2d63c2e63c4aeaf37> weight: 1531 fee/byte: 20065.3, count: 31
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.943        I Transaction added to pool: txid <9b2c3349c44aff4289f9055bf5bf37c5dbbb87254a14c8fc68b1ff1549b4ae4f> weight: 3591 fee/byte: 20055.7, count: 32
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.946        I Transaction added to pool: txid <856a03430213ca0d3783e89e9b32d701e243779a69b1f735e47d4d7624a871df> weight: 1524 fee/byte: 20026.2, count: 33
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.950        I Transaction added to pool: txid <22a4e7ed9c6d4e85c1a9b898c6910f8f7fd46033acabfef6fcd5270894ea7110> weight: 1530 fee/byte: 20013.1, count: 34
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.953        I Transaction added to pool: txid <85869e9b063db5e66c9b0dc9026ffb00778dd8f6a4d7ae5b23d91baef4d59c46> weight: 2225 fee/byte: 20000, count: 35
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.957        I Transaction added to pool: txid <01cd4d42dbb7e3c316e99f4b70e07df58e6abd0a257cbee168dbdeb4244855ad> weight: 2212 fee/byte: 20000, count: 36
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.960        I Transaction added to pool: txid <2535dea39ba15ab71b6f8e1d30e7f3e905dd926de826c8ecc1baf098bbdab726> weight: 2221 fee/byte: 20000, count: 37
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.964        I Transaction added to pool: txid <fa69010ca559d95643913c692b430476dd645bed1fa4059458b763b45cd84a73> weight: 2219 fee/byte: 20000, count: 38
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.967        I Transaction added to pool: txid <5b5e70bd142ade3ab98996dd3cd55bec13cc0143875476e4568875dd208b7e9b> weight: 2220 fee/byte: 20000, count: 39
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.989        I Transaction added to pool: txid <e1abe466fe076ed87bb172685ff0752b2c38ddde2a15c38562417cf9bdad92e3> weight: 15952 fee/byte: 20000, count: 40
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.993        I Transaction added to pool: txid <326b71dd326ccb2c4d2ec5cce231fceef929d1eae140d48c92347599ee1dc56e> weight: 2216 fee/byte: 20000, count: 41
Dec 25 02:10:15 docker-4 3026041b80e6[768]: 2023-12-25 07:10:15.996        I Transaction added to pool: txid <57795ea5e98efefe1bd08cc4a76cc8d6142d37f4bcfd2dbe3f307389f3b2020a> weight: 2216 fee/byte: 20000, count: 42
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.000        I Transaction added to pool: txid <ab173cc24be777034b395246885e62d6e2eba0d3f4d9097997daa1386510cda5> weight: 2221 fee/byte: 20000, count: 43
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.003        I Transaction added to pool: txid <994cd60fd97db7767ff051fd9329bd23c60e4dbbded736780874179561aa4343> weight: 2222 fee/byte: 20000, count: 44
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.007        I Transaction added to pool: txid <0a051bc2fced2a389054951888029eb6fd97f13bfd740aed95cb0f299c2de581> weight: 1535 fee/byte: 20000, count: 45
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.021        I Transaction added to pool: txid <21cf0bce457d27cdcfd2ff3675d020ac9c8d280d61ffdd9ead4adb5211456119> weight: 15100 fee/byte: 20000, count: 46
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.025        I Transaction added to pool: txid <ce304b73587e91f9a3e01b5ba9061cebc33c08ed9ce7a9ada8ae4fc742a5a8ab> weight: 1533 fee/byte: 20000, count: 47
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.028        I Transaction added to pool: txid <23100411ff9125117b13cad13ca9034c9a2a82dadca21b8d67fec25307beec46> weight: 1537 fee/byte: 20000, count: 48
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.031        I Transaction added to pool: txid <6c875ba964a985e45d8a06d29bd7b54071c657e7a3d8b41187d66bc43a2253dc> weight: 1533 fee/byte: 20000, count: 49
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.035        I Transaction added to pool: txid <5ebe83b690302f84dfe8eae9f50549d7e7e1a4522bcdfb5435cb389242423b51> weight: 1530 fee/byte: 20000, count: 50
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.038        I Transaction added to pool: txid <74bad28704b70dc03b02512024b5efc4dff347a08b3b1c215d96b1a703edda23> weight: 1536 fee/byte: 20000, count: 51
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.041        I Transaction added to pool: txid <d7573679c5f82a1d410a612cadcfcf1a67758b7e047eb4e3533bf180806819d6> weight: 1531 fee/byte: 20000, count: 52
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.045        I Transaction added to pool: txid <df7271326e0c8912159fbd0dcaa879cfd72ba1ca9b56f5a46993ea0fe4f9e771> weight: 1535 fee/byte: 20000, count: 53
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.048        I Transaction added to pool: txid <99a852747520ffbf56208d01a723cc528330b72576345b803931a3df506ff0b6> weight: 1534 fee/byte: 20000, count: 54
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.051        I Transaction added to pool: txid <7e138184f398697e4adc3c089fc5c7f4d3ea370b5a404df0d5f9faab3c515306> weight: 1534 fee/byte: 20000, count: 55
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.054        I Transaction added to pool: txid <a10e0e25983405d466c7af754ac5d1627ea5d48b2fd51671719fb1650b5574b3> weight: 2224 fee/byte: 20000, count: 56
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.058        I Transaction added to pool: txid <5f909c15a58577e6d9ef9f66e2c815c218d85ab66af2c0683e82f59599d8f4bc> weight: 1530 fee/byte: 20000, count: 57
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.061        I Transaction added to pool: txid <5a5d850eed08aed42acf6481571c0c07ec6666f30530a31db5749c3d0a22cc4f> weight: 1534 fee/byte: 20000, count: 58
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.065        I Transaction added to pool: txid <b6d387bd93b76f8653808a7459a1902afa347d9d8fb036603d82f2d8d012cc4d> weight: 2906 fee/byte: 20000, count: 59
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.068        I Transaction added to pool: txid <e7611dcad1e2255dc452a15186dd61192a40c0dce5a5a57f003a0b9c2f40e961> weight: 1533 fee/byte: 20000, count: 60
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.071        I Transaction added to pool: txid <5fef7141c7e55e22edc0d2f57192f9e6703758cda233132ef13eb69ff5f51e14> weight: 1528 fee/byte: 20000, count: 61
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.075        I Transaction added to pool: txid <e34043ca34886c8b3c80c6f603d298615c45d02164a7ec29b38d5f1ed8b27bc6> weight: 2220 fee/byte: 20000, count: 62
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.078        I Transaction added to pool: txid <9822cf0903e11ea3b047e168c2646d1d5b1e371554d576bb2245b4a74f47a5ea> weight: 2220 fee/byte: 20000, count: 63
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.082        I Transaction added to pool: txid <65fe4b091ea51f2a6625c4126e2d482f454e89cb386c1767619da85a8f3d8a08> weight: 1531 fee/byte: 20000, count: 64
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.085        I Transaction added to pool: txid <1607cc0030bb25d306860506c91d881b32c4e8bd3f3d000ea805d73cb237ca29> weight: 1535 fee/byte: 20000, count: 65
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.089        I Transaction added to pool: txid <1102fadd508d2fc37dae303ef5a28ab36787683c6c6219235f8de3899c04535a> weight: 2218 fee/byte: 20000, count: 66
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.092        I Transaction added to pool: txid <892300c7746a67e48d790993446e5a8c1f583765dfbc53309addebda1f45205c> weight: 1533 fee/byte: 20000, count: 67
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.095        I Transaction added to pool: txid <08444c612713796cb2e233c0cd550eda151127dd4f43a5db0dcd637490034b75> weight: 1530 fee/byte: 20000, count: 68
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.099        I Transaction added to pool: txid <3d196149c317f07feffe8784219904e20d3e70a9917f9e59ce4e662a8182a681> weight: 1531 fee/byte: 20000, count: 69
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.105        I Transaction added to pool: txid <88162aabf7afd8bb2f2d46688c7d1aa53b318fb5d0ddf254a324ce7f1a998227> weight: 2217 fee/byte: 20000, count: 70
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.108        I Transaction added to pool: txid <4c861dc66cc0ddb3e81e23f2e98a790e2d7d3d07d7ecc1213b42ee2ce5c35724> weight: 1533 fee/byte: 20000, count: 71
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.111        I Transaction added to pool: txid <d0ed3acf2b073d67715c962a2d133519e00b4084206abed24b5e7126c29364f3> weight: 2222 fee/byte: 20000, count: 72
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.118        I Transaction added to pool: txid <5028fc8a47db048f8405cc8a50bb9876ddce0e441db897729f87a32cef57eb5a> weight: 6649 fee/byte: 20000, count: 73
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.121        I Transaction added to pool: txid <158b4eadec81d52849f423ec63f1d885a6e15fe3ab5e7de5ae5b0fbb895bb244> weight: 4259 fee/byte: 20000, count: 74
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.125        I Transaction added to pool: txid <193c243d4ed6a9281f1195ac3cd116a34853be68cb6770b268f84bf1900601c1> weight: 1532 fee/byte: 20000, count: 75
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.128        I Transaction added to pool: txid <6b74d5ea8517d590393b32fc4f78141c0f73acd4c0c09d1fac79bafb5687d966> weight: 1534 fee/byte: 20000, count: 76
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.131        I Transaction added to pool: txid <c0da90af49cac73cb7bb32561317043b6c930f551d04ddc2036df8ed583be439> weight: 2217 fee/byte: 20000, count: 77
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.135        I Transaction added to pool: txid <39fa7f72dbb0a1b72f8c5423adf483b06f694bafbab9785e23444343156bcd52> weight: 2219 fee/byte: 20000, count: 78
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.138        I Transaction added to pool: txid <828c4e2989e64a65b3af4b7025d28297e20fad843c97caf2aa264c26cc3a84f9> weight: 1529 fee/byte: 20000, count: 79
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.141        I Transaction added to pool: txid <7640c46c0072db50a73ad22fc5d25b40b207d4d582594be350a1f37b2dd88d5c> weight: 1531 fee/byte: 20000, count: 80
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.145        I Transaction added to pool: txid <7f5e62e9a444b64886240527d8966351b175728d383a25b9688ad2751151ca7a> weight: 1534 fee/byte: 20000, count: 81
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.148        I Transaction added to pool: txid <05decca85604d89af5fc415f691068ef413b785b824353672866419d3c73b63b> weight: 2222 fee/byte: 20000, count: 82
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.152        I Transaction added to pool: txid <0d389a6f67f8dc8448f98e353744cf2e16ea5e874393339a737609c39d0165c8> weight: 1533 fee/byte: 20000, count: 83
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.155        I Transaction added to pool: txid <d3b438d0a0a5d08dcea6c3b7a38efac28810623669e666d9f987e64d77e5eb76> weight: 2906 fee/byte: 20000, count: 84
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.158        I Transaction added to pool: txid <288dff67608ec951ce15545df75bfb2cd4428a903f50659cb4ced2fc95fa81d9> weight: 1533 fee/byte: 20000, count: 85
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.162        I Transaction added to pool: txid <df4a44167734f93ef1f8ce5a82c137f3b870621850fe536c5579602d65b4633f> weight: 1535 fee/byte: 20000, count: 86
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.165        I Transaction added to pool: txid <bed6c60554613d06b7265333d486a4ddb202d49dc6ccb97e3aff43227e7e3957> weight: 1529 fee/byte: 20000, count: 87
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.168        I Transaction added to pool: txid <a9c80e0db4d1cb83c22639859bbef6a7bbea0a696bbb52169ff313259a2c97ac> weight: 2219 fee/byte: 20000, count: 88
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.172        I Transaction added to pool: txid <7ff5d6132476a34707fad665eff4c949ffee6f5315ebe29f6ae368515c787d10> weight: 2224 fee/byte: 20000, count: 89
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.175        I Transaction added to pool: txid <9b955e095ebc37737ebe3a90f9022f14a5a641e9494b9f975f641de459cfe143> weight: 3019 fee/byte: 20000, count: 90
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.179        I Transaction added to pool: txid <686315e58da5f568c7f8dd828697257d8577edba24c779fdd13f0d6e6edee71a> weight: 1534 fee/byte: 20000, count: 91
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.182        I Transaction added to pool: txid <1aeaf5ea5ff87bfdcefe3a26b16cf71ceee9d8c51adcccc7832903c289a85928> weight: 4151 fee/byte: 20000, count: 92
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.185        I Transaction added to pool: txid <c9d1d81a240ea040f6af9ccf93bb6e451e5505b871727425dc6ab4f434464f25> weight: 1532 fee/byte: 20000, count: 93
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.189        I Transaction added to pool: txid <eedc68c0c2b5704230b35c0ab81ba19453dedb68c3fe6b5ac03858b16d52ea3f> weight: 1536 fee/byte: 20000, count: 94
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.192        I Transaction added to pool: txid <43fcc75c94d1a1da38da8864a861fedbdf8d9ed212374fd074d5bbe7bc00e6d1> weight: 2326 fee/byte: 20000, count: 95
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.195        I Transaction added to pool: txid <81050941590b9bcdf670770473145a66774d9e61f68d784d8e073d652521de8d> weight: 1533 fee/byte: 20000, count: 96
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.199        I Transaction added to pool: txid <27f06689346bd715b8b0bdb4361f0fecd393886b0951cafd44eca5fd3e24f7a0> weight: 2223 fee/byte: 20000, count: 97
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.202        I Transaction added to pool: txid <41f8bbaa9077686e72572350227487e06f51204409867c417727b7d1a956322c> weight: 1532 fee/byte: 20000, count: 98
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.205        I Transaction added to pool: txid <7030445dde2f8a4faec2e7a8812a3f8f46096b1e4bb17ed240138be5f6a1b5d7> weight: 1530 fee/byte: 20000, count: 99
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.209        I Transaction added to pool: txid <d1e557d080c7763507740038954827faf1c899f23918520610b74ad4e2b6484e> weight: 1534 fee/byte: 20000, count: 100
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.212        I Transaction added to pool: txid <ca38f35a73e93ed1756eed92df6d832bcdaca038c158a114c1a2d6d7fd95fffa> weight: 1537 fee/byte: 20000, count: 101
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.215        I Transaction added to pool: txid <b7ba7668994e89278276762c57158f052f2c7ecd9103f1643c888038f62747d9> weight: 1534 fee/byte: 20000, count: 102
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.219        I Transaction added to pool: txid <352bab4b5a59a7dbfa3c02267d81d25576974ca31e8138a0b8480f0a7e4aab0e> weight: 1533 fee/byte: 20000, count: 103
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.222        I Transaction added to pool: txid <1abc9d5a39c3bc75422adb4b2aef092dcf9080dd804388941149d3438a8003c1> weight: 1530 fee/byte: 20000, count: 104
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.225        I Transaction added to pool: txid <6857f36e633ccda7293a518daf9610a8232bb354928ef680940262ee7b092e18> weight: 1531 fee/byte: 20000, count: 105
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.229        I Transaction added to pool: txid <5f129a4273b4f1820338b5335cfe8aaa5cfcfa1c7c7d5abf2e3b88b6024df215> weight: 1526 fee/byte: 20000, count: 106
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.232        I Transaction added to pool: txid <e92f0b0c53fb205fd4af12f07c844a4d8c2f4e967f9005be686735500b2bd39a> weight: 1534 fee/byte: 20000, count: 107
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.238        I Transaction added to pool: txid <7fa1429e65810e69f2daea3d29d7d4c186ca5a2937af9e79631fb0bc14b07f24> weight: 2220 fee/byte: 20000, count: 108
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.242        I Transaction added to pool: txid <6e6338fb4b6dc2ea1f59b8ea366b65864a4d1039287a3f77d2ef4b09a2b223d2> weight: 2218 fee/byte: 20000, count: 109
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.245        I Transaction added to pool: txid <a28a81830683ee3e8d5a3ce3102932b981bbdf0311be6411f713c352e6126e46> weight: 1529 fee/byte: 20000, count: 110
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.249        I Transaction added to pool: txid <07c668ee1e43a83d0421d8cad8940bf51c3e26a05e56f646317ad56b3d32c85f> weight: 1536 fee/byte: 20000, count: 111
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.252        I Transaction added to pool: txid <72b2c167223ec401ce3b4baccda5260b4cfa13488fd20295d1001811af56b458> weight: 6706 fee/byte: 20000, count: 112
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.256        I Transaction added to pool: txid <fcb53cd37a8e12e2905be27cbb6a50463abe81dd1687d100b7735edfbed59b52> weight: 2217 fee/byte: 20000, count: 113
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.259        I Transaction added to pool: txid <d72357f0a647ed2bfeea4e6b269ea0c9ad96960a1e2c1c7d2a0d036efab9559e> weight: 2226 fee/byte: 20000, count: 114
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.263        I Transaction added to pool: txid <c6b4be4826d821a351af0406460ad8d33b57844dcf7e4a4f816b79852c9ff4f9> weight: 2218 fee/byte: 20000, count: 115
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.266        I Transaction added to pool: txid <507111bd2854ea4ff2daee505532915646957542bd9eb7336fd5238ff9cd4b13> weight: 1537 fee/byte: 20000, count: 116
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.269        I Transaction added to pool: txid <6cbadeff9985c10167e93a7d4f211e0c6c47e3b68426563d0e8356b2c27fac41> weight: 1530 fee/byte: 20000, count: 117
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.273        I Transaction added to pool: txid <d8e3ea4b4fd042cfa9e92dea49e6896cf7a32f536cac9596e6526b1ddc2ec841> weight: 1535 fee/byte: 20000, count: 118
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.276        I Transaction added to pool: txid <69adbae368dc01d218dba084f671a1fd14fe93d059238bc2301d0a8c3f7f7347> weight: 2216 fee/byte: 20000, count: 119
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.296        I Transaction added to pool: txid <0fca59da860e755ab2ccb6a3bea8f38cd02c4cffec4cd12ad6566e676849faa5> weight: 10469 fee/byte: 19893, count: 120
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.315        I Transaction added to pool: txid <cde1e8fce48fae6d5078f082e4994be930a4275f6f91ddce1da1504cb8bdbb6c> weight: 10489 fee/byte: 19855.1, count: 121
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.323        I +++++ BLOCK SUCCESSFULLY ADDED
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.323        I id:        <269f8d8a7541a551ecd790e58c8389723900dbee22e7e662b73ebb461b3430b4>
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.323        I PoW:        <d50438246412931145e32b5b370423740ace5958d8314c92d3668c0300000000>
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.323        I HEIGHT 3040433, difficulty:        270682699886
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.323        I block reward: 0.683016130000(0.600000000000 + 0.083016130000), coinbase_weight: 97, cumulative weight: 281608, 9(0/4)ms
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.330        I Pruning blockchain...
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.333        I Pruned blockchain in 2 ms: 0 MB (0 MB) pruned in 0 records (0/4801491 4096 byte pages), 0/226 pruned records
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.396        I Target height decreasing from 3047197 to 0
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.396        I [185.220.101.180:51483 INC] [0] state: closed in state synchronizing
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.396        I [185.220.101.180:51483 98354b92-c093-49ae-a581-3a5c4f75f11a INC] CLOSE CONNECTION
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.397        I net_service loop stopped.
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.398        I p2p net loop stopped
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.403        I Stopping core RPC server...
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.403        I Stopping restricted RPC server...
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.403        I Node stopped.
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.404        I Deinitializing core RPC server...
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.417        I Deinitializing restricted RPC server...
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.426        I Deinitializing p2p...
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.426        I Killing the net_node
Dec 25 02:10:16 docker-4 3026041b80e6[768]: 2023-12-25 07:10:16.563        I Joined extra background net_node threads
```

Nothing stands out to me as a non-developer.

## moneromooo-monero | 2023-12-25T15:20:05+00:00
I do not see any hint of a crash here.
Something is apparently asking monerod to stop. Are you using systemd ? Many people before had issues with systemd deciding to stop monerod on its own accord. Similar software might also have this particularity.

## arhue | 2023-12-25T16:05:45+00:00
I'm using Docker Swarm to orchestrate the container. Systemd is launching the Docker daemon. I'm unfamiliar with how Monerod works, this is the first time I'm trying to host a node, but shouldn't it continue where it left off and not start from 0 if this was a clean shutdown? The only thing that could be killing it is OOM killer on the host, but I see no evidence of that on VM's stdout and that would likely kill containerd and not the actual process? Not sure about that. This is what Docker service logs say:

```
varun@docker-4:~$ sudo docker service ps monero_monerod
ID             NAME                   IMAGE                               NODE       DESIRED STATE   CURRENT STATE            ERROR                              PORTS
kkqcenhf6f10   monero_monerod.1       sethsimmons/simple-monerod:latest   docker-4   Running         Running 2 minutes ago                                       *:18089->18089/tcp,*:18089->18089/tcp,*:18080->18080/tcp,*:18080->18080/tcp
brqlmigsh6nz    \_ monero_monerod.1   sethsimmons/simple-monerod:latest   docker-4   Shutdown        Complete 2 minutes ago                                      
idc883gre8ck    \_ monero_monerod.1   sethsimmons/simple-monerod:latest   docker-4   Shutdown        Shutdown 8 hours ago                                        
zkvcaaf5tbuu    \_ monero_monerod.1   sethsimmons/simple-monerod:latest   docker-4   Shutdown        Complete 8 hours ago                                        
```

I gave the node way more CPU and memory and still it seems to be happening. 

The 3rd shutdown signal is misleading because I had restarted the node. Looks like the task itself exits for some reason and reports a clean shutdown when Swarm hasn't asked it to shutdown? 

https://docs.docker.com/engine/swarm/how-swarm-mode-works/swarm-task-states/


## moneromooo-monero | 2023-12-25T16:12:18+00:00
monerod should start syncing from whatever height it had previously reached. I assume your /home/varun is persistent ?

## arhue | 2023-12-25T16:19:29+00:00
Correct, persistent. OK, I think I see what the issue could be.

```
varun@docker-4:~/monero/bitmonero$ sudo docker exec -it 762668251cf5 sh
/home/monero # ls -lah^C
/home/monero # ls
/home/monero # l -a
sh: l: not found
/home/monero # ls -a
.           ..          .bitmonero
/home/monero # cd .bitmonero/
/home/monero/.bitmonero # ls -lah
total 8K     
drwxr-xr-x    2 root     root        4.0K Dec 24 14:46 .
drwxr-sr-x    1 root     root        4.0K Dec 25 12:02 ..
/home/monero # cd /root
~ # ls
~ # ls -lah
total 16K    
drwx------    1 root     root        4.0K Dec 25 16:13 .
drwxr-xr-x    1 root     root        4.0K Dec 25 16:10 ..
-rw-------    1 root     root         131 Dec 25 16:15 .ash_history
drwxr-x--x    3 root     root        4.0K Dec 25 16:15 .bitmonero
~ # cd .bitmonero/
~/.bitmonero # ls
bitmonero.log                      bitmonero.log-2023-12-25-16-15-43
bitmonero.log-2023-12-25-16-11-49  lmdb
bitmonero.log-2023-12-25-16-12-57  rpc_ssl.crt
bitmonero.log-2023-12-25-16-13-53  rpc_ssl.key
bitmonero.log-2023-12-25-16-14-48
```

It's creating the dir in /root/ because of the GID/UID I supplied. For some reason it didn't work with monero user's GID/UID.

This is completely my fault for overlooking. I guess I'll close this then because even if Docker Swarm asked it to shutdown for whatever reason, it should not be an issue if the dir is persistent.

## arhue | 2023-12-25T16:22:11+00:00
Closing this issue. Sorry for leading you into my wild goose chase.

## arhue | 2023-12-28T05:42:43+00:00
Reopening issue because this wasn't actually fixed. It crashed again and this time didn't persist data even when the disk was attached correctly.

```
2023-12-28 03:06:06.665 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 2793908/3049235 (91%, 255327 left)
^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@2023-12-28 03:09:45.102     560bee0c4dc8        INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-12-28 03:09:45.102     560bee0c4dc8        INFO    global  src/daemon/main.cpp:309 Monero 'Fluorine Fermi' (v0.18.3.1-release)
2023-12-28 03:09:45.102     560bee0c4dc8        INFO    global  src/daemon/protocol.h:53        Initializing cryptonote protocol...
2023-12-28 03:09:45.102     560bee0c4dc8        INFO    global  src/daemon/protocol.h:58        Cryptonote protocol initialized OK
2023-12-28 03:09:45.103     560bee0c4dc8        INFO    global  src/daemon/core.h:64    Initializing core...
2023-12-28 03:09:45.103     560bee0c4dc8        INFO    global  src/cryptonote_core/cryptonote_core.cpp:523     Loading blockchain from folder /root/.bitmonero/lmdb ...
2023-12-28 03:09:45.172     560bee0c4dc8        INFO    global  src/cryptonote_core/cryptonote_core.cpp:698     Loading checkpoints
2023-12-28 03:09:45.173     560bee0c4dc8        INFO    global  src/cryptonote_core/cryptonote_core.cpp:730     Pruning blockchain...
2023-12-28 03:09:45.174     560bee0c4dc8        INFO    global  src/daemon/core.h:81    Core initialized OK
2023-12-28 03:09:45.174     560bee0c4dc8        INFO    global  src/daemon/p2p.h:64     Initializing p2p server...
2023-12-28 03:09:45.205     560bee0c4dc8        INFO    global  src/daemon/p2p.h:69     p2p server initialized OK
2023-12-28 03:09:45.205     560bee0c4dc8        INFO    global  src/daemon/rpc.h:63     Initializing core RPC server...
2023-12-28 03:09:45.206     560bee0c4dc8        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 0.0.0.0 (IPv4):18081
2023-12-28 03:09:45.218     560bee0c4dc8        INFO    global  src/daemon/rpc.h:69     core RPC server initialized OK on port: 18081
2023-12-28 03:09:45.218     560bee0c4dc8        INFO    global  src/daemon/rpc.h:63     Initializing restricted RPC server...
2023-12-28 03:09:45.218     560bee0c4dc8        INFO    global  contrib/epee/include/net/http_server_impl_base.h:79     Binding on 0.0.0.0 (IPv4):18089
2023-12-28 03:09:45.450     560bee0c4dc8        INFO    global  src/daemon/rpc.h:69     restricted RPC server initialized OK on port: 18089
2023-12-28 03:09:45.545     560bee0c4dc8        INFO    global  src/daemon/rpc.h:74     Starting core RPC server...
2023-12-28 03:09:45.545 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     core RPC server started ok
2023-12-28 03:09:45.546 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:74     Starting restricted RPC server...
2023-12-28 03:09:45.546 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:79     restricted RPC server started ok
2023-12-28 03:09:45.546 [SRV_MAIN]      INFO    global  src/daemon/daemon.cpp:214       Public RPC port 18089 will be advertised to other peers over P2P
2023-12-28 03:09:45.547 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:79     Starting p2p net loop...
2023-12-28 03:09:46.547 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818
2023-12-28 03:09:46.547 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818    **********************************************************************
2023-12-28 03:09:46.548 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818    The daemon will start synchronizing with the network. This may take a long time to complete.
2023-12-28 03:09:46.548 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818
2023-12-28 03:09:46.548 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818    You can set the level of process detailization through "set_log <level|categories>" command,
2023-12-28 03:09:46.548 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818    where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-12-28 03:09:46.548 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818
2023-12-28 03:09:46.548 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818    Use the "help" command to see the list of available commands.
2023-12-28 03:09:46.548 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818    Use "help <command>" to see a command's documentation.
2023-12-28 03:09:46.548 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1818    **********************************************************************
2023-12-28 03:09:47.071 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     [23.92.36.60:18080 OUT] Sync data returned a new top block candidate: 1 -> 3049238 [Your node is 3049237 blocks (9.7 years) behind]
2023-12-28 03:09:47.071 [P2P6]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:406     SYNCHRONIZATION started
2023-12-28 03:09:47.315 [P2P7]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1696    Synced 101/3049238 (0%, 3049137 left)
```

I'm going to switch it to log level 1 again. I had turned it off because I thought it was fixed.

## arhue | 2023-12-28T05:46:48+00:00
I'm wondering if Docker Swarm someone causes 2 instances of monerod to run at one time in some specific instances. The time where it started from 0 again was also the time when I accidentally shut down my computer/Proxmox instance, taking down the VM. Would that have anything to do with it?

## selsta | 2023-12-28T05:47:11+00:00
There is no code in monerod that would delete or overwrite the blockchain, has to be a misconfiguration with docker.

## arhue | 2023-12-30T21:28:43+00:00
@selsta There were logs from before when it started from 0 present in the same directory. I modified my Docker compose file a bit

```
services:
  monerod:
    image: sethsimmons/simple-monerod:latest
    user: 0:0
    volumes:
      - /mnt/vol1/monero/bitmonero:/root/.bitmonero
    entrypoint: ["sh", "-c", "touch /root/.bitmonero/lmdb/test && rm /root/.bitmonero/lmdb/test && echo 'Test for mounted filesystem passed' && /entrypoint.sh"]
...
      - "--db-sync-mode=safe"
```

Seems to be working fine since then. I think it's most likely the `--db-sync-mode=safe` flag that has done the trick. I have an another issue with 18081 port not opening after I apply this flag, but I'll debug that separately. 

Thanks for your help. Closing this.

## arhue | 2024-01-04T03:32:06+00:00
This was still an issue for me. After debugging a lot of things I realised it was an Intel NIC driver bug that affected 2 of the hosts I had. Posting just incase it's useful for someone.

## cachho | 2024-02-04T13:37:30+00:00
@arhue I'm running into the same problem, also on an Intel machine. Can you share your whole `docker-compose.yml`?

## arhue | 2024-02-05T04:25:38+00:00
@cachho Here you go! Key thing is that I'm just making sure those dirs exist before allowing monerod to start so that it doesn't overwrite them. Still running smoothly for me after that.

The NIC driver bug was a separate issue that was affecting my GlusterFS shared storage. What NIC card do you have? I had I219 series onboard NIC and it was causing network to hang intermittently. 

```
version: '3.3'

services:
  monerod:
    image: sethsimmons/simple-monerod:latest
    user: 0:0
    volumes:
      - /mnt/vol1/monero/bitmonero:/root/.bitmonero
    entrypoint: ["sh", "-c", "touch /root/.bitmonero/lmdb/test && rm /root/.bitmonero/lmdb/test && echo 'Test for mounted filesystem passed' && /entrypoint.sh --rpc-restricted-bind-ip=0.0.0.0 --rpc-restricted-bind-port=18089 --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18081 --confirm-external-bind --public-node --enable-dns-blocklist --prep-blocks-threads=1"]
    deploy:
      labels:
        homepage.group: Services
        homepage.name: Monero
        homepage.description: Monero Public Node
        homepage.icon: monero.png
        homepage.href: https://monero.ca.varunpriolkar.com
        homepage.widget.type: customapi
        homepage.widget.url: http://linux-1.ca.varunpriolkar.com:5000/monero
        homepage.widget.mappings[0].label: price(cad)
        homepage.widget.mappings[0].field: cad
        homepage.widget.mappings[1].label: status
        homepage.widget.mappings[1].field: status
      mode: replicated
      replicas: 1
      resources:
        limits:
          cpus: '1.5'
      placement:
        constraints:
          - node.hostname != rpi
    networks:
      - monero
    ports:
      - 18080:18080
      - 18089:18089
      - 18081:18081
    expose:
      - "18080"
      - "18081"
      - "18089"
  tor:
    image: goldy/tor-hidden-service:latest
    environment:
        MONEROD_TOR_SERVICE_HOSTS: 18089:monerod:18089
        MONEROD_TOR_SERVICE_VERSION: '3'
    volumes:
      - /mnt/vol1/monero/tor:/var/lib/tor/hidden_service/
    networks: 
      - monero
    deploy:
      mode: replicated
      replicas: 1
      placement:
        constraints:
          - node.hostname != rpi
  gui:
    image: hvalev/monero-dashboard:latest
    networks:
      - monero
      - caddy
    environment:
      MONERO_HOST: monerod
      MONERO_PORT: 18081
      TICKER: "true"
      PORT: 3333
    deploy:
      mode: replicated
      replicas: 1
      labels:
        caddy: "monero.ca.varunpriolkar.com"
        caddy.reverse_proxy.to: "{{upstreams 3333}}"
        caddy.tls.dns: "route53"
        caddy.tls.dns.access_key_id: "{env.AWS_ACCESS_KEY}"
        caddy.tls.dns.secret_access_key: "{env.AWS_SECRET_KEY}"
 
networks:
  caddy:
    external: true
  monero:
    driver: overlay
    attachable: true
```

## cachho | 2024-02-26T15:20:00+00:00
> @cachho Here you go! Key thing is that I'm just making sure those dirs exist before allowing monerod to start so that it doesn't overwrite them. Still running smoothly for me after that.
> 
> The NIC driver bug was a separate issue that was affecting my GlusterFS shared storage. What NIC card do you have? I had I219 series onboard NIC and it was causing network to hang intermittently.
> 
> ```
> version: '3.3'
> 
> services:
>   monerod:
>     image: sethsimmons/simple-monerod:latest
>     user: 0:0
>     volumes:
>       - /mnt/vol1/monero/bitmonero:/root/.bitmonero
>     entrypoint: ["sh", "-c", "touch /root/.bitmonero/lmdb/test && rm /root/.bitmonero/lmdb/test && echo 'Test for mounted filesystem passed' && /entrypoint.sh --rpc-restricted-bind-ip=0.0.0.0 --rpc-restricted-bind-port=18089 --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18081 --confirm-external-bind --public-node --enable-dns-blocklist --prep-blocks-threads=1"]
>     deploy:
>       labels:
>         homepage.group: Services
>         homepage.name: Monero
>         homepage.description: Monero Public Node
>         homepage.icon: monero.png
>         homepage.href: https://monero.ca.varunpriolkar.com
>         homepage.widget.type: customapi
>         homepage.widget.url: http://linux-1.ca.varunpriolkar.com:5000/monero
>         homepage.widget.mappings[0].label: price(cad)
>         homepage.widget.mappings[0].field: cad
>         homepage.widget.mappings[1].label: status
>         homepage.widget.mappings[1].field: status
>       mode: replicated
>       replicas: 1
>       resources:
>         limits:
>           cpus: '1.5'
>       placement:
>         constraints:
>           - node.hostname != rpi
>     networks:
>       - monero
>     ports:
>       - 18080:18080
>       - 18089:18089
>       - 18081:18081
>     expose:
>       - "18080"
>       - "18081"
>       - "18089"
>   tor:
>     image: goldy/tor-hidden-service:latest
>     environment:
>         MONEROD_TOR_SERVICE_HOSTS: 18089:monerod:18089
>         MONEROD_TOR_SERVICE_VERSION: '3'
>     volumes:
>       - /mnt/vol1/monero/tor:/var/lib/tor/hidden_service/
>     networks: 
>       - monero
>     deploy:
>       mode: replicated
>       replicas: 1
>       placement:
>         constraints:
>           - node.hostname != rpi
>   gui:
>     image: hvalev/monero-dashboard:latest
>     networks:
>       - monero
>       - caddy
>     environment:
>       MONERO_HOST: monerod
>       MONERO_PORT: 18081
>       TICKER: "true"
>       PORT: 3333
>     deploy:
>       mode: replicated
>       replicas: 1
>       labels:
>         caddy: "monero.ca.varunpriolkar.com"
>         caddy.reverse_proxy.to: "{{upstreams 3333}}"
>         caddy.tls.dns: "route53"
>         caddy.tls.dns.access_key_id: "{env.AWS_ACCESS_KEY}"
>         caddy.tls.dns.secret_access_key: "{env.AWS_SECRET_KEY}"
>  
> networks:
>   caddy:
>     external: true
>   monero:
>     driver: overlay
>     attachable: true
> ```

That was  really helpful. I use nginx proxy manager instead of caddy, so I had to change some things around.

```
version: '3.3'

services:
  monerod:
    image: sethsimmons/simple-monerod:latest
    container_name: simple_monerod
    user: 0:0
    volumes:
      - /srv/dev-disk-by-uuid-8840/bitmonero:/root/.bitmonero
    entrypoint: ["sh", "-c", "mkdir -p /root/.bitmonero/lmdb && touch /root/.bitmonero/lmdb/test && rm /root/.bitmonero/lmdb/test && echo 'Test for mounted filesystem passed' && /entrypoint.sh --rpc-restricted-bind-ip=0.0.0.0 --rpc-restricted-bind-port=18089 --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18081 --confirm-external-bind --public-node --enable-dns-blocklist --prep-blocks-threads=1"]
    networks:
      - monero
      - nginx-proxy-manager-network
    ports:
      - 18080:18080
      - 18089
      - 18081:18081
    restart: unless-stopped
  tor:
    image: goldy/tor-hidden-service:latest
    container_name: monerod-tor
    environment:
        MONEROD_TOR_SERVICE_HOSTS: 18089:monerod:18089
        MONEROD_TOR_SERVICE_VERSION: '3'
    volumes:
      - /srv/dev-disk-by-uuid-8840/monero-tor:/var/lib/tor/hidden_service/
    networks: 
      - monero
  gui:
    image: hvalev/monero-dashboard:latest
    container_name: monero-gui
    networks:
      - monero
      - nginx-proxy-manager-network
    environment:
      MONERO_HOST: monerod
      MONERO_PORT: 18081
      TICKER: "true"
      PORT: 3333
    ports:
      - 3333
 
networks:
  nginx-proxy-manager-network:
    name: nginx-proxy-manager-network
    external: true
    driver: bridge
  monero:
    driver: bridge

```

# Action History
- Created by: arhue | 2023-12-24T22:10:49+00:00
- Closed at: 2023-12-30T21:28:43+00:00
