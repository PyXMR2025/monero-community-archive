---
title: 'Question: Seems I send monero to two address in a single payment'
source_url: https://github.com/monero-project/monero/issues/8244
author: ycMia
assignees: []
labels: []
created_at: '2022-04-08T11:05:19+00:00'
updated_at: '2022-04-08T11:27:17+00:00'
type: issue
status: closed
closed_at: '2022-04-08T11:22:01+00:00'
---

# Original Description
Hi, I'm new here. I created a full-node on my laptop by monerd.exe. And have kept on using monero-wallet-cli for about a half year.
The version of my monerod till now is `0.17.3.0-release` while the version of the wallet is `Monero 'Oxygen Orion' (v0.17.3.0-release)`.

I runs windows 10 as my system.

------
The confusing circumstances happens in today `[UTC](+8) Fri Apr  8 18:21:39     2022` at txid `4861c59e665a476f1ea0849ccf86bbc1ca8b2d9d70568954128ed57da275967f`. 

I was just ready to `sweep_all` my monero to a address. I ran the command `address_book` and checked twice if I send to the right address before I really have launch the transfer. Then I launched, and comfirmed that transfer, pressed 'Y' and enter. Everything is normal.

Just after that I ran `show_transfer`, the result is incredible. One strange address come into my sight. I only pay out my monero to a single address in this wallet. I can recognize how his address spells.

That was the result. ( I have hidden the address I familiar with. )

```
 2590107    out        -       2022-03-29 09:03:04       0.033330000000 156def72ff4e4d2c41428d188ad2d876aba5508d8b4a3000a801f07c5eaee71b 0000000014ec72d3 0.000006420000 *****LkfwY6aHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSHZRbNv4xE7TQt*****:0.033330000000 0 -
 2590188    out        -       2022-03-29 12:03:05       0.033000000000 00efc307b79d9a33751de285f06cb406f4889486c468059e87f1a306ba9b099f 0000000014ec72d3 0.000006420000 *****LkfwY6aHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSHZRbNv4xE7TQt*****:0.033000000000 0 -
 2590216    out        -       2022-03-29 12:52:13       0.033000000000 5afb6f982743a6104e1ee6eb04433773b6d43ec303b27e39258b1d452816e0aa 0000000014ec72d3 0.000006410000 *****LkfwY6aHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSHZRbNv4xE7TQt*****:0.033000000000 0 -
 2595968    out        -       2022-04-06 12:41:41       0.033000000000 fdbedf1f63c08a2939f2e26acb89c26fbbfd9b024bb3e72fa70baa03921adc3c 0000000014ec72d3 0.000006360000 *****LkfwY6aHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSHZRbNv4xE7TQt*****:0.033000000000 0 -
 2597325    out        -       2022-04-08 09:34:17       0.038610935589 4861c59e665a476f1ea0849ccf86bbc1ca8b2d9d70568954128ed57da275967f 0000000014ec72d3 0.000006350000 45XxdXwBLGaaHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSCE5eDre:0.038610935589 0 -
```

I was scared about if I'm under a virus attack -- someone may change your clipboard, you know, and checked that txid immidately to ensure that tranasfer was correct, but both of the are comfirmed by the network. into

That is the result I received after I correctly ran the command `check_tx_key`. I've hidden the private tx id and the address as well.
```
[wallet ******]: check_tx_key 4861c59e665a476f1ea0849ccf86bbc1ca8b2d9d70568954128ed57da275967f ******cb40ec6fee9c02af3704efd4d81709854b2ef98f9a424ad466ce****** 45XxdXwBLGaaHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSCE5eDre
45XxdXwBLGaaHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSCE5eDre received 0.038610935589 in txid <4861c59e665a476f1ea0849ccf86bbc1ca8b2d9d70568954128ed57da275967f>
This transaction has 22 confirmations
```

```
[wallet ******]: check_tx_key 4861c59e665a476f1ea0849ccf86bbc1ca8b2d9d70568954128ed57da275967f ******cb40ec6fee9c02af3704efd4d81709854b2ef98f9a424ad466ce****** *****LkfwY6aHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSHZRbNv4xE7TQt*****
45XxdXwBLGaaHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSCE5eDre received 0.038610935589 in txid <4861c59e665a476f1ea0849ccf86bbc1ca8b2d9d70568954128ed57da275967f>
This transaction has 22 confirmations
```

Both results are pointing to the address 45XxdXwBLGaaHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSCE5eDre, that made me confused.

Then I asked the owner of the address *****Lkfw whether he received monero or not. He said yes, he definitely received that.

So is that proves there are some extra monero was transferred on address "45Xxd " ? If not, what is the reason behind this? I wonder.

ycMia
2022/4/8

# Discussion History
## selsta | 2022-04-08T11:12:41+00:00
Both addresses look equivalent, check the middle part, just that `*****LkfwY6aHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSHZRbNv4xE7TQt*****` is an integrated address while `45XxdXwBLGaaHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSCE5eDre` is the base address.

Base address + payment id = integrated address.

## ycMia | 2022-04-08T11:22:00+00:00
> Both addresses look equivalent, check the middle part, just that `*****LkfwY6aHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSHZRbNv4xE7TQt*****` is an integrated address while `45XxdXwBLGaaHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSCE5eDre` is the base address.
> 
> Base address + payment id = integrated address.

Thank you for replying that fast! I haven't realized that similarity yet. Seems I need to study further. 😃 

## selsta | 2022-04-08T11:24:29+00:00
Integrated addresses are a bit confusing, that's why it would be ideal if merchants switch to subaddresses.

## selsta | 2022-04-08T11:26:53+00:00
Inside `monero-wallet-cli` you can enter the following command, just without the censored address:

```
integrated_address *****LkfwY6aHDAay6A3qLTgoAnoaMVW5bxAYcC51tnP4SYTDWEFfAt6HNe2YvW5sXLpQLoFsiZXq7hNpMAnKqKSHZRbNv4xE7TQt*****
```

To get the separate address and payment id. Then you can check if they fully match.

# Action History
- Created by: ycMia | 2022-04-08T11:05:19+00:00
- Closed at: 2022-04-08T11:22:01+00:00
