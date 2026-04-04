---
title: 'Buildbot: nightly builds on macOS 10.13, not OS X 10.11'
source_url: https://github.com/monero-project/meta/issues/211
author: anonimal
assignees: []
labels: []
created_at: '2018-04-24T03:39:52+00:00'
updated_at: '2018-04-26T10:54:01+00:00'
type: issue
status: closed
closed_at: '2018-04-26T10:54:01+00:00'
---

# Original Description
Required to resolve https://github.com/monero-project/kovri/issues/696. The 10.13 static binaries will also run on 10.11 and 10.12.

@danrmiller Is there a reason we're currently building on 10.11 for nightlies?

# Discussion History
## danrmiller | 2018-04-25T17:39:01+00:00
Mainly because for monero and monero gui the 10.13 builds don't run on 10.11, I think because of a newly added c library function that isn't present on the older ones, I can find the exact reason later. Also we regularly have issues on those projects where osx builds are more forward compatible than backward compatible. Also in general it seems good to ensure it works with the earliest supported version.

But I will be happy to change to or add an osx 10.13 static build and can have that done for you today.

## danrmiller | 2018-04-25T17:59:09+00:00
The nightly kovri-static-osx job will now be run by the osx 10.13 builder, I kicked off a sample job:
https://build.getmonero.org/builders/kovri-static-osx/builds/466

There is now an additional nightly job called kovri-static-osx-10.11
https://build.getmonero.org/builders/kovri-static-osx-10.11

## anonimal | 2018-04-26T10:54:01+00:00
Thank you **very much** Dan for doing both!

Having the 10.11 nightly available will also be useful come integration time (if kovri will need to fix the 10.11 issues by then).

# Action History
- Created by: anonimal | 2018-04-24T03:39:52+00:00
- Closed at: 2018-04-26T10:54:01+00:00
