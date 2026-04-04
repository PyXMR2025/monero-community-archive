---
title: Automate monitoring of critical OpenSSL updates for static binary releases
source_url: https://github.com/monero-project/meta/issues/38
author: anonimal
assignees: []
labels: []
created_at: '2017-01-10T04:56:38+00:00'
updated_at: '2017-03-16T17:52:30+00:00'
type: issue
status: closed
closed_at: '2017-03-16T17:52:30+00:00'
---

# Original Description
For the static builds on the website: `monerod` uses libunbound which in turn uses OpenSSL statically. `kovri` uses cpp-netlib which in turn uses OpenSSL statically (now that the static builds are ready).

This is a problem for the website binaries in terms of keeping up with critical OpenSSL updates. We should somehow decide who takes care of what, and how, and preferably the process would be as automated as possible.

This idea was originally going to be only for kovri until just now when I noticed the capacity of monerod's libunbound usage.

I'll cross-post this into monero's repo since there are far more eyes there than here (though I'll close the issue there if someone thinks it should stay here). Maybe someone will want to jump at the opportunity and pickup the slack?

# Discussion History
## anonimal | 2017-01-24T01:37:33+00:00
```
anonimal | I'm going to go ahead and take on https://github.com/monero-project/meta/issues/38 https://github.com/monero-project/monero/issues/1554
anonimal | What this means is I'll subscribe to the openssl announcement list and yell "fire!" when needed.
anonimal | From there I imagine we'll just push an immediate point or letter release based either off the latest tag or whatever you want and then push to the site, etc.
```

## anonimal | 2017-01-30T02:43:25+00:00
@hyc and I agreed to take on the responsibility. Ultimately, we will also need @fluffypony involved since he builds the releases. I'm not sure how we can automate this though since reviewing the openssl changes requires manual review. Ideas welcome.

# Action History
- Created by: anonimal | 2017-01-10T04:56:38+00:00
- Closed at: 2017-03-16T17:52:30+00:00
