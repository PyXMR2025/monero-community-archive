---
title: How to change intensity and worksize in v5.0.1?
source_url: https://github.com/xmrig/xmrig/issues/1322
author: wisnia37
assignees: []
labels: []
created_at: '2019-11-27T16:42:39+00:00'
updated_at: '2024-05-03T13:31:32+00:00'
type: issue
status: closed
closed_at: '2021-04-12T15:27:34+00:00'
---

# Original Description
How do you change these parameters in the latest version to bypass the default settings for the NVIDIA card?

# Discussion History
## username1565 | 2020-12-01T07:04:07+00:00
Hello. Can you add argument --intensity, or "intensity":value in JSON-config,
to set intensity of mining on each core, and decrease this intensity, using `trottling`, or some `delay`?
Because limitation of number of the CPU-threads, decreasing usage of CPU-cores,
but loading on this corea is 100%, and temperatures is maximum, on each loaded CPU-core.
Not good...
What if need to load 8 cores up to 25%, and no more?

Thanks.

## Spudz76 | 2020-12-04T09:30:29+00:00
@wisnia37 CUDA doesn't use intensity or worksize you're thinking of OpenCL.  As the autoconfig for CUDA is generated inside the `xmrig-cuda` plugin there are no commandline options for threads/blocks, and the ones for bfactor/bsleep don't seem to work either:
```
      --cuda-bfactor-hint=N     bfactor hint for autoconfig (0-12)
      --cuda-bsleep-hint=N      bsleep hint for autoconfig
```
So then let it generate the highest possible threads/blocks and turn them down (and/or add bsleep/bfactor) by hand.

---

@username1565 Repaste your heatsinks if you can't run 100% 24/7 without hitting thermal throttling.

25% would be running autoconfig once for a "full" setup and then go in and delete 75% of the threads in some balanced way.

There is an option for this (`--cpu-max-threads-hint=N  maximum CPU threads count (in percentage) hint for autoconfig
`) but I've never had it work right, therefore I just let it calculate 100% and then carve it away by hand.

## username1565 | 2020-12-09T19:25:42+00:00
@Spudz76, yes, now I using `threads:2` in `algo` config-section, instead of `--cpu-max-threads-hint=N`, and I see 2 cores from 8 was been loaded. But this is loaded up to 100% and temperatures there about 100 celsium.
I just wanted to use something, like `--max-cpu-usage=25` to set 25% of loading for each core, and do not see so high temperatures, on each core. Maybe there is possible to use trottling, or time delays, to implement this.

## James4Ever0 | 2024-05-03T12:36:02+00:00
Turned out it is straightforward to slow down the mining process, by adding some sleep code [here](https://github.com/xmrig/xmrig/blob/master/src/core/Miner.cpp):

```cpp
xmrig::Job xmrig::Miner::job() const
{
    std::lock_guard<std::mutex> lock(mutex);

    return d_ptr->job;
}
```

I will make a pull request ASAP.

# Action History
- Created by: wisnia37 | 2019-11-27T16:42:39+00:00
- Closed at: 2021-04-12T15:27:34+00:00
