---
title: Store binary checksums alongside with files being released
source_url: https://github.com/monero-project/monero-site/issues/811
author: artyomsol
assignees: []
labels:
- downloads
- feature
created_at: '2018-07-27T15:39:37+00:00'
updated_at: '2022-08-31T21:27:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`downloads.getmonero.org` holds historical releases for some reasons, but _canonical_ PGP-singed checksums `https://getmonero.org/downloads/hashes.txt` are for the last one release (tough it mentioned on every release note on github for all versions the same).
If previous releases are need to be available they must be provided with signed hashes files for every single version. 
It would be convenient to have them at the same resource as a binaries are.

# Discussion History
## el00ruobuob | 2018-07-27T15:58:15+00:00
The old release are not removed from the website, but they are not available through any link on downloads.getmonero.org.
So, i do not believe we should offer the pgp hash from the website itself. Perhaps should we remove the old binaries.

## artyomsol | 2018-08-17T07:24:33+00:00
@el00ruobuob Old release files  referenced to the `downloads.getmonero.org` by github release pages (i.e. https://github.com/monero-project/monero/releases/tag/v0.12.2.0). Where last paragraf states:

> A GPG-signed list of the hashes is at https://getmonero.org/downloads/hashes.txt and should be treated as canonical, with the signature checked against the appropriate GPG key in the source code (in /utils/gpg_keys)

## binaryFate | 2021-05-17T12:44:30+00:00
Note that you can check the git history of `hashes.txt` for any past version. On github it's at https://github.com/monero-project/monero-site/commits/master/downloads/hashes.txt


## KunNw0n | 2021-05-17T13:46:20+00:00
> Note that you can check the git history of `hashes.txt` for any past version.

Yeap. That is exactly what I am doing for instance to verify hashes of recent releases
```shell
  set -exu; \
  xmrArch="monero-linux-x64-v${XMR_VERSION}.tar.bz2"; \
  curl -SLO https://downloads.getmonero.org/cli/$xmrArch; \
# scan canonical downloads/hashes.txt for latest signed checksum
  curl -sSL "https://github.com/monero-project/monero-site/commits/master/downloads/hashes.txt" | \
    sed -nE 's;^.*href="/monero-project/monero-site/commit/([a-f0-9]{40})#diff-.*$;\1;p' | \
      while read _COMMIT; do \
        hashes=$(curl -sS "https://raw.githubusercontent.com/monero-project/monero-site/$_COMMIT/downloads/hashes.txt"); \
        if echo "$hashes" | grep -qE "^($xmrArch,\s+[a-f0-9]{64}|[a-f0-9]{64}\s+\*?$xmrArch)$"; then \
          echo "$hashes" > hashes.txt && break; \
        fi; \
      done; \
  gpg --no-tty --batch --verify hashes.txt; \
  test "$(grep "$xmrArch" hashes.txt | grep -oE "[a-f0-9]{64}")" = "$(sha256sum -b $xmrArch | cut -d" " -f1)"; \
  tar --transform 's:.*/::g' -xaf *.tar.bz2 -C /usr/local/bin; \
```
This ugly workaround could be reduced significantly if signed `hashes.txt` will be available on `downloads.getmonero.org` for every binaries version.

## binaryFate | 2021-05-17T15:29:11+00:00
@KunNw0n what about we add a second file `old-hashes.txt` that contains a forever expending list of all hashes for all versions? (`hashes.txt` would keep having only last version).

My concern with your proposal of one `hashes.txt` per version is that newbies and users that are not too technical will be totally lost. It's already a challenge to have them check the hashes at all.

## KunNw0n | 2021-05-17T15:49:55+00:00
@binaryFate 
> what about we add a second file `old-hashes.txt` that contains a forever expending list of all hashes for all versions?

Totally fine as long as it has actual PGP signature (means it should be re-signed every time after update).  
I'd better to back up previous `hashes.txt` to a `hashes-v.X.Y.Z.txt` during release of the new version. Then it will keep not only the hashes but the signature aswell.

> My concern with your proposal of one `hashes.txt` per version is that newbies and users that are not too technical will be totally lost.

Having single version tagged file per release version (i.e. `hashes-v.X.Y.Z.txt`) is not harder to deal with while one chooses proper binary archive `monero-linux-x64-vX.Y.Z.tar.bz2`, IMHO.
Newbies ~and muggles~ are out of scope of this issue - they should always use the latest one release.

## binaryFate | 2021-05-17T17:24:29+00:00
> Having single version tagged file per release version (i.e. hashes-v.X.Y.Z.txt)

I'm fine with this. (And indeed, as long as it does not change anything to the current simple enough workflow for most users and does not add any confusion to what they can read or do, it's ok).
Let's see if anyone has more comments.

## erciccione | 2021-05-19T07:01:51+00:00
Ok for me too.

## artyomsol | 2021-05-21T09:23:00+00:00
> Having single version tagged file per release version (i.e. hashes-v.X.Y.Z.txt)

Indeed, it is the solution I was expecting to see. 

## binaryFate | 2022-08-31T21:27:14+00:00
ping myself @binaryFate discussed on IRC again and todo

# Action History
- Created by: artyomsol | 2018-07-27T15:39:37+00:00
