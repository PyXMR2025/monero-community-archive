---
title: Verifying PGP signature not working?
source_url: https://github.com/xmrig/xmrig/issues/2257
author: Shinaolord
assignees: []
labels:
- question
created_at: '2021-04-13T07:22:39+00:00'
updated_at: '2021-04-13T17:16:18+00:00'
type: issue
status: closed
closed_at: '2021-04-13T17:16:18+00:00'
---

# Original Description
So, I've imported your certificate public key after verifying the github and xmrig.com ones were identical, and then downloaded the latest release of xmrig on windows (`wget "https://github.com/xmrig/xmrig/releases/download/v6.11.2/xmrig-6.11.2-gcc-win64.zip" -outfile xmrig-6.11.zip` ). I then unzipped it, downloaded SHA256SUMS.sig, and ran the following command:



```

gpg --verify SHA256SUMS.sig SHA256SUMS

>      gpg:                using RSA key 9AC4CEA8E66E35A5C7CDDC1B446A53638BE94409
>     gpg: BAD signature from "XMRig <support@xmrig.com>" [full]
```

And I get a bad signature error.

I am new to using PGP, is there something I am doing or have done incorrectly? I have a feeling I'm missing something rather important on verifying the authenticity of programs; and I would like to know what, if anything, I am doing wrong, so that I can feel and be safer in downloading mining software.

# Discussion History
## xmrig | 2021-04-13T11:45:31+00:00
`SHA256SUMS.sig` should be used with this file https://github.com/xmrig/xmrig/releases/download/v6.11.2/SHA256SUMS it contains SHA256 hashes of all download files including the `xmrig-6.11.2-gcc-win64.zip`.
`SHA256SUMS` inside the zip file is not signed and contains hashes of content of the archive.
Thank you.


## Shinaolord | 2021-04-13T17:16:18+00:00
Y

> `SHA256SUMS.sig` should be used with this file https://github.com/xmrig/xmrig/releases/download/v6.11.2/SHA256SUMS it contains SHA256 hashes of all download files including the `xmrig-6.11.2-gcc-win64.zip`.
> `SHA256SUMS` inside the zip file is not signed and contains hashes of content of the archive.
> Thank you.

Yep that worked, and gave a Good signature! Didn't realize the SHA256SUM on the releases page was different from the one inside the zip. That's my mistake, thank you!

# Action History
- Created by: Shinaolord | 2021-04-13T07:22:39+00:00
- Closed at: 2021-04-13T17:16:18+00:00
