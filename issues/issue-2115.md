---
title: hashes.txt doesnt work when doing sha256sum -c ??
source_url: https://github.com/monero-project/monero/issues/2115
author: ghost
assignees: []
labels: []
created_at: '2017-06-24T00:10:24+00:00'
updated_at: '2017-06-28T09:46:43+00:00'
type: issue
status: closed
closed_at: '2017-06-28T09:46:43+00:00'
---

# Original Description
The file https://getmonero.org/downloads/hashes.txt has 3 comment lines:

> This GPG-signed message exists to confirm the SHA256 sums on Monero binaries.
> 
> Please verify the signature against the signature for fluffypony in the
> source code repository (/utils/gpg_keys).

which causes the below command to not work/verify, ive realized commenting out those lines makes the command work.  funny enough if i delete the word fluffypony in the line or edit it, it will verify ok.

sha256sum -c "hashes.txt" "monero-gui-linux-x64-v0.10.3.1.tar.bz2" 2>&1 | grep OK

It would be easier if you could comment them out so that the file can be downloaded for users who want to auto-check their hashes without needing to edit the hashes.txt file

# Discussion History
## ghost | 2017-06-26T22:25:39+00:00
Has anyone investigated this issue or seen same results? please respond.

## glv2 | 2017-06-27T08:04:14+00:00
To check the hashes automatically with sha256sum, you can strip the signature and the message from the file before processing it:

``` bash
grep -E '^[[:xdigit:]]{64} ' hashes.txt | sha256sum --ignore-missing -c
```


## ghost | 2017-06-28T09:46:39+00:00
Thanks @glv2 !!!

# Action History
- Created by: ghost | 2017-06-24T00:10:24+00:00
- Closed at: 2017-06-28T09:46:43+00:00
