---
title: base32 algorithm with a basic unit_test
source_url: https://github.com/seraphis-migration/monero/pull/2
author: DangerousFreedom1984
assignees: []
labels: []
created_at: '2023-06-06T20:19:23+00:00'
updated_at: '2023-09-18T18:55:36+00:00'
type: pull_request
status: closed
closed_at: '2023-09-18T18:55:36+00:00'
merged_at: null
---

# Original Description
One file base32 algorithm using specified Jamtis alphabet.

# Discussion History
## UkoeHB | 2023-06-06T22:03:54+00:00
The ends of files need newlines. If you glance over the PR on github you will see a nice symbol complaining about it.

## DangerousFreedom1984 | 2023-06-07T03:51:07+00:00
Thanks

## rbrunner7 | 2023-06-09T11:25:22+00:00
I see here a very good opportunity to explain why we use a different alphabet than almost anybody else for "our" Base32 variant, and mention which characters are missing or different.

## rbrunner7 | 2023-06-09T11:35:17+00:00
> Quite different now.

I wonder quite a bit about this. Why, explained on a high conceptual level, did the code have to change much? The different alphabet is clear of course, but beyond that?

I have a hard time anyway to compare your code with the forked original code, which makes it very hard to quickly decide whether the code is still correct without basically looking at everything. The original ist this file, right? https://github.com/ahmed-masud/libbase32/blob/master/base32.c

## rbrunner7 | 2023-06-09T11:44:29+00:00
Ok, misunderstand from my side, this line is not from you, @DangerousFreedom1984 , but already present in the code that you forked:

> Adapted from https://github.com/ahmed-masud/libbase32

As far as I see you don't give info in this PR where you got the code from, unfortunately, but I think I found it here: https://github.com/tplgy/cppcodec/blob/master/cppcodec/detail/base32.hpp , with parts from other files of that repo copied in, to have it all in one file I suppose.

Which still leads me to the question: That file from Ahmed Masud I linked above is wonderfully small, and wonderfully readable. Is it really not fit for purpose?

## rbrunner7 | 2023-06-09T11:46:04+00:00
Do you happen to know what "decode the tail" means, and whether we really need this?

## DangerousFreedom1984 | 2023-06-11T10:58:15+00:00
That was the agreed alphabet proposed by tevador after some research and discussion: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#35-base32-encoding 

## DangerousFreedom1984 | 2023-06-11T11:05:21+00:00
Yes, I copied most of the code from https://github.com/tplgy/cppcodec/blob/master/cppcodec/detail/base32.hpp as it seems to me the most reliable and efficient base32 library.
The code from Ahmed does not seem to be as efficient as this one as they improved it. I may be wrong though.
Since both are MIT licenses I believe that the correct way to copy is by pasting the exact header in our header file, right? 

## DangerousFreedom1984 | 2023-06-11T11:49:19+00:00
Yes we need it. It decodes correctly the last remaining block. You can check the idea of the algorithm here:
https://herongyang.com/Encoding/Base32-Encoding-Algorithm.html

I believe that this is the typical PR that needs different implementations, comparison and performance tests. I dont expect this exact code to be used in the final version but so far I do believe that it is correct, optimized and will serve for our purposes at the moment.

## rbrunner7 | 2023-06-11T13:49:12+00:00
> Since both are MIT licenses I believe that the correct way to copy is by pasting the exact header in our header file, right?

I am a unsure myself. The wording of the license is a bit different, maybe just a different iteration. At least we are on the safe side if we copy verbatim I guess.

## rbrunner7 | 2023-06-11T13:51:06+00:00
Well, yes, I know, you know, but a reader new to the code and Seraphis in general will not, hence my idea why not make some comments?

## vtnerd | 2023-09-10T16:01:26+00:00
We've typically returned `bool` in these types of (simple/basic) functions.

## vtnerd | 2023-09-10T16:02:19+00:00
There should be some tests for invalid characters that "`return false`".

## vtnerd | 2023-09-10T16:02:36+00:00
Nitpick, but why have the function at all?

## vtnerd | 2023-09-10T16:03:12+00:00
These could be constants instead of functions, the compiler doesn't have to reserve static memory for them if the address is never taken, etc.

## vtnerd | 2023-09-10T16:04:02+00:00
Nitpick again, but this function isn't really doing much.

## vtnerd | 2023-09-10T16:04:23+00:00
Why have this function at all? Is it going to change in some future revision?

## vtnerd | 2023-09-10T16:05:17+00:00
We are using C++14, so the `constexpr` rules have relaxed. This could be an `if`/`else` ladder, which might be easier to read

## vtnerd | 2023-09-10T16:07:45+00:00
This may be why you didn't `return false`, it ruins the `constexpr` flow in here.

## vtnerd | 2023-09-10T16:09:44+00:00
Why not return the `std::string here`? It's a cleaner interface, and easier on the compiler for aliasing rules. And the string is always being cleared out anyway.

## vtnerd | 2023-09-10T16:23:54+00:00
We are using C++14 now, and this (at a glance) appears to be implementing `std::integer_sequence<unsigned, ...>` and `gen_seq` appears to be implementing `std::make_integer_sequence<unsigned, ....>`. Seems better to just use them, instead of reimplementing in here:

```c++
template<unsigned... Is>
using seq = std::integer_sequence<unsigned, Is...>;

template<unsigned I>
using gen_seq = std::make_integer_sequence<unsigned, I>;
```

## vtnerd | 2023-09-10T16:27:02+00:00
The minimum gcc supported by Monero is currently  `5`, so I would just drop this compatibility code.

But even better, use the `struct` version _all the time_, as I can't think of any penalty to using it that way.


## vtnerd | 2023-09-10T16:40:32+00:00
Why not just return `256`? This logic can fail if `T` is 64-bits, etc.

## vtnerd | 2023-09-10T16:41:44+00:00
Yikes, why not `throw std::logic_error{}` here with a readable message. Or a `MERROR("")` before the `abort()`?

## vtnerd | 2023-09-10T18:31:16+00:00
`result.clear();`?

## vtnerd | 2023-09-10T18:52:00+00:00
Is this possible? Seems like a good candidate for `assert`. Or just `throw std::logic_error`.

## vtnerd | 2023-09-10T19:09:12+00:00
`const std::string& input` or even better `epee::span<const std::uint8_t>`. It doesn't appear the null termination byte can ever be used in the encoder or decoder.

## vtnerd | 2023-09-10T19:10:33+00:00
Again, `const std::string&` or `epee::span<const std::uint8_t>`?

## vtnerd | 2023-09-10T19:13:32+00:00
Perhaps mark `alphabet_index const* const` for both?

## vtnerd | 2023-09-10T19:23:43+00:00
Is this even possible given the logic of the function ? An `assert()` if this should never fail is ok.

## DangerousFreedom1984 | 2023-09-13T22:50:37+00:00
Yeah, better.

## DangerousFreedom1984 | 2023-09-13T22:50:44+00:00
I could do that but then I would have to use const_cast in this line `alphabet_index_ptr = const_cast<alphabet_index_t* (alphabet_index_start);`
Which I dont know if it make things safer.

## DangerousFreedom1984 | 2023-09-13T22:51:03+00:00
Ok.

## DangerousFreedom1984 | 2023-09-13T22:51:09+00:00
Yeah, abort is too abrupt.

## DangerousFreedom1984 | 2023-09-13T22:51:11+00:00
Looks like resize(0) could be faster but I think it makes no difference. 

## DangerousFreedom1984 | 2023-09-13T22:51:14+00:00
Yeah, better.

## DangerousFreedom1984 | 2023-09-13T22:51:17+00:00
Yeah, better.

## DangerousFreedom1984 | 2023-09-13T22:51:20+00:00
Ok, done.

## DangerousFreedom1984 | 2023-09-13T22:51:22+00:00
They are reimplementing because of that Clang 3.6 limitation of template recursion. Should I still replace by the std as you propose?

## DangerousFreedom1984 | 2023-09-13T22:51:26+00:00
Ok. Done. Now it is more similar to the base58 interface.

## DangerousFreedom1984 | 2023-09-13T22:51:35+00:00
Fixed.

## DangerousFreedom1984 | 2023-09-13T22:51:39+00:00
Was dumb. More tests were created.

## DangerousFreedom1984 | 2023-09-13T22:51:42+00:00
Included.

## DangerousFreedom1984 | 2023-09-13T22:51:46+00:00
Is there any problem in using 'throw' ? 

# Action History
- Created by: DangerousFreedom1984 | 2023-06-06T20:19:23+00:00
- Closed at: 2023-09-18T18:55:36+00:00
