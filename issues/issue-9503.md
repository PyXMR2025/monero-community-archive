---
title: Can't sync to stagenet blockchain (COMMAND_HANDSHAKE Failed)
source_url: https://github.com/monero-project/monero/issues/9503
author: Demontager
assignees: []
labels:
- reproduction needed
- more info needed
created_at: '2024-10-04T13:49:15+00:00'
updated_at: '2025-12-19T15:03:46+00:00'
type: issue
status: closed
closed_at: '2025-12-19T15:03:46+00:00'
---

# Original Description
I tried to sync Fluorine Fermi' (v0.18.3.4-83dd5152e) to full stagent, but constantly getting  COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
However i was able to sync to pruned stagent.
```
dem@xeon:~/monero-release/monero/build/Linux/release-v0.18/release/bin$ ./monerod --stagenet --log-level=1 --data-dir /home/dem/.bitmonero_stagenet_full
2024-10-04 13:41:57.669	I Monero 'Fluorine Fermi' (v0.18.3.4-83dd5152e)
2024-10-04 13:41:57.669	I Moving from main() into the daemonize now.
2024-10-04 13:41:57.669	I Initializing cryptonote protocol...
2024-10-04 13:41:57.669	I Cryptonote protocol initialized OK
2024-10-04 13:41:57.670	I Initializing core...
2024-10-04 13:41:57.670	I Loading blockchain from folder /home/dem/.bitmonero_stagenet_full/stagenet/lmdb ...
2024-10-04 13:41:57.671	I batch transaction mode already enabled, but asked to enable batch mode
2024-10-04 13:41:57.671	I batch transactions enabled
2024-10-04 13:41:57.671	I Blockchain initialized. last block: 0, d3822.h2.m53.s4 time ago, current difficulty: 1
2024-10-04 13:41:57.671	I Validating txpool contents for v1
2024-10-04 13:41:57.671	I Loading checkpoints
2024-10-04 13:41:57.672	I Core initialized OK
2024-10-04 13:41:57.672	I Initializing p2p server...
2024-10-04 13:41:57.674	I Setting LIMIT: 2048 kbps
2024-10-04 13:41:57.674	I Set limit-up to 2048 kB/s
2024-10-04 13:41:57.674	I Setting LIMIT: 8192 kbps
2024-10-04 13:41:57.674	I Setting LIMIT: 8192 kbps
2024-10-04 13:41:57.674	I Set limit-down to 8192 kB/s
2024-10-04 13:41:57.674	I Setting LIMIT: 2048 kbps
2024-10-04 13:41:57.674	I Set limit-up to 2048 kB/s
2024-10-04 13:41:57.674	I Setting LIMIT: 8192 kbps
2024-10-04 13:41:57.674	I Setting LIMIT: 8192 kbps
2024-10-04 13:41:57.674	I Set limit-down to 8192 kB/s
2024-10-04 13:41:57.674	I Set server type to: 2 from name: P2P, prefix_name = P2P
2024-10-04 13:41:57.674	I Binding (IPv4) on 0.0.0.0:38080
2024-10-04 13:41:57.674	I Net service bound (IPv4) to 0.0.0.0:38080
2024-10-04 13:41:57.675	I p2p server initialized OK
2024-10-04 13:41:57.675	I Initializing core RPC server...
2024-10-04 13:41:57.675	I Set server type to: 1 from name: RPC, prefix_name = RPC
2024-10-04 13:41:57.675	I Binding on 127.0.0.1 (IPv4):38081
2024-10-04 13:41:57.677	I core RPC server initialized OK on port: 38081
2024-10-04 13:41:57.678	I ZMQ now listening at tcp://127.0.0.1:38082
2024-10-04 13:41:57.678	I Starting core RPC server...
2024-10-04 13:41:57.678	I Run net_service loop( 2 threads)...
2024-10-04 13:41:57.678	I core RPC server started ok
2024-10-04 13:41:57.679	I Starting p2p net loop...
2024-10-04 13:41:57.679	I Run net_service loop( 10 threads)...
2024-10-04 13:41:57.679	I ZMQ Server started
2024-10-04 13:41:58.680	I 
2024-10-04 13:41:58.680	I **********************************************************************
2024-10-04 13:41:58.680	I The daemon will start synchronizing with the network. This may take a long time to complete.
2024-10-04 13:41:58.680	I 
2024-10-04 13:41:58.680	I You can set the level of process detailization through "set_log <level|categories>" command,
2024-10-04 13:41:58.680	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2024-10-04 13:41:58.680	I 
2024-10-04 13:41:58.680	I Use the "help" command to see the list of available commands.
2024-10-04 13:41:58.680	I Use "help <command>" to see a command's documentation.
2024-10-04 13:41:58.680	I **********************************************************************
2024-10-04 13:41:58.683	I adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5
2024-10-04 13:41:58.683	I adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D
2024-10-04 13:41:58.725	I Found TXT record for updates.moneropulse.org
2024-10-04 13:41:58.726	I Found TXT record for updates.moneropulse.org
```

And here where failed connects happens
```
2024-10-04 13:41:59.353	W [51.79.173.165:38080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2024-10-04 13:41:59.353	W [51.79.173.165:38080 OUT] COMMAND_HANDSHAKE Failed
2024-10-04 13:41:59.353	I [51.79.173.165:38080 OUT] Failed to HANDSHAKE with peer 51.79.173.165:38080
2024-10-04 13:41:59.353	I [51.79.173.165:38080 OUT] [0] state: closed in state before_handshake
2024-10-04 13:41:59.353	I [51.79.173.165:38080 1cd7c25e-73ca-48da-a96b-f48ade18897e OUT] CLOSE CONNECTION
2024-10-04 13:42:04.354	I 0Connect failed to 77.172.183.193:38080
2024-10-04 13:42:04.399	I [176.9.0.187:38080 3e9c4e0c-7664-417e-ba21-7ccbf0d4a4ce OUT] NEW CONNECTION
2024-10-04 13:42:04.399	I [176.9.0.187:38080 OUT] 262 bytes sent for category command-1001 initiated by us
2024-10-04 13:42:04.444	I Failed to invoke command 1001 return code -3
2024-10-04 13:42:04.444	W [176.9.0.187:38080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2024-10-04 13:42:04.444	W [176.9.0.187:38080 OUT] COMMAND_HANDSHAKE Failed
2024-10-04 13:42:04.444	I [176.9.0.187:38080 OUT] Failed to HANDSHAKE with peer 176.9.0.187:38080
2024-10-04 13:42:04.445	I [176.9.0.187:38080 OUT] [0] state: closed in state before_handshake
2024-10-04 13:42:04.445	I [176.9.0.187:38080 3e9c4e0c-7664-417e-ba21-7ccbf0d4a4ce OUT] CLOSE CONNECTION
2024-10-04 13:42:04.574	I [192.99.8.110:38080 08a6d4ac-06ef-4b66-ae0c-b6464370f137 OUT] NEW CONNECTION
2024-10-04 13:42:04.574	I [192.99.8.110:38080 OUT] 262 bytes sent for category command-1001 initiated by us
2024-10-04 13:42:04.702	I Failed to invoke command 1001 return code -3
2024-10-04 13:42:04.702	W [192.99.8.110:38080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2024-10-04 13:42:04.703	W [192.99.8.110:38080 OUT] COMMAND_HANDSHAKE Failed
2024-10-04 13:42:04.703	I [192.99.8.110:38080 OUT] Failed to HANDSHAKE with peer 192.99.8.110:38080
2024-10-04 13:42:04.703	I [192.99.8.110:38080 OUT] [0] state: closed in state before_handshake
2024-10-04 13:42:04.703	I [192.99.8.110:38080 08a6d4ac-06ef-4b66-ae0c-b6464370f137 OUT] CLOSE CONNECTION
2024-10-04 13:42:04.757	I [37.187.74.171:38080 b475afd0-b110-45c0-9899-a36115507076 OUT] NEW CONNECTION
2024-10-04 13:42:04.757	I [37.187.74.171:38080 OUT] 262 bytes sent for category command-1001 initiated by us
2024-10-04 13:42:04.812	I Failed to invoke command 1001 return code -3
2024-10-04 13:42:04.812	W [37.187.74.171:38080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2024-10-04 13:42:04.812	W [37.187.74.171:38080 OUT] COMMAND_HANDSHAKE Failed
2024-10-04 13:42:04.812	I [37.187.74.171:38080 OUT] Failed to HANDSHAKE with peer 37.187.74.171:38080
2024-10-04 13:42:04.812	I [37.187.74.171:38080 OUT] [0] state: closed in state before_handshake
2024-10-04 13:42:04.812	W Failed to connect to any of seed peers, trying fallback seeds
2024-10-04 13:42:04.812	I [37.187.74.171:38080 b475afd0-b110-45c0-9899-a36115507076 OUT] CLOSE CONNECTION
2024-10-04 13:42:04.813	I Resolving node address: host=176.9.0.187, port=38080
2024-10-04 13:42:04.813	I Added node: 176.9.0.187:38080
2024-10-04 13:42:04.813	I Resolving node address: host=192.99.8.110, port=38080
2024-10-04 13:42:04.813	I Added node: 192.99.8.110:38080
2024-10-04 13:42:04.813	I Resolving node address: host=37.187.74.171, port=38080
2024-10-04 13:42:04.813	I Added node: 37.187.74.171:38080
2024-10-04 13:42:04.813	I Resolving node address: host=51.79.173.165, port=38080
2024-10-04 13:42:04.813	I Added node: 51.79.173.165:38080
2024-10-04 13:42:04.813	I Resolving node address: host=77.172.183.193, port=38080
2024-10-04 13:42:04.813	I Added node: 77.172.183.193:38080
2024-10-04 13:42:04.858	I [176.9.0.187:38080 75073c8e-40d5-4b82-8ac9-0f24024c944f OUT] NEW CONNECTION
2024-10-04 13:42:04.859	I [176.9.0.187:38080 OUT] 262 bytes sent for category command-1001 initiated by us
2024-10-04 13:42:04.904	I Failed to invoke command 1001 return code -3
2024-10-04 13:42:04.905	W [176.9.0.187:38080 OUT] COMMAND_HANDSHAKE invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)
2024-10-04 13:42:04.905	W [176.9.0.187:38080 OUT] COMMAND_HANDSHAKE Failed
2024-10-04 13:42:04.905	I [176.9.0.187:38080 OUT] Failed to HANDSHAKE with peer 176.9.0.187:38080
```

# Discussion History
## selsta | 2024-10-31T15:17:11+00:00
Can you add more information how it fails? It just gets stuck? Does not keep any connections? Does it only terminate some connections but keep others?

## selsta | 2025-12-19T15:03:42+00:00
Closing due to lack of reply. There has also been a lot of changes recently due to stressnet testing so please check the latest version.

# Action History
- Created by: Demontager | 2024-10-04T13:49:15+00:00
- Closed at: 2025-12-19T15:03:46+00:00
