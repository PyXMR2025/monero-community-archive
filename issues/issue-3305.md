---
title: '*** buffer overflow detected ***: terminated on recent NixOS'
source_url: https://github.com/xmrig/xmrig/issues/3305
author: '0x241F31'
assignees: []
labels:
- bug
created_at: '2023-07-19T21:23:44+00:00'
updated_at: '2024-03-20T21:18:33+00:00'
type: issue
status: closed
closed_at: '2023-08-24T17:38:19+00:00'
---

# Original Description
**Describe the bug**
In NixOS after recent update I'm getting error on rx/0 algo. However, kawpow with CUDA. works fine
Trace: https://paste.mozilla.org/aSMka3oZ

**To Reproduce**
My NixOS configuration:
``` nix
systemd.services.xmrig-rx =
  mkXmrig
  {
    pools = [
      {
        enabled = true;
        url = "127.0.0.1:3333";
        user = "huanazhi";
        keepalive = true;
        tls = false;
      }
      {
        enabled = true;
        url = "gulf.moneroocean.stream:10128";
        user = moneroWallet;
        algo = "rx/0";
        pass = "<>";
        keepalive = false; # Mandatory for moneroocean
        tls = false;
      }
    ];
    randomx."1gb-pages" = true;
    cpu.huge-pages = true;
    cpu.yield = false;
    cpu.priority = 4;
  }
  {after = ["p2pool.service"];};
```

**Required data**
![image](https://github.com/xmrig/xmrig/assets/17229619/ba3a3ca8-3993-4ddc-a87d-05935096bc51)
`Linux huananzhi 6.1.38 #1-NixOS SMP PREEMPT_DYNAMIC Wed Jul  5 17:27:38 UTC 2023 x86_64 GNU/Linux`
NixOS

**Additional context**
Add any other context about the problem here.
It was working before.
I tried both 6.19.4 and 6.20.0, none worked

# Discussion History
## SChernykh | 2023-07-20T08:15:36+00:00
I tried to compile XMRig using GCC 11 and GCC 13 with `-D_FORTIFY_SOURCE=2 -fstack-protector` but I couldn't reproduce it.

## 0x241F31 | 2023-07-21T12:37:50+00:00
> I tried to compile XMRig using GCC 11 and GCC 13 with `-D_FORTIFY_SOURCE=2 -fstack-protector` but I couldn't reproduce it.

Any ideas about trace?

## 0x241F31 | 2023-07-21T20:07:32+00:00
@ratsclub @kim0

## ghost | 2023-07-24T04:26:30+00:00
I am hitting the same thing, but using xmrig-mo , also on nixOS

## Spudz76 | 2023-07-24T15:30:33+00:00
```
#4 0x00007f0b3dc51679 __fortify_fail (libc.so.6 + 0x117679)
#5 0x00007f0b3dc4fea4 __chk_fail (libc.so.6 + 0x115ea4)
```

Seems like that's where things go wrong.  NixOS so hardened you can't do anything.  Figure out how to loosen it for xmrig.

Edit: probably thinks something wanting to use 3.5GB of memory is a hack

Edit2: try setting env before compile:
```
export hardeningDisable=all
export NIX_HARDENING_ENABLE=""
```

Also you can see all the added flags it is trying to use with:
```
NIX_DEBUG=true gcc
NIX_DEBUG=true g++
```

If all you are doing is mining just use Ubuntu and save everyone on Earth the pain of a hardened distro (for no reason, on an inaccessible LAN, etc)

## Spudz76 | 2023-07-24T15:48:44+00:00
Also since it's a NixOS problem, and if you are using their package, try asking them why it sucks.

https://github.com/NixOS/nixpkgs/issues?q=xmrig

## ratsclub | 2023-07-24T20:49:36+00:00
I approved the new version there, ping me if this doesn't fix the issue.

## AndersonTorres | 2023-08-23T21:35:31+00:00
> try asking them why it sucks.

Because it is sadistically funny to make people lose their minds about "smashing the stack for fun and profit".

Our sincere apologies for the excessive paranoia.



## ratsclub | 2023-08-24T13:16:38+00:00
@MrFoxPro, may you or a maintainer close this issue, please? It was solved downstream.

## xmrig | 2024-03-20T21:18:32+00:00
This issue solved in dev branch #3450 without disabling fortify hardening.
Thank you.

# Action History
- Created by: 0x241F31 | 2023-07-19T21:23:44+00:00
- Closed at: 2023-08-24T17:38:19+00:00
