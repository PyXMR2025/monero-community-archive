---
title: Idea for ASIC resistance
source_url: https://github.com/monero-project/monero/issues/3545
author: zawy12
assignees: []
labels: []
created_at: '2018-04-03T11:45:42+00:00'
updated_at: '2024-09-20T17:36:30+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:22:18+00:00'
---

# Original Description
If ASICs are going to be a recurring problem, can you change the POW to maybe 5 or 10 different options every block based on the hash value of the previous block? That way the software could be changed in GPUs  whereas ASICs would hopefully require different hardware for each POW if they are logically and/or mathematically independent enough.   Even better would be if a POW could change a single variable to require a different ASIC, then the previous hash would be used to set the variable for the next block.  

# Discussion History
## moneromooo-monero | 2018-04-03T14:05:05+00:00
That's the idea used by myriadcoin IIRC. It just increases the ASIC cost incrementally though. Maybe it's part of a solution though. For clarity for others reading this, what we've done for v7 is about breaking ASICs through unpredictable change, rather than making harder to build ASICs.

zawy12, could you rename the issue to "ideas for ASIC resistance" or so, we'll need to collect ideas anyway for next switch, since we're very unlikely to have a new PoW by then. So we'll use this to get people start thinking about different ways we could go.


## tevador | 2018-04-03T20:28:31+00:00
I started developing a similar concept of an ASIC resistant PoW.

Basically, the idea is to create a virtual instruction set with basic bitwise, arithmetic and floating point operations and some branching (this must be designed carefully to avoid infinite loops). At the start of each new block, the hash of the previous block is expanded into a few hundred random instructions and compiled into machine code (for CPU/GPU). This random program is then applied to the scratchpad (initialized from the current block header). At the end, the scratchpad is hashed and the result is compared to the target.

Therefore, the PoW would change with every block and if the instuction set is broad enough to cover the majority of what current CPUs/GPUs implement in hardware, then any potential ASIC would be basically a CPU/GPU with similar performance.

The specific details can be tuned so the benefits from a custom hardware are negligible - for example, the PoW code should fit into L1I cache, scratchpad fits into L2/L3 cache, 64 bytes of data are processed at a time (whole cache line) etc. A different permutation of opcodes could be chosen for every block to prevent direct hardware decoding.

This approach has some disadvantages, but it's the only one guaranteed to be ASIC resistant.

## zawy12 | 2018-04-03T20:51:09+00:00
That's really interesting. How would you make solvetime be in the correct ballpark for a given network hahrate? That is, how do you come up with a difficulty setting for an unpredictable algorithm?

## hyc | 2018-04-04T00:02:43+00:00
Sounds a lot like what I outlined here https://www.reddit.com/r/Monero/comments/865vbb/asic_resistance/dw2p4b7/

The basic idea is to use randomly generated code. If you simply select from a handful of known algorithms, eventually someone will build an ASIC that just implements the entire set of algorithms. Using randomly generated code, with an RNG with an intractably large set of states, will defeat that possibility.

My approach is to randomly generate javascript. Developing your own instruction set sounds great but such a development will be immature for quite a long time, leaving countless opportunities for fatal flaws and unexpected optimizations. Using something mature like javascript means most optimization opportunities have already been exploited. (And meanwhile, if anyone *does* manage a new optimization, it becomes useful to the entire computing community.) I will have deployable code demonstrating this approach in a few days.

## zawy12 | 2018-04-04T00:50:04+00:00
Again I can't imagine how you guys are going to be able to adjust a difficulty for randomly generated code that has an unknown solve time. I guess you're right that they could build an Asic for 5 algorithms.

## tevador | 2018-04-04T08:33:56+00:00
@zawy12 The result of the PoW is a standard 256 bit hash of the collapsed scratchpad state, so difficulty targeting is not affected. Basically, just the memory-hard loop of cryptonight would be replaced. Everything else stays the same.

Mining would go like this:
1) Select a nonce value.
2) Compute the Keccak state of the block header and initialize a 2 MiB scratchpad (same as cryptonight).
3) Apply the block-specific algorithm to the scratchpad.
4) Collapse the modified scratchpad to a 256 bit hash (same as cryptonight).
5) If the hash meets the difficulty for the current block, the block is solved. Otherwise repeat from step 1).

The random algorithm would be long enough so that the latencies of different instructions average out and step 3) should take approximately the same time for every block.

The only major difference would be the addidional compilation step when a new block is found.

## ghost | 2018-04-09T15:14:19+00:00
How do you determine the difficulty of the random algorithm though? How do you determine if it even terminates? There must be some rules governing how the algorithm is generated and in that case it may be vulnerable to FPGAs or CGRAs using dynamic partial reconfiguration.

## gsovereignty | 2018-04-09T16:25:40+00:00
> Using randomly generated code, with an RNG with an intractably large set of states, will defeat that possibility.

@hyc that sounds pretty cool, what's the source of randomness though, how do you prove this is random to everyone else? Or doesn't it matter for your solution? 

If verifiable randomness is needed, Micali's VRFs could maybe help but that would probably require a shift towards a PoS-ish solution.

If randomness isn't verifiably random, couldn't an ASIC just propose their own 'randomness' that they are optimized for solving?



## ghost | 2018-04-09T16:56:56+00:00
@gazhayes I don't think the source of randomness matters, people solving based on their own randomness will not get the same result as everyone else, and thus would be rejected.

## hyc | 2018-04-09T18:39:50+00:00
The source of randomness is the block hashing template and the nonce. These are fed as a seed into the PRNG. Everyone must use the same PRNG and same random program generator, otherwise the results are invalid.

## hyc | 2018-04-09T19:51:24+00:00
Proof of concept is here https://github.com/hyc/randprog note that the actual program generator is some pretty bad code. This is nowhere close to useable for real, it literally only illustrates the idea.

Some other differences between mine and @tevador 's proposal - this approach generates an entirely new program for every nonce, his generates a single program for a given block. In my approach, the PRNG and the program generator play a more significant role in the overall PoW. The other approach relies primarily on the difficulty of executing the generated program.

## zawy12 | 2018-04-10T02:09:29+00:00
@hyc It seems like the miner might be able to see higher difficulty in some algorithms and just skip them (go to a new nonce).  Trevador said the algorithm would be long enough that it's computational difficulty would average out.  I'm skeptical but maybe it's possible by bounding outliers.  I can't see how you've address the problem, especially with all functionality of javascript.  It seems like ya'll are attempting a form of genetic programming, which has rules on what can be combined so that valid algorithms are created.   

How are nodes going to easily validate the work without redoing it all?  

Why change the algorithm with each nonce?  Why not use  bits of the hash of the previous block?  All miners would know the algorithm as soon as they start working on a block.



## LordMajestros | 2018-04-10T04:46:36+00:00
On further consideration I don't think verifying this will be easy. It seems to me that the only way to verify it is to do it all over again.

## hyc | 2018-04-10T05:38:11+00:00
Yes, the only way to verify is to perform the same steps. But that's true for Cryptonight too so this is no worse in that respect. (This is not the only approach we're exploring. There are other avenues which allow the verifier to be cheaper than the original proof but I'm not directly involved in that work.)

@zawy12 as I noted, this particular code isn't directly usable. But yes, having all of the functionality of javascript is partly the point. A real solution would ensure some uniformity of difficulty for all of the generated code. E.g., "output will have [30-40] functions, [80-100] variables; functions will have [10-20] statements" etc. - the actual range of parameters will need to be chosen to provide a large enough set of permutations.

Why change on every nonce? Because we already know that companies like Bitmain have automatic tools to turn e.g. C code into e.g. RTL - Someone using FPGAs could easily reconfigure if you only use one algorithm per block. Generating a new program for every nonce eliminates any such advantage. It also eliminates a lot of compiler advantage too - both AOT and JIT compilation trade off compile time for run time on code that executes more than once. Since the generated code will only ever execute once, complex AOT or JIT optimization are pointless.

## zawy12 | 2018-04-10T10:52:58+00:00
@hyc OK, so the validator only has to run the "winning" nonce etc (algorithm) while the miner had to do it for a bunch of different algorithms.  Maybe you should use reverse-polish-notation (stack) thinking which is probably how a lot of genetic programming is done (not to be confused with GAs).  By this I mean your first 2 variables go into a single math operation which might be limited to +, -, * , and /.  Or maybe there is a set of operations that CPUs are better at.  You choose variable widths optimized for CPU, equal to something like 64 bits.  The output from the first operation is one of two inputs to the next operation, and a 3rd variable is the other.  So you have N operations and N+1 variables. To be Turing complete, you have to enable outputs the ability to be inputs to earlier (make it recursive) or later operations, so N+1 is the max number of variables. Cellular automata can be similarly Turing complete.  You don't need all of a language which may require a lot more protective logic (or limitations) for dealing with (or preventing) mal-formed operations. Some variables (and therefore operation difficulty on them) are going to blowup in size (and therefore difficulty).  So to meet the "near equal" computation difficulty requirement, I would make the variable sizes equal to the max for the declaration and let truncation at the max to prevent overflow end be the norm.   Maybe have to make sure the number of each of the possible math operations are always equal, including the recursion count of that operation. But you can't count the number of recursions until you run the simulation, and it's not Turing complete if this is not an option. So it can't be that general, unless you have a rule that the process stops after a certain number of operations, and that stopping point is the output.  But then you can't predict if you'll have way too many divisions compared to additions, unless the stopping point includes an assumption about the relative difficulty of the operations which may not be a good idea.  With recursion, I'm doubtful you can depend on a law of averaging like trevador requires.  This brings me back to the idea of simpler cellular automata where the amount of computation in each step is known, so after the algorithm is created, you know exactly how many steps are required to meet the difficulty requirement.  I guess this is effectively the same thing as the 4 math operations with recursion, except that the method of recursion is pre-defined in the algo at each step, instead of being a free-for-all in what you could end up creating.  

So maybe there is a way to have a very unpredictable algorithm that CPUs are good at that also can have its computational difficulty fixed.  I assume a hash of the output is the thing that is trying to meet the difficulty target.  I don't know why it would be needed, but you might be able to increase the number of steps required via a difficulty algorithm instead of lowering the target hash, or do both.

What I've described goes in a completely different direction than I think equihash and cryptonight, if it is not done to require a large amount of RAM for random access.  But does a GPU or ASIC haved any advantage over CPU with this?  By requiring a lot of step-by-step recursion without much memory, the central processor of any of the architectures would generate a lot of heat. So it's electricity intensive instead of up front equipment cost.  The smallest resolution IC's would have an efficiency advantage, which I think puts ASICs at a disadvantage.

## zawy12 | 2018-04-10T12:31:15+00:00
What I've described above could be done most cost-effectively (least electricity per simple computation) on risc architecture like cell phones, especially since they're optimized for electrical efficiency and low ram. FPGAs and ASICs would be at a disadvantage due to lagging the line resolution in GPUs and CPUs.  An ARM expert could identify the math operations (including bitwise operations) that ARM excels at.  It only needs a way to generate recursive procedures that result in pseudo-random complex patterns like certain cellular automata.  But I don't know if Wolfram found a large "generate-able" class of them that reliably gives complex patterns. 

I'm saying "cellular automata" but they're just sort of discrete differential equations. So you can think in those terms: just find a class of simple non-linear DE's that has these characteristics (predicable computation difficulty per step, yet non-reducible across their class to a more efficient computation).  Both CA and DE's require initial conditions, and if the class of DE's is complex enough the only way to solve is step-by-step recursive procedure that's already been optimized by mathematicians. 

## ipbc-dev | 2018-04-10T13:22:12+00:00
Hello, we thought that a recent idea we started building might be of interest to this discussion:
https://github.com/ipbc-dev/TuringsNightmare (Very WIP)

The idea is similar to what tevador suggests, I think.

## SChernykh | 2018-04-10T14:21:58+00:00
@moneromooo-monero I have a great idea which can be used as a building block for the next small tweak to Cryptonight. It's not a big change like everything discussed above.

So, current Cryptonight is memory-intensive in terms of memory latency, but not bandwidth. Modern CPUs use 64-byte wide cache lines, but Cryptonight only loads/stores 16 bytes at a time, so 75% of available CPU cache bandwidth is wasted. ASICs are optimized for these 16 byte-wide memory accesses, so they always use 100% of whatever memory they have.

The idea is to do something computationally light and safe with the other 48 bytes of the same cache line (which is loaded in L1 cache anyway) on each half-step.

I did a quick test, basically this: _mm_load_si128 -> _mm_shuffle_epi32 -> _mm_store_si128 for the other 3 16-byte chunks in current 64-byte cache line, right after _mm_aesenc_si128 instruction and right after _umul128 instruction. CPU mining performance stayed the same! Well, it went down 0.5-1% in my test, but that's negligible. It's easy to explain why: modern CPUs execute code out of order and have plenty of execution resources, so they can do it in parallel, and these 3 16-byte chunks are already in L1 cache, so no additional delay happens. It's just executed in parallel with AES instruction and MUL instruction.

I haven't tested it on GPU yet, but my estimations show that GPUs use only 15-20% of their memory bandwidth when mining Cryptonight, so they should also handle this change with minimal impact on performance.

ASICs, on the other hand, will have to deal with 4x more bandwith usage, so they will be 4 times less efficient compared to the original Cryptonight ASICs.

This building block (_mm_load_si128 -> _mm_shuffle_epi32 -> _mm_store_si128 for the other 3 16-byte chunks) is easy to add to the next PoW change, together with other changes. And it can't break anything, because it only shuffles DWORDs that are in the scratchpad, it can never cancel anything out to 0 like XOR (if implemented unsafe) or reduce entropy in any other way.

P.S. I just realized that this makes FPGAs 4 times less efficient as well. Not only ASICs.

## hyc | 2018-04-11T01:09:10+00:00
@ipbc-dev All that's needed to solve this is an ASIC designed to execute your 255 instruction opcodes. 255 instructions is a trivially small number to implement.

@zawy12 Your suggestion boils down to a finite state machine. It would require only a small number of logic gates to implement each state, and some other amount of memory.

@SChernykh a 4x speedup for CPUs is nice, but we're looking at ASICs with ~300x CPU efficiency. Spitting into the wind.

https://www.reddit.com/r/Monero/comments/8bbhxq/understanding_network_hashrate_prepost_asics_and/

> Let's start with a rx 580 8gb rig and compare it to an asics rig. A 6 gpu rig gets 5000 h/s. The asics rig from bitmain gets 220,000 h/s for the same amount of power usage. You would need 44 - 6 gpu rigs to get the same hashrate.

## SChernykh | 2018-04-11T05:22:45+00:00
@hyc It's not a speedup for CPU, more 4x slowdown of ASICs. I never said it would solve the ASIC problem entirely, but 4x more ROI time for ASICs could actually make them economically useless with 6 month PoW update cycle. Original ASICs had 1 month ROI, and had 3 months until the PoW change. With 4 times less efficient ASICs they will never ROI before the PoW change, or at least it will be questionable.

## zawy12 | 2018-04-11T08:37:03+00:00
@hyc ASIC gains depend exclusively on a particular algorithm that can be optimized where calculations can be skipped. Very simple recursive algorithms that produce pseudo-random output can't be optimized because they already are optimized.  The extent to which the algorithm produces non-random output is the extent to which they can be optimized, but optimization beyond a certain point requires human tinkering. Before that point, a CPU can figure out the optimization before sending it off to a fabrication lab, so pseudo-random or even being some distance from random may not be a problem.  But the general class of the on-the-fly generate-able algorithms should not have a significant demonstrable general pattern to them that could then be encoded as an optimization in an ASIC.

What I'm saying is the answer.  Everyone's been thinking more RAM is the key, and it has a side marketing benefit of potentially not requiring as much electricity.  But I'm saying there is a great route here that specifically tries to waste electricity. That provable waste is the underlying value of non-fiat coins like gold (see Szabo's writings, Dai's b-money comments about what he was trying to acheive, and attempts to make currency equal to Joules).  Recursive output from simple algorithms can't be optimized.  I read Wolfram's "New Kind of Science" and know the basic theoretical limits of computing which is how I know ASICs and FGPA's are not going to help.  

I'm not sure your changing the algo "per nonce" method is better than the "per block" method, and it might not be good if a miner can identify harder algorithms and just skip it (lending to an exploit by ASICs), but it may be needed to average out the difficulty miners face in the series of recursive algorithms.  I think per block might be better and force us to find a class of algorithms that have the same per-recursive-step computation time.  This tightness might also force us to end up with something more similarly random, and more easily provably unfit for ASICs.

Each single bit transition in a computing element like the output of a NAND gate requires at least  k\*T\*ln(2) joules of energy.  Our devices are many orders of magnitude above this Landauer limit, largely depending on how small the gates can be.  CPUs and GPUs have smaller gates than ASICs and FGPAs, or at least ASICs and FGPAs are not smaller.  

Wolfram and others have proven you can't reduce certain very simple recursive algorithms in a way that eliminates the need to recursively go through all the steps. ASICs will have to burn more electricity than cell phones to do the same computations.

## zawy12 | 2018-04-11T13:03:13+00:00
@hyc [Elementary cellular automata](https://en.wikipedia.org/wiki/Elementary_cellular_automaton) are not necessarily finite state machines and can be Turing complete like wiki says.  I was thinking of automata that potentially use more than just the 2 adjacent cells (the definition of the elementary type) so that it is more likely to be pseudo-random output.  One algorithm per nonce might be required because instead of trynig to create an FPGA per block, you would create a lookup table to fill RAM and use that instead of computing.  But that can't be done with a change every nonce on a large general of algorithms.

Or maybe it could be done with 1 algorithm per block like this:  make it start with 256 bits (cells). A hash of your nonce would be the random number that creates that initial condition.  That way you can't build a lookup table for the algorithm.  If it's random enough, you won't be able to reduce the logic for programming into a FPGA in the time span of a block.

If a very general class could be created that has the same amount of computation per step, then you would have a fixed number of steps to the answer which would be hashed to get your target.  Just as an interesting point, maybe the difficulty could change that number of steps instead of making the target hash lower. 

## hyc | 2018-04-11T16:20:48+00:00
@zawy12 
> ASIC gains depend exclusively on a particular algorithm that can be optimized where calculations can be skipped. Very simple recursive algorithms that produce pseudo-random output can't be optimized because they already are optimized.

This is only part of the story. ASICs are also faster because their memory subsystems don't require complex caches and cache coherency protocols that general purpose CPUs require. You're only looking at the theory, but we're dealing with real world practice where other considerations apply. A state machine implemented in an ASIC can certainly be made to iterate through a set of states far faster than a CPU could be programmed to do. It's not just about a single specific algorithm, it's about all the auxiliary support that does (or doesn't) have to be put in place.

When you toss around mention of "Turing completeness" remember that a Turing machine is just a device that reads or writes one memory cell at a time on a very large ("infinite") memory tape. It is trivial to implement in hardware for a given size of memory. We already know that depending on "xxMB is too expensive to implement in ASIC" as a defense is inadequate.

Whenever you focus in on simple state machines, you're reducing to a Turing machine and the only hardness is how much memory it will need. My approach here is specifically focused on making the algorithm more complex, because (a) while all algorithms can eventually be reduced to something executable by a Turing machine, the number of steps needed to perform that reduction will drastically impact its runtime and (b) increasing the algorithm complexity increases difficulty far faster than just increasing memory requirement.


## zawy12 | 2018-04-11T16:40:48+00:00
Again, the primary goal is to not allow more than minimal memory to be helpful. The only thing that can be fed into the processor is mainly the previous output of the processor, i.e. a heavy reliance on unpredictable recursiveness instead of memory.  I mentioned Turing completeness the second time because you stated it was a state machine which is not Turing complete.  Turing complete is not needed, but something complex enough to have output that can't be easily predicted.  We're talking about changing the "state machine" every block or nonce, so the ASIC and FPGA can't be created ahead of time.  (to execute an optimization of the state machine) ( i am not talking about a finite state machine anyway)

To say it another way, modeling of complex differential equations has to do things 1 recursive step at a time like this.  An ASIC or FPGA could be could be designed for a given model.  But if the model is changing all the time, they can't help.

## hyc | 2018-04-11T17:14:09+00:00
> An ASIC or FPGA could be could be designed for a given model. But if the model is changing all the time, they can't help.

Yes, in this respect we're saying the same thing.

> ( i am not talking about a finite state machine anyway)

Beside the point. The cellular automaton you're talking about is a trivially small set of logic states. All it does is transition from one state to another based on the current input. My point is we need a much larger set of states to transition between.

## zawy12 | 2018-04-11T17:18:29+00:00
Why are more than 2^256 states per cycle (per recursion) needed?  (maybe 1,000,000 loops per hash)

## hyc | 2018-04-11T17:22:49+00:00
All you've described is essentially a compute engine with 4 instructions in its instruction set and a 256 bit program. It is ridiculously trivial to implement.

## zawy12 | 2018-04-11T17:27:42+00:00
Trivial to implement is core to my goal, not a problem. Do you mean it's trivial to optimize?
```
myhash = ffx32 
unless (myhash < target) {
   nonce++
   j =  hash(previous block hash + nonce)
   for (1 to 100)  { 
       j++
       function = generate_function( hash( j ) )
       for  (k=1 to 100,000) {
           input=output
           output = function( input )
       }
   }
   myhash = hash(output)
}
if ( myhash < target ) { claim my block }
```
The ending j and k need to be included in the header for validators, and j checked for being a reasonably small multiple of 100 above hash(previous block hash + nonce)  Reasonably small would be < 1000x of expected hashes per block needed by the largest miner, assuming that miner has 10x rest of the network).  

Where our goal is a class of functions that is reasonably unpredictable in logic, but predictably difficult to optimize and predictably nearly equal in time to compute (for a given "CPU") as all of those in its class.

## hyc | 2018-04-11T17:34:18+00:00
How is what you describe in *any* way different from Cryptonight, which has already been broken?

## zawy12 | 2018-04-11T17:38:16+00:00
You mean other than not using read-writes to random memory and changing my function every hash instead of never?

## zawy12 | 2018-04-11T17:40:29+00:00
OK, now I see the why of your question.  I just inserted a missing part in my pseudocode.

## hyc | 2018-04-12T04:57:05+00:00
I think you're still missing the point. One of the key concepts you seem to be missing is that operations (instructions, code, whatever you want to call it) are interchangeable with data. Cryptonight was "memory hard" because it accessed RAM in random order. I.e, the sequence of steps that accessed the data was unpredictable. This unpredictability didn't prevent ASICs from being developed, because the sequence of instructions required to execute the random pattern was known in advance. (And the instructions themselves were trivial to hardwire.)

Your trivially simple cellular automaton is supposedly going to execute a random sequence of instructions, which you believe an ASIC cannot execute because the sequence can't be known in advance. This is fallacious, because the sequence of instructions you're proposing to generate is merely data. The rules that your automaton operates under are the actual instructions that matter, and again, they're fully known in advance. And the set of instructions you're proposing is tiny, which means they can be implemented trivially in hardware, and their execution efficiency will still outstrip any CPU's.

The reason I've proposed generating code in Javascript is because the set of operations is non-trivial, and executing a Javascript program will require an ASIC developer to implement an actual CPU on their chip.

## LordMajestros | 2018-04-12T12:04:28+00:00
A CPU for every single asic chip This should work if it is feasible. How far along are you on this? @hyc 

## hyc | 2018-04-12T12:33:29+00:00
@LordMajestros I already posted a proof of concept https://github.com/monero-project/monero/issues/3545#issuecomment-379873084 you can try it out yourself.

## zawy12 | 2018-04-12T16:06:54+00:00
@hyc
>The rules that your automaton operates under are the actual instructions that matter, and again, they're fully known in advance. 

They're not known in advance because I am changing the "automata" algorithm 100 times per nonce.  See my psuedocode above.  I thought of automata because I knew off-hand some classes can't be solved for "N loops" into the future without having already run the recursion itself.  Then I remembered most real world differential equations are the same.  My psuedocode is more general than either.  The recursiveness was needed to address the problem of unknown execution time. Otherwise, I'm not arguing for something different than your idea.   I'm trying to make it work and optimize it for cell phones.

Cryptnight's algorithm is known in advanced but ours' are not.  My smaller instruction set is optional, but I wanted to pick instructions that are more efficient on RISC cell phones than on CPUs and GPUs.  I didn't want complex instructions that are not implementable  directly and completely on a RISC chip.  A simpler instruction set may also enable better control of execution time and theoretical characterization of what the results will be.

To try to address your complaint about a simpler instruction set, suppose I have 5x more combinations of instructions than your scheme but use only 4 instructions.  Then I would have 4^5 =1024 advanced instructions in each group of 5 instruction.  Even 1 instruction is feasible:  All javascript is expressible in  NAND or XOR instructions in a specific type of arrangement. 

Let's say I use only the NAND gate (a simple binary if-then statement).  My output every 1,000 loops will be hashed to get a new set of NAND gate combinations out of a possible 2^256 combinations. There could be more if needed.  An FPGA or ASIC or GPU program would have to figure out a simplified version of the NAND gate 100 times per nonce.  This is possible if the inner loop of 1000 is too many loops.  So there's an upper limit on it. Also, the algorithm generating function loop of 100 has an upper bound: it's a slow algorithm that could be optimized by ASIC or GPU programmer, so the time to generate the next algorithm must not be a large fraction of the time to do the inner loop.    

A larger instruction set has the same problems to the exact same extent if I use ```log2(javascript instructions)``` more combinations of NAND gates.  Both schemes seem to need some bound on how the instructions can be combined in order to get approximately reasonable exceution, but that should not change this point.

I found the need to change your scheme by making it change the algorithm 100 times per nonce in order to get an averaging out of solvetimes to be approximately the same while preventing ASIC and GPU programmers from skipping nonces that give apparently slow algorithms.  Generalized loops and skipping sections of code within our created algorithms are not feasible due to creating an unknown completion time, which is a deal breaker.  I have an interior loop of 1,000 to keep the created algorithm 1000x smaller, but thiis just to make sure no one benefits from larger memory.  This is for cell phone efficiency per instruction while negating the benefit of a large CPU cache.  


## hyc | 2018-04-12T20:14:17+00:00
I'm skeptical about skipping nonces - they have no way to know in advance whether any particular nonce will yield a hash that satisfies the target. Skipping a nonce may deprive them of a win.

Yes, all instructions can be boiled down to combinations of a single gate type, but it costs a larger number of gates to do so, and the number of gates a design requires directly determines its cost. The more complexity, the more gates used, the more expensive the ASIC design.

## tevador | 2018-04-12T20:33:54+00:00
@hyc I tested your code and I think it's an interesting concept. Any idea how the ratio of CPU:GPU mining performance would be affected?

My proposal is basically a simpler version of yours, having a lower level language in which random code is generated. Yours has the advantage of a mature VM.

My concept is almost finished. The VM has 3 registers, 4 MiB of memory and can execute 128 instructions. I'm not sure if it's worth developing further (I don't have any test code yet). 

## hyc | 2018-04-12T21:11:26+00:00
@tevador I really have no clue how well a GPU will handle this. Projects like this exist http://gpu.rocks/ but they're aimed at running highly parallelizable functions on the GPU and none of the randomly generated code is really vector oriented.

As you'll have seen from my debate with @zawy12 I'm of the opinion that a simpler VM is a weakness because it becomes too easy to implement in hardware. But we have to balance that against @zawy12's point that it makes future optimization less likely.

## tevador | 2018-04-12T21:46:32+00:00
The problem is that if this algorithm ends up being only CPU-mineable, monero can lose a majority of miners, who form a large part of the community. It would also incentivize malware mining.

That's why I designed my algorithm to be GPU-mineable.

## zawy12 | 2018-04-12T22:41:29+00:00
Skipping nonces: what I'm saying is that I don't think you have bounds on the time-difficulty of the generated algorithms, but that an ASIC could be designed to quickly recognize if an algorithm is going to be difficult to solve, so they'll skip it.  

I can't see if you still disagree.  In reference to ASIC complexity, as I was saying, as I would just use the smaller set of instructions a larger number of times to equal your larger set of instructions with fewer steps.  I want to send it assembly meant for ARM processors and for it to be as difficult as your javascript.   We can go so far beyond what an ASIC can predict, I'm trying to cheat by redirecting it's output to its input, enabling "only" 2^256 different functions on random 32 byte seeds.    

I think the general method of a small instruction set is the only one that can have predictably similarly difficult functions like I'm saying seems absolutely necessary.  With say 4 instruction (they might just be well-chosen bit operations) it seems possible to know what average amount of computation they have, and to prove the 4 selected will continually add complexity rather than going towards patterns like all 0's or all 1's.  

It's not that I know a larger instruction set won't work. The problem is that I view the task of getting similar execute time to be less daunting with fewer instructions.  BTC script had to exclude loops and other things for the same reason. And still many scripts can go bad.  Fewer instructions might be useful in proving the algorithms are well-behaved.  

I think not only limiting the type of instructions is needed, but probably also limiting how they can combine.  This increases the risk of an ASIC optimization of the gneral class of algorithms you produce.

+, -, /, and * creates something wider in scope than power series which can approximate any function.  But maybe it should be required to follow the rules of power series.  Actually power series are recursive like automata and D.E.s, it does fit in well with my desire that the only loop be external to the "function".  I'm been using "function" very unmathematically to mean "algorithm of any type", since I don't have those details worked out. 

>@zawy12's point that it [fewer instruction] makes future optimization less likely.

I don't think I said that.  I don't view my scheme as more difficult for ASICs to "hack", but that I have more hope it will help the design process in creating an "algorithm generator" that has well behaved  output and similar execution time. 

There's another potential advantage to doing recursive simple steps "on chip".  When you have a large algorithm full of a wide range of instructions that are not going to be native to the chip, there are delays from going back and forth to RAM.  If you have an instruction set of say 256, and if they all need to have 64 bit inputs and 64 bit outputs and follow each other sequentially (in order to be well behaved), then a lookup table 3GB in size (or much less with compression) could be used instead of actually computing each sequence of 4 instructions. There may be ways around this like changing input data before instructions by a 1 to 4 bit shift based on something unpredictable, or similarly every instruction could have two inputs where one is the output of a previous instruction and the other is seed data.  

Fewer instructions has the same problem with this, but I'm hoping a chip can go through more instruction than can be pre-implemented in a lookup table, faster than the time for a lookup-memory transfer in an ASIC.  I probably need to use as many on-chip instructions as possible, supporting @hyc 's viewpoint.   But my reasons for wanting to keep a limit on instructions remain.  

GPUs as well as CPUs can use a lookup table, and may not be improved upon by ASICs, but I _feel_ like this is a problem that should tried to be avoided, and but my starting point (same size inputs and outputs going from 1 instruction to the next) is seductively simple in terms of getting constant compute time and good behavior implemented.

If one of the two ways to foil lookup tables works, an ASIC may still implement the actual logic of every hard-to-compute pair, triple, and maybe quadruple sequence of complex instructions.  It can't do every pair due to the large instruction set.  Just implementing all non-redundant pairs of 256 instructions could be difficult.  It would have a lot more flexibility in exploiting sequences of fewer instructions, so that's a  +1 for @hyc .  I mean it could easily optimize and implement every 5-instruction sequence of a 4-instruction set, naively giving it a 4x speedup, if it can be done as a fast as on chip.   So I'll say I'll make the instruction set as large as I can as long as it stays on the chip, and as long as I can make them predictable in computation time and otherwise well-behaved.  So maybe I'm in trevador's ball park.  

My pseudocode (that I've been changing all day as I realized problems) applies as well to large sets as small:  I think the recursion outside the algorithm as the only loop allowed is a requirement for this to work.  Without it, the algorithm will have to be a lot more complex which means a lot of complicated memory usage that means too much room for GPU optimization.  It's not that I'm that strongly against GPUs, but I don't the long drawn out process of GPU devs slowly increasing hashpower for a pecentage.  It makes me think if GPU optimization can be done, there's a loophole for ASICs.  Assembly code doable solely on the chip seems like it has the nice possibility of never becoming optimizeable.

If the algorithm generator can make algorithms with solvetimes +/- 5%, then my 100 algos per nonce is not needed, and 1 algorithm per block might be sufficient.  I don't think you can get a routine to optimize the algorithm and automatically reprogram an FPGA that fast.  But since GPUs could, I might still prefer the per nonce method.

## hyc | 2018-04-12T23:43:01+00:00
GPU support is looking pretty bad, from what I can see. I think most of the work winds up being done on the host CPU. The generator could be translated into OpenCL, no problem. But we'd need something to transform the generated code into OpenCL as well, and the OpenCL compiler only runs on the host. I don't know any portable way to transform the generated code into GPU-native code on the GPU itself. (You want to use a vendor-supplied GPU compiler, because it knows all the device-specific details of each target.) But this isn't really my specialty, maybe someone else knows how to handle this.

Or: someone ports the entire VM into OpenCL, and the GPU just interprets the generated code. I suppose that's fine.

## joijuke | 2018-04-13T05:35:24+00:00
@yinwang0 can you join talking?? 

## ipbc-dev | 2018-04-13T06:09:57+00:00
@hyc  why you want to use gpu? think about devices without a gpu.
@zawy12 please take a look here https://github.com/ipbc-dev/TuringsNightmare/blob/master/TN_Explanation.md

## Gingeropolous | 2018-04-14T04:36:41+00:00
I wouldn't worry about GPUs at this point. I'd say get a working thing up and running, and then do what tromp did with cuckooo cycle - claim that its not GPU mineable, slap a bounty on it, and see what happens. 

miner developers *will* find a way to mine on GPUs ...thats sort of a given. 

## tevador | 2018-04-14T14:55:32+00:00
I made some research about the possibility of running general purpose code on a GPU.

Firstly, all AMD GPUs before the GCN architecture (everything older than Radeon 7700 Series) do not support non-inlined function calls and recursion, so you could not even compile the javascript VM for these architectures (the compiler gives "irreducible control flow error").

CUDA and GCN graphics cards seem to have the necessary hardware support to actually run a full javascript (or any other) VM, although someone might have to write a new compiler for that.

The problem is that although these modern GPUs could theoretically run a full virtual machine, they lack support for speculative execution and branch prediction, so their performance per clock would be at best at the level of the first generation Intel Atom CPUs. Combined with the fact that GPUs typically run at about half the core frequency of a modern CPU, their "per-core" performance would be about 6-7 times lower than a CPU core. This estimate is based on [Passmark CPU benchmark score of Intel Atom 230 vs AMD Ryzen 1700](https://www.cpubenchmark.net/compare/Intel-Atom-230-vs-AMD-Ryzen-7-1700/603vs2970) and it's a conservative estimate because this Intel Atom has core frequency higher than most GPUs (1.6 GHz) and supports branch prediction. In reality GPUs can be closer to 10 times slower.

To give a real example, the AMD Radeon RX 570 graphics card has 32 compute units (CU). Each compute unit has a separate instruction scheduler, so they can be considered like "cores" on a CPU, since each CU could run a separate mining thread. The estimated mining performance would be simular to 3-5 CPU cores, or about half the performance of a Ryzen 7 1700, which costs 30% less than the GPU.

In conclusion, the performance per dollar of GPU mining would be around 3 times lower than CPU mining. I think this is enough to make it unprofitable.

Sources:
https://community.amd.com/thread/167912
https://community.amd.com/message/1298840#comment-1298840
http://www.nvidia.com/content/PDF/fermi_white_papers/P.Glaskowsky_NVIDIA's_Fermi-The_First_Complete_GPU_Architecture.pdf
https://en.wikipedia.org/wiki/Intel_Atom


## zawy12 | 2018-04-14T15:08:54+00:00
Unless botnets become a problem I don't think CPUs being competitive with gpus is a drawback. It has historically been considered ideal for CPUs to be more competitive than gpus. This is so that the network can remain diverse and therefore less subject to attack

## LordMajestros | 2018-04-14T15:15:49+00:00
GPU miners attach several GPUs to a motherboard, it is more difficult to scale this way with CPUs. 
I don't see the problem unless of course botnets become a bigger issue.

## hyc | 2018-04-14T16:12:56+00:00
@tevador thanks for digging into this. It might be acceptable to shut out pre-GCN GPUs. There's another aspect of this, a full JS interpreter will be a few MB of code itself. Lower end GPUs wouldn't have the memory for it anyway. (Most smartphone GPUs already lack the memory for CryptoNight so this isn't very surprising.)

## hyc | 2018-04-14T18:21:20+00:00
(For the record, the spaghetti-code function in https://community.amd.com/thread/167912 can be rewritten equivalently as this
```
void qwe() {
   int CUR = 2;
   int i=0;
   while (i<300) {
      i++;
      if (CUR > 0) {
         CUR--;
         continue;
      }
      break;
   }
   while (CUR <2) {
      CUR++;
   }
}
```
Pretty much any use of gotos can always be rewritten in structured form. If this was the only obstacle, that'd be OK. Probably not the only obstacle of course.)

## zawy12 | 2018-04-14T19:00:16+00:00
@LordMajestros Does or can the motherboard build the assembly code for the CU and pass it off for on-the-CU processing?  If not, then interrupts from all the CUs to the motherboard would slow it down to the speed of 1 CPU. 

 If botnets are a major concern and GPUs preferred, then the simple instruction set could be optimized for GPU CUs.  Then for an ASIC to beat a GPU, it would have to be basically a larger set of CUs than a GPU.  But ASICs will not be able to do it as electricity-efficient as mass-produced GPUs that have smaller etching lines.  Even if cell phones and CPUs can use the electricity more efficiently per hash, they can't scale so that if price goes up faster than cell and CPU power comes online, then GPUs would fill the gap. This is with an instruction set and algorithm size that can stay "on-chip".  Because of the lookup table problem, I would use the largest instruction set that can stay on chip.  The sequence of instructions must be a reliable computation time.  So I would group the instructions based on having execution time within +/- 10%  Let's say I have 256 instructions that have speed like in 16 different groups, and I selected the possible instructions based on this requirement so that there are 14 to 17 instructions in each group.  The generated algorithm per nonce would be 256 possible instructions in a sequence of 32 instructions. So only 2 instructions from each of the 16 similar-execution-time groups would be allowed in each algorithm.  A 32 instruction algorithm would not need to access off-chip memory.   This is hopefully complex enough that a GPU can't reduce it to much simpler equation and feed  the CUs the simpler code before the original code finishes and goes to next nonce.  The 256 bit random number needed to select them would the previous block's hash. A hash of that hash would provide the seed.  The actual bit-size of the seed could be bigger or smaller.  Each instruction would operate "nicely" on inputs.  By this I mean its output must be the same size and not reduce its entropy too much.  Each instruction might be a pair of instructions to meet the entropy criteria.  For example, if you use a 256 bit input with an addition instruction, you might split the input data in half and add the halves, ending up with a 129 bit number and 127 leading zeros, reducing the input's entropy.  

Such a simple algorithm requires the inner loop above, which is just using the algorithm's ouput to create the seed for the next iteration. The outer loop is not needed (since I'm keeping a tight constrain on solvetimes). But it could be used if the constraints can't be as tight as I specified.

We do not have the expertise to prove it would be ASIC resistant, but maybe there is enough knowledge here to turn it into a functioning POW.   If my equal-solvetime criterion is met, I can get  a cryptonote clone or two to implement it live. 

## tevador | 2018-04-14T20:33:56+00:00
@zawy12 My virtual machine does mostly what you described. I will have proof of concept code ready soon.

## tevador | 2018-04-15T20:57:26+00:00
"CNVM" algorithm - proof of concept code: https://github.com/tevador/cnvm

## hyc | 2018-04-16T11:46:46+00:00
@tevador as I mentioned before, this seems way too simple. Randomizing the opcode map isn't accomplishing much either since a lookup table can sort that out. It would be pretty easy to implement this entire VM as a hardwired ASIC.

## zawy12 | 2018-04-16T15:13:15+00:00
His instruction set and algorithm construction seem to be following what I'm looking for, if it can result in near-equal solvetimes (using the selection process I described).  If ASICS can't be made to have more CUs than GPUs, then my idea might work. 

## tevador | 2018-04-16T15:33:10+00:00
@hyc Ultimately, all VMs can be implemented in hardware (even javascript). It's just a question of how much silicon would be required to do it.
 

## joijuke | 2018-04-18T15:38:18+00:00
simd in js  

## hyc | 2018-04-19T01:09:04+00:00
@tevador Yes, absolutely. My perspective is that javascript is far more complex than what you're working with, and will take a lot more silicon to implement. Which means larger cores, which means fewer cores per chip, less computational advantage.

## tevador | 2018-05-12T21:01:31+00:00
I started developing my own javascript generator written in C#.

Also I modified the proof of work algorithm to be asymmetrical (faster verification than solving).

Working demo here: https://github.com/tevador/RandomJS (still in development).



## hyc | 2018-05-14T05:57:41+00:00
Could you give a more detailed description of how the asymmetric verification works?

## tevador | 2018-05-14T13:47:53+00:00
[Algorithm description](https://github.com/tevador/RandomJS) added.

Feel free to review it and comment.

## baryluk | 2018-05-16T15:55:19+00:00
Just my two cents. I like the idea, but I would also suggest to include 64x64 bit multiplication and 64x64 bit division operations, which are notoriously complex to implement, and almost never used in crypto ASICs or hash designs, as their circuits either are slow, very large, or poorly understood from crypto research side of view. CPU and GPUs can do it. Implementing wide multiplications and divisions on only 32-bit archs, is also possible, at the expense of some few more branches, which is fine. FPGAs rarearly do have so wide multipliers, they do have DSP blocks with FMA units, but usually it is more like 18 or 28 bits or something like that (which is fine for almost all signal processing in real world with input data from ADC only having 16 or 14 bits of resolution anyway), you can probably combine multiple blocks for something wider, but that is also fine. I do not have much against FPGAs, as they are easier to obtain by general public in arbitrary quantities (sure, it is hard to buy large or very high frequency FPGAs, or FPGA eval boards, as they tend to be expensive, and populated with a lot of stuff that is not relevant to crypto). If anything, random algorithm generated by the generator should be small enough that it fits in L1 or L2 cache or on medium size FPGA (<50k gates).


## baryluk | 2018-05-16T16:02:45+00:00
As for the RandomJS, the idea is ok as a prototype, but I am very against adding V8 as an enormous dependency of project like that. It just creates a lot of security issues, toolchain issue and portability to other platforms problems (V8 was not working on aarch64 well until just last year basically for example, and it doesn't work on more obscure, but otherwise capable, archs and operating systems at all).

The nice thing about the RandomJS is that is basically bypasses JIT to big extent, or at least make it the same both for miner and for verifier, by changing entire algo not just for the specific block, but also for each nounce. That actually also makes it hard to implement in FPGA. (which I am not sure it entirely good idea, from network security point of view, but otherwise I think fine).

As a more production oriented option I would suggest Lua (standard C implementation) or LuaJit (C/C++ alternative implementation for multiple platforms). They are small in size and well maintained and portable, and designed for embedding in other programs. You can also have multiple independent VMs in same process or even same thread, so parallel verification, mining, etc is easy.

## tevador | 2018-05-16T22:06:01+00:00
@baryluk 

> Just my two cents. I like the idea, but I would also suggest to include 64x64 bit multiplication and 64x64 bit division operations, which are notoriously complex to implement, and almost never used in crypto ASICs or hash designs, as their circuits either are slow, very large, or poorly understood from crypto research side of view. CPU and GPUs can do it. Implementing wide multiplications and divisions on only 32-bit archs, is also possible, at the expense of some few more branches, which is fine. FPGAs rarearly do have so wide multipliers, they do have DSP blocks with FMA units, but usually it is more like 18 or 28 bits or something like that (which is fine for almost all signal processing in real world with input data from ADC only having 16 or 14 bits of resolution anyway), you can probably combine multiple blocks for something wider, but that is also fine. I do not have much against FPGAs, as they are easier to obtain by general public in arbitrary quantities (sure, it is hard to buy large or very high frequency FPGAs, or FPGA eval boards, as they tend to be expensive, and populated with a lot of stuff that is not relevant to crypto). If anything, random algorithm generated by the generator should be small enough that it fits in L1 or L2 cache or on medium size FPGA (<50k gates).

Most of your points are implemented in the CNVM proof of concept. The problem is that the VM can still be realized entirely in hardware with much higher efficiency than CPUs/GPUs can achieve. 

By the way, GPUs usually don't have hardware integer dividers and divison must be done in software. 

In any case, this debate needs ASIC design specialists to help us make the right choices.

> As for the RandomJS, the idea is ok as a prototype, but I am very against adding V8 as an enormous dependency of project like that. It just creates a lot of security issues, toolchain issue and portability to other platforms problems (V8 was not working on aarch64 well until just last year basically for example, and it doesn't work on more obscure, but otherwise capable, archs and operating systems at all).

The algorithm does not necessarily need to use the V8. There are other ECMAScript engines - for example, [this](https://github.com/jerryscript-project/jerryscript) is one lightweight implementation. Personally, I don't see any security issues here with using the V8. For mining software, you want to use the fastest possible implementation, which is the V8 at the moment. There could be a more portable version using a slower Javascript engine just for blockchain verification.

> As a more production oriented option I would suggest Lua (standard C implementation) or LuaJit (C/C++ alternative implementation for multiple platforms). They are small in size and well maintained and portable, and designed for embedding in other programs. You can also have multiple independent VMs in same process or even same thread, so parallel verification, mining, etc is easy.

I think one of the arguments for using Javascript was that even if an ASIC was developed, it would benefit everyone because then perhaps we could have hardware accelerated browsers one day.
Also the Javascript implementation being larger in size is actually an advantage against ASICs.

## baryluk | 2018-05-16T22:15:20+00:00
LuaJIT is faster than V8. And it is maybe 200KB of code. Not 60MB of hell that takes 20 hours to compile on decent computer.

## Gingeropolous | 2018-05-19T05:25:19+00:00
well, make it in luajit :)

## hyc | 2018-05-19T05:58:53+00:00
You're not helping.

Javascript is a good choice *because it's bulky* - an ASIC developer will need more resources to implement it on a chip.

## tevador | 2018-05-20T10:11:08+00:00
I managed to get the runtime of the random program relatively under control. See https://github.com/tevador/RandomJS/issues/1 for detailed statistics.

I found 3 major reasons for outliers with high runtime:
1. *Nested loops.* I fixed this by capping the total number of loop cycles in a program.
1. *Function calls inside loops.* I fixed this by disabling function invocation in loop body.
1. *Large strings.* String concatenation can slow down the program by memory allocation/garbage collection if the string length exceeds reasonable limits. I fixed this by capping the maximum length of a string.

Still I have to somewhat reduce the complexity of the program as I'm aiming for an average runtime around 5 ms.

As for program features, I still plan to incorporate objects (currently only numbers, strings and functions are used).

## zawy12 | 2018-05-20T10:42:26+00:00
@tevador The runtime problem is why some of us have said the complex algorithm solutions will not work. I believe that by the time you've got a stable runtime solution, you will have restricted the possible algorithms in a way that it may be amenable to ASIC implementation.  

The solution I proposed may also be too amenable to ASICs because I would have a restricted set of instructions, so the ASICs would just be 10,000 simplified "CPUs" running the algo in parallel with difference nonces. So the problem with my idea is approximately zero hardware cost compared to GPUs, although ASIC electricity cost may be 2x higher. But it may be salvageable for a constant-value coin that has no mining rewards or mining fees, but runs on everyone's cell phone with the wallet.  So only a 51% attack would be profitable and very difficult if there are sufficient cell phones and CPUs running it in the background.

## tevador | 2018-05-20T11:08:05+00:00
@zawy12 I don't think the optimizations are too restrictive to enable ASIC implementations. The program is still way too complex for that.

I any case, the generator has an XML config file, so you can disable the restrictions and test. The only restriction which must be in place is 3), otherwise the program crashes sometimes when string concatenation happens in a loop.

By the way, today there was a guy in the chat on supportxmr.com claiming he has a new ASIC in development for cryptonight + any possible variants of it (includes an FPGA so it's partly programmable). He was quoting 100 KH/s @ 1 kW, shipping in July. I think he was legit.

## zawy12 | 2018-05-20T12:49:52+00:00
I'm waiting to see if you guys are successful with the more complex approach.

## moneromooo-monero | 2018-05-24T15:05:01+00:00
> I did a quick test, basically this: _mm_load_si128 -> _mm_shuffle_epi32 -> _mm_store_si128 for the other 3 16-byte chunks in current 64-byte cache line, right after _mm_aesenc_si128 instruction and right after _umul128 instruction. 

@SChernykh, would you mind posting some code implementing this so we're sure to use the exact same code ? I'm planning on using this as one of the v2 changes.


## SChernykh | 2018-05-24T15:09:30+00:00
@moneromooo-monero Yes, I'll post it here later today. I deleted the original code, but it's easy to recover from scratch.

## SChernykh | 2018-05-24T15:54:16+00:00
Here you go: https://github.com/SChernykh/xmr-stak-cpu/commit/5f8acd10ed2ae55f1ee8a02f0302e186c9f410cc

I took the old xmr-stak-cpu repo for testing purposes. It still has the original Cryptonight implementation, you can see what exactly I did there. Performance difference with shuffle on is negligible on CPU.

## LordMajestros | 2018-05-26T17:46:15+00:00
Here is another approach to asic resistance that claims asics can only get 1.1-1.2x improvement over GPUs. https://github.com/ifdefelse/ProgPOW

## hyc | 2018-05-27T14:48:35+00:00
@LordMajestros I've been emailing them privately to discuss their scheme. One thing I don't like about it is that it's GPU-centric, and CPUs are at a large disadvantage.

## zawy12 | 2018-05-27T15:21:37+00:00
@hyc Although it may be possible to make electricity more expensive on GPUs and ASICs compared to cell phones and CPUs, the hardware cost to get a lot of instances running should be a lot less on GPUs and ASICs. For this reason, if the only way to beat ASICs is with GPUs, then so be it.  A POW for cell phones and CPUs seems to have serious potential only if there are no profits in mining and if the coin is widespread as a wallet+miner app on cell phones.  Satoshi's idea was to make the network strong against attack by making it profitable, but it seems like this has the hard-to-avoid side effect of centralization.  Maybe strong-by-widespread-adoption combined with diverse-by-being-unprofitable is an implementable solution, somehow.  

## baryluk | 2018-05-27T15:33:56+00:00
GPUs and CPUs are general chips and can do the same set of tasks. Any PoW is parallelizable (because multiple independent miners need to be able to mine in parallel ), and no matter what is the ratio of compute to memory usage and bandwidth, the GPU can hide memory latencies much easier due to highly threaded nature. As such I think fighting GPUs is not an option, and any future PoW algorithm should be compatible reasonably with GPUs. If you design PoW to be more efficient on CPU right now, with time GPUs will catch up on this specific front, and be more efficient. Also the issue is about ASIC resistance, not GPU resistance. And I would advise to not set goals too high at first, before actually having something that works good on GPU. Iterate from there then.

## tevador | 2018-05-27T16:07:25+00:00
> Here is another approach to asic resistance that claims asics can only get 1.1-1.2x improvement over GPUs. https://github.com/ifdefelse/ProgPOW

I didn't find any details how the 1.1-1.2x ASIC improvement was calculated.

It doesn't use any floating point operations, so I think an ASIC chip could be a lot smaller than a GPU in terms of the required silicon area.

## SChernykh | 2018-05-27T16:39:01+00:00
@moneromooo-monero I improved my shuffling modification a bit: https://github.com/SChernykh/xmr-stak-cpu/commit/cf5175aabbf08cd25366b66a4e4b98e4e8958a48

My concern was that data never crossed 16-byte border during shuffling which could lead to some ASIC/FPGA optimizations. For example, ASIC/FPGA could just maintain virtual ordering (1 byte per 16 bytes of data) instead of actually moving the data in memory. Now it's moved all across 64-byte cache line.

P.S. Maybe some other simple operations like XOR could be applied in addition to shuffling without impact to performance. I'll keep experimenting.

## moneromooo-monero | 2018-05-30T18:14:28+00:00
Is there any mileage in doing some operation on that extra memory for which there's a fast enough CPU instruction, and which would require substantial extra silicon, like a a division ? Those seem to be still slowish on CPU but it might be "hidden" by memory latency ?

## SChernykh | 2018-05-30T18:20:02+00:00
Division, unfortunately, is a showstopper for parallel execution. It occupies a lot of resources, even if its result is not needed for the next instruction. It's in my plans to try hiding division latency - maybe by using division result only on the next iteration. But I still think it will slow down the main loop.

## tevador | 2018-05-30T18:37:46+00:00
Division is usually not pipelined in the CPU because its latency varies widely depending on the values of the operands. This means any instructions that depends on the result of division are stalled until the division is complete, which can be up to 100 clock cycles for 64-bit division.

One alternative would be to use the completely free floating point unit.

## SChernykh | 2018-05-30T18:53:52+00:00
@tevador Up to 94 clock cycles on Skylake (and *-lake successors), but only up to 46 clock cycles on Ryzen: http://agner.org/optimize/instruction_tables.pdf

## SChernykh | 2018-05-30T19:44:18+00:00
@moneromooo-monero @tevador  I've added division modification to test: https://github.com/SChernykh/xmr-stak-cpu/commit/c76996617c5175ffe9f03f7ca1b3f9b3115a60a3

It looks like my idea with using division result on the next iteration to hide latency worked, only 3.5% slowdown in my tests. And even combined with shuffle modification it's still only 3.5% slowdown.

P.S. I had a stupid copy-paste error in that commit, but it didn't change performance results.
P.P.S. Actually, it's 6.5% slowdown with division. I rebooted my notebook and tested it again without anything else running in background.

## tevador | 2018-05-30T21:00:22+00:00
For a 3.5 GHz CPU @ 70 h/s, it's at most 95 clock cycles per cryptonight iteration, which is very close to the maximum division latency. So this might work with one division per iteration. Would be interesting to also test it on a GPU.

## SChernykh | 2018-05-30T21:02:08+00:00
GPUs have an abundance of computing power, they're mostly limited by memory access when running Cryptonight.

## tevador | 2018-05-30T21:46:12+00:00
However, the shuffle can have some impact on GPU performance, For example, xmr-stak in default configuration splits the scratchpad into 16 byte chunks interleaved with the chunks of other threads. This pattern will have to change to avoid 3 additional memory accesses.

## SChernykh | 2018-05-31T05:23:26+00:00
Yes, just interleave 64 byte chunks instead. I don't see a problem for GPUs in that. Quite the contrary, GPUs like accessing larger chunks, they're optimized for sequential access. The only problem is 4x memory bandwidth usage, but GPUs also have enough bandwidth:

Radeon Vega 64 uses 15% of bandwidth currently: 37 MB per hash, 2000 h/s = 74 GB/s out of 483.8 GB/s available.
Radeon Vega 56 uses 16.2% of bandwidth currently: 37 MB per hash, 1800 h/s = 66.6 GB/s out of 409.6 GB/s available.
Radeon RX 580 uses 12% of bandwidth currently: 37 MB per hash, 830 h/s = 30.71 GB/s out of 256 GB/s available.

And so on...

## tevador | 2018-05-31T08:16:10+00:00
I just tested with an RX 550 using the "mem_chunk" option in xmr-stak. You are right, no performance drop when switching to 64 byte chunks.

If a GPU execution unit can emulate integer division in less than ~1000 clock cycles (approximate time of one CN interation for my RX 550 @ 1200 MHz), then there should be no impact on GPU performance.

## SChernykh | 2018-05-31T08:23:45+00:00
And I just tested shuffle & division on the newest Skylake-X processor. Division latency is hidden entirely here, no performance drop at all: only 2.5% slowdown with shuffle and the same slowdown with shuffle and division. Funny thing is that the actual performance with one thread is lower on modern 4 GHz Skylake-X than on 6 years old 2.7 GHz Ivy Bridge notebook processor, even with the original Cryptonight. It proves once again that Cryptonight is memory latency bound and we can add a lot of computations without affecting performance.

## Gingeropolous | 2018-05-31T12:14:41+00:00
@SChernykh , can you weigh in on this whole javascript code proof of work thing? I see you are active on this thread, but haven't directly spoke up on the javascript thing that @hyc and @tevador have proposed and created prototypes for. Specifically, @tevador mentioned above

> In any case, this debate needs ASIC design specialists to help us make the right choices.



## SChernykh | 2018-05-31T12:33:11+00:00
I'm not an ASIC specialist. But as a programmer, I see it as a high risk change at this point, maybe even in a year from now, after a lot of testing, it will still be risky. Chrome's V8 engine is huge and of course contains (yet unknown) bugs that can be exploited. The random code can't be truly random because of so called "halting problem" (google it), so the programs generated must be a small and limited subset of what Javascript (and any other programming language) can offer. But yes, it will make an ASIC hardware implementation look a lot more like CPU/GPU than it is now, with almost no performance gains.

And, judging by current tendentions in general purpose CPUs - all these new instruction set extensions, they're likely to have some JS acceleration support in the future. Which is good for this approach.

P.S. Right now I concentrate on how to modify Cryptonight to use CPU strengths that are not used yet, making it less efficient for ASICs without impact on CPU/GPU. Shuffling exploits unused cache bandwidth, division takes advantage of out-of-order execution. Maybe there is something else I'm missing here. But it's still a temporary solution. Random programs is the way to go for the future.

P.P.S. And random programs must also have an efficient GPU implementation, otherwise we'll have a big problem with mining community and a lot of unneeded fork debates.

## tevador | 2018-05-31T13:03:16+00:00
@SChernykh The halting problem is based on deciding whether an arbitrary program will halt or run forever. However, this has no impact on random program generation, because we don't generate *arbitrary* programs. For example, it's trivial to restrict the generation routine to exclude infinite loops and infinite recursion. The subset of programs that don't run forever is still so large that this has no impact on ASIC resistance.

As for bugs in V8, the worst thing I can think of is if someone can find blocks that generate programs that crash the VM. This is not really a security issue.

But I agree that it's a big change and needs a lot of testing before being deployed by a major cryptocurrency like Monero. I'm currently starting a collaboration with the Wownero dev team to implement RandomJS (Wownero is a fork of Monero).

## SChernykh | 2018-05-31T14:05:17+00:00
One more concern is determinism. The same JS program/JS engine combo must produce exactly the same results on all supported platforms (x86, ARM), OSes and compilators in order to be used for hashing. It's very hard to achieve this, especially with floating point calculations enabled in generated programs.

## baryluk | 2018-05-31T16:43:21+00:00
Not only that, even future versions of the same engine (i.e. corrected for bugs or security issues), can change results, due to different ordering of operations that are assumed to be commutative, or optimized, or just finding out that the engine is not conforming to spec (which should not happen as long as we stick to basic operations, and do not call external functions, i.e. from Math module). This mostly applies to floats, i.e. when doing multiplications, additions and divisions, (i.e. (a/x + b/x) = (1.0/x) * (a + b), second being faster, but not actually equal). The problem is JS all numbers are floats! So you are screwed. This also applies to integers to some extent, where many compilers will assume overflows do not happen in well conforming program, and use various shortcuts. Also JIT might change behavior of function inlining and loop unrolling, which will have unpredictable effect on performance, memory and Lx caches.  Lua or something more defined in semantic, could be better.

## zawy12 | 2018-05-31T17:17:37+00:00
Division should be the only problem and it can be solved by doing something like the following after each division.
``` if ( ceil( x + 0.001) > ceil(x - 0.001)) { x = ceil( x + 0.004); }```

I mean, if you aren't going to use more advanced functions.  You'd have to apply the above to every function like SQRT and whatnot.

## SChernykh | 2018-05-31T17:23:00+00:00
@zawy12 If only it was that simple... Just read this: https://gafferongames.com/post/floating_point_determinism/

## zawy12 | 2018-05-31T18:08:14+00:00
They are only talking about being exact to the same resolution of the float being declared.  I don't see anything suggesting my if statement is not always deterministic. To use it, you would not let a "double" go above 1 trillion so that compilers can be off as much as +/- 2 digits (a +/- 100x error)  in the least significant digits.  

You could just restrict your code to integer division.  I don't know if other complex math functions can be assured to be the same when performed on integers.  But they should be if the equation used is the exact same, and integer division at each step.

## SChernykh | 2018-05-31T18:17:32+00:00
In theory yes, but there are countless cases that can slip through fingers. For example, positive feedback loop that increases rounding error exponentially. This can happen in random generated code. Existing PoW/hash functions don't use floating point for a reason.

One more good article on the subject: https://randomascii.wordpress.com/2013/07/16/floating-point-determinism/

## zawy12 | 2018-05-31T18:32:12+00:00
I just remembered my code above is only for getting a deterministic integer output.  Off hand I can't think of a way to do it with floating point.  The protection would go hand-in-hand with any division or other problematic function, so if the problem function is in the loop, the correction would be too.  As I've said before, there's a lot of restrictions needed to make sure their random function idea to terminate at the correct time (the function does not merely need to terminate under some limit, but must stay within +/- 10% of a protocol-determined execution time if you want difficulty to be that accurate.  You could have wider limits by changing it every nonce so that the average execution time is what you plan for.  So it's far from random, which might open a door for ASICs.

Maybe this will work:
```if ( ceil( 100*(x + 0.001)) > ceil(100*(x - 0.001))  ) { x = ceil( 100*(x + 0.004))/1000; }  ```

## tevador | 2018-05-31T18:33:30+00:00
> One more concern is determinism. The same JS program/JS engine combo must produce exactly the same results on all supported platforms (x86, ARM), OSes and compilators in order to be used for hashing. It's very hard to achieve this, especially with floating point calculations enabled in generated programs.

Yes, this must be taken care of. However, the ECMA specification requires floating point math to conform to IEEE 754, which in turn requires bit-exact rounding for basic operations (+, -, *, /). Operations with inexact results (sqrt, log, exp, etc.) must be handled in code by rounding manually. We have to decide the required precision that is supported by most platforms (it's one of the parameters of the generator).

AFAIK there was [one bug](https://bugs.chromium.org/p/v8/issues/detail?id=436) in chrome related to floating point precision and it has been fixed. V8 now requires SSE2 support, which means it will not run on CPUs older than Pentium 4 or Athlon 64 (15+ years old CPUs).

> For example, positive feedback loop that increases rounding error exponentially. This can happen in random generated code. Existing PoW/hash functions don't use floating point for a reason.

This is not a problem as long as each intermediate result is correctly rounded (as required by IEEE 754). Then everybody will arrive at the same result (even if the value is "wrong" compared to a theoretical infinite precision case),

> Not only that, even future versions of the same engine (i.e. corrected for bugs or security issues), can change results

Yes, this can happen. I guess if we decide in the future to update the V8 version, we will have to scan the whole blockchain with the new version to see if everything validates. If not, both versions will have to be included and the switch will happen at a predetermined block height.

> I mean, if you aren't going to use more advanced functions. You'd have to apply the above to every function like SQRT and whatnot.

Currently I use this function in RandomJS:
```
function __prec(x) { return +x.toPrecision(__fpMathPrec); }
```
where `__fpMathPrec` is a constant (I tested with values between 10 and 14). The maximum precision of 64-bit float is 15-17 decimal digits.

## SChernykh | 2018-05-31T18:39:11+00:00
@tevador Does ECMA specification define a strict order of floating point operations for all cases? I'm thinking about compiler optimizations like a*b+a*c -> a*(b+c) which can change the result. Even if V8 engine applies it every time in the same way, different С++ compilers on different platforms will compile V8 and its floating point internals differently, giving unpredictable changes. So again, in theory it's all fine, IEEE-754 and ECMA standards are respected, but the actual tests are needed.

## tevador | 2018-05-31T20:13:42+00:00
@SChernykh 
IEEE 754, chapter 10.4

> A language standard should require that by default, when no optimizations are enabled and no alternate exception handling is enabled, language implementations preserve the literal meaning of the source code. That means that language implementations do not perform value-changing transformations that change the numerical results or the flags raised.
> A language implementation preserves the literal meaning of the source code by, for example:
> * Preserving the order of operations defined by explicit sequence or parenthesization.
> * Preserving the formats of explicit and implicit destinations.
> * Applying the properties of real numbers to floating-point expressions only when they preserve
> numerical results and flags raised:
>     - Applying the commutative law only to operations, such as addition and multiplication, for
> which neither the numerical values of the results, nor the representations of the results, depend
> on the order of the operands.
>     - Applying the associative or distributive laws only when they preserve numerical results and
> flags raised.
>     - Applying the identity laws (0 + x and 1 × x) only when they preserve numerical results and flags
> raised.

So I think it should be safe as long as some exotic compiler flags are not used (such as `-ffast-math` in GCC).

Anyways I agree that we need to test the algorithm carefully at least on the most common platforms..

## SChernykh | 2018-06-01T13:21:32+00:00
I've tweaked and fine-tuned my Cryptonight modifications, making them more robust and harder to crack for ASIC/FPGA. Also added some short description to README.md: https://github.com/SChernykh/xmr-stak-cpu 

## tevador | 2018-06-02T12:35:42+00:00
I tested RandomJS on a Raspberry PI (armv7l) and it gives the same hashes as the x64 platform (except it runs 10x slower than a Core i5 laptop, which is expected).

## baryluk | 2018-06-02T17:20:46+00:00
> A language standard should require ...

Notice the word SHOULD. It is not a guarantee. Nor there is mandate that the JS implementations follow this guideline either. (This is not a C or FORTRAN). I.e. it is common even for C programs to violate IEEE 754, for example by using FMA operation that often do have smaller errors than separate mul and add. In fact IEEE 754-2008 mandates to use single rounding in such situation, which is indirect violation of previous standard.


## hyc | 2018-06-02T17:37:47+00:00
ECMA spec says all numbers are IEEE 754-2008. It says that many functions in the Math library may return approximations, but it does not allow that for the standard arithmetic operators.

By the way, I've started looking at using MuJS instead of v8 - it's a smaller, simpler implementation. Might be more suitable for a reference implementation. https://artifex.com/mujs/

## hyc | 2018-06-02T17:39:58+00:00
Fwiw I'm not as optimistic as @tevador about using Math.* functions and manually rounding the results. We'd have to insert rounding statements at every invocation, to ensure deterministic roundoff error across implementations. Doable, but annoying.

## tevador | 2018-06-02T18:03:32+00:00
@baryluk Feel free to search for a platform which gives a different result: https://github.com/tevador/RandomJS/issues/3

> By the way, I've started looking at using MuJS instead of v8 - it's a smaller, simpler implementation. Might be more suitable for a reference implementation. https://artifex.com/mujs/

Is there a performance difference compared to the V8?

It seems to be only ES5 implementation, so it's unusable for my ES6 generator.

## zawy12 | 2018-06-04T08:45:01+00:00
> I'm thinking about compiler optimizations like ab+ac -> a*(b+c) which can change the result.

Good point. It seems something like my ciel() method is required. (and not only for divisions like I was thinking). Effort would need to be made to make sure the rounding is done very efficiently compared to the scope it's protecting or it would be a source of optimization.

## tevador | 2018-06-09T18:06:35+00:00
I have commited a draft of [RandomJS generator documentation](https://github.com/tevador/RandomJS/blob/master/doc/generator.md).

It would be best if someone could review it before I start implementing the generator in C++. I'm sure there is some room for improvements and I'd like to hear your comments.

BTW I'm planning to use [this Javascript interpreter](https://github.com/Moddable-OpenSource/moddable) for the reference implementation. It's a lot smaller than Chrome V8 and has (almost) full support of ES6 (it's a fork of the KinomaJS engine).

## SChernykh | 2018-06-09T18:16:27+00:00
Thanks, I'll have a look at the documentation.

That JS interpreter is rather new - first commit is from October, 2017 and there's a been a lot of active development in it. It may contain a lot of bugs. Did you test it for "hashing" compatibility with V8?

## tevador | 2018-06-09T18:33:26+00:00
@SChernykh  they cloned the engine from here: https://github.com/Kinoma/kinomajs
You can see it in issue 28 where one dev explains the original repo is no longer maintained. I'm not sure why they didn't keep the commit history, though.

I'm planning to compare the results to the V8 and also make some performance comparison.

## baryluk | 2018-06-09T22:58:37+00:00
So, if the generated code is used in a prototype, but the generated code doesn't actually use heavily any JavaScript related functionality (like libraries, prototypes, etc), there seems there is nothing stopping me to rewrite the prototype to generate an equivalent Lua code or Java bytecode that produces same result, and run it - faster, with less memory, etc. Am I right?



## baryluk | 2018-06-10T00:59:32+00:00
@tevador Oh, I see your EvalExpression with random content. That Is Evil.

## tevador | 2018-06-10T06:33:57+00:00
@baryluk Yes, there are two things that will make that approach harder:

1. The EvalExpression (with the default settings, there is about 60 of them in each program on average).
2. The hash of the reference source code is part of the PoW, so you have to generate it anyways.

## moneromooo-monero | 2018-06-10T09:00:29+00:00
> The remaining ~77% is a SyntaxError.

Does that mean that a miner might choose to always claim syntax error (IIRC returning just "SyntaxError" + thatstring) to avoid the load of procesing this eval, at the cost of 23% of the hashes being incorrect ? Whether it's a good choice depends on how much time that eval code takes compared to a typical whole hash.


## moneromooo-monero | 2018-06-10T09:04:23+00:00
Also, this PoW is actually *useful* beyond PoW as a large scale fuzzer for javascript implementations. I'm starting to like it a bit more now :)

## SChernykh | 2018-06-10T09:04:24+00:00
@moneromooo-monero An average random program does about 60 evals, so there is no way to avoid it.

In the meantime, some guys claim they achieved 14 KH/s @ 150 watts on FPGA for Cryptonight V1 and are going to send the first batch in August: https://bitcointalk.org/index.php?topic=3688965.0

## hyc | 2018-06-10T09:07:34+00:00
@moneromooo-monero considering that the original randprog was used as a fuzzer for C compilers, that's not surprising

## tevador | 2018-06-10T16:06:56+00:00
@moneromooo-monero 

> Does that mean that a miner might choose to always claim syntax error (IIRC returning just "SyntaxError" + thatstring) to avoid the load of procesing this eval, at the cost of 23% of the hashes being incorrect ? Whether it's a good choice depends on how much time that eval code takes compared to a typical whole hash.

I was aware of this strategy, that's why I tried to find a character set which produces the lowest possible amount of SyntaxErrors.

Anyways, your comment made me run the numbers. I tested a simple regex.Replace to turn all EvalExpressions into string literals as if they all produced a SyntaxError. Using the default generator options, about 61% of programs have the same output as with the original code and the optimized code runs ~36% faster.

So effectively, a solo miner would reduce their chance of finding a valid block by ~17% with this optimization (0.61 * 1.36 ~ 0.83). Pool miners would get banned by the pool because of ~39% of invalid shares.

Before, I was also thinking to include the whole error message in the output. It would completely eliminate this optimization, but it would also force everyone to use the reference engine (or an engine which produces the same error messages).

## baryluk | 2018-06-10T19:20:10+00:00
@tevador Could you dump somewhere (maybe into test vectors directory) sample of ~100 programs generated with input seeds and hashes, and timing distribution?

> The hash of the reference source code is part of the PoW, so you have to generate it anyways.

That is not a problem, just a minor slowdown.

AFAIK because the eval sees very simple strings, very simplified parser could be used, definitively not a full JS parser is needed. Also converting it into another language wouldn't be hard. I believe I could still implement equivalent Lua code, that would be able to process it.

What would be probably better is to:

1) rewrite the generator in the JS itself, or provide a JS function that calls back generator, so you can do `code2, hash_of_code2 = generator(some_seed, max_depth)`,  from the generated code dynamically, and then run it with `(new Eval(code2))(additional_input_to_generated_code)`. Where generator would generate recursively new code (possibly with more eval and generator calls, unless `max_depth <= 0`). some_seed would be some string or integer, that is coming from current level execution, and `max_depth` is `max_depth-1` current level. generated code should use both bunch of local variables and global variables (shared with all other levels), and global variables only shared with current level. Any given code generated would be called exactly once, and on each level between 0 and 2 calls to generator (with 0 at the last level), would be performed.

About 1), this still do not preclude me of doing Lua implementation actually. Even if I need to generate code twice, the implementation would be about 100 times smaller than full V8 engine.

2) To exercise parser even better, generated code should use more features, including comments and regular expression, as well array manipulations, including array methods.

3) Highly recursive calls would be interesting.

4) How many eval with different strings on average is there in a generated program? If it is something like 10+, then you cannot statistically make them all SyntaxErrors and be still correct.

I still the current implementation is way to heavy, and hacky. It poses multiple problems, portability, security, maintenance, hacky handling of integers/floats, ad-hoc additional of simple eval.

You can achieve all the same with Lua, plus it is much better defined, more portable to more operating systems and machine, and easier on verifier, i.e. mobile phones. Also you can easily run 30 Lua engines on one multi core machine, in single process, without big strain on memory and impact on other programs on the same machine.

## tevador | 2018-06-10T22:11:38+00:00
> Could you dump somewhere (maybe into test vectors directory) sample of ~100 programs generated with input seeds and hashes, and timing distribution?

For program generation:
`./Tevador.RandomJS.exe > sample_program.js`

For distribution of runtimes:
`./Tevador.RandomJS.Test.exe --count 10000 --verbose --threads 2`
(This will generate a histogram of runtimes.)

> That is not a problem, just a minor slowdown.

Program generation can be at least 5-10% of one hash. It means all optimizations will have a negative starting point.

>AFAIK because the eval sees very simple strings, very simplified parser could be used, definitively not a full JS parser is needed. Also converting it into another language wouldn't be hard. I believe I could still implement equivalent Lua code, that would be able to process it.

Yes, a full parser is not needed, but still it adds significant complexity if someone wanted to bypass the parser  and generate bytecode directly. Anyways, I challenge you to make a very simple parser that can handle all the random eval strings.

As for your points:

1. Interesting approach, but I think the generator would need to generate very simple code to meet the runtime targets.

> About 1), this still do not preclude me of doing Lua implementation actually. Even if I need to generate code twice, the implementation would be about 100 times smaller than full V8 engine.

The reference implementation will not use the V8. I'm testing a lightweight interpreter for it. Also what matters for mining is the performance, not size.

2. More features can certainly be added, but the problem is that all code paths must handle all types to keep the output entropy high, so adding more features will be harder and harder. Comments and regular expressions are already included in EvalExpression. If you manage to implement some additional features, you can make a pull request.

3. Recursive calls already happen. I debugged some programs where a function was passed to itself for a constructor call. These cases are quite common. You can test it by disabling call depth protection and you will see the programs crashing with call stack errors.

4. There are about 60 evals per program on average (default ProgramOptions). But not all of them affect the output of the program.

>I still the current implementation is way to heavy, and hacky. It poses multiple problems, portability, security, maintenance, hacky handling of integers/floats, ad-hoc additional of simple eval.

Portability seems good so far. I'm not aware of any security issues.  Can you elaborate about "hacky handling of integers/floats"?



## tevador | 2018-06-11T09:59:32+00:00
@moneromooo-monero 

> Also, this PoW is actually useful beyond PoW as a large scale fuzzer for javascript implementations. I'm starting to like it a bit more now :)

Yes, RandomJS already found [2 bugs](https://github.com/Moddable-OpenSource/moddable/issues) in the XS interpreter.

## SChernykh | 2018-06-11T15:03:15+00:00
@moneromooo-monero My latest and greatest shuffle modification: https://github.com/SChernykh/xmr-stak-cpu/commit/9169ef624250e8ab73ec362d7905abcb00ba91a4

Not only it takes advantage of 64-byte wide L1 cache accesses, it also takes advantage of L1 cache size. This one actually needs to be tested on GPUs, because it also makes 2 times more random memory accesses. GPUs have cache too, so I guess people will eventually figure out how to do it without losing performance.

P.S. CPUs are fine, I've already tested it: 2-2.5% slowdown only.
P.P.S. And it also makes use of the 4 least significant bits of the scratchpad index which were previously unused. Nice!

## Gingeropolous | 2018-06-11T16:21:16+00:00
@SChernykh , do u have a monerod and pool version of those mods for testing, or can I just run that miner on my GPUs to get hash results?

## SChernykh | 2018-06-11T16:24:57+00:00
No, just CPU miner for now. It's an early prototype, it needs testing and tweaking. And I also need to make a GPU version of all these modifications.

P.S. You just run it in benchmark mode to test performance.

## SChernykh | 2018-06-12T14:55:12+00:00
GPU version of shuffle and division modifications: https://github.com/SChernykh/xmr-stak-amd
I've tested it on GTX 1060 6 GB. Division modification doesn't slow it down at all. Shuffle modification slows down GPU a lot. It also forced me to lower intensity. Hashing speed is ~1.8 times slower at the same intensity and ~2 times slower comparing to the original Cryptonight running at max intensity. Maybe it's possible to fix this, but I don't know how at the moment.

@Gingeropolous @tevador @moneromooo-monero
Can anyone with AMD card test it? Just compile it, play with config.txt settings and run it.

## SChernykh | 2018-06-14T22:00:49+00:00
I found a way to squeeze two (!) integer square root calculations in addition to the division, without any troubles with rounding and without any additional slowdown! This starts to look very interesting, I'll test it on GPU tomorrow. Both division and square roots are good to fight ASIC because they are implemented on hardware level either as an iterative logic (slow, many clock cycles), or as a pipelined logic (fast, but occupies a lot of space on chip).

## moneromooo-monero | 2018-06-15T08:13:35+00:00
I asked hyc to have a look at what this does on ARM (some of them appear to be pretty good at hash/watt).

## SChernykh | 2018-06-15T09:15:56+00:00
I've added square roots to both CPU and GPU test repos, also updated the description:
https://github.com/SChernykh/xmr-stak-cpu
https://github.com/SChernykh/xmr-stak-amd

Feel free to test. My tests on Ivy Bridge and Skylake CPUs show 3% slowdown with one division and two square roots per iteration. No slowdown at all on GTX 1060! Awesome.

P.S. It will most likely kill the performance on ARMs which don't have out-of-order execution. And all energy efficient ARMs don't have it.
P.P.S. Only high performance ARMs like Cortex A72-A75 can handle it, but they're not so energy efficient and have relatively large die, comparing to other ARMs

## tevador | 2018-06-15T12:26:12+00:00
@SChernykh 
My results for AMD Radeon RX 550 on Ubuntu 16.04.

For reference, my cards make 480 H/s on cryptonight-v1 (latest xmr-stak) and never produce invalid hashes.

https://github.com/SChernykh/xmr-stak-amd
All tests with intensity 600, worksize 8.

||MATH_MOD OFF|MATH_MOD ON|
|-----|-----|----|
|__SHUFFLE_MOD OFF__|425 H/s|170 H/s|
|__SHUFFLE_MOD ON__|325 H/s *|130 H/s *|

 \* With SHUFFLE_MOD ON, the cards produce some invalid hashes. I tested 6 different cards and all produce invalid hashes for the same nonce values, so it looks like a bug in opencl code rather than hardware errors.

## SChernykh | 2018-06-15T12:28:41+00:00
@tevador Yes, CPU checking code doesn't have shuffle mod yet, don't pay attention to these messages. Is it really that bad for AMD cards? I saw no change in hashrate on GTX 1060, even though this was originally OpenCL code for AMD cards. I'll grab RX 560 from my friend for testing today.

## SChernykh | 2018-06-15T12:46:51+00:00
@tevador I've submitted shuffle mod for CPU checking code, you can pull and test again now. There shouldn't be any CPU/GPU mismatch errors anymore.

## tevador | 2018-06-15T12:48:11+00:00
Results for AMD Ryzen (1 thread) with https://github.com/SChernykh/xmr-stak-cpu

|Mode|Hashrate|
|-----|----|
|-|71.1 H/s|
|shuffle|69.3 H/s|
|shuffle+int_math|67.0 H/s|
|int_math|70.0 H/s|
|shuffle_with_lag|69.1 H/s|

Reproducible to within 0.1 H/s.

## SChernykh | 2018-06-15T12:50:18+00:00
So, it's confirmed now that shuffle and int_math mods can be handled fine by all modern CPUs. Ivy Bridge, Skylake and Ryzen tested so far. Nice.

## tevador | 2018-06-15T17:01:48+00:00
@SChernykh I was able to increse the hashrate of my RX 550 with the int_math mod to ~315 H/s by increasing the worksize. It's still a significant drop in performance, though (~25%).

This is with intensity 760 (highest possible) and worksize 32.

```
[2018-06-15 18:46:36] : Compiling code and initializing GPUs. This will take a while...
[2018-06-15 18:46:36] : Device 3 work size 32 / 256.
[2018-06-15 18:46:36] : clBuildProgram options: -I. -DWORKSIZE=32 -DINT_MATH_MOD
[2018-06-15 18:46:41] : Running a 20x10 second benchmark...
[2018-06-15 18:46:41] : Starting GPU thread, no affinity.
[2018-06-15 18:46:51] : Average = 264.9 H/S, Current = 264.9 H/S
[2018-06-15 18:47:01] : Average = 292.1 H/S, Current = 316.6 H/S
[2018-06-15 18:47:11] : Average = 291.0 H/S, Current = 288.3 H/S
[2018-06-15 18:47:21] : Average = 302.7 H/S, Current = 336.6 H/S
[2018-06-15 18:47:31] : Average = 304.0 H/S, Current = 310.2 H/S
[2018-06-15 18:47:41] : Average = 312.9 H/S, Current = 357.3 H/S
[2018-06-15 18:47:51] : Average = 313.6 H/S, Current = 317.5 H/S
[2018-06-15 18:48:01] : Average = 310.9 H/S, Current = 289.6 H/S
[2018-06-15 18:48:11] : Average = 313.9 H/S, Current = 336.7 H/S
[2018-06-15 18:48:21] : Average = 313.3 H/S, Current = 307.5 H/S
[2018-06-15 18:48:31] : Average = 317.1 H/S, Current = 354.4 H/S
[2018-06-15 18:48:41] : Average = 316.9 H/S, Current = 314.7 H/S
[2018-06-15 18:48:51] : Average = 314.5 H/S, Current = 283.7 H/S
[2018-06-15 18:49:01] : Average = 315.7 H/S, Current = 331.1 H/S
[2018-06-15 18:49:11] : Average = 315.1 H/S, Current = 304.8 H/S
[2018-06-15 18:49:21] : Average = 317.6 H/S, Current = 355.5 H/S
[2018-06-15 18:49:31] : Average = 317.5 H/S, Current = 315.8 H/S
[2018-06-15 18:49:41] : Average = 315.9 H/S, Current = 286.4 H/S
[2018-06-15 18:49:51] : Average = 317.0 H/S, Current = 334.9 H/S
[2018-06-15 18:50:01] : Average = 316.5 H/S, Current = 307.5 H/S
```

## SChernykh | 2018-06-15T17:06:31+00:00
@tevador I think it's just because RX 550 doesn't have enough computing power. Considering the fact that GTX 1060 works fine with the same hashrate. We need to test it on Vega 56/64. I'll also test it on RX 560 tomorrow.

## SChernykh | 2018-06-15T19:35:15+00:00
@tevador I've tested RX 560 on Windows 10: all stock, monitor plugged in, intensity 1000, worksize 32:

Mod|Hashrate
-----------|------------
\- | 379.9 H/s
INT_MATH_MOD | 383.1 H/s
SHUFFLE_MOD | 371.6 H/s
Both mods|350.9 H/s

I'll test on Linux and with no monitor plugged in tomorrow. But it already looks like that RX 550 is just too weak to handle all these divisions and square roots.

## zawy12 | 2018-06-15T22:39:22+00:00
I do not want anyone to interrupt the current thread, but I was thinking about my simple algorithm idea.  I previously said ASICs and GPUs present the problem of being able to implement many cores to do the simple calculations, but they are not as efficient in terms of electricity use.  Since electricity is half the cost in typical mining, ASICs and GPUs only provide a hardware-cost advantage, so they are a max of 2x more efficient.  But if many people have a miner as well as wallet running on their laptop, it's like zero hardware cost.  Besides that, I could do a POW that could make laptop or desktop burn 50 W above idle.  A 300 W GPU could only do 6x more calculations before getting too hot.  It can't use all its cores.  Same thing with ASICs.  So they should not have anything near the 2x advantage for these reasons, maybe a 2x disadvantage. 

If I write a simple POW that changes with every nonce to make my desktop run hot, can someone try to optimize it for use on a GPU to try to beat my hash per electricity costs?  Seems like my idea could be implemented and tested a lot quicker.  Like 1 day for someone who knows how to optimize a GPU.  That could be the starting point rather than CPU: how do you make a GPU core burn the most electricity with the simplest class iterative equations?  Is SQRT of a "random" seed enough to do it?   

The idea of intentionally trying to burn the most electricity may have prevented this route from being investigated for "moral" reasons, but as I described before, it's not really different than a hard-expensive route.

## SChernykh | 2018-06-16T07:07:27+00:00
@zawy12 They (ASICs) are very efficient in terms of performance/watt.
> how do you make a GPU core burn the most electricity with the simplest class iterative equations? Is SQRT of a "random" seed enough to do it?

Just look at what LinX test does. It burns CPUs like hell. Lots of floating point math, AVX instructions. But I'm not sure it can be used for hashing.

Basically, you need to run as many FMA (multiply and add) instructions per clock cycle as possible. The closer you get to the theoretical FLOPs limit of the device, the better.

## zawy12 | 2018-06-16T08:47:50+00:00
@SChernykh What do you think of my general idea and reasoning?  That since electricity is half the cost, and this is so simple, that it's probably a good route to follow?

## zawy12 | 2018-06-16T09:03:18+00:00
@SChernykh 
>But I'm not sure it can be used for hashing.

A hash of the (nonce + previous block hash) would be the seed for the simple N=10,000(?) loop that is required in order to get an output nonce upon which the real hash is performed.  Validation would repeat the process.

The extreme idea of changing every nonce is more than synergistic with the idea of making the algo simple but iterative.  It's so simple it might cause disbelief, but I can't find an error with it.

I think the loop should require 10x more computation than the 2 hashes, so fast hashing provides minor benefit, and the 10x loop as opposed to 100x loop would not not be a burden to validate, although as far as I know 100x is not be a big burden either.

## tevador | 2018-06-16T10:04:03+00:00
Final results for RX 550 (with 10 compute units).

|Mode|Intensity/Worksize|Hashrate|
|-----|----|----|
|-|600/8|425 H/s|
|shuffle|760/16|380 H/s|
|int_math|760/32|315 H/s|
|shuffle+int_math|760/32|255 H/s|

Hashrate is rounded to multiples of 5 H/s due to fluctuations.

There are also RX 550s with just 8 compute units which will fare even worse.

## tevador | 2018-06-16T10:54:30+00:00
@zawy12 The problem is that with these static compute-intensive workloads, an ASIC will be always more efficient than general-purpose hardware.

## moneromooo-monero | 2018-06-16T10:54:36+00:00
Is anyone familiar enough with ASIC design to estimate what impact having to add div and/or sqrt hardware might have on the performance and cost ?

## SChernykh | 2018-06-16T11:34:19+00:00
@moneromooo-monero I've spent the last few days learning how FPGAs/ASICs work and how divisions and square roots are implemented in hardware. They're iterative algorithms with high execution latency - something that current Cryptonight lacks. The whole Cryptonight inner loop can be implemented in 1 cycle per iteration. Division and square root logic take more logical elements each (space on chip) than everything else in the loop, and they bring latency. The loop must be unrolled and pipelined many times more to hide this latency (space on chip x15-x20), and of course it will require many times more parallel scratchpads to feed all this logic (won't fit in on-chip memory).

I'm not a hardware designer though. We had @cloudHH and @rufus210 giving valuable feedback in Cryptonight V1 discussion:
https://github.com/monero-project/monero/pull/3253#issuecomment-366142870
https://github.com/monero-project/monero/pull/3253#issuecomment-367946170

## zawy12 | 2018-06-16T11:36:03+00:00
The algorithms for simple math should be already optimized for a given 64 bit-width and I don't think it can be improved upon by going to wider channels.  They could create a massive number of miniature CPUs that do only with the simple operations, but they still have to go through the same number of physical transistor state-change operations (think FLOPs) which means the same amount of electricity usage (or more for reasons I mentioned).  

It may have to be a single operation, or a sequence of a kind of wide range of operations.  If only 4 operations were used as I originally said, they could dedicate "simplified CPUs" to each of the 3^4 possible sequences of 3 operations.  A sequence of 3 operations may have an optimization superior to a CPU only optimized for each of them individually.  

But if a single operation is used, there might be a a known optimization that uses a huge lookup table to replace calculations that would not be feasible for generic CPUs.

## SChernykh | 2018-06-16T11:42:57+00:00
@zawy12 Every single computational-intensive algorithm so far has failed to resist ASICs. Take away instruction fetch and decoders, caches, out-of-order execution logic, branch prediction etc. from CPU, leave only the math and you'll get 10x more hashes per watt.

## zawy12 | 2018-06-16T11:45:36+00:00
@SChernykh that's only because the algos are not changing every nonce.  [edit: or they were complicated enough to be optimizable]

## SChernykh | 2018-06-16T11:48:47+00:00
But random generated code PoW is already being developed? Not for the next fork, but it'll eventually be ready.

## SChernykh | 2018-06-16T11:50:48+00:00
> If only 4 operations were used as I originally said, they could dedicate "simplified CPUs" to each of the 3^4 possible sequences of 3 operations. A sequence of 3 operations may have an optimization superior to a CPU only optimized for each of them individually.

This is where you're wrong. They only need to implement each operation once, the sequencing logic is very simple in hardware.

## zawy12 | 2018-06-16T11:53:42+00:00
All the things you mentioned are not used by CPUs on simple algorithm, so CPUs will not be expending electricity or time on them.  I'm saying it may not be necessary to use such a wide instruction set or a big algorithm, so there is less likely to be an error or unforeseen optimization.  I don't follow your last post.  It sounds like you're agreeing with me. 

## SChernykh | 2018-06-16T11:55:43+00:00
@zawy12 ASIC doesn't need to have 3^4 simplified CPUs for each possible sequence. Just 3 simplified CPUs and very simple interconnect logic that gets the order of operations as an input.

## zawy12 | 2018-06-16T12:05:30+00:00
But that does not reduce the number state changes necessary to get the answer so the amount of electricity burned should be the same. With the simple math big or small cache (let alone RAM) or speed of getting the next instruction should not help or hurt.  There's no instruction fetch / prediction optimization possible. It should all be in a small amount of cache close to the CPU and not changing sequence until the next nonce fetch which is small amount of time required compared to the iterative calculating.

## SChernykh | 2018-06-16T12:21:20+00:00
@zawy12 You underestimate how much all the complex CPU logic consume. If you run LinX on a modern CPU, you'll get something around 400 GFLOPs at 150 watts at best, so ~2.67 GFLOP/watt. GTX 1080 ti can do 12000 GFLOPs at 300 watts, so 40 GFLOP/watt. An order of magnitude better. ASIC will be one more order of magnitude better.

## zawy12 | 2018-06-16T15:56:04+00:00
That's after the GPU has been optimized for the algorithm.CPUs were competitive with GPUs on Zcash for a few weeks after launch on a hash/kWh basis because the GPU devs had not yet figured out how to optimize, despite having 6 months lead time.   If by "Linx" you mean the coin with a POW, I assume that POW is complicated and therefore optimizable, so not related to what I'm talking about.    We're talking about changing the algorithm every nonce so that this can't happen.  I think the only difference in what's being attempted and what I'm saying is that a much simpler instruction set is possible, and it makes me wonder if a single instruction in a long loop is possible by virtue of it already being optimized.

## SChernykh | 2018-06-16T16:06:44+00:00
By LinX I mean CPU stress test program: https://linx.en.lo4d.com/
It's based on Intel LINPACK software.

## zawy12 | 2018-06-16T17:04:17+00:00
GPU software has been optimized for LinPack because it is a narrow but popular engineering problem that lends itself to optimization. It seems to be memory-heavy which is the opposite direction of what I'm saying.  There must have been a lot of optimization in that direction because in about 2010 nvidia said only a 3.5x gain (verses your 15x) when they added 60% more hardware cost in GPUs to a CPU.   http://www.nvidia.com/content/pdf/sc_2010/theater/phillips_sc10.pdf

## SChernykh | 2018-06-16T17:15:05+00:00
@tevador I've tested RX 560 on Ubuntu 18.04 with latest drivers (having monitor plugged or unplugged didn't change anything):

Mod|Hashrate
-----------|------------
\-|379.8 H/s
INT_MATH_MOD|378.7 H/s
SHUFFLE_MOD|374.7 H/s
Both mods\*|336.3 H/s

\* I noticed that with both mods turned on, it does 445 H/s for the first minute, then drops to 310 H/s. Maybe the card is overheating and drops frequencies?

@zawy12 I still need to see detailed algorithm description to understand how it can prevent ASICs from being more energy efficient.

## SChernykh | 2018-06-17T09:08:49+00:00
@tevador I did some more testing with RX 560 downclocked to 595 MHz on core to simulate performance of RX 550. I also tested various combinations of division and square roots:

Mod|Hashrate
-----------|------------
\-|359.1 H/s
DIV+52-bit SQRTx2|261.4 H/s
DIV+52-bit SQRT|288.3 H/s
DIV|356.7 H/s
DIV+24-bit SQRTx4|360.0 H/s

It appears that double precision square roots are the main bottleneck. Single precision square roots, even when I combine 4 of them with division, don't slow it down at all. So next step is to try implement efficient code to calculate 52-bit integer square root for GPU. Using double precision floats for this is definitely not the best way. And we need 52-bit square root only, because it has the highest latency when implemented in hardware. 24-bit square roots won't do the trick.

## tevador | 2018-06-17T13:52:03+00:00
@SChernykh Just 26-bit precision is needed to calculate integer square root of a 52-bit integer. That means a single precision result (24-bit significand) will be accurate ±4.

You can take the single precision result and perform a single Newton-Raphson iteration to increase the precision to ~48 bits:

```c++
//calculates square root with ~48-bit precision using only 
//single precision square root and 4 double precision multiplications
double sqrt_interpolated(uint64_t x) {
	double xd = (double)x;

	//reciprocal square root
	double rsd = 1.0f / sqrt((float)x);

	//one iteration of Newton-Raphson
	rsd = rsd / 2 * (3 - xd * rsd * rsd);

	return xd * rsd; //sqrt(x) = x * 1/sqrt(x)
}
```
The reciprocal square root costs nothing because GPUs usually implement it in hardware (so no division is needed). For AMD Polaris, this is the `V_RSQ_F32` instruction.

I don't know if 4 DP multiplications can be faster than a DP square root. In any case, I'm sure this method can still be improved because we don't need 48-bit precision, just 26 bits (the rest is truncated anyways).

## SChernykh | 2018-06-17T14:54:44+00:00
@tevador One more division to calculate square doesn't improve performance, I've tried it.

> That means a single precision result (24-bit significand) will be accurate ±4.

You are absolutely right. I managed to get a slight improvement from 260 to 285 H/s by calculating single precision square root, subtracting 8 from it and then adding 8, 4, 2, 1 when needed. So this code can handle errors in the range [-7; +8]. The "when needed" logic takes 8 single precision multiplications and 4 conditional moves. I'll experiment some more and then submit this optimized code.

## SChernykh | 2018-06-17T17:27:57+00:00
@tevador After some more experimenting, I decided to reduce square root size to 48 bits (still large enough), so error will be -1 or +1 which simplifies code a lot. Submitted it: https://github.com/SChernykh/xmr-stak-amd/commit/aa01b78edf6fd09bda4c42173b20cd70df0a0f83

Tested it again on RX 560:
- CPU checks turned off to reduce fluctuations in hashrate
- Monitor unplugged
- Core clock set to 595 MHz to emulate RX 550 performance

Version|Hashrate
--------|----------
No mods|360 H/s
old sqrt code|265 H/s
new sqrt code|315 H/s

It's much better now even for low-end GPUs.

## zawy12 | 2018-06-17T17:47:18+00:00
@SChernykh It was a bit harder than I expected, but I didn't think it would only take a day to implement.  For the current  settings in the program below, my computer went from 28 Watts standby to 117 Watts.  12 threads seem more efficient than 8.  At 12 threads, it went through each loop (a hash) in 9.5 seconds.   I have it set to many iterations for a single hash because in early testing this was more likely to expose an error by crashing.   

So, I get  12/9.5/(117-28) = 0.014 H/s per watt.   The loop is set to 2 M iterations.  In a coin I guess 2 k iterations is closer to what it should be to make it 14 H/s per watt on my CPU.  This is my CPU:

```
Intel(R) Core(TM) i7-2600 CPU @ 3.40GHz
4 core, 8 T, 8051 
RAM (supposedly not relevant to this algo)	
Size: 4096 MB
Speed: 1333 MHz
Size: 4096 MB
Speed: 1333 MHz
```  
The lithographic line resolution is 32 nm. If you test it, let me know what your GPU is. My guess is that it's a linear, but if it is squared a 14 nm RX 560 doing 4x better on this algo is not really doing better because of my older chip technology.

This C++ POW program uses 11 math functions in seed-generated "random" sequence of 22 operations.  Each is used exactly twice. The code to select the sequence from the seed and to use them exactly twice was the hard part. This gives  (11!)^2 = 1E15 possible algorithms The inputs to each math function are scaled to be in a good range for that function, where you have to actually use the function to get the answer.  The output from each function drops the high digits before the next function, so there's no way to optimize the calculations via mathematical reduction.  

The sequence of 22 operations is repeated many times, using the output of the previous iteration as the input to the next, so the H/s difficulty is easily scaled and not cheatable.  At every step, I throw away the low digits in my doubles, so presumably there's no problem from differences in doubles.

https://github.com/zawy12/Proof-of-Work

For multiplication, I multiplied the high 6 digits times the low 6 digits. The seed, input and output of each function, and the final output is a 12 digit integer.  Hash that ouput to see if you are below the difficulty target.  

[edit here are the relative speeds for the 11 functions] 
**[edit ignore this.  subsequent post has much better measurements per operation]**
```
	if	( seq == 1 )	{ k = 1/k; }			// Speeds: 52
	else if	( seq == 2 )	{ k=(k*10)/1e12+1; k = log(k); } // 142
	else if	( seq == 3 )	{ k = sqrt(k);  }		// 54
	else if	( seq == 4 )	{ k=(10*k)/1e12; k = exp(k); } 	// 133
	else if	( seq == 5 )	{ k = sin(k)+1.01; }		// 150
	else if	( seq == 6 )	{ k=k/1e12; k = asin(k); }	// 86 +/- 5
	else if	( seq == 7 )	{ k=(10*k)/1e12; k = sinh(k); }	// 112
	else if	( seq == 8 )	{ k=(10*k)/1e12; k = asinh(k); }// 157
	else if	( seq == 9 )	{ k=(1.2*k)/1e12; k = erf(k); }	// 78
	else if	( seq == 10 )	{ k=k/1e12; k = tgamma(k); } 	// 217
	else if	( seq == 11 )   { k = multiply(k); }   		//  75
```

## SChernykh | 2018-06-17T17:54:21+00:00
@zawy12 I'm done and exhausted for today, I've spent the whole day with this square root code. Will check it tomorrow.

## SChernykh | 2018-06-17T20:09:15+00:00
@zawy12 Ok, I took some time to look at the code.
- To get a random shuffle where each function repeats exactly 2 times, first fill it like this: (F1, F1, F2, F2, ..., F11, F11) then do https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle - very simple and correct random permutation algorithm.
- Calling sin(k) with k~=1e12 is a very bad idea. The result is very implementation dependent.
- Multiply and extract digits functions can be optimized drastically
- All if ... else can be removed, select_and_do_operation fully inlined if we generate assembly code on the fly before the main PoW loop
- Overall performance improvement will be small though because most time will be spent in trigonometric functions.

ASIC/FPGA will still be an order of magnitude better in terms H/s per watt. They're not bad in floating point, quite the contrary. People spent decades optimizing trigonometric and math functions for DSP processors.

P.S. The number of different sequences will be 22!/2^11 ~ 5.49*10^17

## zawy12 | 2018-06-17T20:22:26+00:00
@SChernykh I edited the post above to include relative solvetimes.  The trig functions were medium speed.  I edited the sin function to be in the 0 to about 2\*pi range.  This is for demonstration purposes of the general and my curiosity as to if a GPU can do better on this. Other operations can be selected to target CPUs, GPUs, or cell phones.  Also, the 11 functions can be changed to a variety of things, so ASICs would have to target a single coin.  

I would think on-board math co-processers have the same DSP technology.  Why would an ASIC or FPGA be better at floating point than CPU math co-processors for the simplest functions?

## zawy12 | 2018-06-17T20:26:00+00:00
I can't use the Yates shuffle you recommended because it has to be deterministic for validation.  Also, it has to be from the sha256 (nonce + previous block hash) so that nonces can't be selected in order to cherry pick a specific algorithm that an ASIC or FPGA could be be optimized for.  

## hyc | 2018-06-17T20:28:54+00:00
Trig functions now tend to be all driven by lookup tables. All quite fast, single-cycle lookups typical.

## SChernykh | 2018-06-17T20:31:09+00:00
> Why would an ASIC or FPGA be better at floating point than CPU math co-processors for the simplest functions?

Because they can have _more_ floating point logic instead of all stuff they don't need, but CPU needs. Caches, branch predictors, instruction decoding etc. They can pipeline all math functions so that they can have throughput of 1 input value per clock cycle. CPUs and GPUs don't do this, they always have latency. For example, one SIN logic block in ASIC has latency of 50 cycles (just a ballpark number), but it can be used in 50 different nonce loops at the same time.

Yates shuffle is deterministic. Random generator can start with seed generated from the previous block hash.

@hyc Lookup tables for double precision? No way.

Lookup table to get 10 bits of result (at best) and then a few iterations of Taylor series to get the exact result - maybe.

## zawy12 | 2018-06-17T20:51:28+00:00
@SChernykh ASIC's seem to require knowing the algorithm ahead of time in order to coordinate the use of the SIN block in that manner.  It should have more state changes to do what you've described, proportional to it's increased usage. So it sounds like you're describing a more efficient use of logic block space than its electrical usage.  

Part of the idea is to make the algorithm simple enough so that the CPU does not need an overhead of branch prediction, excessive cache use, or instruction decoding.  I have no idea how to get code "close to the CPU" and satisfy my other goals, so I've just done what I can in selecting math functions.  It would take an assembly language / CPU expert to really optimize for the CPU.  But my scheme should be easy for a GPU expert to optimize for GPUs, and all the better if he knows of things to avoid to reduce the threat of ASICs.

[edit: there were massive inefficiencies in my code...working on it.  The functions are like 20x faster than the code implied.  Strange things too, like calling a simple function taking 10x longer than putting it in the loop....c++ compiling seems very dumb. ]

## SChernykh | 2018-06-18T09:28:09+00:00
@tevador Apparently the optimized code doesn't work on NVIDIA GPUs because they cut some corners when calculating SQRT and the resulting error is larger. I've submitted a fix and also added a new parameter to test different SQRT code versions.

@zawy12 Once more, ASICs can handle random order without any problems. They only need to implement each function and then add logic to process these function in given order. This logic is very simple. Even if CPU doesn't use some functional blocks when running it, they will still consume power, so ASICs will be much more efficient.

P.S. NVIDIA OpenCL compiler uses sqrt.approx instruction instead of proper sqrt.rn instruction which NVIDIA CUDA compiler uses, weird. Anyway, it gives error in the range [-2; +2] in OpenCL code, but should be fine in CUDA code.

## baryluk | 2018-06-18T13:19:47+00:00
@zawy12 Unless sequence of operations is different in every loop, ASIC and FPGA  could easily be reconfigured rapidly to do a pipelined routing between operations using semi static configuration. The same can be done for CPU, to remove almost all branching from the code. It will be at least 30 times more efficient than CPU or GPU. Even just running such code trough very fast optimized compiler for DSP will result in extremely high efficiency (easily 10 times more efficient than CPU). And it will be faster than compiling a GPU kernel and uploading it to GPU.

It is easy to design an flexible ASIC that will process 1 hash round per cycle, by using multiple function units, long input queues to units with long delays, and extreme levels of multithreading (i.e. tag all data with 10 bit id, and state would be id + current loop position and sequence operation,  60 bit total). You can easily do 1000 states in parallel, and hide all latency of operations and interconnects, at almost zero power.

> I can't use the Yates shuffle you recommended because it has to be deterministic for validation.

It is deterministic. It produces deterministic shuffles. What is the problem?

## zawy12 | 2018-06-18T18:20:29+00:00
@baryluk Schernykh explained it can be determininstic, but my method is "only" about 5x slower and outside the main loop, so I haven't worked on it.

@SChernykh and @baryluk Does it require an ASIC to clearly "beat my method" or is there a way a GPU can do something like an ASIC that a CPU can't do.  How will it compare in hashes/sec/watt to my CPU if someone runs 50 or 100 threads on a GPU?

Is there is a fundamental difference between my method and trevador's other than scale? If I had 1000 different functions in a sequence of 1000 would it still be impractical for an ASIC?  If not, then is there anything an ASIC can't beat with this "easy" rescheduling you've described for random algorithm? 

I made several obvious speed improvements not related to the math and made the math more difficult. Now 8 threads is the max.  With 100,000 iterations, a hash is completed at 0.7 per second per watt.   

FWIW, here are the solvetimes per function. The erf(k), sqrt(k), and 1/k functions were 15x faster than the others, so I removed them.
```
		if ( seq == 1 )         { k = pow(k,5.123); }   // 60 ns
		else if ( seq == 2 )    { k = log(k); }   // 80 ns
		else if	( seq == 3 )	{ k = exp(k*1e-11); } // 72 ns
		else if	( seq == 4 )	{ k = sin(k*6.28e-12)+1.01; } // 70 ns
		else if	( seq == 5 )	{ k = asin(k*1e-12); } // 30 ns
		else if	( seq == 6 )	{ k = sinh(k*1e-11); } // 55 ns
		else if	( seq == 7 )	{ k = asinh(k*1e-12); } // 53 ns
		else if	( seq == 8 )	{ k = 1/erf(0.001*sqrt(sqrt(k))); } // 40 ns
```

The following inner loop did not slow it up more than 10%.  I mean this:
```

for ( 1 iteration ) {
   for (function = 1; function <= 16; function++) { 
        // insert the above if statements here 
        k = extract_12_digits(k); // 20 ns
   }
}
``` 
was not hardly slower than this
```
for ( 16 iterations) {
    k = sinh(k*1e-11);  
    k = extract_12_digits(k);
}
```
Distributions were random.

## SChernykh | 2018-06-18T19:28:02+00:00
> Is there is a fundamental difference between my method and trevador's other than scale?

Yes. Turing completeness. Your code doesn't have loops, conditional operators, memory use etc. RandomJS is Turing complete (i.e. it can in theory generate a code that implements any possible algorithm) and you need a full blown CPU to calculate the hash of it. Everything simple, even if it's 1000 different functions, is still prone to ASIC optimizations.

## zawy12 | 2018-06-18T20:21:13+00:00
The output is fed back into the input, so it has a loop.  It has conditional operators,  and memory to do use these things.  The input here is 1e9 possible programs with 1e12 possible outputs.   Trevador's is more complicated but does not seem fundamentally different.  It's not changing the program after the seed and it has a deterministic output.  It has a larger choice of functions (made up of a much smaller set of functional blocks that could be hardware), and more options for how the functional blocks interact.  Obviously it would be harder to schedule the pipeline and come up with optimized functional blocks, so I could work up from the bottom to go towards his complexity.  I think working up in complexity rather than coming down is able to isolate and fix bugs easier.

## SChernykh | 2018-06-18T20:34:25+00:00
You didn't quite understand. Your main loop is a sequence of M fixed functions repeated N times. There is no conditional operators, additional loops or arbitrary amount of memory used inside. @tevador's code changes with every nonce too. "just seems to have a larger choice of functions" and "more options for how the functional blocks interact" is what makes it Turing complete. Quantity becomes quality.

## zawy12 | 2018-06-18T20:57:57+00:00
My algorithm changes with every nonce. I could change it unpredictably during the nonce too, thanks to the loop. That could lead to more complex conditional operators and a changing memory size if it needs to.  Do you have any other requirements?   You're saying my 8-tree forest is too simple and thereby vulnerable.  I can add biodiversity with flowers and insects.   

Turing complete can be done with a few NAND gates (a single function that can also implement memory).   Single-instruction Turing complete computers exist.

## SChernykh | 2018-06-18T21:50:10+00:00
And you don't understand the whole point about Turing completeness. Imagine we switched to RandomJS PoW and there is an ASIC that can do it 10 times more efficient than CPU. What does it mean? That we have a device that can run _any_ code 10 times more efficient than existing CPUs. In essence, it will just be a new generation CPU that Intel and AMD will replicate and start mass producing as soon as possible to stay up to date and not loose their market share. Back to square one where ASICs don't have any advantages over CPUs.

P.S. ASIC that can run any code is a CPU by definition. Do you see the point?

## zawy12 | 2018-06-18T22:51:14+00:00
That's a good point. That's why I thought to target the math co processor. If Asics can do better, then they would be our math co-processors.  

Backing up a little, Asics aren't specifically my goal, but to have a scheme where GPUs can't be modifiable to be 5x or 10x better a year from now on a new POW. That's been a problem nearly as big as asics  in my view. So I imagine small coins using different schemes of the simpler approach as the primary defense against Asics, not necessarily taking them on directly. 

## zawy12 | 2018-06-19T09:23:17+00:00
A reverse goal could be to use my scheme to target an off-the-shelf math ASIC.  This one with 1024 cores (not a commercial success, so it does not appear to be "off-the shelf") gets 4x more FLOPS/watt than Nvidia's P100 using the same 16nmFF process.  Their cost analysis is interesting.

https://www.parallella.org/wp-content/uploads/2016/10/e5_1024core_soc.pdf

I'm modifying it to change the algorithm every iteration instead of each nonce.

## zawy12 | 2018-06-19T11:27:07+00:00
All the Monero clones are using my LWMA difficulty algorithm (now LWMA-2), so if someone comes up with a good POW, let me know and I can get Monero clones to try it so that bigger coins have a preliminary test the wild.  

I'll not post about my idea in this thread anymore, but move it to [my own Github issue.](https://github.com/zawy12/Proof-of-Work/issues/1)  Each idea should be moved to a new issue and someone can recommend I close this issue. You can't link directly to comments in Github issues when they get this long and at least my Github app can't scroll down very well.

Here's the general random POW procedure I'll continue explore.  "function" can be any valid program that has a standard output type (I've chosen doubles and math functions for now).

```
// coin defines it own functions
myhash = ffx32;
while (myhash >= target) {
   nonce++;
   h =  sha256( "previous_block_hash" + "nonce");
   seed = get_seed ( h )
   for (1 to 10,000)  { 
       sequence = extract_sequence_of_functions( seed )
       for (1 to N_functions) { 
           seed = execute_function( seed );
           seed = normalize_seed_to_safe_input_form( seed );
       }
   }
   myhash = hash(seed)
}
claim my block;
```
Correction:  I may need to make it a restricted to NAND gate via ```unless ( a > b || c > d) { }```  The end of each block can't be limited to its own iteration so I can't ensure it finishes without a timer or counter to decide when to exit out at least 1 block level.

## moneromooo-monero | 2018-06-20T09:50:42+00:00
I'd rather this bug stays open for other people to propose other things. In depth discussion about particular approaches can certainly be moved to their own entry if needed.

## SChernykh | 2018-06-20T10:22:43+00:00
Please discuss my proposed modifications here: https://github.com/SChernykh/xmr-stak-cpu/issues/1

## tevador | 2018-06-20T12:15:39+00:00
Discussion about RandomJS can continue here: https://github.com/tevador/RandomJS/issues

## zawy12 | 2018-06-20T14:21:50+00:00
This is an idea to generate random code that doesn't unexpectedly halt or get stuck in a loop.  To produce the most wide-ranging code per byte (highest entropy), a Turing-complete logic gate (or intel's mov instruction) by itself is required, but most cases halt or loop.  This might generate more random code per byte than a full language generator, but that does not mean it would max out a CPU better:  redundancies in languages and CPUs are optimized for human-useful problems whereas this explores a wider range of fundamental logic.

As shown, it's not useful because the "operation construction" would take longer than it's output.   Just calling an empty routine takes longer than an if statement.   Not to mention the delays caused by calling a timer that often.  If not a distinct number of loops to replace that part, then maybe _while (seed > some_target)_. 

It could accidentally produce a SQRT() or Hamlet in ASCII, but it's so unlikely it will never happen.  It eliminates redundancies in a full language.  For example, **if ( a > b)** is same as **if (b < a)** and **unless ( a < b)** and **unless ( b > a)** and then all the variants with **not**.  So I will use only **>** so their are none of these type duplications.  I can't use == because it almost always will not be true, but it can produce that outcome if two "if" statements in a row included 1+ and > correctly.   

I have not (yet) included a method for passing data down more than 1 layer. I do not see a way to usefully include complex data structures or pointers.

```
myhash = ffx32;
while (myhash >= target) {
   nonce++;
   h =  sha256 ( "previous_block_hash" + "nonce");
   seed = get_seed ( h );
   while (timer < 1)  { 
       get_for_or_if_with_data_type ( seed );
       get_object_data_and_type ( seed ); 
       get_action_to_perform_on_data_and_loop_var (seed ); // very simple
       seed = perform_conditional_and_action_on_object_data ( );
   }
   myhash = sha256(seed)
}
claim_my_ block();
```
[edit:  I may need to make the "if" statement option a NAND gate ```unless ( a > b || c >d)``` and I can't let blocks always terminate in the same iteration in order to be Turing complete, so I have to have a counter to limit sub blocks and/or terminate inelegantly. ]

## SChernykh | 2018-06-20T18:41:39+00:00
@tevador Can you please test my mods on your RX 550 again? I've fixed fluctuations in reported hashrate on GPU, it's much more stable now.

## MoneroCrusher | 2018-06-22T21:46:02+00:00
@SChernykh
Can you provide me a linux binary? I'll test it. I have an RX 550 with 8 CUs as well as 10 CUs
Doing 505 stable CN7 on both.

## SChernykh | 2018-06-23T06:05:26+00:00
@MoneroCrusher source code is here: https://github.com/SChernykh/xmr-stak-amd
Then do this to get the binary:
```
sudo apt-get install ocl-icd-opencl-dev libmicrohttpd-dev libssl-dev cmake build-essential	
cmake .	
make
```

You'll have to overclock GPU core as much as possible to get better hashrates with mods. RX 550 is very weak for them, but RX 560 and better cards are good enough.

P.S. Don't expect to get 505 H/s even without mods with this code. It's an old xmr-stak-amd code without the latest strided_index and mem_chunk tweaking parameters.

## MoneroCrusher | 2018-06-23T11:28:49+00:00
If both shuffle and integer are false, is sqrt_opt_level ignored? Meaning it's 100% normal xmr-stak-amd?Tested both RX 550 with 8 CUs and 10 CUs with 2 threads at 432 intensity in Ubuntu 16.04 Server:

**Sapphire RX 550 2GB 8 CU: 1970mckl/1270 sckl**

Version (Square root 2) | Hashrate | System Power Draw (wall)
-- | -- | --
xmr-stak 2.4.3 | 500 H/s | 70W
test_shuffle = false, test_int_math = false, sqrt_opt_level = 2 | 465.4 H/s | 66W
test_shuffle = true, test_int_math = false, sqrt_opt_level = 2 | 384.5 H/s | 70W
test_shuffle = false, test_int_math = true, sqrt_opt_level = 2 | 230.3 H/s | 60W
test_shuffle = true, test_int_math = true, sqrt_opt_level = 2 | 201.0 H/s | 64W

**Gigabyte RX 550 2GB 8 CU: 2150mckl/1220sckl**

Version (Square root 2) | Hashrate | System Power Draw (wall)
-- | -- | --
xmr-stak 2.4.3 | 504.2 H/s | 72W
###FIRST 2 MINUTES: 
test_shuffle = false, test_int_math = false, sqrt_opt_level = 2 | 471.2 H/s | 67W
###THEN "CPU/GPU mismatch at nonce 23443!!!" 
test_shuffle = false, test_int_math = false, sqrt_opt_level = 2 | 508.8 H/s | 67W
MANY "CPU/GPU mismatch errors", hashrate didnt change, test_shuffle = true, test_int_math = false, sqrt_opt_level = 2 | 375.5 H/s | 72W
test_shuffle = false, test_int_math = true, sqrt_opt_level =  2 | 221.3 H/s | 63W
test_shuffle = true, test_int_math = true, sqrt_opt_level = 2 | 192.5 H/s | 66W

**Sapphire RX 550 2GB 10 CU: 2100mckl/1170 sckl**

Version (Square root 2) | Hashrate | System Power Draw (wall)
-- | -- | --
xmr-stak 2.4.3 | 519.1 H/s | 73W
test_shuffle = false, test_int_math = false, sqrt_opt_level = 2 | 528.5 H/s | 68W
test_shuffle = true, test_int_math = false, sqrt_opt_level = 2 | 377.5 H/s | 71W
test_shuffle = false, test_int_math = true, sqrt_opt_level = 2 | 225.4 H/s | 63W
test_shuffle = true, test_int_math = true, sqrt_opt_level = 2 | 196.1 H/s | 66W

wow...ill use the old xmr stak amd from now on for the baffin based RX 550.

So which of these results would be planned to be implemented?

I think it's important to equalize GPU/CPU somehow or even tweak it in such a way that GPUs are favoured. Botnets would become a big problem if it's implemented as is.

## SChernykh | 2018-06-23T11:50:56+00:00
It's better to move the discussion here: https://github.com/SChernykh/xmr-stak-cpu/issues/1

> If both shuffle and integer are false, is sqrt_opt_level ignored?

This option is used only if test_int_math = true

> CPU/GPU mismatch

Your GPU core or memory is unstable. I don't have mismatches on my stock RX 560 and GTX 1060.

> I think it's important to equalize GPU/CPU somehow or even tweak it in such a way that GPUs are favoured. 

It is tweaked for both CPU and GPU. There is almost no slowdown for RX 560 and better cards - look at numbers on the link I gave. The problem is that there is no way to make the inner loop computationally intensive without slowing down low-end cards like RX 550.

> So which of these results would be planned to be implemented?

It's not decided yet. But we need both shuffle and int_math mods to properly fight FPGAs that are going to hit the network in August. They advertise 14 KH/s @ 150 W, in reality they already have 20 KH/s bitstreams and are working on 100+ KH/s bitstreams. 5000 FPGAs in August. You do the math. Small tweaks won't help in this case. We do have an option to calculate one square root instead of two which will make things better for RX 550.

## tevador | 2018-06-23T12:22:12+00:00
@SChernykh There is also this: https://bitcointalk.org/index.php?topic=3628532.0
They claim 7 KH/s @ 10 W of power consumption. They are now dispatching the first 5000 units and additional 25000 units in July (allegedly). If true, it would be about 210 MH/s.

The changes should be tested on a Vega 56/64 because they make up most of the GPU hashpower.

## SChernykh | 2018-06-23T12:24:58+00:00
> The changes should be tested on a Vega 56/64 because they make up most of the GPU hashpower.

Yes, we need these numbers for Vega 56/64. But I'm pretty confident they'll get a minimal slowdown. But still need the actual numbers. Those DWARF FPGA miners (7 KH/s @ 10 W) are a scam.

## SChernykh | 2018-07-16T07:25:24+00:00
@moneromooo-monero My mods have been tested on a wide range AMD, Intel CPUs, Radeon and GeForce GPUs: https://github.com/SChernykh/xmr-stak-cpu/blob/master/README.md#performance

Slowdown compared to current CryptonightV1 is noticeable, but minimal. Note that both mods are actually needed to properly resist current and future ASICs because these mods target different classes of ASIC implementations. Out of the two mods, integer math is more important right now because it slows down current ASICs with on-chip memory. Shuffle mod does nothing against current ASICs, it's more like a preventive measure against future ASICs with external memory.

## moneromooo-monero | 2018-07-18T11:33:41+00:00
Thanks, those numbers look nice. I asked if anyone is able to run on ARM to get an idea of the change there.


## SChernykh | 2018-07-18T12:37:05+00:00
@moneromooo-monero I could test it on Raspberry Pi 3 in 64-bit mode when I'm back from vacation in August, but I don't think it would be relevant at all: it has Cortex-A53 processor which doesn't have enough cache even for a single Cryptonight scratchpad.

## moneromooo-monero | 2018-07-18T21:58:22+00:00
AIUI, some ARMs are currently pretty good in hash/watt.

## SChernykh | 2018-07-21T08:55:59+00:00
@moneromooo-monero I got an answer to your question regarding ARM: https://github.com/SChernykh/xmr-stak-cpu/issues/1#issuecomment-406781548

In short, ARM processors with NEON, AES instructions and enough cache can achieve more than 25 H/s per watt, so they're indeed energy efficient. My mods slow them down ~1.75 times, removing this advantage. They'll still be a bit more efficient than Radeon Vega, but only a bit.

## timolson | 2018-10-08T20:08:53+00:00
The idea of code generation is _not_ ASIC-resistent, and I'm not sure why people think it would be.  We had Java chips in the 90's and a JavaScript chip is entirely feasible.  I would argue that RandomJS and hyc's code gen are even easier than writing a JavaScript chip.

In effect, all you are doing is defining the PoW as a compiler.  An ASIC designer simply creates a chip which does compilation.  This approach does little to nothing to stop an ASIC from being built.

In anticipation of the argument that any ASIC built to perform compilation and code generation is effectively a CPU, that is simply not true.  All modern CPU's have a ton of crap on them which would not be used or exercised, like vector instructions, sophisticated cache handling, and L1 cache itself.  In fact, L1 cache dominates chip area and would largely be wasted in a code-generation PoW, meaning that CPU's would have all this useless die area.  An ASIC would certainly be more efficient.

IMHO the best anti-ASIC measure is still to tie the PoW to DRAM which is by far the most commoditized component.  But even this approach, as we have seen with Ethash and Equihash, is more efficient in custom-built hardware.

Like it or not, custom hardware is inevitable for any coin with sufficient mining value.

## SChernykh | 2018-10-08T20:20:44+00:00
@timolson
> An ASIC designer simply creates a chip which does compilation

Haha, "simply creates" :1st_place_medal: A chip complex enough to do compilation is simply a general purpose CPU. Compilation is a complex process which uses all kinds of logic/arithmetic operations, different data structures, lots of memory, and branches in the code.

>  In fact, L1 cache dominates chip area and would largely be wasted in a code-generation PoW, meaning that CPU's would have all this useless die area. An ASIC would certainly be more efficient.

Good luck trying to run complex algorithms like compilation without cache, performance will be 1% of what you would get with cache.

Are you a hardware (or at least software) engineer at all? Basing by what you just wrote, it seems you have no idea what you're talking about.

## timolson | 2018-10-08T20:25:09+00:00
That was very rude.  My credentials are here:

https://github.com/altASIC/Open-CryptoNight-ASIC

Our design trashes BitMain's by a factor of 5x, and you may test that claim yourself.  Assuming of course you even have access to a hardware development stack.

## SChernykh | 2018-10-08T20:26:15+00:00
Yes, I'm rude sometimes. Ok, but Java != Javascript. Java chips accelerated compiled JavaVM code, they didn't do compilation.

## timolson | 2018-10-08T20:28:23+00:00
I'm trying to help the Monero community by publicly pointing out these flaws in the code generation approach.  I could have kept this private and made a lot of money building an ASIC for your new PoW.  If you want to ignore me, do not complain when I do just that.

## SChernykh | 2018-10-08T20:29:57+00:00
I just don't understand how an ASIC "without cache" could do compilation fast. Can you explain?

## paulshapiro | 2018-10-08T20:30:30+00:00
@timolson there has been some recent discussion by andytoshi, gmaxwell, and hyc in #monero-research-lab (freenode IRC) that the nonces which correspond to easier mining algos can be picked out and run preferentially. The conclusion was it should be simulated. May I invite you to come join the conversation? 

## MoneroCrusher | 2018-10-08T20:33:13+00:00
@timolson @SChernykh 
While I have no knowledge in hardware or software, from having read about this now for a big part of the year, I also think specialized hardware will always have an edge.
But do you know what is really ASIC resistant? The Monero community spitting out a new algo every 6 months, increasing ASIC cost & complexity in the same step. That's what's truly ASIC resistant about this Oct. 18th, knowing that another unknown one is just around the corner.
@timolson can you tape out an ASIC on a large scale within that 6 month period, break even all the labour, production cost, installation, electricity, disposing the ASICs after next fork etc? If so, tell the community about ASIC logistics/business, so we can take measures and i.e. increase forking frequency to 3 months if necessary or take other steps.

## timolson | 2018-10-08T20:38:15+00:00
Forking is not significantly different from code generation.  An ASIC designer can start with a baseline CN impl like ours and intercept the datapath at various points to implement the tweaks in a simple CPU.  The best thing the latest tweak does is change the datapath to memory.  That breaks a lot and does require a great deal of rework.

The issue with tweaking the PoW so frequently is that it doesn't get enough review.  You need to _trust_ the difficulty of your PoW and if it's changing all the time you can't do that.

I'll jump on IRC.

## MoneroCrusher | 2018-10-08T20:43:23+00:00
@timolson Nothing against you, but obviously you have to preserve self-interest and your interest lies in bringing ASICs to Cryptonight, as you've clearly outlined. So you come in here and say ASICs are inevitable, why should we trust you to have a neutral view on this?
Can you say that you could profitably tape out CNv2 on a large scale within 6 months, including all expenses, including the risk of having worthless hardware in 6 months from now?

## SChernykh | 2018-10-08T20:44:45+00:00
>  The best thing the latest tweak does is change the datapath to memory. That breaks a lot and does require a great deal of rework.

What exactly do you mean by the latest tweak? There was a big change from me and a small tweak from @vtnerd - can you go through them step by step and describe how it affects ASICs?

## timolson | 2018-10-08T20:48:32+00:00
> == Cannot send to nick/channel: #monero-research-lab

Private channel?

## SChernykh | 2018-10-08T20:49:25+00:00
@timolson you have to register your nick:
`/msg NickServ register password email`

## zawy12 | 2018-10-08T21:30:58+00:00
@paulshapiro Like gmaxwell, I mentioned several times in this issue it's a "no-go" if the "nonces" can be searched to select code that's easier to compile + solve.  The answer seemed to be "We've got that covered. The solve times will be about equal."  But I didn't see that answer given to gmaxwell.  

## timolson | 2018-10-08T21:39:16+00:00
The answer to the easy nonce problem which was posted in the RandomJS issue does not seem sufficient to me.  By using permutations instead of combinations, you are _reducing_ complexity, _simplifying_ the datapaths in an ASIC, and _guaranteeing_ a fixed ratio of execution units.

## timolson | 2018-10-09T16:01:41+00:00
> @timolson Nothing against you, but obviously you have to preserve self-interest and your interest lies in bringing ASICs to Cryptonight, as you've clearly outlined. So you come in here and say ASICs are inevitable, why should we trust you to have a neutral view on this?

Technical arguments may be weighed on objective merits, so you don't need to trust me.  Go ahead and assume it's not a neutral view; that is fine.  If a "friendly adversary" makes the PoW better, that's great.

However, in defense of my personal honor, there are plenty of startup projects to choose from.  Even if it "had" to be mining and "had" to be an ASIC, we could focus our attention on other coins.  I do honestly believe--and all evidence so far supports this--that specialized mining hardware is inevitable.  The Monero community is the most passionate about maintaining decentralization and the original core values of cryptocurrency, and it is the strongest test of this inevitability claim.  There would be _many_ easier things to try than propose an ASIC for Monero...

## binaryFate | 2018-10-10T18:00:41+00:00
A potential solution to the easy-nonce problem was discussed on IRC recently, which is to chain several generation&execution, where the next code generated depends on the output from the execution of the previous one.

This forces an attacker to actually execute the first N randomly-generated code to even know the code generated at step N+1.

## zawy12 | 2018-10-11T10:13:42+00:00
@binaryFate That might work for small N and be needed if you can't prevent some algos from having quick compile+solvetimes.  You can only do it for small N because all nodes for all time have to verify the input to the N+1 algo which means they have to compile and execute all N+1 algorithms.  I've been wondering if this is really a "proof of compile" POW rather than "proof of algo execution", and needing to do a sequence of N+1 compiles makes me wonder that even more. What percent of time is spent compiling compared to algo execution?

## tevador | 2018-10-11T12:06:20+00:00
It might be a good solution with 2 chained code gen/exec steps. Longer chains would cause the verification time to be too high or require significant reduction of the average complexity of the program.

 > I've been wondering if this is really a "proof of compile" POW rather than "proof of algo execution"

It's a proof of program execution. There is no compilation going on. We are using an interpreted engine (XS) and even using a compiled engine (such as the V8) doesn't improve peformance much because each program is only executed once.

## SChernykh | 2018-10-11T12:50:24+00:00
> There is no compilation going on. We are using an interpreted engine (XS) and even using a compiled engine (such as the V8) doesn't improve peformance much because each program is only executed once.

Formally you are correct, but compilation does happen in reality. XS engine parses the code, then compiles it to internal byte-code format and then executes it.

## tevador | 2018-10-11T13:36:53+00:00
True. But the compilation step is not required to calculate the PoW. Someone could in theory directly execute the expression tree as produced by the code generator. If the hash of the Javascript source code wasn't part of the PoW, there would be no need to even generate it.

It's one of the open issues being discussed here: https://github.com/tevador/RandomJS/issues/9#issuecomment-428851480

## timolson | 2018-10-11T16:17:43+00:00
This point about skipping any compilation or parsing or anything is what I was trying to say about ASIC’s.  All these JS engines do far too much work relative to how an ASIC would operate.  x86 generation wouldn’t change that.

## hyc | 2018-10-11T17:15:18+00:00
You seem to be assuming that 100% of the algorithm will be implemented on the ASIC. That seems unlikely. It seems more likely to me that the code generator will reside on a host CPU, and its output will be fed to an ASIC for accelerated execution. In that case, you still need at least an IR or bytecode to transmit the code to the ASIC.

## timolson | 2018-10-11T17:43:44+00:00
> You seem to be assuming that 100% of the algorithm will be implemented on the ASIC. That seems unlikely. It seems more likely to me that the code generator will reside on a host CPU, and its output will be fed to an ASIC for accelerated execution. In that case, you still need at least an IR or bytecode to transmit the code to the ASIC.

Assuming the easy nonce problem is sufficiently solved, yes, everything on the ASIC. Sending bytecode in or out of the ASIC is an absolute disaster because now you are bandwidth bound on the IO bus. Only the header needs to be sent during an initialization step once per block.  100% of the hashing algo will be implemented on-chip, even if you need to embed an ARM core, which I don’t think is necessary. Personally, I’d experiment with a custom “JS CPU” before resorting to an ARM license.

## cjdelisle | 2018-11-26T12:25:26+00:00
After looking at RandomJS and Vitalik's previous work on random executable code, I suspect that what gmax said in https://pastebin.com/spug4a8x is in fact correct and that anything random-code like is going to fall for miners pre-sifting to remove most of the code snippets and only retain the ones which they have optimized circuitry for.

However, I would like to suggest selecting a PoW algorithm based on a value beyond the miner's control (such as block height). If you have *n* radically different functions, each of which takes approximately the same amount of time to complete on "typical hardware" and the PoW for a block is `FUNCTIONS[block_height % *n*]`, ASIC miners will need to either keep *n* times the circuitry around or will need to dynamically reconfigure, making them not vastly different from an FPGA.

Ideally these algorithms should be radically different in their demands for hardware, one using almost only floating point math, the next one using purely integer math, one using large amounts of memory, the next one using no memory at all, one requiring significant inter-core bus communication, the next being embarrassingly parallel, etc. The objective here is to make sure that at any given time, a largest possible amount of necessary circuitry remains idle.

This should still be quite easy for GPUs and quickly re-programmable FPGAs to mine. With my limited hardware understanding, I understand that the reason why FPGAs were never massively faster than GPUs for Bitcoin is because their flexibility requires them to have a lot of unused circuitry.

---

I think the algorithm designer wants to ensure that each transistor on an FPGA gets about 1/*n* of the usage. If it's not balanced then ASICs will skip certain blocks.

## tevador | 2018-11-26T13:08:08+00:00
@cjdelisle 

> anything random-code like is going to fall for miners pre-sifting to remove most of the code snippets and only retain the ones which they have optimized circuitry for

This problem was discussed in the RandomJS issue linked above and the solution is to chain multiple "code snippets" so that the output of a previous program becomes the seed of the next program.

This way, "filtering" is virtually impossible because the miner doesn't know which functions will be used in the next program until they have executed the first code snippet.

> PoW for a block is `FUNCTIONS[block_height % 256]`

For a double-spend attack, you would need an ASIC that supports less than 30 of the 256 functions.

I don't think it's feasible to design 256 radically different PoW algorithms.


## hyc | 2018-11-26T13:42:22+00:00
> I don't think it's feasible to design 256 radically different PoW algorithms.

If it were feasible, it would be easy to implement in hardware. Self-defeating exercise.

## cjdelisle | 2018-11-26T13:51:31+00:00
@tevador 

> the solution is to chain multiple "code snippets" so that the output of a previous program becomes the seed of the next program

This is a good idea, it reduces the effectiveness of sifting by `2**number_of_iterations` but then the cost is born by the verifiers (I understand at some point someone will need to actually check that the code does make the claimed output).

> For a double-spend attack, you would need an ASIC that supports less than 30 of the 256 functions.

That sounds scary, but if you say "you need 30 different ASICs" it sounds less scary. I'm not really convinced by this logic.

@hyc I think you're missing the point, it's *meant* to be easy to design the ASIC, but making the entire ASIC run at once requires an advancement in ALU design. Imagine for a moment that every other block required heavy integer math or floating point math to mine. Anyone who figures out how to design a chip where 50% of the chip is not idling at any given time has designed a better ALU...

## tevador | 2018-11-26T15:20:00+00:00
> This is a good idea, it reduces the effectiveness of sifting by 2**number_of_iterations but then the cost is born by the verifiers (I understand at some point someone will need to actually check that the code does make the claimed output).

The cost of verification increases linearly, but the cost of "filtering nonces" increases more than exponentially.

> you need 30 different ASICs

An ASIC could just have a board with 1 chip per PoW function. It would be still orders of magnitude more efficient than a CPU, just the initial investment would be larger, which would only cause more centralization.

I think an ASIC that implements just 32 "easiest" functions would be economically feasible (you could mine only 1/8 of the blocks, but this would be compensated by much higher efficiency).


## zawy12 | 2019-03-02T11:01:35+00:00
This article delineates security in POW and shows electrical waste is not part of it.  I'l describe a "virtual-POW" using VDF's with stake or hard-drive space.

[ edit: moved all the text to **[my blog ](https://zawy1.blogspot.com/2019/03/a-virtual-pow-to-prevent-51-attacks.html)**   ]

## selsta | 2021-08-13T04:22:18+00:00
RandomX has been implemented since Nov 2019.

# Action History
- Created by: zawy12 | 2018-04-03T11:45:42+00:00
- Closed at: 2021-08-13T04:22:18+00:00
