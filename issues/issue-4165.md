---
title: 'Error: Couldn''t connect to daemon: 127.0.0.1:18081 - Is it because two or
  more Monero GUI Wallets are not allowed on the same device?'
source_url: https://github.com/monero-project/monero-gui/issues/4165
author: ch9PcB
assignees: []
labels: []
created_at: '2023-05-01T13:18:51+00:00'
updated_at: '2024-11-24T15:11:51+00:00'
type: issue
status: closed
closed_at: '2023-05-03T08:11:06+00:00'
---

# Original Description
Below are the software that I use on my device (Intel 12th generation CPU, 24GB of RAM, 1TB of PCIe NVMe SSD):

Debian 11.7.0, 64bit (backported kernel version 6.1.15-1~bpo11+1)
Monero GUI Wallet, 0.18.2.2 - Fluorine Fermi

The first wallet was created about two years ago, and the path to the wallet points to a directory/folder of a different partition of the SSD. Let's call the folder `monero` and the partition is called `K`. This wallet does not give me problems at all. (The fully pruned blockchain of about 55GB had been downloaded to the folder called `monero` on the `K` partition.)

A few days ago, I decided to create a new wallet with a new seed. The path to this second wallet points to a folder that is called `monero-2` and it resides on the `K` partition as well.  I realized that I needed to download about 57.2GB of pruned blockchain.

**Problem**

My second wallet is unable to download the pruned blockchain of 57.2GB of data from Monero network.

Below is a snippet of the error log:

```
[29/4/23 10:05 AM] 2023-04-29 10:05:21.117 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/4/23 10:05 AM] 2023-04-29 10:05:45.414 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/4/23 10:05 AM] 2023-04-29 10:05:48.821 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
```

**Questions**

1. The reason my second wallet is unable to download the pruned blockchain is that there is already an existing wallet on the same partition but in a different folder. The software Monero GUI Wallet is confused. Is that correct?

2a. Suppose the software Monero GUI Wallet does allow two or more wallets to exist on the same device and partition. What is the cause of my second wallet not being able to download the blockchain?

2b. Instead of downloading the entire pruned blockchain for my second wallet, can I just copy `data.mdb` in the folder called `lmdb` of the first wallet and paste it into my second wallet?


# Discussion History
## selsta | 2023-05-01T13:24:15+00:00
Why do you download two separate blockchains? You can run two wallets with a single blockchain. You simply open the other wallet file. The location of the wallet file is irrelevant.

> The reason my second wallet is unable to download the pruned blockchain is that there is already an existing wallet on the same partition but in a different folder. The software Monero GUI Wallet is confused. Is that correct?

No.

> 2a. Suppose the software Monero GUI Wallet does allow two or more wallets to exist on the same device and partition. What is the cause of my second wallet not being able to download the blockchain?

Unclear based on the info you have provided. The error log doesn't show anything relevant.

> 2b. Instead of downloading the entire pruned blockchain for my second wallet, can I just copy data.mdb in the folder called lmdb of the first wallet and paste it into my second wallet?

I don't understand why you want to separate blockchains in the first place. The correct solution would be having a single blockchain.

## ch9PcB | 2023-05-01T19:55:43+00:00
> Why do you download two separate blockchains? You can run two wallets with a single blockchain.

I didn't know that I could run two or more wallets with a single blockchain.

Can you show me how please? I have searched the tutorials, documentations and posts in the official Monero wiki and Reddit pages and also using Google Search and none of them showed me how to run two or more wallets using a single blockchain.

> You simply open the other wallet file.

Did you mean the second wallet that was recently created? Before I open the second wallet, I must create it, yes? During the process of creating it, I need to specify the name of the second wallet, path of the wallet and password, yes? I also must write down the new 25-word seed, yes?

After creating the new 25-word seed, the next page shows that I need to download about 55GB of the data of the blockchain.

So please show me how to tell the software `Monero GUI Wallet` to have the second wallet use the blockchain of the first wallet?

>The location of the wallet file is irrelevant.

I have just learned something new.

>Unclear based on the info you have provided. The error log doesn't show anything relevant.

Please show me which log to give it to you.

>I don't understand why you want to separate blockchains in the first place. The correct solution would be having a single blockchain.

Monero wiki, posts on Reddit and Google Search do not provide instructions or guides on how to create two or more wallets using a single blockchain.





## selsta | 2023-05-01T20:02:56+00:00
> After creating the new 25-word seed, the next page shows that I need to download about 55GB of the data of the blockchain.

<img width="1026" alt="wizard" src="https://user-images.githubusercontent.com/7697454/235521201-2b5638ae-13dc-4589-9c5e-66b8c1f82133.png">

Do you mean this screen? You simply click on next like you did while creating the first wallet. If you selected a custom location you set the same custom location.

## ch9PcB | 2023-05-01T21:03:18+00:00
 > Do you mean this screen? You simply click on next like you did while creating the first wallet. If you selected a custom location you set the same custom location.

Your screenshot is different from what I had. There's a word `reset` in orange. I clicked `reset` and checked the box `Prune blockchain`. After doing that, I clicked `Browse` to specify the custom location of the blockchain.

## selsta | 2023-05-01T21:04:28+00:00
The reset button just means that you can reset the blockchain location back to the default one if you changed it.

## ch9PcB | 2023-05-03T04:46:04+00:00
@selsta

I managed to learn how to create a second, third and subsequent wallet successfully.

After you have read this comment of mine, you may proceed to close this issue.

Thanks.

## diamondsteel259 | 2023-08-03T16:47:16+00:00
Hi @selsta im currently exercising the same problem however im not running 2 wallets i simply opened up xmrig while the blockchain was downloading on the GUI. I'm still quite new at all of this but when i closed my GUI and opened xmrig and let that run for a while my pc shut off due to power outages in my sh1t country south africa. When i powered it on again and opened everything up daemon wouldnt connect and all i got from log was.


2023-08-03 16:24:08.046	9972	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-08-03 16:24:11.144	9972	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2023-08-03 16:24:14.212	2280	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-08-03 16:24:14.212	2280	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-08-03 16:24:17.031	2280	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Couldn't connect to daemon: 127.0.0.1:18081
2023-08-03 16:28:35.666	10740	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-08-03 16:28:35.666	10740	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.2.2-release)
2023-08-03 16:28:35.666	10740	INFO	global	src/daemon/protocol.h:53	Initializing cryptonote protocol...
2023-08-03 16:28:35.666	10740	INFO	global	src/daemon/protocol.h:58	Cryptonote protocol initialized OK
2023-08-03 16:28:35.666	10740	INFO	global	src/daemon/core.h:64	Initializing core...
2023-08-03 16:28:35.666	10740	INFO	global	src/cryptonote_core/cryptonote_core.cpp:523	Loading blockchain from folder C:\Program Files\Monero GUI Wallet\p2pool\lmdb ...
2023-08-03 16:28:35.728	10740	WARNING	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:75	Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2023-08-03 16:28:35.728	10740	INFO	global	src/daemon/protocol.h:75	Stopping cryptonote protocol...
2023-08-03 16:28:35.728	10740	INFO	global	src/daemon/protocol.h:79	Cryptonote protocol stopped successfully
2023-08-03 16:28:35.728	10740	ERROR	daemon	src/daemon/main.cpp:364	Exception in main! Failed to open db handle for m_blocks : MDB_CORRUPTED: Located page was wrong type - you may want to start with --db-salvage
2023-08-03 16:28:37.647	10256	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO
2023-08-03 16:28:37.647	10256	INFO	global	src/daemon/main.cpp:296	Monero 'Fluorine Fermi' (v0.18.2.2-release)

Please help.

## n0ping | 2024-09-03T16:34:26+00:00
i got this error when i did restart my ubuntu. it works now when i opend the folder i save the blockchain in (external disk). my error must be becous Monero GUI did not find the folder

## OrmandoA | 2024-11-24T15:11:50+00:00
> Hola, actualmente estoy ejerciendo el mismo problema, sin embargo, no estoy ejecutando 2 billeteras, simplemente abrí xmrig mientras la cadena de bloques se descargaba en la GUI. Todavía soy bastante nuevo en todo esto, pero cuando cerré mi GUI y abrí xmrig y lo dejé funcionar por un tiempo, mi PC se apagó debido a cortes de energía en mi país sh1t, Sudáfrica. Cuando lo encendí de nuevo y abrí todo, el demonio no se conectaba y todo lo que obtuve del registro fue.
> 
> 03/08/2023 16:08/2023 24:08.046 9972 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release) 2023-08-03 16:24:11.144 9972 ERROR msgwriter src/common/scoped_message_writer.h:102 Error: No se pudo conectar al demonio: 127.0.0.1:18081 2023-08-03 16:24:14.212 2280 INFO logging contrib/epee/src/mlog.cpp:273 Nuevas categorías de registro: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL, global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO 2023-08-03 16:24:14.212 2280 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release) 2023-08-03 16:24:17.031 2280 ERROR msgwriter src/common/scoped_message_writer.h:102 Error: No se pudo conectar al demonio: 127.0.0.1:18081 2023-08-03 16:28:35.666 10740 INFO registro contrib/epee/src/mlog.cpp:273 Nuevas categorías de registro: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR,stacktrace:INFO,logging:INFO,msgwriter:INFO 2023-08-03 16:28:35.666 10740 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release) 2023-08-03 16:28:35.666 10740 INFO global src/daemon/protocol.h:53 Inicializando el protocolo cryptonote... 2023-08-03 16:28:35.666 10740 INFO global src/daemon/protocol.h:58 Protocolo Cryptonote inicializado OK 2023-08-03 16:28:35.666 10740 INFO global src/daemon/core.h:64 Inicializando core... 2023-08-03 16:28:35.666 10740 INFO global src/cryptonote_core/cryptonote_core.cpp:523 Cargando blockchain desde la carpeta C:\Program Files\Monero GUI Wallet\p2pool\lmdb ... 2023-08-03 16:28:35.728 10740 ADVERTENCIA blockchain.db.lmdb src/blockchain_db/lmdb/db_lmdb.cpp:75 No se pudo abrir el identificador de la base de datos para m_blocks : MDB_CORRUPTED: La página ubicada era de tipo incorrecto: es posible que desee comenzar con --db-salvage 2023-08-03 16:28:35.728 10740 INFO global src/daemon/protocol.h:75 Deteniendo el protocolo cryptonote... 2023-08-03 16:28:35.728 10740 INFO global src/daemon/protocol.h:79 El protocolo Cryptonote se detuvo con éxito 2023-08-03 16:28:35.728 10740 ERROR daemon src/daemon/main.cpp:364 ¡Excepción en main! No se pudo abrir el identificador de la base de datos para m_blocks : MDB_CORRUPTED: La página ubicada era de tipo incorrecto: es posible que desee comenzar con --db-salvage 2023-08-03 16:28:37.647 10256 INFO logging contrib/epee/src/mlog.cpp:273 Nuevas categorías de registro: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,daemon.rpc:FATAL,global:INFO,verify:FATAL,serialization:FATAL,daemon.rpc.payment:ERROR, stacktrace:INFO,logging:INFO,msgwriter:INFO 2023-08-03 16:28:37.647 10256 INFO global src/daemon/main.cpp:296 Monero 'Fluorine Fermi' (v0.18.2.2-release)
> 
> Por favor, ayuda.

Hola saludos a distancia amigo te digo, tu error es debido a que se ha dañado el archivo, al aparse intencionalmente se dañan los bloques, lo que te quedaria hacer es borrar y reiniciar la descarga ya no se puede hacer nada mas. SALUDOS...

# Action History
- Created by: ch9PcB | 2023-05-01T13:18:51+00:00
- Closed at: 2023-05-03T08:11:06+00:00
