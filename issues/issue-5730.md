---
title: Release monero-linux-x64-v0.14.1.0.tar.bz2 == invalid bzip2 file (rather gzip)
source_url: https://github.com/monero-project/monero/issues/5730
author: jonathancross
assignees: []
labels:
- invalid
created_at: '2019-07-03T16:00:14+00:00'
updated_at: '2019-07-17T19:49:20+00:00'
type: issue
status: closed
closed_at: '2019-07-03T16:57:47+00:00'
---

# Original Description
It seems the Linux cli v0.14.1.0 release has been compressed using gzip rather than bzip2:

```
$ curl https://downloads.getmonero.org/cli/monero-linux-x64-v0.14.1.0.tar.bz2 --output monero-linux-x64-v0.14.1.0.tar.bz2

$ openssl dgst -sha256 monero-linux-x64-v0.14.1.0.tar.bz2
SHA256(monero-linux-x64-v0.14.1.0.tar.bz2)= 2b95118f53d98d542a85f8732b84ba13b3cd20517ccb40332b0edd0ddf4f8c62

$ bunzip2 monero-linux-x64-v0.14.1.0.tar.bz2
bunzip2: monero-linux-x64-v0.14.1.0.tar.bz2 is not a bzip2 file.

$ file monero-linux-x64-v0.14.1.0.tar.bz2
monero-linux-x64-v0.14.1.0.tar.bz2: gzip compressed data, max compression, from Unix
```

**Note:** *gzip* rather than *bzip2* as in previous releases.

# Discussion History
## moneromooo-monero | 2019-07-03T16:52:44+00:00
Yes, it is known. I expect it'll change for next release. You can file it on the monero-site repo also since that's where those files live.

+invalid


## jonathancross | 2019-07-04T13:08:49+00:00
Moved to: https://repo.getmonero.org/monero-project/monero-site/issues/964

## jonathancross | 2019-07-04T13:40:09+00:00
Seems this [should be fixed](https://www.reddit.com/r/Monero/comments/c0w3cp/cli_v01410_boron_butterfly_released/er9rne5/) in the gitian yml files (eg [/contrib/gitian/gitian-linux.yml](https://github.com/monero-project/monero/blob/master/contrib/gitian/gitian-linux.yml)), so it might make more sense to have this open here?

## ghost | 2019-07-17T19:49:20+00:00
I noticed this as well, caught me by surprise.

Nice change, not a big fan of bzip2. xz would make sense if you wanted better compression than gzip, though.

# Action History
- Created by: jonathancross | 2019-07-03T16:00:14+00:00
- Closed at: 2019-07-03T16:57:47+00:00
