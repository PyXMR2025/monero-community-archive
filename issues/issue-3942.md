---
title: license missing for SUPERCOP ref10
source_url: https://github.com/monero-project/monero/issues/3942
author: jonassmedegaard
assignees: []
labels: []
created_at: '2018-06-06T11:47:13+00:00'
updated_at: '2018-07-19T21:48:59+00:00'
type: issue
status: closed
closed_at: '2018-07-19T21:48:59+00:00'
---

# Original Description
Hi,

the file src/crypto/crypto_ops_builder/README.md states that

> The majority of the work we are using is from SUPERCOP, and copyrights and attribution fall to those developers and cryptographers.

I fail to locate any license grant from the authors of SUPERCOP - neither in Monero project nor upstream in <http://hyperelliptic.org/ebats/supercop-20141124.tar.bz2>

Please clarify under which license the SUPERCOP code has been included.

# Discussion History
## moneromooo-monero | 2018-06-06T14:47:16+00:00
http://ed25519.cr.yp.to/software.html says:

"The Ed2519 software is available as the crypto_sign/ed25519 subdirectory of the SUPERCOP benchmarking tool [,,,]"

and:

"The ed25519 software is in the public domain."

Looking at the source, it seems that the ref10 source in monero is the crypto_sign/ed25519 software, modulo two small files, "description" and "designers".


## jonassmedegaard | 2018-06-08T07:19:50+00:00
Thanks!

The piece I was missing was the existence of web page http://ed25519.cr.yp.to/software.html

I suggest to extend file "description" (which seemingly is already edited by you - by copying ../descrition from upstream tarball and adding a line linking to the tarball URL) with a line pointing to http://ed25519.cr.yp.to/software.html as homepage of the upstream code and mention that its (non-)license is stated there.

Example:

  Homepage (listing the code as being in the public domain): http://ed25519.cr.yp.to/software.html

## moneromooo-monero | 2018-06-18T12:55:51+00:00
https://github.com/monero-project/monero/pull/4021

## moneromooo-monero | 2018-07-19T21:41:16+00:00
+resolved

# Action History
- Created by: jonassmedegaard | 2018-06-06T11:47:13+00:00
- Closed at: 2018-07-19T21:48:59+00:00
