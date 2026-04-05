---
title: Building in OpenCL configuration on IBM POWER (ppc64el)
source_url: https://github.com/xmrig/xmrig/issues/3478
author: tucnak
assignees: []
labels: []
created_at: '2024-05-13T08:59:06+00:00'
updated_at: '2025-06-18T22:14:39+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:14:39+00:00'
---

# Original Description
I have finally managed to put AMD Instinct card to work with the latest ROCm on my IBM POWER9 server.

I have also been trying to build xmrig with opencl support, however it seems that even the "portable" code isn't exactly portable? x86intrin all the way, I had replaced with altivec occasionally, but CN/soft_aes code is just completely impenetrable. To be honest, I don't even see a reason why any of this needs to be built given OpenCL target, however maybe I would have better luck with CUDA code?

AMD HIP is actually pretty compatible with CUDA, there's hipify tool to convert pre-existing code to HIP and run that on AMD GPU. Unfortunately, I imagine that CUDA code would similarly depend on cryptonight/soft_aes stuff a.k.a. CPU vectorisations, so I'm back to square 1 in that regard. Really hope to somehow get this working, as it would be really cool. Related #2227

# Discussion History
## SChernykh | 2024-05-13T12:26:34+00:00
XMRig supports x64 and ARMv8 code only. AES is a part of RandomX, and XMRig uses CPU code to verify hashes found by GPU.

# Action History
- Created by: tucnak | 2024-05-13T08:59:06+00:00
- Closed at: 2025-06-18T22:14:39+00:00
