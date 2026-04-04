---
title: Cannot broadcast transaction through the wallet RPC (stagenet)
source_url: https://github.com/monero-project/monero/issues/8372
author: jekkodev
assignees: []
labels: []
created_at: '2022-06-02T13:54:27+00:00'
updated_at: '2025-09-01T21:54:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello!

I'm trying to write a simple automaton to send the received coins to some addresses via the wallet RPC interface. 
I'm using the stagenet for testing as decribed in the [documentation](https://monerodocs.org/infrastructure/networks/#stagenet), however, I'm missing something and I cannot find anyone with the same issue as me

I start the monero RPC (v.0.17.3.2) wallet connecting to a remote daemon and set the log level to 4:
`monero-wallet-rpc --stagenet --rpc-bind-ip 127.0.0.1 --rpc-bind-port 38082 --wallet-dir /path/to/monero/wallets --daemon-address ct36dsbe3oubpbebpxmiqz4uqk6zb6nhmkhoekileo4fts23rvuse2qd.onion:38081 --proxy 127.0.0.1:9050 --disable-rpc-login --log-level=4`

I use the RPC calls to retrieve the current balance on every address, build a transaction to calculate the fee and everything seem to work fine.  I try to make a transaction sending all the money contained in two address to another two address. I make sure to use less money than the total subtracting the fees to the outputs:

`curl http://127.0.0.1:38082/json_rpc -d '{"method":"transfer","params":{"account_index":1,"destinations":[{"amount":695282695003,"address":"773b8zYQ52hVdXSwv4PW9HEiCBbttfjJY4HYG3SBLUVdNJEBe1Fi293JgwgdZsKzB3R7nAfGeZ4meNjrrMD2VPyZ3MdCr65"},{"amount":21515971701,"address":"79EnhaHfb6CeXPdK84uQiqMvsmEXP4ZLrHYHzKMdtu555a782wv54TSAqXerZWtExgjcpWcU6NTdxdbY7wJQQPqh9uVuVzy"}],"subaddr_indices":[1,2],"priority":2,"mixin":10,"ring_size":11,"unlock_time":0,"get_tx_key":true,"get_tx_hex":true,"do_not_relay":false},"jsonrpc":"2.0","id":"0"}'`

You can read the full log of the wallet RPC when I make the call until the transaction is broadcasted **[here](https://github.com/monero-project/monero/files/8824512/monero_rpc_transfer_log.txt)**

Everything seems to work fine, however, after 500 seconds I get the following message that states that the transaction was never actually broadcasted:

> 2022-06-02 13:14:50.922 I Refresh done, blocks received: 1, balance (all accounts): 0.000000000001, unlocked: 0.000000000000
> 2022-06-02 13:15:11.087 T update_pool_state start
> 2022-06-02 13:15:12.999 T READ ENDS: Success. bytes_tr: 327
> 2022-06-02 13:15:13.000 T http_stream_filter::parse_cached_header(*)
> 2022-06-02 13:15:13.000 T update_pool_state got pool
> 2022-06-02 13:15:13.001 I Pending txid <d3dc473f9b8e0220b48d70027d577bd3eab46659d455ecb9fc4481909eea8324> not in pool after 500 seconds, marking as failed
> 2022-06-02 13:15:13.002 I Resetting spent status for output 0: <cc3cff599365cafe7e021ebb31f7f77f9b2a444ceb487d43edbe30160b5d6e16>
> 2022-06-02 13:15:13.002 D Setting UNSPENT: ki <cc3cff599365cafe7e021ebb31f7f77f9b2a444ceb487d43edbe30160b5d6e16>, amount 0.517199056705
> 2022-06-02 13:15:13.002 I Resetting spent status for output 1:
 <9f77857974d5f6abd08875ed0f70d319c87ed5ff6e896143955ede660583b08e>
> 2022-06-02 13:15:13.003 D Setting UNSPENT: ki <9f77857974d5f6abd08875ed0f70d319c87ed5ff6e896143955ede660583b08e>, amount 0.200000000000
> 2022-06-02 13:15:13.003 T update_pool_state done first loop
> 2022-06-02 13:15:13.004 T update_pool_state done second loop
> 2022-06-02 13:15:13.004 I Found new pool tx: <a580eb33eb7634e2be31964fe1ec64c117be6e2d9241127a3bc9a48023633c55>
> 2022-06-02 13:15:13.005 D Already seen <70afdd8b37f3aa9582dd2ac74863af87f20cd2d352047837126be55c7b60d5ee>, and not for us, skipped
> 2022-06-02 13:15:13.005 D asking for 1 transactions
> 2022-06-02 13:15:13.643 T READ ENDS: Success. bytes_tr: 1184
> 2022-06-02 13:15:13.644 T http_stream_filter::parse_cached_header(*)
> 2022-06-02 13:15:13.645 D Got 1 and OK
> 2022-06-02 13:15:13.646 T update_pool_state end
> 2022-06-02 13:15:13.646 D Pulling blocks: start_height 0
> 2022-06-02 13:15:14.330 T READ ENDS: Success. bytes_tr: 276
> 2022-06-02 13:15:14.331 T http_stream_filter::parse_cached_header(*)
> 2022-06-02 13:15:14.331 D Pulled blocks: blocks_start_height 0, count 0, height 0, node height 1105514
> 2022-06-02 13:15:14.332 I Refresh done, blocks received: 0, balance (all accounts): 0.717199056705, unlocked: 0.717199056705

If I try to redo the transaction with the same command, I get the response: 
`{
  "error": {
    "code": -4,
    "message": "transaction was rejected by daemon"
  },
  "id": "0",
  "jsonrpc": "2.0"
}`

And the log of the wallet RPC states that the transaction was rejected for double spending:

> 2022-06-02 13:18:38.793 E daemon_send_resp.status != CORE_RPC_STATUS_OK. THROW EXCEPTION: error::tx_rejected
> 2022-06-02 13:18:38.793 W /home/ubuntu/build/monero/src/wallet/wallet2.cpp:6288:N5tools5error11tx_rejectedE: transaction was rejected by daemon, status = <error>, tx:
> 2022-06-02 13:18:38.794 W {
> 2022-06-02 13:18:38.794 W   "version": 2,
> 2022-06-02 13:18:38.795 W   "unlock_time": 0,
> 2022-06-02 13:18:38.796 W   "vin": [ {
> 2022-06-02 13:18:38.796 W       "key": {
> 2022-06-02 13:18:38.797 W         "amount": 0,
> 2022-06-02 13:18:38.797 W         "key_offsets": [ 4788588, 176947, 29877, 4721, 30835, 405, 14976, 1549, 3277, 4150, 1125
> 2022-06-02 13:18:38.797 W         ],
> 2022-06-02 13:18:38.798 W         "k_image": "cc3cff599365cafe7e021ebb31f7f77f9b2a444ceb487d43edbe30160b5d6e16"
> 2022-06-02 13:18:38.799 W       }
> 2022-06-02 13:18:38.799 W     }, {
> 2022-06-02 13:18:38.800 W       "key": {
> 2022-06-02 13:18:38.800 W         "amount": 0,
> 2022-06-02 13:18:38.801 W         "key_offsets": [ 4746775, 18737, 212149, 28496, 31937, 4735, 8226, 4154, 108, 1847, 270
> 2022-06-02 13:18:38.801 W         ],
> 2022-06-02 13:18:38.802 W         "k_image": "9f77857974d5f6abd08875ed0f70d319c87ed5ff6e896143955ede660583b08e"
> 2022-06-02 13:18:38.802 W       }
> 2022-06-02 13:18:38.803 W     }
> 2022-06-02 13:18:38.803 W   ],
> 2022-06-02 13:18:38.803 W   "vout": [ {
> 2022-06-02 13:18:38.804 W       "amount": 0,
> 2022-06-02 13:18:38.805 W       "target": {
> 2022-06-02 13:18:38.805 W         "key": "d01859ff0e299746174dfecb4c146b4e2a4a70920820518c06c5e44b5fa98c3e"
> 2022-06-02 13:18:38.806 W       }
> 2022-06-02 13:18:38.806 W     }, {
> 2022-06-02 13:18:38.806 W       "amount": 0,
> 2022-06-02 13:18:38.807 W       "target": {
> 2022-06-02 13:18:38.807 W         "key": "da908b2ab4ace24a184cdaf1a9bbebc495dc3f5251dfbd18368ae026bb54ed7b"
> 2022-06-02 13:18:38.808 W       }
> 2022-06-02 13:18:38.808 W     }, {
> 2022-06-02 13:18:38.808 W       "amount": 0,
> 2022-06-02 13:18:38.809 W       "target": {
> 2022-06-02 13:18:38.809 W         "key": "c0babe2f7f328cbd8c888bd686542d4526a908fa01e700433a0fed1a364eb44b"
> 2022-06-02 13:18:38.810 W       }
> 2022-06-02 13:18:38.810 W     }
> 2022-06-02 13:18:38.811 W   ],
> 2022-06-02 13:18:38.811 W   "extra": [ 1, 40, 237, 138, 198, 97, 198, 149, 210, 226, 165, 67, 242, 92, 69, 181, 231, 145, 212, 215, 231, 12, 224, 41, 57, 214, 102, 157, 186, 35, 63, 125, 48, 4, 3, 32, 222, 209, 117, 97, 115, 5, 186, 173, 28, 86, 57, 26, 25, 60, 246, 199, 69, 45, 157, 55, 177, 32, 26, 218, 47, 152, 173, 130, 82, 253, 15, 17, 59, 166, 90, 77, 56, 36, 45, 7, 64, 222, 75, 18, 165, 24, 205, 54, 165, 49, 82, 165, 181, 65, 109, 2, 232, 235, 35, 56, 237, 89, 11, 92, 151, 152, 67, 169, 90, 141, 38, 135, 98, 138, 125, 167, 183, 92, 240, 185, 189, 239, 24, 93, 118, 170, 190, 182, 64, 57, 91, 165, 55, 115, 30
> 2022-06-02 13:18:38.813 W   ],
> 2022-06-02 13:18:38.814 W   "rct_signatures": {
> 2022-06-02 13:18:38.814 W     "type": 5,
> 2022-06-02 13:18:38.814 W     "txnFee": 400380000,
> 2022-06-02 13:18:38.815 W     "ecdhInfo": [ {
> 2022-06-02 13:18:38.815 W         "amount": "28dc547be5df8efc"
> 2022-06-02 13:18:38.816 W       }, {
> 2022-06-02 13:18:38.816 W         "amount": "5501bcabd73326e1"
> 2022-06-02 13:18:38.817 W       }, {
> 2022-06-02 13:18:38.817 W         "amount": "41afb73ae0333a3e"
> 2022-06-02 13:18:38.818 W       }],
> 2022-06-02 13:18:38.818 W     "outPk": [ "9bf3127d019298ee4c2ce17865679f45ed3b8ce1dabc5fa36fddb9ed1d6a8c01", "137aa737ddd63a36f0ccba35f436cca052058fc52624873e9bf02351a0643258", "2cf76ebea9f8e43310f54fc027d268868422f4a1bcde6007c95042c8106fcf29"]
> 2022-06-02 13:18:38.819 W   },
> 2022-06-02 13:18:38.819 W   "rctsig_prunable": {
> 2022-06-02 13:18:38.819 W     "nbp": 1,
> 2022-06-02 13:18:38.820 W     "bp": [ {
> 2022-06-02 13:18:38.820 W         "A": "7f5004d6fc92666f35c40d40d4077addbe92b34fe9b7c463da11adf9e1bc3a03",
> 2022-06-02 13:18:38.821 W         "S": "137338e4a655ae6db5b71a47e45772d8a3e2d20eddaabf4e2a93bb9245d4d134",
> 2022-06-02 13:18:38.821 W         "T1": "a440a317e990e404e81946a30d384f7b19990fc6e523502c9109ec6db771a7f9",
> 2022-06-02 13:18:38.822 W         "T2": "042d7b88b7e63d6bdce9ce16cd41092cc791f333e04fa19e46cf0d068763db92",
> 2022-06-02 13:18:38.822 W         "taux": "05d9bebfd71097ee0bdc5af44294df42b6127205d22af2b723c870edf4f8e608",
> 2022-06-02 13:18:38.822 W         "mu": "e546ab277ba2d16d1707a375a925ca87705c685c343dd6e5ff4693a7848e1a05",
> 2022-06-02 13:18:38.823 W         "L": [ "9cce454e746aba9894958b9d6ca3d4912414cd05e77e8b3ae7a2dce110e6f517", "d1be7fb8506473de7fed1cffb111b2250e2577f77623e104d5f6c27436c68a7f", "e9f68951ee3a63511f309f9677da9be7abde5989c3f9eff93725c09403660fea", "b560bbbdac05338cc25b286109d27bb8865b47a98b8c2e627a718c3c7dcdace0", "8b51969a667037a2e96f17a6e840fe12f30fde276197cddba08c93638245e808", "1cafe3b9d1e840c4304ea23847e8f5f94a6acc88fba0f9f95ab49512dcd28152", "6e876b6956df616f76072971fb0f76fd096e436ef646c8fa1bb1860f90d2b19a", "08c23944e5fabeae31ae08573379919385d1c557a704f6299ba43f9fb0e50217"
> 2022-06-02 13:18:38.823 W         ],
> 2022-06-02 13:18:38.824 W         "R": [ "99b3e52cbe564ce818cfeba7da769997cfe52732c867730e81bec32150a5880b", "37299f5856946f342161c947bbe1ae381e3a2fc8131cd22254a44ef5231e0a6c", "0709faf4a33864f1656ee004642372a4126397f6fab22b66dd70a42a3ad7b838", "59e706a72890940954ff0ec2b627c5aed21731d31121575abe2ed63589757520", "faed817cf8aa7b71924da9cb4fb12d92e4dc96d21d3c40d25452a0c40d6ad9ab", "813e72876609d6cedfb4cb24899864d1ad9f0b1f1b9bb4ad61edf93c3bc0c474", "c550c684bd0edea17870ee48c864912167d930ec65057e925a1972ee95776bf7", "371ee760f331d61fe2b804e52876ad0460fce9ff3d559674c7ea531f783bc206"
> 2022-06-02 13:18:38.824 W         ],
> 2022-06-02 13:18:38.824 W         "a": "de5e5f595d428e815b6483e94ac473f73f6ba7bac37f2c490b75c1204277f202",
> 2022-06-02 13:18:38.825 W         "b": "2e47f6a1f8b0a6468e4c5263d7bc6cd4d940cbd84407e39c597c29a2204dc20a",
> 2022-06-02 13:18:38.825 W         "t": "4f436190cacca9bb1c301f6bd9f4143dcfde272208c3892ad9d03f0c0e60f60d"
> 2022-06-02 13:18:38.826 W       }
> 2022-06-02 13:18:38.826 W     ],
> 2022-06-02 13:18:38.826 W     "CLSAGs": [ {
> 2022-06-02 13:18:38.829 W         "s": [ "e205bcbc04bb8fc507dd3cd1b77084e6489ea01ee58bda14463d5917a796d001", "e7c27ddbf2517b1c4796482e9233542ca3e34114d06c7ca74f6e86ecb2328000", "5f614600a4ac76269bb97345fe12ae4909b3a783792e0c2c5a83db960cad8a00", "7208162494ab1479178d64c68494cb6a14502cfa2d301e7c29672a42653eae09", "ca204291be6677034f0fe41cfcb40cc5c4b813837ea5c7e14a400a4558d67c07", "0c4461fd2a3a05f4937ce0ac7c7dc434b16c1c2d817109f71ca682cd1e68810b", "fce636ccf78e7780a41e2a7dfa195a17024b423698ab6de76df62523671c8d09", "6b6126d0769322c09000a63ccd7ac716731154099a611ff560861c426caf360d", "89419e629d0c1384380b5a4a89d50c50f81438b62c41fd2784d3f07078830009", "6354fd8561508515183748f95509aaa3d523c0e032e7e4f1b3dc25a9aec3be0a", "6b8341705ba0f46108b3409c678e6222d88a05b036f9e03e3077e0377b7eac0f"],
> 2022-06-02 13:18:38.830 W         "c1": "926350f899347d0d6f6ce746a18b6048eb4903a78bf7bbb2f2336186f3fd4d01",
> 2022-06-02 13:18:38.830 W         "D": "978b8201694900c794f9b783b23996b6ae8788f4c861e3473cebd9fc6e9ce747"
> 2022-06-02 13:18:38.830 W       }, {
> 2022-06-02 13:18:38.831 W         "s": [ "4c88bd3b0ac0b55e722df1a56b94ee88b5ffeb6446388453a220df9c766aa603", "fa5c7fff3ff9c3be300584ffd85b4d5b5a958e50941b1cd17ccc139a4c29e00b", "2601e034b6467a58a32c941ecb53cca52fb8d91147e8d33c3f73590203b48204", "1679b019927ce68c8b2cf043f5740f90af647ab5d2a2bda3057f8eb49be4830a", "1a560105251fe3e143604bee4e1eb97639f8b9771e29c18f66c1348135d93600", "5ea45ccaa8d0ef3034c4ff5b198b6392a55fac74b851101358b20a33e958470c", "06759e6f60dde9980d95eba75f328d97d30cd71cd932273b08d96a2070c2e30b", "e73777672bc27162c79d8ce6457de257bf206129fc2eebd1580e726fc3509005", "8dc7dcbb25b2cb707191022ecd65c7f041f7c1be2607c506d63e53236b654202", "10abc6cc90033d1f582c961569511d6594501a5bc652e08eb681b8e365073204", "fad67d2b6249bfc8a39a5a1a1574e7cd827703146cc78e664d6cc669d48f170c"],
> 2022-06-02 13:18:38.831 W         "c1": "ace5c436abfc456d282822853348baf1bf4eea811435f2548afcd3244a092c0b",
> 2022-06-02 13:18:38.832 W         "D": "9332c26ad6d8e5a471b1e0e068de53267999be5d314a5181058b26c406e73aa3"
> 2022-06-02 13:18:38.832 W       }],
> 2022-06-02 13:18:38.833 W     "pseudoOuts": [ "96edd69155bc6f59d6f4bd2a3a6fcf173f9ebdaf242e1ba4f77303ecc6acd56a", "a926dc69ca1093a37040189f634b080299838f6342b3622091d04d598627bcab"]
> 2022-06-02 13:18:38.833 W   }
> 2022-06-02 13:18:38.834 W } (double spend)

I've tried using multiple daemons and I get the same errors. The transaction is marked as "failed" if I try to retrieve the transfers in the wallet and I can only make the transfer by opening the wallet in the Monero GUI (I tried multiple times to do that).

Is it a bug or am I missing something out? 

# Discussion History
## j-berman | 2022-06-02T17:43:26+00:00
Is the daemon using the tor tx proxy/do you have logs from the daemon? It sounds like the daemon is failing to broadcast the tx to the rest of the network rather than an issue with the wallet RPC

Related: #8251, #6929, #6938 

## jekkodev | 2022-06-02T18:11:00+00:00
I do not own the daemon, but I had the same issue with other daemons under the tor network.

I try to connect to a clearnet node allowing every ssl certificate:
`monero-wallet-rpc --stagenet --rpc-bind-ip 127.0.0.1 --rpc-bind-port 38082 --wallet-dir /path/to/monero/wallets --daemon-address node2.sethforprivacy.com:38089 --proxy 127.0.0.1:9050 --disable-rpc-login --daemon-ssl-allow-any-cert --log-level=4`

I open the wallet and try to submit the same transaction:

`curl http://127.0.0.1:38082/json_rpc -d '{"method":"transfer","params":{"account_index":1,"destinations":[{"amount":695282695003,"address":"773b8zYQ52hVdXSwv4PW9HEiCBbttfjJY4HYG3SBLUVdNJEBe1Fi293JgwgdZsKzB3R7nAfGeZ4meNjrrMD2VPyZ3MdCr65"},{"amount":21515971701,"address":"79EnhaHfb6CeXPdK84uQiqMvsmEXP4ZLrHYHzKMdtu555a782wv54TSAqXerZWtExgjcpWcU6NTdxdbY7wJQQPqh9uVuVzy"}],"subaddr_indices":[1,2],"priority":2,"mixin":10,"ring_size":11,"unlock_time":0,"get_tx_key":true,"get_tx_hex":true,"do_not_relay":false},"jsonrpc":"2.0","id":"0"}'`

The transaction seems to be broadcasted, it has got a confirmation (e9ad6040afa907921a628fbe00f1d5ec47ac6535ffc9cf054a99bd55c7f319a0).

How can I prevent this to happen? Are tor nodes only affected?



## selsta | 2022-06-02T18:14:40+00:00
> Are tor nodes only affected?

No, but in general if you use a random Tor node we have no idea what daemon version they are running. They could be outdated for example and there aren't many stagenet Tor nodes in the first place.

> How can I prevent this to happen?

Run your own node or find a node that works for you. Tor itself isn't the problem.

## jekkodev | 2022-06-02T18:22:32+00:00
How can I prevent this to happen on my node? Should I always look for failed transactions and flush the tx pool in case that happens?

## selsta | 2022-06-02T18:24:44+00:00
If you run master branch there are some fixes to the daemon tx relay logic so that it shouldn't happen in the first place, as linked by @j-berman in his previous comment.

## gituser | 2025-09-01T15:02:20+00:00
This issue is still actual on the latest monero version `v0.18.4.2`.

I think this bug is either a race condition in `monero-wallet-rpc` or some sort of.

This bug only happens if in the network there is block reorganization is happening, e.g. something like this:
```
2025-08-21 21:33:54.116 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3482933
2025-08-21 21:33:54.116 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <45db51d7afa9f1616f6a3a9953eb64429f88ec206f0998cadb500037dff963ad>
2025-08-21 21:33:54.116 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <aea7540e650512fd729b9db9af51302eaf5b5246a295ea2acc54b80000000000>
2025-08-21 21:33:54.116 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     611393876150
2025-08-21 21:33:54.133 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3482934
2025-08-21 21:33:54.133 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <bd243ec4474fe0f696fc5876fe38047daa5cf34c410d07cee6fb8c1a9bc2d309>
2025-08-21 21:33:54.133 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <8ace71c839a07ee05d34a536d592ad0fef83c969d13bd8f2251a630100000000>
2025-08-21 21:33:54.133 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     612438615951
2025-08-21 21:33:54.150 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3482935
2025-08-21 21:33:54.150 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <ebfe42ccbadbca3760e9b0c2358c333100e14c9644d84d74983f9a0e8ca90004>
2025-08-21 21:33:54.150 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <4d5d6d7d63c621ea9e5ce119f665c6681b8e931147233df9dbba9e0100000000>
2025-08-21 21:33:54.150 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     612451820380
2025-08-21 21:33:54.167 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3482936
2025-08-21 21:33:54.167 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <7de6912be3aba6cd5864caa182b52c49300cb4666bdd08f6a50b5c38af78e2e3>
2025-08-21 21:33:54.167 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <2a29917442eb014a786438fe48c13e869b759c0978eecab8c4e0630100000000>
2025-08-21 21:33:54.167 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     611734783063
2025-08-21 21:33:54.183 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2099 ###### REORGANIZE on height: 3482933 of 3482936 with cum_difficulty 500788064685518903
2025-08-21 21:33:54.183 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2099  alternative blockchain size: 5 with cum_difficulty 500788676524240494
2025-08-21 21:33:55.485 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3482933
2025-08-21 21:33:55.485 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <d7be666a122542aa61d7bed9d8bc2e73adf1c30b61ce2b95c0e990f11b03f59f>
2025-08-21 21:33:55.485 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <2c8283c2747d4afda45cf8b49381d22ee021965146db1b24fbcc5d0000000000>
2025-08-21 21:33:55.485 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     611393876150
2025-08-21 21:33:55.535 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3482934
2025-08-21 21:33:55.535 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <f32c85324383d3d2f5ed4498e5f4d7cae42dab7f836e66ffa9eedc525f6f30cb>
2025-08-21 21:33:55.535 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <7befcf2a10a4c31819da995747ec48cfd6dc5e67af8f082bfd29e80000000000>
2025-08-21 21:33:55.535 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     612438615951
2025-08-21 21:33:55.574 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3482935
2025-08-21 21:33:55.574 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <034c7e93f879a0d6b7ac99701061cca2dce63f1394d3852f538e68fa59c99d12>
2025-08-21 21:33:55.574 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <549b4e1086e4574e8b5eee9c446c671d57f1c1ba407461e0c6ae6a0000000000>
2025-08-21 21:33:55.574 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     612451820380
2025-08-21 21:33:55.594 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3482936
2025-08-21 21:33:55.594 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 id:     <ca263e7bacd7ff310785fc81c49aa1cc5948fede1f09e56423782bd58eacf486>
2025-08-21 21:33:55.594 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 PoW:    <f192f30db8475f87db5e50fb288e03c5c0aaac52308c16c14d9e430100000000>
2025-08-21 21:33:55.594 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:2110 difficulty:     611734783063
2025-08-21 21:33:56.227 [P2P2]  INFO    global  src/cryptonote_core/blockchain.cpp:1217 REORGANIZE SUCCESS! on height: 3482933, new blockchain size: 3482938
2025-08-21 21:33:56.256 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1618    Synced 3482938/3482938
```

And if you send a transaction via `monero-wallet-rpc` when chain reorganization is happening `monero-wallet-rpc` will return to you `transaction_rejected` error.

Probably in the wallet code there should be some check for monerod status or something that daemon is fully synchronized and working fine prior to sending transaction.

ChatGPT as a workaround suggests to manually use `get_info` RPC call to `monerod` and check these 2 fields prior sending the transaction:
```
 "status": "OK",
    "synchronized": true,
```

Not sure if it would help, it might be still not enough if the reorg happens right after the check (race).

Could you please look at this issue @selsta @j-berman @jeffro256 @tobtoht.

Thanks.


## nahuhh | 2025-09-01T16:11:11+00:00
@gituser your issue is different.

OPs issue is that the node did not bradcast the tx to the network. A node issue. If there is a wallet issue, its that the tx WAS broadcast to the node, but incorrectly claimed that it was not. Rejected for a doublespend (trying to spend an output that is already in the txpool)
Possibly related: [#10032](https://github.com/monero-project/monero/issues/10032)

Your issue is unknown without knowing the reason for the rejection.

If your error was also a double spend, the error is _presumably_ because you had spends already in the some of the confirmed blocks that, when node reorged, had txs pushed from blocks -> mempool. When your _wallet_ reorged, it did not see the txs re-enter the mempool, and tried to spend them again.
Possibly related: [#10013](https://github.com/monero-project/monero/issues/10013)



## gituser | 2025-09-01T19:04:32+00:00
@nahuhh 
> [@gituser](https://github.com/gituser) your issue is different.
> 
> OPs issue is that the node did not bradcast the tx to the network. A node issue. If there is a wallet issue, its that the tx WAS broadcast to the node, but incorrectly claimed that it was not. Rejected for a doublespend (trying to spend an output that is already in the txpool) Possibly related: [#10032](https://github.com/monero-project/monero/issues/10032)

I've checked logs an I see this:

```
2025-08-25 19:00:12.918 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:7578     daemon_send_resp.status != CORE_RPC_STATUS_OK. THROW EXCEPTION: error::tx_rejected
2025-08-25 19:00:12.919 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:996  /home/build/monero/source/src/wallet/wallet2.cpp:7578:N5tools5error11tx_rejectedE: transaction was rejected by daemon, status = Failed, tx:
```

After some other logs (related to outputs etc) there is:

```
2025-08-25 19:00:12.919 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:996  } (double spend)
2025-08-25 19:00:12.919 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:134  Exception: tools::error::tx_rejected
2025-08-25 19:00:12.919 [RPC0]  INFO    stacktrace      src/common/stack_trace.cpp:135  Unwound call stack:
```

Not sure if this is #10032 or not.

> 
> Your issue is unknown without knowing the reason for the rejection.
> 
> If your error was also a double spend, the error is _presumably_ because you had spends already in the some of the confirmed blocks that, when node reorged, had txs pushed from blocks -> mempool. When your _wallet_ reorged, it did not see the txs re-enter the mempool, and tried to spend them again. Possibly related: [#10013](https://github.com/monero-project/monero/issues/10013)

Also could be this issue.

Is there any 100% workaround for the issue I'm having? I can open a separate issue if it will help fixing it.

## nahuhh | 2025-09-01T21:54:42+00:00
The issue is, imo, likely to be #10013 if its caused by a reorg.
wallets unaware of spends in the txpool, if they were put there by another wallet (or in this case, by a reorg).

The reorgs DO mess up wallet history, dropping tx details.

10013's behavior is reproducible. Hasn't been checked against reorg behavior though.

# Action History
- Created by: jekkodev | 2022-06-02T13:54:27+00:00
