---
title: hashes.txt.sig fails GPG verification against current hashes.txt (v0.18.5.1)
source_url: https://github.com/monero-project/monero-site/issues/2706
author: AlexanderWalls
assignees: []
labels: []
created_at: '2026-09-15T17:21:38+00:00'
updated_at: '2026-09-15T19:02:42+00:00'
type: issue
status: closed
closed_at: '2026-09-15T19:01:33+00:00'
---

# Original Description
`hashes.txt.sig` does not cryptographically verify against the current
`hashes.txt` content, using the key it claims to be signed by.

## Steps to reproduce

    curl -fsSLO https://getmonero.org/downloads/hashes.txt
    curl -fsSLO https://getmonero.org/downloads/hashes.txt.sig
    curl -fsSLO https://raw.githubusercontent.com/monero-project/monero/master/utils/gpg_keys/luigi1111.asc
    gpg --import luigi1111.asc
    gpg --verify hashes.txt.sig hashes.txt

## Result

    gpg: Signature made Sun 17 May 2026 13:49:11 BST
    gpg:                using RSA key 8777AB8F778EE89487A2F8E7F4ACA0183641E010
    gpg: BAD signature from "luigi1111 <luigi1111w@gmail.com>" [unknown]

Reproduced consistently across multiple fresh fetches (different times,
inside and outside a container), so it isn't a CDN cache race. TLS on
getmonero.org checks out (valid cert, no sign of MITM). The tarball itself
is fine - `monero-linux-x64-v0.18.5.1.tar.bz2`'s own sha256 matches the
line for it inside `hashes.txt` exactly - so this looks like `hashes.txt`
and `hashes.txt.sig` having gone out of sync on the server, not a bad
release or a compromised binary.

This breaks the documented verification flow
(https://docs.getmonero.org/interacting/verify-monero-binaries/) for anyone
following it today - worth fixing given it's the officially recommended
way to verify a release.

## Environment
- Debian 13, gpg 2.4.7
- Confirmed against binaryfate.asc AND luigi1111.asc from
  utils/gpg_keys/ - fails against both being the wrong key; only luigi1111
  matches the signature's key ID, and even that fails cryptographic
  verification.

# Discussion History
## selsta | 2026-09-15T17:35:16+00:00
> This breaks the documented verification flow (https://docs.getmonero.org/interacting/verify-monero-binaries/) for anyone

Unless I'm missing something, hashes.txt.sig is not even mentioned here.

The file is used for the GUI auto updater which is currently not setup for the latest version, that's why it is failing.

## AlexanderWalls | 2026-09-15T19:01:31+00:00
Correction, sorry for the noise: hashes.txt is inline-clearsigned (verify
with `gpg --verify hashes.txt` alone, per docs.getmonero.org's documented
flow), not a detached signature paired with hashes.txt.sig as I assumed.
hashes.txt.sig is apparently a separate artifact used by the GUI
auto-updater, unrelated to the CLI verification flow I was following -
thanks @selsta 

Verified locally: `gpg --verify hashes.txt` gives a clean "Good signature
from binaryFate" against the current file. No actual bug here  -
closing.

# Action History
- Created by: AlexanderWalls | 2026-09-15T17:21:38+00:00
- Closed at: 2026-09-15T19:01:33+00:00
