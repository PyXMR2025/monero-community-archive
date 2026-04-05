---
title: Please resolve my issue
source_url: https://github.com/xmrig/xmrig/issues/3286
author: arsalan123ahmed
assignees: []
labels: []
created_at: '2023-06-14T09:32:06+00:00'
updated_at: '2025-06-18T22:40:54+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:40:54+00:00'
---

# Original Description
**Describe the bug**
A clear and concise description of what the bug is.
I am using xmrig on termux android
**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**~/xmrig $ ./xmrig -o xmr-asia1.nanopool.org:14433 -u 48pU3UieC8pEqHhwven7ekjcvakHsCaYmYcSQk3MnNKc78yF4BV8VMnZ3sj3fFwtUFbwPi15gyMwMcmkuSWyHQr3MNbdnBy --tls --coin monero
 * ABOUT        XMRig/6.19.3 clang/16.0.5
 * LIBS         libuv/1.45.0 OpenSSL/3.1.1
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          ARM Cortex-A53 (1) 32-bit -AES
                threads:4
 * MEMORY       1.1/1.8 GB (59%)
 * DONATE       1%
 * POOL #1      xmr-asia1.nanopool.org:14433 coin Monero
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2023-06-14 14:03:38.598]  net      use pool xmr-asia1.nanopool.org:14433 TLSv1.3 139.99.101.198
[2023-06-14 14:03:38.600]  net      fingerprint (SHA-256): "c38886efdee542ebd99801b75c75d3498d97978bbcdec07c7271cb19729e014f"
[2023-06-14 14:03:38.600]  net      new job from xmr-asia1.nanopool.org:14433 diff 480045 algo rx/0 height 2907821 (53 tx)
[2023-06-14 14:03:38.601]  cpu      use argon2 implementation default
[2023-06-14 14:03:39.808]  randomx  init dataset algo rx/0 (4 threads) seed a18b4e4ddc9dbb74...
[2023-06-14 14:03:39.808]  randomx  not enough memory for RandomX dataset
[2023-06-14 14:03:39.809]  randomx  failed to allocate RandomX dataset, switching to slow mode (1 ms)
[2023-06-14 14:03:44.944]  net      new job from xmr-asia1.nanopool.org:14433 diff 480045 algo rx/0 height 2907821 (56 tx)
[2023-06-14 14:03:46.492]  randomx  dataset ready (6684 ms)
[2023-06-14 14:03:46.493]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
[2023-06-14 14:03:46.494]  cpu      READY threads 4/4 (4) huge pages 0% 0/4 memory 8192 KB (2 ms)
[2023-06-14 14:03:50.577]  net      new job from xmr-asia1.nanopool.org:14433 diff 480045 algo rx/0 height 2907822 (1 tx)
A clear and concise description of what you expected to happen.

**Required data**
 - Miner log as text or screenshot
![Screenshot_20230614-140715](https://github.com/xmrig/xmrig/assets/53614483/8e0b10bf-37b4-4e70-aa6e-2ae992a71137)
![Screenshot_20230614-140738](https://github.com/xmrig/xmrig/assets/53614483/4482b3ee-ed6d-46da-b0e7-f6dce4a72bbc)

 - For GPU related issues: information about GPUs and driver version.

**Additional context**
Add any other context about the problem here.
My mining start but not mining in wallet
I have tried so many time but I can't understand what is my issue


# Discussion History
## SChernykh | 2023-06-14T09:47:13+00:00
Your phone has less than 2 GB memory, so it will be using slow mode for RandomX (fast mode requires more than 2 GB). Also XMRig is compiled as 32-bit binary, which is an additional 10 times slowdown. You should recompile it for 64-bit, but even if you do it, you will have 20 h/s at best which is not enough to mine anything. This phone is just too weak for RandomX mining.

## arsalan123ahmed | 2023-06-14T10:17:50+00:00
Thanks for your reply I have 32 bit PC and another 2gb mobile I will try on
other device hope they will work fine

On Wed, Jun 14, 2023, 2:47 PM SChernykh ***@***.***> wrote:

> Your phone has less than 2 GB memory, so it will be using slow mode for
> RandomX (fast mode requires more than 2 GB). Also XMRig is compiled as
> 32-bit binary, which is an additional 10 times slowdown. You should
> recompile it for 64-bit, but even if you do it, you will have 20 h/s at
> best which is not enough to mine anything. This phone is just too weak for
> RandomX mining.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/3286#issuecomment-1590862958>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AMZBPE5KH7MGGHGFTPBIAQ3XLGCC3ANCNFSM6AAAAAAZGCI7WY>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


# Action History
- Created by: arsalan123ahmed | 2023-06-14T09:32:06+00:00
- Closed at: 2025-06-18T22:40:54+00:00
