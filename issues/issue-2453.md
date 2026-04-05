---
title: Is it possible to compile every thing into one single executable?
source_url: https://github.com/xmrig/xmrig/issues/2453
author: Joe23232
assignees: []
labels:
- question
created_at: '2021-06-23T13:18:56+00:00'
updated_at: '2021-06-28T12:24:23+00:00'
type: issue
status: closed
closed_at: '2021-06-28T12:24:23+00:00'
---

# Original Description
Hi there, so I have been following instructions on how to compile `xmrig`  for Windows. I followed these instructions:

```
1. pacman -S mingw-w64-x86_64-gcc git make
2. git clone https://github.com/xmrig/xmrig.git
3. mkdir xmrig/build && cd xmrig/build
4. "c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64
5. make -j$(nproc)
```
and some addtional instructions according to this [issue](https://github.com/xmrig/xmrig/issues/2452#issuecomment-865935014) that I created.

My question is:

1. Is it possible to compile everything into a single executable?
2. if `1` is applicable, then does `xmrig` _still_ require dynamic dependencies (that is NOT preinstalled on Windows 7/10) where I have to install separately on Windows?
3. If `2` is applicable, then is there an easy way to statically link all those other dependencies so it will run on Windows just fine?
4. Are there otherways to improve the performance of the application by using special flags or something which does NOT build specifically for the CPU and it will work on any `x64` CPU architecture still?

The current way I am compile creates a lot of files:

![image](https://user-images.githubusercontent.com/34926497/123103407-4e04c980-d479-11eb-82f2-680f72e29ab1.png)

Do I need all these files or can I run `xmrig.exe` on its own?

If I can't then is there a way to statically compile this into one single executable?

# Discussion History
## Spudz76 | 2021-06-23T20:13:04+00:00
WinRing0x64.sys is required for MSR access and must be a sys/driver file due to Windows limitations.  It will run without it but you get no MSR setting features then.  You can install Open Hardware Monitor which installs a Ring0 driver and then xmrig will use that one instead (still technically external but part of a different installer).

`-DBUILD_STATIC=ON` added to the cmake command (step 4) should make everything else part of the exe.  I have never not built directly on the rig so I am not sure about portability of the result.

## Pemekk | 2021-06-23T20:48:53+00:00
#2453

ในวันที่ พฤ. 24 มิ.ย. 2021 03:13 น. Tony Butler ***@***.***>
เขียนว่า:

> WinRing0x64.sys is required for MSR access and must be a sys/driver file
> due to Windows limitations. It will run without it but you get no MSR
> setting features then. You can install Open Hardware Monitor which installs
> a Ring0 driver and then xmrig will use that one instead (still technically
> external but part of a different installer).
>
> -DBUILD_STATIC=ON added to the cmake command (step 4) should make
> everything else part of the exe. I have never not built directly on the rig
> so I am not sure about portability of the result.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2453#issuecomment-867126603>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AUEA5UOUQEVUUXPTKYIU4ITTUI55TANCNFSM47FZINRA>
> .
>


## Joe23232 | 2021-06-24T10:33:11+00:00
@Spudz76 Hi and thanks for your response,

> It will run without it but you get no MSR setting features then.

Is this some monitoring program this MSR thingy?

## Spudz76 | 2021-06-24T19:23:03+00:00
Well, MSR means *Model Specific Registers* and they do lots of things.  Model Specific just means they are different per CPU model.  It's where deep CPU settings *and* reporting are, so it's for both monitoring and control.  Since it is a very low-level knob it requires "Ring0" in windows which is like a driver that can get kernel-access to the CPU.  Normal user programs do not have access, even as Administrator.  Therefore a driver stub `sys` file.  You also have to have SecureBoot off or BIOS blocks the OS from MSR access.

In xmrig it is used to turn off cache prefetch since the predictor doesn't predict the patterns RandomX uses and thus wastes cache bandwidth prefetching things nobody needs.  You can sometimes disable prefeches in BIOS if the options are there, but not all motherboards have that.

In Open Hardware Monitor it is used to read Vendor-specific things like Watts or voltage or some thermals that aren't available through the usual sensor API (which may only provide case therms and not on-die therms or watts or etc).

Prefetch-off helps various amounts depending on the CPU.  It's not required just a tweak that adds a bit more hashrate.

## Joe23232 | 2021-06-25T08:38:26+00:00
@Spudz76 

> Well, MSR means Model Specific Registers and they do lots of things. Model Specific just means they are different per CPU model.

Is there some argument I can pass when executing `xmrig` to automatically optimize RandomX as much as possible?

> Prefetch-off helps various amounts depending on the CPU. It's not required just a tweak that adds a bit more hashrate.

How do I do `Prefetch-off`?

## Spudz76 | 2021-06-25T17:07:32+00:00
Either you check BIOS for stuff that says prefetch, and turn them all off.  They might not be there.

Or you drag the ring0 sys file around with the executable.  Or you install Open Hardware Monitor and use its ring0 service.

## Joe23232 | 2021-06-26T07:09:21+00:00
I see, thanks mate :)

On Sat, Jun 26, 2021 at 3:07 AM Tony Butler ***@***.***>
wrote:

> Either you check BIOS for stuff that says prefetch, and turn them all off.
> They might not be there.
>
> Or you drag the ring0 sys file around with the executable. Or you install
> Open Hardware Monitor and use its ring0 service.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2453#issuecomment-868708425>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AIKO7IJUPRH7E4ENYY5VLALTUSZV5ANCNFSM47FZINRA>
> .
>


## Pemekk | 2021-06-28T05:36:05+00:00
#2453

ในวันที่ พฤ. 24 มิ.ย. 2021 17:33 น. Joe23232 ***@***.***>
เขียนว่า:

> @Spudz76 <https://github.com/Spudz76> Hi and thanks for your response,
>
> It will run without it but you get no MSR setting features then.
>
> Is this some monitoring program this MSR thingy?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2453#issuecomment-867528282>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AUEA5UPUH7JM3HLPHMHC7ATTUMCXDANCNFSM47FZINRA>
> .
>


# Action History
- Created by: Joe23232 | 2021-06-23T13:18:56+00:00
- Closed at: 2021-06-28T12:24:23+00:00
