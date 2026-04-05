---
title: --cpu-priority not being honored?
source_url: https://github.com/xmrig/xmrig/issues/2351
author: rpodgorny
assignees: []
labels:
- bug
created_at: '2021-05-06T23:54:49+00:00'
updated_at: '2025-06-16T20:01:29+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:01:28+00:00'
---

# Original Description
XMRig/6.12.1 gcc/10.2.0 - arch linux amd64

when trying to set "idle" cpu priority using " --cpu-priority=0" i still see the mining processes being scheduled with niceness of 0 (instead of expected 19 or 20). i'd bet some of the previous versions used to work fine...

anyway, maybe unrelated - the help is also wrong:
```
--cpu-priority            set process priority (0 idle, 2 normal to 5 highest)
```
...shouldn't it be --cpu-priority=N ? now it almost looks like this option does not accept the argument.

# Discussion History
## Spudz76 | 2021-05-07T18:52:22+00:00
Unknown which way the commandline option works but likely without the `=`;

 I just change `cpu`->`prority` within the `config.json` from `null` to `0` and it works fine.

## rpodgorny | 2021-05-07T21:02:30+00:00
even with "--cpu-priority 0" it does not change the nice level in any way.

the config.json way may work but i need that to work as a command-line argument... :-(

## xmrig | 2021-05-07T21:39:59+00:00
Please show all command line options. I just checked it on Ubuntu and all works as expected: niceness of mining threads is 19 and niceness of main thread is 5.
Thank you.


## rpodgorny | 2021-05-07T23:04:20+00:00
/usr/bin/xmrig -o stratum+tcp://pool.supportxmr.com:3333 --keepalive --cpu-priority=0 --donate-level=1 -u <redacted> -p ruprt

## rpodgorny | 2021-05-07T23:04:51+00:00
```
radek@ruprt ~> /usr/bin/xmrig --version                                                                                                                         (+00:00:16) 2021-05-08 01:03:19
XMRig 6.12.1
 built on May  6 2021 with GCC 10.2.0
 features: 64-bit AES

libuv/1.41.0
OpenSSL/1.1.1k
hwloc/2.4.1```

## Spudz76 | 2021-05-08T22:07:46+00:00
non-root maybe doesn't have access to mod the niceness (it should be able to "give up" niceness but never "get more")

I never ran non-root so IDK, but it always works.

## rpodgorny | 2021-05-08T22:38:46+00:00
> non-root maybe doesn't have access to mod the niceness (it should be able to "give up" niceness but never "get more")
> 
> I never ran non-root so IDK, but it always works.

oh, sorry i didn't mention that - i AM running xmrig as root (using sudo)...

## dvershinin | 2021-05-19T10:31:00+00:00
My observations of actual niceness level with XMRig 6.12.1 and `cpu->priority` values in `config.json`:

* 0 sets the nice level to 5
* 1 sets the nice level to 0 (unchanged)
* 2 sets the nice level to -5
* 3 sets the nice level to -10
* 4 sets the nice level to -15
* 5 sets the nice level to -15 

So it does seem buggy, because:

* It does not really act in the entire range of nice levels of -20 to 19. It is only -15 to 5
* priority: 5 does not really set maximum nice level -20. 
* priority values 4 and 5 lead to the same nice level -15.

So the consequence is that if someone  sets the priority to 5 and expecting highest CPU use possible, it won't be maximum compared to simply running `nice -n -20 xmrig`

And if someone prefers the lowest CPU use by setting `priority` config to 0 and expecting "as idle as possible" it won't be, because it will be nice level 5 and not 19...

## bluexcoin | 2021-05-19T10:46:27+00:00
How can you optimize the CPU ? can gave me anyone a tipp
 "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [0, 2, 3],
        "astrobwt": [0, 1, 2, 3],
        "cn": [
            [1, 0],
            [1, 2]
        ],
        "cn-heavy": [
            [1, 0]
        ],
        "cn-lite": [
            [1, 0],
            [1, 2],
            [1, 3]
        ],
        "cn-pico": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 1],
            [2, 2],
            [2, 3]
        ],
        "rx": [0, 2],
        "rx/arq": [0, 1, 2, 3],
        "rx/wow": [0, 2, 3],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/keva": "rx/wow"
    },

## SChernykh | 2021-05-19T10:53:10+00:00
@dvershinin https://github.com/xmrig/xmrig/blob/master/src/base/kernel/Platform_unix.cpp#L106
It sets "niceness" to 19, 5, 0, -5, -10, -15 for priorities 0, 1, 2, 3, 4, 5.

## dvershinin | 2021-05-19T10:59:40+00:00
@SChernykh [not so](https://github.com/xmrig/xmrig/blob/v6.12.1/src/base/kernel/Platform_unix.cpp#L109-L127) in the current release 6.12.1.

Still, in the master branch, it's not possible to go nice level 20 or -19. I think most people prefer to go the extremes: either as idle as possible, or highest usage as possible, or without adjustment (the default).

## SChernykh | 2021-05-19T11:21:55+00:00
It is exactly the same code and it hasn't changed since February. Niceness 5 is set for priority 1, priority 0 is niceness 19.

## dvershinin | 2021-05-19T11:31:28+00:00
@SChernykh apologies then. I see.

And yet the actual nice level is like I said: 5 for priority 0.

![image](https://user-images.githubusercontent.com/250071/118805266-66982780-b8ae-11eb-8e4e-c966ee89777d.png)

![image](https://user-images.githubusercontent.com/250071/118805320-77489d80-b8ae-11eb-9d7b-25f962708987.png)

I don't have much glue how with that code it gets to 5, but it does.


## dvershinin | 2021-05-19T11:37:33+00:00
I believe it's from [here](https://github.com/xmrig/xmrig/blob/69590f9777a56cb1bcd32c39cfd1049a1c6348ad/src/core/Miner.cpp#L379). The priority is being incremented by 1 then in the `switch` statement of `setThreadPriority` function it is already 1 instead of 0? Thus ending with nice level 5.

## SChernykh | 2021-05-19T11:49:57+00:00
This is the main thread and it must have higher priority to display miner output in console without delays. Miner threads have niceness 19, use htop to check this. TLDR: not a bug.

## xmrig | 2021-05-19T11:55:43+00:00
![niceness](https://user-images.githubusercontent.com/27528955/118808492-c48b3600-b8d3-11eb-9867-f0f071c1cbfe.png)


## rpodgorny | 2021-05-19T12:31:43+00:00
could you guys please try setting the priority using command line argument? (that's what this bug is originally about)

## Spudz76 | 2021-06-01T12:04:46+00:00
With or without any `priority: null` in config.json it definitely is not working.

```
   9997 root       20   0 11368  2480  1872 S  0.0  0.0  0:00.27 │  │           └─ -bash
2049253 root       20   0 3715M 20784  7848 S 604.  0.1  2:31.95 │  │              └─ xmrig --cpu-priority=0
2049281 root       20   0 3715M 20784  7848 R 102.  0.1  0:20.10 │  │                 ├─ xmrig --cpu-priority=0
2049280 root       20   0 3715M 20784  7848 R 102.  0.1  0:20.07 │  │                 ├─ xmrig --cpu-priority=0
2049279 root       20   0 3715M 20784  7848 R 98.3  0.1  0:19.78 │  │                 ├─ xmrig --cpu-priority=0
2049278 root       20   0 3715M 20784  7848 R 101.  0.1  0:19.96 │  │                 ├─ xmrig --cpu-priority=0
2049277 root       20   0 3715M 20784  7848 R 101.  0.1  0:19.91 │  │                 ├─ xmrig --cpu-priority=0
2049276 root       20   0 3715M 20784  7848 R 97.7  0.1  0:19.69 │  │                 ├─ xmrig --cpu-priority=0
2049258 root       20   0 3715M 20784  7848 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig --cpu-priority=0
2049257 root       20   0 3715M 20784  7848 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig --cpu-priority=0
2049256 root       20   0 3715M 20784  7848 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig --cpu-priority=0
2049255 root       20   0 3715M 20784  7848 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig --cpu-priority=0
2049254 root       20   0 3715M 20784  7848 S  0.0  0.1  0:00.64 │  │                 └─ xmrig --cpu-priority=0
```

```
   9997 root       20   0 11368  2480  1872 S  0.0  0.0  0:00.27 │  │           └─ -bash
2049187 root       20   0 3715M 20668  7936 S 598.  0.1  1:04.20 │  │              └─ xmrig --cpu-priority=5
2049213 root       20   0 3715M 20668  7936 R  99.  0.1  0:05.29 │  │                 ├─ xmrig --cpu-priority=5
2049212 root       20   0 3715M 20668  7936 R 100.  0.1  0:05.31 │  │                 ├─ xmrig --cpu-priority=5
2049211 root       20   0 3715M 20668  7936 R 99.3  0.1  0:05.28 │  │                 ├─ xmrig --cpu-priority=5
2049210 root       20   0 3715M 20668  7936 R  99.  0.1  0:05.31 │  │                 ├─ xmrig --cpu-priority=5
2049209 root       20   0 3715M 20668  7936 R 99.3  0.1  0:05.30 │  │                 ├─ xmrig --cpu-priority=5
2049208 root       20   0 3715M 20668  7936 R  99.  0.1  0:05.27 │  │                 ├─ xmrig --cpu-priority=5
2049192 root       20   0 3715M 20668  7936 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig --cpu-priority=5
2049191 root       20   0 3715M 20668  7936 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig --cpu-priority=5
2049190 root       20   0 3715M 20668  7936 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig --cpu-priority=5
2049189 root       20   0 3715M 20668  7936 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig --cpu-priority=5
2049188 root       20   0 3715M 20668  7936 S  0.0  0.1  0:00.64 │  │                 └─ xmrig --cpu-priority=5
```

Zeroes all the way down...

## Spudz76 | 2021-06-01T12:07:05+00:00
However, putting `"priority": 5,` into config.json does work fine:
```
   9997 root       20   0 11368  2488  1872 S  0.0  0.0  0:00.29 │  │           └─ -bash
2049440 root        5 -15 3715M 20588  7864 S 599.  0.1  1:04.53 │  │              └─ xmrig
2049471 root        5 -15 3715M 20588  7864 R 99.7  0.1  0:05.34 │  │                 ├─ xmrig
2049470 root        5 -15 3715M 20588  7864 R 99.7  0.1  0:05.34 │  │                 ├─ xmrig
2049469 root        5 -15 3715M 20588  7864 R 99.2  0.1  0:05.30 │  │                 ├─ xmrig
2049468 root        5 -15 3715M 20588  7864 R 99.7  0.1  0:05.34 │  │                 ├─ xmrig
2049467 root        5 -15 3715M 20588  7864 R 99.7  0.1  0:05.33 │  │                 ├─ xmrig
2049466 root        5 -15 3715M 20588  7864 R 99.2  0.1  0:05.33 │  │                 ├─ xmrig
2049445 root        5 -15 3715M 20588  7864 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig
2049444 root        5 -15 3715M 20588  7864 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig
2049443 root        5 -15 3715M 20588  7864 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig
2049442 root        5 -15 3715M 20588  7864 S  0.0  0.1  0:00.00 │  │                 ├─ xmrig
2049441 root        5 -15 3715M 20588  7864 S  0.0  0.1  0:00.67 │  │                 └─ xmrig
```

## SChernykh | 2021-06-01T12:18:04+00:00
If there's a config.json, command line option might be overridden.

## xmrig | 2021-06-01T12:23:36+00:00
@Spudz76 If you use mixed configuration (config + command line), config will override the command line, because the file loaded later. For example `xmrig -c config.json --cpu-priority=0` and pure command line configuration will work as expected.
Thank you.

## Spudz76 | 2021-06-01T12:55:21+00:00
Correct.  But I removed cpu->priority from the config.json which logically would be identical to not having any config (for purposes of cpu->priority).

Also I thought command line always overrides config.json otherwise why bother?

## rpodgorny | 2021-06-05T10:29:25+00:00
well, i have cpu.priority set to null in the config file.

but anyway, command line argument should always override the config file setting - that's how tools are made since... ...forever? ;-)

## Spudz76 | 2021-06-05T23:58:45+00:00
Agree.

## xmrig | 2021-06-06T07:11:55+00:00
`xmrig -c config.json --cpu-priority=0`

## SChernykh | 2021-06-06T07:13:16+00:00
Changing current behavior will break many existing setups when they update, so it's better to keep it as is.

## rpodgorny | 2021-06-06T09:42:08+00:00
> `xmrig -c config.json --cpu-priority=0`

could you please elaborate more on what the suggested command should do? for me, the niceness level of spawned mining processes is still 0 (instead of expected 19 or 20). even with "xmrig -c /dev/null --cpu-priority=0" - something fishy is going on here... :-(

...is there a way make xmrig print out the priority it thinks user specified (so we don't have to check in htop)?

## rpodgorny | 2021-06-06T09:50:10+00:00
> Changing current behavior will break many existing setups when they update, so it's better to keep it as is.

i doubt anyone sane is depending on such behaviour (using the command line arguments but relying on config file values to overwrite those). i suspect most people just run xmrig with no arguments at all and for them nothing would break.

also, having a program behave in a non-standard way is really confusing - this very bug's existence is the evidence. and you don't know about all the "silent" people who had lost their time trying to figure this out and finally giving up with "f*ck this, i'm just putting this to config" solution... ;-)

anyway, fixing the config source precedence and  bumping the major version to indicate compatibility-breaking change is usually enough...

## menacemessage | 2021-06-06T11:44:02+00:00
Joiñ the alíbàhba app tradíñg from 8ñdía

On Sun, Jun 6, 2021, 2:42 AM Radek Podgorny ***@***.***>
wrote:

> xmrig -c config.json --cpu-priority=0
>
> could you please elaborate more on what the suggested command should do?
> for me, the niceness level of spawned mining processes is still 0 (instead
> of expected 19 or 20). even with "xmrig -c /dev/null --cpu-priority=0" -
> something fishy is going on here... :-(
>
> ...is there a way make xmrig print out the priority it thinks user
> specified (so we don't have to check in htop)?
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2351#issuecomment-855370050>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ALPNMXQUHE3GWMA3OGWLKETTRM7HZANCNFSM44IFGM3Q>
> .
>


## xmrig | 2021-06-06T12:34:56+00:00
`xmrig -c /dev/null --cpu-priority=0` This is invalid configuration because no pool is specified.

## rpodgorny | 2021-06-06T13:55:51+00:00
> `xmrig -c /dev/null --cpu-priority=0` This is invalid configuration because no pool is specified.

yes, of course - i've shortened it to keep some brevity - the full command is:

/usr/bin/xmrig -c /dev/null -o stratum+tcp://pool.supportxmr.com:3333 --keepalive --cpu-priority=0 --donate-level=1 -u XXXX -p YYYY

## xmrig | 2021-06-06T13:56:41+00:00
Anyway mixed configuration e.g. multiple config files, config AND command line which also transformed to config file is just a bonus of the internal config load chain. This is not the main use case, it has limitations and not all possible configurations checked. If you for some reason do not use pure configuration (command line OR single config file) you must understand this.
Thank you.

## xmrig | 2021-06-06T13:58:10+00:00
`/usr/bin/xmrig -c /dev/null -o stratum+tcp://pool.supportxmr.com:3333 --keepalive --cpu-priority=0 --donate-level=1 -u XXXX -p YYYY`
But it should work in any case, `-c /dev/null` not required.

## Spudz76 | 2021-06-06T16:34:42+00:00
My use case is to just never, ever use commandline anything and only design correct config.json files.

But that was born of the commandline stuff not really working correctly and wasting my time.

## menacemessage | 2021-06-06T17:21:36+00:00
Hi beautiful 😘

On Sun, Jun 6, 2021, 9:34 AM Tony Butler ***@***.***> wrote:

> My use case is to just never, ever use commandline anything and only
> design correct config.json files
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2351#issuecomment-855425855>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ALPNMXUEBMOSUF7EW6MXKBTTROPS3ANCNFSM44IFGM3Q>
> .
>


## Evi5 | 2022-04-08T06:28:58+00:00
The parameter "--cpu-priorit=0" when running from the command line or bat file, must be specified at the end
For Example:
sudo xmrig --coin keva --randomx-1gb-pages --donate-level 1 -o kevacoin.miningocean.org:7332 -u address.name -k --cpu-priority=0

## rpodgorny | 2022-04-08T08:52:29+00:00
> The parameter "--cpu-priorit=0" when running from the command line or bat file, must be specified at the end For Example: sudo xmrig --coin keva --randomx-1gb-pages --donate-level 1 -o kevacoin.miningocean.org:7332 -u address.name -k --cpu-priority=0

confirming putting --cpu-priority as the last option works. thanks @Evi5 ! ...but still, this is completely counterintuitive, undocumented and ridiculous... :-(

## Spudz76 | 2022-04-08T10:41:41+00:00
> ...but still, this is completely counterintuitive, undocumented and ridiculous... :-(

Agree but it's an odd bug and very unclear why it has to be last, the argument processing isn't built to force that, more of a side effect that hasn't been found yet.

## snipeTR | 2022-04-08T11:21:47+00:00
Start "" /low cmd /c xmrig.exe
https://ss64.com/nt/start.html

## SChernykh | 2022-04-19T17:58:32+00:00
> > ...but still, this is completely counterintuitive, undocumented and ridiculous... :-(
> 
> Agree but it's an odd bug and very unclear why it has to be last, the argument processing isn't built to force that, more of a side effect that hasn't been found yet.

Fixed it in https://github.com/xmrig/xmrig/pull/3031

# Action History
- Created by: rpodgorny | 2021-05-06T23:54:49+00:00
- Closed at: 2025-06-16T20:01:28+00:00
