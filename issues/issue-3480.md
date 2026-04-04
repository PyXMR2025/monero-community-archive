---
title: How reproducible are the reproducible builds?
source_url: https://github.com/monero-project/monero-gui/issues/3480
author: bonevays
assignees: []
labels: []
created_at: '2021-05-13T17:42:49+00:00'
updated_at: '2021-05-14T13:08:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I am quite happy to report I was able to follow the docker recipe on Windows and (re)produce monero-wallet-gui.exe with just a few warnings. However, the build runs some commands like "apt update" which are most definitely not deterministic. If you run them 6 months later you will get quite a different mix of Linux binaries and libraries, which does not really inspire confidence in building binaries with the same hash. In fact, my binary is a different size from the one I downloaded, and I am quite happy too as the downloaded binary never starts on my "tweaked" Windows, the thingy was spinning and spinning, despite me fetching all kinds of updates and libraries. 

Just to harp on the same theme, doesn't "git clone master" also spoil the reproducibility of the builds, unless you "pin" released versions?

# Discussion History
## selsta | 2021-05-13T17:58:46+00:00
> If you run them 6 months later you will get quite a different mix of Linux binaries and libraries

Yes, the CLI reproducible builds have the same issue. It should be reproducible if you build around the same time. We don't release the CLI before multiple users confirmed matching hashes, this can be seen here: https://github.com/monero-project/gitian.sigs

We don't do the same for the GUI because 1) we have less contributors here and 2) don't have reproducible Mac build yet.

> and I am quite happy too as the downloaded binary never starts on my "tweaked" Windows, the thingy was spinning and spinning, despite me fetching all kinds of updates and libraries.

What do you mean here exactly?

> Just to harp on the same theme, doesn't "git clone master" also spoil the reproducibility of the builds, unless you "pin" released versions?

Where do you see master getting cloned in the dockerfile?

## bonevays | 2021-05-14T13:03:23+00:00
I had a casual look at the build process and saw some master clone, somewhere. I run Windows "nightly" and the official GUI does not start at all. Like I said, my build starts and works as expected.

## selsta | 2021-05-14T13:08:22+00:00
We were able to reproduce the issue with hashes not matching and are looking into it.

> I had a casual look at the build process and saw some master clone, somewhere.

I don't see master being used anywhere for release binaries.

> Like I said, my build starts and works as expected.

That's due to a bug with multiple monitors  unrelated to reproducible builds. It is fixed in v0.17.2.2.

# Action History
- Created by: bonevays | 2021-05-13T17:42:49+00:00
