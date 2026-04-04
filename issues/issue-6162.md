---
title: Improving pgp security
source_url: https://github.com/monero-project/monero/issues/6162
author: mendisobal
assignees: []
labels: []
created_at: '2019-11-20T14:10:17+00:00'
updated_at: '2020-05-17T14:41:37+00:00'
type: issue
status: closed
closed_at: '2020-05-17T14:41:37+00:00'
---

# Original Description
I suggest adding the fluffypony.asc signature key and SHA256 sums on Monero binaries to txt domain record getmonero.org
The substitution can be recognized by the changed serial number of the zone.

# Discussion History
## fluffypony | 2019-11-20T14:48:08+00:00
My full GPG key is in the Monero source tree, which already provides an out-of-band record. I don’t think GPG-over-DNS is a standard, otherwise that certainly be novel, but largely pointless as we already use DNSSEC-signed TXT records of the file hashes for the auto-updater, no GPG needed.

## wartjugger | 2019-11-21T06:21:33+00:00
> My full GPG key is in the Monero source tree, which already provides an out-of-band record. I don’t think GPG-over-DNS is a standard, otherwise that certainly be novel, but largely pointless as we already use DNSSEC-signed TXT records of the file hashes for the auto-updater, no GPG needed.

I've imported your key from https://github.com/monero-project/monero/blob/master/utils/gpg_keys/fluffypony.asc
When I try to verify the signed message in https://web.getmonero.org/downloads/hashes.txt I get "Key NOT valid" as the status.

## dEBRUYNE-1 | 2019-11-21T07:06:47+00:00
@wartjugger - Are you following these guides?

https://src.getmonero.org/resources/user-guides/verification-windows-beginner.html (Windows)

https://src.getmonero.org/resources/user-guides/verification-allos-advanced.html (Linux & Mac OS)

## wartjugger | 2019-11-21T09:07:51+00:00
> @wartjugger - Are you following these guides?
> 
> https://src.getmonero.org/resources/user-guides/verification-windows-beginner.html (Windows)
> 
> https://src.getmonero.org/resources/user-guides/verification-allos-advanced.html (Linux & Mac OS)

Ok, it's working with the Linux guide. I was using GNU Privacy Assistant without setting a trust level.

## moneromooo-monero | 2020-05-17T14:41:37+00:00
No bug here.

# Action History
- Created by: mendisobal | 2019-11-20T14:10:17+00:00
- Closed at: 2020-05-17T14:41:37+00:00
