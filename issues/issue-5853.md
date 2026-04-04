---
title: monero-wallet-cli wierdness
source_url: https://github.com/monero-project/monero/issues/5853
author: trasherdk
assignees: []
labels: []
created_at: '2019-08-26T06:39:45+00:00'
updated_at: '2019-09-04T00:44:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm running `Monero 'Boron Butterfly' (v0.14.1.2-cdfa2e58d)` on `testnet`.
Looking at `show_transfers out` I noticed a few things.

Each transaction is `send 200 to address 9xJxeT......`

The first `1-3` has the destination address. The rest don't.
The next `4-8` didn't actually send any XMR, but has a transaction fee. ???
The last `9-10` did the transfer.

What did I miss?

```
[wallet 9zwQfv]: show_transfers out
 1253343    out        -       2019-07-11 22:35:29     200.000000000000 561ae1e15132bf3a43f1a5cea5f556d3bc327d95c3b947fe9f3cb863a82632d1 0000000000000000 0.000068830000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1253353    out        -       2019-07-11 23:01:36     200.000000000000 729270c908a779e841a5e4d1e039da6f27519500fbaacb7206eb051cddaef077 0000000000000000 0.000100870000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1253367    out        -       2019-07-11 23:16:48     200.000000000000 75a4bff25ad30e1330d79949b13f3819c72cf12bc0a30f292e6f6483af6ba19e 0000000000000000 0.000068910000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 24d534c250264e7cfdaf3a6c2a9f9769e7a7d6624091cfb0c535d2ba1573d431 0000000000000000 0.000095800000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 fa7a225e420ca6a2c6b58ef77135a27d92350dc4abba24b77a4962985fb79f2f 0000000000000000 0.000095690000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 5190ac62a7972c5f3c2389283f37d035fcd98f28e86448641eac77e99b6fbd5f 0000000000000000 0.000095730000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 8f9aa7631abb2c39c02e1ab20946a298ab4e34fe8c85e96cc0a58623182389c6 0000000000000000 0.000095620000 - 0 - 
 1281401    out        -       2019-08-20 11:46:42       0.000000000000 d2dad72402007b6f9431315a5fb6eaff834417bacecb7207ea8e086a960a1c50 0000000000000000 0.000095620000 - 0 - 
 1282118    out        -       2019-08-21 10:58:09     200.000000000000 cf285577c450c84ca8f298aabe2d62624a44eada6e50f06dcffbc2d26a3463b7 0000000000000000 0.000095560000 - 0 - 
 1282131    out        -       2019-08-21 11:30:57     200.000000000000 ad0d7b4519f278f5de3ac540d557e26868d78933f567ca8c91de87402010485b 0000000000000000 0.000095670000 - 0 - 
```


# Discussion History
## moneromooo-monero | 2019-08-26T08:37:34+00:00
Did you remove the cache between those heights ?

## moneromooo-monero | 2019-08-26T08:37:45+00:00
(or run rescan_bc)

## trasherdk | 2019-08-26T12:33:22+00:00
I didn't do anything to change config.
I have recompiled, quite often. First from `v0.14.1.2` and later, from `master`.

Running `rescan_bc` just removed destination address from the output of `show_transfers out`

## moneromooo-monero | 2019-08-26T14:30:25+00:00
Recompiling should not change anything unless you go back in "time". The load/save is supposed to be backward compatible (but might be buggy).

## trasherdk | 2019-08-29T04:59:16+00:00
This specific build is for my version of [monero-pool](https://github.com/trasherdk/monero-pool/) `pool-fee-wallet` branch.

Before #5728 got merged into `master`, I build from `v0.14.1.2`. After the merge, I build from `master`.

So far, it has only been running on `testnet`.

On every change to my [pool-fee-wallet](https://github.com/trasherdk/monero-pool/tree/pool-fee-wallet) branch, I am building `monero` of a fresh `git clone`.

By `load/save` do you mean `starting/stopping` a wallet? If no, I don't know what you mean.

Anyway. The part the worried me, is the the transactions with zero value, but have a fee.

## trasherdk | 2019-08-29T05:05:05+00:00
And the destination address is back in **show_transfers out**
```
 1253343    out        -       2019-07-11 22:35:29     200.000000000000 561ae1e15132bf3a43f1a5cea5f556d3bc327d95c3b947fe9f3cb863a82632d1 0000000000000000 0.000068830000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1253353    out        -       2019-07-11 23:01:36     200.000000000000 729270c908a779e841a5e4d1e039da6f27519500fbaacb7206eb051cddaef077 0000000000000000 0.000100870000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1253367    out        -       2019-07-11 23:16:48     200.000000000000 75a4bff25ad30e1330d79949b13f3819c72cf12bc0a30f292e6f6483af6ba19e 0000000000000000 0.000068910000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 8f9aa7631abb2c39c02e1ab20946a298ab4e34fe8c85e96cc0a58623182389c6 0000000000000000 0.000095620000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 5190ac62a7972c5f3c2389283f37d035fcd98f28e86448641eac77e99b6fbd5f 0000000000000000 0.000095730000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 24d534c250264e7cfdaf3a6c2a9f9769e7a7d6624091cfb0c535d2ba1573d431 0000000000000000 0.000095800000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 fa7a225e420ca6a2c6b58ef77135a27d92350dc4abba24b77a4962985fb79f2f 0000000000000000 0.000095690000 - 0 - 
 1281401    out        -       2019-08-20 11:46:42       0.000000000000 d2dad72402007b6f9431315a5fb6eaff834417bacecb7207ea8e086a960a1c50 0000000000000000 0.000095620000 - 0 - 
 1282118    out        -       2019-08-21 10:58:09     200.000000000000 cf285577c450c84ca8f298aabe2d62624a44eada6e50f06dcffbc2d26a3463b7 0000000000000000 0.000095560000 - 0 - 
 1282131    out        -       2019-08-21 11:30:57     200.000000000000 ad0d7b4519f278f5de3ac540d557e26868d78933f567ca8c91de87402010485b 0000000000000000 0.000095670000 - 0 - 
```
This is what it looks like on [testnet.xmrchain.com](https://testnet.xmrchain.com/)

![image](https://user-images.githubusercontent.com/5003891/63911559-e33cff80-ca54-11e9-9620-dd509f526fef.png)


## moneromooo-monero | 2019-08-29T10:38:06+00:00
Loading/saving a wallet cache file to/from disk. The outputs above show ~20. You said in the first post that all txes are for 200. Can you confirm that ?

## trasherdk | 2019-08-30T08:07:58+00:00
Memory is not what it used to be.
The 5 x `0.000000000000` was indeed supposed to be 5 x `20.000000000000`.

## moneromooo-monero | 2019-09-02T11:31:46+00:00
Is the destination address from the same wallet as the sending address ?

## trasherdk | 2019-09-03T07:04:45+00:00
Well, I don't really remember. ~~They was not supposed to be.~~ Looks like they were. 
I just tried sending 20 to another address, and 20 to the sending address.
```
[wallet 9zwQfv]: show_transfers out
 1253343    out        -       2019-07-11 22:35:29     200.000000000000 561ae1e15132bf3a43f1a5cea5f556d3bc327d95c3b947fe9f3cb863a82632d1 0000000000000000 0.000068830000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1253353    out        -       2019-07-11 23:01:36     200.000000000000 729270c908a779e841a5e4d1e039da6f27519500fbaacb7206eb051cddaef077 0000000000000000 0.000100870000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1253367    out        -       2019-07-11 23:16:48     200.000000000000 75a4bff25ad30e1330d79949b13f3819c72cf12bc0a30f292e6f6483af6ba19e 0000000000000000 0.000068910000 9xJxeTBNxmbYwQduR3HqQK5JnEcek1YrhcNj1nPni2X8iotSNDS4zY8U8YNYbg9Fa6iHD1Ucc8uB9G6YW8nXzgmGGov4o9x:200.000000000000 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 5190ac62a7972c5f3c2389283f37d035fcd98f28e86448641eac77e99b6fbd5f 0000000000000000 0.000095730000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 24d534c250264e7cfdaf3a6c2a9f9769e7a7d6624091cfb0c535d2ba1573d431 0000000000000000 0.000095800000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 8f9aa7631abb2c39c02e1ab20946a298ab4e34fe8c85e96cc0a58623182389c6 0000000000000000 0.000095620000 - 0 - 
 1281400    out        -       2019-08-20 11:45:20       0.000000000000 fa7a225e420ca6a2c6b58ef77135a27d92350dc4abba24b77a4962985fb79f2f 0000000000000000 0.000095690000 - 0 - 
 1281401    out        -       2019-08-20 11:46:42       0.000000000000 d2dad72402007b6f9431315a5fb6eaff834417bacecb7207ea8e086a960a1c50 0000000000000000 0.000095620000 - 0 - 
 1282118    out        -       2019-08-21 10:58:09     200.000000000000 cf285577c450c84ca8f298aabe2d62624a44eada6e50f06dcffbc2d26a3463b7 0000000000000000 0.000095560000 - 0 - 
 1282131    out        -       2019-08-21 11:30:57     200.000000000000 ad0d7b4519f278f5de3ac540d557e26868d78933f567ca8c91de87402010485b 0000000000000000 0.000095670000 - 0 - 
 1291209    out        -       2019-09-03 06:25:54      20.000000000000 841f146ae2940f2f6e68ee4a44ca62d42dc77aa1bb85dd2876a0376a8f4e9243 0000000000000000 0.000093880000 9wiAxp9aY2CRei29DDVqvJQmtaWKDe1QJN59nu3KDg4YUkbSE3ASesRM5DVrFyBJ3fRz1Kn9NZWfUE8anRJt6psJ6jAH3N8:20.000000000000 0 - 
 1291211    out        -       2019-09-03 06:33:18       0.000000000000 00fd265ce7917d3db26074acbb2c09cb7a8654f94730be13de977ee513d9bfe4 0000000000000000 0.000093920000 9zwQfvQvvLrBURLrmw4rS61n8hWMXgijdGf8e7e6Q7EWR7WCKenAqsYQHto7dymD2KP4Wh5Sym5DoX5FTXCYdMomGzGPMzW:20.000000000000 0 - 
[wallet 9zwQfv]:                
```
Those 2 transactions looks quite different than the ones above.  
The `last transaction, send to self` in block-explorer.
![image](https://user-images.githubusercontent.com/5003891/64150965-8de95f80-ce53-11e9-8c7b-9294bba98751.png)


## moneromooo-monero | 2019-09-03T13:31:07+00:00
Sending to the sending address is the same as sending nothing, since you can't tell what is change and what is not change. At least when restoring from seed/keys. The wallet ought to remember that though, until you do restore.

## trasherdk | 2019-09-04T00:44:32+00:00
Yes, the `sending to self` is a special case.
But, the last of the above transactions, at least `the wallet` knows the `receiving address` and the `amount`.

There are 7 transactions before that, where that information is not known, and that's the ones I was wondering about.

# Action History
- Created by: trasherdk | 2019-08-26T06:39:45+00:00
