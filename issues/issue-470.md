---
title: 'Build: cannot find -lepee'
source_url: https://github.com/monero-project/monero-gui/issues/470
author: voidzero
assignees: []
labels: []
created_at: '2017-02-12T00:01:46+00:00'
updated_at: '2017-03-03T01:13:30+00:00'
type: issue
status: closed
closed_at: '2017-03-03T01:13:30+00:00'
---

# Original Description
Trying to build monero-core on Linux 64bit (Gentoo) gives me this message.

So I tried to issue this command by hand:
`make -C monero/build/release/contrib/epee all install`
This does create libepee.a in monero-core/monero/lib/libepee.a. But when I follow it up with build.sh, the message is "cannot find -lepee" and when I check the directory monero/lib again, the file libepee.a is indeed gone.

So then I figured, let's prevent deletion and did 'chattr +i monero/lib/libepee.a'. Ran build again, and here's where it seems to happen:

<pre>
cleaning up existing monero build dir, libs and includes
rm: cannot remove ‘/mnt/coindb/src/monero-core/monero/lib/libepee.a’: Operation not permitted
</pre>

It still doesn't build - but that's now because of a different reason, lots of undefined references to cryptonote::foo.

# Discussion History
## thoriumbr | 2017-02-16T17:18:14+00:00
Edit `monero-wallet-gui.pro` and change this:

`-lepee \`
with
`$$WALLET_ROOT/build/release/contrib/epee/src/libepee.a \`



## voidzero | 2017-02-17T16:12:22+00:00
Thanks for your comment. Yeah I did try that but essentially it's doing the same thing though because that path is already specified with -L.

But the problem is that libepee.a file disappears like I said.

The chattr +i is a working workaround but certainly not clean. I can't figure out where it is removed. It seems that get_libwallet_api.sh deletes stuff as part of "cleaning up existing monero build dir, libs and includes" but even if I comment it out it is deleted by something else. So the problem is not that libepee cannot be found - the problem is that libepee.a is unjustly deleted.

## voidzero | 2017-02-17T16:13:31+00:00
Oh, and, after get_libwallet_api.sh I do have to run that make command by hand.

<pre>
make -C monero/build/release/contrib/epee all install
</pre>

## Jaqueeee | 2017-02-17T17:30:32+00:00
This is fixed in #466 
Merge that PR and you should be ok. 
ping @fluffypony 

## voidzero | 2017-03-03T01:13:30+00:00
This is fixed indeed. Closing. Thank you!

# Action History
- Created by: voidzero | 2017-02-12T00:01:46+00:00
- Closed at: 2017-03-03T01:13:30+00:00
