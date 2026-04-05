---
title: Hi, I have some questions regarding this project
source_url: https://github.com/xmrig/xmrig/issues/2311
author: Joe23232
assignees: []
labels:
- question
created_at: '2021-04-25T01:19:26+00:00'
updated_at: '2022-04-03T14:40:03+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:40:03+00:00'
---

# Original Description
Hi, I have some questions regarding this project:

1. Am I able to import it as a library/crate into my own [Rust](https://www.rust-lang.org/) programming language code and integrate it into my own software so I can compile all into a single executable?
2. Does it support either [Beam](https://beam.mw/),  [Zcash](https://z.cash/) or [Monera](https://www.getmonero.org/) or any other privacy respecting cryptocurrency?
3. How efficient is it compared to something like [gminer](https://github.com/develsoftware/GMinerRelease)?
4. Do you guys get a commission from my cryptomining if I were to use this library/crate?
5. How well maintained is this project? How many people are working on it?

# Discussion History
## Spudz76 | 2021-04-25T01:48:32+00:00
1. Not easily I'd guess, but then again this is the first time I've heard of Rust.  Also, why?
2. No, the supported coins/algos are always [listed here](https://github.com/xmrig/xmrig/blob/master/doc/ALGORITHMS.md#algorithm-names)
3. Generally equal, but gminer supports some additional algos (c29 types, Ethash).  It might be slightly faster on KawPow
4. Not if you hack the donation minimum limit in the code and set donation to 0, which should be easy once you've learned enough C++ to Rust it up (can't be done on gminer, so your hashrate can be donation percent better, gminer has various donation percentages per algo)  Somewhat prefer if you've donated some other way to the project then, though (such as I lurk the Issues, occasionally submit useful Pull Requests... try to give back some value)
5. Very, updates are almost annoyingly often.  Between several and many.

## Joe23232 | 2021-04-25T02:04:07+00:00
> Not easily I'd guess, but then again this is the first time I've heard of Rust. Also, why?

Can I at least import it into a C++ library at least so that I can then generate one executable and tightly integrate it within my software for my own PC?

> No, the supported coins/algos are always listed here

Do you happen to know which one is a privacy oriented focused cryptocurrency?

> Not if you hack the donation minimum limit in the code and set donation to 0, which should be easy once you've learned enough C++ to Rust it up (can't be done on gminer, so your hashrate can be donation percent better, gminer has various donation percentages per algo) Somewhat prefer if you've donated some other way to the project then, though (such as I lurk the Issues, occasionally submit useful Pull Requests... try to give back some value)

Right I see thanks.

> Very, updates are almost annoyingly often. Between several and many.

Thanks man.

## Joe23232 | 2021-04-25T06:52:26+00:00
Thanks mate

## AndyRPH | 2021-04-25T19:12:32+00:00
To correct the above, this absolutely supports Monero, although I think the reply you for was because you spelled it MonerA but linked to monero's info. 

## Joe23232 | 2021-04-27T12:55:07+00:00
@AndyRPH Right my mistake :)

# Action History
- Created by: Joe23232 | 2021-04-25T01:19:26+00:00
- Closed at: 2022-04-03T14:40:03+00:00
