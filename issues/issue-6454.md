---
title: undefined behavior in keccak
source_url: https://github.com/monero-project/monero/issues/6454
author: tankf33der
assignees: []
labels: []
created_at: '2020-04-16T11:53:58+00:00'
updated_at: '2020-10-15T22:45:55+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:45:54+00:00'
---

# Original Description
I cut crypto hash functions (blake, groestl, jh, keccak and skein) to pass to clang's sanitizers (address, memory, undefined) and [TIS](https://trust-in-soft.com/tis-interpreter/). All passed exept keccak.

Two independent tools TIS and [ccomp](http://compcert.inria.fr/) (-interp mode) reports undefined behavior in this [line](https://github.com/monero-project/monero/blob/master/src/crypto/keccak.c#L181) in "IS_ALIGNED_64" define:
```
Stuck state: in function keccak_update, expression
        <loc is_aligned> = 0 == (7 & <ptr> - 0LL)
        Stuck subexpression: <ptr> - 0LL
        ERROR: Undefined behavior
        make: *** [Makefile:14: interp] Error 126
```

```
keccak/keccak.c:201:[kernel] warning: pointer subtraction:
                  assert \base_addr((char const *)in) ≡ \base_addr((char const *)0);
                  stack: keccak_update :: keccak/hmac-keccak.c:52 <-
                         hmac_keccak_init :: keccak/hmac-keccak.c:78 <-
                         hmac_keccak_hash :: keccak/main.c:21 <-
                         main
[value] Stopping at nth alarm
[value] user error: Degeneration occurred:
                    results are not correct for lines of code that can be reached from the degeneration point.
```

I did the same checks for hash functions from [bytecoin](https://github.com/bcndev/bytecoin) and keccak passed. 

# Discussion History
## moneromooo-monero | 2020-04-16T13:54:51+00:00
Is it happy with:

#define IS_ALIGNED_64(p) ((((uintptr_t)p) & 7) == 0)


## tankf33der | 2020-04-16T17:00:24+00:00
> Is it happy with:
> 
> #define IS_ALIGNED_64(p) ((((uintptr_t)p) & 7) == 0)

I dont think so:
```
$ ccomp -interp -quiet mike.c
start
Stuck state: in function keccak_update, expression
        <loc is_aligned> = (<ptr> & 7) == 0
Stuck subexpression: <ptr> & 7
ERROR: Undefined behavior
make: *** [Makefile:14: interp] Error 126
```
```
keccak/keccak.c:202:[value] warning: The following sub-expression cannot be evaluated:
                 (unsigned long)in & (unsigned long)7
                 
                 All sub-expressions with their values:
                 unsigned long  (unsigned long)in ∈ {{ (unsigned long)&pad }}
                 unsigned long  (unsigned long)7 ∈ {7}
                 uint8_t const *  in ∈ {{ &pad[0] }}
                 int  7 ∈ {7}
                 
                 Stopping
                 stack: keccak_update :: keccak/hmac-keccak.c:52 <-
                        hmac_keccak_init :: keccak/hmac-keccak.c:78 <-
                        hmac_keccak_hash :: keccak/main.c:21 <-
                        main
[value] user error: Degeneration occurred:
                    results are not correct for lines of code that can be reached from the degeneration point.
```

## moneromooo-monero | 2020-04-16T18:20:42+00:00
I don't see what's wrong here. I don't suppose it gives any other info ?

## LoupVaillant | 2020-04-16T18:45:44+00:00
I've seen this kind of thing [in Libsodium](https://github.com/jedisct1/libsodium/issues/934). Long story short, converting to `uintptr_t` didn't make the comparison any less undefined. It is unclear who is right there (the tools or Libsodium), and compilers generate the right code anyway. But it does look like what they're trying to do is simply impossible in fully compliant C.

Your attempt to check for alignment may fall prey to the same pitfall. If you want to avoid UB The only reliable workaround I see here is to not process pointers (even if you convert them) but indices.

As a matter of personal taste, I believe checking for alignment is kind of a code smell. I have implemented a cipher and two hashes, with update APIs that had to handle unaligned input. There was no need to check for alignment.

On the other hand, I understand this would be significant work.


## moneromooo-monero | 2020-04-16T18:49:10+00:00
The first UB was the pointer arithmetic fwiw.

I suppose we could memcpy all the time, but this seems slower.

Anyway, other possible macro:

#define IS_ALIGNED_64(p) ((((uintptr_t)(const void*)p) & 7) == 0)


## hyc | 2020-04-16T18:54:45+00:00
Since when is checking for bits being set or unset in an integer undefined behavior?

These tools need to seriously improve their diagnostic output if they expect programmers to take them seriously. If they're going to flag something as undefined behavior, they should reference which section of the language spec says so.

## LoupVaillant | 2020-04-16T19:20:49+00:00
@hyc I agree, but those are two independent tools. The fact they agree with each other tends to trigger my spidey senses.

## tankf33der | 2020-04-18T18:27:26+00:00
Latest blog [post](https://trust-in-soft.com/blog/2020/04/06/gcc-always-assumes-aligned-pointers/) from authors of TIS about alignment.

## moneromooo-monero | 2020-05-16T12:29:31+00:00
https://github.com/monero-project/monero/pull/6538

## pascal-cuoq | 2020-06-15T13:23:52+00:00
Hello,

I am responsible for the design choices in the TrustInSoft tools, and I have also used `ccomp -interp` quite a bit for differential testing. Both these tools occupy the previously-neglected part of the design space “providing guarantees about the execution that hold for all memory layouts”. In contrast, ASan and Valgrind only find problems with the particular memory layout that they use, and that memory layout is different from the memory layout used when executing the program without them.

In order to detect bugs that can happen in any possible memory layout, TrustInSoft tools and `ccomp -interp` use a symbolic representation of base addresses, such as `t` in:
```
char t[100];
```
Subtracting a null pointer from `t` is not the right way to access the representation of the address of `t` (it is not one of the cases allowed in https://cigix.me/c17#6.5.6.p9 ) and each of these tools would warn on this basis alone. However, going through `uintptr_t` is the correct way for any compiler that allows to convert pointers to integers. Unfortunately, for the tools being discussed, for the sort of guarantees they attempt to provide and the means they need to use in order to provide them, `(uintptr_t)t & 7` is still annoying. The result can be any value between 0 and 7, when another choice they have made was to treat C programs as deterministic so that it would be easy to follow the execution from beginning to end.

TrustInSoft CI lets you work around the problem by assuming that every variable has some minimum alignment, say 8, and recognizing a number of patterns, such as `(uintptr_t)t & 7`, evaluating to a single value under this assumption. This is illustrated at https://github.com/pascal-cuoq/automatic-waffle/blob/71e7022e6b89e1b48f26c06d6d762df3fd2904fa/tis.config#L14-L23 , leading test 3 to go through in https://ci.trust-in-soft.com/projects/pascal-cuoq/automatic-waffle/3 .

This is an unsatisfying workaround, and it is planned to recognize each base address' alignment from its type and to support C17's `_Alignas` at some point. But the crude global option is available now in order to still obtain some results on code where the idiom must stay.

## moneromooo-monero | 2020-06-17T00:32:53+00:00
If the tool assumes a particular alignment, leading to (uintptr_t)t & 7 to evaluate to a constant, this would cause some of the code to be dead, which seems irrelevant to whether the code as a whole contains UB. AFAIK some code being dead is not UB in itself. Could you expand on why this alignmemt workaround causes this spurious trigger please ?

## pascal-cuoq | 2020-06-18T12:52:03+00:00
@moneromooo-monero The workaround is to use `"raw_options": { "-address-alignment": "8" }` in the configuration file `tis.config`, which is not the default, and makes the analyzer assume that all base addresses are multiple of 8. This makes the test fit inside the analyzer's limitations, and as a result, the analyzer's execution of the test no longer stops at `((uintptr_t)(const void*)p) & 7`. The test can be fully analyzed, and since it does not do anything else that is either forbidden or outside the analyzer's possibility to model, it runs to its end without diagnostic.

There is no spurious warning when the workaround is used. The spurious warning only appears when the workaround is not used. I called the workaround “unsatisfying” because when the workaround is used, an Undefined Behavior that would result from a `char array` being placed in memory at an address that is, say, a multiple of 8 plus 5, and that only happens in these conditions, would not be detected by the analyzer (which assumes, as instructed, that the address of the array must be a multiple of 8).

## moneromooo-monero | 2020-10-15T22:45:54+00:00
That one's fixed, feel free to report others you may find.

# Action History
- Created by: tankf33der | 2020-04-16T11:53:58+00:00
- Closed at: 2020-10-15T22:45:54+00:00
