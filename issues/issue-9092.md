---
title: Redesign and Improve the Logging Infrastructure
source_url: https://github.com/monero-project/monero/issues/9092
author: '0xFFFC0000'
assignees:
- '0xFFFC0000'
labels:
- enhancement
- low priority
- proposal
- discussion
created_at: '2023-12-20T10:23:48+00:00'
updated_at: '2026-02-18T21:50:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello Monero community,

Past few days I have been working on the logging infrastructure in the Monero codebase. There are a few measures that we can to clean up and improve our logging infrastructure. Before getting into those this is the overall picture of what we have right now:
1. For the core of our logging we use the EasyLogging++ library. 
2. We do have Monero-specific API abstraction in `contrib/epee/include/misc_log_ex.h` which calls EasyLogging++ APIs.
3. `EasyLogging++` provides multiple logging levels `Global, Trace, Debug, Fatal, Error, Warning, Verbose, Info, Unknown`. Our APIs are only using `Fatal, Error, Warning, Info, Debug, Trace` levels for logging.
4. We do have support for categories for Logging. For example, by defining a category `console_handler` we can distinguish that logging has been done by `console_handler`. Which is a matrix of (`Levels` * `Categories`).
5. We do support logging to multiple files.
6. We do support console logging and colourful logging.

That is the status of what we have right now. There are a few serious downsides to it:

1. **Extremely hackyway** to implement categories ([here](https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/contrib/epee/src/mlog.cpp#L238), [here](https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/contrib/epee/src/mlog.cpp#L97) and many other examples).
2. **Extremely hackyway** to implement log rotation ([here](https://github.com/monero-project/monero/blob/ac02af92867590ca80b2779a7bbeafa99ff94dcb/contrib/epee/src/mlog.cpp#L167)).
3. Extra dependency. We do depend on the [EasyLogging++](https://github.com/abumq/easyloggingpp/) library for logging. While EasyLogging++ is a good library IMHO, if we can remove that it means a reduction in our dependencies which is a win. 
4. Even if we want to keep using [EasyLogging++](https://github.com/abumq/easyloggingpp/) it lacks any support for concept of categories. And many half-baked features e.g. [here](https://github.com/abumq/easyloggingpp/issues/408#issuecomment-1741751975).

## What Options Do We Have
There are many logging libraries in C++ community ([spdlog](https://github.com/gabime/spdlog), [Boost.Log](https://github.com/boostorg/log), [glog](https://github.com/google/glog), [plog](https://github.com/SergiusTheBest/plog), and many others). But each one of them does have its downside, plus the headache of porting our infrastructure and all the manpower we have to invest. 

The only option that would be a win for Monero source code in my opinion is `Boost.Log` which I will explain in detail here.

## Replace EasyLogging++ with Boost.Log
First of all, we already depend on `Boost`. We do use `Boost` extensively in our source code. So if we can port our logging infrastructure to `Boost.Log` we will remove another dependency. 

Second, `Boost.Log` does provide a clean API for logging. Particularly we are interested in its `channel` APIs which are the same as the `category` concept we use in our logging. Their log rolling and rotation are much more robust than EasyLogging++. 

Third, better code quality with `Boost.Log`. Once we removed the categories and cleaned up the rotation. We are going to have much cleaner C++ code.

Fourth, much better customizability options for our logging. we can have log configuration files and many many other options.

One last thing to consider is since logging does not interact with secret data in Monero source code, usually, there are not that much risk to replace the logging code base..

### Downside
The only downside is the colourful output. Although `EasyLogging++` support for colourful output is already halfbaked (I would've not released it if I were its developer). 

There are [ways](https://stackoverflow.com/a/38316911) to make the `Boost.Log` output colourful, but I would not suggest that.



P.S. I am working on this in my spare time, and eventually will release the source code as branch `0xfffc/boost/log` on my Github. *Waiting to hear the community's feedback.*

# Discussion History
## iamamyth | 2023-12-20T19:47:15+00:00
I don't have a particular affinity for the existing logging infrastructure, but I would just note that changes like this one require a time investment from reviewers and so they need a plausible cost-benefit tradeoff.

The current approach, irrespective of the backing library, has some benefit in its minimalism: Not supporting complex config files means the logging doesn't lock in a particularly set of opinions inherited from a library. If you expose options like file-based config, you're likely stuck with boost, forever, so you make a soft dependency a hard one, effectively increasing the dependency burden. I also don't agree with the characterization that switching from easylogging++ to boost logging eliminates a library dependency, due to the project already using boost: Boost is a collection of many libraries, not one giant library, so every new boost component is a new dependency.

Regardling colorized logging, I don't personally like it, but it exists now, and presumably that means someone thought it worthy of adding. So, removing it requires some buy-in from a variety of parties.

## Gingeropolous | 2024-01-30T12:26:14+00:00
all i know is the existing log system is way better than the original one.

I'm also a fan of the colors - it helps spot things while watching the log stream (because... thats what normal people do, right?)

just my 2 cents.

but then again, no one asked me when they changed from the original logging to the current system, and that was a major improvement. 

# Action History
- Created by: 0xFFFC0000 | 2023-12-20T10:23:48+00:00
