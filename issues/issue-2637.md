---
title: 'Ryzen 5900x: MSR apparently crashes the PC; having it off doesn''t seem to
  lower the hashrate'
source_url: https://github.com/xmrig/xmrig/issues/2637
author: hauzer
assignees: []
labels: []
created_at: '2021-10-19T05:17:14+00:00'
updated_at: '2021-10-19T20:33:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Setup**
*OS: Windows 10
CPU: Ryzen 5900x
MB: GA B550M
xmrig version: 6.15.2*

**Description**
Simply put, running xmrig with MSR enabled (as an admin) crashes the whole PC (unresponsive black screen) after a couple of minutes. Running it as a regular user is stable. Either way, the hashrate seems to hover around 12-13k, with a couple of jumps as high as 16k. No huge differences, but this is up for debate and dispute, of course. I haven't exactly run tight measurements.

Fully updated drivers, BIOS, and Windows. Stock BIOS settings, absolutely zero OC. No previous BSOD/crash incidents whatsoever. Stress-tested both memory and CPU for several hours each; perfectly stable.

I haven't tried the `wrmsr` config from [here](https://xmrig.com/docs/miner/randomx-optimization-guide/msr) yet, but I'm under the impression that it's automatically used when the relevant CPU is detected.

Tried searching for a solution, but found only tangentially relevant information. Any ideas?

**Config**
```
{
    "autosave": true,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "...",
            "user": "...",
            "keepalive": true,
            "tls": true
        }
    ]
}
```

**Command line**
`xmrig.exe -o ... -u ... -k --tls`

# Discussion History
## Spudz76 | 2021-10-19T09:40:37+00:00
Find `"verbose"` in config and set `true` then it says a little bit more at the MSR step (exactly which values it's trying).

`"rdmsr"` and `"wrmsr"` should just be `true`

## hauzer | 2021-10-19T17:17:50+00:00
It's `ryzen_19h`, as it should be.

`[2021-10-19 19:06:26.591]  msr      register values for "ryzen_19h" preset have been set successfully (447 ms)`

Not sure where's the defect here. I've run xmrig *without* MSR at 100% CPU for 8 hours, unattended, and the instant I started opening and using other programs, I got a crash. Oh well, probably not your problem.

Feel free to close the issue.

## Spudz76 | 2021-10-19T20:33:58+00:00
Was at a loss for how the MSRs would even cause such a thing.  Could be flaky power considering you've tested the memory itself a bunch of times.

# Action History
- Created by: hauzer | 2021-10-19T05:17:14+00:00
