---
title: not enough money to transfer
source_url: https://github.com/monero-project/monero/issues/1058
author: Atrides
assignees: []
labels: []
created_at: '2016-09-06T12:39:23+00:00'
updated_at: '2018-01-08T14:08:30+00:00'
type: issue
status: closed
closed_at: '2018-01-08T14:08:30+00:00'
---

# Original Description
I created new wallet for the pool and tried to transfer balance between wallets.

```
[wallet 48Rqot]:
Starting refresh...
Refresh done, blocks received: 0                                
Balance: 477.000180560614, unlocked balance: 477.000180560614
[wallet 48Rqot]: transfer 0 42HeDcrpUR1VRVvt2ZvvTW7n7EAGT11CRAndmKow54Y6a64XgmGSD9Ufn1yaBz61zaFVpUXubGa8dEi9iWNj9D8W37KxE2R 5
Error: not enough money to transfer, available only 0.000000000000, transaction amount 5.000000000000 = 5.000000000000 + 0.000000000000 (fee)

```

Unmixable also doesn't work.

```
[wallet 48Rqot]: sweep_unmixable
Error: No unmixable outputs found

```

"incoming_transfers available" shows a LOT of green available coins.

After rescan and restore wallet.bin from scratch, the same situation.
Also redownloaded full blockchain, the same situation.
It's not only due to dust, old wallet has some amount of coins>7

```

0,01     F          454487  <24fb0a4e64c04e5792c31e9293623259935bc5febb84cf384edfe9fb9b066305>
0,01     F          454488  <804a55601a1f4e73334123042419a0040a21d8fd12767a250ffd85b3abf8c38c>
0,01     F          454498  <7372659011a2abe3707476145454a328011fdb6ab0c0e6121d7e578dbfec56d2>
0,01     F          454539  <1baa8a25207555a2ad9902e8383937198e4682469cba3be32b92444a60bc3de0>
0,01     F          454584  <a2c8971abacb319bbc3f36fd89eccdd3dc8c3382845bd28b718f2f8d93d709e0>
0,01     F          454586  <bca304bae030fbb7ea0c44b468da74a5ef98a9a1578d1a7b375042b6bc53e091>
0,01     F          454601  <bd012be4f00bb9a582fb9ec56a3a79ccfdff6d5b8df2798d33753672a2fee4ac>
0,01     F          454610  <a6edca75cecf58fb4358b08756400eaf071f13de619f7636798c734ab19d157d>
0,03     F          282592  <3b3fc4c213753f2129d40bdb9586998336971ec527d034d08f6349b238763e7a>
13   F              28  <7d726f18e6fc5178423a5b57b269bf6359bdf3e0678f36d3715ad180d50ea6ee>
13   F              32  <efef70c4f2153f7c755401e1650b6ecf0be4985e527c2234c4c8ad249ac13d6a>
13   F              33  <615f8f268a3439b6485293a9bdab6f8044f45c9615f73399a459090aec26b894>
13   F              43  <273dd5edc88d8e5542cbbd1921bbb158bb6734cdceaa67e35f69a895b33d6586>
13   F              44  <07ffc3af1883e0385145779c7af5ac3d39629ec9a54a2abc7bc33a9b44c5bf51>
13   F              47  <5eb8a72d237d3e3b2f8d9b980618dcc306a5a46ebe25c5f9443e8b448f0003bb>
13   F              49  <4cbe8ee7a90b30767909feefbff675e0f4cc42f6088c9836b9e91992442d4a6c>
13   F             104  <d670696959265143868013160a12c5c328aa04225531d7eccbb1f6f5452d5a9f>
13   F             194  <5def5c0cd870905d2fea9c07b15493335f21967ab5cadbfb600d4c8863c6d505>
13,3     F              18  <014921bbb5effc12089b6c3d8fd49cce3f9427ac8bd12776fe58b748bb6e3d43>
13,35    F              11  <f97cdceebac77214b25f3eb38221875ff74ee2d32c8fc2cb45b5b3fe004b56fb>
13,38    F               0  <78636f0017d03e24e75fb8eaa56d7df12b3b83693f5585939167b0d733428e8b>
13,4     F              28  <14d7060053c5a4b53cb0bbe161f341bc3355f1db1c364b2fc5887d1107773fde>
13,4     F             119  <35cc37e4e2e04213ec50761c07839153a3b42601fe9247bcda09a906bf903029>
13,46    F               4  <4f3ca5520a39044ca1bf7af6df934966d093c40df6de5a8eb81f80d2af9fafb5>
13,5     F               5  <e6005d1e40a95120180f9f2a0f9b1723d4a98f7415856b3c00976759871b0cfb>
13,9     F               6  <9b09fb4b71bcae4024378c7d469fe42753a5cfe6cb59723a1c47e3e60577e72c>
13,91    F               1  <19f114db3da76b79e10142dd8e7c66a5f45839d34da35828abb3dcf84191fc10>
13,95    F               1  <a78d0773bd15f9da5ebf78ef9a53cac317a6022c475184ce86ee1b30cd862c6b>
13,96    F               3  <74905382c53a3a06973debd0fdf42392838a2a034bff589dbeb414947cc5fbfc>
13,97    F               0  <ac9f576708f59097b4e94e6220cdbcc421f51c8297eeea9211d7747ba9305bef>
13,97    F               1  <1cd2b72054147e541de2de656ff1b33c05f9277d7bbdac8e8057fcc4568bdee8>
13,97    F               3  <eea68d3ed53940c1e63c529da2a3382ffdb49dbdbe27a8cd4cf957dfe44a7b2a>
13,97    F               5  <86b787d99edb246a1da99fdbc392ff69de76981261445730531ece1b1545e4e8>
14   F              15  <1587f5e1bdd431994f07c253e48f9edec94b124b2ea1e7b10eb3f005870f650c>
14   F              19  <3ec019e83867450c1efd379fe27aed3d0ed8ee0844ae3fed143831fcb553894a>
14,02    F               2  <7444f051103f4d8dbf09f6a159ff5d4c336b927da1c49361a728233aa340f1d1>
14,03    F               1  <81e3889775d105634a6d711220f6f6c7ae90c90092890199c28df02c343360f5>
14,05    F               2  <7d58e0c01f92cd2c5e627dfdb37a793b327eb094eb2cfdd9b9a868174c0c6d50>
14,4     F               0  <d561c92ce22d60896fb728120952407a0f006197c30207c6e5970f90f840ffdc>

```

BTW, sadly that anti-dust command were deleted in last simplewallet.
BTW2, TX-cost is currently ca. 1$, I think it's too expensive.


# Discussion History
## Atrides | 2016-09-06T12:56:18+00:00
sweep_dust via RCP shows

> 2016-Sep-06 14:55:02.612411 [RPC0]failed to deserialize extra field. extra = 01655a9b3122c2760d4d9547847404af816819da79b62976c630abd3f578a13bcc022100c3f5cecae0b64dbd40affa049a664613fef87e3dddcef19906b4558e6048c7bfde20a45b4aefa4ad7d9213861f8db71d826f6e09f56126a36d2e560c0d253be03762
> 2016-Sep-06 14:55:02.612497 [RPC0]Transaction extra has unsupported format: <2825653053a8423a42a1b14c5153ef2140ae84b9bf210fda1d13d4c643cf9388>
> 2016-Sep-06 14:55:02.615123 [RPC0]failed to deserialize extra field. extra = 0184adc57f8587a70381d71b06e546280dca2da9970c1d74a493d75a31762b6f7dde20410282ca332fef16a63711caa0af669799b333f0c81d5c1ab7af5d485a9f9b9e
> 2016-Sep-06 14:55:02.615179 [RPC0]Transaction extra has unsupported format: <c2d7180f1f01e3e5260eb5021177785aed57b3a103b8585113b3e6e9786b1831>

command:

> curl -X POST http://127.0.0.1:18181/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sweep_dust"}' -H 'Content-Type: application/json'
> {
>   "id": "0",
>   "jsonrpc": "2.0",
>   "result": {
>   }


## Atrides | 2016-09-06T15:18:23+00:00
With fresh compiled monero from github:

> Balance: 477.000180560614, unlocked balance: 477.000180560614
> Background refresh thread started
> [wallet 48Rqot]: [wallet 48Rqot]: 
> [wallet 48Rqot]: sweep_all 48RqotWvKKkBbiABkoYHReNCjNbykMx1bWesek7Vb8RKUswPvCk8AQAHuxHWW3gDPJEuuAxNkEFUf9jCRtKJUBmQTSoXt2A
> Error: not enough outputs for specified mixin_count = 4:
> output amount = 14.020000000000, found outputs to mix = 4
> output amount = 13.910000000000, found outputs to mix = 4
> output amount = 14.030000000000, found outputs to mix = 4
> output amount = 13.950000000000, found outputs to mix = 4
> output amount = 14.050000000000, found outputs to mix = 3
> 
> [wallet 48Rqot]: sweep_all 3 48RqotWvKKkBbiABkoYHReNCjNbykMx1bWesek7Vb8RKUswPvCk8AQAHuxHWW3gDPJEuuAxNkEFUf9jCRtKJUBmQTSoXt2A
> Error: internal error: Duplicate indices though we did not ask for any
> 
> [wallet 48Rqot]: sweep_all 0 48RqotWvKKkBbiABkoYHReNCjNbykMx1bWesek7Vb8RKUswPvCk8AQAHuxHWW3gDPJEuuAxNkEFUf9jCRtKJUBmQTSoXt2A
> Error: failed to find a suitable way to split transactions
> 
> [wallet 48Rqot]: sweep_all 0 42HeDcrpUR1VRVvt2ZvvTW7n7EAGT11CRAndmKow54Y6a64XgmGSD9Ufn1yaBz61zaFVpUXubGa8dEi9iWNj9D8W37KxE2R
> Sweeping 477.000180560614 in 36 transactions for a total fee of 23.370000000000.  Is this okay?  (Y/Yes/N/No)Y
> Error: transaction <306343fac571818a008821cff5e6f89f16f6092e8524f8d90fe73cdbb7ba7fea> was rejected by daemon with status: Failed
> Error: Reason: mixin too low
> 
> [wallet 48Rqot]: sweep_all 3 42HeDcrpUR1VRVvt2ZvvTW7n7EAGT11CRAndmKow54Y6a64XgmGSD9Ufn1yaBz61zaFVpUXubGa8dEi9iWNj9D8W37KxE2R
> Error: internal error: Duplicate indices though we did not ask for any


## moneromooo-monero | 2016-09-11T13:59:11+00:00
> [wallet 48Rqot]: sweep_unmixable
> Error: No unmixable outputs found

Do you have any unmixable outputs ? If so, how did you tell ? If not, it worked.

> Transaction extra has unsupported format: 

Is that your tx ?

> Duplicate indices though we did not ask for any

I know what this is, and it will be fixed very soon.

> Error: failed to find a suitable way to split transactions

You probably have a lot of very small outputs, which don't pay enough for the fee.

Try sweep_all. This tries to match small and larger outputs, so it can move all, but at the expense of privacy.


## Atrides | 2016-09-12T17:10:51+00:00
> Do you have any unmixable outputs ? If so, how did you tell ? If not, it worked.

No. 
 ~~ sweep_unmixable
Error: No unmixable outputs found

> Is that your tx ?

No. But I see this TX now in block explorer:
https://minergate.com/blockchain/xmr/transaction/2825653053a8423a42a1b14c5153ef2140ae84b9bf210fda1d13d4c643cf9388

> You probably have a lot of very small outputs, which don't pay enough for the fee.

That's true, because it was a pool wallet very long time. I counted ca. 22k unspent transactions.

> Try sweep_all. This tries to match small and larger outputs, so it can move all, but at the expense of privacy.

I tried it many times, see my last answer above. I tried it also with compiled last version from github.


## moneromooo-monero | 2016-09-17T15:30:03+00:00
From what I can tell, you have mixable outputs that are too small to pay for themselves. The "Duplicates found" error was fixed in recent github, and this might fix your problem. It might also work a bit better in a couple weeks when the lower fee will kick in.


## moneromooo-monero | 2016-09-24T08:00:26+00:00
Try again with latest master plus https://github.com/monero-project/monero/pull/1121


## AJIekceu4 | 2016-10-30T09:56:09+00:00
May be it help, seems it is same problem as i have:
https://github.com/monero-project/monero/issues/1052#issuecomment-257141896


## dEBRUYNE-1 | 2018-01-08T13:17:26+00:00
+resolved

# Action History
- Created by: Atrides | 2016-09-06T12:39:23+00:00
- Closed at: 2018-01-08T14:08:30+00:00
