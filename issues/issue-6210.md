---
title: please PGP-sign release tarballs
source_url: https://github.com/monero-project/monero/issues/6210
author: jonassmedegaard
assignees: []
labels: []
created_at: '2019-12-02T16:05:34+00:00'
updated_at: '2022-02-19T04:43:45+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:43:45+00:00'
---

# Original Description
It is helpful for automated integrity validation if each release tarball is PGP-signed as recommended at https://wiki.debian.org/UpstreamGuide#Tarballs

# Discussion History
## jonassmedegaard | 2019-12-02T16:08:58+00:00
...and what is more helpful is that the _tarball_ is signed, instead of (or in addition to) signing a list of checksums as mentioned at https://github.com/monero-project/monero/issues/6177#issuecomment-560456552

## moneromooo-monero | 2019-12-02T19:43:37+00:00
Not quite what you asked, but Pony just added the source tarballs to the hashes.txt file.

## fluffypony | 2019-12-02T19:46:57+00:00
@jonassmedegaard I get a 403 accessing that. I'd prefer we don't, but if it's absolutely essential we could add GPG-signed source tarballs to the release engineering list.

## jonassmedegaard | 2019-12-02T19:57:57+00:00
If you mean that https://wiki.debian.org/UpstreamGuide#Tarballs is a 403 error for you then that's odd - just double-checked and works fine for me.

It is not "absolutely essential" to be able to automatically validate source releases cryptographically. But I do consider it quite wise to do, even if adding a slight extra burden onto your release procedure.

## moneromooo-monero | 2019-12-02T20:02:31+00:00
hashes.txt (now) allows automated verification. sha256sum -c can read it I think (might have to grep ^monero), and it can be GPG checked.

## jonassmedegaard | 2019-12-02T20:51:25+00:00
yes, I do understand that your existing convoluted verification procedure works now. Great for you.

The issue I raised here is, however, a request to ease verification for those (re)distributors who do not happen to use that particular method, but instead the methos of signing the tarball.

Feel free to close as a wontfix.  It is your project and you decide how you want to manage it.

## vtnerd | 2019-12-03T01:24:00+00:00
This method is not convoluted, it is a valid method for signing files. Gentoo signs their auto-releases this way for instance. Kernel.org also signs patches against the head release this way instead of individual signatures (but signs the tarball for the entire source tree release). As moo said, ``shasum256 -c --ignore-missing`` will be helpful.

## jonassmedegaard | 2019-12-03T02:03:28+00:00
Quoting Lee Clagett (2019-12-03 02:24:00)
> This method is not convoluted, it is a valid method for signing files. Gentoo signs their auto-releases this way for instance. Kernel.org also signs patches against the head release this way instead of individual signatures (but signs the tarball for the entire source tree release). As moo said, ``shasum256 -c --ignore-missing`` will be helpful.

Sorry if I offended anyone - I only meant to describe it as "layered" 
and in fact tried to phrase it more politely than was done at 
https://github.com/monero-project/monero/issues/6177#issuecomment-560456552

-- 
 * Jonas Smedegaard - idealist & Internet-arkitekt
 * Tlf.: +45 40843136  Website: http://dr.jones.dk/

 [x] quote me freely  [ ] ask before reusing  [ ] keep private


## jonassmedegaard | 2019-12-03T02:06:06+00:00
Fact is Debian supports validating release tarballs by use of an ASCII-armoured PGP signature file.  There is flexibility in where to locate that file, but not in the method of doing the validation.

Would be helpful if Debian could automatically validate releases from Monero.

## fluffypony | 2019-12-03T05:46:35+00:00
@jonassmedegaard don't worry, you didn't offend anyone - we're just curious and asking questions so we understand:) Will add a note to release engineering, and will try produce this for 0.15.0.1 in the next few days so we can make sure we're doing it correctly.

## jonassmedegaard | 2019-12-03T12:16:07+00:00
Quoting Riccardo Spagni (2019-12-03 06:46:36)
> @jonassmedegaard don't worry, you didn't offend anyone - we're just curious and asking questions so we understand:) Will add a note to release engineering, and will try produce this for 0.15.0.1 in the next few days so we can make sure we're doing it correctly.

That's great! Thanks!

-- 
 * Jonas Smedegaard - idealist & Internet-arkitekt
 * Tlf.: +45 40843136  Website: http://dr.jones.dk/

 [x] quote me freely  [ ] ask before reusing  [ ] keep private


## selsta | 2022-02-19T04:43:45+00:00
Resolved: https://www.getmonero.org/downloads/hashes.txt

# Action History
- Created by: jonassmedegaard | 2019-12-02T16:05:34+00:00
- Closed at: 2022-02-19T04:43:45+00:00
