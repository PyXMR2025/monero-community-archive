---
title: Ring Binning
source_url: https://github.com/monero-project/research-lab/issues/84
author: UkoeHB
assignees: []
labels: []
created_at: '2021-06-01T02:08:36+00:00'
updated_at: '2022-08-16T21:24:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
note: tx chaining was removed after [discussion](https://github.com/monero-project/research-lab/issues/84#issuecomment-877873623) (July 18, 2020)

## Table Of Contents

- [Abstract](#Abstract)
- [Motivation](#Motivation)
- [Algorithm summary](#Algorithm-summary)
- [Binning strategy](#Binning-strategy)
    - [Bin configuration details](#Bin-configuration-details)
    - [Bins](#Bins)
    - [Binning algorithm: tx construction](#Binning-algorithm-tx-construction)
        - [Constants and inputs](#Constants-and-inputs)
        - [Ring seed](#Ring-seed)
        - [Binning upper bound](#Binning-upper-bound)
        - [Selecting bins](#Selecting-bins)
        - [Selecting bin members](#Selecting-bin-members)
        - [Full ring member set](#Full-ring-member-set)
    - [Binning algorithm: tx validation](#Binning-algorithm-tx-validation)
    - [Modifications for small ring sizes (WIP)](#Modifications-for-small-ring-sizes-WIP)
- [Tx changes](#Tx-changes)
    - [Tx validation](#Tx-validation)
    - [Blockchain and tx hashes](#Blockchain-and-tx-hashes)
- [Rationale](#Rationale)
- [Backward compatibility](#Backward-compatibility)
- [License](#License)
- [References](#References)



## Abstract

Reference on-chain outputs for ring membership deterministically to minimize storage, and introduce a binning strategy to mitigate failures of the decoy selection distribution (e.g. gamma distribution).



## Motivation

Monero is planning to implement a next-gen protocol with sublinear scaling that should allow ring sizes on the order of 2^6 to 2^8 (64 to 256) (either Triptych or some alternative). Referencing each ring member individually is inefficient, so '[deterministic](https://arxiv.org/pdf/1704.04299/)' references are beneficial. 'Deterministic' means being able to recover an arbitrary number of on-chain indices from a small tuple of variables that include some kind of entropy.

As discussed in [An Empirical Analysis of Traceability in the Monero Blockchain](https://arxiv.org/pdf/1704.04299/), selecting ring decoys directly from a distribution that spans the entire ledger is not perfect. If an observer has special timing knowledge about a given transaction, and/or knows that the selection distribution does not match the true spend distribution, then they can gain a significant advantage when trying to guess the true spends in that transaction.

That problem can be mitigated by selecting 'clumps' of decoys from the ledger-spanning selection distribution. A 'clump' (or 'bin') of decoys is a small set of decoys that are located very close to each other on the ledger. This way, even if an observer can guess the age of a transaction's true spend to within a few hours or less, the true spend will still be hidden among some decoys.

It isn't ideal to _only_ select decoys that are close to the real spend. Even if some observers have special timing information about transactions, other observers may not. It is therefore useful to combine clumping/binning with selection from the ledger-wide distribution (recommended by [Foundations of Ring Sampling](https://petsymposium.org/2021/files/papers/issue3/popets-2021-0047.pdf)).

This proposal describes a deterministic ring member referencing strategy where clumps/bins of decoys are selected from a ledger-wide distribution. Privacy considerations are discussed where appropriate.



## Algorithm summary

To set the stage, I will briefly summarize the ring member referencing algorithm here (glossing over all the details, which can be found in the actual algorithm below). Each output spent by a transaction will have its own ring member reference tuple (set of variables to recover its set of ring members from).

1. Define `binning_upper_bound`, which is the index of the highest output in the ledger that can be referenced by this input. Defining this is necessary so interacting with the ledger-wide selection distribution is deterministic.
1. Choose a random output from a fixed range around the true spend `[true_spend_index - bin_radius, true_spend_index + bin_radius]`, which is equal to the width that bins will have.
1. Map that random output from the ledger-wide selection distribution (defined based on `binning_upper_bound`) to a uniform distribution with a CDF. Its value in the uniform distribution is denoted `mapped_real_spend_bin_center`.
1. Use a hash function and public entropy to generate `n` points in the uniform distribution.
1. Select a point `n'` at random from those `n` points. Define `bin_rotator = mapped_real_spend_bin_center - n' mod uniform_distribution.size()`.
1. Redefine all `n` points: `n += bin_rotator mod uniform_distribution.size()`. Note that `n'` will now equal `mapped_real_spend_bin_center`.
1. Map all `n` points from the uniform distribution back into the ledger-wide selection distribution with a reverse CDF. All points `mapped_n` are 'bin centers', the centers of each of the bins in the final ring member reference set. If bins should have only one member each (`bin_radius = 0`), then `mapped_n` can be treated directly as ring member references and you don't need to proceed further.
1. Around each bin center `mapped_n`, use a hash function and public entropy to generate `m` bin members from the range `[mapped_n - bin_radius, mapped_n + bin_radius]`.
1. In the bin that contains the real spend, randomly select a bin member `m'`. Define `bin_member_rotator = real_spend_index - m' mod 2*bin_radius + 1`.
1. Redefine all `m` points in all bins: `m = [(m - [mapped_real_spend_bin_center - bin_radius]) + bin_member_rotator mod 2*bin_radius + 1] + [mapped_real_spend_bin_center - bin_radius]`. Note that `m'` will now equal `real_spend_index`.
1. Return: hash function, public entropy, `binning_upper_bound`, `bin_rotator`, and `bin_member_rotator`. In practice, only `bin_rotator` and `bin_member_rotator` need to be unique between transaction inputs.



## Binning strategy

For a given tx, reference all its inputs' ring members with the following strategy inspired by [How to Squeeze a Crowd](https://isi.jhu.edu/~mgreen/mixing.pdf).


### Bin configuration details

Each transaction has:
- `binning_upper_bound` (varint): An on-chain index that sets the upper bound for the range of outputs that can be members of bins. There is one of these per transaction.

Each input has:
- `bin_rotator` (unsigned 8-byte integer): Rotates pseudo-randomly generated bin centers around the bin selection distribution.
- `bin_member_rotator` (varint): Rotates pseudo-randomly generated bin members within all bins.

Instead of public entropy, we will use a pseudo-random seed computed from parts of the transaction.


### Bins

Define the number of bins for each input.

- `NUM_BINS = floor(sqrt(RING_SIZE))`. [[[TODO: is logarithmic bin division better? other ideas? discussion is ongoing, however there is general consensus that in practice NUM_BINS should be >= current ring size (11)]]]
    - `RING_SIZE`: A constant defined by the Monero protocol.

Given `uneven_bins = RING_SIZE mod NUM_BINS`, define the number of bin members in each bin.

- After computing each bin's `bin_center` (discussed below), sort the bins. Let `index(bin, bins)` give the index of `bin` in vector `bins`.

```CPP
if (index(bin, bins) + 1 > NUM_BINS - uneven_bins)
    num_bin_members = ceil(RING_SIZE/NUM_BINS);
else
    num_bin_members = floor(RING_SIZE/NUM_BINS);
```

#### Rationale/Discussion

- We recommend `sqrt()` for deciding the number of bins to balance between selecting bins (ledger-scope) and bin membership (local-scope).
- If all bins can't have the same number of members, then the remainder is divided among the 'upper' bins. Monero's gamma distribution favors higher indices, so giving higher-indexed bins more members conforms with that idea.


### Binning algorithm: tx construction

Define the bin configuration details and obtain the list of ring members for each input.

#### Constants and inputs

```CPP
struct binning_config //[[[TODO: define these; consider using constructor to validate config settings]]]
{
    size_t BINNING_UPPER_BOUND_SELECTION_WIDTH;
    size_t BIN_RADIUS;
    size_t RING_SIZE;
    size_t NUM_BINS;
    ledger_distribution_config LEDGER_DIST_CONFIG;

    size_t max_index;   // max on-chain output index when making tx, assumed to be in 'spendable' range
    size_t min_index;   // min on-chain output index that can be used as a ring member
};

/// input variables
binning_config config;  // configuration for the binning algorithm
vector<size_t> spend_output_indices;    // indices of outputs to be spent

assert(max_index >= min_index);
assert(spend_output_indices.size() > 0);

/// leave early if there are not enough outputs on-chain to construct a ring
assert(height_from_output_index(max_index) - height_from_output_index(min_index) >= BINNING_UPPER_BOUND_SELECTION_WIDTH);

size_t min_binning_upper_bound_block = height_from_output_index(max_index) - BINNING_UPPER_BOUND_SELECTION_WIDTH;
size_t min_binning_upper_bound = get_last_output_index_of_block(min_binning_upper_bound_block);

assert(min_binning_upper_bound >= min_index);
assert(min_binning_upper_bound - min_index + 1 >= (2 x BIN_RADIUS + 1));
```

#### Rationale/Discussion

- To construct a ring, you need enough blocks to cover the maximum binning upper bound selection-range and enough outputs to span a full bin member selection-range (i.e. a single bin) below the minimum binning upper bound. In practice, if this were implemented, you'd have to wait until enough binning-eligible outputs have been added to the chain before a tx using binning can be constructed.
- The output at `max_index` must be 'spendable', meaning a transaction that references that output won't be rejected if immediately submitted to the network. Monero has a 10-block `DEFAULT_SPENDABLE_AGE` that disallows adding a transaction to the chain if the tx references an output from the previous 10 blocks.
    - If a transaction author is concerned that `DEFAULT_SPENDABLE_AGE` is not wide enough to protect their transaction from reorgs, then they should set `max_index` to an output from a sufficiently low block.

#### Ring seed

Compute a pseudo-random number for generating all the bins and bin members for the transaction's inputs. We use a pseudo-random number in place of public entropy.

```CPP
// ring entropy
u128 ring_seed = H("ring_seed", tx.key_images, tx.pseudo_output_commitments);
```

#### Rationale/Discussion

- The ring seed is a hash of both key images and pseudo output commitments for uniqueness between transaction attempts.
    - A robust Monero transaction builder always has unique pseudo-output commitments, either because at least one of them has a randomly-generated blinding factor (if there are more than one), or (if there is only one) because one blinding factor is set equal to the sum of the tx's new outputs' commitments' blinding factors (which are generated as hashes of sender-receiver shared secrets, which should be based on a randomly generated unique-per-tx-attempt transaction private key). This indirect inheritance of entropy can be considered 'not ideal' from a security standpoint, but is an optimization that piggybacks on a more serious security problem. If pseudo-output commitments made by a tx-builder are _not_ apparently random, this represents a serious flaw because badly generated pseudo-output commitments can reveal the amounts spent by a transaction.
    - Multiple transaction attempts will reveal the true spend due to ring member intersections. The only way to avoid this (in this proposal) would be to use `input_seed = H("input_seed", input.key_image)` instead of `ring_seed` (i.e. a unique seed per input, that is constant between tx attempts), and also use the same `binning_upper_bound` for each attempt.
- The ring seed is deterministic from tx details so tx verifiers can reconstruct the ring members for each input.
    - An alternative would be randomly generating a 16-byte `ring_entropy` and recording it explicitly in transactions. We don't see any meaningful advantage to that approach.

#### Binning upper bound

Select the binning upper bound, which is the maximum index that can be referenced by a bin. The same upper bound will be used for all inputs.

```CPP
size_t bound_selection_max;
size_t bound_selection_min;

/// block where highest spendable output can be found
size_t max_block_index = height_from_output_index(max_index);
bound_selection_max = max_block_index;

/// find highest real-spend
size_t max_spend_index{0};

for (const auto spend_output_index : spend_output_indices)
{
    assert(spend_output_index <= max_index);
    assert(spend_output_index >= min_index);

    if (spend_output_index > max_spend_index)
        max_spend_index = spend_output_index;
}

// block where highest real-spend can be found
size_t max_spend_block = height_from_output_index(max_spend_index);
assert(max_spend_block <= max_block_index);

/// binning upper bound must be >= all real-spends
bound_selection_min = max_block_index - BINNING_UPPER_BOUND_SELECTION_WIDTH;

if (bound_selection_min < max_spend_block)
    bound_selection_min = max_spend_block;

// rand_from_range<T>(): select integral of type T randomly from a range [a, b]
size_t binning_upper_bound_block = rand_from_range<size_t>(bound_selection_min, bound_selection_max);

/// binning upper bound is last output in the 'binning upper bound block'
size_t binning_upper_bound = get_last_output_index_of_block(binning_upper_bound_block);

/// set fee
u64 fee = get_fee_from_height(height_from_output_index(binning_upper_bound), priority);

return: binning_upper_bound, fee
```

#### Rationale/Discussion

- All inputs use the same `binning_upper_bound` to reduce storage in transactions. Beyond that, if there were unique upper bounds per input, then observers could use the average binning upper bound of multi-input transactions to more accurately estimate the time those tx were constructed.
- The `BINNING_UPPER_BOUND_SELECTION_WIDTH` is the region to randomly select a binning upper bound from. Selecting it from a range of blocks instead of using a fixed distance from `max_index` makes it harder for observers to analyze precisely when a transaction was constructed.
- Fees are set off the `binning_upper_bound` instead of `max_index`. In other words, the algorithmic minimum fee for the block containing the output with index `binning_upper_bound` should be used to set the transaction's fee. This mitigates observers' ability to use the transaction fee to estimate when a transaction was constructed.

#### Selecting bins

Deterministically select the bins for input `input_index`.

```CPP
/// set input seed
u128 input_seed = H("input_seed", ring_seed, input_index);

/// prepare bin centers
vector<u64> bin_centers_flattened;
assert(NUM_BINS);
bin_centers_flattened.resize(NUM_BINS);

for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
    // rand_from_seed<T>(seed): pseudo-randomly generate integral type T using input 'seed' to seed the generator
    // note: this must be uniformly distributed
    // - simple solution: return seed mod T:max
    //  - requires: either seed_type:max mod T:max == 0, OR seed_type:max >>> T:max
    //  - and must assume input seed is uniformly distributed
    bin_centers_flattened[bin_index] = rand_from_seed<u64>(H("bin_centers", input_seed, bin_index));


/// set bin_rotator

// 1. randomly select the real bin's center from around the output
size_t real_bin_max = spend_output_indices[input_index] + BIN_RADIUS;
size_t real_bin_min = spend_output_indices[input_index] - BIN_RADIUS;

// snap bin bounds to allowed range (with adjustments in case of integer overflow)
if (real_bin_max > binning_upper_bound || real_bin_max < spend_output_indices[input_index])
    real_bin_max = binning_upper_bound;

if (real_bin_min < min_index || real_bin_min > spend_output_indices[input_index])
    real_bin_min = min_index;

size_t real_bin_center = rand_from_range<size_t>(real_bin_min, real_bin_max);

// 2. randomly select a bin to be the 'real one'
size_t real_bin_index = rand_from_range<size_t>(0, bin_centers_flattened.size() - 1);

// 3.map the real bin center into the uniform distribution
// map_index_to_ledger_probability_dist(ledger-wide distribution config, 'index' normalized, 'max-index' of binning normalized)
// returns: (probability a randomly generated number in ledger-wide selection distribution over range [0, 'max-index'] is <= than 'index') x max(u64)
// [[[TODO: implementation (may need to take into account block:output relationship, e.g. density issue)]]]
u64 real_bin_center_flattened = map_index_to_ledger_probability_dist(LEDGER_DIST_CONFIG, real_bin_center - min_index, binning_upper_bound - min_index);

// 3. map the selected bin onto the real spend's bin center via 'bin_rotator'

// mod_subtract(a, b, c): a - b mod c
u64 bin_rotator = mod_subtract(real_bin_center_flattened, bin_centers_flattened[real_bin_index], max(u64));


/// rotate all the bins

// mod_add(a, b, c): a + b mod c
for (auto &bin_center : bin_centers_flattened)
    bin_center = mod_add(bin_center, bin_rotator, max(u64));


/// convert bin centers to real index space
vector<size_t> bin_centers;
bin_centers.resize(NUM_BINS);

for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
{
    // map_ledger_probability_dist_to_index(ledger-wide distribution config, 'probability', 'max-index' of binning normalized)
    // returns: index in range [0, 'max-index'] where random selection from the ledger-wide distribution on that range will have 'probability' probability of being <= the return value
    // [[[TODO: implementation]]]
    bin_centers[bin_index] = map_ledger_probability_dist_to_index(LEDGER_DIST_CONFIG, static_cast<double>(bin_centers_flattened[bin_index])/max(u64), binning_upper_bound - min_index) + min_index;

    // snap bin centers into the available range for bin members
    if (bin_centers[bin_index] > binning_upper_bound - BIN_RADIUS)
        bin_centers[bin_index] = binning_upper_bound - BIN_RADIUS;

    if (bin_centers[bin_index] < min_index + BIN_RADIUS)
        bin_centers[bin_index] = min_index + BIN_RADIUS;

    assert(bin_centers[bin_index] <= binning_upper_bound - BIN_RADIUS);
    assert(bin_centers[bin_index] >= min_index + BIN_RADIUS);
}


/// sort the bin centers and update real bin index accordingly

size_t real_bin_center = bin_centers[real_bin_index];
bin_centers.sort();

// if there are duplicates of the real bin's center, then randomly select which bin will contain the spent output
size_t min_candidate_index{NUM_BINS};
size_t max_candidate_index;

for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
{
    if (bin_centers[bin_index] == real_bin_center)
    {
        if (min_candidate_index == NUM_BINS)
            min_candidate_index = bin_index;

        max_candidate_index = bin_index;
    }
}

real_bin_index = rand_from_range<size_t>(min_candidate_index, max_candidate_index);

return: input_seed, bin_centers, bin_rotator, real_bin_index
```

#### Rationale/Discussion

- The real spend's bin center is uniformly distributed with respect to the real spend, so if the ledger-wide selection distribution across any bin's width is effectively uniform, then bin centers cannot be used to infer which bin member is the true spend.
    - If bins are too wide, so the ledger-wide selection distributin (and/or true spend distribution) is not effecitvely uniform across the width of each bin, then observers may be able to use the relative position of bin members with respect to bin centers to gain an advantage when guessing which bin member is the true spend.
- The method of generating bin centers in the uniform distribution, rotating them onto the real spend's bin center, then mapping the bin centers into the ledger-wide selection distribution, is conceptually equivalent to selecting, at random, one of the permutations of selections from the ledger-wide selection distribution that just so happens to include the real spend's bin center. Since the transaction author chooses which generated bin center to map onto his real spend at random, observers cannot use `bin_rotator` to deduce which bin has the true spend unless the ledger-wide selection distribution is flawed.
- Note that section [Bins](#Bins) requires bins to be sorted because the bins with the highest bin centers will have more ring members than lower bins if there is a remainder when dividing ring members among bins (in the next section).

#### Selecting bin members

Deterministically select the bin members for input `input_index`.

```CPP
/// select bin members

vector<vector<size_t>> bin_members_per_bin;
bin_members_per_bin.resize(NUM_BINS);

for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
{
    // get_num_bin_members(which bin, number of bins, number of ring members) - defined by secion 'Bins'
    size_t num_bin_members = get_num_bin_members(bin_index, NUM_BINS, RING_SIZE);
    assert(num_bin_members);
    assert(num_bin_members <= 2 x BIN_RADIUS + 1);
    bin_members_per_bin[bin_index].resize(num_bin_members);

    size_t bin_min_index = bin_centers[bin_index] - BIN_RADIUS;

    // deterministically generate bin members in the range [bin_min_index, bin_max_index]
    for (size_t bin_member_index{0}; bin_member_index < num_bin_members; bin_member_index++)
    {
        bool was_duplicate;
        size_t duplicate_nonce{0};

        // prevent duplicates within each bin
        do
        {
            was_duplicate = false;

            // mod_large(a, c): a mod c, where a >> c
            bin_members_per_bin[bin_index][bin_member_index] = mod_large(rand_from_seed<u128>(H("bin_members", input_seed, bin_index, bin_member_index, duplicate_nonce)), 2 x BIN_RADIUS + 1) + bin_min_index;

            for (size_t i{0}; i < bin_member_index; i++)
            {
                if (bin_members_per_bin[bin_index][i] == bin_members_per_bin[bin_index][bin_member_index])
                {
                    was_duplicate = true;
                    ++duplicate_nonce;

                    break;
                }
            }
        } while (was_duplicate);
    }
}


/// in real bin, randomly select a bin member to be the real one
size_t real_bin_member_index = rand_from_range<size_t>(0, bin_members_per_bin[real_bin_index].size() - 1);


/// define the bin member rotator
size_t bin_member_rotator;
size_t real_bin_min_index = bin_centers[real_bin_index] - BIN_RADIUS;

bin_member_rotator = mod_subtract(spend_output_indices[input_index] - real_bin_min_index, bin_members_per_bin[real_bin_index][real_bin_member_index] - real_bin_min_index, 2 x BIN_RADIUS + 1);


/// rotate all bin members and sort each bin
for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
{
    size_t real_bin_min_index = bin_centers[bin_index] - BIN_RADIUS;

    for (auto &bin_member : bin_members_per_bin[bin_index])
        bin_member = mod_add(bin_member - real_bin_min_index, bin_member_rotator, 2 x BIN_RADIUS + 1) + real_bin_min_index;

    bin_members_per_bin[bin_index].sort();
}


/// get real bin member index post-sorting

// note: there should be no duplicate bin members
for (size_t bin_member_index{0}; bin_member_index < bin_members_per_bin[real_bin_index].size(); bin_member_index++)
{
    if (bin_members_per_bin[real_bin_index][bin_member_index] == spend_output_indices[input_index])
    {
        real_bin_member_index = bin_member_index;

        break;
    }
}

return: bin_members_per_bin, bin_member_rotator, real_bin_member_index
```

#### Rationale/Discussion

- Within each bin, bin members are selected pseudo-randomly then they are all rotated so that one of the bin members in the true spend's bin lands on the true spend. Since all bins have the same width, and the within the true spend's bin the bin member to rotate on to the true spend is selected at random by the transaction author, an observer cannot use `bin_member_rotator` to infer anything about which bin contains the true spend, nor which bin member in any given bin is more/less likely to be the true spend.
    - As noted in the previous section, if the ledger-wide selection distribution is not effectively uniform across the width of each bin, then observers will have an advantage when trying to guess which bin members are more/less likely to be the true spend.
- For simplicity, the algorithm above permits bins to have the same center, and for bin members to be duplicates between different inputs or between different bins (but not within the same bin). [[[TODO: better for performance not to test for duplicates? ok for performance to test for duplicates more rigorously?]]]

#### Full ring member set

```CPP
/// concatenate the bins together to get the full ring-member set; also get the real-spend's index in the ring
vector<size_t> all_bin_members;
all_bin_members.reserve(RING_SIZE);
size_t real_bin_member_index_in_ring{0};
bool passed_real;

for (const auto &bin_members : bin_members_per_bin)
{
    if (bin_members == bin_members_per_bin[real_bin_index])
    {
        real_bin_member_index_in_ring += real_bin_member_index;

        passed_real = true;
    }
    else if (!passed_real)
        real_bin_member_index_in_ring += bin_members.size();

    for (const auto bin_member: bin_members)
        all_bin_members.emplace_back(bin_member);
}

return: all_bin_members, real_bin_member_index_in_ring
```


### Binning algorithm: tx validation

Recover the ring members of each input in a transaction `tx` from the bin configuration details.

```CPP
/// inputs
Tx tx;
binning_config config;


/// recover ring members
u128 ring_seed = H("ring_seed", tx.key_images, tx.pseudo_output_commitments);
vector<vector<size_t>> all_ring_members_per_input;]

assert(NUM_BINS);
assert(tx.binning_upper_bound >= min_index + 2 x BIN_RADIUS + 1);

for (size_t input_index{0}; input_index < tx.inputs.size(); input_index++)
{
    u128 input_seed = H("input_seed", ring_seed, input_index);

    /// generate bin centers and rotate them
    vector<u64> bin_centers_flattened;
    bin_centers_flattened.resize(NUM_BINS);

    for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
        bin_centers_flattened[bin_index] = rand_from_seed<u64>(H("bin_centers", input_seed, bin_index));

    for (auto &bin_center : bin_centers_flattened)
        bin_center = mod_add(bin_center, tx.inputs[input_index].bin_rotator, max(u64));

    /// convert bin centers to real index space
    vector<size_t> bin_centers;
    bin_centers.resize(NUM_BINS);

    for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
    {
        // [[[TODO: implementation]]]
        bin_centers[bin_index] = map_ledger_probability_dist_to_index(LEDGER_DIST_CONFIG, static_cast<double>(bin_centers_flattened[bin_index])/max(u64), tx.binning_upper_bound - min_index) + min_index;

        if (bin_centers[bin_index] > tx.binning_upper_bound - BIN_RADIUS)
            bin_centers[bin_index] = tx.binning_upper_bound - BIN_RADIUS;

        if (bin_centers[bin_index] < min_index + BIN_RADIUS)
            bin_centers[bin_index] = min_index + BIN_RADIUS;

        assert(bin_centers[bin_index] <= tx.binning_upper_bound - BIN_RADIUS);
        assert(bin_centers[bin_index] >= min_index + BIN_RADIUS);
    }

    bin_centers.sort();

    /// generate bin members
    vector<vector<size_t>> bin_members_per_bin;
    bin_members_per_bin.resize(NUM_BINS);

    for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
    {
        size_t num_bin_members = get_num_bin_members(bin_index, NUM_BINS, RING_SIZE);
        assert(num_bin_members);
        bin_members_per_bin[bin_index].resize(num_bin_members);

        size_t bin_min_index = bin_centers[bin_index] - BIN_RADIUS;

        // deterministically generate bin members in the range [bin_min_index, bin_max_index]
        for (size_t bin_member_index{0}; bin_member_index < bin_members_per_bin[bin_index].size(); bin_member_index++)
        {
            bool was_duplicate;
            size_t duplicate_nonce{0};

            // prevent duplicates within each bin
            do
            {
                was_duplicate = false;

                bin_members_per_bin[bin_index][bin_member_index] = mod_large(rand_from_seed<u128>(H("bin_members", input_seed, bin_index, bin_member_index, duplicate_nonce)), 2 x BIN_RADIUS + 1) + bin_min_index;

                for (size_t i{0}; i < bin_member_index; i++)
                {
                    if (bin_members_per_bin[bin_index][i] == bin_members_per_bin[bin_index][bin_member_index])
                    {
                        was_duplicate = true;
                        ++duplicate_nonce;

                        break;
                    }
                }
            } while (was_duplicate);
        }
    }

    /// rotate all bin members
    assert(tx.inputs[input_index].bin_member_rotator < 2 x BIN_RADIUS + 1);

    for (size_t bin_index{0}; bin_index < NUM_BINS; bin_index++)
    {
        size_t bin_min_index = bin_centers[bin_index] - BIN_RADIUS;

        for (auto &bin_member : bin_members_per_bin[bin_index])
            bin_member = mod_add(bin_member - bin_min_index, tx.inputs[input_index].bin_member_rotator, 2 x BIN_RADIUS + 1) + bin_min_index;

        bin_members_per_bin[bin_index].sort();
    }

    /// concatenate bins for full set of ring members
    all_ring_members_per_input[input_index].reserve(RING_SIZE);

    for (const auto &bin_members : bin_members_per_bin)
        for (const auto bin_member: bin_members)
            all_ring_members_per_input[input_index].emplace_back(bin_member);
}

return: all_ring_members_per_input
```

#### Rationale/Discussion

- Note that there is a lot of duplication between this section and the earlier sections, so in practice the algorithm can be condensed.


### Modifications for small ring sizes

This algorithm can be adjusted so all bins only have one member each, which can applied as an optimization/upgrade to Monero's current transaction protocol. Doing so would reduce input reference bytes from `(num_inputs x ring_size x varint)` to `(varint + num_inputs x (u64 + varint))`.

- Set:
    - `NUM_BINS = RING_SIZE`
    - `BIN_RADIUS = 0`
    - These settings imply that `get_num_bin_members()` will only return `1`, and that each bin center will equal its lone bin member.
- Exclude `bin_member_rotator` from bin configuration details.



## Tx changes

Modify the transaction input structure and the form of the message signed by transaction inputs.

- As @TheCharlatan explains [below](https://github.com/monero-project/research-lab/issues/84#issuecomment-860070191), the `txin_to_key` struct should contain a vector of commitments to outputs (i.e. hashes of each output).
- The `txin_to_key` struct should also contain the values `bin_rotator` and `bin_member_rotator` introduced by this proposal.
- The transaction prefix hash should include `binning_upper_bound` from this proposal:

```
m_p = Hash(version, unlock_time, binning_upper_bound, {txin_i}_i, {txout_i}_i, extra)
```


### Tx validation

When you encounter a tx to validate, recover the ring members for each input from the bin configuration details defined in this proposal.


### Blockchain and tx hashes

1. A transaction hash includes all tx data.
2. Output references (e.g. all binning details) are stored in the blockchain as part of tx structs. Since output references and the outputs themselves are part of tx hashes, the blockchain can only be re-validated with the correct output references for each tx.



## Rationale

#### Why not use the binning strategy from [this paper](https://arxiv.org/pdf/1704.04299/)?

- The paper's strategy requires more data. Individual bins are referenced with independent identifiers, instead of implicitly via a hash function and pseudo-random seed.
- In the paper's strategy, bins are implementation-defined, which means they can't be enforced by the consensus protocol. The result would be less transaction uniformity if multiple transaction-builders use different methods to define bins.
- Bin selection in the paper is relatively inferior to this proposal. In the paper, the real spend's bin is 'added' to the set of decoy bins, whereas in this proposal we select a set of bins directly from the ledger-wide selection distribution that just so happens to include the real spend's bin. Doing so eliminates the ability of observers to guess which bin is least likely to have been selected from the ledger-wide selection distribution.
    - Note that this proposal's approach does not solve analysis that spans many transactions. For example, if all transactions have a true spend in a bin that is exactly 1 day old, then when looking at the bins selected by many transactions, the over-selection of 1-day-old bins will stand out.
- Bin member selection in the paper is somewhat haphazard and does not address edge cases effectively (e.g. true spends that don't land in deterministic bins).



## Backward compatibility

This proposal changes the structure of tx and tx validation rules, so it requires a hard fork. It is well-suited to being implemented in the same hard fork that rolls out Triptych (or a similar next-gen tx protocol with large ring sizes), but is also [compatible](Modifications-for-small-ring-sizes) with Monero's current transaction protocol.



## License

[MIT license](https://opensource.org/licenses/MIT)



## References

- [An Empirical Analysis of Traceability in the Monero Blockchain](https://arxiv.org/abs/1704.04299)
- [How to Squeeze a Crowd](https://isi.jhu.edu/~mgreen/mixing.pdf)
- [Foundations of Ring Sampling](https://petsymposium.org/2021/files/papers/issue3/popets-2021-0047.pdf)


# Discussion History
## sedited | 2021-06-12T15:40:30+00:00
This proposal has a lot of potential to fix many of the UX problems of Monero. If constructed carefully it could also get rid of the 10 confirmation spending requirement, allow transaction mempool replaceability, and fee bumping techniques. To make the above proposal work, the signature message structure needs to be changed. Adopting some of the notation for MLSAG message construction from the [hardware wallet paper](https://eprint.iacr.org/2020/281.pdf) the current signature message structure `m` is:

`txin_i`is the input struct
`txout_j` is the output struct
 `ECDH_i` represent encrypted amounts 
`C_i` are the output commitments 
 `m_p = Hash(version, unlock_time, {txin_i}_i, {txout_i}_i, extra)` is the transaction prefix hash
`m = Hash(m_p || Hash({ECDH_i}_i || {C_i^0}_i) || Hash({rangeProofData_i}_i))` is the signature message

In the code `txin_i` and `txin_out` are encoded in the `transaction_prefix`, `m_p` in the above notation, in [cryptonote_basic.h](https://github.com/monero-project/monero/blob/master/src/cryptonote_basic/cryptonote_basic.h#L163). Both are encoded as a collection of types, two of which, `txin_to_script`/`txout_to_script` and `txin_to_scripthash`/`txout_to_scripthash`, are unused. `txin_gen` encodes coinbase inputs, while `txin_to_key`/`txout_to_key` are used for all other transactions. `txout_to_key` contains the output one time key.

`txin_to_key` is defined with the fields:
```
struct txin_to_key { 
    uint64_t amount;
    std::vector<uint64_t> key_offsets;
    crypto::key_image k_image;  // double spending protection
```

The transaction prefix hash is what needs to be changed. Instead of `txin_to_key` encoding a vector of key offsets, it should encode a vector of commitments to the specific output. This can be achieved by creating a new input type struct and adding a vector of the one-time public key of the output, the output index in the transaction (the analog of vout in Bitcoin) and the transaction id of the transaction containing the output to the `txin_to_key` struct. This ensures that a truly unique output is selected from.

The transaction ID construction currently uses the same `transaction_prefix_hash` as well. Any malleability caused by adding the floating bin index later on would not change the transaction id if it would still be reusing the function for the signature message hashing. At the same time this is problematic, since data outside of a transaction would need to be hashed as well. Instead, two distinct transaction ID's can be computed, similar to what Bitcoin has done to eliminate transaction malleability. One  including the binning information and one without.

## boogerlad | 2021-06-24T04:32:55+00:00
Probably a stupid question: if both transactions need to be constructed before the first one is sent, how does that fix the UX issue in Monero regarding the 10 confirmation spending requirement? Couldn't the user just construct one transaction with multiple outputs?

## UkoeHB | 2021-06-24T04:39:27+00:00
@boogerlad I think the idea is if you spend an output added to the chain in the recent 10 blocks, then if the chain gets reorged, your tx can survive if the other tx also survives. The output you spend would be 'floating', so miners can adjust the floating offset when there is a reorg.

## boogerlad | 2021-06-24T05:05:30+00:00
I see. Can step 2 and 3 be swapped?

## UkoeHB | 2021-06-24T05:40:21+00:00
Sure they can, the steps are just demonstrating tx chaining (making tx when output you are spending doesn't exist in chain yet).

## Mitchellpkt | 2021-06-30T16:53:14+00:00
Clever construction. Just one thought about maintaining transaction indistinguishability and fungibility:  if we allow _any_ transaction to have a floating ring member, then the protocol should enforce that _every_ transaction has a floating ring member. Then it won't stand out when people do use the feature.

## vtnerd | 2021-06-30T20:47:09+00:00
I find the concept of a hash-based bin selection interesting, because assuming the algorithm is reproducible across CPUs(!), the transaction size should be much smaller than listing each ring member. Or did I misunderstand that part of the proposal?

> @boogerlad I think the idea is if you spend an output added to the chain in the recent 10 blocks, then if the chain gets reorged, your tx can survive if the other tx also survives. The output you spend would be 'floating', so miners can adjust the floating offset when there is a reorg.

If attempting to spend immediately, then this also leaks the real spend? If so, then this is certainly a "non-starter" if a user has to choose between privacy and immediate spending. This hurts the on-chain privacy of everyone.

## UkoeHB | 2021-06-30T21:48:32+00:00
> I find the concept of a hash-based bin selection interesting, because assuming the algorithm is reproducible across CPUs(!), the transaction size should be much smaller than listing each ring member. Or did I misunderstand that part of the proposal?

Yes it is hash-based and reproducible across CPUs.

> If attempting to spend immediately, then this also leaks the real spend? If so, then this is certainly a "non-starter" if a user has to choose between privacy and immediate spending. This hurts the on-chain privacy of everyone.

@vtnerd If all tx have a floating index in the same range (relative to chain height), then observers won't necessarily know if floating index in last 10 blocks is due to a fast spend or randomness.

The key to this is defining a floating output selection zone (constants `BINNING_UPPER_BOUND_SELECTION_WIDTH` and `MIN_ALLOWED_WIDTH_FLOATING`) that doesn't give away information in most cases.

## Gingeropolous | 2021-07-01T22:34:48+00:00
love the binning and chaining. I'm pondering the specific use-case of the 1 floating ring member. IMO, an ideal monero protocol would be able to survive a complete netsplit - i.e., 2 subnetworks form that end up completely isolated from each other. Then, at some other time, the two networks become reconnected. Afaiu, it should be theoretically possible for the two subnetworks blockchains to reform into a single chain in a massive re-org. For instance, in bitcoin I think this is possible - the txs in the alt chain would just be dumped to the txpool, and they get mined back into the mainchain. 

From what I'm understanding from this proposal, the 1 floating ring member wouldn't accommodate such an event. 

I mean, I get it, the single floating ring member is designed for a specific use case of tx-chaining and not really the possible but improbable netsplit. However, I'm always a fan of making the protocol more robust. cockroach factor. E.g., can monero be designed to survive nuclear war?  

## UkoeHB | 2021-07-01T22:47:53+00:00
@Gingeropolous the 'Reorg' section discusses netsplits. You can't have both a binning strategy (to minimize reference storage) and recover from arbitrarily large netsplits, but you can recover from small reorgs.

## sethforprivacy | 2021-07-02T12:37:20+00:00
Relevant article on a real-world use-case that would benefit from this *today*:

https://comit.network/blog/2021/07/02/transaction-presigning/

> It is our assumption that anything that relies on joint-outputs and pre-signing spending transactions doesn't actually work on present day Monero. We haven't done an extensive analysis on what this affects but our guess is that this applies to at least anything Layer2 but likely also to other blockchain protocols developed for Monero. Most "interesting" blockchain protocols today work on the basis of a joint-owned output with spending transactions which leak secrets when broadcast. As long as we want to remain trustless, we have to create valid spending transactions before the actual output gets mined, otherwise we are dependent on cooperating with the other party to unlock our funds.

## vtnerd | 2021-07-02T16:41:18+00:00
> The key to this is defining a floating output selection zone (constants BINNING_UPPER_BOUND_SELECTION_WIDTH and MIN_ALLOWED_WIDTH_FLOATING) that doesn't give away information in most cases.

"in most cases" is not a good phrase in the given context. The problem is that the hash-based approach should require some information leakage about the real spend, correct? And technically this occurs in all contexts afaik.

In other words, with this approach the signer has to "work-backwards" from the real-spend and put some information so that the verifier is guaranteed to use it in the ring. The signer must do this because a purely hash-based approach will never "select" the desired output. So instead, we have this scheme where the signer tries to obfuscate the real spend, but in so doing is leaking more information than the current approach.

This scheme is just too complicated and is going to have subtle leaks to be acceptable.

## UkoeHB | 2021-07-02T17:28:55+00:00
> The problem is that the hash-based approach should require some information leakage about the real spend, correct? And technically this occurs in all contexts afaik.

I'm not sure what you mean by this. The scheme described here only leaks:
- a ballpark of when the tx was constructed (a function of `BINNING_UPPER_BOUND_SELECTION_WIDTH`); I don't see any way to _not_ leak this while using a gamma distribution for ring members (i.e. we already leak this).
- if `BINNING_UPPER_BOUND_SELECTION_WIDTH + MIN_ALLOWED_WIDTH_FLOATING` is too large, then the probability of the floating output being the real spend will be greater than `1/RING_SIZE` (I believe there is a theoretical optimal size for this zone based on the gamma distribution; these are non-consensus constants as well, and can be adjusted algorithmically). Note that if there is no floating index, no binning upper bound width, and all real spends match the gamma distribution, then in this scheme the probability any ring member is the real spend will be `1/RING_SIZE`.
- if the floating output is outside the random selection zone width, then it is almost guaranteed to be the real spend; I view this as a vector for 'opting-out' of privacy guarantees. It is impossible for Monero to have tx chaining without this vector.

## vtnerd | 2021-07-02T17:40:37+00:00
> I'm not sure what you mean by this. The scheme described here only leaks:

There is more information about the real spend than the current approach. Or rather, there is more subtle metadata about the real-spend in these floating values than the current dead-simple approach. The problem stems from the hash-based approach for ring selection - it forces the signer to commit to some value with a relationship to the real spend. 

>  I view this as a vector for 'opting-out' of privacy guarantees

Which hurts the privacy of others typically because this output cannot be used in a ring past or present. Monero has been moving away from optional features for this reason, particularly with ring-selection. The size of the ring isn't even signer selectable for instance.

## UkoeHB | 2021-07-02T17:56:47+00:00
> Or rather, there is more subtle metadata about the real-spend in these floating values than the current dead-simple approach. The problem stems from the hash-based approach for ring selection - it forces the signer to commit to some value with a relationship to the real spend.

Metadata leakage about the real spend, in the context of a floating output, is mostly independent of how ring members are selected (the use of hashes here is irrelevant because everything important is randomized). If we had pure random selection over a gamma distribution, then the floating index would still leak information. Maybe even the same amount of information, because with large rings you can more accurately extrapolate the 'distribution upper bound' (i.e. the max index when selecting from the gamma distribution).

The problem is all ring members must be known when constructing a transaction. Practically speaking, this means all non-spends must exist on-chain already. If all your decoys are selected from on-chain, then the chain height when you selected ring members cannot be greatly obfuscated. Floating outputs that are too far away from that chain height cannot be hidden.

Do you have a suggestion how tx chaining can be done better? Or are you arguing tx chaining should not be supported at all?

## vtnerd | 2021-07-02T18:50:30+00:00
> Metadata leakage about the real spend, in the context of a floating output, is mostly independent of how ring members are selected (the use of hashes here is irrelevant because everything important is randomized). If we had pure random selection over a gamma distribution, then the floating index would still leak information. Maybe even the same amount of information, because with large rings you can more accurately extrapolate the 'distribution upper bound' (i.e. the max index when selecting from the gamma distribution).

You need to elaborate on all cases where the real spend is leaked. So far it appears when tx-chaining is used, it _definitely_ leaks the real spend to miners and anyone watching the mempool. I don't see how this is an acceptable tradeoff if Monero's privacy can be weakened simply by using a feature to use outputs quicker. And as I already stated, this hurts the privacy of **everyone** on-chain because it reduces the anonymity set.

What I'm also pointing out, and you appear to be dodging through unclear language, is that even in the normal case metadata is leaked. This actually easiest to see in the verification algorithm. The signer does not control the seed for the randomizer function, but still has to get the verifier to select the "real" output in a "bin". So there's a connection between the real-spend and these offset values (that are stored on-chain), that is not present in the current approach

> The problem is all ring members must be known when constructing a transaction. Practically speaking, this means all non-spends must exist on-chain already. If all your decoys are selected from on-chain, then the chain height when you selected ring members cannot be greatly obfuscated. Floating outputs that are too far away from that chain height cannot be hidden.

Yes, I understand the problem you are trying to solve.

> Do you have a suggestion how tx chaining can be done better? Or are you arguing tx chaining should not be supported at all?

I have no reason to "not support" tx chaining (i.e. the question is non-sense, of course I would want something like tx chaining in Monero). However, tx chaining should not be added if it reduces privacy. I don't see how its possible to have both, unless the tx size is increased dramatically.

## UkoeHB | 2021-07-02T19:53:17+00:00
> You need to elaborate on all cases where the real spend is leaked.

 "**warning**: if floating_index - binning_upper_bound > BINNING_UPPER_BOUND_SELECTION_WIDTH + MIN_ALLOWED_WIDTH_FLOATING, then an input is guaranteed to be flagged as floating=real & real=chained"

Aside from this
- if `BINNING_UPPER_BOUND_SELECTION_WIDTH + MIN_ALLOWED_WIDTH_FLOATING` is too large, then the probability of a floating output being real is `> 1/RING_SIZE` due to overlap with the gamma distribution (if you integrate the gamma distribution from [binning upper bound, chain height at tx construction], and `result/(integrate entire curve) > 1/RING_SIZE`, then the chance the real spend is floating will be disproportionate to other ring members)
- observers can use {unknown at the time of analysis} real-world heuristics to discern the true spend; things like differences between the true spend distribution and the gamma distribution, patterns of use for tx chaining, etc.

> I don't see how this is an acceptable tradeoff if Monero's privacy can be weakened simply by using a feature to use outputs quicker. And as I already stated, this hurts the privacy of everyone on-chain because it reduces the anonymity set.

This argument is fine with me and definitely needs to be discussed. I don't have a strong opinion either way - tx chaining was requested by other people. However, I'd like to disentangle it from more technical criticisms of the scheme.

> What I'm also pointing out, and you appear to be dodging through unclear language, is that even in the normal case metadata is leaked. This actually easiest to see in the verification algorithm. The signer does not control the seed for the randomizer function, but still has to get the verifier to select the "real" output in a "bin". So there's a connection between the real-spend and these offset values (that are stored on-chain), that is not present in the current approach

Rather than dodging it, these sections are **WIP** and I have not gotten around to explaining why it works. I agree if the offsets leak any metadata then the scheme is broken. The scheme is supposed to:
1. if the real spend is in a bin, randomize the 'center' of the bin relative to the true spend index
2. use a uniformly distributed offset to map one hash-derived bin center onto the real spend's bin center
3. within the real spend's bin, use a uniformly distributed offset to map one hash-derived bin member onto the real spend's index

If each of those is uniformly distributed, then no information is leaked about which bin member is the real spend. In other words, it is equally probable that the offsets map any of the hash-generated things onto the real bin/bin member.

> I have no reason to "not support" tx chaining (i.e. the question is non-sense, of course I would want something like tx chaining in Monero). However, tx chaining should not be added if it reduces privacy.

I don't appreciate the antagonistic pedantics. Everything 'added' to Monero is 'supported' by Monero, so arguing that tx chaining shouldn't be 'added' means you are arguing it shouldn't be 'supported' (in my view of the meaning of these words....).

## vtnerd | 2021-07-02T20:39:31+00:00
> If each of those is uniformly distributed, then no information is leaked about which bin member is the real spend. In other words, it is equally probable that the offsets map any of the hash-generated things onto the real bin/bin member.

I doubt this claim is accurate, but I'm going to need something closer to pseudo-code/Python before going further - the real-spend is the only one where the offsets were manipulated to work and these offsets are recorded permanently in the blockchain.

> I don't appreciate the antagonistic pedantics. Everything 'added' to Monero is 'supported' by Monero, so arguing that tx chaining shouldn't be 'added' means you are arguing it shouldn't be 'supported' (in my view of the meaning of these words....).

Your original statement was "Or are you arguing tx chaining should not be supported at all?", and I was stating that I can be against your approach, but in-favor of the feature in general. Perhaps there is no way to add tx-chaining without reducing privacy (for others) or increasing tx size, in which case the feature should not be supported. That's typically how the Monero community has done feature selection in the past at least.

If the ring-selection algorithm can filter out definitely leaked real-outputs, this changes the argument because other participants are _less_ affected by tx-chaining (it lowers potential anonymity set size but not the ring security). I believe this is possible, but likely complicates the ring-selection even further.



## vtnerd | 2021-07-02T20:45:55+00:00
> If the ring-selection algorithm can filter out definitely leaked real-outputs, this changes the argument because other participants are less affected by tx-chaining (it lowers potential anonymity set size but not the ring security). I believe this is possible, but likely complicates the ring-selection even further.

As a quick follow-up: everytime a ring member is identified as a real-spend, it weakens the privacy of other rings where it was used as a "dummy". This was why ring size 1 was banned, but this case is different if all participants can see the "leak" during transaction construction. It's still on the edge of what the Monero community has supported in the past as this creates two distinct sets of Monero transactions, whereas all of the analytic researchers are trying to eliminate anything different in transactions. Their ideal is all uniform cryptographic data.

## UkoeHB | 2021-07-02T21:39:11+00:00
> As a quick follow-up: everytime a ring member is identified as a real-spend, it weakens the privacy of other rings where it was used as a "dummy". This was why ring size 1 was banned, but this case is different if all participants can see the "leak" during transaction construction. It's still on the edge of what the Monero community has supported in the past as this creates two distinct sets of Monero transactions, whereas all of the analytic researchers are trying to eliminate anything different in transactions. Their ideal is all uniform cryptographic data.

I had similar thoughts. My take was if most txs that need to use floating outputs can be 'hidden' among normal txs, then a floating offset style may be worthwhile. If most txs using floating outputs cannot be hidden (e.g. because floating outputs are mostly used for tx-chaining, and the delay between tx signing and floating output being added to chain is too big in most of those cases), then floating offsets are no better than a 1-member ring, so we might as well support two input types (pure binning, and 1-member rings) if we want floating outputs.

When the proposal gets more fleshed out I will be sure to discuss this aspect of the topic, thank you for bringing it up.

## vtnerd | 2021-07-02T22:28:58+00:00
> If most txs using floating outputs cannot be hidden (e.g. because floating outputs are mostly used for tx-chaining, and the delay between tx signing and floating output being added to chain is too big in most of those cases), then floating offsets are no better than a 1-member ring

In this scenario, the privacy of Monero has arguably dropped considerably. We've allowed people a technique to "shoot themselves in the foot" (Monero is private, unless you do this one thing!), and the total anonymity set has dropped weakening any future gains from Triptych. The more the discussion continues, I don't see how I could support the floating offsets idea (when it is a defacto 1-member ring).

In fact, why not just allow tx chaining with 1 member rings? Its less complicated and more clear on whats actually happening. Which...

>  we might as well support two input types (pure binning, and 1-member rings) if we want floating outputs.

If this approach is taken,  "pure binning" would need a separate discussion for its inclusion because it is no longer required for tx-chaining to work. Although you've suggested as such with the title "Tx Chaining and Ring Binning".

## UkoeHB | 2021-07-02T23:17:51+00:00
> In fact, why not just allow tx chaining with 1 member rings? Its less complicated and more clear on whats actually happening.

The problem from my pov is, for example, that all tx trying to get around the 10-block lock time would have to use the 1-member rings. But at least some of those tx could be obfuscated among slower spends using this proposal, so there is an opportunity cost.

While outputs spent by 1-member rings can be blackballed, they can only be blackballed _after_ they have been spent. Rings created before then can be polluted. Plus, you can just as easily blackball floating outputs from this proposal that are unequivocally real-spends.

- (1-member rings): can blackball all outputs after they have been spent
- (this proposal): can blackball all outputs that are unequivocally real-spends after they have been spent; _some_ of the remaining outputs may not be heuristically neutral

So, if I were to advocate 1-member rings over this proposal, I would have to think that the pollution of ring signatures with heuristically non-neutral outputs is a greater cost (combined with the chain cost of useless ring signatures created for unequivocal real-spends) than the benefit of allowing those outputs (plus a set of outputs that are heuristically neutral) to be spent in ring signatures. I don't have enough information to judge this trade-off.

> The more the discussion continues, I don't see how I could support the floating offsets idea

Floating offsets are very easy to chop out of this proposal if ultimately not desired.

## vtnerd | 2021-07-03T04:55:49+00:00
> Plus, you can just as easily blackball floating outputs from this proposal that are unequivocally real-spends.

Then why not just use 1-member rings in these cases. Its simpler for all parts of the code, and there's no hiding the weakened privacy/security in obscure algorithms.

> some of the remaining outputs may not be heuristically neutral

Can you clarify this point? A proposal where the real-spend is known initially but is later hidden isn't acceptable because it creates "land-mines" in the output selection process. It gives chain-analysis companies that are constantly monitoring the mempool an advantage over Monero wallets that are not constantly monitoring the mempool.

So to repeat - if a real-spend can be determined after leaving the node of origin, then the 1-member ring approach should be used. Its simpler and is effectively the same thing. The community dropped such rings previously though, which is ultimately why I have been critical of this part of the idea.

> Floating offsets are very easy to chop out of this proposal if ultimately not desired.

Ok, but the binning approach still requires much scrutiny as I suspect it also leaks metadata.

## UkoeHB | 2021-07-03T05:49:29+00:00
> > some of the remaining outputs may not be heuristically neutral

> Can you clarify this point? 

In this proposal, a floating output with an index way higher than the binning upper bound is unequivocally a real spend (unless the tx author is messing around or there is a wonky implementation). However, floating outputs close to the upper bound might be real spends or decoys.

If those floating outputs are heuristically neutral, then there exist no heuristics that, when used, increase the observer's chance of correctly guessing if one of them is a true spend. There is no way to guarantee that no such heuristic exists, so for the sake of argument we can assume that at least some proportion of floating outputs may not be heuristically neutral (i.e. guessing that they are the true spend has `> 1/RING_SIZE` chance of being correct).

These hypothetical floating outputs with heuristic weaknesses would not exist in the 1-member ring scenario, so the fact they would be able to pollute ring signatures is a cost that must be added to the analysis (even if in practice it is insignificant).

**Note**: Even pure ring signatures over a gamma distribution might not be heuristically neutral if the true spend distribution does not match the gamma distribution. An analyst who knows the true spend distribution has a heuristic advantage for detecting true spends.

> A proposal where the real-spend is known initially but is later hidden isn't acceptable because it creates "land-mines" in the output selection process.

This is not possible here.

> So to repeat - if a real-spend can be determined after leaving the node of origin, then the 1-member ring approach should be used. Its simpler and is effectively the same thing. The community dropped such rings previously though, which is ultimately why I have been critical of this part of the idea.

I don't have strong opinions about the best approach. My goal is to finish the proposal, explain it as best I can, and adjust it according to other people's discussion. Perhaps talking to those who are invested in floating outputs (be it via this proposal or simple 1-member rings) would be more productive toward reaching a final consensus @TheCharlatan.

The reason I did not propose 1-member rings originally was two-fold:
- at least some floating output real-spends can be obfuscated by ring signatures
- it isn't clear how beneficial it would be to support both this proposal and 1-member rings (i.e. for unequivocal floating output spends), compared to the implementation effort

## vtnerd | 2021-07-03T14:50:16+00:00
> Note: Even pure ring signatures over a gamma distribution might not be heuristically neutral if the true spend distribution does not match the gamma distribution. An analyst who knows the true spend distribution has a heuristic advantage for detecting true spends.

Why "ring binning"? Ignore "tx chaining" for second - would this design still be recommended without that use case? Does it result in smaller transaction sizes, etc.? Because it certainly does not improve on the heuristics of a bad RNG for the gamma distribution stage.

Edit: Above you mentioned O(1) scaling, but this scheme does not appear to be that. So I'm primarily looking for a comparison of your actual approach instead of an abstract case. 

> at least some floating output real-spends can be obfuscated by ring signatures

This portion of my response is about "tx chaining" (spending outputs currently in the mempool or less than 10 blocks).

Can you list the scenarios where this is possible. Let me help you - is the transaction being broadcast multiple times or is the miner manipulating the transaction? Because if there are re-broadcasts by the wallet this gives away some metadata to people watching the mempool (it was a quick spend). OR if the miners can do it, what magic allows them to adjust the indexes without knowing the real spend (they would have to know the real spend to set the indexes)? Just walk through the transaction chaining scenario a bit more.

I'm insisting on specifics here because I suspect once its implemented if people knew how it worked they would reject it (1-member rings achieve the same thing without the obfuscation and complicated algorithm).

> it isn't clear how beneficial it would be to support both this proposal and 1-member rings (i.e. for unequivocal floating output spends), compared to the implementation effort

This portion of my response is about "tx-chaining"

1-member rings are dead simply compared to this approach. And I'm not supporting 1-member rings but they allow transaction chaining easily.

## UkoeHB | 2021-07-03T20:21:24+00:00
> Why "ring binning"? Ignore "tx chaining" for second - would this design still be recommended without that use case? Does it result in smaller transaction sizes, etc.? Because it certainly does not improve on the heuristics of a bad RNG for the gamma distribution stage.

Yes it would still be recommended.
- "We show this binned sampling ensures privacy even in spite of a compromised sampling distribution." [source](https://arxiv.org/pdf/1704.04299.pdf)
- The storage required is very small: varint + num_inputs*(u8 + varint [+ varint for floating offsets]). There aren't any other proposals to compare it with, but I doubt you will find anything that uses less storage.

> > at least some floating output real-spends can be obfuscated by ring signatures
> Can you list the scenarios where this is possible. Let me help you - is the transaction being broadcast multiple times or is the miner manipulating the transaction? Because if there are re-broadcasts by the wallet this gives away some metadata to people watching the mempool (it was a quick spend). OR if the miners can do it, what magic allows them to adjust the indexes without knowing the real spend (they would have to know the real spend to set the indexes)? Just walk through the transaction chaining scenario a bit more.

Miners can adjust the floating offset, they don't need to know which output is the real spend. Check out the '**Reorgs**' section of the proposal for a full discussion.

A ring with 128 ring members looks like this:
[ 127 members: deterministic from binning details ] | 1 floating member

The floating member is referenced like `floating_index = floating_offset + binning_upper_bound`. The `floating_offset` is not signed by tx authors, so miners can change it to match the real location of the floating member, or tx authors can set it _after_ the tx has been constructed. In tx chaining, the real spend is the floating member. You wait until the tx you chain on top of is added to the ledger before setting the floating offset value.

> > at least some floating output real-spends can be obfuscated by ring signatures

Every tx input has a floating member. Most of those will be decoys. Tx authors with decoy floating members must select the decoys from a range of blocks above the `binning_upper_bound`. This range has a certain maximum width. If a real-spend floating member is within that range, then an observer won't know for sure if it is a decoy or real-spend. If they have good heuristics, they may be able to guess with probability of success `> 1/RING_SIZE` if the floating member is real or not.

Tx authors won't always know in advance if their real-spend floating member will fall into the 'decoy range'. This is because the final index of that member may be unknown.

## vtnerd | 2021-07-03T20:55:57+00:00
> Yes it would still be recommended.
>
>* "We show this binned sampling ensures privacy even in spite of a compromised sampling distribution." source
> * The storage required is very small: varint + num_inputs*(u8 + varint [+ varint for floating offsets]). There aren't any other proposals to compare it with, but I doubt you will find anything that uses less storage.

The source paper has less variables and the selection algorithm is vastly more simple. Can you explain why the changes from the paper? It appears to be for the reorg/chaining case. This also means the claims of the paper no longer apply and analysis of your altered approach needs to be done. The approach in the paper is simpler than what you have here.

> Miners can adjust the floating offset, they don't need to know which output is the real spend. Check out the 'Reorgs' section of the proposal for a full discussion.
>
>  In tx chaining, the real spend is the floating member. You wait until the tx you chain on top of is added to the ledger before setting the floating offset value.

Ok, your alteration to the paper is more clear now. You incorrectly answered my question above though. **Nodes constantly watching the mempool have an advantage.** The recipient always knows when transaction chaining has been enabled (the floating offset is the real spend), people watching the mempool can assume its the real spend when `floating_offset` is spent before 10 blocks (or whatever cutoff), but the blockchain is not guaranteed to store this transaction within the 10-block (or whatever) cutoff.

I now understand why your answers have been a bit all over the place (from my perspective), there isn't a guaranteed way to avoid some of these transactions after-the-fact. I'm still advocating for 1-member rings instead of your proposal for this reason. Also a reminder to anyone bothering to read this: the paper supplied above has a different algorithm and scheme that is simpler, and I would support that scheme over this one (although I haven't done enough reading to say whether the claims in that paper are accurate).

## UkoeHB | 2021-07-03T21:55:06+00:00
> You incorrectly answered my question above though. Nodes constantly watching the mempool have an advantage. The recipient always knows when transaction chaining has been enabled (the floating offset is the real spend), people watching the mempool can assume its the real spend when floating_offset is spent before 10 blocks (or whatever cutoff), but the blockchain is not guaranteed to store this transaction within the 10-block (or whatever) cutoff.

This response confuses me. Decoy floating members can and should be selected from the most recent 10 blocks. Why wouldn't they be? It's true that the presence of a floating output in the last 10 blocks may be a heuristic that increases the likelihood of it being a real spend, but it is not any 'guaranteed' information. This does not contradict my earlier comments.

How would a recipient know anything more than observers about inputs to a tx? EDIT: ah, if the recipient knows they are receiving an output from a chained tx, then they will know the floating output is a real-spend.

It's true that nodes watching the mempool have a slight advantage. They witness all reorgs, so they will have some slight timing information about transactions that a later observer won't have. I had not considered this (not that my failure to think of something warrants your aggressive attitude).

> I now understand why your answers have been a bit all over the place (from my perspective), there isn't a guaranteed way to avoid some of these transactions after-the-fact. I'm still advocating for 1-member rings instead of your proposal for this reason.

You seem to be assuming most people would use the blackball tool. Maybe @SamsungGalaxyPlayer can give some insight on how many people actually use it in practice.

## vtnerd | 2021-07-03T23:00:05+00:00
> This response confuses me. Decoy floating members can and should be selected from the most recent 10 blocks. Why wouldn't they be? It's true that the presence of a floating output in the last 10 blocks may be a heuristic that increases the likelihood of it being a real spend, but it is not any 'guaranteed' information. This does not contradict my earlier comments.

Yes, I probably responded too quickly previously -

If Bitcoin is any indication, there would be a strong-bias towards the `floating_index` being the real spend. And the gamma distribution cannot select within this range (did I miss that part? there's multiple overlapping knobs in this thing), so that changes heuristics/statistics tremendously. Its basically telling you that x% of the time, the `floating_index` will be the real spend. This should help chain-analysis ... ?

>  I had not considered this (not that my failure to think of something warrants your aggressive attitude).

I'm being harsh because you made statements like `"We show this binned sampling ensures privacy even in spite of a compromised sampling distribution." source`, but failed to mention that the algorithm presented here differs from the paper significantly. In some pretty major ways in fact. Even using the hash function as a seed (its not _entropy_ as claimed) forces the signer to go through a gate that requires additional knobs to "hide" the real spend. This should also help statistics/heuristics identify the real-spend, but its going to take a while for me to show that one.

And even after all that, the binning approach is sub-optimal to the `bin_size == 1` algorithm that's currently in use (because it reduces the gamma distribution sampling making the "noise" smaller).

> How would a recipient know anything more than observers about inputs to a tx? EDIT: ah, if the recipient knows they are receiving an output from a chained tx, then they will know the floating output is a real-spend.

Sorry got my explanation jumbled up. The entire thing is dodgy because when a new block arrives, anyone can broadcast a chained transaction for outputs in the last block. Transactions that go out immediately are more likely to be real-spends than ones delayed even by 20 seconds, etc. Its basically telling mempool watchers the real-spenders. I suppose wallets could have a randomized delay/backoff that matches a gamma distribution towards the 10-block cutoff ... but there's no way to enforce this at the policy at the node (aside from our current approach of banning outputs within last 10 blocks).

The problem is "ahh my wallet just selected a 9-block wait time, no way, let me kludge that to 1 block in my copy of the code".

EDIT: In comparison, the current approach allows for multiple alternate decoys to be selected in the 10 block during the gamma distribution stage.

> You seem to be assuming most people will use the blackball tool. Maybe @SamsungGalaxyPlayer can give some insight on how many people actually use it in practice.

I'm assuming that most people will not use the blackball tool. It should be trivial for signers to "skip" 1-member ring outputs but the idea is crap anyway (there's a reason why they were banned).

`floating_index` is trickier and basically requires the blackball approach afaik. And even then its someone doing messy heuristics that will never be exactly what chain-analysis companies have.

## UkoeHB | 2021-07-06T00:50:13+00:00
> I'm being harsh because you made statements like "We show this binned sampling ensures privacy even in spite of a compromised sampling distribution." source, but failed to mention that the algorithm presented here differs from the paper significantly.

I was responding to your question "Why "ring binning"?" Binning is recommended by that paper, hence 'the use of binning' is still recommended. I was not using that quote to claim this proposal's design is flawless. Hopefully this clears up any misunderstanding...

> Even using the hash function as a seed (its not entropy as claimed) forces the signer to go through a gate that requires additional knobs to "hide" the real spend. This should also help statistics/heuristics identify the real-spend, but its going to take a while for me to show that one.

I was admittedly using the term 'entropy' haphazardly. The `ring_seed` (renamed) borrows entropy from the pseudo-output commitments.

If the hash-based generation of bins and bin members has any statistical flaws, then I will happily revise this proposal. My intention is not to break Monero... just to pursue the most efficient possible ring binning algorithm. The tradeoff between complexity and tx size can be made after alternatives are well understood (a work-in-progress for everyone, I think).

> EDIT: In comparison, the current approach allows for multiple alternate decoys to be selected in the 10 block during the gamma distribution stage.

Not sure what you mean. Due to the 10-block locktime enforced by consensus, 'the current approach' cannot reference outputs in the last 10 blocks.

> And even then its someone doing messy heuristics that will never be exactly what chain-analysis companies have.

I agree with this. It is easier to assess the implications of a 'floating output' with a concrete algorithm. Can a floating output scheme with some elements of privacy exist? I want to at least analyze something concrete, try to address criticisms with concrete adjustments, etc. I have neither the authority nor coding competence to force Monero into using this stuff.

Maybe if you were the only stakeholder in the system I wouldn't bother going through the effort, but floating outputs and a maximally-optimized algorithm for binning were both requested by @TheCharlatan, so this discussion will not find its conclusion that easily.

## vtnerd | 2021-07-06T19:03:43+00:00
> I was responding to your question "Why "ring binning"?" Binning is recommended by that paper, hence 'the use of binning' is still recommended. I was not using that quote to claim this proposal's design is flawless. Hopefully this clears up any misunderstanding...

Yes but I have some criticisms of the paper. They don't appear to do an apples-to-apples comparison - the charts don't directly compare number of outputs, making the analysis misleading (i.e. `bin_size == 1, num_bins == 5` is `outputs == 5` whereas `bin_size == 2, num_bins == 5` is `outputs == 10`). Their argument is that the `bin_size == 2` is better because more outputs are referenced - which is true - but `10` independently selected outputs would be even better.

From a privacy-only standpoint, `bin_size == 1, num_bins == 128` > `bin_size == 4, num_bins == 32` even though `outputs == 128` in both cases. So above where you have `floor(sqrt(RING_SIZE - 1))` with a question about logarithm - NO! The formula should be `num_bins == ring_size`.

In summary, the Monero community should select the `num_bins` based on transaction size (exactly as we do now with `ring_size`), then select `bin_size` based on some rough performance numbers. Using the `bin_size` to "scale down" the transaction is reducing the security/privacy. Or else scrap bin selection mode altogether for complexity reasons.

> I was admittedly using the term 'entropy' haphazardly. The ring_seed (renamed) borrows entropy from the pseudo-output commitments.

The hash function is not taking entropy, its creating a "gate" (no different than an AND gate in digital signatures) that a signer must "solve" in order to get their output in the ring. This was not in the original "binning" paper and should be removed from the proposal entirely as it (almost certainly) weakens the security.

> If the hash-based generation of bins and bin members has any statistical flaws, then I will happily revise this proposal. My intention is not to break Monero... just to pursue the most efficient possible ring binning algorithm. The tradeoff between complexity and tx size can be made after alternatives are well understood (a work-in-progress for everyone, I think).

The analysis in the paper has to be completely thrown away because this proposal is too different.

> Not sure what you mean. Due to the 10-block locktime enforced by consensus, 'the current approach' cannot reference outputs in the last 10 blocks.

The problem is allowing just a single referenced output in the 1-10 block range. If a gamma distribution were done from 1-infinitity, then multiple outputs would be referenced in the 1-10 block frequently. This provides more "cover" in the expected spend range and is preferable to a single floating index.

> I agree with this. It is easier to assess the implications of a 'floating output' with a concrete algorithm. Can a floating output scheme with some elements of privacy exist? I want to at least analyze something concrete, try to address criticisms with concrete adjustments, etc. I have neither the authority nor coding competence to force Monero into using this stuff.

Yes, you make all members floating instead. By making just one member floating, you are leaking critical statistical information. It necessarily creates an outlier. The other option is zero floating members.

> Maybe if you were the only stakeholder in the system I wouldn't bother going through the effort, but floating outputs and a maximally-optimized algorithm for binning were both requested by @TheCharlatan, so this discussion will not find its conclusion that easily.

I don't see how @TheCharlatan / atomic swap concerns supercede privacy concerns. And atomic swaps don't need the binning approach afaik.

## UkoeHB | 2021-07-06T20:36:19+00:00
> This was not in the original "binning" paper and should be removed from the proposal entirely as it (almost certainly) weakens the security.

This is comical. Please read [the paper cited by the proposal](https://isi.jhu.edu/~mgreen/mixing.pdf) and address your 'feelings' toward that paper. I'd like to hear concrete criticisms instead of speculation. Setting aside floating outputs, the proposal uses an RSS with Inverse Transform Sampling to get bin loci, and a second simple RSS to define bin members.

The distinction between bins and bin members (as opposed to pure selection over the gamma distribution) is based on the Moser paper, which quite reasonably argues that binning mitigates failures of the selection distribution (either due to the selection being inaccurate to ground truth, or because the analyst has special timing knowledge about the transaction). These are failures Monero does not handle right now. Frankly, even if the Moser paper has crap analysis and a crap recommendation for a binning algorithm, the existence of these failures and the potential of binning to solve them seems fairly obvious.

> From a privacy-only standpoint, bin_size == 1, num_bins == 128 > bin_size == 4, num_bins == 32 even though outputs == 128 in both cases. So above where you have floor(sqrt(RING_SIZE - 1)) with a question about logarithm - NO! The formula should be num_bins == ring_size.
> 
> In summary, the Monero community should select the num_bins based on transaction size (exactly as we do now with ring_size), then select bin_size based on some rough performance numbers. Using the bin_size to "scale down" the transaction is reducing the security/privacy. Or else scrap bin selection mode altogether for complexity reasons.

This is just you making bald assertions.

> The problem is allowing just a single referenced output in the 1-10 block range. If a gamma distribution were done from 1-infinitity, then multiple outputs would be referenced in the 1-10 block frequently. This provides more "cover" in the expected spend range and is preferable to a single floating index.
> 
> Yes, you make all members floating instead. By making just one member floating, you are leaking critical statistical information. It necessarily creates an outlier. The other option is zero floating members.

It is not efficient for all outputs to be floating if there are 128 ring members. It is only efficient to have a few floating outputs at most.

I am open to increasing the number of floating outputs to 3-5 (~6-15 bytes per input), which isn't a horrible idea at least.

> I don't see how @TheCharlatan / atomic swap concerns supercede privacy concerns. And atomic swaps don't need the binning approach afaik.

If privacy was the only concern, then we would have ringsize = num_outputs_that_exist. Ah, but scaling matters. So, we might as well explore complexity if it improves scaling right? Just like we went through all that trouble with Bulletproofs+ for 96 bytes per tx? The privacy implications of floating outputs are worth exploring compared to the benefits (whatever they may be), and @vtnerd's opinion isn't enough to make that discussion end.

## Gingeropolous | 2021-07-07T02:53:08+00:00
i think a lot can be gained here if 1) we think in the reality of having larger ringsizes and then 2) we think about treating the "recent window", whatever it may be (10 blocks, or things that are in the mempool), as a bin.

The larger ringsize (64 seems modestly acceptable with triptych) would allow ~5.8 11-member bins to exist. That way, we could make the entire first bin (the one that floats in this proposal) an 11 member subset (or we could make it the 1.8 share of the 5.8), which could mitigate the "oh, the floating member is obviously the real input" problem.

this sort of hacks on our existing model. Our existing model states that 11 ring members are fine. Therefore, a recent window bin of 11 members should also be fine. 

And as the ringsize increases (say, 128 is deemed the magic number), then we have 11.6 bins of 11 member bins. 

Yo I heard you like rings. So I put some rings in your rings. 

is kinda what i imagine it as.

but if this is totally off base then usher me out. 

## vtnerd | 2021-07-07T03:42:44+00:00
> This is comical. Please read the paper cited by the proposal and address your 'feelings' toward that paper. I'd like to hear concrete criticisms instead of speculation. Setting aside floating outputs, the proposal uses an RSS with Inverse Transform Sampling to get bin loci, and a second simple RSS to define bin members.

ELI5 (for at least one person that PMed me): This proposal contains a new, not yet analyzed, technique for specifying outputs in a transaction. This is **separate idea from both binning and floating indexes**. The original source paper, referenced by @UkoeHB , talked about binning only (no discussion of "floating indexes" nor this new technique for referencing bins). I think the onus should be on the presenter of the new "tech" (@UkoeHB ) and not on other MRL regulars in this case.
...
I don't see how this technique is going to withstand any scrutiny. There's no entropy provided with the transaction. You cannot do this deterministically unless the index is hidden with a ECDLP or similar (and its not). I realize this provides amazing space savings, but this looks to be primarily obfuscation.

> It is not efficient for all outputs to be floating if there are 128 ring members. It is only efficient to have a few floating outputs at most.
>
> I am open to increasing the number of floating outputs to 3-5 (~6-15 bytes per input), which isn't a horrible idea at least.
>
> It is not efficient for all outputs to be floating if there are 128 ring members. It is only efficient to have a few floating outputs at most.
>
> I am open to increasing the number of floating outputs to 3-5 (~6-15 bytes per input), which isn't a horrible idea at least.

Monero has never selected scaling/space savings over a reduction in privacy. Creating separate "floating indexes" is reducing the privacy because it ruins the uniformity in the decoy selection process. And the ~6-15 bytes per input comparison is assuming that your hash-based approach is accepted. There is no reduction in space efficiency when compared to our current approach, for instance.

> If privacy was the only concern, then we would have ringsize = num_outputs_that_exist. Ah, but scaling matters. So, we might as well explore complexity if it improves scaling right? Just like we went through all that trouble with Bulletproofs+ for 96 bytes per tx? The privacy implications of floating outputs are worth exploring compared to the benefits (whatever they may be), and @vtnerd's opinion isn't enough to make that discussion end.

Again, Monero has never chosen to reduce security/privacy at the behest of scaling, and the formula you provided for `num_bins` is invalid. The important number for security/privacy is how many RNG values are injected into the decoy system. The source paper doesn't make this clear unfortunately.

So to get the same level of security with "binning" (that Monero has right now), at least 11 bins are needed. If we want something comparable to ring-size 128 then `num_bins == 128`, etc. This is why I suggested choosing "bins" like we do rings currently (bandwidth/storage), then adjust `bin_size` based on CPU/disk throughput.

For those ELI5 folks, if the community decides `num_bins == 16, bin_size == 8` then that is sensible, but `num_bins == 8, bin_size == 16` is going "backwards" compared to `ring_size == 11` . This is due to _less_ RNG values for decoy selection (10 vs 7), but if `num_bins == 16` then RNG decoy values are increased from 11 to 15, etc. The amount of RNG entropy is the critical value.


## vtnerd | 2021-07-07T03:54:43+00:00
> The larger ringsize (64 seems modestly acceptable with triptych) would allow ~5.8 11-member bins to exist. That way, we could make the entire first bin (the one that floats in this proposal) an 11 member subset (or we could make it the 1.8 share of the 5.8), which could mitigate the "oh, the floating member is obviously the real input" problem.

Remember 5.8 bins is roughly equivalent to a ring size of 5 in terms of entropy. I would recommend a bin size of 11 or greater to equal our current security levels.

## vtnerd | 2021-07-07T03:56:50+00:00
> > The larger ringsize (64 seems modestly acceptable with triptych) would allow ~5.8 11-member bins to exist. That way, we could make the entire first bin (the one that floats in this proposal) an 11 member subset (or we could make it the 1.8 share of the 5.8), which could mitigate the "oh, the floating member is obviously the real input" problem.
> 
> Remember 5.8 bins is roughly equivalent to a ring size of 5 in terms of entropy. I would recommend a bin size of 11 or greater to equal our current security levels.

Sorry "bin size of 11 or greater" should've read "11 bins or greater"

## Gingeropolous | 2021-07-07T04:31:24+00:00
right, so 128 seems to be the minimum total ringsize to accommodate 11 bins of 11 members.  This would also allow for the single bin floating member to have the (almost) exact same properties of an existing monero transaction (11 ring members), therefore (perhaps) satisfying the "Monero has never selected scaling/space savings over a reduction in privacy" coda. Coda? 

Anyway, i sprinkle in some perhaps in there because now the recent bin has 11 members, but those 11 members aren't from the entire chain... they're from a smaller subset, so perhaps its even "stronger" than existing monero transactions, because its potentially 1 real output and 10 fake outputs all within the span of say, 200 outputs, as opposed to, the whole chain? 

> The important number for security/privacy is how many RNG values are injected into the decoy system. 

right, so, as you mentioned, the paper describes splitting up the existing 11 ring members into 2 bins, so really you've provided a way for the attacker to say "its somewhere in these two bins", which are more temporally related than 11 unbounded ring members distributed (via gamma) over the entire chain. So the graph narrows by a funnel of 2, really, instead of 11. Because the blockchain is a timestamping device. 

( cough ringsize a bajillion cough )

## Gingeropolous | 2021-07-07T04:38:50+00:00
i mean, in one version of this binning, it might make sense to have the bins variable sizes, like starting at 20 members for the first most recent, then down to 15, then 10 etc. This would integrate the dogma that the most recent outputs are usually the real ones.

wheres the stats peoples. 

## UkoeHB | 2021-07-07T06:54:25+00:00
> ELI5 (for at least one person that PMed me): This proposal contains a new, not yet analyzed, technique for specifying outputs in a transaction. This is separate idea from both binning and floating indexes. The original source paper, referenced by @UkoeHB , talked about binning only (no discussion of "floating indexes" nor this new technique for referencing bins). I think the onus should be on the presenter of the new "tech" (@UkoeHB ) and not on other MRL regulars in this case.

Sorry but this paragraph tells me you still haven't read the right paper: https://isi.jhu.edu/~mgreen/mixing.pdf. You seem pretty confident despite ignoring my citation.

> I don't see how this technique is going to withstand any scrutiny. There's no entropy provided with the transaction.

More speculation, and a dubious statement. Each transaction's pseudo-output commitments are effectively randomly generated, and each transaction's key images are unique on-chain. If using these to seed the ring PRNG is not enough, then I'd like to hear a **concrete** reason, not speculation. I would be very happy to hear **concrete** flaws in the proposal, because I want to pursue **concrete** improvements.

> the formula you provided for num_bins is invalid

Calling it invalid is pure nonsense. It is a real formula that works. Is there a better idea? Maybe... and look - I even put in [[[TODO]]] asking for other ideas. What's up with the toxic attitude?

Are you imagining a difference between `RING_SIZE` and the total number of decoys? `RING_SIZE` is determined by verification speed of transactions, and always equals the total number of outputs referenced by an input. It is only a question of how, or if, those ring members should be divided into bins.

I can't help but *appreciate* how you neglected to even comment on the potential utility of binning. Can't throw me a bone? lmao

> The important number for security/privacy is how many RNG values are injected into the decoy system.

Are you claiming that a separate entropy source is required for each decoy? This is the first I have heard about such an assumption, compared to having one entropy source that may be stretched to multiple PRNG outputs.

In this proposal (for the binning component) there are several inputs that can contain entropy: ring seed (key images & pseudo-output commitments), random selection of the real bin's locus, random selection of which generated bin to map onto the real bin's locus, random selection of which bin member in the real bin to map onto the real spend.

## Gingeropolous | 2021-07-07T12:28:42+00:00
yeah, there seem to be 3 distinct issues here - tx chaining, ring binning, and the hash encoding of ring members. 

I thought the general gestalt was that ring binning is an improvement in privacy. @vtnerd , i get the sense you think otherwise - do you know of any research on this side of the coin?

tx-chaining seems to be a desired feature that has the potential to reduce privacy compared to existing monero if parameters (mostly ringsize) are wrong, but that could just be my interpretation. 

hash-encoding of ring members is a data compression technique whose utility is also greatly affected by ringsize. 

Perhaps, in order to make this conversation and those around these potential protocol modifications more coherent, should we break apart this issue into the 3 distinct issues that exist? They really seem independent, and mostly dependent on the existence of large ring sizes IMO. 

## vtnerd | 2021-07-07T18:01:13+00:00
> Sorry but this paragraph tells me you still haven't read the right paper: https://isi.jhu.edu/~mgreen/mixing.pdf. You seem pretty confident despite ignoring my citation.

You switched papers on me from first to second post, and I admittedly skipped the reference section at the bottom of the original post. 

After reading the paper, where is `P` over a prime field `F`? Since `M==1` there should be a constant referenced with the transaction ... ? The actual implementation is going to be complex, so its understandable if this was intentionally omitted for brevity. Some inline references to the paper would've helped too.

> More speculation, and a dubious statement. Each transaction's pseudo-output commitments are effectively randomly generated, and each transaction's key images are unique on-chain. If using these to seed the ring PRNG is not enough, then I'd like to hear a concrete reason, not speculation. I would be very happy to hear concrete flaws in the proposal, because I want to pursue concrete improvements.

This isn't speculation, anyone who has studied ZKP systems can see that this is really close to a ZKP AND gate, and I didn't see anything analogous to a DLP (the source paper has a random `k` and `P` over a prime field).

> Calling it invalid is pure nonsense. It is a real formula that works. Is there a better idea? Maybe... and look - I even put in [[[TODO]]] asking for other ideas. What's up with the toxic attitude?

I already gave my idea. Ignore the total number of pubkeys going into the signature because that is misleading. Instead, look at the number of rings/bins with bin members >1 being a (potential) "bonus" to what we have now. But do not drop the number of bins below the current ring threshold as this is reducing the security (see next paragraphs).

> Are you imagining a difference between RING_SIZE and the total number of decoys? RING_SIZE is determined by verification speed of transactions, and always equals the total number of outputs referenced by an input. It is only a question of how, or if, those ring members should be divided into bins.

The security comes from the entropy in selecting the bins/rings. A quick reductio absurdum - if you had 1 bin with 128 members this clearly has less entropy than 128 bins with 1 member. With only 1 bin, the sender is leaking the timeframe of the real spent output to within <10mins or so. The more bins, the more "timeframes"/entropy into the system. So number of bins should be considered roughly equivalent to the number of members in a ring.

> I can't help but appreciate how you neglected to even comment on the potential utility of binning. Can't throw me a bone? lmao

I'm not sure if this technique is that useful (at the moment). Its not making things worse from a privacy perspective but might be putting more constraints on throughput for minimal privacy gains.

> Are you claiming that a separate entropy source is required for each decoy? This is the first I have heard about such an assumption, compared to having one entropy source that may be stretched to multiple PRNG outputs.

No, I was (and still am) unsure of how this could work because the construction just seems off. In the source paper `P` should be hiding the real spend in the prime field, but what about here?

-------------------
@Gingeropolous 

>I thought the general gestalt was that ring binning is an improvement in privacy. @vtnerd , i get the sense you think otherwise - do you know of any research on this side of the coin?

I think my above response clears up my thoughts on ring binning. Most people think in terms of total pubkeys going into the signature algorithm as the security level, which is what makes the binning approach attractive, but its also useful to think in terms of "timeslots". 128-rings has 128 unique time slots, but 64x2 "binning" has 64 unique time slots.

Some of this is difficult to compare/quantify, such as 8x64 "bins" vs. 11x1 "rings". The latter is still arguably better because it allows for 3 more sampling points over the expected spend curve.

So in summary, I support binning (somewhat), but do not support dropping below 11 bins (as that is demonstrably worse than what we have now). And I want people to think more about "leaking timeslots" instead of purely how many pubkeys get slammed into the signature algorithm.

> tx-chaining seems to be a desired feature that has the potential to reduce privacy compared to existing monero if parameters (mostly ringsize) are wrong, but that could just be my interpretation.

Tx-chaining has privacy issues when there is a separate mechanism for specifying members. If the current model (i.e. one Monero used now) remains in use, then there is no privacy issue, only an implementation issue for the miners (which now have to manipulate txes based on output number changes).

If we switch to something from the Chator et al paper, then it requires two different methods for specifying members which is never ideal.

> hash-encoding of ring members is a data compression technique whose utility is also greatly affected by ringsize.
>
> Perhaps, in order to make this conversation and those around these potential protocol modifications more coherent, should we break apart this issue into the 3 distinct issues that exist? They really seem independent, and mostly dependent on the existence of large ring sizes IMO.

If the original paper is followed, it may work. But I'd have to inspect the paper too (Matthew Green is quite respected so it most likely works, but is probably hard to implement). The pseudocode above doesn't appear to match exactly in two ways. One is intentional, one might be for brevity.

## UkoeHB | 2021-07-07T18:56:03+00:00
> Of course, this simple scheme works only for cases where there is a single real transaction. In practice, real protocols may require the spender to embed _several_ real transactions into T. In our main construction, we generalize the above construction by replace the single value C with a polynomial P(.) evaluated over a field Fp for some large prime p.
> pg. 3

The proposal here does not use the polynomial generalization (each RSS only has 1 real point to land on), so the stuff about prime p is not relevant.

I will work on improving the rationale/citations this weekend.

> This isn't speculation, anyone who has studied ZKP systems can see that this is really close to a ZKP AND gate, and I didn't see anything analogous to a DLP (the source paper has a random k and P over a prime field).

Originally I planned to add a randomly generated 16-byte ring entropy, but switched to a hash of tx details because it seemed equivalent. I admit to not being an expert in this area, so if there is any specific reason this doesn't work I'd like to learn more. Just saying it doesn't work is not very helpful.

> I already gave my idea. Ignore the total number of pubkeys going into the signature because that is misleading. Instead, look at the number of rings/bins with bin members >1 being a (potential) "bonus" to what we have now. But do not drop the number of bins below the current ring threshold as this is reducing the security (see next paragraphs).

Sure, I don't have a strong opinion on this.

> The security comes from the entropy in selecting the bins/rings. A quick reductio absurdum - if you had 1 bin with 128 members this clearly has less entropy than 128 bins with 1 member. With only 1 bin, the sender is leaking the timeframe of the real spent output to within <10mins or so. The more bins, the more "timeframes"/entropy into the system. So number of bins should be considered roughly equivalent to the number of members in a ring.

I think this analysis is naive. Selection over the spend distribution vs binning: these address different privacy concerns. The first addresses the case where the observer doesn't have timing information. The second addresses the case where the observer _does_ have timing information (either due to failures of the selection distribution, or special knowledge about a transaction). Is the 'privacy maxima' at either end of the spectrum, or in the middle? This is a balancing act with no clear answer. Trying to frame it as 'number of bins equals number of ring members' is misleading at best.

EDIT: However, it does make some sense to avoid 'backtracking' on current privacy dimensions by taking fewer samples from the spend distribution (i.e. have fewer bins than current ring members). This is partially why I chose `sqrt()` for the `num_bins` computation in the first place - `sqrt(128) = 11.3`.

> constraints on throughput

What constraints?

## vtnerd | 2021-07-08T00:46:54+00:00
My main criticism, after your feedback, is that floating index + RSS don't work well together. I think we're stuck either choosing tx chaining with larger tx sizes OR smaller compact txes without tx chaining. You haven't really provided a good technique or explanation on how to merge these two ideas.

Also, merging them made it real difficult to sift through the idea initially, because there was so much special logic for floating indexes it mucked up the algorithm a bit.

> The proposal here does not use the polynomial generalization (each RSS only has 1 real point to land on), so the stuff about prime p is not relevant.

After going back over both, `bin_rotator` is your `P`, but you dropped the prime field arithmetic. I doubt this is a good idea because it changes the properties of modular arithmetic entirely (possibly invalidating the proofs).

And a 64-bit `P` seems _really_ sketchy, but the source paper used this in their example (with the caveat that you could choose larger). Also note they mentioned a 64-bit prime. One thing to consider is future extensibility, because as the number of outputs increases the security margin of a 64-bit value decreases.


> I will work on improving the rationale/citations this weekend.

 * Floating indexes WITH RSS security issues. There's good rational for floating indexes + binning OR RSS standalone, but there's serious privacy issues with floating indexes + RSS.
 * Where does the paper indicate that we can do away with prime fields?
 * What about `k`, dropping it also changes from the paper

>Originally I planned to add a randomly generated 16-byte ring entropy, but switched to a hash of tx details because it seemed equivalent. I admit to not being an expert in this area, so if there is any specific reason this doesn't work I'd like to learn more. Just saying it doesn't work is not very helpful.

Then why drop `k` from the paper which was the entropy you described? Seems rather bold to change away from the paper.

> I think this analysis is naive. Selection over the spend distribution vs binning: these address different privacy concerns. The first addresses the case where the observer doesn't have timing information. The second addresses the case where the observer does have timing information (either due to failures of the selection distribution, or special knowledge about a transaction). Is the 'privacy maxima' at either end of the spectrum, or in the middle? This is a balancing act with no clear answer. Trying to frame it as 'number of bins equals number of ring members' is misleading at best.

This is not misleading; if they address different concerns then both might be important. 

The "bins"/"rings" leak metadata - mainly it reduces the possible receive times to a fixed number of windows. I'm not certain how important this is, other than a small number of bins leaks lots of information. So it seemed prudent to keep `bin_size >= 11` so that Monero isn't going in the wrong direction for privacy.

I think `sqrt(RING_SIZE)` or `log2(RING_SIZE)` is the wrong equation; more entropy from the first stage should be extracted. I was/am surprised you recommended this RSS approach with such low numbers of bins.

> What constraints?

There's still disk access time and bandwidth from memory -> CPU registers. There's always some cost to adding more bytes of stuff. This may be less than the penalty of larger sizes from the signature itself though. I mentioned solely to indicate that there are limitations on how large the bins can be.

## UkoeHB | 2021-07-08T03:35:45+00:00
> After going back over both, bin_rotator is your P, but you dropped the prime field arithmetic. I doubt this is a good idea because it changes the properties of modular arithmetic entirely (possibly invalidating the proofs).
> 
> And a 64-bit P seems really sketchy, but the source paper used this in their example (with the caveat that you could choose larger). Also note they mentioned a 64-bit prime. One thing to consider is future extensibility, because as the number of outputs increases the security margin of a 64-bit value decreases.

Not sure why I need to repeat myself. The prime stuff is irrelevant here, because I am not use polynomials. The `bin_rotator` is `C` from section 1.A. Section 1.A further only specifies that the hash function be 'keyed'. Sampling `k` randomly is only mentioned there as an example. All that matters is that each key be unique between different RSS instances, and determined by the tx author.

Even if the adversary knows the key in advance of a tx being constructed, it can't be used to provide any information about the real spend (assuming they can't choose which key the tx author uses, and can't meaningfully choose the chain's composition after learning the key).

>  I think we're stuck either choosing tx chaining with larger tx sizes OR smaller compact txes without tx chaining.

Why do you think having all-floating-outputs solves the problems with floating outputs in this proposal? The problems you have pointed out are high-fidelity heuristics that cannot defended against (i.e. rapid appearance of a tx in the mempool after an output it spends appears, presence of a floating output in last 10 blocks, floating output outside decoy-selection-range).

> more entropy from the first stage should be extracted

What?

> There's still disk access time and bandwidth from memory -> CPU registers. There's always some cost to adding more bytes of stuff. This may be less than the penalty of larger sizes from the signature itself though. I mentioned solely to indicate that there are limitations on how large the bins can be.

Huh? I am recommending a maximally compact design. This proposal has no impact on or opinion about how many total decoys are selected for rings.

## Kanigo2 | 2021-07-08T09:48:47+00:00
Gentelmen,I wanted to step in as an alternate voice here for clarity on a few alternate issues I have.
These current questions are for UKoeHB.
Thank you,please.

1) I am concerned with the “lockup phase” and 10 block confirmations-as I am to understand moneros current process that transaction is locked from the moment you “send the the transaction”-there is no going back.
Even in your current submittal UKoeHB even if we submit the transactions in the way you are suggesting regardless of ring sizes/binning/Or any other implementaion and we come to find out the transaction STILL hasnt been completed and we hit the “infamous 11th block situation”


Are the balance of funds returned to the wallet?


Because this would expose the wallet address twice (the original spend submittal-and subsequent collapse of transaction)(and I do understand the entire balance of wallet is sent out and balance returned in each transaction)(I know you are rolling over the chain of tx in the last 10 blocks-and hiding it)but please consider this hypothetical.

We have gone past this now “unchangable chain-11th block”
“Point of inflection”
“Event horizon”
-or as COMIT team put it,”the punishment phase”
What happens? -just asking for some clarity and how you see it.
Does the transaction Simply collapse/closed? Or are the funds time locked?

This is the “holy terror” inflection point for all folks wishing to see atomic swaps.


Which brings me directly to my next subject
2) Tx fees. So in Monero current process every transaction is single,irreversible,wallet to wallet,with a single transaction output to chain-cheap and quick,the cost for this transaction currently is 6.3 Nanoneros/Byte. 
I can go on TXStreet(or any explorer) and click on any single transaction and I can see instantly exactly what that transaction paid in fees,individually,transaction by transaction.

Now comes along Atomic swaps,in this current submittal, instead of a single transaction it will require (at a minimum) twice the calculations/txs.
The transaction fees to be paid by the Monero holder (buyer?)out of thier transaction.

I understand that you are setting the transaction fee in upperbound.
Upperbound apparently is apparently pretty stable in Reorgs. Transaction fees are placed in upperbound and are using “ input_seed = H("input_seed", input.key_image) instead of ring_seed ” -but during a rollover if that fee value is changed in that intial transaction-IT WILL stand out.
Additionally if the fee is much higher or lower in the later completion of the transaction,that will also stand out.
Trying to balance them equally would also stand out.
Once that Initial transaction is set, that fee must remain.
If that value changes anywhere in the next 20 minutes,somebody is going to know.

You spoke of heuristic tracking in this set with multiple transactions.This fee value is set range bound.
 Is it possible that the fee value could change in the first transaction upon a reorg? 
Are all the fee values equally divided and of the same value? 
And in heavy trading can the value of the final transaction be well outside of a “mean value” range?

I dont see any specific randomness in the decoy fees-Or in the intial and last transaction.
Is it possible that the two transaction(in/out)fees would exactly equal one another?
Do you agree?

3) I run a node,I sit and try to catch any little nuance I see that looks out of the ordinary,not too long ago I caught,in red letters a descriptor, it said and I paraphrase ,(i have image upon request)
“Transaction failed  utilizing the Dandelion++ network”

If a transaction fails in your current submittal beyond rolling back the last 10 blocks,will there be a reporting system on the node Dashboard? Because even rolling back 10 blocks isnt going to remove an output as obvious as having a failed transaction scrolling by in red letters.

ill assume you are connected to the BTC chain and XMR chain simultaniously in a atomic swap.
There is a single input minimum that is going to be inputed from an outside chain that can cause a point of failure.

Please forgive my edits Im trying to collect my thoughts-as I examine-reexamine the code.
Ive been reading and considering since you posted,UKoeHB.
I am a simple rogue beta tester:)
-Final edit-12pm 7/8/21-complete
Im Open to any comment on this.














## SamsungGalaxyPlayer | 2021-07-08T21:13:23+00:00
On the binning side of things, I think it's important to remember that each sort of scenario holds up better depending on what targeted surveillance you assume. If for a specific transaction you have information to know approximately when the real output was spent, having a decoy in the same approximate window/bin is better than the status quo random selection.

Given that Monero largely doesn't use binning techniques right now, my impression is that it's probably a better tradeoff to use many bins of smaller sizes. Eg: 64 bins of 2 outputs each. Real-life efficiency limitations may get in the way however.

Further, I think it's incorrect to say that overall, having fewer bins than 11 makes the privacy afforded to users worse. It's more complicated than that. But given the existing research and the promise of a larger ringsize, I don't see why we need to compromise anyway.

Take the obvious win that's understood to offer incrementally better privacy than the status quo regardless of the scenario. Refine later if necessary.

Compared to the status quo, all of the following are obviously better (bins)x(outputs):

128x1
64x2
32x4
16x8

I need to think more about the other two components of this proposal. I think the terrible UX of the 10 block locktime is significant and should be addressed (even with some reasonable tradeoffs) if possible. I care far less about accounting for the atomic swaps use-case.

## UkoeHB | 2021-07-11T22:25:59+00:00
@Kanigo2

> I am concerned with the “lockup phase” and 10 block confirmations-as I am to understand moneros current process that transaction is locked from the moment you “send the the transaction”-there is no going back.
> Even in your current submittal UKoeHB even if we submit the transactions in the way you are suggesting regardless of ring sizes/binning/Or any other implementaion and we come to find out the transaction STILL hasnt been completed and we hit the “infamous 11th block situation”

A transaction is not locked when it is submitted. The transaction lands in the mempool, where it sits until a miner adds it to a block. It's true that in some sense there is 'no going back', because practically speaking it is very hard to prevent a tx that lands in the mempool from ending up in a block. However, the 10-block thing is separate. When a tx is added to a block, the 'outputs' created by that tx cannot be spent until 10 blocks have passed.

This proposal would allow you to spend outputs as soon as you receive them, instead of needing to wait for 10 blocks.

> Are the balance of funds returned to the wallet?

There are two situations where an otherwise-valid transaction that lands in the mempool can fail.

1. The tx fee is too low, so no miners add it to a block.
2. You, the person who made the tx, make another tx that spends the same outputs as the first one. If the second tx ends up in a block before the first one, then the first one will fail (aka the 'double-spend' situation).

> This is the “holy terror” inflection point for all folks wishing to see atomic swaps.

I don't know much about atomic swaps, so you may need to ask someone else for clarification related to that topic.

> I understand that you are setting the transaction fee in upperbound.
> Upperbound apparently is apparently pretty stable in Reorgs. Transaction fees are placed in upperbound and are using “ input_seed = H("input_seed", input.key_image) instead of ring_seed ” -but during a rollover if that fee value is changed in that intial transaction-IT WILL stand out.

Currently, Monero has an algorithmic 'minimum fee' that changes every block. Nodes look at transactions in their mempool, and transactions received from wallets, and decide if they should abandon them by comparing the tx fees with the current minimum fee (I may be getting the precise details of this wrong). The practical effect of this is tx with low fees won't end up in blocks (even though fees are not enforced by consensus, so a low-fee tx can be added to a block if a non-standard miner decides to make such a block).

Since the minimum fee changes every block, if the fee in a tx is a function of the 'most current' minimum fee when the tx is constructed, then observers will have very accurate knowledge of when the tx was constructed. This proposal tries to mitigate that heuristic by saying tx authors should set their fee based on the minimum fee that existed when the 'binning upper bound' was the highest block. It can work if 'binning upper bound' is selected somewhat randomly, so observers have a harder time pinpointing exactly when a tx was constructed.

> If that value changes anywhere in the next 20 minutes,somebody is going to know.

I am not sure what you mean by this. After a tx has been constructed, the fee cannot change. To support this proposal, tx authors would probably need to select a fee high enough that it won't be invalidated by minimum fee volatility between the 'binning upper bound' block and the block where the tx is likely to end up. You can do this by estimating the maximum volatility that can occur over a certain timeframe.

> Is it possible that the two transaction(in/out)fees would exactly equal one another?

I am not sure what you mean by this.

> If a transaction fails in your current submittal beyond rolling back the last 10 blocks,will there be a reporting system on the node Dashboard?

I am not involved in node development, so I don't know. What failure scenario are you thinking might need to be reported?

> ill assume you are connected to the BTC chain and XMR chain simultaniously in a atomic swap.
> There is a single input minimum that is going to be inputed from an outside chain that can cause a point of failure.

Unfortunately, as I don't know much about atomic swaps, I can't address this topic.

## UkoeHB | 2021-07-11T22:59:12+00:00
#### Problem

Decoy selection from the 'reorg zone' (e.g. most recent 10 blocks) has an inescapable flaw. I pointed this out on IRC, but want to record it here where it is most relevant.

Outputs in the 'reorg zone' can be completely removed from the chain by a reorg, because any output that can be reorged can be double-spent. If an attacker spams the network with double-spends of his own outputs, then on a regular basis 'naturally occurring' reorgs will cause some of his transactions to be replaced by double-spends of those transactions. If an output created by the first group is used as a decoy by a random person, then that person's transaction will become invalid after the reorg.

In other words, decoys are vulnerable to the 'confirmation' problem. A tx author should only use decoys that are 'strongly confirmed', i.e. decoys that are buried below the 'reorg zone'.

#### Consequence

As a result, the 'floating offset' part of this proposal is greatly weakened. Decoy floating outputs can only be selected from below the reorg zone, yet it is reasonable to expect that a non-trivial proportion of tx inputs whose real-spends are floating outputs will be in the reorg zone.

#### Alternative

The alternative to floating offsets is to define a new input type with only 1 ring member whose on-chain reference (i.e. index) is not signed by tx authors (as discussed earlier in this thread).

#### Moving forward

From my point of view as the proposal author and general Monero contributor/enthusiast, this problem with floating offsets is enough for me to dislike the idea.

Since 1-member-ring inputs are unrelated to ring binning, I won't include it in the above proposal. However, before removing floating offsets from the proposal I will leave it as-is for 1 more week in case others want to comment further.

## Gingeropolous | 2021-07-12T03:13:20+00:00
> If an attacker spams the network with double-spends of his own outputs, then on a regular basis 'naturally occurring' reorgs will cause some of his transaction to be replaced by double-spends of those transactions. 

So an attacker spams double spends, injecting them into different parts of the network in the hopes that a re-org will occur and therefore weaken the number of useful decoys from the floating set? (im assuming here we're using a floating set and not just the 1 proposed in this Issue, because if just the 1 then yeah, definitely not good). 

> In other words, decoys are vulnerable to the 'confirmation' problem. A tx author should only use decoys that are 'strongly confirmed', i.e. decoys that are buried below the 'reorg zone'.

Sure, that is generally the best approach. However, if tx-chaining is *really* that important, then i think there are ways forward that just assume decoy attrition. E.g., if you imagine the extreme idea of a 128 member ring, where the first 117 members are chosen from the tip of the chain (or the txpool directly), then this set of 117 decoys can stand to lose some while maintaining the obfuscation. 



## UkoeHB | 2021-07-12T03:32:17+00:00
>  if you imagine the extreme idea of a 128 member ring, where the first 117 members are chosen from the tip of the chain (or the txpool directly), then this set of 117 decoys can stand to lose some while maintaining the obfuscation.

The problem is some decoys will be **permanently removed** from the chain due to a double spend, so the transactions that reference them will be **permanently invalid**.

## vtnerd | 2021-07-12T04:46:26+00:00
@UkoeHB 

> Not sure why I need to repeat myself. The prime stuff is irrelevant here, because I am not use polynomials. The bin_rotator is C from section 1.A. Section 1.A further only specifies that the hash function be 'keyed'. Sampling k randomly is only mentioned there as an example. All that matters is that each key be unique between different RSS instances, and determined by the tx author.

The polynomial `P` is a tuple of constants, and this is the order-0 case. The equations listed in section 1.A are mentioned to be "incomplete", and the authors may have done a "look how to simple it is" while pushing the complexity of uniform distributions to the latter sections and proofs (the proofs make use of the prime field).
...
I don't see a security proof for the equations are you using (`mod max(u64)` followed by `mod num_outputs` doesn't have uniform distribution for instance).

> Even if the adversary knows the key in advance of a tx being constructed, it can't be used to provide any information about the real spend (assuming they can't choose which key the tx author uses, and can't meaningfully choose the chain's composition after learning the key).

I'm possibly being overly conservative here - the `key_images` and (especially) `pseudo_outs` should have enough bits of unpredictability to match the requirements from the proofs. But injecting entropy via `k` leaves little doubt when auditing that portion of the code.

>> I think we're stuck either choosing tx chaining with larger tx sizes OR smaller compact txes without tx chaining.
>
> Why do you think having all-floating-outputs solves the problems with floating outputs in this proposal? The problems you have pointed out are high-fidelity heuristics that cannot defended against (i.e. rapid appearance of a tx in the mempool after an output it spends appears, presence of a floating output in last 10 blocks, floating output outside decoy-selection-range).

This proposal selects pubkeys from two different processes then merges them into one for use in a single ring-signature. You'll need some good justification for this as all prior work (that I am aware of) is on uniform exponential selection to match the real spend patterns.
...
There is a known bias towards newer pubkeys, so having two distinct sets means the spend is more likely to be in the "floating index" stage. Having 1-4 fixed number of floating indexes is arbitrary compared to the uniformity of the exponential distribution over all spendable blocks that we use now.

The best (partial) solution I can muster is to select `num_floating_indexes` based on expected/average number of bins that should be in blocks 1-10 given a specific `bin_size`. So `num_floating_indexes` will no longer be arbitrary and hopefully _less_ likely to leak statistical information, but it still leaves the unexplored funkiness of having two selection processes for decoys.

>> more entropy from the first stage should be extracted
>
> What?

`log(RING_SIZE)` or `log2(RING_SIZE)` provides too few bins.

>> There's still disk access time and bandwidth from memory -> CPU registers. There's always some cost to adding more bytes of stuff. This may be less than the penalty of larger sizes from the signature itself though. I mentioned solely to indicate that there are limitations on how large the bins can be.
>
> Huh? I am recommending a maximally compact design. This proposal has no impact on or opinion about how many total decoys are selected for rings.

Then why list a formula for specifying how many bins there should be?

> **Alternative**
The alternative to floating offsets is to define a new input type with only 1 ring member whose on-chain reference (i.e. index) is not signed by tx authors (as discussed earlier in this thread).

This is identical in concept to the floating indexes concept ?

---

@SamsungGalaxyPlayer 


> I need to think more about the other two components of this proposal. I think the terrible UX of the 10 block locktime is significant and should be addressed (even with some reasonable tradeoffs) if possible. I care far less about accounting for the atomic swaps use-case.

There's plenty of work, testing, and auditing needed just to get tx-chaining implemented. Although, once implemented the RSS/hash decoy selection algorithm may never get merged because having two different decoy selection algorithms is suboptimal.

## UkoeHB | 2021-07-12T06:25:00+00:00
> The polynomial `p` is a tuple of constants, and this is the order-0 case.

Umm.. the order-0 case of a polynomial is a single constant. The whole paper boils down to proving the relation `f_k(j) + P(j) = I_j mod l` is legit. The term `P(j) mod l` reduces to a constant in the range `0 <= C < l` if `P(x)` is a 0-order polynomial. In other words, the prime field used to construct `P(x)` is irrelevant if you can derive `C = I_j - f_k(j) mod l` directly.

The trivial case is literally so trivial the authors had full right to give it just one sentence.

> I don't see a security proof for the equations are you using (mod max(u64) followed by mod num_outputs doesn't have uniform distribution for instance).

The modular operations in this proposal are all `mod l` like in the paper. Bin loci are selected from the transform-space (i.e. [inverse transform sampling](https://stephens999.github.io/fiveMinuteStats/inverse_transform_sampling.html)) of the gamma distribution (`mod max(u64)`), and bin members are selected from 'within a bin' (`mod bin_size`).

> Then why list a formula for specifying how many bins there should be?

?????

The amount of data stored in transactions in this proposal is O(1). You could have 3 total decoys, or 3 million total decoys.

Do you have some fundamental misunderstanding about this proposal lurking under the surface?

> This is identical in concept to the floating indexes concept ?

Huh? We already discussed this earlier in the thread. A 1-ring-member input is literally an input that only references the output being spent.

## vtnerd | 2021-07-12T20:46:51+00:00
>>    The polynomial p is a tuple of constants, and this is the order-0 case.
>
>Umm.. the order-0 case of a polynomial is a single constant.

Yes, the `P` tuple contains 1+ constants. The sarcasm was unnecessary here.

>
> The whole paper boils down to proving the relation f_k(j) + P(j) = I_j mod l is legit. The term P(j) mod l reduces to a constant in the range 0 <= C < l if P(x) is a 0-order polynomial. In other words, the prime field used to construct P(x) is irrelevant if you can derive C = I_j - f_k(j) mod l directly.
>
> The trivial case is literally so trivial the authors had full right to give it just one sentence.

The paper shows the first relationship you describe then also attempts a security proof. It is the latter that I was concerned about in these responses.  `x + y mod l` has uniform distribution only when `l` meets certain properties, otherwise some outputs from that expression are more likely than others. The difference is admittedly trivial though.

Do you know why a prime field is necessary for the 2+ case then?

>>    I don't see a security proof for the equations are you using (mod max(u64) followed by mod num_outputs doesn't have uniform distribution for instance).

> The modular operations in this proposal are all mod l like in the paper. Bin loci are selected from the transform-space (i.e. inverse transform sampling) of the gamma distribution (mod max(u64)), and bin members are selected from 'within a bin' (mod bin_size).

Where does `BIN_RADIUS` fit into all of this?

>>>>There's still disk access time and bandwidth from memory -> CPU registers. There's always some cost to adding more bytes of stuff. This may be less than the penalty of larger sizes from the signature itself though. I mentioned solely to indicate that there are limitations on how large the bins can be.
>>>
>>> Huh? I am recommending a maximally compact design. This proposal has no impact on or opinion about how many total decoys are selected for rings.
>> 
>>   Then why list a formula for specifying how many bins there should be?
>
> ?????
>
>The amount of data stored in transactions in this proposal is O(1). You could have 3 total decoys, or 3 million total decoys.
>
>Do you have some fundamental misunderstanding about this proposal lurking under the surface?

I provided more context. This discussion devolved due to terse responses.

I was specifying how I would determine `bin_size` and `num_bins`, regardless of how the decoys were encoded (as its not guaranteed to be implemented, tx-chaining itself is a big enough feature in a fork). In the RSS O(1) scheme, that would've been `bin_size == 1`; the utility of the bins seemed low with this scheme. You and Justin have persuaded me slightly otherwise - we'd probably have to take real chain-analysis into account though.

I'm still against the `sqrt` or `log` approaches, especially with RSS (there's no space savings), as it seems the bias should be towards exponentially selected decoys.

>
> Huh? We already discussed this earlier in the thread. A 1-ring-member input is literally an input that only references the output being spent.

My apologies for responding poorly - it still has an obvious privacy leak, so its not really a viable alternative.

## ArticMine | 2021-07-13T04:41:50+00:00
I have a question. How does this proposal impact transaction sizes? In particular ring 11 and say ring 17 (CLSAG) and say ring 64 and ring 128 (Trtptych)

## UkoeHB | 2021-07-13T07:57:01+00:00
> `x + y mod l` has uniform distribution only when `l` meets certain properties, otherwise some outputs from that expression are more likely than others.

I don't think this is quite right, and it is pertinent here. Whether or not `x + y mod l` is uniformly distributed depends on A) how `x` and `y` are generated, B) the relation between `l` and those generation methods. For example, if `x` is randomly selected from `0 <= x < l/2`, and `y` from `0 <= y <= l/3`, this would clearly not produce a random distribution in `x + y mod l`. But, if both `x` and `y` are selected randomly from `0 <= n < 2*l`, then the result will be uniformly distributed.

Importantly, if `n`s generation space is `>> l`, then even if `n` is not uniformly distributed in its own selection space, `n mod l` will be uniformly distributed 'in practice' (i.e. probabilistically). This behavior is used in the paper for reducing polynomials into the index space, because most polynomials are not uniformly distributed. I assume the use of a 'prime'  prevents subgroup issues when solving the polynomial for a given input.

EDIT: I just remembered the proposal uses this behavior too, when going from [hash output] -> [selection space]. A hash output is a multiple of 8 bytes, so it will be uniformly distributed in the bin loci space (u64), and the hash space is >> bin width (on the order of 100-10000, compared to 2^128-2^256) so bin members will be effectively uniformly distributed. I'm guessing this is what you have been talking about. It would help if you quote lines from the proposal directly.

If you look at Figure 1 in the paper, steps 5-7 simplify to the stuff in section 1.A when `P()` is 0-order, and step 1 (defining the prime) becomes irrelevant.

> Where does `BIN_RADIUS` fit into all of this?

`BIN_RADIUS` is used to set the default 'bin width', which is the number of of outputs on-chain to select a bin's members from (i.e. the decoys for a ring sig). If `BIN_RADIUS = 50`, then each bin will have 101 outputs to select bin members from. The reason I don't use `BIN_WIDTH` directly is because most operations related to bins are with respect to bin loci, rather than e.g. the lower bounds.

> I was specifying how I would determine bin_size and num_bins, regardless of how the decoys were encoded (as its not guaranteed to be implemented, tx-chaining itself is a big enough feature in a fork). In the RSS O(1) scheme, that would've been bin_size == 1; the utility of the bins seemed low with this scheme. You and Justin have persuaded me slightly otherwise - we'd probably have to take real chain-analysis into account though.

I see, thank you for clearing this up.

> I'm still against the sqrt or log approaches, especially with RSS (there's no space savings), as it seems the bias should be towards exponentially selected decoys.

The reason I like `sqrt` is because it evenly distributes 'decoy selection' between the two timing attack vectors (spend-time selection, local-vicinity selection). Since we can't know in advance which vector is more prevalent or important, allocating selection to them equally is a solid compromise (in my view).

> My apologies for responding poorly - it still has an obvious privacy leak, so its not really a viable alternative.

I think it is the **most** viable solution, even if the level of viability is too low for it to be accepted. Since it is most viable, it should at least be mentioned for context.

---

@ArticMine This proposal would reduce tx sizes compared to our current protocol.

- **Current**: 1 varint x ring_size x num_inputs
- **Proposal**: 1 varint + 1 uint64 x num_inputs [+ 1 varint x num_inputs (if num_bin_members > 1)]

The proposal is O(1) with respect to number of decoys.

## Gingeropolous | 2021-07-13T12:14:10+00:00
> > if you imagine the extreme idea of a 128 member ring, where the first 117 members are chosen from the tip of the chain (or the txpool directly), then this set of 117 decoys can stand to lose some while maintaining the obfuscation.
> 
> The problem is some decoys will be **permanently removed** from the chain due to a double spend, so the transactions that reference them will be **permanently invalid**.

right.... I am imagining that there is some cryptomagic that allows you to still have a valid ring signature with some ring members missing. Sorta like how a multisig is possible with an incomplete set. 

But that doesn't exist.... ?

## luckysori | 2021-07-13T12:38:45+00:00
> right.... I am imagining that there is some cryptomagic that allows you to still have a valid ring signature with some ring members missing. Sorta like how a multisig is possible with an incomplete set.
> 
> But that doesn't exist.... ?

I think in your scenario you just wouldn't get to the point of verifying the ring signature, because the transaction would reference non-existent outputs in the input ring. That is surely disallowed, but even if you could get past that you would not be able to produce the original signature hash to verify against, given that some data (e.g. output commitments) would be missing or wrong.

## Gingeropolous | 2021-07-14T02:30:02+00:00
well, on second thought, in the case of a double spend / re-org, 

> given that some data (e.g. output commitments) would be missing or wrong.

those data aren't missing, they are just now on the orphaned chain. 

but yeah. not saying that it should be done, but there's probably a hacky way that it could be done. But for sure, this avenue of thought is sufficiently bricked over for me at least. 

## Gingeropolous | 2021-07-14T13:31:34+00:00
well it seems I can't brick up this avenue that well.

you could call this a "fray", and its kinda like ethereums uncle blocks... but yeah, in the case of a re-org, you could carry the alt-chain to maintain the data references .... but yeah, pretty ugly and probably opens some attack surfaces. 

## j-berman | 2021-07-15T04:20:15+00:00
I think allowing for 1 member rings is actually a pretty solid alternative that makes the network safer/enables a stronger degree of privacy for most users.

Today there are some honest users who rely on making transactions transparent; [mining pools making payouts to pool members](https://xmr.2miners.com/account/89rnEizYnqr9fNTKeMDcuKh6TkwGAZXAniExdb38p1QTXN5QUCeWNXMaJQwRxDdKazgvQVAaeP8sh2ycmCjPZfhT5dmP4p6#payments-tab) are one such example. In this case, honest users who benefit Monero are revealing their spent outputs and negatively affecting others on the network, who then include those outputs in their rings. Another example: a potential Thorchain integration, where all transactions that happen on Thorchain would be made public. Allowing an alternative tx (1 member rings) for these good-faith users, without polluting the global output set for other users who want privacy by default (or bloating the chain with unnecessarily large rings), seems like a reasonable use case that makes the network safer for everyone.

Basically, if you're an honest user but you're going to make your transaction public anyway, just make it transparent on the chain in a silo'd part of the chain where others can't use your known spent outputs, so you won't negatively affect other users. Plus, you have the added benefit of marginally cheaper transactions, and it saves space.

Edit: it could work by designating an output as only usable in a 1 member ring going forward. For example, a mining pool knows it's going to pay out the block reward in a new tx in the future, so in the miner tx, the output would be designated as only being usable in a 1 member ring - something along those lines. That way no one else would attempt to use that output as a decoy in their ring.

## trasherdk | 2021-07-15T07:48:56+00:00
So, what happens when a bunch of **honest users** makes a shitload of 1-ringmember outputs?
Wouldn't that help the **dishonest observers** having a smaller set of outputs in need of analyzing?

## j-berman | 2021-07-15T08:38:18+00:00
My assumption is that the feature would be used by people who are either *already* revealing their spent outputs anyway such as mining pools (this group is adding to the set of outputs in a way that is harmful today -- these additional outputs added to the global set of outputs are not beneficial in any way whatsoever), or would not otherwise add to the set of outputs at all.

I wasn't thinking that it would take away from people who are adding to the output set in a beneficial way (i.e. I didn't think this would alter normal usage of Monero, where the average user doesn't reveal their spent outputs to the world).

Though if there is an incentive of significantly lower fees, it might attract people to want to use it instead of normal ring tx's, and therefore potentially take away from the output set. Perhaps could require a fee on par with normal tx's, and so the only incentive to using it is either altruistic (i.e. can't do harm using it, but it's beneficial for other users), or it allows you to do something you wouldn't have otherwise done.

## j-berman | 2021-07-15T10:01:46+00:00
Realized the above is basically one of the recommendations of [An Empirical Analysis of Traceability in the Monero Blockchain](https://arxiv.org/pdf/1704.04299/) (pg. 16)

> Avoid including publicly deanonymized transaction
outputs as mixins

> We have empirically shown the harmful effect of publicly
deanonymized (i.e. 0-mixin) transactions on the privacy
of other users. Since non-privacy-conscious users may
make 0-mixin transactions to reduce fees, Monero had
instituted a 2-mixin minimum, and recently increased
this to 4. However, even 4+mixin transactions may be
publicly deanonymized; in particular, as discussed in
Section 5.1, mining pools have a legitimate interest in
forgoing anonymity by publicly announcing their blocks
and transactions for the sake of accountability. Thus, we
propose that Monero develop a convention for flagging
such transactions as “public,” so that other users do not
include them as mixins.

## trasherdk | 2021-07-15T10:16:09+00:00
You are also assuming honest users actually exists, and would be the only ones to utilize this,
while you should assume that any user is potential adversarial, and should maximize protection
against those **friendly honest users** :smile: 


## j-berman | 2021-07-15T11:14:40+00:00
Fair enough. Thought it through more deeply and there are reasons to think honest users may be pulled into using this feature over using normal tx's, thereby reducing the size of the output set. Here are the scenarios where that might happen:

- If the unlock time is done away with for 1-member rings, users who value being able to make quicker payments over privacy may now opt to use 1-member rings over normal tx's. Exchanges probably the largest source of tx's that fit the bill here.

- Users may atomic swap Monero for Bitcoin thanks to this feature instead of going to Haveno and exchanging for Bitcoin using their protocol (where spent output data wouldn't be published I believe).

- Users who value performance over privacy at the point of tx construction may opt to construct the quicker-to-construct and transmit 1-member ring tx's.

There are probably more I'm not seeing. Thorny tradeoffs.

## Hueristic | 2021-07-15T21:57:52+00:00
> 
> 
> Fair enough. Thought it through more deeply and there are reasons to think honest users may be pulled into using this feature over using normal tx's, thereby reducing the size of the output set. Here are the scenarios where that might happen:
> 
>     * If the unlock time is done away with for 1-member rings, users who value being able to make quicker payments over privacy may now opt to use 1-member rings over normal tx's. Exchanges probably the largest source of tx's that fit the bill here.
> 
>     * Users may atomic swap Monero for Bitcoin thanks to this feature instead of going to Haveno and exchanging for Bitcoin using their protocol (where spent output data wouldn't be published I believe).
> 
>     * Users who value performance over privacy at the point of tx construction may opt to construct the quicker-to-construct and transmit 1-member ring tx's.
> 
> 
> There are probably more I'm not seeing. Thorny tradeoffs.

Not at all, if you don't want to be part of the anonymity set then don't use the coin.

You smell like a plant with an agenda to weaken the coin.

## j-berman | 2021-07-15T22:10:09+00:00
@Hueristic 

My initial angle was to strengthen the anonymity set, which is currently actively being weakened by honest users, which is evident in that mining pool page I linked.

My last comment that you're responding to was fully fleshing out and acknowledging the downsides. If anything that would be the comment you should agree with most from your perspective.

In any case, I'm tapping out of this conversation, since I agree that those downsides, which I explained fully, are significant enough I don't feel comfortable pushing forward 1-member rings.

## SamsungGalaxyPlayer | 2021-07-16T03:00:54+00:00
In theory it would be fine to grab the efficiency gains of the 1-output rings and the flagging that could be shown to wallets, but this isn't realistic or enforceable. Thus, the status quo of the minimum ringsizes seems to be the best option in practice. We already know marking outputs as spent on the wallet side is possible but terrible in practice. Most mining pools now share less information to the public anyway, and Monero network activity has far surpassed these mining pool outputs anyway so it's no longer a significant problem.

I share concerns about the visible outputs through something like Thorchain, and the desire to flag these outputs as a special kind so they can be avoided (along with whatever else should be flagged). From a consensus design decision however, it's best to limit on-chain fuckery as much as possible, or else it's like Monero's past where people widely used 1-ring transactions for no good reason.

We had a similar discussion for coinbase outputs and possibly requiring coinbase-only rings (since those are already marked, no avoiding that). This was passed on mostly for complexity and not-significant-enough-of-a-harm reasons.

Anyway, I'd rather steer this discussion back to the other main topics. Whether Monero should have a public output tier should be a completely separate issue.

## Gingeropolous | 2021-07-21T02:58:53+00:00
@UkoeHB , i would recommend changing the title back and just starting a new issue for ring binning. If you change the original post, then the responses aren't gonna make sense etc etc. 

I mean, you can do what you want obvi :) but in 2 years we'll have no idea what happened here. 

and its good to have documented why a particular feature / solution was sent back to the drawing board. 

## UkoeHB | 2021-07-21T03:34:34+00:00
Github comments/etc. have a history of edits you can look at. I added the date to my comment about removing tx chaining if people want to look at the old version.

## UkoeHB | 2021-09-19T20:11:48+00:00
I think @vtnerd has mentioned it might not be good to bake a selection algorithm directly into the consensus rules. This proposal can be modified for use in that context (generate bin locations locally, generate bin members deterministically).

- tx storage per input
  - set of bin centers (e.g. if there are 11 bins, there will be 11 varint offsets locating the centers of each bin, similar to current ring member references)
  - bin-member rotator (same as in the proposal, this rotates deterministically-generated bin members within each of the input's bins)
- proposal modifications
  - use a local rng to seed bin center generation, instead of a deterministic seed
  - each tx input can have a different binning upper bound, since binning upper bounds would be invisible to consensus
- consensus rules
  - ring size (constant)
  - num bins (constant)
  - ring size -> bin division mapping (num bin members per bin)
  - bin radius (constant)
  - deterministic bin member generation and rotation based on a per-input seed derived from tx data (~ same as in the proposal)
  - require that bin centers be `>= lowest_output + bin_radius` and `<= highest_output - bin_radius` based on validating node's ledger

The disadvantages compared to a baked-in selection algorithm are:
- larger tx (have to store all bin centers for each input)
- implementation fingerprinting is possible
  - implementers can allow inputs with different binning upper bounds
  - implementers can use different selection algos


## j-berman | 2021-10-05T22:53:56+00:00
I think I have a bit of a clearer explanation for the subtle leak @vtnerd talked about [here](https://github.com/monero-project/research-lab/issues/84#issuecomment-873157973). I don't yet see a perfect way around it with a simple client-side binning approach I've been trying to think through either.

It's easier to see it if you assume 100 bin members. You'll have a "jar of marbles" so to speak that revolve around the center. So the bin center would be clearly deducible.

If your real output is used as a bin center, then it's fairly trivial there would be no benefit to binning. An observer could just eliminate any outputs that aren't bin centers.

If you take your real output, and try to select a new bin center using the real output, the new bin center is still statistically more likely to be closer to the real output (can qualify this claim further with some kind of proof). Therefore, the outputs that are closer to the bin center are still more likely to be real than the outputs further away.

At this point, I'm trying to reason through if it's possible to avoid this leak by fixing the bin size to 2, and going with an approach that doesn't scale to >2 bin members. But with >2 bin members, I think the above should help make it a bit clearer a leak is introduced with an approach along these lines.

Perhaps the Moser paper's approach for fixing bins may be the best way to go after all.

## UkoeHB | 2021-10-05T22:58:48+00:00
> If you take your real output, and try to select a new bin center using the real output, the new bin center is still statistically more likely to be closer to the real output (can qualify this claim further with some kind of proof).

Unless I am missing something, selecting a bin center at random from around the real spend means the `real spend - center` delta will be uniformly distributed (equally likely to be any value).

## j-berman | 2021-10-06T00:58:33+00:00
Yep, nevermind I believe you are right @UkoeHB  -- that was me tripping up. Fairly simple python script that should support your claim and show I was wrong:

```python
import random
import statistics

BIN_WIDTH = 100
BIN_RADIUS = int(BIN_WIDTH / 2)
REAL_OUTPUT_INDEX = 150

NUM_SIMULATIONS = 100000
BIN_MEMBERS = 50

init_bin = range(REAL_OUTPUT_INDEX - BIN_RADIUS, REAL_OUTPUT_INDEX + BIN_RADIUS)

real_is_closer_than_bin_members = 0
real_is_further_than_bin_members = 0
deltas = []

for i in range(NUM_SIMULATIONS):
    bin_center = random.choice(init_bin)
    final_bin = range(bin_center - BIN_RADIUS, bin_center + BIN_RADIUS)

    bin_member_distances = []

    for j in range(BIN_MEMBERS):
        bin_member = random.choice(final_bin)

        # on average, expect this distance to be BIN_WIDTH / 4
        distance_from_bin_center = abs(bin_member - bin_center)
        bin_member_distances.append(distance_from_bin_center)

    avg_bin_member_distance_from_bin_center = sum(bin_member_distances) / len(bin_member_distances)
    median_bin_member_distance = statistics.median(bin_member_distances)

    # on average, expect this to be BIN_WIDTH / 4
    real_distance_from_bin_center = abs(REAL_OUTPUT_INDEX - bin_center)

    if real_distance_from_bin_center < median_bin_member_distance:
        real_is_closer_than_bin_members += 1
    elif real_distance_from_bin_center > median_bin_member_distance:
        real_is_further_than_bin_members += 1

    # my initial claim was that this would be negative with significance
    real_and_bin_member_delta = real_distance_from_bin_center - avg_bin_member_distance_from_bin_center
    deltas.append(real_and_bin_member_delta)

# but not the case
print("Delta should be close to 0 to show initial claim was wrong:", sum(deltas) / len(deltas))

# my claim was the real would tend to be closer to the bin center than other bin members, not the case with significance
print("Real is closer to bin center than other bin members:   ", real_is_closer_than_bin_members, "times")
print("Real is further than bin center than other bin members:", real_is_further_than_bin_members, "times")
```

EDIT: another sanity check from a different angle:

```Python
import random

BIN_WIDTH = 100
BIN_RADIUS = int(BIN_WIDTH / 2)
REAL_OUTPUT_INDEX = 150

NUM_SIMULATIONS = 1000000
BIN_MEMBERS = 20

init_bin = range(REAL_OUTPUT_INDEX - BIN_RADIUS, REAL_OUTPUT_INDEX + BIN_RADIUS)

# is the real's distance from bin center uniformly distributed?
real_output_bin_member_distance_index_counts = {}
for i in range(BIN_MEMBERS + 1):
    real_output_bin_member_distance_index_counts[i] = 0

for i in range(NUM_SIMULATIONS):
    bin_center = random.choice(init_bin)
    final_bin = range(bin_center - BIN_RADIUS, bin_center + BIN_RADIUS)

    bin_member_distances = []
    selected_bin_members = { REAL_OUTPUT_INDEX: True }
    real_distance_from_bin_center = abs(REAL_OUTPUT_INDEX - bin_center)
    bin_member_distances.append(real_distance_from_bin_center)

    for j in range(BIN_MEMBERS):
        bin_member = random.choice(final_bin)

        # no duplicates
        while bin_member in selected_bin_members:
            bin_member = random.choice(final_bin)
        selected_bin_members[bin_member] = True

        distance_from_bin_center = abs(bin_member - bin_center)
        bin_member_distances.append(distance_from_bin_center)

    bin_member_distances.sort()

    real_output_bin_member_index = bin_member_distances.index(real_distance_from_bin_center)

    # sometimes there will be duplicate distances, and index() will always choose the closer one.
    # to avoid this, check the next elem in the bin_member_distances array. if it's the same, then
    # 50% of the time, just bump the real_output_bin_member_index by 1
    if real_output_bin_member_index < len(bin_member_distances) - 1:
        if real_distance_from_bin_center == bin_member_distances[real_output_bin_member_index + 1]:
            if random.choice(range(2)) == 1:
                real_output_bin_member_index += 1

    real_output_bin_member_distance_index_counts[real_output_bin_member_index] += 1

# expect roughly equivalent counts for each index
for i in range(BIN_MEMBERS + 1):
    print("Idx:", i, " Count:", real_output_bin_member_distance_index_counts[i])
```

EDIT 2:

A more visual way of seeing the problem:

```
 . is some other output in the chain
 x is the real output
 y is the bin center
 bin radius is 2
```

Start with x:

```
..x..
```

Now here are all plausible bin centers:

```
x.y..
.xy..
..x..     <- x & y are the same
..yx.
..y.x
```

Knowing the indexes of `x` and `y` yields no useful information about `x` being real, because `x` can be in any position of the bin with equal likelihood.

(Edited again for clarity.)

## j-berman | 2021-10-07T20:07:41+00:00
Question on this part:

```
// 1. randomly select the real bin's center from around the output
size_t real_bin_max = spend_output_indices[input_index] + BIN_RADIUS;
size_t real_bin_min = spend_output_indices[input_index] - BIN_RADIUS;

// snap bin bounds to allowed range (with adjustments in case of integer overflow)
if (real_bin_max > binning_upper_bound || real_bin_max < spend_output_indices[input_index])
    real_bin_max = binning_upper_bound;

if (real_bin_min < min_index || real_bin_min > spend_output_indices[input_index])
    real_bin_min = min_index;

size_t real_bin_center = rand_from_range<size_t>(real_bin_min, real_bin_max);
```

Am I following right that the bin width is likely to shrink if you're at the edge? If your real output is the max output allowed, your theoretical bin center could be between the real output and the `real output - BIN_RADIUS`, which would mean in most cases the upper part of the bin is cut off at the edge

## UkoeHB | 2021-10-07T21:05:12+00:00
> Am I following right that the bin width is likely to shrink if you're at the edge?

The bin center selection zone is shrunken/cropped. There isn't any other way to do it, because upper/lower bounds are just that - the boundaries of your data set, and because bin width is fixed - the bin center must be within +/- `BIN_RADIUS` of the real spend.

> which would mean in most cases the upper part of the bin is cut off at the edge

Yep

## j-berman | 2021-10-07T21:18:55+00:00
I *think* there may be an issue at the edge. Am I missing something here?

```
assume bin radius = 2

real output 0 can have bin center at 0, 1, 2
real output 1 can have bin center at 0, 1, 2, 3
real output 2 can have bin center at 0, 1, 2, 3, 4
real output 3 can have bin center at    1, 2, 3, 4, 5
...
```

Real output 0 has 0 bin center 1/3 times, real output 1 has 0 bin center 1/4 times, real output 2 has 0 bin center 1/5 times. Assuming you have roughly the same number of 0's, 1's, and 2's, then you would expect a higher % of the 0 bin centers to be real output 0.

Therefore, if you know the bin center is 0 (or in real terms, if you know the bin center is the closest possible bin center to the upper bound), your best guess for the real is output 0, next best guess is output 1, etc.

What am I missing?

## UkoeHB | 2021-10-07T21:43:43+00:00
I don't think you are missing anything, that is correct (and unavoidable).

On the other hand, you will also have a slightly disproportionate 'piling up' of decoys bins at the boundaries. I think if the true spend distribution matches the bin selection distribution, then these two effects cancel each other out (from a high-level statistical pov; if you have special timing knowledge about an output, then binning is less effective at the boundaries of the data set).

## j-berman | 2021-10-07T22:29:08+00:00
I think I have a way to avoid it in the wallet-side algorithm (at least for the tip of the chain), though I'm not sure it's possible to apply here: using fixed bins, similar to how the Moser paper suggests. I.e. you know a group of outputs must fall into a particular bin.

You could say `outputs 0-99 in the chain = bin 0`, `outputs 100-199 in the chain = bin 1`, etc. all the way until the back of the chain, where the final bin is likely to be smaller. Which seems fine to deal with because the chances of the final bin being used are extremely tiny versus the tip of the chain's bin.

## UkoeHB | 2021-10-08T00:16:41+00:00
I think that can be applied here. Just define the binning upper bound, pre-define bins relative to the binning upper bound (`(upper_bound - BIN_RADIUS) - (2*BIN_RADIUS + 1)*bin_selector`). Then instead of defining bin centers directly, you deterministically select a bin member, then find which bin it belongs to. For the real spend's bin, you'd randomly select a bin member from its bin to map into the uniform distribution.

## ghost | 2021-12-03T14:31:11+00:00
so transaction chaining is out? is this something that Seraphis can allow?

## UkoeHB | 2021-12-03T15:12:57+00:00
@r4v3r23 yes, Seraphis allows transaction chaining. The current RingCT protocol could technically do tx chaining with a LOT of code work and protocol changes, but the real spends in chained tx would always be the 'newest' ring member, which is an unpleasant and perhaps not-worthwhile heuristic.

## ghost | 2021-12-07T23:37:01+00:00
> @r4v3r23 yes, Seraphis allows transaction chaining. The current RingCT protocol could technically do tx chaining with a LOT of code work and protocol changes, but the real spends in chained tx would always be the 'newest' ring member, which is an unpleasant and perhaps not-worthwhile heuristic.

would tx chaining allow for spending unconfirmed outputs and remove the 10-block confirmation lock when receiving funds?

## UkoeHB | 2021-12-07T23:56:15+00:00
> would tx chaining allow for spending unconfirmed outputs and remove the 10-block confirmation lock when receiving funds?

Tx chaining lets you make a partial tx that spends outputs that aren't in the chain. However, the 10-block lock time must remain in place. Here's what you can do (Alice and Bob are friends):
1. Alice receives output A from Carol in block X.
2. Alice makes a partial tx spending A, that sends output B to Bob.
3. Alice gives her partial tx to Bob at height X + 1. The outputs in this tx aren't spendable yet (not until height X + 10).
4. After height X + 10, Bob can complete Alice's tx and submit it. NOTE: Bob will know that Alice's tx spends output A, so Alice should only do this if she trusts Bob (or doesn't care about leaking A)!

## tevador | 2021-12-08T11:12:19+00:00
I think TX chaining and spending of outputs younger than 10 blocks could be still done with binning if the youngest bin referenced outputs by hash instead of by index. This would increase output sizes (for example by 128 bytes for `num_bin_members  = 4`), but would make the scheme resistant to reorgs and preserve some privacy when spending such outputs.

In the example given by @UkoeHB Alice could draw some decoys from block X, so Bob will not know which *exact* output is being spent.

## UkoeHB | 2021-12-08T13:13:21+00:00
> I think TX chaining and spending of outputs younger than 10 blocks could be still done with binning if the youngest bin referenced outputs by hash instead of by index.

This is basically the floating output idea this issue originally proposed. I think it is [too flawed to pursue](https://github.com/monero-project/research-lab/issues/84#issuecomment-877873623).

## ghost | 2021-12-25T17:51:11+00:00
@tevador @UkoeHB from the latest getmonero.org Seraphis write-up:

>> Ignore 10-block lock time when transacting with a trusted party (i.e. allow them to make your tx's membership proofs and submit the tx to the network on your behalf).

is it possible to remove the 10-block lock time in practice without harming privacy across the board by revealing the real output in "trusted" transactions? can this at least remove the lock time on unconfirmed change since its essentially a self-spend with not other party involved? 

just trying to get a feel for how this would change UX when transacting



## tevador | 2021-12-25T18:34:37+00:00
Publicly revealing the spent output weakens all rings that have used that output as a decoy, so that would be a significant hit to the overall privacy of Monero.

## ghost | 2021-12-25T20:05:04+00:00
right so in practice the 10-block limit stays

## tevador | 2022-08-16T19:51:19+00:00
Have any problems been found with this deterministic ring selection algorithm? @UkoeHB's current Seraphis code seems to encode the bin centers explicitly by index rather than generating them from a seed.

There are several advantages of selecting the bins deterministically:

1. More compact reference set encoding, which would reduce transaction sizes.
1. Enforcing a uniform decoy selection algorithm across all wallet implementations. Currently wallets are free to implement their own algorithms, which can lead to privacy leaks.
1. Preventing malicious rings that leak the real spend by selecting the same decoys for multiple outputs (there are thousands of such transactions in the blockchain).
1. If the `binning_upper_bound` was implemented as a blockchain height, this would give us an equivalent of Bitcoin's [nLockTime](https://en.bitcoin.it/wiki/NLockTime) for free. Assuming this field would be signed by the Seraphis ownership proof, it could be used in trustless protocols such as atomic swaps to create a transaction that cannot be submitted to the network for a certain number of blocks. This could entirely replace the current [broken timelock feature](https://github.com/monero-project/research-lab/issues/78) that itself interferes with deterministic selection.

## UkoeHB | 2022-08-16T20:27:25+00:00
Disadvantages:

1. implementation complexity - I predict deterministic bin loci would introduce a lot of edge cases that are difficult to reason about. As it stands, no complete algorithm has even been proposed by anyone.
2. greatly expanded heuristic surface of the protocol - A deterministic bin loci algorithm would be riddled with heuristics, which increases ecosystem dependence on the core team by inviting more hard forks. We want the protocol to become increasingly timeless and independent, not more contextual and dependent.
3. unit test headaches - I don't like headaches.

> If the binning_upper_bound was implemented as a blockchain height, this would give us an equivalent of Bitcoin's [nLockTime](https://en.bitcoin.it/wiki/NLockTime) for free.

If the bin loci are deterministic, but a sub-range of the selection zone is unknown, then you have to brute force rings that only sit within the known range. Since selection distributions greatly favor recent blocks, it may be prohibitively expensive to find viable rings to get a lock time.

>  Assuming this field would be signed by the Seraphis ownership proof

It cannot be signed by ownership proofs, because that would greatly weaken tx chaining. For example, I want to make multisig txs where the decoy references are selected moments before submitting each tx (this is deferred membership proofs, which is the precursor to tx chaining), in order to make multisig txs more indistinguishable from regular txs. That timing can't be known in advance (when building the signatures). For tx chaining, if `binning_upper_bound` is baked into signatures, then you can't chain off an enote if it gets added after `binning_upper_bound`.

## tevador | 2022-08-16T20:52:28+00:00
> you have to brute force rings that only sit within the known range

No. You have to defer making the membership proof until the lock time has elapsed and all outputs in the specified range are known. This is the main point of a time lock field. Consensus would reject transactions with `binning_upper_bound > current_height`.

> I want to make multisig txs where the decoy references are selected moments before submitting each tx

Valid issue, but not insurmountable. Assuming the multisig participants cooperate, they can estimate the required lock time when the signature will be completed.

I guess it's a matter of deciding if we need cheap time locks that are actually usable or the ability to pre-sign a transaction without locking it.

## UkoeHB | 2022-08-16T21:12:52+00:00
> No. You have to defer making the membership proof until the lock time has elapsed and all outputs in the specified range are known.

Ah yes, my mistake.

> Assuming the multisig participants cooperate, they can estimate the required lock time when the signature will be completed.

If you aren't online around the right time, then it becomes a brute force problem again. If we want a cleartext `min_mineable_height` it would be much simpler to just add one varint to txs for that purpose. A more privacy-oriented solution would [use range proofs](https://github.com/monero-project/research-lab/issues/78#issuecomment-1003195804).


## tevador | 2022-08-16T21:24:24+00:00
> If we want a cleartext min_mineable_height it would be much simpler to just add one varint to txs for that purpose

This has the problem of leaking that the tx was time-locked.

> A more privacy-oriented solution would https://github.com/monero-project/research-lab/issues/78#issuecomment-1003195804

More costly to store and verify.

But I digress, this discussion would be more suitable for the time locks issue. I just wanted to point out that ring selection could be used as a proxy time lock.

# Action History
- Created by: UkoeHB | 2021-06-01T02:08:36+00:00
