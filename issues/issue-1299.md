---
title: generic code for randomX
source_url: https://github.com/xmrig/xmrig/issues/1299
author: amitceder
assignees: []
labels:
- question
created_at: '2019-11-18T11:06:01+00:00'
updated_at: '2019-12-22T19:36:33+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:36:33+00:00'
---

# Original Description
Hi,
Is there a possibility to release a generic code and not platform sepcific?
in variant 4 there was a generic one, but for randomx it seems there's a source for jit_compiler only for arm64 bit or for x86.


# Discussion History
## SChernykh | 2019-11-18T15:11:36+00:00
JIT compiler will be used on supported platform (ARM64 and x86-64), all other platforms will automatically use VM interpreter (what you call "generic code").

## amitceder | 2019-11-18T17:31:01+00:00
Thanks for your quick reply.

Will this (VM interpreter) be supported in the future or already in version 5.0.0 ?

Are the relevant files for other platforms are the one starting with vm_interpreted and vm_compiled?

Amit

 �

 �

From: SChernykh <notifications@github.com> 
Sent: Monday, November 18, 2019 5:12 PM
To: xmrig/xmrig <xmrig@noreply.github.com>
Cc: amitceder <amitceder@gmail.com>; Author <author@noreply.github.com>
Subject: Re: [xmrig/xmrig] generic code for randomX (#1299)

 �

JIT compiler will be used on supported platform (ARM64 and x86-64), all other platforms will automatically use VM interpreter (what you call "generic code").

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/1299?email_source=notifications&email_token=AG3GEIOZ3ZMCJUSC3ETRI2TQUKWDLA5CNFSM4JORXGJ2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEEKYDOA#issuecomment-555057592> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AG3GEIPVNOSEBFFLU2MUN4DQUKWDLANCNFSM4JORXGJQ> .



## amitceder | 2019-11-18T17:32:28+00:00
more precisely - is there a define or any build instructions for other platforms? 

## SChernykh | 2019-11-18T17:34:21+00:00
You just build it normally, JIT compiler files are only included in the build on supported platforms. Then at runtime XMRig will check if JIT compiler is available and select VM interpreter if there is no JIT.

## amitceder | 2019-11-20T15:01:20+00:00
another related question:
Is there a way to run the function "randomx_calculate_hash" which is under randomx.cpp on a separate machine? (connecting them with simple udp connection for example).

## trasherdk | 2019-11-21T03:19:30+00:00
@amitceder Something like a [proxy](https://github.com/xmrig/xmrig-proxy)?

## amitceder | 2019-11-21T13:03:27+00:00
not exactly. more like running a pc for the linux connectivity to the ethernet, protocol handling etc, while the other runs the virutal machine.

# Action History
- Created by: amitceder | 2019-11-18T11:06:01+00:00
- Closed at: 2019-12-22T19:36:33+00:00
