---
title: About static.
source_url: https://github.com/xmrig/xmrig/issues/9
author: ghost
assignees: []
labels: []
created_at: '2017-05-27T02:53:05+00:00'
updated_at: '2017-09-03T03:09:49+00:00'
type: issue
status: closed
closed_at: '2017-09-03T03:09:49+00:00'
---

# Original Description
This is a best miner.
I have different versions of Linux.
I don't know how to do static compilation.

This is CentOS 6.8.GCC 5.1:

[xblacktimes_012@localhost Desktop]$ ldd yam 
	not a dynamic executable
[xblacktimes_012@localhost Desktop]$ ldd xmrig
	linux-vdso.so.1 =>  (0x00007fffa6875000)
	libcurl.so.4 => /usr/lib64/libcurl.so.4 (0x00007f6bab4dc000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x000000346ae00000)
	libc.so.6 => /lib64/libc.so.6 (0x000000346aa00000)
	libcares.so.2 => /usr/lib64/libcares.so.2 (0x00007f6bab2ca000)
	libnghttp2.so.14 => /usr/lib64/libnghttp2.so.14 (0x00007f6bab0a9000)
	libssh2.so.1 => /usr/lib64/libssh2.so.1 (0x00007f6baae7d000)
	libssl.so.10 => /usr/lib64/libssl.so.10 (0x000000347b600000)
	libcrypto.so.10 => /usr/lib64/libcrypto.so.10 (0x0000003477a00000)
	libgssapi_krb5.so.2 => /lib64/libgssapi_krb5.so.2 (0x0000003477e00000)
	libkrb5.so.3 => /lib64/libkrb5.so.3 (0x0000003479e00000)
	libk5crypto.so.3 => /lib64/libk5crypto.so.3 (0x0000003479a00000)
	libcom_err.so.2 => /lib64/libcom_err.so.2 (0x0000003477200000)
	libldap-2.4.so.2 => /lib64/libldap-2.4.so.2 (0x000000347f200000)
	libz.so.1 => /lib64/libz.so.1 (0x000000346be00000)
	librt.so.1 => /lib64/librt.so.1 (0x000000346b600000)
	/lib64/ld-linux-x86-64.so.2 (0x000000346a600000)
	libdl.so.2 => /lib64/libdl.so.2 (0x000000346b200000)
	libkrb5support.so.0 => /lib64/libkrb5support.so.0 (0x0000003478600000)
	libkeyutils.so.1 => /lib64/libkeyutils.so.1 (0x0000003478200000)
	libresolv.so.2 => /lib64/libresolv.so.2 (0x000000346ce00000)
	liblber-2.4.so.2 => /lib64/liblber-2.4.so.2 (0x000000347ea00000)
	libsasl2.so.2 => /usr/lib64/libsasl2.so.2 (0x000000347fe00000)
	libssl3.so => /usr/lib64/libssl3.so (0x000000347ba00000)
	libsmime3.so => /usr/lib64/libsmime3.so (0x000000347be00000)
	libnss3.so => /usr/lib64/libnss3.so (0x0000003479600000)
	libnssutil3.so => /usr/lib64/libnssutil3.so (0x0000003478e00000)
	libplds4.so => /lib64/libplds4.so (0x000000347a600000)
	libplc4.so => /lib64/libplc4.so (0x0000003478a00000)
	libnspr4.so => /lib64/libnspr4.so (0x000000347a200000)
	libselinux.so.1 => /lib64/libselinux.so.1 (0x000000346c600000)
	libcrypt.so.1 => /lib64/libcrypt.so.1 (0x0000003476600000)
	libfreebl3.so => /lib64/libfreebl3.so (0x0000003476a00000)

# Discussion History
## xmrig | 2017-05-27T05:18:25+00:00
Static build more complicated, first you need custom libcurl build to reduce dependencies, see windows instructions for example https://github.com/xmrig/xmrig#windows
After that remove line 95 and 97 https://github.com/xmrig/xmrig/blob/master/CMakeLists.txt#L95 to enable static build.

I have some issues with libcurl, it can be crashed if you run on different linux version. For example static build for Ubuntu 16.04 work fine on Debian 8 too, but crashed on newer Ubuntu versions. I have plans to remove libcurl in next major update.

Thank you.

## ghost | 2017-06-01T07:52:17+00:00
5

## fpgablr | 2017-06-07T08:11:27+00:00
i am looking for help to build an fpga based mining kit using cryptonight
algo.. Can you assist me in this project?


On Mon, Jun 5, 2017 at 10:45 PM, x052 <notifications@github.com> wrote:

> I also can't build statically, is there any more detail you can provide to
> help?
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/9#issuecomment-306247530>, or mute
> the thread
> <https://github.com/notifications/unsubscribe-auth/Ab02F8JsNAjuhsai3bpAUYwJkvi91yw3ks5sBDeugaJpZM4NoNh->
> .
>


## xmrig | 2017-06-07T14:36:37+00:00
@x052 Still can't build?

@fpgablr cryptonight is designed to avoid FPGA/ASIC and do it very well. Each hash required 2 MB of fast low latency memory.

I heard available some FPGAs with that amount of memory, 1 cycle latency it's looks very good.
But... price $1000-$2000 and more for just only chip, without board, without development.
But... #2 Just 250 MHz, it can eat all profit from fast memory.

So this is a very high-risk, expensive adventure. Probably you just lose your money without any profit. If you ok with that, I know one guy who works with FPGA, maybe he can help you. Please feel free to contact me via email for more details.

## b-i-t-n | 2017-07-01T12:17:16+00:00
@ghost you could use Docker for this.
I have an [example](https://github.com/b-i-t-n/alpine-xmrig/blob/master/Dockerfile) and [images](https://hub.docker.com/r/bitnn/alpine-xmrig/) available.

Contact me if you need help.

# Action History
- Created by: ghost | 2017-05-27T02:53:05+00:00
- Closed at: 2017-09-03T03:09:49+00:00
