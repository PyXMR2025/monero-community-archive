---
title: seg fault when using opencl for cn/r algo
source_url: https://github.com/xmrig/xmrig/issues/2397
author: brianmcfadden
assignees: []
labels: []
created_at: '2021-05-20T17:09:04+00:00'
updated_at: '2021-05-22T23:08:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
Using opencl with AMD card, and using cryptonight/r algo, I see this:

[2021-05-20 12:28:55.973]  opencl   GPU #1 compiling...
[2021-05-20 12:28:55.986]  opencl   GPU #1 compilation completed (12 ms)
[2021-05-20 12:28:55.987]  opencl   READY threads 2/2 (137 ms)
Segmentation fault: 11

**To Reproduce**
1. Turn opencl on in the config, setting "enabled" to "true" in the opencl block of config.json
2. Modify the config to have "algo": "cn/r"
3. Set the URL to somewhere that uses cn/r.  My config,json has -- "url": "pool.xmc.fairhash.org:3333"
4. start xmrig


**Expected behavior**
Mining would begin

**Required data**
OS: Mac OS Catalina
GPU: AMD Radeon Pro 455 Compute Engine

**Additional context**

Note that this only happens for OpenCL.

The problem seems to be in src/backend/opencl/runners/OclCnRunner.cpp.  During the build() function, we create m_cn0 and m_cn2, but if and only if the algo is CN/R, we avoid creating m_cn1.  Then, when it comes time to run(), we call m_cn0->enqueue(), then m_cn_1-<enqueue(), then m_cn2, but the call to m_cn1 fails because cn_1 isn't created during build().  

I don't know if the fix would be to create the m_cn1 during build(), or to avoid using m_cn1 during run() when algo==cn/r.


# Discussion History
## Spudz76 | 2021-05-20T23:00:10+00:00
I have been working on Apple OpenCL fixes, part of the issue is when the GPU has AMD in the name it assumes it's full-stack AMD.  But with AppleCL none of the custom AMD things (`cl_amd_*` extensions, raw GCN assembly, maybe other quirks) work at all, and other "sloptimized" things the AMD stack ignores, Apple will not tolerate.  I have been testing against nvidia's OpenCL stack since it also didn't work well (and doesn't need to thanks to CUDA however it is a good non-AMD OpenCL to find crashes with, that likely apply to AppleCL or even Intel OpenCL which also is rickety).  I don't have any OSX with GPUs to actually test repeatedly in a tight hack-check-hack-check loop.

There is another thread #2345 about kawpow failure which turned into more of a generic AppleCL debugging festival, there are some links to whatever my current test branch is over there.  Would be nice to have another test participant.

## brianmcfadden | 2021-05-22T21:33:10+00:00
Sure, I'll take a look at that thread... I can do a checkout of
Spudz76-dev-fixCLKawPowPlatformHandling and test.  I'll get back to you in
that issue.

On Thu, May 20, 2021 at 7:00 PM Tony Butler ***@***.***>
wrote:

> I have been working on Apple OpenCL fixes, part of the issue is when the
> GPU has AMD in the name it assumes it's full-stack AMD. But with AppleCL
> none of the custom AMD things (cl_amd_* extensions, raw GCN assembly,
> maybe other quirks) work at all, and other "sloptimized" things the AMD
> stack ignores, Apple will not tolerate. I have been testing against
> nvidia's OpenCL stack since it also didn't work well (and doesn't need to
> thanks to CUDA however it is a good non-AMD OpenCL to find crashes with,
> that likely apply to AppleCL or even Intel OpenCL which also is rickety). I
> don't have any OSX with GPUs to actually test repeatedly in a tight
> hack-check-hack-check loop.
>
> There is another thread #2345 <https://github.com/xmrig/xmrig/issues/2345>
> about kawpow failure which turned into more of a generic AppleCL debugging
> festival, there are some links to whatever my current test branch is over
> there. Would be nice to have another test participant.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/2397#issuecomment-845536021>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAOC7YQINLTQCV2Y3URZZYTTOWIAZANCNFSM45HOUMDA>
> .
>


## Spudz76 | 2021-05-22T23:08:38+00:00
Nah that one is already included into `dev` branch

Use the `dev-fixAppleOpenCL` that is where the work has been happening.

# Action History
- Created by: brianmcfadden | 2021-05-20T17:09:04+00:00
