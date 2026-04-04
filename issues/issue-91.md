---
title: Seraphis Performance Results
source_url: https://github.com/monero-project/research-lab/issues/91
author: UkoeHB
assignees: []
labels: []
created_at: '2021-11-11T20:36:06+00:00'
updated_at: '2022-04-15T20:06:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
UPDATE: See [this comment](https://github.com/monero-project/research-lab/issues/91#issuecomment-1047191259) for most current results.

## Seraphis Performance Results

Below I display and discuss performance results from several transaction protocol mock-ups (CLSAG, Triptych, Seraphis-Concise, Seraphis-Merge, Seraphis-Squashed), collected during one test run. The purpose of this report is to inform engineering/design decisions around a potential real-world implementation of Seraphis.



## Preliminaries

### Test Context

The test was run single-threaded on a `zenith2alpha` motherboard with an AMD Ryzen Threadripper 3970X 32-Core processor and 256GB RAM. It was run on my [Seraphis perf test branch](https://github.com/UkoeHB/monero/tree/seraphis_perf) at commit `e0620b4f71faa20e69afcac6206a4180102f251d`, and started at `2021-11-09 : 18:02:12 UTC` (according to the machine's clock). The test command was `./build/Linux/seraphis_perf/release/tests/performance_tests/performance_tests --filter=\*mock_tx\* --stats --loop-multiplier=10 --timings-database=/home/user/seraphis_perf/test_results/perf_3.txt > /home/user/seraphis_perf/test_results/stdout_perftest_3.txt`.


### Terminology

- **Enote** (a.k.a. 'output' or 'txo'): A small message containing an _amount_ and a _recipient address_.
- **Input**: A transaction input (an enote being spent).
- **Output**: A transaction output (a new enote).
- **Reference set size**: The number of old enotes referenced by an input's membership proof. A membership proof demonstrates that a transaction spends an enote that exists in the ledger. If the reference set size is >1, then proof verifiers will not know which of the referenced enotes is being spent (just that the spent enote is one of the referenced enotes).
- **Reference set size decomposition**: `ref_set_size = n^m`, where `n` is the 'decomposition base'. This detail is relevant to Grootle membership proofs (used in Triptych, Seraphis, Lelantus-Spark), which require `n` and `m` to be integers.


### Test Questions

There were a number of questions I wanted to answer with this test.
- How are tx verification/size costs affected by changing the reference set size? What is the impact on those costs if transactions are batch-verified?
    - Bulletproofs+ proofs can be batch-verified for non-trivial savings.
- How are tx verification/size costs of Grootle-based tx protocols affected by changing the ref set size decomposition base (`n`)?
- Do any Grootle-based protocols have relative advantages compared to each other when increasing the number of transaction inputs (all else equal)?
    - CLSAG is trivially worse-performing than Grootle proofs for equivalent reference set sizes (i.e. the 'all else equal'), so it was not considered here.
- Are there any advantages to 'splitting' Bulletproofs+ range proofs within transactions? What is the interaction between range-proof splitting and batch-verifying transactions?
    - A BP+ range proof can aggregate multiple range proofs in a single structure, or those proofs can be separated into different structures.
- **Note**: All protocol types are \~equivalent as a function of outputs, so that variable is not of great interest.



## Results

#### Experiment 1: reference set size (no batching)

Fixed parameters: 2-input/2-output, no BP+ splitting, no tx verification batching. Note that the verification plot is logarithmic in the y-axis.

![refset_2series_ver](https://user-images.githubusercontent.com/37489173/141365115-960fa1ba-1a50-4bbc-9bc1-17319db6f502.png)
![refset_2series_size](https://user-images.githubusercontent.com/37489173/141365105-cccc2cec-c452-4b98-b960-7ac3d5b36ba4.png)


#### Experiment 2: reference set size (25 tx per batch)

Fixed parameters: 2-input/2-output, no BP+ splitting, 25 tx per batch (normalized to cost/tx). Note that the verification plot is logarithmic in the y-axis.

![refset_2series_25batch_ver](https://user-images.githubusercontent.com/37489173/141365224-7c7e009f-60e9-4be0-a18b-05e278567bc8.png)


#### Experiement 3: reference set size decomposition

Fixed parameters: 2-input/2-output, no BP+ splitting, no tx verification batching.

![decomp_concise_ver](https://user-images.githubusercontent.com/37489173/141364698-9180d255-7225-44a4-b676-d690af3c060b.png)
![decomp_concise_size](https://user-images.githubusercontent.com/37489173/141364683-8dcbfd40-f0db-4176-accf-11ae57c140da.png)


#### Experiment 4: inputs

Fixed parameters: 2-output, reference set decomposition 2^8, no BP+ splitting, no tx verification batching.
- For squashed tx: batching shown in legend.

These results are normalized to 1 input for each protocol type.

![inputs_ver](https://user-images.githubusercontent.com/37489173/141364721-8140a36e-6ff9-4656-acf7-f1a74c968a4d.png)
![inputs_size](https://user-images.githubusercontent.com/37489173/141364717-f445b0ab-a406-4f75-b260-462cdd6e0162.png)


#### Experiment 5: BP+ splitting (no batching)

Fixed parameters: 2-input, reference set decomposition 2^8, 1 tx per batch (normalized to cost/tx).

![outputs_concise_1batch_ver](https://user-images.githubusercontent.com/37489173/141365260-cc898eb6-77a5-4910-91c8-234920b982b1.png)
![outputs_concise_1batch_size](https://user-images.githubusercontent.com/37489173/141365257-87dacd2c-449f-4810-aa1e-b01116f4fa94.png)


#### Experiment 6: BP+ splitting (25 tx per batch)

Fixed parameters: 2-input, reference set decomposition 2^8, 25 tx per batch (normalized to cost/tx).

![outputs_concise_25batch_ver](https://user-images.githubusercontent.com/37489173/141365287-db48db0e-333d-4c33-b4c2-145b80445f18.png)



## Discussion


My key take-aways:
- Compared to CLSAG, other protocols are about 4x more efficient in terms of verification costs. However, Seraphis-Squashed stands out as noticeably more efficient than the other options, especially when batching is taken into account.
- There is no benefit to using a reference set size decomposition base other than `n = 2` or `n = 3`. I believe `2^6 = 64`, `3^4 = 81`, and `2^7 = 128` are the best candidates for a reference set size using one of the new variants, taking CLSAG with `ref_set_size = 16` as a baseline for comparison (`16` is likely to be the reference set size after Monero's next hardfork).
- Seraphis-Squashed scales significantly better with rising input counts than the other protocols, especially when batching is included.
- Seraphis-Merge saves 96 bytes per input compared to Seraphis-Concise and Seraphis-Squashed, but has negligible relative impact on verification times. The cost of Seraphis-Merge over other variants is it becomes impossible to do 'collaborative funding', where independent parties provide inputs to the same transaction.
- While BP+ splitting has noticeable verification-cost-reduction effects when there is no batching, those differences are amortized (even reversed slightly) when batching is included. Since BP+ splitting causes larger transactions, and since performance/size analysis is geared toward the 'upper end' of transaction throughput (when batching can/should be applied to all transactions, since blocks will contain many transactions), I don't recommend implementing BP+ splitting.






# Discussion History
## rbrunner7 | 2021-11-12T18:38:58+00:00
How do those Seraphis "merge", "concise" and "squashed" variants differ? An ELI5 would be something for crypto-challenged people like me :)

## UkoeHB | 2021-11-12T18:45:31+00:00
@rbrunner7 
- Merge
  - membership proof: concise grootle
  - ownership proof (and proof that key images are correct): merged Seraphis composition proof (one proof for all inputs)
- Concise
  - membership proof: concise grootle
  - ownership proof (and proof that key images are correct): separate Seraphis composition proofs (one proof per input)
- Squashed
  - membership proof: simple grootle (concise vs plain doesn't matter)
  - ownership proof (and proof that key images are correct): separate Seraphis composition proofs (one proof per input)
  - extra: BP+ range proofs for inputs

Basically, 'concise' is the plain one, 'merge' is slightly more efficient but you have to sign all inputs at the same time (tx author must own all funds spent by the tx, different from other variants where multiple people can fund a tx), and 'squashed' allows simpler membership proofs at the cost of needing to make a range proof for each input.

Squashed can also use the merged composition proof, I just separated 'merge' into its own tx type for comparisons.

## boogerlad | 2021-11-12T20:22:15+00:00
@UkoeHB 
> other variants where multiple people can fund a tx

Are there any wallets that allow for this via gui? This seems to be just a theoretical benefit. (multiple people funding a transaction vs multiple transactions just seems to save on fees and make the history a bit cleaner?)

## UkoeHB | 2021-11-12T20:24:49+00:00
> Are there any wallets that allow for this via gui? This seems to be just a theoretical benefit. (multiple people funding a transaction vs multiple transactions just seems to save on fees and make the history a bit cleaner?)

It is not possible with the current protocol. One example of the technique's use is the BCH crowdfunding system.

## ghost | 2021-11-12T23:20:27+00:00
I think Seraphis-Merge for collaborative funding sounds so interesting. 

## UkoeHB | 2021-11-12T23:34:34+00:00
> I think Seraphis-Merge for collaborative funding sounds so interesting.

Seraphis-Merge _prevents_ collaborative funding (which Seraphis-Concise/Seraphis-Squashed can do). It allows a bit smaller tx (96 bytes fewer per tx input).

## Rucknium | 2021-11-13T03:05:13+00:00
> This seems to be just a theoretical benefit.

@boogerlad @garth-xmr Collaborative funding is very real on the BCH blockchain. Over [9,000 BCH has been contributed to 85 projects](https://flipstarters.bitcoincash.network) through their Flipstarter system. At this point Flipstarter is the main funding mechanism for BCH development. You could almost say that it saved BCH from a devtax (the devtax advocates forked off anyway and their coin is now called eCash).

BCH's [AnyoneCanPay special transaction type](https://read.cash/@flipstarter/introducing-flipstarter-695d4d50) allow this permissionless, noncustodial, and self-hosted funding mechanism. For now, Monero has mostly relied on the CCS funding system, which is good but is also permissioned, centralized, and custodial. @emergent-reasons from BCH may be able to explain more. @plowsof recently sought and [received funding](https://monerodevs.org/) through a Flipstarter campaign.

## emergent-reasons | 2021-11-13T13:40:51+00:00
[Old introduction article](https://read.cash/@flipstarter/introducing-flipstarter-695d4d50) to Flipstarter. It's fundamentally the same thing as @mikehearn's Lighthouse. It's an entirely self-hosted, open source funding solution that uses trustless assurance contracts (all or nothing) where pledgers' money stays fully within their control until the moment that the funding transaction pulls together all the pledged inputs. I don't want to derail the discussion, so please feel free to contact me on the internet under variations of "emergent_reasons".

## UkoeHB | 2021-11-17T18:45:48+00:00
One design concern to keep in mind: Seraphis-Squashed requires range proofs for inputs. This may or may not entail limits on input counts (i.e. the 16-output limit was imposed when Bulletproofs were introduced).

Maybe someone can comment on why Bulletproofs led to a 16-output limit. For example, there could be a DDOS vector where a max-in/out transaction causes batch verification to slow down significantly (i.e. greatly increases the average verification cost across a batch).

UPDATE: I did some testing and found that per-proof verification improves with batching even if you combine many small-aggregate proofs (e.g. aggregates of 2 proofs) with few large-aggregate proofs (e.g. aggregates of 128 proofs). Basically, batching does not open a DDOS vector. However, it is still necessary to impose a limit on the number of tx inputs, since BP+ has a config limit on the number of proofs you can aggregate. One reasonable limit might be 112 inputs, 16 outputs (for a per-tx maximum of 128, which is a power of 2).

UPDATE2: The issue with large aggregations is, if a large proof aggregation (e.g. tx with many inputs) has no other large proofs to batch-verify with, then the per-range-proof verification cost of that large aggregation will be significantly higher than if it could be batched (~3-5x higher). This is the basic reason I investigated range proof splitting (so rare large aggregate proofs can be split into smaller proofs that will benefit more from batching).

## ArticMine | 2022-01-20T20:24:02+00:00
One question that comes to mind is the impact of GPU verification on verification cost per tx especially with large batch sizes 25 txs, 100 txs etc. if a performance improvement of 50x or more over a single core CPU can be achieved, this would be a material improvement that could enable for example a 256 ring size in Seraphis. Here is an example of performance improvements of 28.4x over a 8 core CPU and 8.4x over a 32 core CPU. https://www.dataversity.net/what-are-gpus-and-why-do-data-scientists-love-them/ 

## UkoeHB | 2022-01-21T16:03:08+00:00
While GPUs might significantly improve verification times, I have a couple concerns.

1) What is the engineering effort required to implement a GPU verifier?
2) I think the Seraphis upper tx througput limit would be ~10 TPS, with ~3.2 MB blocks (32 MB over 10 mins, for comparison to Bitcoin's 1 MB-per-10min-block that handles 7 TPS). TPS is constrained by the ability of common hardware to re-validate the blockchain. At ~10ms to verify a Seraphis tx with 128 ring size on a high-end CPU, you can verify 100 tx per second. That's maybe 30-70 on low-to-medium-end hardware. If the rate of new tx is >= the rate of verification, then a computer can never catch up. Therefore the upper limit on network throughput should be an order of magnitude lower than the rate of verification (~20 TPS for 11-member CLSAG, ~13 TPS for 64-member ring, ~10 TPS for 128-member ring, ~6 TPS for 256-member ring). If we allow GPUs to increase that limit, then we are basically saying _only_ people with GPUs can fully validate the chain (and _only_ people with GPUs can run full nodes).

## Hueristic | 2022-01-22T19:31:53+00:00
> only people with GPUs can run full nodes

Well that would be a non starter.

Can this code be optimized in assembler and any extensions leveraged?

## Rucknium | 2022-02-04T00:50:14+00:00
@UkoeHB Could you clarify this comment?:

>I think the Seraphis upper tx througput limit would be ~10 TPS...

Is this assuming use of a single core of a CPU or multiple cores? And if multiple cores, how many?

## UkoeHB | 2022-02-04T01:00:00+00:00
@Rucknium Yes that estimate is based on single-threaded verification.

## j-berman | 2022-02-05T06:58:44+00:00
Results of timing tests on experiments 1-4 on my medium-end-ish [core i7 1.8 GHz](https://cpu.userbenchmark.com/SpeedTest/891469/IntelR-CoreTM-i7-10510U-CPU---180GHz) + 32gb RAM, based on commit a63e39c6604d4ac493acee0f1c923dbefd50cca3.

To my eye, the relative efficiency gains seem fairly close.
________

**Experiment 1: reference set size (no batching)**

Fixed parameters: 2-input/2-output, no BP+ splitting, no tx verification batching. Note that the verification plot is logarithmic in the y-axis.

![Experiment 1](https://user-images.githubusercontent.com/26468430/152631860-62bfd6d8-f227-4f7b-8a9d-458a77475065.png)



**Experiment 2: reference set size (25 tx per batch)**

Fixed parameters: 2-input/2-output, no BP+ splitting, 25 tx per batch (normalized to cost/tx). Note that the verification plot is logarithmic in the y-axis.

![Experiment 2](https://user-images.githubusercontent.com/26468430/152631877-55981bf4-9451-41eb-b598-1312c2714e07.png)



**Experiement 3: reference set size decomposition**

Fixed parameters: 2-input/2-output, no BP+ splitting, no tx verification batching.

![Experiment 3](https://user-images.githubusercontent.com/26468430/152631894-3e45d224-02f9-49c5-9694-763bff94d6a8.png)




**Experiment 4: inputs**

Fixed parameters: 2-output, reference set decomposition 2^8, no BP+ splitting, no tx verification batching.

    For squashed tx: batching shown in legend.

These results are normalized to 1 input for each protocol type.

![Experiment 4](https://user-images.githubusercontent.com/26468430/152631915-b27b7b6f-944d-46d1-84b1-8119ef209c56.png)





## UkoeHB | 2022-02-21T20:02:27+00:00
Here are updated test results as of commit `86b253ebb9a6e47d621cc38e162b252c50b6fd46` (updated with small optimization: combine BP+ and grootle multiexponentiations into one operation).

There were two optimizations to grootle proofs:
1) use the A/B optimization from section 1.3 of [this paper](https://eprint.iacr.org/2019/1287.pdf) to allow smaller proofs (thanks to a certain someone for pointing this out!)
2) batch-verify a small part of the proof (~5-10% speedup I think)

I also added an `Sp-Plain` tx type, which uses the grootle proof style that [Spark](https://eprint.iacr.org/2021/1173.pdf) recommends (I used 2-byte weights for aggregating keys during verification).

Note that I removed the BP+-splitting experiments since the prior results suggested it wasn't a worthwhile approach.

## Results

#### Experiment 1: reference set size (no batching)

Fixed parameters: 2-input/2-output, no tx verification batching. Note that the verification plot is logarithmic in the y-axis.

![refset_1batch_ver](https://user-images.githubusercontent.com/37489173/155199137-efa767b0-3498-44bf-83ef-625faa3ec921.png)
![refset_1batch_size](https://user-images.githubusercontent.com/37489173/155199154-9215eb15-3195-4446-bcfe-ee230eb993aa.png)


#### Experiment 2: reference set size (25 tx per batch)

Fixed parameters: 2-input/2-output, 25 tx per batch (normalized to cost/tx). Note that the verification plot is logarithmic in the y-axis.

![refset_25batch_ver](https://user-images.githubusercontent.com/37489173/155199196-b281e47f-9780-4e06-9315-4d4c1f48d3ac.png)


#### Experiement 3: reference set size decomposition

Fixed parameters: 2-input/2-output, no tx verification batching.

![decomp_ver](https://user-images.githubusercontent.com/37489173/155199215-d9d4e6d2-702c-4b28-9fe2-01558922d65a.png)
![decomp_size](https://user-images.githubusercontent.com/37489173/155199231-df7b1a4d-e4a9-4190-b9a3-8489c06ffc85.png)


#### Experiment 4: inputs

Fixed parameters: 2-output, reference set decomposition 2^7, no tx verification batching.
- For squashed tx: batching shown in legend.

These results are normalized to 1 input for each protocol type.

![inputs_ver](https://user-images.githubusercontent.com/37489173/155199256-6804983c-7f48-4f73-b377-9f2543a934a3.png)
![inputs_size](https://user-images.githubusercontent.com/37489173/155199262-0b27959f-14e1-4e5a-91bf-b34128b79b41.png)


#### Experiment 5: 16 in/out batching

Fixed parameters: 16 inputs, 16 outputs, decomp 2^7

![16inout_ver](https://user-images.githubusercontent.com/37489173/155199290-e1743480-2003-4186-9e26-f5ffdae1fc6c.png)



## Discussion

- Partial batching of grootle proofs also means combining the verification of many proofs in one multiexponentiation, which provides a speedup just on its own. It is the combination of these factors (partial batching, larger multiexponentiations) that accounts for the unexpectedly significant speedups seen here.
- The grootle proof verification optimization means `Sp-Squashed` at 128 ring size can be batch-verified faster than `CLSAG` with 16 ring size.
- The 'plain' grootle style used in Spark is barely faster than `Sp-Concise`, at the cost of noticeably larger transactions.

# Action History
- Created by: UkoeHB | 2021-11-11T20:36:06+00:00
