---
title: 'failed to deserialize keys buffer '
source_url: https://github.com/monero-project/monero/issues/8684
author: Gingeropolous
assignees: []
labels: []
created_at: '2022-12-20T04:54:53+00:00'
updated_at: '2023-03-10T23:28:56+00:00'
type: issue
status: closed
closed_at: '2023-03-10T23:28:56+00:00'
---

# Original Description
https://old.reddit.com/r/monerosupport/comments/zpz5zs/keys_file_cant_restore_couldnt_open_wallet/

this is the second instance I've seen of this. Old monero users getting new software and running into this with old wallet files.

and if there's 2 people that post something, that means there's millions!

someone on IRC says its probably a corrupt file. 

# Discussion History
## afungible | 2022-12-21T02:25:12+00:00
And which version are the users talking about? Latest is `v0.18.1.2`

Might it be a good to check the delta of `bool wallet2::load_keys_buf(..) `with previous version where this wallet file worked.
https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L4181



## selsta | 2022-12-21T02:31:38+00:00
Is there anyone who reported that they have a .keys file that opens with an old version and doesn't with a new version? If yes, which exact version breaks?

So far I feel like this is just a corrupted file.

## plowsof | 2022-12-23T02:28:15+00:00
testing with monero-wallet-cli [v0.10.0.0](https://github.com/monero-project/monero/releases/tag/v0.10.0) Sep 19, 2016:
- cli v18.1.2 opens the keys file without issue
- gui v18.1.2 will complain - but will open the wallet without issue after cli creates the cache for it (no mention of deserialize here in this particular version)
```
Error opening wallet with password:  boost::filesystem::copy_file: Invalid argument: "/home/username/Downloads/monero.linux.x64.v0-10-0-0/wallet-v0.10_2", "/home/username/Downloads/monero.linux.x64.v0-10-0-0/wallet-v0.10_2.unportable"
```

## selsta | 2023-03-10T23:28:56+00:00
Since there's no clear way to reproduce (@plowsof did testing) and no other reports I'll close this for now. It's highly likely simply a corrupted wallet file.

# Action History
- Created by: Gingeropolous | 2022-12-20T04:54:53+00:00
- Closed at: 2023-03-10T23:28:56+00:00
