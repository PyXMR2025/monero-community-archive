---
title: build for xmrig on raspberry pi 4
source_url: https://github.com/xmrig/xmrig/issues/1387
author: amitceder
assignees: []
labels: []
created_at: '2019-12-05T09:37:55+00:00'
updated_at: '2021-04-12T15:11:19+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:11:19+00:00'
---

# Original Description
Hi,
I'm trying to build the ubuntu build sequence on raspberry with raspbian.
trying to run it shows it recognized arm v7 and not v8 for some reason, though raspberry uses ARM A72 which is V8.
I also needed to run the cmake with some changes:
down graded the gcc-5 and g++-5 compilers to complete the make.
also running the cmake with flag:
-DOPENCV_EXTRA_EXE_LINKER_FLAGS=-latomic

if I don't do that - the make compile fails due to neon issues.
If I do use the V7, it uses interpreter mode - which of course sucks... (don't even get a single hash).
any suggestions?



# Discussion History
## SChernykh | 2019-12-05T10:03:00+00:00
You have to install 64-bit OS to be able to compile for ARMv8.

## amitceder | 2019-12-05T14:08:26+00:00
I’m pretty sure Raspbian is 64 bit – why would that team create an OS for a 64 bit processor with 32 bit?

 �

From: SChernykh <notifications@github.com> 
Sent: Thursday, December 5, 2019 12:03 PM
To: xmrig/xmrig <xmrig@noreply.github.com>
Cc: amitceder <amitceder@gmail.com>; Author <author@noreply.github.com>
Subject: Re: [xmrig/xmrig] build for xmrig on raspberry pi 4 (#1387)

 �

You have to install 64-bit OS to be able to compile for ARMv8.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/1387?email_source=notifications&email_token=AG3GEINA3GPMFC2JGFVBN23QXDGVLA5CNFSM4JVWVR22YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEGAFMAA#issuecomment-562058752> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AG3GEIMABCTKLORKRRL62VTQXDGVLANCNFSM4JVWVR2Q> .



## amitceder | 2019-12-05T14:17:07+00:00
Oops – I think I understand what you mean – 

 �

From  this I learned that : https://raspberrypi.stackexchange.com/questions/100926/64-bit-os-on-raspberry-pi-4

Seems the user space is 32 bit although the kernel is 64 bit.

 �

From: SChernykh <notifications@github.com> 
Sent: Thursday, December 5, 2019 12:03 PM
To: xmrig/xmrig <xmrig@noreply.github.com>
Cc: amitceder <amitceder@gmail.com>; Author <author@noreply.github.com>
Subject: Re: [xmrig/xmrig] build for xmrig on raspberry pi 4 (#1387)

 �

You have to install 64-bit OS to be able to compile for ARMv8.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/1387?email_source=notifications&email_token=AG3GEINA3GPMFC2JGFVBN23QXDGVLA5CNFSM4JVWVR22YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEGAFMAA#issuecomment-562058752> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AG3GEIMABCTKLORKRRL62VTQXDGVLANCNFSM4JVWVR2Q> .



## grahamreeds | 2020-05-28T12:53:49+00:00
A 64bit Kernal + 64bit userland was released today. I can confirm that the 3b+ builds and runs xmrig with no editing of the cmake files needed. 

## amitceder | 2020-05-28T20:37:41+00:00
I was able to do that with gentoo 64b server for pi4 a week ago.
it required to install on it ubuntu server with virtual machine, and that
actually worked as 64b.


On Thu, May 28, 2020, 3:54 PM Graham Reeds <notifications@github.com> wrote:

> A 64bit Kernal + 64bit userland was released today. I can confirm that the
> 3b+ builds and runs xmrig with no editing of the cmake files needed.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1387#issuecomment-635331606>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AG3GEIJMR6AHNKDBIK3DQ3LRTZNGZANCNFSM4JVWVR2Q>
> .
>


## grahamreeds | 2020-05-29T08:25:53+00:00
Yes, and I was able to do it using nspawn last week or installing d64.

Point is: no VM's needed or convoluted jumping through hoops.

On Thu, 28 May 2020 at 21:37, amitceder <notifications@github.com> wrote:

> I was able to do that with gentoo 64b server for pi4 a week ago.
> it required to install on it ubuntu server with virtual machine, and that
> actually worked as 64b.
>
>
> On Thu, May 28, 2020, 3:54 PM Graham Reeds <notifications@github.com>
> wrote:
>
> > A 64bit Kernal + 64bit userland was released today. I can confirm that
> the
> > 3b+ builds and runs xmrig with no editing of the cmake files needed.
> >
> > —
> > You are receiving this because you authored the thread.
> > Reply to this email directly, view it on GitHub
> > <https://github.com/xmrig/xmrig/issues/1387#issuecomment-635331606>, or
> > unsubscribe
> > <
> https://github.com/notifications/unsubscribe-auth/AG3GEIJMR6AHNKDBIK3DQ3LRTZNGZANCNFSM4JVWVR2Q
> >
> > .
> >
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1387#issuecomment-635594126>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABGL3HE2EQPAHBMMKCXCA5DRT3DSFANCNFSM4JVWVR2Q>
> .
>


## amitceder | 2020-05-29T20:59:11+00:00
sounds good, will try it on sunday

On Fri, May 29, 2020, 11:26 AM Graham Reeds <notifications@github.com>
wrote:

> Yes, and I was able to do it using nspawn last week or installing d64.
>
> Point is: no VM's needed or convoluted jumping through hoops.
>
> On Thu, 28 May 2020 at 21:37, amitceder <notifications@github.com> wrote:
>
> > I was able to do that with gentoo 64b server for pi4 a week ago.
> > it required to install on it ubuntu server with virtual machine, and that
> > actually worked as 64b.
> >
> >
> > On Thu, May 28, 2020, 3:54 PM Graham Reeds <notifications@github.com>
> > wrote:
> >
> > > A 64bit Kernal + 64bit userland was released today. I can confirm that
> > the
> > > 3b+ builds and runs xmrig with no editing of the cmake files needed.
> > >
> > > —
> > > You are receiving this because you authored the thread.
> > > Reply to this email directly, view it on GitHub
> > > <https://github.com/xmrig/xmrig/issues/1387#issuecomment-635331606>,
> or
> > > unsubscribe
> > > <
> >
> https://github.com/notifications/unsubscribe-auth/AG3GEIJMR6AHNKDBIK3DQ3LRTZNGZANCNFSM4JVWVR2Q
> > >
> > > .
> > >
> >
> > —
> > You are receiving this because you commented.
> > Reply to this email directly, view it on GitHub
> > <https://github.com/xmrig/xmrig/issues/1387#issuecomment-635594126>, or
> > unsubscribe
> > <
> https://github.com/notifications/unsubscribe-auth/ABGL3HE2EQPAHBMMKCXCA5DRT3DSFANCNFSM4JVWVR2Q
> >
> > .
> >
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1387#issuecomment-635843907>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AG3GEIIZOOY55RQZOLXKUKTRT5WR5ANCNFSM4JVWVR2Q>
> .
>


# Action History
- Created by: amitceder | 2019-12-05T09:37:55+00:00
- Closed at: 2021-04-12T15:11:19+00:00
