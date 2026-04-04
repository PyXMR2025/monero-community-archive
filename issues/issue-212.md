---
title: Linux distribution from getmonero.org is a tarbomb
source_url: https://github.com/monero-project/monero-site/issues/212
author: aluminiumgeek
assignees: []
labels: []
created_at: '2017-01-08T22:29:49+00:00'
updated_at: '2017-02-24T15:27:00+00:00'
type: issue
status: closed
closed_at: '2017-02-24T15:27:00+00:00'
---

# Original Description
Why do you guys distribute it as a tarbomb (http://www.linfo.org/tarbomb.html)? Is where a particular reason why you do that?
A tarball exploding into an existing directory can be a major annoyance, or even dangerous. That is, it can result in the overwriting of any files and directories that have the same names and which reside in the same directory.


# Discussion History
## KristijanZic | 2017-01-15T20:42:00+00:00
It would be a good idea to distribute it as a snap package. See http://snapcraft.io/ .
I've already proposed this on telegram/irc but here it is again.

## anonimal | 2017-01-15T20:56:06+00:00
@aluminiumgeek I don't like tarbombs either but tar's aren't designed to read minds. `-C` should always be used if there is concern. For this issue, I think the binaries should be put into a folder named after the tarfile: something like `monero.linux.x64.v0-10-1-0`
@KristijanZic https://github.com/monero-project/monero/issues/1532

## anonimal | 2017-02-24T14:57:54+00:00
This issue has been resolved as proven in latest point release https://getmonero.org/downloads/.  @aluminiumgeek can you please close this issue?

# Action History
- Created by: aluminiumgeek | 2017-01-08T22:29:49+00:00
- Closed at: 2017-02-24T15:27:00+00:00
