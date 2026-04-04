---
title: GNU Guix Packaging
source_url: https://github.com/monero-project/monero/issues/1854
author: HulaHoopWhonix
assignees: []
labels:
- proposal
created_at: '2017-03-08T17:26:46+00:00'
updated_at: '2021-08-13T04:10:47+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:10:47+00:00'
---

# Original Description
Hi. Please consider making a Monero package available via the GNU Guix package manager. Its a modern package manager that has many unique security and maintenance features including atomic updates, rollback and reproducible builds.

A Guix package would make it easy for us (WhonixOS - a privacy distro) to include Monero in our OS because lower package update/maintenance overhead.

https://www.gnu.org/software/guix/
https://www.gnu.org/software/guix/packages

cc/ @adrelanos

# Discussion History
## danrmiller | 2017-03-08T17:29:10+00:00
I'm very interested in doing this too and will take a stab at it.

## dEBRUYNE-1 | 2018-01-08T12:37:30+00:00
+proposal

## sedited | 2019-06-12T09:33:54+00:00
Started to follow up on this, since gitian reproducible builds are working now. Guix allows for full bootstrapability, which is very desirable even over gitian building. Gitian is not that actively maintained anymore, a bunch of projects using it are moving towards Guix now.

## glv2 | 2019-06-12T10:01:54+00:00
@TheCharlatan, I have some Guix package definitions for not too ancient development versions of monero and monero-gui (commit 5fbfa8a65663e807c6500ae9485e898df9b7c470 for monero and commit c286c7e5a8e67d769bc9054f661ab742a8b1a5ba for monero-gui).

If you want to update them for release 14.1 (and send the final patch to guix-patches), I can send them to you.

## glv2 | 2019-06-17T09:17:54+00:00
I proposed patches to Guix for release 0.14.1.0:

 1. [patch for monero 0.14.1.0](https://debbugs.gnu.org/cgi/bugreport.cgi?bug=36258)
 2. [patch for monero-gui 0.14.1.0](https://debbugs.gnu.org/cgi/bugreport.cgi?bug=36259)

Several builds on my x86-64 machine (Intel i7 CPU) produce identical binaries, but it would be useful if someone with a different x86-64 CPU could check that they get the same result as me. I also haven't checked for other architectures.


## glv2 | 2019-07-03T13:05:28+00:00
Update: the package definitions for monero-0.14.1.0 and monero-gui-0.14.1.0 have been merged in GNU Guix.


## selsta | 2021-08-13T04:10:47+00:00
- https://guix.gnu.org/packages/monero-gui-0.17.2.2/
- https://guix.gnu.org/packages/monero-0.17.2.0/

# Action History
- Created by: HulaHoopWhonix | 2017-03-08T17:26:46+00:00
- Closed at: 2021-08-13T04:10:47+00:00
