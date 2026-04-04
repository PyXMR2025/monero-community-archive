---
title: wallet-cli can't sign transfer without daemon
source_url: https://github.com/monero-project/monero/issues/5275
author: xnum
assignees: []
labels: []
created_at: '2019-03-13T06:39:50+00:00'
updated_at: '2019-04-16T22:25:34+00:00'
type: issue
status: closed
closed_at: '2019-04-16T22:25:34+00:00'
---

# Original Description
After recent software upgrade, I stuck at signing transfer operation:

The last output in stdin is

```
Loaded 1 transactions, for ???.000000000, fee 0.000053030000, sending ????.0000 to 84xxxxx, 0.418239360000 change to 43xx, with min ring size 11, dummy encrypted payment ID. 98 outputs to import. Is this okay? (Y/Yes/N/No): 
```

After I typed Yes, it won't complete this operation.

I also added `--log-level=1` option and it shows `sign transfer failed: no daemon` ...etc
but I want to sign transfer offline, is it must be connected to a daemon?

# Discussion History
## moneromooo-monero | 2019-03-13T09:21:20+00:00
Signing offline should not require a daemon. If something broke here, it will be fixed.

## moneromooo-monero | 2019-03-13T11:33:50+00:00
https://github.com/monero-project/monero/pull/5277

## MoneroChan | 2019-03-23T07:38:17+00:00
UPDATE. @moneromooo-monero @xnum

**WORKAROUND SOLUTION FOUND**

-  Running daemon offline can trick the CLI / GUI to sign file.
-  You have to disable all firewalls and enable loopback adapter on your cold signing computer if it is locked down.


## xnum | 2019-03-23T07:53:58+00:00
Thanks for notices me this workaround, but we can't run a daemon in inner service network on production due to our signing restriction policy. Keep waiting for the patch merged from contributor.


## MoneroChan | 2019-03-23T08:01:11+00:00
UPDATE: @xnum @moneromooo-monero

**Actually the problem may go deeper**
-  I just tried using this workaround.  It WILL Sign the transaction successfully with Daemon running without internet, but when you try to submit it on the hot computer connected to internet, it will be rejected by Reason: "Invalid Output" or "Fee too low"  (one of the above 2)

@moneromooo-monero  - Could this be a deeper problem? 

## moneromooo-monero | 2019-03-23T14:55:38+00:00
If you can reproduce this, please post a log of daemon, hot wallet and cold wallet, all with --log-level 2.
The wallet info will contain private info (no secret keys, but which outputs you own), so if it's a mainnet wallet and you want that info kept private, feel free to encrypt the logs with my public key in utils/gpg_keys.

## moneromooo-monero | 2019-03-23T16:31:15+00:00
BTW you're on recent enough master, right ? If on 0.14.0.x, this is old code and it may well have been fixed in master a while ago.

## xnum | 2019-03-23T16:51:57+00:00
I am trying to reproduce this on testnet but it has another problem so still it my wip list.

Not sure which commit hash we're using, version returns from built docker image is

```
Monero 'Boron Butterfly' (v0.14.0.0-release)
```

And this image was built at Feb 25 on branch release-v0.13. Will we fix this issue by building latest v0.13 branch or must be master?

## moneromooo-monero | 2019-03-23T18:06:12+00:00
You really want 0.14.0.2 if you can.
The bug is not fixed in master. The PR was not merged yet. You can apply it on top of either 0.14.0.2 or master.

## moneromooo-monero | 2019-03-24T21:10:12+00:00
The patch is now merged.

## dnaleor | 2019-04-01T16:23:17+00:00
> I just tried using this workaround. It WILL Sign the transaction successfully with Daemon running without internet, but when you try to submit it on the hot computer connected to internet, it will be rejected by Reason: "Invalid Output" or "Fee too low" (one of the above 2)

Just had the same issue: first the fee error, then the invalid output error after adjusting the fee. 
Just checking, the patch fixes this?

If next release doesn't happen anytime soon, I guess I'll compile myself, like a true Monerano :)

## xnum | 2019-04-09T09:21:20+00:00
I got fee too low at testnet too.

daemon response:

```
{
  "double_spend": false,
  "fee_too_low": true,
  "invalid_input": false,
  "invalid_output": false,
  "low_mixin": false,
  "not_rct": false,
  "not_relayed": false,
  "overspend": false,
  "reason": "fee too low",
  "status": "Failed",
  "too_big": false,
  "untrusted": false
}
```

here is cold signing log. It connects to an offline mode daemon without any blockchain data.

```
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Boron Butterfly' (v0.14.0.2-8039b8d9)
2019-04-09 09:15:53.804     7f2a8385cd10        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:207  Setting log level = 1
2019-04-09 09:15:53.804     7f2a8385cd10        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:210  Logging to: /root/rpc-21254.log
Logging to /root/rpc-21254.log
2019-04-09 09:15:53.804     7f2a8385cd10        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3402   Loading wallet...                                               2019-04-09 09:15:53.805     7f2a8385cd10        INFO    wallet.wallet2  src/wallet/wallet2.cpp:6312     ringdb path set to /root/.shared-ringdb/testnet                         2019-04-09 09:15:53.920     7f2a8385cd10        INFO    wallet.wallet2  src/wallet/wallet2.cpp:6336     caching ringdb key
2019-04-09 09:15:53.948     7f2a8385cd10        WARN    wallet.wallet2  src/wallet/wallet2.cpp:4593     Loaded wallet keys file, with public address: 9xttFdWis9x5BbDj24X2YLHVYB4DTsdic25SHpRFGSvKeLS2tZ1xL3eAgZYLYMqnr213b4jVy7huzQhM7gL7YGG67cTddJg
2019-04-09 09:15:53.948     7f2a8385cd10        INFO    wallet.wallet2  src/wallet/wallet2.cpp:4615     Trying to decrypt cache data
2019-04-09 09:15:53.997     7f2a8385cd10        INFO    wallet.wallet2  src/wallet/wallet2.cpp:6476     Found and saved rings for 0 transactions                                2019-04-09 09:15:54.175     7f2a8385cd10        INFO    wallet.wallet2  src/wallet/wallet2.cpp:2791     Refresh done, blocks received: 0, balance (all accounts): 0.000000000000
, unlocked: 0.000000000000
2019-04-09 09:15:54.175     7f2a8385cd10        INFO    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3441   Successfully loaded                                             2019-04-09 09:15:54.175     7f2a8385cd10        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:917   Set server type to: 1 from name: RPC, prefix_name = RPC
2019-04-09 09:15:54.175     7f2a8385cd10        INFO    global  contrib/epee/include/net/http_server_impl_base.h:76     Binding on 127.0.0.1:21254
2019-04-09 09:15:54.176     7f2a8385cd10        WARN    wallet.rpc      src/wallet/wallet_rpc_server.cpp:3455   Starting wallet RPC server                                      2019-04-09 09:15:54.176     7f2a8385cd10        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:89     Run net_service loop( 1 threads)...
2019-04-09 09:16:02.889 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5538     Loaded tx unsigned data from binary: 1 transactions
2019-04-09 09:16:02.890 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:5566      1: 2 inputs, ring size 11                                                              2019-04-09 09:16:03.014 [RPC0]  INFO    default src/cryptonote_core/cryptonote_tx_utils.cpp:256 Encrypted payment ID: <1c2a96b1d9784324>
2019-04-09 09:16:03.016 [RPC0]  INFO    perf    src/common/perf_timer.cpp:111   PERF             ----------
2019-04-09 09:16:03.016 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF      263    PROVE_v
2019-04-09 09:16:03.266 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:170  Hi/Gi cache size: 64 kB
2019-04-09 09:16:03.266 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:171  Hi_p3/Gi_p3 cache size: 320 kB
2019-04-09 09:16:03.266 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:172  Straus cache size: 300 kB
2019-04-09 09:16:03.266 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:173  Pippenger cache size: 320 kB
2019-04-09 09:16:03.266 [RPC0]  INFO    bulletproofs    src/ringct/bulletproofs.cc:175  Total cache size: 1004kB
2019-04-09 09:16:03.268 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF      762      PROVE_v
2019-04-09 09:16:03.268 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF       36      PROVE_aLaR
2019-04-09 09:16:03.281 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF    13624      PROVE_step1
2019-04-09 09:16:03.283 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF     1277      PROVE_step2
2019-04-09 09:16:03.364 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF    81267      PROVE_step3
2019-04-09 09:16:03.678 [RPC0]  INFO    perf    src/common/perf_timer.cpp:140   PERF   314436      PROVE_step4
2019-04-09 09:16:03.744 [RPC0]  INFO    construct_tx    src/cryptonote_core/cryptonote_tx_utils.cpp:596 transaction_created: <3ad0df0f83549e2f68803b6df199bdd768b501857045114bca
bf3519b9e475d5>
{
  "version": 2,
  "unlock_time": 0,
  "vin": [ {      "key": {
        "amount": 0,
        "key_offsets": [ 322961, 78423, 50511, 6212, 16442, 9918, 42, 20, 551, 40, 105                                                                                                  ],
        "k_image": "c0011cb57649f6eb184cc0550fedaee864c1f66198bcfe78618c6515592b8a0d"
      }
    }, {
      "key": {
        "amount": 0,
        "key_offsets": [ 408666, 67704, 2700, 4282, 56, 1103, 660, 4, 25, 39, 19
        ],
        "k_image": "3d3228640f7bbe954906cab26570f133f88bb3a0b47bb9bf1c9409bc4b301c4a"                                                                                                 }                                                                                                                                                                             }
  ],                                                                                                                                                                              "vout": [ {
      "amount": 0,
      "target": {                                                                                                                                                                       "key": "171dee459febb29a2a04e66514702f0376ed8146a6808ff925d74b5004ae8c76"
      }
    }, {                                                                                                                                                                              "amount": 0,
      "target": {
        "key": "fea3449a4aae928d6cf28c384fec3292ee0a2a66bd787ff7634c1e4155253733"                                                                                                     }
    }
  ],                                                                                                                                                                              "extra": [ 2, 9, 1, 28, 42, 150, 177, 217, 120, 67, 36, 1, 63, 40, 111, 152, 54, 186, 5, 219, 112, 144, 195, 73, 35, 211, 141, 247, 13, 112, 99, 74, 242, 188, 162, 240, 221,
95, 151, 25, 46, 209, 166, 24
  ],
  "rct_signatures": {
    "type": 3,
    "txnFee": 114680000,
    "ecdhInfo": [ {
        "mask": "ffda752903bf830c108f7feced7b8b3ae5e017b74d828f8b7603155ab094ef01",
        "amount": "aaa6baaf9573ca85967e6bba2a198a0a3ee792afa9ae9f3bc3aa4a6895294d0b"
      }, {
        "mask": "75747ac717e485c05e6b468ae3419cecebc510d09b26dd6767017a3bf13fac09",
        "amount": "b1cc905d4b892bd4c6803ef339e5c7539238ad851ef0eb6f843f61d8cfbebf09"
      }],
    "outPk": [ "f6dbefa549aad526d497dc2440c5b26ec250fa00622581a4834ead7788276fc5", "3245ddabc69710e07b41fbc2c7ab010a6f9cd8b2788e2b59b3075d850e98eb0e"]
  },
  "rctsig_prunable": {
    "nbp": 1,
    "bp": [ {
        "A": "18b7487703bc30c98509cdd68df8b97c4946830d4a2bf7454d6d4ffe573a3115",
        "S": "3da20602b0037d31073c1fe173729dacf2d3bb9e47a585f3116068c270ac702e",
        "T1": "6847810905efc7fde462617a10f41dc5a6319474abd4bed799bf1930813b0fb6",
        "T2": "699d22565d06ddfdd795ebded022dee0b34237d451d518c44b4b81962f5dc3f4",
        "taux": "8f71d6fc1d9475fbb8f42463c3ee906006d4283098b52e6b02e27e1f4b30f60d",                                                                                                     "mu": "df5f430aed8ead7c1136819baab3c4724629c76160da8395f8641b6fbed1ae0e",
        "L": [ "f48c6037fc8565e4e8170931a4390f89b40d9578582bce8a591a6012529f3f64", "73685113fd77f443d1dfa7bbeb5f5b7be1fefdb8ca0656441a80a312525213c6", "b40d3a6978197f31d5370317
d22b84b24db611dd53dd2f03aab319ddc13f179c", "86a7f762796f64ef89fc7dc0b550fac8aebbd2d826ae29d56321665213ec7e59", "b3e5f7aca920193d7dfc45cb8dfbe41702e62a8b6d11e44b21f764d7e4f7a1ee
", "236b831ba1ec6ae7f4bf84df99a9e13b67b9509c80986d54efce86c6f2b6835c", "bd777b7802e1ea420f3d8339b810c5bce154d7dd6a425ba17bd55a4381979772"
        ],
        "R": [ "99f6e05a3ca17a7eb8c323003875686ce3c599762d14822125f6821baf7ef183", "4b62fbc1c929ad21f60a5081234debbe00976aa6b6f64979b8e7e0d283b7da20", "4927b49f7ed78900792c0143
ddeae2cd3564981c5a6008171ec2583cf18222ec", "e9e17d3f50d484f5aaeec1aee95cd552315f70c6e66302279105704dfbc379b1", "d11631f1f39da7f84a7f963a48d018c9161f0c3f15666d62e49b243a65aad2a5
", "bbe9cc4652519dbfb5f03869748864b5834cc5df8bc69652056454385b9e8c56", "3cfcf31d9a91663cab54736427d5ab576c00804019f1a0f3d64cdd95434f4a26"
        ],                                                                                                                                                                              "a": "ad1c899afabdab369003e17ced97355eabcb261f62934d37358eff5a722f5106",                                                                                                        "b": "be991bdb97209baa23cfe5ed1c566fe9c1726b484f43a2cef1183830e6da2c05",
        "t": "2a1b4296ab74e48f9df6a07f7473f387b6e7d1d9b4da4b82be7629745053a902"                                                                                                       }
    ],
    "MGs": [ {                                                                                                                                                                          "ss": [ [ "791fbf4a55c97f52a168a046f6ed4c0491b99d405f3337951bae86bdc07eac08", "4d1113a141dfe06728adc1cd248c5c4666c1c7a48027349dae0ce20c3ac1c107"], [ "738de16529e1c127b6
c2087131e37d1e392d511d8ad3a1126502b62ae46c2a0b", "1147a4725db01063af94681d2f205ede9805ac06c2237d8f5a5b849cd0a24b0d"], [ "71ac173975a601b9ac255df3d75afc8768f90f7b74d79a9026caed1
070b33102", "80cf988f0a506663943b71753a2637797f8205f63cecf1bb5ca6e9b0a02eca04"], [ "b6370dfd9b8c986307d936edfcc3d0f51e89e149662cd79780cd20a004ea8c06", "34212e37355efd1621b3d8115abb333ea18c487e3b85f53b26d994a0f6ba2803"], [ "92d667493db06b37fee251d5bc4a4a98b00bd194e12a99d726d32e226c71e406", "9d9a482c3f44a19ca1d27fdae21c0292523a64d3570ba8ec550f95808612b
c03"], [ "5b49ac02c8f82d6c9055bbde2f39571dff6234e5a00b316bb92a7ed1a3af4f01", "46f50b282ed59519fd02536f0a8f9da699e7ef90748ab7acdab7ad021a5b3a0a"], [ "022427ff95918d33a0fc67a860d
690d18ad0d0a9c40a87ecd8e1258205f53903", "d58fd6c8f4118d767609071ac5bf617c8df678eb4eb4bb32312b82f301eda005"], [ "b47a82b4bb4cbdb321e86cd79461bbec939b2927d1b04091a5d77a5e59de4c09", "2f60d96daec90d0ea578adf8121d77ae8650c172177d82a51821208decf6f406"], [ "e19385367fb0f8084dbf7f7959c16b0c13afaa5029927b78026426dd57ac8b0e", "df58ad847402d69ed3a8f4b3036a5d281
e14fceb1d36a21b1b870d4c06a6d60a"], [ "19d19e4d9841f529f7d98e82b3c89dc652c20112ab995412d2ccaf4b884f4904", "b0f0a250610f77ad9538ee6eea679973bde25d6c43e4ded838c0a96ce0da050e"], [
"839ed5d49ab083948c0795a650b3fca396be62f6958c7c41207c260d280eeb05", "16010ea2a39dd6e55d94544c56c3261a816ee61edef63989c890439921d21907"]],                                               "cc": "990fd53634d31b21f3a7e7e273181af05e06bdbe1ba894422ee1f7ce2cd48605"
      }, {
        "ss": [ [ "09b36f66ddaeb90ca21a06e42594eee4b08108a2b9309a72cd3784daa3797b07", "d0368c1aa0f4d2b9a5c475cc66790c22934c8adf6ee87bf87962db17a9251401"], [ "56920317320051020d
2fd31a07c265f33648117d2573c55d33beea95ded3590f", "fce79d2e11b37d2f48c12c2ea80789dadc2b246b6b78c7a9f6792736be68b10e"], [ "124a9647353fbc568733ab1c2ec833d6d356546fdc6b3739164c66b
250386f04", "b66e6f8210d231978e79429baf4e3883f6601fedfba1faf23f846bafa28b3809"], [ "64206212c21668bcaa467dc83347016999cc3ad07c94fa27aea8b0a3fefc6b06", "2ed93033c19b17a20f8ffd8b
92129d73fa077b4b723b548fc872840fd3609906"], [ "f1f74a5b83f17aea0d0ee62cd8e7b5800453aa4fc78656fd4211cc297325c006", "be82d1972bfcd07c1a729204aaa07aa6c392dc5f0920232e3e1bc62695df0
40b"], [ "671b87c25f26d4a903677c4ca32885922161dc6b0d38d9dd092c7e8ea185d304", "64ffb10a5ddf09ec75166997bfc6e167337e6abddfc2b8ee461a5bbed6fa390b"], [ "e84443c2ff876bdcfc0ecc3039e
a9e03a38e32f7d1e7d7cddb6b5c3d7d1d8b0d", "22185534c35e675fca2818e8959f2620aad38a2bf48af08b5077c59bce02cf06"], [ "d7fc7270e267f86ac35f2db45a05e7d9eccae2878b77599b07d7f3dc5b519703
", "a52e081c86cffbc886a4c53adb156c519d5498045b97b0dc439c22f045359b04"], [ "c77211bf7c512843a036918a301cfe1bdd78b4bb1937265e3cf1410a0405010d", "ae8768b6313b92c71b28023ef38c9002f
2b6f294671423d08f26f753960d190e"], [ "96561afc98fc965366b3c282b7b629afeb8173817bd78483de1a078b75355b00", "60151ae3331ed7d72be003da467754b6df51ebc18422a831425b62d8664ec507"], [
"1383aea2ee0ab78229da1a13fe7d7814e8e112fcb1ac2daa5d7cfe3d6f96ae0a", "286cc1a0967d739e6cac2016794843aa3226c8759c73f20acb148adab89d6008"]],
        "cc": "0bda96a7546a683d9fac8acdbcd4f98b0c8c4b1757cd050c290a3afb84f0840d"
      }],
    "pseudoOuts": [ "5c3bd5f70d0e1f4ad35e690b5e22cee6be976158a7b390b6acbe602a1832b9dc", "27f0975d40a71161751808555ba998ba9505e21714b9d85beb2fb3e93126951a"]
  }
}

```

## moneromooo-monero | 2019-04-09T14:07:53+00:00
Is this with the fix in ?

## xnum | 2019-04-09T14:15:05+00:00
Sorry, I did this experiment on `'Boron Butterfly' (v0.14.0.2-8039b8d9)`. I will compiling master branch and test again.

## xnum | 2019-04-10T03:31:20+00:00
Update: cli cold signing approach shows the same result when importing at master branch, its output is

```
Error: Failed to import outputs /tmp/xmr-10268665938960487708/outs: Failed to import outputsImported outputs omit more outputs that we know of
[wallet 9xttFd]:
```

but if I imports back to read-only wallet, it returns successful result.

---

I tried again at `v0.14.1.0-5dbcceb6`. When I imported output, it returns error, but it was working on v0.14.0.2 before.

request payload:

```
{"jsonrpc":"2.0","method":"import_outputs","params":{"outputs_data_hex":"4d6f6e65726f206f75747
07574206578706f7274040dbcd35a6e8076ddc27c7991a8ad91371d92172d84a88f40a33242b2ce8cc36ebce44d101eb5cc7d0fc728cb99e6ce6c03d68d2cf6b45550a338113bef1ca63b36e387f2e03033e79d2a96696794feb764253bc63735b4298de5310fc62c82c2f41c87bb61a8c537caf76b8628bda8cd1419074ca9992d0e46357fa43254a393b1005f628b6a52be59f903940322985eb6c6c54fe1404ee4fe8a8f181bb9d8ed4e53db4505ad13c19f3101"}
```

response:

```
{
        "error": {
                "code": -1,
                "message": "Failed to import outputsImported outputs omit more outputs that we know of"
        },
        "id": "1",
        "jsonrpc": "2.0"
}
```
information below may be helpful for debugging.

viewkey pair:

```
secret: 804adf53a5c456b3367bf44961c0cd078994c686a24d048dcb9b48a109bad400
public: 3627d5e81b311d39e2aa9543373bcf004446666ac64b918daabcd1e33d4f5f3a
```

transfers from wallet-rpc's response, only 3 transfers and all are incoming ones.

```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "in": [{
      "address": "9xttFdWis9x5BbDj24X2YLHVYB4DTsdic25SHpRFGSvKeLS2tZ1xL3eAgZYLYMqnr213b4jVy7huzQhM7gL7YGG67cTddJg",
      "amount": 100000000000,
      "confirmations": 1425,
      "double_spend_seen": false,
      "fee": 78240000,
      "height": 1185305,
      "note": "",
      "payment_id": "0000000000000000",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 1,
      "timestamp": 1554705695,
      "txid": "374bef9384cdb2a8ee0caa6137afd1e5a938b0e75a9799a5a45d23c622119e7f",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "9xttFdWis9x5BbDj24X2YLHVYB4DTsdic25SHpRFGSvKeLS2tZ1xL3eAgZYLYMqnr213b4jVy7huzQhM7gL7YGG67cTddJg",
      "amount": 100000000000,
      "confirmations": 1392,
      "double_spend_seen": false,
      "fee": 79300000,
      "height": 1185338,
      "note": "",
      "payment_id": "89ccbf029c8595f9cbb638fcc58dbd76ddac19b555bbb0907f7646bc16388587",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 1,
      "timestamp": 1554710663,
      "txid": "cad004b36f6fcf7fe043e8444ce0d608e3c9d4586a86ff408750feefd1b42345",
      "type": "in",
      "unlock_time": 0
    },{
      "address": "9xttFdWis9x5BbDj24X2YLHVYB4DTsdic25SHpRFGSvKeLS2tZ1xL3eAgZYLYMqnr213b4jVy7huzQhM7gL7YGG67cTddJg",
      "amount": 10000000000000,
      "confirmations": 752,
      "double_spend_seen": false,
      "fee": 79340000,
      "height": 1185978,
      "note": "",
      "payment_id": "89ccbf029c8595f9cbb638fcc58dbd76ddac19b555bbb0907f7646bc16388587",
      "subaddr_index": {
        "major": 0,
        "minor": 0
      },
      "subaddr_indices": [{
        "major": 0,
        "minor": 0
      }],
      "suggested_confirmations_threshold": 2,
      "timestamp": 1554784209,
      "txid": "46fe6be64b537917660db75e9ef90406e7aa42faca27dc53efa05b92c67a3b6b",
      "type": "in",
      "unlock_time": 0
    }]
  }
}
```

cold wallet log

```
Monero 'Boron Butterfly' (v0.14.1.0-5dbcceb6)
2019-04-10 03:25:12.696     7f9a5b177b70        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:207  Setting log level = 2
2019-04-10 03:25:12.696     7f9a5b177b70        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:210  Logging to: /root/rpc-37536.log
Logging to /root/rpc-37536.log
2019-04-10 03:25:12.697     7f9a5b177b70        WARNING wallet.rpc      src/wallet/wallet_rpc_server.cpp:4144   Loading wallet...
2019-04-10 03:25:12.697     7f9a5b177b70        INFO    wallet.wallet2  src/wallet/wallet2.cpp:1168     setting daemon to http://127.0.0.1:28081
2019-04-10 03:25:12.707     7f9a5b177b70        INFO    global  contrib/epee/src/net_ssl.cpp:90 Generating SSL certificate
2019-04-10 03:25:14.907     7f9a5b177b70        INFO    wallet.wallet2  src/wallet/wallet2.cpp:6934     ringdb path set to /root/.shared-ringdb/testnet
2019-04-10 03:25:14.952     7f9a5b177b70        INFO    global  contrib/epee/src/net_ssl.cpp:90 Generating SSL certificate
2019-04-10 03:25:16.322     7f9a5b177b70        INFO    wallet.wallet2  src/wallet/wallet2.cpp:6958     caching ringdb key
2019-04-10 03:25:16.351     7f9a5b177b70        WARNING wallet.wallet2  src/wallet/wallet2.cpp:5126     Loaded wallet keys file, with public address: 9xttFdWis9x5BbDj24X2YLHVYB
4DTsdic25SHpRFGSvKeLS2tZ1xL3eAgZYLYMqnr213b4jVy7huzQhM7gL7YGG67cTddJg
2019-04-10 03:25:16.352     7f9a5b177b70        INFO    wallet.wallet2  src/wallet/wallet2.cpp:5148     Trying to decrypt cache data
2019-04-10 03:25:16.400     7f9a5b177b70        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7057     Finding and saving rings...
2019-04-10 03:25:16.400     7f9a5b177b70        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:7069     Found 0 transactions
2019-04-10 03:25:16.400     7f9a5b177b70        INFO    wallet.wallet2  src/wallet/wallet2.cpp:7108     Found and saved rings for 0 transactions
2019-04-10 03:25:16.400     7f9a5b177b70        ERROR   wallet.mms      src/wallet/message_store.cpp:735        No message store file found: /tmp/xmr-10405730166344798999/xmr.k
eys.mms
2019-04-10 03:25:16.400     7f9a5b177b70        DEBUG   net.http        contrib/epee/include/net/http_client.h:381      Reconnecting...
2019-04-10 03:25:16.449     7f9a5b177b70        DEBUG   net.ssl contrib/epee/src/net_ssl.cpp:338        SSL handshake success
2019-04-10 03:25:16.450     7f9a5b177b70        DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:2542     Block is already in blockchain: 48ca7cd3c8de5b6a4d53d2861fbdaedca1415535
59f9be9520068053cda8430b
2019-04-10 03:25:16.451     7f9a5b177b70        INFO    wallet.wallet2  src/wallet/wallet2.cpp:3182     Refresh done, blocks received: 0, balance (all accounts): 0.000000000000
, unlocked: 0.000000000000
2019-04-10 03:25:16.452     7f9a5b177b70        INFO    wallet.rpc      src/wallet/wallet_rpc_server.cpp:4183   Successfully loaded
2019-04-10 03:25:16.452     7f9a5b177b70        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:1034  Set server type to: 1 from name: RPC, prefix_name = RPC
2019-04-10 03:25:16.452     7f9a5b177b70        INFO    global  contrib/epee/include/net/http_server_impl_base.h:82     Binding on 127.0.0.1:37536
2019-04-10 03:25:16.466     7f9a5b177b70        INFO    global  contrib/epee/src/net_ssl.cpp:90 Generating SSL certificate
2019-04-10 03:25:16.601     7f9a5b177b70        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:962   start accept
2019-04-10 03:25:16.602     7f9a5b177b70        DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:144       Spawned connection #0 to 0.0.0.0 currently we have socke
ts count:1
2019-04-10 03:25:16.602     7f9a5b177b70        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:107   test, connection constructor set m_connection_type=1
2019-04-10 03:25:16.602     7f9a5b177b70        WARNING wallet.rpc      src/wallet/wallet_rpc_server.cpp:4197   Starting wallet RPC server
2019-04-10 03:25:16.602     7f9a5b177b70        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:95     Run net_service loop( 1 threads)...
2019-04-10 03:25:16.602 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1060  Run server thread name: RPC
2019-04-10 03:25:16.602 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1067  JOINING all threads
2019-04-10 03:25:17.604 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:2542     Block is already in blockchain: 48ca7cd3c8de5b6a4d53d2861fbdaedca141553559f9be9520068053
cda8430b
2019-04-10 03:25:17.639 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:3182     Refresh done, blocks received: 0, balance (all accounts): 0.000000000000, unlocked: 0.00
0000000000
2019-04-10 03:25:21.681 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1151  handle_accept
2019-04-10 03:25:21.681 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1164  New server for RPC connections, SSL autodetection
2019-04-10 03:25:21.682 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:880   set m_connection_type = RPC
2019-04-10 03:25:21.682 [RPC0]  DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:144       Spawned connection #1 to 0.0.0.0 currently we have sockets count:2
2019-04-10 03:25:21.682 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:107   test, connection constructor set m_connection_type=1
2019-04-10 03:25:21.738 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:316    connection type RPC 127.0.0.1:37536 <--> 127.0.0.1:35390 (via 127.0.0.1
:35390)
2019-04-10 03:25:21.738 [RPC0]  DEBUG   net.ssl contrib/epee/src/net_ssl.cpp:229        SSL detection buffer, 627 bytes: 80 79 83 84 32 47 106 115 111
2019-04-10 03:25:21.738 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:448   That does not look like SSL
2019-04-10 03:25:21.739 [RPC0]  INFO    wallet.rpc      src/wallet/wallet_rpc_server.h:67       HTTP [127.0.0.1] POST /json_rpc
2019-04-10 03:25:21.739 [RPC0]  INFO    wallet.rpc      src/wallet/wallet_rpc_server.h:123      [127.0.0.1:35390 INC] Calling RPC method import_outputs
2019-04-10 03:25:21.775 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:11978    outputs.first > m_transfers.size(). THROW EXCEPTION: error::wallet_internal_error
2019-04-10 03:25:21.775 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:873  /root/monero/src/wallet/wallet2.cpp:11978:N5tools5error21wallet_internal_errorE: Importe
d outputs omit more outputs that we know of
2019-04-10 03:25:21.787 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:12095    THROW EXCEPTION: error::wallet_internal_error
2019-04-10 03:25:21.787 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:873  /root/monero/src/wallet/wallet2.cpp:12095:N5tools5error21wallet_internal_errorE: Failed
to import outputsImported outputs omit more outputs that we know of
2019-04-10 03:25:21.788 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:667   do_send_chunk() NOW SENSD: packet=154 B
2019-04-10 03:25:21.788 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:652   do_send_chunk() NOW just queues: packet=168 B, is added to queue-size=2
2019-04-10 03:25:21.788 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:855   handle_write() NOW SENDS: packet=168 B, from  queue size=1
```

read-only wallet log

```
Monero 'Boron Butterfly' (v0.14.1.0-5dbcceb6)
2019-04-10 02:51:40.103     7f325983bb70        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:207  Setting log level = 2
2019-04-10 02:51:40.103     7f325983bb70        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:210  Logging to: monero-wallet-rpc.log
Logging to monero-wallet-rpc.log
2019-04-10 02:51:40.107     7f325983bb70        INFO    net     contrib/epee/include/net/abstract_tcp_server2.inl:1034  Set server type to: 1 from name: RPC, prefix_name = RPC 2019-04-10 02:51:40.108     7f325983bb70        INFO    global  contrib/epee/include/net/http_server_impl_base.h:82     Binding on 0.0.0.0:18079
2019-04-10 02:51:40.118     7f325983bb70        INFO    global  contrib/epee/src/net_ssl.cpp:90 Generating SSL certificate
2019-04-10 02:51:40.531     7f325983bb70        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:962   start accept
2019-04-10 02:51:40.532     7f325983bb70        DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:144       Spawned connection #0 to 0.0.0.0 currently we have socke
ts count:1
2019-04-10 02:51:40.532     7f325983bb70        DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:107   test, connection constructor set m_connection_type=1
2019-04-10 02:51:40.532     7f325983bb70        WARNING wallet.rpc      src/wallet/wallet_rpc_server.cpp:4197   Starting wallet RPC server
2019-04-10 02:51:40.532     7f325983bb70        INFO    net.http        contrib/epee/include/net/http_server_impl_base.h:95     Run net_service loop( 1 threads)...
2019-04-10 02:51:40.532 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1060  Run server thread name: RPC
2019-04-10 02:51:40.532 [SRV_MAIN]      DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1067  JOINING all threads
2019-04-10 02:52:12.650 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1151  handle_accept
2019-04-10 02:52:12.651 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:1164  New server for RPC connections, SSL autodetection
2019-04-10 02:52:12.651 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:880   set m_connection_type = RPC
2019-04-10 02:52:12.651 [RPC0]  DEBUG   net.conn        contrib/epee/src/connection_basic.cpp:144       Spawned connection #1 to 0.0.0.0 currently we have sockets count:2
2019-04-10 02:52:12.651 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:107   test, connection constructor set m_connection_type=1

...

2019-04-10 02:52:25.107 [RPC0]  INFO    wallet.rpc      src/wallet/wallet_rpc_server.h:67       HTTP [10.12.2.134] POST /json_rpc
2019-04-10 02:52:25.107 [RPC0]  INFO    wallet.rpc      src/wallet/wallet_rpc_server.h:122      [10.12.2.134:59654 INC] Calling RPC method export_outputs
2019-04-10 02:52:25.134 [RPC0]  DEBUG   wallet.rpc      src/wallet/wallet_rpc_server.h:122      /json_rpc[export_outputs] processed with 0/27/0ms
2019-04-10 02:52:25.134 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:667   do_send_chunk() NOW SENSD: packet=160 B
2019-04-10 02:52:25.134 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:652   do_send_chunk() NOW just queues: packet=469 B, is added to queue-size=2
2019-04-10 02:52:25.134 [RPC0]  DEBUG   net     contrib/epee/include/net/abstract_tcp_server2.inl:855   handle_write() NOW SENDS: packet=469 B, from  queue size=1
```

## moneromooo-monero | 2019-04-10T10:25:43+00:00
That error is when you exported twice without importing. The exporter thinks "I already exported that, let's skip it", but the importer never saw it, so gets confused. Export all if that happened. But... I see there is no flag in RPC to tell it to. I'll add that now.

## moneromooo-monero | 2019-04-10T10:38:58+00:00
https://github.com/monero-project/monero/pull/5418 should do that.

## xnum | 2019-04-10T12:02:06+00:00
It works on import outputs, but similar error message happened when signing transfer

request:

```
{"jsonrpc":"2.0","method":"sign_transfer","params":{"export_raw":true,"unsigned_txset":"4d6f665726f20756e7369676e65642074782073657404f7eb66578cf87c6d9f9a3a13aa1ce1293ef2309d3dd8cd873fe79002a1fa1d1a3fe973bc65ac1feea0b064de2d9fadbfd2ba983595293f208cc4a1d0280a58c67a276971a0ee68e9bfc4100cf618169eaa6872371a2f499f8aac0ac1748df3e77850e0e539e050e57c272a295fbfbb8a3ff8adadf0f52eb14a720af38e1cb1e5041a3b515b1b20b67e934b92251c2a76b552ae30ce0131c5c866b8d0721a7f79da84b7b171bd32e09578d0f2caba15ee3941814c05e0d030bd1a1d63f29f596fdb9c827f560670bc31bb33c7699cc417b653c8b096b061394947ba9525938e6735fd285eaaa08a89316fc5f2c6fc885e14324253e8633f13c5b0d9c2311fd1f5b94c5898d8a95471b6346f605fa72a90ed8004a7994f58edec9b3646d0510d32b9a7a63b59205c229caaa5817cefadcf548a88ed1cffc1e24c6b1e911e32581d77b28c7794bebda19298efe795c413bf91bbfaaebd95e52d6328bff243315ca10825eeec546b8164e85f07dfc1d70d170d7c2855a907d643920b68142c42ae6fc5530a627dbf794db77b7812fdeff4e59c104e2da5d676be86c5f547dc42ec7aa1bf43fdb3538a599f9d18e86f95339c1b076bd344ca688841b847e21a468586a466dff4036416f37182c85e9f8d375a9ac97ba82c66a3dc85a9a890be364b677302add23cbca6edbf7ac7d510c0e0e8ed1c27fc6c7d608a50d25952397096aed524a9c0ff18874c23546ab86641fac16eaf5b1b2ed3c788e90481c1b8c71883f6344504032b65d2e84e9c3e91446788936917137949e162c0ab950cd30e49b2b59c69de796011984b8c483f57e353e2fd07a9286c46bea4efe1cd79aac632033458a2ccec8d5f64212d2b4ea779013c0dae0046af94f198959ba2816468164ea1f8d00d1c632a413f643bc9abeb08c559cb1b5bc7436c1003cc9e3a786f28b9c752668ecadc6bb1d6b350bf2f428d6859650309ea3c4828a70594a5b3e605fc701c7ce07c8a25e67f3a21fbf8f37b20638e1ab4a7296d739372bdca6ee9bc29149477c4c04c53281655899e7fe51094038c54c84ebcef9ea7310d4149f4bebbad1b4ed851c87cb756835bf057046958b3b8f13a3aa389e3b45fc98e3153306779e17af49eea65005fd2f4ab192e5818fea8a353a02e013401dc99e553198ee3b802a6eeb581bd63a3169db5ccc04d5e2b5e2d7402dbfa1df596847f7aa084f77b6d303a00d82eaaca2283c3c674fa98072c0b85529c5a94327e4ecbed45b7cdd0782b0ef95ec8e306c0420cc631ede0b15ca46fbbdf7159167890d19680ed38583b86b89cee84f33fa4d027d2db5036eb933e099bd1626d5aebedc7340ddab63ebe162945079693d03c75ba8751a05bd259b76d5dc29aa1aec2630957295bc9f853ee43e41958f7e87dd3fb1a57c65eb09e2507431b12a0b340279f03019dc66d54a25a9f83cf9c7293e110ff34b375e5b879909f587ad3dad3a554d7a946addeeeb82562cd760cad38c67215df5fc301a2876122b1094c878bedebb6e9f3ce15d3f2cd549fadab20b328ccb0007b254acffc420ea7a0cd21498a71507b85e1967ac09453e52329df8bcece3f0384fa4018ee458994e08763585039f4824395144be2630ef5a2eca811bce057091efe931d917f4ba966c7aa472d2daa5d82acb32321fe36aab81535ef5f61f64cae1ffc360dae03feba08ff6f3659093d313de57e39608ac6c316d4f0a90cb6c23f393b7066251abadf9399b80f56840c36fe3f61ee7288a62763b2cbc157755dfa66cfd245f9f8c2e7b2e6a8fc45e9936758f32cd3ba755ede5fa37e41d9b$095cb8ccc605bdab934a1dd925fdd8fe1513e44c9f2b63bff709328b973d01c6c38f867dc851a10e263d2b265a18f9b32bc04a94dc5052358898a618df60db2e06c8ae2671b0114214001756a4bad86a566eb6f404c32db3cfe8fb3b9e40b93fc4e50f2de3e38baca9ab7059d3b9ba2bc7188a5098f59e9b1e411a5488c9eac6589d09b735d8a837421d9346961777f7430c93a15b80aa48d93a1d7e0b54b192b6bab093f519e54695b335b70aedd3b644b34b361cde95f4008abf3066ff32564df82f006c6651e6b034923678258d0f8b8b082b9ea3dc6f05a7b5616d4741a8a7c86696afbd7fb8de1df578c47b940cdb1da1d3308039e271f192c1feab5f1292775356e408cbd7a657fa75474d18c90d678cdefa48e752517ebfc20f98f102d36ea44ebf256844256a9de002054670bfe77f24371421758e5a48905039be47758e9afe1a0e23dd9e2df844750f44f8145fc0d98c52e09c6426b27e0c9cf3c41d1350c5807c69c342d359867a8aab55472de254e08d3aa7428a9b725abf09f84e9cba4caf460a7d51df606c78abdba4557952511192e666a2618fac1e55ffc587648c8697a43c8a979c8eda2b0eed020bcc18df80d8240512064c8ba47f4395d2a602936bf4af0ac05501b3e064d3c39266f09bf54aab0454f64904770ee5e7ea8894be140006b65242e7b55d26f3aafffd9a802e676cd2c8890acdc61c29fa218730308f6a7a5fca1691eff18b6e4d7c3ec8d2cea29fde0461194b80eb010d8f7e8c730e4922eb255d0a43716c809a604eaa183a68a3da0c7fe85186f1c61e39fe9f38e7bdc0126acfd51b97ad45da0d39ff91c82aadea413088f8a68350e0d346c7487$8d34c5c44c39d472a43a84582229d62e04d7287550117e1a691d2803695193ea7d7101ab7206140bcb52a24e12f1735c4fbf3f1947ef786300eba6d97b406eafcfe9d2ea4711287a37256ac6835341a52e6499e580494370e633e338dcf3c953238b37e8fc9a08a7872189de9e2102cf8412a8685bc7cd126e9a86a29b5fa788b2f9f36298d01f0ce1ee762ba5a67a14f2e909a573e186a96ed937b59596f53fec0011bc8ccb1b4f966ee88b2a2f9482b3c14d4045a00d32b63a950cc8b31fac76eeed19345caf4b2c839734166260ef560c7bd8b449a361c70467fb1c52b2f2b9fbf7509079fe7fa41863b4c5e0a3e00078ed7a670861e316e2fd68f4fbd6de8623819475cd39658e75c2d3eb652b738b4b004e5ec795142c5f15ebc7ab5ed53fccb7ff1622c4391b2e1079d5263e18870175132316f6a51af51232bbfbf20e22b8156b2ea3e4736b449d416ce58e7ba4a22ca6796af6e3a6c9d56ad06165284a101d143b213344bcb9a8ad20e77bbc3b1c791ed4f9e6e1fd4eec3ad2968a081386014a43637a3c38e0eb055d2bb3493730d2da6fae4e819e73fb1c59bd7e07e616e210c89066e2560fea9b44361ebfb62942fc0a592de5c626c78acde3856d2eec2dd151601eeb04c5a6a058166d83cd84d4d48a9442a7eddd5319741caa93c3f28db7db4b32f94d601f0e79673137058e648e997b967e0b2e4cbcb96d1037091d9da7f990bb74d6d5482d94927cce103ac3ad9dba810887ab54c8f837c7caca7cd0e6e98cd7b6b46d278848d7543cd37267d4b302030231b026c1261c546548f3ea539a4a2c222c4efe65ad4a32a847be6a12fa39c2f3ab93c0449005d0a123f5df6a0$1cf8470ae31a65128f3810423261f80ea64f2ce278c493855143935a1d6d449fffe5b67e390672b845b399e06cbc700f9a8012b7b127ddcdd0a37f8638288e08da85db9b3c278d45eef214ff8fb0cda15c7efcc18a42438227a01862efeedf5c84918e0bf9f9630895e3f21f2b22053b134d38cf830458229e8527e5a0036bef4179846046c004d9207d4dc78d9d18571d6dd0710398f9f2db563f316adbc604034d73f79b4a32afe4174a130e0be1$d24a7b1c156cc7205f384c03f4513358d95c1682007805140faaa8232075a796b6333766c4c5340f050b3b0a"}}
```

response:

```
{
        "error": {
                "code": -42,
                "message": "Failed to sign unsigned tx: Imported outputs omit more outputs that we know of"
        },                                                                                                                                                                              "id": 0,
        "jsonrpc": "2.0"
}
``` 

log:

```
2019-04-10 11:57:50.540 [RPC0]  INFO    wallet.rpc      src/wallet/wallet_rpc_server.h:67       HTTP [127.0.0.1] POST /json_rpc
2019-04-10 11:57:50.540 [RPC0]  INFO    wallet.rpc      src/wallet/wallet_rpc_server.h:89       [127.0.0.1:35682 INC] Calling RPC method sign_transfer
2019-04-10 11:57:50.577 [RPC0]  INFO    wallet.wallet2  src/wallet/wallet2.cpp:6113     Loaded tx unsigned data from binary: 1 transactions
2019-04-10 11:57:50.577 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:11979    outputs.first > m_transfers.size(). THROW EXCEPTION: error::wallet_internal_error
2019-04-10 11:57:50.577 [RPC0]  WARNING net.http        src/wallet/wallet_errors.h:873  /root/monero/src/wallet/wallet2.cpp:11979:N5tools5error21wallet_internal_errorE: Import$
d outputs omit more outputs that we know of
```

## moneromooo-monero | 2019-04-10T14:03:46+00:00
Did you export twice without importing ?

## xnum | 2019-04-10T14:15:08+00:00
I imported to a clean cold wallet, but read-only wallet is permanent. Basically every time I sign transfer,
a clean cold wallet rpc server will be setup. We use one read-only wallet rpc server to scan incoming transfer, get balance, create transfer.
So.. yes?

I added {"all": true} option when importing outputs and it returns the correct imported number it should be.
Then export key images and import key images looks good too.

## moneromooo-monero | 2019-04-10T15:03:19+00:00
If you do that, then the cold wallet cache "forgets" previously imported data. Then the automatic incremental export/import piggybacking on transfer will not be enough. You will have to explicitely export/import outputs and key images every time you restore a cold wallet from seed/keys.
There could be a wallet setting to make that auto export/import always do all outouts/key images, but I'm not sure how useful it'd be beyond your special case.

## xnum | 2019-04-10T15:09:42+00:00
I use the same instance to do these operations (import, export outputs, key images and sign), and it works before v0.13. it only create a new instance for each transfer signing. the cold wallet should remember unspent output. so I think this signing procedure is correct. or it's changed at v0.14?

## moneromooo-monero | 2019-04-10T15:11:25+00:00
Maybe I misunderstood your setup. Describe the operations in detail.

## xnum | 2019-04-10T15:50:12+00:00
I just reviewed our code and realize it does have a misuse. I only use the same instance on import/export but not signing because `Create` and `Sign` is two function at high level design and may create a new backend. It was working at v0.13 actually but not at v0.14. #5277 and #5418 could solve this problem and I finally send a transaction successfully on testnet.

@moneromooo-monero thank you very much. we fixed withdrawal functionality finally. The wallet rpc server has a very big improvement after v0.12, I don't have to operate cli automatically via `expect` and do some signature calculation, derivation myself.

The only problem is even cold wallet rpc server needs an offline daemon to work properly, or it shows can't connect to daemon and exited. Maybe we can have an offline option?

The whole operations are:
1. open read-only wallet rpc server with view key listen on 0.0.0.0 (can be reuse)
2. prepare public full node or on-premise full node as trusted daemon (can be reuse)
3. open daemon with offline option to make step2 working (on demand)
4. open cold wallet rpc server with view/spend key but only listen on localhost (on demand)
5. `export_outputs` from read-only wallet
6. `import_outputs` to cold wallet
7. `export_key_images` from cold wallet
8. `import_key_images` to read-only wallet
9. call `transfer` on read-only wallet
10. call `sign_transfer` on cold wallet
11. call `send_raw_transfer` on full node
12. close cold wallet and cleanup private key data

## moneromooo-monero | 2019-04-12T22:24:51+00:00
Don't close if you want me to see it :)
But yes, there will be an offline option.

## moneromooo-monero | 2019-04-15T22:22:53+00:00
https://github.com/monero-project/monero/pull/5445

## moneromooo-monero | 2019-04-16T22:12:53+00:00
+resolved

# Action History
- Created by: xnum | 2019-03-13T06:39:50+00:00
- Closed at: 2019-04-16T22:25:34+00:00
