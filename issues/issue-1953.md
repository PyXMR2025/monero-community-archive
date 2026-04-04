---
title: 'Document: How big is the monero blockchain?'
source_url: https://github.com/monero-project/monero-site/issues/1953
author: maltfield
assignees: []
labels:
- 📚 docs
created_at: '2022-04-28T11:30:29+00:00'
updated_at: '2025-08-07T19:40:14+00:00'
type: issue
status: closed
closed_at: '2025-08-07T19:40:14+00:00'
---

# Original Description
Please add some documentation to the website that can help answer the question:

```
I have X GB of free space on my disk. Will the monero blockchain currently fit on it?
```

### Why

First some facts:

1. There are significant benefits for running your own walllet with the full blockchain synced locally (even if not mining)
1. The benefits of downloading the full blockchain locally are especially true for Monero (a privacy coin)
1. For may people around the world, it can take weeks or months to download the monero blockchain.
1. The official monero website currently does not clearly answer the question: how many GB do I need to store the Monero blockchain on my disk *as of this morning*?
1. The official monero website currently does not clearly answer the question: how can I estimate how many GB I will need to store the Monero blockchain X months into the future?

**Before a user even begins** to sync the blockchain, they should be able to *quickly* determine if they have enough disk space to store it. And the same page should guide the reader in how to make an educated guess at how long this drive will suffice to hold the blockchain as it grows, and when they can roughly expect to upgrade their disk size. This information should be so easily accessible that even non-technical users can quickly ascertain if their disk is big enough for their needs.

I'm a very technical user, and I found this information to be stiflingly hard to determine. I posted about it on stackexchange, and got some decent information that suggested the blockchain is 90G -- so it should fit on my 128G disk.

 * https://monero.stackexchange.com/questions/13570/what-is-the-current-monero-blockchain-size-in-gb/

It took me 4 weeks to finish syncing the blockchain, and I now know that -- err -- I cannot fit the blockchain onto my 128G disk :facepalm:

IMHO:

1. I shouldn't have to sync the whole blockchain to figure out if my disk is big enough to use it
2. I should be able to quickly get this information from the official monero website before downloading the software

### Solution

The official monero website should document very clearly for the layman:

1. How big is the monero blockchain currently
2. How can the reader extrapolate the growth of the blockchain over time

IMHO, more important than the website saying "the blockchain is currently XYZ GB large", it should guide the reader how to figure out the current size of the blockchain (obviously without requiring them to download the blockchain first).

# Discussion History
## maltfield | 2022-04-28T11:39:09+00:00
The website already has an FAQ item "How big is the Monero blockchain?"

 * https://www.getmonero.org/get-started/faq/#anchor-block-size
 * https://github.com/monero-project/monero-site/pull/1442

While I do appreciate this information, note that this does *not* satisfy this request.

This request is to add to the FAQ's Answer: a whole document expounding:

1. how the user can determine the blockchain's size *as of "today"* and
2. guide them in extrapolating how big it will be X months into the future.

## maltfield | 2022-04-28T11:41:00+00:00
inb4 pruning: I don't mind if you additionally include info about pruning into the documentation, of course! But the size of the unpruned blockchain should also be documented.

## erciccione | 2022-05-01T09:51:44+00:00
Hello @maltfield, thanks for opening the issue. Just leaving here that we have different faq entries about the size of the blockchain. See https://www.getmonero.org/get-started/faq/#anchor-block-size

Agree would be useful to expand.

## maltfield | 2022-05-01T10:10:13+00:00
I'm trying to figure out how this can be achieved. Per the suggestion on [stack exchange](https://monero.stackexchange.com/questions/13570/what-is-the-current-monero-blockchain-size-in-gb/), I know that:

1. I can get a list of public monero nodes from https://monero.fail/
2. I can query any of the above monero nodes' json rpc endpoint with `curl`

For example

```
user@disp7529:~$ curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' https://node.monerod.org/json_rpc | grep 'database_size'
    "database_size": 53687091200,
user@disp7529:~$ 
```

The above database size is 53687091200 bytes = 50 GB.

I know now (only because I just downloaded the whole blockchain) that this is clearly not an unpruned blockchain size.

This begs the question: Is it currently possible to query a node and ask "Is your database pruned?"

If it's not currently possible to determine via the json_rpc endpoint if the given node's DB is pruned, can we please add that feature so that users have a way to iterate though a bunch of nodes until they find one with an unpruned DB to determine the size of the unpruned blockchain size?

## DeeDeeRanged | 2022-09-07T12:14:11+00:00
@maltfield Saw something like that query bu t it had a syntax error in it. Managed to solved it like this in a script:

#!/bin/bash
#set -x
x=$(curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' https://node.monerod.org/json_rpc | grep 'database_size' | sed -e 's/.*[^0-9]\([0-9]\+\)[^0-9]*$/\1/');
	y=$((x/1024/1024/1024));
	echo -e "\tCurrent uncompressed Monero block chain is: "$y"GB"

I'll try for myself to improve on it so when I call the script database_size.sh http;//whatever.com:18081/18089 so you are able to just any node to find out the size of the database without having it to change it in the script.

## maltfield | 2022-09-08T17:33:14+00:00
awesome! unfortunately I get a syntax error on that too

```
user@disp3192:~$ x=$(curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' https://node.monerod.org/json_rpc | grep 'database_size' | sed -e 's/.[^0-9]([0-9]+)[^0-9]$/\1/');
sed: -e expression #1, char 28: invalid reference \1 on `s' command's RHS
user@disp3192:~$ 
```

Looks like it's just `sed` because this works fine

```
user@disp3192:~$ x=$(curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' https://node.monerod.org/json_rpc | grep 'database_size');
user@disp3192:~$ echo $x
"database_size": 53687091200,
user@disp3192:~$ 
```

## DeeDeeRanged | 2022-09-08T18:38:47+00:00
Actually it my mistake it should have been:

#!/bin/bash
#set -x

x=$(curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' http://xmr.coinspace.net:18081/json_rpc | grep database_size | sed -e 's/.*[^0-9]\([0-9]\+\)[^0-9]*$/\1/');
	y=$((x/1024/1024/1024));
	echo -e "\tCurrent uncompressed Monero block chain is: "$y"GB"

I used HTTPS instead of HTTP and made an error in sed. Just double chechked and it worked running against various nodes on monero.fail apparantly something weird is going on with copy pasting on github

[database-size.sh.zip](https://github.com/monero-project/monero-site/files/9529816/database-size.sh.zip)


## maltfield | 2022-09-09T14:40:10+00:00
Still sed errors :(

```
user@disp14:~$ x=$(curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' http://xmr.coinspace.net:18081/json_rpc | grep database_size | sed -e 's/.[^0-9]([0-9]+)[^0-9]$/\1/');
sed: -e expression #1, char 28: invalid reference \1 on `s' command's RHS
user@disp14:~$ echo $x

user@disp14:~$ 
```

## maltfield | 2022-09-09T14:47:03+00:00
Here's an alternative without sed :)

```
x=$(curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' http://xmr.coinspace.net:18081/json_rpc | grep database_size | cut -d: -f2 | grep -o "[0-9]*");
y=$((x/1024/1024/1024));
echo -e "\tCurrent uncompressed Monero block chain is: "$y"GB"
```

Example run:

```
user@disp14:~$ x=$(curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' http://xmr.coinspace.net:18081/json_rpc | grep database_size | cut -d: -f2 | grep -o "[0-9]*");
user@disp14:~$ y=$((x/1024/1024/1024));
user@disp14:~$ echo -e "\tCurrent uncompressed Monero block chain is: "$y"GB"
	Current uncompressed Monero block chain is: 280GB
user@disp14:~$ 
```

## maltfield | 2022-09-09T14:48:17+00:00
But how do we know that's the actual uncompressed, unpruned monero block chain size and not the pruned size?

## zigomi | 2022-11-30T03:19:43+00:00
@maltfield what's the muzzle on your face for? 

## puppymati | 2023-04-11T23:42:40+00:00
I feel like the answers above are a bit overkill.
Instead by using [jq](https://stedolan.github.io/jq/) it's as simple as using this oneliner
```bash
echo $((`curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' http://node.moneroworld.com:18089/json_rpc | jq .result.database_size` / 1024 / 1024 / 1024)) GB
```
This is much more redable, portable and doesn't pollute the scope with temp variables.

## maltfield | 2023-05-08T18:27:18+00:00
works for me, just requires `jq` to be installed.

```
user@disp9870:~$ cat /etc/issue
Debian GNU/Linux 11 \n \l

user@disp9870:~$ 

user@disp9870:~$ echo $((`curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' http://node.moneroworld.com:18089/json_rpc | jq .result.database_size` / 1024 / 1024 / 1024)) GB
bash: jq: command not found
(23) Failed writing body
bash: / 1024 / 1024 / 1024: syntax error: operand expected (error token is "/ 1024 / 1024 / 1024")
user@disp9870:~$ 

user@disp9870:~$ sudo apt-get install jq
...
user@disp9870:~$ 

user@disp9870:~$ echo $((`curl -sd '{"jsonrpc":"2.0","id":"0","method":"get_info"}' http://node.moneroworld.com:18089/json_rpc | jq .result.database_size` / 1024 / 1024 / 1024)) GB
155 GB
user@disp9870:~$ 
```

Above output in Debian 11.

...but afaict **this doesn't solve the question of "*how much space do I need if I'm syncing the monero blockchain for the first time*"** because the output is the compressed blockchain. First sync (before pruning) would be much larger, iirc.

## puppymati | 2023-05-08T20:26:38+00:00
I am not expert so take this with a grain of salt, but due to the nature of the blokchain I do not think it is possible to have a proper "how much space do I need if I'm syncing the monero blockchain for the first time" size. There might be ways to extimate it but querying the database size is probably the closest thing to that we have right now.

## jermanuts | 2025-08-06T01:08:56+00:00
https://docs.getmonero.org/technical-specs/#current-blockchain-size

# Action History
- Created by: maltfield | 2022-04-28T11:30:29+00:00
- Closed at: 2025-08-07T19:40:14+00:00
