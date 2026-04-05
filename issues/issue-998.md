---
title: 'Please add Conceal (CCX) correct support '
source_url: https://github.com/xmrig/xmrig/issues/998
author: Dr-Hard
assignees: []
labels:
- algo
- conceal
created_at: '2019-03-19T15:43:36+00:00'
updated_at: '2020-06-21T10:37:25+00:00'
type: issue
status: closed
closed_at: '2020-06-08T19:11:32+00:00'
---

# Original Description
Please add correct support cn (cn/r) "conceal" algo for CCX new fork to xmrig, xmrig-amd & xmrig proxy.

# Discussion History
## gr8form | 2019-03-19T19:57:10+00:00
I second this request!  The conceal team had an amazingly smooth fork, very responsive/accessible devs and really have a unique product contribution.  Would also request addition of xmrig-nvidia.  Thank you!

## Dr-Hard | 2019-05-10T03:37:40+00:00
Please add correct support cn (cn/r) "conceal" algo for CCX new fork to xmrig, xmrig-amd & xmrig proxy. Conceal dev group given you all info for it.

## Dr-Hard | 2019-08-10T18:28:50+00:00
Please add correct and WORKING support cn (cn/r) "conceal" algo for CCX new fork to xmrig, xmrig-amd & xmrig proxy. Conceal dev group given you all info for it.

## UnclWish | 2019-08-20T13:13:09+00:00
Connect to request. Miner needs Conceal CCX support (cn/conceal)

## krypt0x | 2019-11-11T23:01:50+00:00
inline __m128 _mm_set1_ps_epi32(uint32_t x)
{
	return _mm_castsi128_ps(_mm_set1_epi32(x));
}

inline void cryptonight_conceal_tweak(__m128i& cx, __m128& conc_var)
{
	__m128 r = _mm_cvtepi32_ps(cx);
	__m128 c_old = conc_var;
	r = _mm_add_ps(r, conc_var);
	r = _mm_mul_ps(r, _mm_mul_ps(r, r));
	r = _mm_and_ps(_mm_set1_ps_epi32(0x807FFFFF), r);
	r = _mm_or_ps(_mm_set1_ps_epi32(0x40000000), r);
	conc_var = _mm_add_ps(conc_var, r);

	c_old = _mm_and_ps(_mm_set1_ps_epi32(0x807FFFFF), c_old);
	c_old = _mm_or_ps(_mm_set1_ps_epi32(0x40000000), c_old);
	__m128 nc = _mm_mul_ps(c_old, _mm_set1_ps(536870880.0f));
	cx = _mm_xor_si128(cx, _mm_cvttps_epi32(nc));
}

## krypt0x | 2019-11-11T23:02:18+00:00
https://github.com/ConcealNetwork/conceal-xmrig/commit/5160534cf143ab3b17983b8418476e8617147b0c

## aefefgrg | 2019-11-12T05:12:26+00:00
Mİners need this support.

## TheDevMinerTV | 2019-11-12T05:47:39+00:00
+1 from me! 

## system-overflow | 2019-11-12T10:19:55+00:00
CN_Conceal is missing!!! Please add the most energy efficient CN algo out there. I can send you some $CCX mate. Should we raise a bounty on CCX Discord?

## system-overflow | 2019-11-12T10:20:50+00:00
> inline __m128 _mm_set1_ps_epi32(uint32_t x)
> {
> return _mm_castsi128_ps(_mm_set1_epi32(x));
> }
> 
> inline void cryptonight_conceal_tweak(__m128i& cx, __m128& conc_var)
> {
> __m128 r = _mm_cvtepi32_ps(cx);
> __m128 c_old = conc_var;
> r = _mm_add_ps(r, conc_var);
> r = _mm_mul_ps(r, _mm_mul_ps(r, r));
> r = _mm_and_ps(_mm_set1_ps_epi32(0x807FFFFF), r);
> r = _mm_or_ps(_mm_set1_ps_epi32(0x40000000), r);
> conc_var = _mm_add_ps(conc_var, r);
> 
> ```
> c_old = _mm_and_ps(_mm_set1_ps_epi32(0x807FFFFF), c_old);
> c_old = _mm_or_ps(_mm_set1_ps_epi32(0x40000000), c_old);
> __m128 nc = _mm_mul_ps(c_old, _mm_set1_ps(536870880.0f));
> cx = _mm_xor_si128(cx, _mm_cvttps_epi32(nc));
> ```
> 
> }

It looks good mate

## TheHungryRaccoon | 2019-11-12T11:36:25+00:00
How come no CN_Conceal? Please add this algo.

https://medium.com/@ConcealNetwork/new-cn-conceal-pow-algorithm-f68e2159cab0

https://miningpoolstats.stream/conceal

https://www.cryptunit.com/coin/CCX

## realityworks | 2019-11-12T11:53:39+00:00
I could add this in the fork. What's the job? Happy to take Monero as payment.

## system-overflow | 2019-11-12T12:08:09+00:00
> I could add this in the fork. What's the job? Happy to take Monero as payment.

The bounty is to integrate CPU & GPU support on xmrig for CN_Conceal. It would be better to contact the CCX team on their Discord. I am just an user... Thanks

http://discord.conceal.network

## okanist | 2019-11-12T12:08:39+00:00
Conceal algo is one of the most popular one, please add this algo as well. Miners have been asking for it for a long time. They deserve it!

## SChernykh | 2019-11-12T12:34:54+00:00
XMRig's main purpose is Monero mining, so we're concentrated on RandomX (and its variants) support now. Adding new Cryptonight variant is not that easy, don't forget there is also GPU code both for AMD and NVIDIA. But if someone creates a PR here, it can be merged.

## realityworks | 2019-11-12T12:39:32+00:00
> XMRig's main purpose is Monero mining, so we're concentrated on RandomX (and its variants) support now. Adding new Cryptonight variant is not that easy, don't forget there is also GPU code both for AMD and NVIDIA. But if someone creates a PR here, it can be merged.

@SChernykh I'm talking with the CN team at the moment to confirm the change in an update on my fork. Need to review the workload and see what I can contribute to the community time wise.

## system-overflow | 2019-11-12T12:50:39+00:00
> XMRig's main purpose is Monero mining, so we're concentrated on RandomX (and its variants) support now. Adding new Cryptonight variant is not that easy, don't forget there is also GPU code both for AMD and NVIDIA. But if someone creates a PR here, it can be merged.

CCX community has the biggest heart. CCX support will be sorted out but you are depreciating all the GPU miners that have supported you all these years. I can't mine XMR with my GPU rigs, period. :thinking: 

## TheHungryRaccoon | 2019-11-12T12:52:31+00:00
> XMRig's main purpose is Monero mining, so we're concentrated on RandomX (and its variants) support now. Adding new Cryptonight variant is not that easy, don't forget there is also GPU code both for AMD and NVIDIA. But if someone creates a PR here, it can be merged.

No worries. We came here for respect to the authors. IT's good to know you will merge the CCX support PR. Thanks.

## system-overflow | 2019-11-13T16:03:56+00:00
> > XMRig's main purpose is Monero mining, so we're concentrated on RandomX (and its variants) support now. Adding new Cryptonight variant is not that easy, don't forget there is also GPU code both for AMD and NVIDIA. But if someone creates a PR here, it can be merged.
> 
> @SChernykh I'm talking with the CN team at the moment to confirm the change in an update on my fork. Need to review the workload and see what I can contribute to the community time wise.

Fantastic!

## vasssek | 2019-12-02T10:13:34+00:00
Hi, is there intention to add CCX algo ?

## krypt0x | 2020-06-05T10:21:05+00:00
@xmrig we need your help with this. Thanks

## LithyRiolu | 2020-06-05T10:37:28+00:00
+1 for the support of this hashing algorithm!

## ChrisfromNM | 2020-06-06T00:23:14+00:00
Mİners need this support.  @xmrig we need your help with this. Thanks

## SChernykh | 2020-06-07T07:16:47+00:00
It will be added in the next release.
https://github.com/xmrig/xmrig/pull/1717
https://github.com/xmrig/xmrig-cuda/pull/52

## BKdilse | 2020-06-07T18:21:18+00:00
@SChernykh for Cuda only, or OpenCL too?

## SChernykh | 2020-06-07T18:26:45+00:00
For everything, even ARM CPUs.

## BKdilse | 2020-06-07T18:48:52+00:00
> For everything, even ARM CPUs.

Brilliant thanks

## xmrig | 2020-06-08T19:11:32+00:00
[v6.2.0](https://github.com/xmrig/xmrig/releases/tag/v6.2.0-beta) with Conceal support just released.
Thank you.

## krypt0x | 2020-06-21T10:37:25+00:00
Flawless. Great job! Thank you.

# Action History
- Created by: Dr-Hard | 2019-03-19T15:43:36+00:00
- Closed at: 2020-06-08T19:11:32+00:00
