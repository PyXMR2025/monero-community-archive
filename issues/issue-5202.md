---
title: 'Cannot import blockchain.raw: Block received at sync phase was marked as orphaned'
source_url: https://github.com/monero-project/monero/issues/5202
author: s-tikhomirov
assignees: []
labels: []
created_at: '2019-02-26T18:31:01+00:00'
updated_at: '2022-10-02T17:40:54+00:00'
type: issue
status: closed
closed_at: '2019-02-28T09:33:49+00:00'
---

# Original Description
I compiled Monero from sources (version 0.14.0) on Ubuntu 18.04 and am trying to sync the chain using `blockchain.raw` from [the official website](https://ww.getmonero.org/downloads/#source). I get the following error:

```
block 1625080 / 16855822019-02-26 18:24:04.092	    7fbdaec5abc0	ERROR	bcutil	src/blockchain_utilities/blockchain_import.cpp:222	Block verification failed, id = 6210311620b2076c61b60882f0a15793fc8529df4965a193dbd114b643febc59
2019-02-26 18:24:04.247	    7fbdaec5abc0	ERROR	bcutil	src/blockchain_utilities/blockchain_import.cpp:228	Block received at sync phase was marked as orphaned
```

The block with this hash doesn't exist on block explorers. Is the blockchain file corrupted?

# Discussion History
## moneromooo-monero | 2019-02-26T19:02:52+00:00
Add --log-level 1 to see the reason.

## moneromooo-monero | 2019-02-27T10:55:25+00:00
Also, this might be fixed by e98ae34e

## s-tikhomirov | 2019-02-28T09:33:49+00:00
Ok, problem "solved" by syncing from the network.

## caio-silva | 2022-10-02T17:36:59+00:00
I am having the same issue with node monero-x86_64-linux-gnu-v0.18.1.2

Running: monero-blockchain-import --stagenet --input-file blockchain.raw
Results in: 2022-10-02 17:19:00.912 E Block received at sync phase was marked as orphaned
                  2022-10-02 17:19:00.963	E Block received at sync phase was marked as orphaned

Running: monero-blockchain-import --stagenet --input-file blockchain.raw --log-level 1
Results in: 2022-10-02 17:25:30.856 E Block recognized as orphaned and rejected, id = <4b73ac1639e57a69b532ffaf8aa3c8b616baa8e0385f334bc61dd767bf055775>, height 161, parent in alt 0, parent in main 0 (parent <f5c1f941f64212407e729625f75b7254803713d55f62b52290cec73c44500a88>, current top <4f2c269102b90351aec4f5df6a704bbac2b8f079ab6563755837e1de448a4427>, chain height 4341)
2022-10-02 17:25:30.856	E Block received at sync phase was marked as orphaned
2022-10-02 17:25:32.220	E Block recognized as orphaned and rejected, id = <4b73ac1639e57a69b532ffaf8aa3c8b616baa8e0385f334bc61dd767bf055775>, height 161, parent in alt 0, parent in main 0 (parent <f5c1f941f64212407e729625f75b7254803713d55f62b52290cec73c44500a88>, current top <01587cf9abb1dc7694533513d9d54b74fc8dd3c67e97d3bd962b7181eec21e3b>, chain height 4381)
2022-10-02 17:25:32.220	E Block received at sync phase was marked as orphaned


I am updating from network but is way slower than importing. Any tips?

tks

## selsta | 2022-10-02T17:38:16+00:00
Where did you get the blockchain.raw file from?

## caio-silva | 2022-10-02T17:39:50+00:00
> Where did you get the blockchain.raw file from?

https://www.getmonero.org/downloads/#blockchain

## selsta | 2022-10-02T17:40:24+00:00
The website doesn't offer a stagenet blockchain.

## caio-silva | 2022-10-02T17:40:54+00:00
my bad. i thought passing the --stagenet would solve it. Thank you

# Action History
- Created by: s-tikhomirov | 2019-02-26T18:31:01+00:00
- Closed at: 2019-02-28T09:33:49+00:00
