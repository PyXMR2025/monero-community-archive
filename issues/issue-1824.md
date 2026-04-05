---
title: Why no more "notls" builds?
source_url: https://github.com/xmrig/xmrig/issues/1824
author: APT-ZERO
assignees: []
labels: []
created_at: '2020-09-05T08:14:18+00:00'
updated_at: '2021-06-22T15:08:03+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:49:52+00:00'
---

# Original Description
Hi
i like xmrig, it's opensource, standalone, portable, low size, have compiled releases, good hashrate, etc.
and i always using notls file for reasons
idk why you don't compile notls builds anymore
if there is a problem that made you do this, it's OK
but if you are able to compile notls builds, do this please
thank you

# Discussion History
## xmrig | 2020-09-05T11:26:07+00:00
If notls builds will be available only as separate downloads on https://download.xmrig.com/xmrig/ user `xmrig` password `download` is it OK for you? also you don't mention the OS I guess it's Windows?
Thank you.

## APT-ZERO | 2020-09-05T14:00:22+00:00
Yes, That would be fine
And Y, I Meant Windows x64

## APT-ZERO | 2020-09-05T14:08:15+00:00
idk i have to Close this issue or not :|
do it yourself ☹️❤️

## xmrig | 2020-09-05T16:23:58+00:00
https://download.xmrig.com/xmrig/6.3.3/ba336122c0cae2345e568cba63c2ca691301b8f0/xmrig-6.3.3-notls-gcc-win64.zip
https://download.xmrig.com/xmrig/6.3.3/ba336122c0cae2345e568cba63c2ca691301b8f0/xmrig-6.3.3-notls-msvc-win64.zip

## DeadManWalkingTO | 2020-10-08T21:23:51+00:00
You can always compile "notls" builds with `-DWITH_TLS=OFF` disable SSL/TLS support (secure connections to pool). This feature add external dependency to OpenSSL.

## APT-ZERO | 2021-06-22T08:23:22+00:00
@xmrig would you please add "gcc win64 notls"?


## xmrig | 2021-06-22T09:25:29+00:00
@Cyber-Criminal They is still in the same place for every commit https://download.xmrig.com/xmrig/6.12.2/80ae339343f6004ae105e27c71180c0220c939b8 (password mentioned above) just not in github releases.
Thank you.

## APT-ZERO | 2021-06-22T15:08:03+00:00
sorry, i asked because i looked at another folder and it was not there
but it is there in the folder that you linked
thank you

# Action History
- Created by: APT-ZERO | 2020-09-05T08:14:18+00:00
- Closed at: 2021-04-12T14:49:52+00:00
