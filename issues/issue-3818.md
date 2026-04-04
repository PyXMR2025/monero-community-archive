---
title: How to make a original transaction ?????
source_url: https://github.com/monero-project/monero/issues/3818
author: somebodyLi
assignees: []
labels:
- invalid
created_at: '2018-05-17T03:46:32+00:00'
updated_at: '2018-05-23T13:41:11+00:00'
type: issue
status: closed
closed_at: '2018-05-23T13:41:11+00:00'
---

# Original Description
In the offical developer guides ,I saw the method `sendRawtranstion`,so  I want to know how to use it ?? How can I get the parameter for it ???

# Discussion History
## moneromooo-monero | 2018-05-17T07:32:10+00:00
https://getmonero.org/resources/developer-guides/daemon-rpc.html#sendrawtransaction

## stoffu | 2018-05-17T07:51:46+00:00
You can generate hex strings of raw txes by using:

- `monero-wallet-rpc`: `transfer` command with `do_not_relay` and `get_tx_hex` options (see https://getmonero.org/resources/developer-guides/wallet-rpc.html#transfer)
- `monero-wallet-cli`: launch the program with `--do-not-relay` flag, which causes the `transfer` command to save the raw tx hex string to `raw_monero_tx`


## somebodyLi | 2018-05-17T09:18:05+00:00
What is  the `raw_monero_tx` means ???  If I have to sign it ,if not when to sign ??  

## moneromooo-monero | 2018-05-17T09:20:24+00:00
This is a bug tracker, not a help, desk. Ask on #monero on Freenode, or monero.stackexchange.com.

## stoffu | 2018-05-17T09:50:11+00:00
@liyanhrxy 

> What is the `raw_monero_tx` means ??? If I have to sign it ,if not when to sign ??

It's a file saved to the current directory, just like other kind of files such as key images and unsigned transactions.

## somebodyLi | 2018-05-17T11:05:59+00:00
> It's a file saved to the current directory, just like other kind of files such as key images and unsigned transactions.

I have got your idea ,but I want to make a transaction offline like bitcoin `creatRawtractions`--`sign`
 and then I can call `sendRawtractions` anywhere ???  

## stoffu | 2018-05-17T12:38:00+00:00
There’s also the cold signing feature using the watch-only wallet. I don’t know what you want to do and I’m not familiar with bitcoin.

## somebodyLi | 2018-05-17T12:39:37+00:00
anyway,thank you so much 

## jtgrassie | 2018-05-23T12:37:32+00:00
@liyanhrxy 
> I have got your idea ,but I want to make a transaction offline like bitcoin creatRawtractions--sign
and then I can call sendRawtractions anywhere ???

@stoffu answered the [first part](https://github.com/monero-project/monero/issues/3818#issuecomment-389777554) of this (creating the raw tx) and @moneromooo-monero  answered the [second part](https://github.com/monero-project/monero/issues/3818#issuecomment-389772476) (for the sending).

In future, as @moneromooo-monero pointed out, use other channels for help / support. This is a bug tracker.

## moneromooo-monero | 2018-05-23T13:36:15+00:00
+invalid

# Action History
- Created by: somebodyLi | 2018-05-17T03:46:32+00:00
- Closed at: 2018-05-23T13:41:11+00:00
