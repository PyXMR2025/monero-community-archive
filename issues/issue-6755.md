---
title: how to run monero in a private chain?
source_url: https://github.com/monero-project/monero/issues/6755
author: jiebanghan
assignees: []
labels: []
created_at: '2020-08-11T08:48:29+00:00'
updated_at: '2020-09-03T07:02:44+00:00'
type: issue
status: closed
closed_at: '2020-09-03T07:02:44+00:00'
---

# Original Description
hi,  my question is how to run monero as a private chain mode and how to create the private  chain environment ?
Is there documents about  private chain? 
thank you .


# Discussion History
## Adreik | 2020-08-11T10:52:25+00:00
If you start monero in testnet/stagenet and with an --offline flag, this may suit your purposes? 

If you have other nodes you want to connect to it you might use the --add-exclusive-node launch flag and possibly some others.

And of course your chain must have mining on it to progress.

## moneromooo-monero | 2020-08-11T11:32:37+00:00
Also if you use more than one daemon: --no-zmq --data-dir /elsewhere --p2p-bind-port another --rpc-bind-port anotheragain

## SamsungGalaxyPlayer | 2020-08-11T13:29:33+00:00
Please also ask this question in the [Monero StackExchange](https://monero.stackexchange.com).

## jtgrassie | 2020-08-16T21:10:07+00:00
https://github.com/moneroexamples/private-testnet

## jiebanghan | 2020-08-17T08:32:40+00:00
thank you @jtgrassie and other nice men , and I do it according to [this link](https://github.com/moneroexamples/private-testnet) .But in 1st step , I come across a situation, the monero-wallet-cli.exe did not run out the wallet address.it is below:

```
root@DESKTOP-EEM7CKJ MINGW64 ~/testnet
$ monero-wallet-cli.exe --testnet --generate-new-wallet ~/testnet/wallet_01.bin  --restore-deterministic-wallet --electrum-seed="sequence atlas unveil summon pebbles tuesday beer rudely snake rockets different fuselage woven tagged bested dented vegan hover rapid fawns obvious muppet randomly seasons randomly" --password "" --log-file ~/testnet/wallet_01.log;
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.
```

Monero 'Nitrogen Nebula' (v0.16.0.0-c108c5e2f)
Logging to C:/tools/msys64/home/root/testnet/wallet_01.log
and

```
root@DESKTOP-EEM7CKJ MINGW64 ~/testnet
$ tail -10f wallet_01.log
2020-08-17 07:00:12.264 4184    INFO    logging contrib/epee/src/mlog.cpp:273  New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
```
maybe I cannot connect the testnet? how to solve it?By the way ,the environment is MSYS2 64bit.

## moneromooo-monero | 2020-08-17T14:36:40+00:00
What is the problem exactly ? The wallet output stops after "WARNING: Do not reuse..." and does not show a prompt ?

If you want logs, add --log-level 1, they're disabled by default for the wallet.

## jiebanghan | 2020-08-18T01:14:00+00:00
thank you @moneromooo-monero ! Yes, you  are  right.The wallet dose output stops after "WARNING: Do not reuse..." and does not show a prompt.
```
root@DESKTOP-EEM7CKJ MINGW64 ~
$ monero-wallet-cli.exe --testnet --generate-new-wallet ~/testnet/wallet_01.bin  --restore-deterministic-wallet --electrum-seed="sequence atlas unveil summon pebbles tuesday beer rudely snake rockets different fuselage woven tagged bested dented vegan hover rapid fawns obvious muppet randomly seasons randomly" --password "" --log-file ~/testnet/wallet_01.log --log-level 1
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Nitrogen Nebula' (v0.16.0.0-c108c5e2f)
Logging to C:/tools/msys64/home/root/testnet/wallet_01.log
```

root@DESKTOP-EEM7CKJ MINGW64 ~/testnet
```
$ cat wallet_01.log
2020-08-18 01:09:38.092 9692    INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2020-08-18 01:09:38.092 9692    INFO    logging contrib/epee/src/mlog.cpp:273   New log categories: *:INFO,global:INFO,stacktrace:INFO,logging:INFO,msgwriter:INFO,perf.*:DEBUG
2020-08-18 01:09:38.092 9692    INFO    msgwriter       src/common/scoped_message_writer.h:102  This is the command line monero wallet. It needs to connect to a monero
2020-08-18 01:09:38.093 9692    INFO    msgwriter       src/common/scoped_message_writer.h:102  daemon to work correctly.
2020-08-18 01:09:38.093 9692    INFO    msgwriter       src/common/scoped_message_writer.h:102  WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.
2020-08-18 01:09:38.093 9692    INFO    msgwriter       src/common/scoped_message_writer.h:102  Monero 'Nitrogen Nebula' (v0.16.0.0-c108c5e2f)
2020-08-18 01:09:38.093 9692    INFO    wallet.wallet2  src/wallet/wallet_args.cpp:211  Setting log level = 1
2020-08-18 01:09:38.093 9692    INFO    wallet.wallet2  src/wallet/wallet_args.cpp:217  Logging to: C:/tools/msys64/home/root/testnet/wallet_01.log
2020-08-18 01:09:38.093 9692    INFO    msgwriter       src/common/scoped_message_writer.h:102  Logging to C:/tools/msys64/home/root/testnet/wallet_01.log
2020-08-18 01:09:38.139 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'asa' is shorter than its prefix length, 4
2020-08-18 01:09:38.139 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'ave' is shorter than its prefix length, 4
2020-08-18 01:09:38.140 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'boa' is shorter than its prefix length, 4
2020-08-18 01:09:38.141 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'cal' is shorter than its prefix length, 4
2020-08-18 01:09:38.142 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'dar' is shorter than its prefix length, 4
2020-08-18 01:09:38.143 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'don' is shorter than its prefix length, 4
2020-08-18 01:09:38.143 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'dos' is shorter than its prefix length, 4
2020-08-18 01:09:38.143 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'eco' is shorter than its prefix length, 4
2020-08-18 01:09:38.143 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'eje' is shorter than its prefix length, 4
2020-08-18 01:09:38.144 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'fax' is shorter than its prefix length, 4
2020-08-18 01:09:38.144 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'feo' is shorter than its prefix length, 4
2020-08-18 01:09:38.144 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'fin' is shorter than its prefix length, 4
2020-08-18 01:09:38.145 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'gen' is shorter than its prefix length, 4
2020-08-18 01:09:38.146 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'gol' is shorter than its prefix length, 4
2020-08-18 01:09:38.146 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'haz' is shorter than its prefix length, 4
2020-08-18 01:09:38.146 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'ira' is shorter than its prefix length, 4
2020-08-18 01:09:38.147 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'luz' is shorter than its prefix length, 4
2020-08-18 01:09:38.148 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'mar' is shorter than its prefix length, 4
2020-08-18 01:09:38.148 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'mes' is shorter than its prefix length, 4
2020-08-18 01:09:38.148 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'mil' is shorter than its prefix length, 4
2020-08-18 01:09:38.149 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'oca' is shorter than its prefix length, 4
2020-08-18 01:09:38.149 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'ojo' is shorter than its prefix length, 4
2020-08-18 01:09:38.150 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'ola' is shorter than its prefix length, 4
2020-08-18 01:09:38.150 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'oro' is shorter than its prefix length, 4
2020-08-18 01:09:38.150 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'oso' is shorter than its prefix length, 4
2020-08-18 01:09:38.150 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'pan' is shorter than its prefix length, 4
2020-08-18 01:09:38.150 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'pez' is shorter than its prefix length, 4
2020-08-18 01:09:38.150 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'pie' is shorter than its prefix length, 4
2020-08-18 01:09:38.151 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'red' is shorter than its prefix length, 4
2020-08-18 01:09:38.151 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'res' is shorter than its prefix length, 4
2020-08-18 01:09:38.152 9692    WARNING default src/mnemonics/language_base.h:132       Espa帽ol word 'rey' is shorter than its prefix length, 4
2020-08-18 01:09:38.262 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'out' is shorter than its prefix length, 4
2020-08-18 01:09:38.262 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'eye' is shorter than its prefix length, 4
2020-08-18 01:09:38.262 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thin
2020-08-18 01:09:38.262 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'too' is shorter than its prefix length, 4
2020-08-18 01:09:38.262 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'try' is shorter than its prefix length, 4
2020-08-18 01:09:38.262 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'cry' is shorter than its prefix length, 4
2020-08-18 01:09:38.262 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'end' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'off' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: some
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'ask' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: ever
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'got' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'yet' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'run' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'own' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'god' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'new' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'two' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'use' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: some
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'any' is shorter than its prefix length, 4
2020-08-18 01:09:38.263 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'sky' is shorter than its prefix length, 4
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'put' is shorter than its prefix length, 4
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: happ
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: star
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'red' is shorter than its prefix length, 4
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: ever
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'air' is shorter than its prefix length, 4
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'lip' is shorter than its prefix length, 4
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'hit' is shorter than its prefix length, 4
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: real
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: brea
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: agai
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'fly' is shorter than its prefix length, 4
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: unde
2020-08-18 01:09:38.264 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: some
2020-08-18 01:09:38.265 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: real
2020-08-18 01:09:38.265 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'guy' is shorter than its prefix length, 4
2020-08-18 01:09:38.265 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'eat' is shorter than its prefix length, 4
2020-08-18 01:09:38.265 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: brea
2020-08-18 01:09:38.265 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: dark
2020-08-18 01:09:38.265 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: alon
2020-08-18 01:09:38.265 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: beau
2020-08-18 01:09:38.266 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: hear
2020-08-18 01:09:38.266 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'kid' is shorter than its prefix length, 4
2020-08-18 01:09:38.266 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'dad' is shorter than its prefix length, 4
2020-08-18 01:09:38.266 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'war' is shorter than its prefix length, 4
2020-08-18 01:09:38.266 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'act' is shorter than its prefix length, 4
2020-08-18 01:09:38.266 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: chan
2020-08-18 01:09:38.266 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: chil
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'sea' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'lot' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'sad' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'mom' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'few' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: mean
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: real
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'bit' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: happ
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'men' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'age' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'ice' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thro
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'leg' is shorter than its prefix length, 4
2020-08-18 01:09:38.267 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: good
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: know
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: shou
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: pret
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'joy' is shorter than its prefix length, 4
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'dry' is shorter than its prefix length, 4
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: clea
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'son' is shorter than its prefix length, 4
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: sorr
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'hug' is shorter than its prefix length, 4
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'sat' is shorter than its prefix length, 4
2020-08-18 01:09:38.268 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: fina
2020-08-18 01:09:38.269 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: sile
2020-08-18 01:09:38.269 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: ange
2020-08-18 01:09:38.269 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: cont
2020-08-18 01:09:38.269 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'dog' is shorter than its prefix length, 4
2020-08-18 01:09:38.269 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: give
2020-08-18 01:09:38.270 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: your
2020-08-18 01:09:38.270 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'hey' is shorter than its prefix length, 4
2020-08-18 01:09:38.270 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'pay' is shorter than its prefix length, 4
2020-08-18 01:09:38.270 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: take
2020-08-18 01:09:38.270 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: some
2020-08-18 01:09:38.270 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: crea
2020-08-18 01:09:38.270 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: forg
2020-08-18 01:09:38.270 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'rip' is shorter than its prefix length, 4
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'job' is shorter than its prefix length, 4
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: laug
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: some
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stor
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'beg' is shorter than its prefix length, 4
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: simp
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'win' is shorter than its prefix length, 4
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: flow
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stre
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'gun' is shorter than its prefix length, 4
2020-08-18 01:09:38.271 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: heav
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: ever
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: shou
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stra
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thro
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'ash' is shorter than its prefix length, 4
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: imag
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: warm
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: yell
2020-08-18 01:09:38.272 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: frie
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: prob
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'six' is shorter than its prefix length, 4
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: nigh
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thou
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: wors
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: bare
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: crea
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'art' is shorter than its prefix length, 4
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: pass
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: quic
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: brok
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'box' is shorter than its prefix length, 4
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: chil
2020-08-18 01:09:38.273 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'tie' is shorter than its prefix length, 4
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: fore
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'pen' is shorter than its prefix length, 4
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stre
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: comp
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: coun
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'wet' is shorter than its prefix length, 4
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stre
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: forg
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: plan
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: both
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: bott
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'fix' is shorter than its prefix length, 4
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: forg
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: sure
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: teac
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: gent
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: writ
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: chai
2020-08-18 01:09:38.274 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: them
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'cup' is shorter than its prefix length, 4
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: expe
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: free
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'pop' is shorter than its prefix length, 4
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: soft
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stra
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'bar' is shorter than its prefix length, 4
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: love
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: clos
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: hand
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'key' is shorter than its prefix length, 4
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'won' is shorter than its prefix length, 4
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: dirt
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: pres
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: swea
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: ever
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: grow
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: know
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: numb
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: pres
2020-08-18 01:09:38.275 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'buy' is shorter than its prefix length, 4
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'add' is shorter than its prefix length, 4
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: cont
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: dist
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: purp
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thre
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: gras
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: inno
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: shad
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: some
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'toe' is shorter than its prefix length, 4
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: visi
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: cons
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'ink' is shorter than its prefix length, 4
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: sile
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stre
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'bus' is shorter than its prefix length, 4
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'mix' is shorter than its prefix length, 4
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: pray
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: pres
2020-08-18 01:09:38.276 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: trai
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'bag' is shorter than its prefix length, 4
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: expl
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: fami
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: refl
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: scen
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: self
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: wond
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: atte
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: birt
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: perf
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: cons
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'egg' is shorter than its prefix length, 4
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: eter
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: floo
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: scre
2020-08-18 01:09:38.277 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: buil
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: desp
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: mess
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stri
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: clea
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: imag
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: less
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stro
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: bloo
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: foot
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'mud' is shorter than its prefix length, 4
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'nod' is shorter than its prefix length, 4
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: rela
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: sudd
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: admi
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: blin
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: brea
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: cons
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: cree
2020-08-18 01:09:38.278 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: diff
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: empt
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: plan
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'rub' is shorter than its prefix length, 4
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: some
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: tigh
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: brea
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: dese
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: gran
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: plea
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: powe
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thre
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'bee' is shorter than its prefix length, 4
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: blan
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: butt
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: care
2020-08-18 01:09:38.279 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: comp
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: deep
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: drea
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: gott
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: gree
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: repl
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: spin
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: chil
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: coll
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: depr
2020-08-18 01:09:38.280 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: even
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: grou
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: hone
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: nerv
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: pain
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: poet
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: prin
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: show
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stai
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stea
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: trea
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: chee
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: crim
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: exis
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'fog' is shorter than its prefix length, 4
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: foot
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'gay' is shorter than its prefix length, 4
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: illu
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stud
2020-08-18 01:09:38.281 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: supp
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: appr
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: coll
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: conf
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: crea
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: girl
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'hop' is shorter than its prefix length, 4
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: moon
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: peac
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'pig' is shorter than its prefix length, 4
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: scre
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thro
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thro
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'wow' is shorter than its prefix length, 4
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: cour
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'dim' is shorter than its prefix length, 4
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'hum' is shorter than its prefix length, 4
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'led' is shorter than its prefix length, 4
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: natu
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: near
2020-08-18 01:09:38.282 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: need
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: peac
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: perf
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: shin
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: shoo
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'sob' is shorter than its prefix length, 4
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stol
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'tap' is shorter than its prefix length, 4
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: boun
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: deci
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: desp
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'dig' is shorter than its prefix length, 4
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'dot' is shorter than its prefix length, 4
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: hear
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'odd' is shorter than its prefix length, 4
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: quie
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: sent
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stra
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: unde
2020-08-18 01:09:38.283 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: whis
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: anyw
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'bid' is shorter than its prefix length, 4
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: bloo
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: care
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: comp
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: desc
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: doub
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: drea
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: driv
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: even
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: gran
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: hung
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: show
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'shy' is shorter than its prefix length, 4
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: weak
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: wors
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: wort
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: afte
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: conc
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: draw
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'due' is shorter than its prefix length, 4
2020-08-18 01:09:38.284 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: free
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: harm
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: hope
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: quit
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: resp
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: salt
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: shee
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: soci
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'aim' is shorter than its prefix length, 4
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: awak
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: beli
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: bran
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: chee
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: conf
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: conn
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: ever
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: expr
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'fan' is shorter than its prefix length, 4
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'fur' is shorter than its prefix length, 4
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: glor
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: igno
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'law' is shorter than its prefix length, 4
2020-08-18 01:09:38.285 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: migh
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: pati
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: poss
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stri
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stri
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: suff
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'cap' is shorter than its prefix length, 4
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: cert
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: comp
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: crea
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: deli
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: drag
2020-08-18 01:09:38.286 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: ever
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: fore
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: form
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: frig
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'gas' is shorter than its prefix length, 4
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: invi
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: poss
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'raw' is shorter than its prefix length, 4
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: scar
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: seve
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: slig
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'tea' is shorter than its prefix length, 4
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: terr
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thre
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: tric
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'awe' is shorter than its prefix length, 4
2020-08-18 01:09:38.287 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: char
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: chea
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: comm
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: comp
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: crea
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: defe
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: desp
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: dest
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'dew' is shorter than its prefix length, 4
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: dust
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: expl
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'foe' is shorter than its prefix length, 4
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: free
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: guil
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: heal
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: impo
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'jaw' is shorter than its prefix length, 4
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: king
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: mist
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'ode' is shorter than its prefix length, 4
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: path
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:132       EnglishOld word 'pie' is shorter than its prefix length, 4
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: reve
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: scra
2020-08-18 01:09:38.288 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: spir
2020-08-18 01:09:38.289 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: stra
2020-08-18 01:09:38.289 9692    WARNING default src/mnemonics/language_base.h:148       Duplicate prefix in EnglishOld word list: thro
2020-08-18 01:09:38.289 9692    INFO    mnemonic        src/mnemonics/electrum-words.cpp:237    Checksum is valid
2020-08-18 01:09:38.289 9692    INFO    mnemonic        src/mnemonics/electrum-words.cpp:163    Full match for language English
2020-08-18 01:09:38.290 9692    INFO    mnemonic        src/mnemonics/electrum-words.cpp:237    Checksum is valid

root@DESKTOP-EEM7CKJ MINGW64 ~/testnet
$
```


## moneromooo-monero | 2020-08-18T01:43:36+00:00
At that point, it's printing:

> Enter seed offset passphrase, empty if none:

It does flush cout, where it's printed this message. If the message does not appear, either you're piping the output somewhere (though a flush ought to flush the pipe too) or there's a bug in your libc that skips the flush.

In any case, to not set an offset, just press enter, and it'll go on creating your wallet.

Do you have any fancy setup on your console that might explain the lack of printing even when flushed ?

## jiebanghan | 2020-08-18T02:35:48+00:00
thank you @moneromooo-monero , my aim is to study the great monero and you are right and when I press enter it shows below：
```
Generated new wallet: 9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8
View key: 42ba20adb337e5eca797565be11c9adb0a8bef8c830bccc2df712535d3b8f608
**********************************************************************
Your wallet has been generated!
To start synchronizing with the daemon, use the "refresh" command.
Use the "help" command to see a simplified list of available commands.
Use the "help_advanced" command to see an advanced list of available commands.
Use "help_advanced <command>" to see a command's documentation.
Always use the "exit" command when closing monero-wallet-cli to save
your current session's state. Otherwise, you might need to synchronize
your wallet again (your wallet keys are NOT at risk in any case).


NOTE: the following 25 words can be used to recover access to your wallet. Write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.

sequence atlas unveil summon pebbles tuesday beer rudely
snake rockets different fuselage woven tagged bested dented
vegan hover rapid fawns obvious muppet randomly seasons randomly
**********************************************************************
Error: wallet failed to connect to daemon: http://localhost:28081. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
Restore from specific blockchain height (optional, default 0):
```

then I input enter and it stops again and how to solve it ? 
And you ask me "Do you have any fancy setup on your console that might explain the lack of printing even when flushed ?"
my answer is no, I haven't , I will try xshell.
thank you agin with all my heart.

## moneromooo-monero | 2020-08-18T13:15:58+00:00
Did it show "Enter seed offset passphrase, empty if none:" *after* you pressed enter ?

## jiebanghan | 2020-08-19T09:34:52+00:00
thank you @moneromooo-monero ! no , it shows none after I pressed enter . What is the reason? thank you.

however these files were created.
wallet_01.bin
wallet_01.bin.address.txt
wallet_01.bin.keys
wallet_01.log


# Action History
- Created by: jiebanghan | 2020-08-11T08:48:29+00:00
- Closed at: 2020-09-03T07:02:44+00:00
