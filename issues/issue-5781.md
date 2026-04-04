---
title: '[discussion] Improve release archive compression'
source_url: https://github.com/monero-project/monero/issues/5781
author: jonathancross
assignees: []
labels: []
created_at: '2019-07-29T16:45:38+00:00'
updated_at: '2020-05-27T13:14:02+00:00'
type: issue
status: closed
closed_at: '2020-05-27T13:14:02+00:00'
---

# Original Description
Per #5764 It seems there is interest in improving the compression used on the release tarballs.

Here is a useful [compression comparison](https://community.centminmod.com/threads/compression-comparison-benchmarks-zstd-vs-brotli-vs-pigz-vs-bzip2-vs-xz-etc.12764/) which we can use as a general tool for discussion.

In Monero, we also want to have perfectly deterministic compression for reproducible builds. 

### Discussion summary so far...

@hyc Suggested exploring zstd & also mentioned we might checksum the tar file instead of compressed output.

From what I can see, `zstd` is mostly focused on improving compression speed, but it produces larger files than `bzip2` or `xz` (higher priority IMO). I'm a bit hesitant about this because it is not installed by default on the Ubuntu bionic guest OS.  It is also unclear how deterministic the compression output is.

As for checksums of the tar file, I am concerned this would hurt UX and make verification much harder as the Gitian checksummed content (`.tar` file) would not match what was released / signed by fluffypony in [hashes.txt](https://web.getmonero.org/downloads/hashes.txt) (compressed tar files which users download).  If I build with gitian, I cannot be 100% sure it was the same as what fluffy signed.

@ndorf and @fluffypony were interested in switching to `xz`, but this may present problems because compressed output is not deterministic between versions and we currently don't lock down the version.

I found that compressing with multiple threads also broke determinism. Others have expressed [concern about the long-term viability of xz archives](https://www.nongnu.org/lzip/xz_inadequate.html) because of the container structure / flexibility of the format.  Seems like a brittle format.

### xz vs bzip2 compression

Here are some timing / file size comparisons between `bzip2` and `xz` on an i5 Ubuntu system.  I was compressing the `monero-aarch64-linux-gnu.tar` file that is 203MB:

```
+---+------------+------------+-----------
|   |    bzip2   |     xz     | xz --threads=4
| L | TIME  SIZE | TIME  SIZE | TIME  SIZE
+---+------------+------------+-----------
| 0 |   na       | 14.37s 55M |  6.63s 56M
| 1 | 21.60s 65M | 21.06s 52M |  8.59s 53M
| 2 | 21.46s 63M | 30.43s 50M | 11.55s 51M
| 3 | 21.65s 62M | 42.14s 50M | 15.78s 50M
| 4 | 22.33s 61M | 66.91s 47M | 27.35s 47M
| 5 | 23.01s 61M | 84.67s 44M | 35.84s 45M
| 6 | 23.54s 60M | 94.46s 44M | 41.00s 45M
| 7 | 24.67s 60M | 95.49s 28M | 39.35s 31M
| 8 | 24.89s 60M | 95.11s 19M | 51.43s 22M
| 9 | 25.62s 60M | 97.59s 19M | 92.17s 20M
+---+------------+------------+-----------
```

As you can see, `bzip2` doesn't vary much in terms of speed or compression.  `xz` performance varies more dramatically as compression level (`L`) increases.

Here is the 1-liner you can use in your own tests:
```bash
PROG='xz --threads=1'; EXT='xz'; FN=monero-aarch64-linux-gnu; for LEV in `seq 0 9`;do S=$(date +%s%N);${PROG} -cz -${LEV} ${FN}.tar > ${FN}-${LEV}.tar.${EXT};E=$(date +%s%N);TOTAL=$(echo "scale=2; ($E - $S) / 1000000000"|bc); SIZE=$(du -h ${FN}-${LEV}.tar.${EXT} | cut -f1); echo "${PROG} -${LEV}: ${TOTAL}s | ${SIZE}";done
```
To test bzip2, use: `PROG=bzip2` and `EXT=bz2` and `seq 1 9` as bzip2 doesn't support level `0` compression.

# Discussion History
## hyc | 2019-07-29T17:20:40+00:00
re: verifying based on uncompressed checksum - it's as simple as "zcat foo.tar.gz | sha256sum" - I expect that anyone savvy enough to actually compare the checksums can handle this.

re: xz vs bzip2 - the size difference is pretty impressive. But yes, the file format problems seem pretty nasty.

Looks like bzip2 may be the best choice, particularly if we can lock down a specific version in the docker image and prevent it from getting any further updates.



## jonathancross | 2019-08-11T17:46:57+00:00
Thanks for the feedback @hyc.  Hopefully others can chime in. 

> re: verifying based on uncompressed checksum - it's as simple as "zcat foo.tar.gz | sha256sum" - I expect that anyone savvy enough to actually compare the checksums can handle this.

True enough.  I'd still prefer it as easy as possible, every additional step introduces potential for error, misunderstanding or causing people to simply not verify out of laziness.  I'm concerned there are already too few people checking signatures / checksums.

> re: xz vs bzip2 - the size difference is pretty impressive. But yes, the file format problems seem pretty nasty.

Yep.  Agree.
I was not happy to see that using multiple threads in `xz` also produced different output -- supports assertion that this is not the best format for consistent archives.  I suspect there are other undocumented ways to break consistency.

> bzip2 may be the best choice, particularly if we can lock down a specific version in the docker image and prevent it from getting any further updates.

We may not be able to lock down a specific package _inside_ a docker image, but the important thing here is that the version of `bzip2` used is consistent for anyone building a given git tag.  It can change _between_ tags though.  I believe we can rather easily lock down the specific image used (full Ubuntu Bionic image) so it matches a specific git tag.  In talking to @TheCharlatan, it seems we are likely to do that anyway.

One issue with this is that it will mean we have a static set of inputs and will not benefit from security / bug fixes until that image ID is manually updated.  Maybe there is a better solution offered by docker (I'm new to all of this and will look into it a bit).

## ndorf | 2019-08-12T20:05:29+00:00
Checksumming the uncompressed archive is less than ideal, because it would prevent the `sha256sum -c` option from working.

The upstream versions of all packages are fixed when a given Ubuntu (or Debian) release is done. So, `ubuntu:bionic` will always come with the same version of `xz-utils`. Of course, if you use `:latest` instead of `:bionic` then it will change when bionic's successor is released, but so will the compilers, the linker, and every other tool in the chain.

As for multi-threaded compression, bzip2 doesn't seem to support that at all, so I don't see why that should stop us from using xz, as long as it meets our requirements in its single-threaded mode.

## hyc | 2019-08-12T20:39:34+00:00
> The upstream versions of all packages are fixed when a given Ubuntu (or Debian) release is done.
 
Not quite. I've seen my gitian environments pull down a slew of updates when such Ubuntu updates are published.

## ndorf | 2019-08-12T21:00:58+00:00
> > The upstream versions of all packages are fixed when a given Ubuntu (or Debian) release is done.
> 
> Not quite. I've seen my gitian environments pull down a slew of updates when such Ubuntu updates are published.

Yes but those updates do not use newer upstream versions. They only contain backports of issues deemed 'critical' back to the version the Ubuntu release uses, just like Debian releases.

For `xz-utils`, the last time that happened was before the xenial release in 2014: http://changelogs.ubuntu.com/changelogs/pool/main/x/xz-utils/xz-utils_5.1.1alpha+20120614-2ubuntu2/changelog (there were no updates during the entire lifecycle of xenial, or in bionic so far)

Note that the upstream version remains the same, only the ubuntu patch number changes. The entire point of this release/upgrade process is to ensure that user-observable behavior in installed packages does not change between releases. If the output of `xz` were to suddenly change in bionic, that would be a very valid bug against the Ubuntu package unless there was no other feasible way to fix a security vulnerability or other critical bug.



## ndorf | 2019-08-12T21:03:36+00:00
(Just for completeness, there is at least one exception to that in Ubuntu: the Firefox packages. That exception is stated explicitly though and isn't relevant to any of the packages we're discussing here.)

## ndorf | 2019-08-12T21:08:57+00:00
The actual requirements for updating packages in a stable Ubuntu release: https://wiki.ubuntu.com/StableReleaseUpdates

## moneromooo-monero | 2019-08-19T15:20:08+00:00
We don't really care about compression speed. It's compressed once, and decompressed many times. When compressed, it's also done after a lot more time spent building. File size is more relevant here. About checksum/signing, it's best done on the final blob, since it avoids any possible exploit that involves manipulating the compressed stream.

## moneromooo-monero | 2020-05-16T16:24:59+00:00
Anyone going to do anything here ?

## jonathancross | 2020-05-21T16:41:42+00:00
> Anyone going to do anything here ?

IMO bz2 compression works _well enough_ as-is.

## moneromooo-monero | 2020-05-27T13:14:02+00:00
Alright, closing.

# Action History
- Created by: jonathancross | 2019-07-29T16:45:38+00:00
- Closed at: 2020-05-27T13:14:02+00:00
