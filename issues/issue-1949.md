---
title: Establish a Chain of Trust with every release signing Key Transition
source_url: https://github.com/monero-project/monero-site/issues/1949
author: maltfield
assignees: []
labels:
- community
created_at: '2022-04-24T22:54:06+00:00'
updated_at: '2022-08-08T09:37:48+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Request: Please establish a cryptographic chain of trust whenever the key that signs Monero's software releases changes.

### Problem

I haven't used monero for a few years. Last time I used it, the releases were signed by the following `fluffypony` PGP key:

```
pub   rsa2048/0x7455C5E3C0CDCEB9 2013-04-08 [SCEA]
      BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9
uid                             Riccardo Spagni <ric@spagni.net>
sub   rsa2048/0x55432DF31CCD4FCD 2013-04-08 [SEA]
```

Recently, I downloaded the most recent version of monero, and I found that its release signature was invalid. Scary.

```
user@disp4335:~$ wget -q https://www.getmonero.org/downloads/hashes.txt
user@disp4335:~$ gpg --verify hashes.txt
gpg: Signature made Fri 07 Jan 2022 04:43:55 PM CET
gpg:                using RSA key 81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92
gpg: Can't check signature: No public key
user@disp4335:~$ 
```
### How to reproduce

As a user who cares about the authenticity of the software I download, the obvious next-step is to figure out:
1. who owns this `81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92` key, and
2. is it valid?

The hashes.txt file says public key for `binaryFate` can be found in the github repo's `/utils/gpg_keys/` directory. That's at least one out-of-band check.

```
user@disp4335:~$ head hashes.txt 
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

# This GPG-signed message exists to confirm the SHA256 sums of Monero binaries.
#
# Please verify the signature against the key for binaryFate in the
# source code repository (/utils/gpg_keys).
#
#
## CLI
user@disp4335:~$ 
```

So I download the relevant key associated with `binaryFate` from github.com.

```
user@disp4335:~$ wget -q https://raw.githubusercontent.com/monero-project/monero/master/utils/gpg_keys/binaryfate.asc
user@disp4335:~$ 

user@disp4335:~$ gpg binaryfate.asc 
gpg: WARNING: no command supplied.  Trying to guess what you mean ...
pub   rsa4096 2019-12-12 [SCEA]
      81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92
uid           binaryFate <binaryfate@getmonero.org>
sub   rsa4096 2019-12-12 [SEA]
user@disp4335:~$ 

```

And the next step is to establish a chain of trust. I already trust `fluffypony`, so he should have done something publicly to indicate that:

1. The new `81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92` key is, in fact, held by the real `binaryFate` and not an imposter and
3. That `binaryFate` is indeed trustworthy and all new Monero software releases will be signed by their private PGP key corresponding to the public key fingerprint above

The most logical way to do this would be for `fluffypony` to sign `binaryFate`'s public PGP key. So I check `binaryFate`'s key for a signature packet from `fluffypony`'s key = `BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9`. But I don't find that! Yikes, this is sketch.

```
user@disp4335:~$ gpg --list-packets binaryfate.asc | grep -i BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9
user@disp4335:~$ 
```

So `fluffypony` didn't sign `binaryFate`'s PGP key? That sounds like `fluffypony` doesn't trust this key. Or this key is not authentic. Hmm.

But monero has a blog. Maybe they have an important announcement pinned to the top of their news feed with critical security announcements like changes to cryptographic keys? But the monreo blog has, err, 44 pages?? Ok, well, I checked the first 3 pages, and I didn't see anything about the key changing. Yikes, this looks really bad. Who even is this `binaryFate` guy? Did [monero's release infrastructure get hacked again](https://github.com/monero-project/monero/issues/6151)? Is my `hashes.key` file even authentic?

I looked for a search bar on getmonero.org, but couldn't find one. I tried a ddg query `key transition signature site:getmonero.org`. No results.

 * https://duckduckgo.com/?q=key+transition+release+signature+site%3Agetmonero.org

I tried again querying for `"fluffypony" "binaryfate" site:getmonero.org`. That worked:

 * https://duckduckgo.com/?q=%22fluffypony%22+%22binaryfate%22+site%3Agetmonero.org

The top result was this blog post:

 * https://web.getmonero.org/2019/12/16/technical-responsibilities-update.html

The above blog post says that `fluffypony` will step down and all new releases will be signed by `binaryfate`. But, *jaw drop*, **this critical security announcement isn't signed?? How the hell can I trust it to be authentic?**

### Solution

As described above, every attempt made to establish some sort of cryptographic chain of trust for the software release signatures' key transition failed. This should be resolved by:

1. `fluffypony` (`BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9`) should sign `binaryfate`'s public PGP key (`81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92`)
2. The newly signed public key (`81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92`) should be updated in the github repo
4. The announcement [technical responsibilities update (2019-12)](https://web.getmonero.org/2019/12/16/technical-responsibilities-update.html) should be cryptographically signed by `binaryfate`'s PGP key (`81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92`) and (more importantly) with `fluffypony`'s PGP key (`BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9`)
5. The [technical responsibilities update (2019-12)](https://web.getmonero.org/2019/12/16/technical-responsibilities-update.html) article should be more prominent on the getmonero.org website. At least, it should be tagged with `[Cryptography](https://www.getmonero.org/blog/tags/crypto.html)` and `[Urgent](https://www.getmonero.org/blog/tags/urgent.html)` so it appears on those respective sections.

### Key Transition Statement Examples

Key Transition Statements should be cryptographically signed by both the old (currently trusted) key and the new (to be trusted) key. Key transitions generally refer to when a human changes their PGP key, but the same principles apply to when an org changes the PGP key responsible for signing their release.

Riseup has a great template for Key Transition Statements:

 * https://riseup.net/en/security/message-security/openpgp/key-transition

And here's an example of a signed Key Transition Statement from when I changed my personal PGP key in 2017 that establishes a cryptographic chain of trust between my old PGP key and my current PGP key:

 * https://tech.michaelaltfield.net/2017/10/01/gpg-key-transition-statement/

# Discussion History
## plowsof | 2022-04-25T19:46:19+00:00
BinaryFates key has been signed by Riccardo Spagni aka FluffyPony* (among others) - i've not had enough time to figure out the exact steps, but it involves importing keys and such, However, there is a public key server here to show those that have signed BinaryFates key: https://keyserver.ubuntu.com/pks/lookup?search=binaryfate&fingerprint=on&op=index

And i see that one of them is https://keyserver.ubuntu.com/pks/lookup?op=vindex&search=0x7455c5e3c0cdceb9 

## binaryFate | 2022-04-25T21:26:47+00:00
> Recently, I downloaded the most recent version of monero, and I found that its release signature was invalid. Scary.

The signature is cryptographically valid, you are simply missing the key so of course GPG is unable to check it. GPG tells you explicitly "Can't check signature: No public key", nowhere does it say the signature is invalid.


> The most logical way to do this would be for fluffypony to sign binaryFate's public PGP key. So I check binaryFate's key for a signature packet from fluffypony's key = BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9. But I don't find that! Yikes, this is sketch.

Fluffypony did sign my key on the 2019/12/13. This is available on all public PGP keys servers, you just need to import it.

Import both Fluffy's key and mine:
`gpg --keyserver keyserver.ubuntu.com --receive-keys F0AF4D462A0BDF92 7455C5E3C0CDCEB9`
Then
`gpg --list-sig F0AF4D462A0BDF92` will show you the signature.


## maltfield | 2022-04-26T11:42:09+00:00
> you are simply missing the key

I'm reporting a social/organization problem, not simply a technical problem.

Of course users can download the latest release, check the signature, then just download the key that signed the release. ..But that defeats the purpose of signing releases if we all just TOFU every time.

If an organization transitions the key that they use to sign their releases, then the previous signer should publish a [Key Transition Statement](https://riseup.net/en/security/message-security/openpgp/key-transition) that's signed by both the old signing key and the new signing key. The message should state that that the key is transitioning, which keys (listing full fingerprints), why the transition, etc.

### From Ubuntu's keyservers

@binaryFate sorry but the commands you provided does *not* put your key in a keyring with a signature from fluffypony. To reproduce consistently, we can use docker as follows (I'm doing this on debian 11 in both host and guest)

```
sudo apt-get install docker.io
sudo bash -c 'gpasswd -a "${SUDO_USER}" docker'
su - `whoami`

export DOCKER_CONTENT_TRUST=1
docker run --rm -it --entrypoint /bin/bash debian:bullseye-slim

apt update
apt install gpg

gpg --keyserver keyserver.ubuntu.com --receive-keys F0AF4D462A0BDF92 7455C5E3C0CDCEB9
gpg --list-sig F0AF4D462A0BDF92
```
The output shows no signatures on the key

```
root@2d63e298e97e:/# gpg --list-sig F0AF4D462A0BDF92
pub   rsa4096 2019-12-12 [SCEA]
      81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92
uid           [ unknown] binaryFate <binaryfate@getmonero.org>
sig 3        F0AF4D462A0BDF92 2019-12-12  binaryFate <binaryfate@getmonero.org>
sub   rsa4096 2019-12-12 [SEA]
sig          F0AF4D462A0BDF92 2019-12-12  binaryFate <binaryfate@getmonero.org>

root@2d63e298e97e:/# 
```

While I do appreciate making keys available on multiple domains (so they can be cross-checked out-of-band during TOFU), I don't think it makes sense to depend on Ubuntu's keyservers, which can't be controlled by the monero team.

I don't know how ubuntu runs their keyservers, but it's possible that they're intentionally stripping signatures from their keys due to historic Certificate Flooding attacks:

 * https://tech.michaelaltfield.net/2019/07/14/mitigating-poisoned-pgp-certificates/

### From the monero GitHub repo

What we *can* control is the contents of the repo on GitHub.com. Indeed, this is where the `hashes.txt `file instructs the user to download the developer's public keys.

Here we download both keys from the monero repo. Note that there are no signatures on binaryFate's public key.

```
sudo apt-get install docker.io
sudo bash -c 'gpasswd -a "${SUDO_USER}" docker'
su - `whoami`

export DOCKER_CONTENT_TRUST=1
docker run --rm -it --entrypoint /bin/bash debian:bullseye-slim

apt update
apt install wget gpg

wget -q https://raw.githubusercontent.com/monero-project/monero/aa9ba3064e4b59f7c378561f2716ca129bc7f846/utils/gpg_keys/fluffypony.asc
gpg --import fluffypony.asc

wget -q https://raw.githubusercontent.com/monero-project/monero/aa9ba3064e4b59f7c378561f2716ca129bc7f846/utils/gpg_keys/binaryfate.asc
gpg --import binaryfate.asc

gpg --list-sigs BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9
gpg --list-sigs 81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92
```

And the output shows that the public keys stored in the repo have the same issue: binaryFate's public key (`81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92`) is not signed by fluffypony's key (`BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9`)

```
root@4d11e4ab5407:/# gpg --list-sigs BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9
pub   rsa2048 2013-04-08 [SCEA]
      BDA6BD7042B721C467A9759D7455C5E3C0CDCEB9
uid           [ unknown] Riccardo Spagni <ric@spagni.net>
sig 3        7455C5E3C0CDCEB9 2013-04-08  Riccardo Spagni <ric@spagni.net>
sig 3    NX  7FAB114267E4FA04 2014-07-15  [User ID not found]
sig          9F31802C79642F25 2014-06-28  [User ID not found]
sub   rsa2048 2013-04-08 [SEA]
sig          7455C5E3C0CDCEB9 2013-04-08  Riccardo Spagni <ric@spagni.net>

root@4d11e4ab5407:/# gpg --list-sigs 81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92
pub   rsa4096 2019-12-12 [SCEA]
      81AC591FE9C4B65C5806AFC3F0AF4D462A0BDF92
uid           [ unknown] binaryFate <binaryfate@getmonero.org>
sig 3        F0AF4D462A0BDF92 2019-12-12  binaryFate <binaryfate@getmonero.org>
sig          A923B1EB4C78FD58 2019-12-13  [User ID not found]
sig          464C3B38145F3A14 2019-12-13  [User ID not found]
sub   rsa4096 2019-12-12 [SEA]
sig          F0AF4D462A0BDF92 2019-12-12  binaryFate <binaryfate@getmonero.org>

root@4d11e4ab5407:/# 
```

Am I missing something? Or is it that these keys (last updated on the repo [7 years](https://github.com/monero-project/monero/commits/f4b69d553a249ace3694e3b4fd307ddffa156d7d/utils/gpg_keys/fluffypony.asc) and [2 years ago](https://github.com/monero-project/monero/commits/aa9ba3064e4b59f7c378561f2716ca129bc7f846/utils/gpg_keys/binaryfate.asc), respectively) just need to be updated?

## plowsof | 2022-04-26T16:22:27+00:00
Ok i have the same issue as @maltfield - for some reason we're not able to download _all_ the signatures from the key server using ubuntu/pgp (but they are there when you go to ubuntus keyserver site): just not locally, which is either a configuration option in our gpg clients or as you say, to mitigate some kind flooding attack. Would need to look closer into this problem / bug.

Keys are signed - we just can't import them because 'reasons' 
you would like FluffyPony to sign this [Key Transition Statement](https://riseup.net/en/security/message-security/openpgp/key-transition)

## binaryFate | 2022-04-26T19:15:07+00:00
Due to local config of GPG it's dropping non-self-signed signatures, apparently it may have become default (after this signature flooding thing).

I believe this should work (note the additional flag):

`gpg --keyserver pgp.mit.edu --keyserver-options no-self-sigs-only --receive-keys F0AF4D462A0BDF92 7455C5E3C0CDCEB9`

Here it's _pgp.mit.edu_ not _keyserver.ubuntu.com_ server, to illustrate that the keys and signatures are present on many PGP repositories around the world. These servers regularly syncronize their content together so that a key uploaded on one of them propagate on many/all of them in few hours or days.
As far as I know, this is the primary way for PGP users to look for and share keys (and their attached signatures).

I don't see any harm in adding github as an additional delivery mechanism if that makes some people more comfortable. I actually didn't know you could have an ASCII armored exported public key includes some signatures from another key, but if it's possible, I have no problem adding this.

## plowsof | 2022-04-26T23:56:03+00:00
Thanks @binaryFate worked like a charm: Output
```
gpg --keyserver pgp.mit.edu --keyserver-options no-self-sigs-only --receive-keys F0AF4D462A0BDF92 7455C5E3C0CDCEB9
gpg: key 7455C5E3C0CDCEB9: 34 signatures not checked due to missing keys
gpg: key 7455C5E3C0CDCEB9: "Riccardo Spagni <ric@spagni.net>" 34 new signatures
gpg: key F0AF4D462A0BDF92: 21 signatures not checked due to missing keys
gpg: key F0AF4D462A0BDF92: "binaryFate <binaryfate@getmonero.org>" 21 new signatures
gpg: no ultimately trusted keys found
gpg: Total number processed: 2
gpg:         new signatures: 55
```
Now they appear under ```--list-sigs``` /  ```--list-sig``` as being signed by FluffyPony

## fluffypony | 2022-04-27T01:31:32+00:00
My two cents: GPG signing someone's key is dumb, it went out of fashion ages ago because people went to key signing parties and were using the GPG WoT to indicate "I may have met this person once when we were both drunk" instead of "I know and trust this person". Additionally, key servers have been viewed as centralised repositories, and there are plenty of people who (1) don't have their keys on keyservers, and (2) don't publish their trust graph / relationships in any meaningful way.

As a result, my main "flow" around the use of GPG keys in the Monero repos have been: make sure I GPG-sign merge commits, but SPECIFICALLY those that add new GPG keys to the main source repo. Doing so indicates that I have verified the person's GPG key out-of-band, eg. at a conference or using some form of comms outside of the email address linked to their git commits / GitHub profile.

I can confirm that I have known binaryFate for a LONG time, and that in addition to confirming his GPG key out-of-band before merging it into the repo, I have hung out with him in real life often, and I trust him implicitly - hence the extra step of signing his key and uploading that to a keyserver:)

## fluffypony | 2022-04-27T01:36:16+00:00
ALSO: I'd like to point out that I haven't disappeared, and I may sign releases in future, so it's not so much a transition as much as it is a different maintainer signing releases. I think part of the issue is that everyone got too used to me signing the releases, and that's something that we definitely should change. Moving forward I suggest that if anyone outside of the core team starts signing releases we should indeed have a key transition (or additional maintainer key?) statement of some sort, maybe on /monero-project/meta.

## maltfield | 2022-04-27T07:14:21+00:00
> I can confirm that I have known binaryFate for a LONG time...I trust him implicitly...I may sign releases in future

@fluffypony This is all great info. Can we please get such statements formalized, cryptographically signed, and added to the getmonero blog tagged as `cryptography` and `urgent`? And  with a permalink that's linked-to in future `hashes.txt` files?

## maltfield | 2022-04-27T07:23:09+00:00
I think what you're doing by having individual devs alternate signing of releases is a sane trade-off to get authenticity & integrity in a simple way.

However, I should point-out that a better (and magnitudes more complex) option is available. You can use a single PGP key locked in an HSM and have it sign releases only if m-of-n developers sign-off on the release with their private keys.

 * https://github.com/coreos/fero

Don't let perfect be the enemy of good, but the above solution resolves the issue of users trying to figure out of a release suddenly being signed by a new key is valid or malicious.

## maltfield | 2022-04-27T07:36:47+00:00
> I actually didn't know you could have an ASCII armored exported public key includes some signatures from another key, but if it's possible, I have no problem adding this.

This is the default behavior of `gpg` when exporting a public key. @binaryFate I recommend just exporting your public key from your keyring and updating the file here:

 * https://github.com/monero-project/monero/blob/master/utils/gpg_keys/binaryfate.asc

This should be done whenever:

1. you extend the expiration of your key or
2. you'd like to share your key's new signatures or
3. you revoke your key
4. etc

Before doing so, you may want to import your public key from keyservers, but be aware this can break your keyring if your key has been spammed with malicious signatures. Sadly, for this reason, I argue it's better to maintain the ascii-armored public keys of developers here on GitHub (but continue to use keyservers for distribution of the public key sans-signatures).

# Action History
- Created by: maltfield | 2022-04-24T22:54:06+00:00
