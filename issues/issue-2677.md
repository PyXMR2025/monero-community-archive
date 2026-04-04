---
title: blockchain.raw over Tails
source_url: https://github.com/monero-project/monero/issues/2677
author: dranogy
assignees: []
labels: []
created_at: '2017-10-18T09:40:07+00:00'
updated_at: '2021-08-13T04:06:25+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:06:25+00:00'
---

# Original Description
I still cant solve the issue with sync as mentioned in this thread: https://github.com/monero-project/monero/issues/2522 and so I am searching for alternative ways to get the blockchain to be capable to run a full node myself. I will try to download the blockchain.raw from https://downloads.getmonero.org/blockchain.raw. 

How do I use the blockchain.raw, after I download it, within Tails over the Tor with cli commands mentioned in the previous thread? I use an external USB for monerod. The explanation here https://github.com/monero-project/monero/releases/tag/v0.9.0 didn't put any light on it. I am a noob, be forgiving if possible, please. 

Thank you for any help here. 

# Discussion History
## radfish | 2017-10-18T17:33:56+00:00
On Wed, Oct 18, 2017 at 02:40:21AM -0700, dranogy wrote:
> How do I use the blockchain.raw, after I download it, within Tails over the Tor with cli commands mentioned in the previous thread?

Best to build newest monero from master because there have been fixes to sync.
Then, pptionally, wipe your monero dir. Then

    /path/to/monero-blockchain-import --input-file /path/to/blockchain.raw --data-dir /path/to/your/monero/dir


PS. I wouldn't download blockchain.raw over Tor, it's >30GB. Download it
on another machine/network if you're really concerned about privacy. Or,
just download it outside of Tails on your normal internet connection.


## selsta | 2021-08-13T04:06:25+00:00
Question has been answered.

# Action History
- Created by: dranogy | 2017-10-18T09:40:07+00:00
- Closed at: 2021-08-13T04:06:25+00:00
