---
title: '[Write-up, Discussion] Cryptonight-GPU — FPGA-proof PoW algorithm based on
  floating point instructions'
source_url: https://github.com/monero-project/monero/issues/5152
author: fireice-uk
assignees: []
labels: []
created_at: '2019-02-16T17:25:02+00:00'
updated_at: '2019-04-25T10:18:42+00:00'
type: issue
status: closed
closed_at: '2019-02-18T09:48:12+00:00'
---

# Original Description
https://medium.com/@crypto_ryo/cryptonight-gpu-fpga-proof-pow-algorithm-based-on-floating-point-instructions-92524debf8e8

# Discussion History
## SamsungGalaxyPlayer | 2019-02-16T18:17:39+00:00
I had hoped this would actually include some documentation on Cryptonight-GPU. Instead, this is just someone ranting without understanding why documentation is necessary. Seriously, this is their response to the Monero community indicating that it would only consider solutions with even a small amount of documentation:

> I’m always happy to help people that might have trouble reviewing the source code, so here we are =). Overall, it turned out that the power usage is on par with MoneroV8.

...that's it.

This angry rant has no place here. @fireice-uk, if you want people to take you seriously, do an actual writeup on Cryptonight-GPU's design.

## moneromooo-monero | 2019-02-16T18:39:32+00:00
What's the bug/report ? The link indeed seems like an unrelated rant, I didn't go through it. Please elaborate (or just paste the relevant part if appropriate).


## fireice-uk | 2019-02-16T19:30:32+00:00
> This angry rant has no place here. @fireice-uk, if you want people to take you seriously, do an actual writeup on Cryptonight-GPU's design.

You somehow missed half of the article.

> What's the bug/report ? The link indeed seems like an unrelated rant, I didn't go through it. Please elaborate (or just paste the relevant part if appropriate).

A writeup regarding cn-gpu design (more accurately a write-up of why it works, as the design is KISS - "a bunch of 32bit fp ops") has been requested, I deliver.

## SamsungGalaxyPlayer | 2019-02-16T19:47:36+00:00
Thanks @fireice-uk. Would you mind closing this issue then and opening up a new one when you're ready? I'd hate for the discussion to get started on the wrong foot.

## fireice-uk | 2019-02-16T19:54:09+00:00
Why do you think I'm not ready?

## moneromooo-monero | 2019-02-16T20:08:49+00:00
OK, so you're proposing a new PoW basically. I'll read this when I get a moment.


## fireice-uk | 2019-02-16T20:31:23+00:00
> OK, so you're proposing a new PoW basically. I'll read this when I get a moment.

Yes, this is something we already implemented - it does ASIC resistance differently. Not by implementing a fancy feature and hoping it won't be replicated, but instead by anchoring performance to physical number of FP cores.

## SamsungGalaxyPlayer | 2019-02-16T20:33:13+00:00
@fireice-uk it would be helpful for us to begin looking at more than just the code. See the [RandomX documentation](https://github.com/tevador/RandomX/tree/master/doc) as an example of what I'm looking for. It can be simpler than this as long as it gets the point across and is comprehensible.

## fireice-uk | 2019-02-16T20:53:21+00:00
> A bunch of 32 bit FP ops

It is really that simple @SamsungGalaxyPlayer You can do amazing things if you don't do design-by-committee.

## tevador | 2019-02-17T11:18:38+00:00
> A bunch of 32 bit FP ops

It's not that simple. I'll give you some examples of what a detailed write-up should answer:

1. Which floating point operations are used?
1. How do you avoid NaN, which has implementation-defined binary representation?
1. How do you preserve high entropy of the outputs?
1. Is the range of your floating point results large enough to prevent much cheaper fixed-point implementations? 
1. Do you avoid denormal results, which can degrade performance? 
1. Which rounding modes do you use? 
1. Which platforms the algorithm has been tested on?
1. Is the algorithm severely compute-bound or does it only use floating ops to avoid compute stalls in the Cryptonight loop?
1. Why is being "FPGA-proof" a desirable feature?

## fireice-uk | 2019-02-17T12:18:55+00:00
Thanks, some pointful questions at last =]

> Which floating point operations are used?

Addition, subtraction, multiplication, division

> How do you avoid NaN, which has implementation-defined binary representation?

Careful management of range on multiplication and making sure that ABS(divisor) > 2

> How do you preserve high entropy of the outputs?

XOR the answer with the scratchpad, that operation does not change entropy (you can xor a random number with 0 infinitely many times and still have a random number).

> Is the range of your floating point results large enough to prevent much cheaper fixed-point implementations?

Yes, you would need 96 bit integers.

> Do you avoid denormal results, which can degrade performance?

Actually, denormals will ruin the output too since their handling is not mandated by the standard. We found it out the hard way - https://github.com/ryo-currency/ryo-currency/pull/167

> Which rounding modes do you use?

RTN

> Which platforms the algorithm has been tested on?

Intel SSE2, Intel AVX, ARM7, ARM8, AMD, NVIDIA

> Is the algorithm severely compute-bound or does it only use floating ops to avoid compute stalls in the Cryptonight loop?

It is compute bound, with linear relationship between hashrate and TFLOPS (multiplier is around 125)

> Why is being "FPGA-proof" a desirable feature?

For the same reason ASIC-proof.

## tevador | 2019-02-17T13:50:05+00:00
> Actually, denormals will ruin the output too since their handling is not mandated by the standard. We found it out the hard way

Denormal support is actually mandated by the IEEE 754 standard, but not by OpenCL, so GPU manufacturers can cut corners there. Denormals are fully supported by CPUs, just very slow because they are usually handled in microcode.

Overall I think this PoW is not bad except for two problems:

* Purely compute bound algorithm means an ASIC can have a significant efficiency advantage.
* Slow verification on CPUs - if the 100 ms figure from the issue you linked is still true.

## fireice-uk | 2019-02-17T15:14:02+00:00
>  Purely compute bound algorithm means an ASIC can have a significant efficiency advantage.

Are you thinking of SHA256? That's apples and oranges, since sha256 is a series of simple binary operations (not even maths), mostly AND/OR/XOR shifts and transpositions, sprinkled with some additions. All that is easily pipelined.

In contrast for FP cores, the limiting factor is more about the number of cores. 

> Slow verification on CPUs - if the 100 ms figure from the issue you linked is still true.

Yes, that actually is the biggest limiting factor for this algo - but eventually we will want to do something asymmetric. 

## SChernykh | 2019-02-17T15:28:58+00:00
@fireice-uk 
> Addition, subtraction, multiplication, division

Division is not supported natively on GPU, it compiles to a long sequence of instructions (reciprocal, multiplication and some more fixup). ASIC can be 2-3 times faster here.

## tevador | 2019-02-17T16:19:18+00:00
@fireice-uk 

> AND/OR/XOR shifts and transpositions, sprinkled with some additions. All that is easily pipelined

Floating point math can be done entirely using the operations you listed. It's not some silver bullet that ASICs cannot parallelize. Additionally, an ASIC can optimize a lot of the operations since the algorithm never produces NaN, infinity or denormals, which compliant FP cores have to check for.

A fully pipelined ASIC will have just one stage per operation and will be limited only by the amount of memory for scratchpads.

## SChernykh | 2019-02-17T16:37:17+00:00
Adding to what @tevador said: ASIC won't have to check for all edge case because cn-gpu conveniently removed them. It has to implement only one rounding mode and only 4 basic FP operations. The code is fixed, so while GPU has to have full IEEE-754 FP cores, instruction decoders, schedulers, caches on chip, ASIC can get rid of all this. It'll hard-wire the whole inner loop and optimize the layout, so I won't be surprised if it can reach 12.5 TFLOPS with a chip 4-5 times smaller than Vega 64, so it'll be 4-5 times _cheaper_ to produce.

Second problem: 2 MB scratchpad. GPU spend a lot of energy transferring data to memory and back. ASIC will use on-chip SRAM and be overall 10-20 times more efficient per watt than GPU.

## fireice-uk | 2019-02-17T18:20:56+00:00
>  It's not some silver bullet that ASICs cannot parallelize.

I think you are still thinking of FP as a "no hands" feature, it isn't. I will refer you to "Can FPGAs do floating point instructions?". 

> Floating point math can be done entirely using the operations you listed.

All computer operations can be reduced to a series on NAND gates. In the same way, a person is a collection of carbon atoms. Drawing equivalence between behaviour of a person and a wet sack of charcoal is not an intellectually honest argument. I will give you the benefit of doubt and say you came up with that due to peer pressure rather than deliberate bamboozling. 

> It has to implement only one rounding mode and only 4 basic FP operations.

Not reading the source again, I see, no there are two rounding modes there, see if you can find them. I will assume that didn't know that sqrt is implemented using microcodes and not hardware. You are shooting yourself in the foot by including it as you just penalised CPUs/GPUs (again, you need to think in terms of performance and not "no hands" features).

> It'll hard-wire the whole inner loop and optimize the layout, so I won't be surprised if it can reach 12.5 TFLOPS with a chip 4-5 times smaller than Vega 64, so it'll be 4-5 times _cheaper_ to produce.

I will refer you to this paragraph from the write-up

> Can you take a GPU core and strip out everything except FP cores? Sure. But then you have to ask yourself, how much can you strip out? 20% 50% 75%? Assuming the latter, who is going to buy an $6000 ASIC that only does 4x the hashrate of a $500 Vega 64?


## SChernykh | 2019-02-17T18:27:40+00:00
> Not reading the source again, I see, no there are two rounding modes there, see if you can find them.

See, this is why we need proper documentation, not just poorly commented source code. Care to point to the line of code that does different rounding? `_mm_fmod_ps` that calls `trunc` doesn't count as different rounding. Anyway, it's fixed sequence of instructions. ASIC won't care of rounding modes, it'll use small and efficient logic circuit for this.

> But then you have to ask yourself, how much can you strip out? 20% 50% 75%? Assuming the latter, who is going to buy an $6000 ASIC that only does 4x the hashrate of a $500 Vega 64?

Did you read what I said? The ASIC chip for cn-gpu wit the same computing power will be 4-5 times cheaper to produce: $100 for the power of Vega 64. Of course they won't be sold for this price, rather will be mining in secret and then sold for $1000+.

## fireice-uk | 2019-02-17T18:29:48+00:00
> Division is not supported natively on GPU, it compiles to a long sequence of instructions (reciprocal, multiplication and some more fixup). ASIC can be 2-3 times faster here.

Indeed - hence why it is so rare compared to multiplication and addition. It is a balancing act between having only 3 FP operations (out of 5 available to CPUs and GPUs), which is kind of simple. And including sqrt too - which would only serve to slow things down IMO.

## fireice-uk | 2019-02-17T18:39:43+00:00
> The ASIC chip for cn-gpu wit the same computing power will be 4-5 times cheaper to produce: $100 for the power of Vega 64. Of course they won't be sold for this price, rather will be mining in secret and then sold for $1000+.

I'm not worried about an ASIC that's 4x faster - even 10x faster is acceptable. It is 100x+ faster like the current situation that's a problem.

> Anyway, it's fixed sequence of instructions. ASIC won't care of rounding modes, it'll use small and efficient logic circuit for this.

I can see you trying to set up RandomX - but unfortunately no. Do you know why simple instruction set processors (ARM) are slower than complex instruction set (Intel)? Because overhead of decoding is insignificant. In fact it is so insignificant that there is second layer of decoding, that you know of already (micocodes) and it _still_ is faster than RISC.

It is the computation and not fixed vs not fixed order of computation that's the "meat". For reference - compare the power usage Cryptonote (30%) to Cryptonote-GPU (100%). How much of that power is spent on decode?

## SChernykh | 2019-02-17T18:45:52+00:00
> I'm not worried about an ASIC that's 4x faster - even 10x faster is acceptable

Oh, you should be worried. Even 2x advantage will mean that ASIC will gradually replace all GPUs because GPUs already mine at the edge of profitability.

> I can see you trying to set up RandomX - but unfortunately no.

Unfortunately no, I'm trying to compare it to another GPU-only algorithm (ProgPoW) and all I can see is that cn-gpu is inferior in all aspects compared to ProgPoW.

## fireice-uk | 2019-02-17T18:47:23+00:00
> See, this is why we need proper documentation, not just poorly commented source code. Care to point to the line of code that does different rounding? `_mm_fmod_ps` that calls `trunc` doesn't count as different rounding.

https://github.com/ryo-currency/ryo-currency/blob/master/src/crypto/pow_hash/cn_slow_hash_hard_intel.cpp#L489 but yes, it was a deliberate trap - you would have needed to be familiar with SSE2 programming to catch this one.

`trunc` is otherwise known as Round-To-Zero rounding mode https://en.wikipedia.org/wiki/Rounding#Rounding_towards_zero - rest of the code uses Round-To-Nearest

-----
Much later edit:
Since Monero agitprop squad is already using this one to FUD-away [[ 1 ]](https://imgur.com/a/Zxf4aiJ) let me add that the trap is rhetorical - to catch people familiar with programming.

## SChernykh | 2019-02-17T18:49:21+00:00
> but yes, it was a deliberate trap - you would have needed to be familiar with SSE2 programming to catch this one.

I know how SSE2 works and wrote a lot of SSE code, including ASM code. How we can take it seriously when there is no documentation, only source code. And now it turns out there are "deliberate traps" in this code. Childish.

P.S. Single instruction that does different rounding doesn't count either. I was talking about different rounding modes for all FP operations, not just one place where it never changes.

## fireice-uk | 2019-02-17T18:51:53+00:00
> And now it turns out there are "deliberate traps" in this code. Childish.

Only for people who are trying to make arguments about code they don't understand.

> Oh, you should be worried. Even 2x advantage will mean that ASIC will gradually replace all GPUs because GPUs already mine at the edge of profitability.

We will have agree to disagree on that one. Especially as CPUs are still used on CN despite inferior stats. Why? They are more common. Do you see the parallel here?

> Unfortunately no, I'm trying to compare it to another GPU-only algorithm (ProgPoW) and all I can see is that cn-gpu is inferior in all aspects compared to ProgPoW.

Since you chose not to actually back up your points, instead simply going for "my daddy is stronger" , I think we will agree to disagree on that one too.

## SChernykh | 2019-02-17T18:57:07+00:00
> Only for people who are trying to make arguments about code they don't understand.

Not spotting 1 line in the code doesn't mean I don't understand it.

> Since you chose not to actually back up your points, instead simply going for "my daddy is stronger" , I think we will agree to disagree on that one too.

Ok, here's comparison to ProgPoW:
- 2 MB scratchpad vs DAG - it's possible to implement cn-gpu using only on-chip SRAM, but it's not the case with ProgPoW
- Fixed instruction sequence vs randomly changing sequence
- Memory bandwidth not utilized vs fully utilized on ProgPoW
- GPU caches not utilized vs utilized on ProgPoW
- GPU core fully utilized, the same on ProgPoW

So ProgPow wins 4:1. If any coin wants to be GPU-only, why would they choose cn-gpu which can have 4-5 (maybe 10) times faster ASICs? They'll choose ProgPoW and be guaranteed that ASICs won't be more than 50% faster.

## tevador | 2019-02-17T18:58:41+00:00
> All computer operations can be reduced to a series on NAND gates. In the same way, a person is a collection of carbon atoms. Drawing equivalence between behaviour of a person and a wet sack of charcoal is not an intellectually honest argument. I will give you the benefit of doubt and say you came up with that due to peer pressure rather than deliberate bamboozling.

So do we agree that "compute-bound" is basically the same whether it's bit ops or floating point ops? I still can't see why it's "apples to oranges".

You are talking about "FP cores", but an ASIC will not have actual cores like a GPU. It will have a single pipelined chain so that no execution units are idle at any time (unlike a CPU/GPU). An ASIC with a fully pipelined CN-GPU inner loop will have a ballpark hashrate of around 10 KH/s per chip (500MHz/49152).

> Do you know why simple instruction set processors (ARM) are slower than complex instruction set (Intel)? Because overhead of decoding is insignificant. In fact it is so insignificant that there is second layer of decoding, that you know of already (micocodes) and it _still_ is faster than RISC.

They are slower because they trade speed for efficiency. All modern x86 CPUs are RISC machines on the inside, which proves that it _does_ make a difference.

> It is the computation and not fixed vs not fixed order of computation that's the "meat". For reference - compare the power usage Cryptonote (30%) to Cryptonote-GPU (100%). How much of that power is spent on decode?

Not sure about GPUs, but x86 decoders can use 3-10% of the package power [[1](https://www.usenix.org/system/files/conference/cooldc16/cooldc16-paper-hirki.pdf)], which is not insignificant.

The main point why CN/R or RandomX use a changing order of operations is to prevent pipelined designs and force a CPU-like design with a decoder and ALUs/FPUs.

## fireice-uk | 2019-02-17T19:12:02+00:00
> So do we agree that "compute-bound" is basically the same whether it's bit ops or floating point ops? I still can't see why it's "apples to oranges".

No. The difference is  that you have fairly small subsection of the chip working (AND, OR, shift etc) vs having a large section of the chip working. 

> An ASIC with a fully pipelined CN-GPU inner loop will have a ballpark hashrate of around 10 KH/s per chip (500MHz/49152).

Nice! Not sure how you came up with this exact number on the spot, but it is in line with my 4x faster estimate.

> Not sure about GPUs, but x86 decoders can use 3-10% of the package power [[1](https://www.usenix.org/system/files/conference/cooldc16/cooldc16-paper-hirki.pdf)], which is not insignificant. The main point why CN/R or RandomX use a changing order of operations is to prevent pipelined designs and force a CPU-like design with a decoder and ALUs/FPUs.

Indeed and even with two layers of decoders and a complex instruction set, Intel is faster than ARM with a smaller set. 

## fireice-uk | 2019-02-17T19:15:59+00:00
> So ProgPow wins 4:1. If any coin wants to be GPU-only, why would they choose cn-gpu which can have 4-5 (maybe 10) times faster ASICs? They'll choose ProgPoW and be guaranteed that ASICs won't be more than 50% faster.

Yup, for a change those are real issues (apart from random order, IMO that does not confer real advantage, as I explained already). Of course we won't have a DAG so the comparison is a bit unfair, but I agree - it is something we want to do (together with asymmetry in the next iteration).

## SChernykh | 2019-02-17T19:17:48+00:00
> Intel is faster than ARM with a smaller set.

Intel CPUs are RISC inside. They execute micro-OPs. They only expose CISC interface because of compatibility. ARM is not slower per watt.

> apart from random order, IMO that does not confer real advantage, as I explained already

It is an advantage. You can have exactly the same amount of FP ops AND random order. ASIC won't be able to optimize the circuit as with fixed order, they'll have instruction decoder and CPU-like pipeline. They'll be slower.

## fireice-uk | 2019-02-17T22:18:44+00:00
> Intel CPUs are RISC inside. They execute micro-OPs. They only expose CISC interface because of compatibility.

Exactly, two layers and yet it is faster in absolute terms. It says something about the workload.

 > It is an advantage. You can have exactly the same amount of FP ops AND random order. ASIC won't be able to optimize the circuit as with fixed order, they'll have instruction decoder and CPU-like pipeline. They'll be slower.

I understand your approach. And I also don't think it will work, but only time will tell, arguing until we are blue in the face won't change anything. Hopefully we will get enough time to play around with cryptonight-r and an FPGA. It is not like there is anything preventing us from making pre-pipelined xmr-stak-fpga for the next 5000 blocks on a subscription model. 

## JustFranz | 2019-02-17T23:54:54+00:00
I don't understand how can you even make something like a GPU-POW for a cryptocurrency, not have any documentation and maintain credibility? A crypto POW will potentially protect billions of $ (other people's $) and mine additional billions of $. Considering the importance of POW, expecting people to just "read the code" is outrageous. In addition to being incredibly cumbersome, some people can't read code or your code, they might not be familiar with a specific language or lack knowlege about certain nuances that are relevant to the program.

What we have here is a GPU-POW. It is a GPU-POW because of a single sentence claim that says it wouldn't be efficient on a CPU, hence GPU (just like sha256-POW is an ASIC-POW). I'll believe its not efficient on a CPU. As we know it goes something like this, CPU-GPU-FPGA-ASIC. For it to be a GPU-POW and only GPU, it needs to not be an FPGA or ASIC pow too (and it absolutely needs to do that). What that claim boils down to is: FPGA too expensive (20, 000 USD) and ASIC too expensive (6,000 USD), GPU is cheap (500 USD). 

The dollar cost of FPGA/ASIC is just one of the relevant parameters, you need to plug hash rate and power use into the equation too. The cost of a chip is the man hours it takes to design it (major 1 time cost) and materials and manufacturing (fixed or falling cost per machine, negligible compared to the design stage of a low production chip). When you have the design, you can make as many of them as you want. 

With a 2 mil USD design stage, the first chip costs 2,000,000 USD + 50 USD. The millionth chip is 2 USD +  50 USD. You need to make just 4000 ASICs (2 mil design) for each to cost the same as your 500 USD GPU. 8000 ASICs will cost 250 + 50 each and 16000 will be 125 + 50.

16000 ASICs will cost you 2,800,000 USD
16000 GPUs will cost you 8,000,000 USD

Even if the GPU and ASIC are hashrate/power equal, ASIC will murder you if its worth it.

A POW isn't ASIC or FPGA proof, it is a POW. A coin like Monero can claim that its network is ASIC resistant and the POW plays a part in it. Monero ASIC resistance is:

1. The community supports the idea of ASIC resistance
2. The devs and ecosystems ability to execute scheduled and unscheduled hardforks that won't cause a meaningful chain or community split or otherwise degrade the network and services that depend on it.
3. The devs react swiftly to any vulnerability.
4. The community has software devs who can make a good POW that is beneficial for the purpose of ASIC resistance.
5. A good ASIC resistant POW, which in general would be characterized by:
 a) POW that maximizes the needed die area(s) of a potential ASIC
 b) POW that forces an ASIC maker to spend as much as possible on commodity hardware 
 c) keeps the ASIC package hashrate power efficiency as close to that of the target commodity hardware (by using as much and as many parts of it as possible, forcing the ASIC to mimic and duplicate its functions)
 d) by being as dynamic as possible, negating as many efficiencies as possible that a fixed circuit design would benefit from
 e) avoiding sequences of tasks that could be simplified in ASIC hardware
 f) bonus- this increase in ASIC complexity increases the cost of the ASIC design stage.
 
If any of it goes wrong then ASIC resistance or the whole coin could fail. Nothing makes it ASIC proof.


Please, answer these questions.

Why does Cryptonight-GPU exist? What is its purpose and how does it achieve that? What I mean is explain how it is ASIC/FPGA resistant using points 5.a-5.e. What does CN-GPU do, how exactly does it do it and explain the rationale behind each step of the POW. Is it for the benefit of GPU, detriment of ASIC and how and why?


## hyc | 2019-02-18T00:19:45+00:00
@JustFranz well written comment, but you're wasting your time. fireice is too ignorant to give you decent answers.

>> Intel CPUs are RISC inside. They execute micro-OPs. They only expose CISC interface because of compatibility.

>Exactly, two layers and yet it is faster in absolute terms. It says something about the workload.

The fact that ARM cores haven't been faster than x86 has very little to do with CISC vs RISC and more to do with ARM's predominant focus on low power/high efficiency. They've targeted fab processes that are cheaper, lower power, and lower speed. Notice they still dominate the handheld space, a market that Intel has tried multiple times to breach and has failed every time. Meanwhile ARM has been steadily growing their performance upward step by step, the very same way x86 did when it took over the market from the commercial Unix/RISC manufacturers. Note that ARM designs are already entering the HPC space, which completely belies your notion of CISC /x86 being inherently faster. https://twitter.com/ogawa_tter/status/1093163178102423552

fireice, you know so little about hardware you don't even know how much you don't know. But you've made it more than obvious here.

## JustFranz | 2019-02-18T02:41:03+00:00
@hyc I want to give fireice a chance to have an attempt at presenting CN-GPU in a professional and honest manner, where he can't weasel around the issue if he were to produce something reasonable.

I'm afraid the motivation behind this is personal gain, namely promoting an altcoin. I don't think he is able to form valid technical arguments or a line of reasoning in support of CN-GPU and likely nobody even can. No such thought has gone into the POW and it would be found to be flawed in many aspects regarding ASIC resistance.

I think CN-GPU is a hastily slapped together POW that is born out of greed and by someone who doesn't have a deep understanding of the relevant subject matters, nor do they care to. CN-GPU is a marketing tool and now is the opportunity to use it, just have to pick the right buzzword and make it vaguely fit.

This is a manipulative and dishonest attempt to shill a coin, disguised as a POW pitch for Monero. If fireice had made any concrete claims and explanations about CN-GPU then they could be shot down or confirmed, end of discussion. Back to the drawing board.

No claims and "read the code", what can you do? Say that something is bad and get a "No, you!" back? There is nothing to discuss, no unique idea or angle, nothing. 

IMO this should be closed, knowledgeable people have pointed out flawed aspects of the POW and the person developing and pitching it refuses to meaningfully address them. Anyone is free to bring this up again when there is a document that explains the POW. Right now it is unworkable.

## psychocrypt | 2019-02-18T07:50:39+00:00
I flied over the discussion and must say that "both sides" are very emotional. :-(

> I had hoped this would actually include some documentation on Cryptonight-GPU. Instead, ...

@SamsungGalaxyPlayer  I absolute understand the argument that we need to write a documentation but I see that cryptonightR is the next POW of Monero so this argument not counts at all. Maybe I missed it but I have not see any documentation how the random code generator works and [corner cases](https://github.com/monero-project/monero/blob/cf27e26beb9c0ec64417f89b1078f1e82e8e7069/src/crypto/variant4_random_math.h#L300) are described. We are currently implementing it also ony based on the reverence implementation in Monero and xmrig.
Also points like where the cryptonight loop is changes and what is not described.
The best documentation of the three algorithms is provided by [CryptonightX](https://github.com/tevador/RandomX#randomx)

## hyc | 2019-02-18T08:04:53+00:00
@psychocrypt CryptonightR https://github.com/SChernykh/CryptonightR/blob/master/README.md

Extensive discussion https://github.com/SChernykh/CryptonightR/issues/1

## SChernykh | 2019-02-18T08:21:57+00:00
@psychocrypt We have a [high-level description](https://github.com/SChernykh/CryptonightR/blob/master/README.md) for CryptonightR and [more details](https://github.com/SChernykh/slow_hash_test/blob/CryptonightR/variant4_random_math.h) in comments for the reference implementation. If something is not clear, feel free to ask in https://github.com/SChernykh/CryptonightR/issues/1 and I'll update documentation and/or comments in the code.

P.S. Random generator logic and corner cases that you mentioned are worth describing separately, not just in the comments, I agree. However, another miner author (SRBMiner) has already implemented it and the only thing he asked me about is "where's the test pool?" so I guess documentation/comments in the code are good enough already.

## psychocrypt | 2019-02-18T08:37:25+00:00
@hyc and @SChernykh Yes this docu is known but only the in source comments plus the source describe the random code generation. But thanks for collecting it again, it is also helpful for other readers.
The point that SRBMiner already implemented it is that you have the reference implementation already in xmrig. This not means that he reviewed the code generator.

## SChernykh | 2019-02-18T09:07:14+00:00
@psychocrypt I'll write down a comprehensive description of how random code generator works. It'll take some time though, but it will be ready by tomorrow.

## fireice-uk | 2019-02-18T09:48:12+00:00
> I don't understand how can you even make something like a GPU-POW for a cryptocurrency, not have any documentation and maintain credibility?
> Considering the importance of POW, expecting people to just "read the code" is outrageous.
> some people can't read code or your code, they might not be familiar with a specific language or lack knowlege about certain nuances that are relevant to the program.
> where he can't weasel around the issue if he were to produce something reasonable.
> I'm afraid the motivation behind this is personal gain, namely promoting an altcoin. I don't think he is able to form valid technical arguments or a line of reasoning in support of CN-GPU and likely nobody even can.
> This is a manipulative and dishonest attempt to shill a coin, disguised as a POW pitch for Monero.

@JustFranz Your aggressive language does not lead to a reasonable discussion. Given that I'm arguing with a zero day alt and / or who hasn't written a single line of code (something very usual in Monero) I will close it as it is turning to a "NO U!" instead of technical discussion. 

And yes, I do consider ability to read the source code to be a minimum bar for any review. Sorry, learn or shut up, snowflake.

>I'll write down a comprehensive description of how random code generator works. It'll take some time though, but it will be ready by tomorrow.

Thanks, it will be useful. I won't call you all the names above =)



## SomethingGettingWrong | 2019-02-22T01:58:50+00:00
For what its worth cn-gpu might have hurt "cpu mining" but it allowed nvidia to join the game.... that hash was more beneficial then losing cpu's 

# Action History
- Created by: fireice-uk | 2019-02-16T17:25:02+00:00
- Closed at: 2019-02-18T09:48:12+00:00
