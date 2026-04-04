---
title: Wallet-side "binning" PoC for decoy selection algo
source_url: https://github.com/monero-project/research-lab/issues/88
author: j-berman
assignees: []
labels: []
created_at: '2021-10-14T03:55:31+00:00'
updated_at: '2022-04-13T18:33:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## Overview

This is a simplified approach to "binning" done purely in the client. It's meant to demonstrate a PoC that can be implemented in `wallet2` today, while iterating toward a space-saving solution described in @UkoeHB's #84 (which will pair well with significantly larger ring sizes). I debated just implementing this in `wallet2` and submitting a PR, but I figured a PoC would be easier to grok and critique.

Refresher, binning is a strategy in the decoy selection algorithm to select "bins" of decoys, such that the outputs in each bin are temporally close. For example, with a ring size of 22, rather than compose the ring of 22 outputs that span the entire chain, binning instead composes the ring of (for example) 11 bins with 2 bin members in each bin (11 bins * 2 bin members = 22 outputs in the ring). The 11 bins would span the entire chain, but the members in each bin would be temporally close.

Pro: binning mitigates weaknesses of strictly using an estimated spend-time distribution (such as a gamma distribution) to select decoys. Con: reduces the number of selections that can span the entire chain.

Deeper analysis of the pros and cons of binning in general (and parameter choice) is left out of this description. For more on binning, see [Möser et al section 6.2](https://arxiv.org/pdf/1704.04299/), #84, and #86.

### The proposed algorithm

There are 3 main steps in the proposed algorithm:

1. gamma pick outputs (the same way the wallet currently does)
2. determine which bin in the chain each output is in
3. finish selecting decoys by randomly picking outputs from selected bins

When the algorithm runs, all outputs that are 10 blocks old and older are each members of a particular bin in the chain. There can be many outputs in a single bin, and every output belongs to a single bin. Bins span a fixed number of blocks (rather than a fixed number of outputs). And in the final step of the algorithm, decoys are randomly selected from bins. This approach has a number of benefits which will be explained later.

### Walking through the algorithm

It's easiest to explain how the algorithm works in detail by walking through an example. Assume the chain has 5 blocks with 11 total outputs. Block 0 has 1 output in it, block 1 has 3 outputs in it (Output ID's 1, 2, and 3), block 2 has 1 output, block 3 has 3 outputs, block 4 has 3 outputs...

```
block 0: {0}
block 1: {1, 2, 3}
block 2: {4}
block 3: {5, 6, 7}
block 4: {8, 9, 10}
```

Assume a `BIN_WIDTH_IN_BLOCKS` of 2. The algorithm "re-arranges" its view of the chain as follows:

```
bin_index 0: {10, 9, 8, 7, 6, 5} // blocks 4, 3
bin_index 1: { 4, 3, 2, 1, 0}    // blocks 2, 1, 0 -- block 0 is tacked onto the final bin, as opposed to adding a new bin just for the single block 0
```

Assume the real output is **Output ID 3**. The algorithm therefore makes sure to use `bin_index 1` in the ring.

When selecting decoy bins, the algorithm gamma picks an output using the same approach currently used to select decoys, then determines the bin that output is in. For example, assume the algorithm gamma picks `Output ID 9`, therefore `bin_index 0` will also be used in the ring, along with `bin_index 1`.

Continuing the example, stick with the assumption that `BIN_WIDTH_IN_BLOCKS` is 2, and assume the number of members per bin in the ring is 2 and the ring size is 4. This means the final ring will be composed of 2 bins with 2 bin members each.

Taking stock: at this point in the algorithm, the wallet knows that output ID's **3** and **9** will be in the final ring, and therefore bins 1 and 0 will be the bins used in the ring. The wallet now needs to select 1 additional output from `bin_index 1`, and 1 additional output from `bin_index 0` to complete the ring:

- the algorithm randomly picks 1 additional output from `bin_index 1` in order to complete the first bin (the picked output is equally probable to be either Output ID 4, 2, 1, 0). Assume the algorithm picks `Output ID 1`.

- the algorithm randomly picks 1 additional output from `bin_index 0` in order to complete the next bin (equally probable to be either Output ID 10, 8, 7, 6, 5). Assume the algorithm picks `Output ID 5`.

Thus, the final ring is: `{{1, 3}, {5, 9}}`.

### Sample result with more realistic parameters

When using the following parameters:

- `BIN_WIDTH_IN_BLOCKS`: 2
- `NUM_BIN_MEMBERS`: 2
- `NUM_BINS`: 8

and selecting decoys for Output ID 40261601 at height 2465609, a sample ring could look like this:

```
 Bin 1...
     Bin Member 1, output ID 40298540 (DECOY)
     Bin Member 2, output ID 40298554 (DECOY)
 Bin 2...
     Bin Member 1, output ID 40298479 (DECOY)
     Bin Member 2, output ID 40298483 (DECOY)
 Bin 3...
     Bin Member 1, output ID 40280042 (DECOY)
     Bin Member 2, output ID 40280106 (DECOY)
 Bin 4...
     Bin Member 1, output ID 40261601 (REAL)
     Bin Member 2, output ID 40261881 (DECOY)
 Bin 5...
     Bin Member 1, output ID 40010971 (DECOY)
     Bin Member 2, output ID 40010970 (DECOY)
 Bin 6...
     Bin Member 1, output ID 39762824 (DECOY)
     Bin Member 2, output ID 39763234 (DECOY)
 Bin 7...
     Bin Member 1, output ID 38287723 (DECOY)
     Bin Member 2, output ID 38287762 (DECOY)
 Bin 8...
     Bin Member 1, output ID 25236697 (DECOY)
     Bin Member 2, output ID 25236960 (DECOY)
```

### How this differs from Möser et al's approach

Möser et al's approach is functionally very similar to the above approach, with some crucial differences in their approach:

1. bins are a set number of outputs (not a set number of blocks)
2. `bin_width` is equal to the number of members per bin
3. bins stay constant, since they are fixed by the node as each block is added to the chain

Unfortunately Monero's custom timelocks complicate the Möser approach. As described by @UkoeHB here:

> What if the local outputs around the output you want to spend are all locked? There might not be enough decoy outputs available to make a bin with the real spend in it. This opens a serious attack vector.

Therefore, since RingCT outputs can be locked into the future even if the timelock feature is deprecated in the near-term, the algorithm must allow for a `bin_width` wider than the number of members per bin that ultimately gets included in a ring, just in case the other outputs in the bin are locked preventing unlocked outputs from being spendable.

In this proposed algorithm, it's suggested to use a `BIN_WIDTH_IN_BLOCKS >= NUM_BIN_MEMBERS`, to guarantee that there will be enough unlocked outputs to use in the ring. This way it's guaranteed the coinbase outputs can be used to construct a ring once they unlock after 60 blocks, even if all other outputs in the bin are locked.

Another interesting thing they do in the Möser paper is use block headers to shuffle outputs in a bin in order to mitigate a miner ordering outputs in a block to the miner's benefit. The same effect is achieved by randomly selecting outputs from bins in the final step of this proposed algorithm.

### Benefits of this approach compared to other binning approaches

- achieves the goal of binning to select temporally close outputs
- effectively mitigates the threat of a miner ordering transactions in a block to their advantage
- works around locked outputs in what seems to be a safe way, pending more review

## The code

For anyone reading the code, I suggest to start from `binning_algorithm_demo`. In order to run this code, simply replace the contents of `blockchain_usage.cpp` with the code below (and run it the same way you'd run `monero-blockchain-usage`). It takes a bit to run the first time (it's reading the RingCT output distribution from the db), but subsequent runs are fast (since the RingCT output distribution gets written to disk as a file.. I'm sure there's a more clever way to do this, but it works alright here). I also included a sample output at the bottom of this description.

```cpp
// Copyright (c) 2014-2020, The Monero Project
//
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without modification, are
// permitted provided that the following conditions are met:
//
// 1. Redistributions of source code must retain the above copyright notice, this list of
//    conditions and the following disclaimer.
//
// 2. Redistributions in binary form must reproduce the above copyright notice, this list
//    of conditions and the following disclaimer in the documentation and/or other
//    materials provided with the distribution.
//
// 3. Neither the name of the copyright holder nor the names of its contributors may be
//    used to endorse or promote products derived from this software without specific
//    prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
// EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
// MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
// THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
// PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
// INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
// STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
// THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#include <boost/range/adaptor/transformed.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/filesystem/path.hpp>
#include "common/command_line.h"
#include "common/varint.h"
#include "cryptonote_core/tx_pool.h"
#include "cryptonote_core/cryptonote_core.h"
#include "cryptonote_core/blockchain.h"
#include "blockchain_db/blockchain_db.h"
#include "version.h"
#include "crypto/crypto.h"

#undef MONERO_DEFAULT_LOG_CATEGORY
#define MONERO_DEFAULT_LOG_CATEGORY "bcutil"

constexpr const uint64_t TEST_HEIGHT = 2465609;
constexpr const uint64_t TEST_REAL_OUTPUT_ID = 40261601;

#define NUM_DECOYS 15
#define NUM_BIN_MEMBERS 2
#define NUM_BINS ((NUM_DECOYS+1)/NUM_BIN_MEMBERS)
static_assert((NUM_DECOYS+1)%NUM_BIN_MEMBERS==0, "implementation does not support remainder bin members");

#define BIN_WIDTH_IN_BLOCKS 2
static_assert(BIN_WIDTH_IN_BLOCKS>=NUM_BIN_MEMBERS, "must have more blocks than bin members to guarantee outputs can be spent, even if many empty blocks mined in a row");

#define GAMMA_SHAPE 19.28
#define GAMMA_SCALE (1/1.61)

constexpr const std::size_t BLOCKS_IN_A_YEAR = (86400 * 365) / DIFFICULTY_TARGET_V2;
constexpr const std::size_t DEFAULT_UNLOCK_TIME = CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE * DIFFICULTY_TARGET_V2;
constexpr const std::size_t RECENT_SPEND_WINDOW = 15 * DIFFICULTY_TARGET_V2;

#define CSV_FILE_DELIMITER ", "

namespace po = boost::program_options;
using namespace epee;
using namespace cryptonote;

struct gamma_engine
{
  typedef uint64_t result_type;
  static constexpr result_type min() { return 0; }
  static constexpr result_type max() { return std::numeric_limits<result_type>::max(); }
  result_type operator()() { return crypto::rand<result_type>(); }
} engine;

// load from file if present
std::vector<uint64_t> load_rct_offsets(uint64_t height)
{
  std::vector<uint64_t> rct_offsets;
  std::string line;
  std::ifstream rct_offsets_file ("rct_offsets_" + std::to_string(height) + ".txt");
  if (rct_offsets_file.is_open())
  {
    while ( getline (rct_offsets_file, line) )
    {
      size_t last = 0;
      size_t next = 0;
      while ((next = line.find(CSV_FILE_DELIMITER, last)) != std::string::npos) { 
        last = next + 1;
      }
      std::string str = line.substr(last);
      uint64_t ul = std::stoul (str,nullptr,0);

      rct_offsets.push_back(ul);
    }
    rct_offsets_file.close();

    return rct_offsets;
  }
  else
  {
    LOG_PRINT_L0("No rct offsets saved at height " << height << std::endl);
  }

  return rct_offsets;
}

void write_rct_offsets_file(std::vector<uint64_t> rct_offsets, uint64_t height)
{
  std::ofstream rct_offsets_file;
  rct_offsets_file.open ("rct_offsets_" + std::to_string(height) + ".txt");
  for (const auto a: rct_offsets)
    rct_offsets_file << a << "\n";

  rct_offsets_file.close();
}

std::pair<uint64_t, uint64_t> get_bin_start_and_end_rct_offset_indexes(uint64_t most_recent_rct_offset_index, uint64_t bin_index)
{
  uint64_t expected_difference_from_most_recent = bin_index * BIN_WIDTH_IN_BLOCKS;

  if (expected_difference_from_most_recent > most_recent_rct_offset_index)
    throw std::logic_error("expected_difference_from_most_recent cannot be greater than most_recent_rct_offset_index");

  uint64_t bin_start_rct_offset_index = most_recent_rct_offset_index - expected_difference_from_most_recent;
  uint64_t bin_end_rct_offset_index = bin_start_rct_offset_index > BIN_WIDTH_IN_BLOCKS ? bin_start_rct_offset_index - BIN_WIDTH_IN_BLOCKS : 0;

  if (bin_end_rct_offset_index < BIN_WIDTH_IN_BLOCKS)
    bin_end_rct_offset_index = 0;

  return std::make_pair(bin_start_rct_offset_index, bin_end_rct_offset_index);
}

std::pair<uint64_t, uint64_t> get_bin_start_and_end_output_ids(std::vector<uint64_t> rct_offsets, uint64_t most_recent_rct_offset_index, uint64_t bin_index)
{
  std::pair<uint64_t, uint64_t> start_and_end_rct_offset_indexes;
  start_and_end_rct_offset_indexes = get_bin_start_and_end_rct_offset_indexes(most_recent_rct_offset_index, bin_index);

  uint64_t bin_start_output_id = rct_offsets[start_and_end_rct_offset_indexes.first] - 1;
  uint64_t bin_end_output_id = rct_offsets[start_and_end_rct_offset_indexes.second];

  return std::make_pair(bin_start_output_id, bin_end_output_id);
}

uint64_t get_rct_offset_index(std::vector<uint64_t> rct_offsets, uint64_t most_recent_rct_offset_index, uint64_t output_index)
{
  for (uint64_t rct_offset_index = most_recent_rct_offset_index; rct_offset_index != 0; --rct_offset_index)
  {
    if (rct_offsets[rct_offset_index] <= output_index)
      return rct_offset_index + 1;
  }
  return 0;
}

/**
 *
 * Lines up bins of a fixed # of blocks starting at the tip of spendable outputs, while allowing the final
 * bin to be wider when there is a remainder. For example, if there are 11 spendable outputs 
 * in the chain like this:
 *
 * block 0: {0}
 * block 1: {1, 2, 3}
 * block 2: {4}
 * block 3: {5, 6, 7}
 * block 4: {8, 9, 10}
 *
 * Assume a `BIN_WIDTH_IN_BLOCKS` of 2. The algorithm "re-arranges" its view of the chain as follows:
 *
 * bin_index 0: {10, 9, 8, 7, 6, 5} // blocks 3, 4
 * bin_index 1: { 4, 3, 2, 1, 0} // blocks 0, 1, 2 -- block 0 is tacked onto the final bin, as opposed to adding a new bin just for the single block 0
 *
 * Where bin_index 0 is the bin closest to the tip of the chain and has output ID's 10, 9, 8, 7, 6, 5 in it,
 * and bin_index 1 is the final bin.
 *
 * This is contrast to allowing a `bin_index 2` with just {0} in it. This ensures that the final
 * bin has enough outputs to use to construct a bin.
 *
 */
uint64_t get_bin_index(std::vector<uint64_t> rct_offsets, uint64_t most_recent_rct_offset_index, uint64_t output_index)
{
  uint64_t rct_offset_index = get_rct_offset_index(rct_offsets, most_recent_rct_offset_index, output_index);

  uint64_t height_diff_from_tip = most_recent_rct_offset_index - rct_offset_index;
  uint64_t bin_index = height_diff_from_tip / BIN_WIDTH_IN_BLOCKS;

  // check if bin is the final bin_index
  if (bin_index > 0 && rct_offset_index < BIN_WIDTH_IN_BLOCKS && height_diff_from_tip % BIN_WIDTH_IN_BLOCKS != 0)
    bin_index -= 1;

  return bin_index;
}

// copied from monero-lws: https://github.com/vtnerd/monero-lws/pull/22
uint64_t gamma_pick(std::vector<uint64_t> rct_offsets, double outputs_per_second)
{
  const auto end = rct_offsets.end() - CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE;
  const uint64_t num_rct_outputs = *(rct_offsets.end() - CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE - 1);
  std::gamma_distribution<double> gamma(GAMMA_SHAPE, GAMMA_SCALE);

  for (unsigned tries = 0; tries < 100; ++tries)
  {
    double output_age_in_seconds = std::exp(gamma(engine));

    // shift output back by unlock time to apply distribution from chain tip
    if (output_age_in_seconds > DEFAULT_UNLOCK_TIME)
      output_age_in_seconds -= DEFAULT_UNLOCK_TIME;
    else
      output_age_in_seconds = crypto::rand_idx(RECENT_SPEND_WINDOW);

    uint64_t output_index = output_age_in_seconds * outputs_per_second;
    if (num_rct_outputs <= output_index)
        continue; // gamma selected older than blockchain height (rare)

    output_index = num_rct_outputs - 1 - output_index;
    const auto selection = std::lower_bound(rct_offsets.begin(), end, output_index);
    if (selection == end)
      throw std::logic_error{"Unable to select random output - output not found in range (should never happen)"};

    const std::uint64_t first_rct = rct_offsets.begin() == selection ? 0 : *(selection - 1);
    const std::uint64_t n_rct = *selection - first_rct;
    if (n_rct != 0)
      return first_rct + crypto::rand_idx(n_rct);
      // block had zero outputs (miner didn't collect XMR?)
  }
  throw std::runtime_error{"Unable to select random output in spendable range using gamma distribution after 100 attempts"};
}

/**
 * 
 * For the real output, determine the bin it's in, then add it to the array of outputs that will be used to construct bins.
 * 
 * For decoy bins, first gamma pick an output, then determine the bin that output is in, then add it to the array.
 * 
 * Don't allow repeat bins.
 *
 */
std::vector<uint64_t> select_outputs_for_bin_selection(uint64_t real_output_id, uint64_t most_recent_rct_offset_index, 
    std::vector<uint64_t> rct_offsets, double outputs_per_second)
{
  std::vector<uint64_t> output_ids;
  std::unordered_set<uint64_t> seen_bin_indexes;

  // For consideration: select bins from quantiles of the PDF
  // TODO: over-select outputs in case some are locked
  while (output_ids.size() < NUM_BINS)
  {
    uint64_t output_id;

    if (output_ids.size() == 0)
      output_id = real_output_id;
    else
      output_id = gamma_pick(rct_offsets, outputs_per_second);

    uint64_t bin_index = get_bin_index(rct_offsets, most_recent_rct_offset_index, output_id);

    if (seen_bin_indexes.count(bin_index) == 0)
    {
      output_ids.push_back(output_id);
      seen_bin_indexes.insert(bin_index);
    }
  }

  return output_ids;
}

/**
 * 
 * Iterate over the selected outputs, then randomly select outputs from each bin.
 * 
 */
std::vector<std::vector<uint64_t>> construct_bins(std::vector<uint64_t> outputs_for_bin_selection, uint64_t real_output_id,
    uint64_t most_recent_rct_offset_index, std::vector<uint64_t> rct_offsets)
{
  std::vector<std::vector<uint64_t>> bins;
  std::unordered_set<uint64_t> seen_output_ids;
  for (uint64_t i = 0; i < NUM_BINS; ++i)
  {
    std::vector<uint64_t> bin;
    uint64_t output_id_for_bin_selection = outputs_for_bin_selection[i];

    // get bin data needed to select random outputs from the bin
    uint64_t bin_index = get_bin_index(rct_offsets, most_recent_rct_offset_index, output_id_for_bin_selection);
    std::pair<uint64_t, uint64_t> bin_start_and_end_output_ids = get_bin_start_and_end_output_ids(rct_offsets, most_recent_rct_offset_index, bin_index);

    uint64_t bin_start_output_id = bin_start_and_end_output_ids.first;
    uint64_t bin_end_output_id = bin_start_and_end_output_ids.second;
    uint64_t bin_num_outputs = bin_start_output_id - bin_end_output_id + 1;

    MINFO("Bin " << i + 1 << " with bin index " << bin_index << " and starting output ID " << bin_start_output_id << " and ending output ID " 
      << bin_end_output_id << " (" << bin_num_outputs << " outputs in bin)...\n");

    uint64_t output_id;

    // TODO: request more outputs than needed for each bin, similar to how client does today
    for (uint64_t j = 0; j < NUM_BIN_MEMBERS; ++j)
    {
      if (j == 0)
        output_id = output_id_for_bin_selection;
      else
      {
        output_id = bin_start_output_id - crypto::rand_idx(bin_num_outputs);
        while (seen_output_ids.count(output_id) != 0)
          output_id = bin_start_output_id - crypto::rand_idx(bin_num_outputs);
        // TODO: implement fail-safe max attempts allowed, widen bin on failure
      }

      bin.push_back(output_id);
      seen_output_ids.insert(output_id);
      MINFO("    Bin Member " << j + 1 << ", output ID " << output_id << " (" << (output_id == real_output_id ? "REAL" : "DECOY") << ")\n");
    }

    bins.push_back(bin);
  }

  return bins;
}

/**
 * 
 * Step 1: set up gamma distribution params
 * Step 2: gamma pick outputs to be used to select bins
 * Step 3: randomly pick outputs from selected bins
 *
 */
void binning_algorithm_demo(std::vector<uint64_t> rct_offsets, uint64_t real_output_id)
{
  // Step 1: set up gamma distribution params
  const std::size_t blocks_to_consider = std::min(rct_offsets.size(), BLOCKS_IN_A_YEAR);
  const std::uint64_t initial = blocks_to_consider < rct_offsets.size() ?
    rct_offsets[rct_offsets.size() - blocks_to_consider - 1] : 0;
  const std::size_t outputs_to_consider = rct_offsets.back() - initial;

  double outputs_per_block = outputs_to_consider / static_cast<double>(BLOCKS_IN_A_YEAR);
  double outputs_per_second = outputs_per_block / DIFFICULTY_TARGET_V2;

  const uint64_t most_recent_rct_offset_index = rct_offsets.size() > CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE - 1 ?
    rct_offsets.size() - CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE - 1 : 0;

  // Step 2: gamma pick outputs to be used to select bins
  std::vector<uint64_t> outputs_for_bin_selection = select_outputs_for_bin_selection(real_output_id,
      most_recent_rct_offset_index, rct_offsets, outputs_per_second);

  // sort for clearer logging
  std::sort(outputs_for_bin_selection.begin(), outputs_for_bin_selection.end(), std::greater<uint64_t>());

  // Step 3: randomly pick outputs from selected bins
  std::vector<std::vector<uint64_t>> bins = construct_bins(outputs_for_bin_selection, real_output_id,
      most_recent_rct_offset_index, rct_offsets);

  // TODO: get all the output pub keys

  // TODO: if there aren't enough unlocked outputs in a particular bin to construct a ring, then request ALL
  // outputs from that bin. If there aren't at least NUM_BIN_MEMBERS unlocked outputs in a bin, then bin is unusable.
  // Throw bin away and re-select another bin...
}

int main(int argc, char* argv[])
{
  TRY_ENTRY();

  epee::string_tools::set_module_name_and_folder(argv[0]);

  uint32_t log_level = 0;

  tools::on_startup();

  boost::filesystem::path output_file_path;

  po::options_description desc_cmd_only("Command line options");
  po::options_description desc_cmd_sett("Command line options and settings options");
  const command_line::arg_descriptor<std::string> arg_log_level  = {"log-level",  "0-4 or categories", ""};
  const command_line::arg_descriptor<std::string> arg_input = {"input", ""};

  command_line::add_arg(desc_cmd_sett, cryptonote::arg_testnet_on);
  command_line::add_arg(desc_cmd_sett, cryptonote::arg_stagenet_on);
  command_line::add_arg(desc_cmd_sett, arg_log_level);
  command_line::add_arg(desc_cmd_sett, arg_input);
  command_line::add_arg(desc_cmd_only, command_line::arg_help);

  po::options_description desc_options("Allowed options");
  desc_options.add(desc_cmd_only).add(desc_cmd_sett);

  po::positional_options_description positional_options;
  positional_options.add(arg_input.name, -1);

  po::variables_map vm;
  bool r = command_line::handle_error_helper(desc_options, [&]()
  {
    auto parser = po::command_line_parser(argc, argv).options(desc_options).positional(positional_options);
    po::store(parser.run(), vm);
    po::notify(vm);
    return true;
  });
  if (! r)
    return 1;

  if (command_line::get_arg(vm, command_line::arg_help))
  {
    std::cout << "Monero '" << MONERO_RELEASE_NAME << "' (v" << MONERO_VERSION_FULL << ")" << ENDL << ENDL;
    std::cout << desc_options << std::endl;
    return 1;
  }

  mlog_configure(mlog_get_default_log_path("monero-binning-poc.log"), true);
  if (!command_line::is_arg_defaulted(vm, arg_log_level))
    mlog_set_log(command_line::get_arg(vm, arg_log_level).c_str());
  else
    mlog_set_log(std::string(std::to_string(log_level) + ",bcutil:INFO").c_str());

  LOG_PRINT_L0("Starting...");

  bool opt_testnet = command_line::get_arg(vm, cryptonote::arg_testnet_on);
  bool opt_stagenet = command_line::get_arg(vm, cryptonote::arg_stagenet_on);
  network_type net_type = opt_testnet ? TESTNET : opt_stagenet ? STAGENET : MAINNET;

  // If we wanted to use the memory pool, we would set up a fake_core.

  // Use Blockchain instead of lower-level BlockchainDB for two reasons:
  // 1. Blockchain has the init() method for easy setup
  // 2. exporter needs to use get_current_blockchain_height(), get_block_id_by_height(), get_block_by_hash()
  //
  // cannot match blockchain_storage setup above with just one line,
  // e.g.
  //   Blockchain* core_storage = new Blockchain(NULL);
  // because unlike blockchain_storage constructor, which takes a pointer to
  // tx_memory_pool, Blockchain's constructor takes tx_memory_pool object.
  LOG_PRINT_L0("Initializing source blockchain (BlockchainDB)");
  const std::string input = command_line::get_arg(vm, arg_input);
  std::unique_ptr<Blockchain> core_storage;
  tx_memory_pool m_mempool(*core_storage);
  core_storage.reset(new Blockchain(m_mempool));
  BlockchainDB* db = new_db();
  if (db == NULL)
  {
    LOG_ERROR("Failed to initialize a database");
    throw std::runtime_error("Failed to initialize a database");
  }
  LOG_PRINT_L0("database: LMDB");

  const std::string filename = input;
  LOG_PRINT_L0("Loading blockchain from folder " << filename << " ...");

  try
  {
    db->open(filename, DBF_RDONLY);
  }
  catch (const std::exception& e)
  {
    LOG_PRINT_L0("Error opening database: " << e.what());
    return 1;
  }
  r = core_storage->init(db, net_type);

  CHECK_AND_ASSERT_MES(r, 1, "Failed to initialize source blockchain storage");
  LOG_PRINT_L0("Source blockchain storage initialized OK");

  uint64_t height = TEST_HEIGHT;
  uint64_t real_output_id = TEST_REAL_OUTPUT_ID;

  // get RingCT output distribution
  LOG_PRINT_L0("Loading rct offsets...");
  std::vector<uint64_t> rct_offsets = load_rct_offsets(height);

  if (rct_offsets.size() == 0)
  {
    std::vector<uint64_t> heights;
    for (uint64_t h = 0; h < height; ++h)
      heights.push_back(h);
    rct_offsets = (std::vector<uint64_t>) core_storage->get_db().get_block_cumulative_rct_outputs(heights);
    
    // write the file to disk so can eager load it on future runs while testing
    write_rct_offsets_file(rct_offsets, height);
  }
  LOG_PRINT_L0("Finished loading rct offsets"); 

  LOG_PRINT_L0("Starting binning algorithm demo..."); 
  binning_algorithm_demo(rct_offsets, real_output_id);

  LOG_PRINT_L0("Binning algorithm demo complete");
  return 0;

  CATCH_ENTRY("Export error", 1);
}

```

Here is an output sample from running the above code:

```
2021-10-28 05:57:46.721	W Starting...
2021-10-28 05:57:46.721	W Initializing source blockchain (BlockchainDB)
2021-10-28 05:57:46.722	W database: LMDB
2021-10-28 05:57:46.773	W Source blockchain storage initialized OK
2021-10-28 05:57:46.773	W Loading rct offsets...
2021-10-28 05:57:46.904	W Finished loading rct offsets
2021-10-28 05:57:46.904	W Starting binning algorithm demo...
2021-10-28 05:57:47.095	I Bin 1 with bin index 3 and starting output ID 40298565 and ending output ID 40298489 (77 outputs in bin)...
2021-10-28 05:57:47.096	I     Bin Member 1, output ID 40298540 (DECOY)
2021-10-28 05:57:47.096	I     Bin Member 2, output ID 40298554 (DECOY)
2021-10-28 05:57:47.114	I Bin 2 with bin index 4 and starting output ID 40298488 and ending output ID 40298469 (20 outputs in bin)...
2021-10-28 05:57:47.114	I     Bin Member 1, output ID 40298479 (DECOY)
2021-10-28 05:57:47.114	I     Bin Member 2, output ID 40298483 (DECOY)
2021-10-28 05:57:47.135	I Bin 3 with bin index 119 and starting output ID 40280154 and ending output ID 40279953 (202 outputs in bin)...
2021-10-28 05:57:47.135	I     Bin Member 1, output ID 40280042 (DECOY)
2021-10-28 05:57:47.135	I     Bin Member 2, output ID 40280106 (DECOY)
2021-10-28 05:57:47.157	I Bin 4 with bin index 214 and starting output ID 40262328 and ending output ID 40261552 (777 outputs in bin)...
2021-10-28 05:57:47.157	I     Bin Member 1, output ID 40261601 (REAL)
2021-10-28 05:57:47.157	I     Bin Member 2, output ID 40261881 (DECOY)
2021-10-28 05:57:47.178	I Bin 5 with bin index 1594 and starting output ID 40011113 and ending output ID 40010912 (202 outputs in bin)...
2021-10-28 05:57:47.178	I     Bin Member 1, output ID 40010971 (DECOY)
2021-10-28 05:57:47.178	I     Bin Member 2, output ID 40010970 (DECOY)
2021-10-28 05:57:47.198	I Bin 6 with bin index 2943 and starting output ID 39763238 and ending output ID 39762787 (452 outputs in bin)...
2021-10-28 05:57:47.198	I     Bin Member 1, output ID 39762824 (DECOY)
2021-10-28 05:57:47.198	I     Bin Member 2, output ID 39763234 (DECOY)
2021-10-28 05:57:47.219	I Bin 7 with bin index 12837 and starting output ID 38287809 and ending output ID 38287723 (87 outputs in bin)...
2021-10-28 05:57:47.219	I     Bin Member 1, output ID 38287723 (DECOY)
2021-10-28 05:57:47.219	I     Bin Member 2, output ID 38287762 (DECOY)
2021-10-28 05:57:47.240	I Bin 8 with bin index 100285 and starting output ID 25237151 and ending output ID 25236602 (550 outputs in bin)...
2021-10-28 05:57:47.240	I     Bin Member 1, output ID 25236697 (DECOY)
2021-10-28 05:57:47.240	I     Bin Member 2, output ID 25236960 (DECOY)
2021-10-28 05:57:47.243	W Binning algorithm demo complete

```

EDIT: restructured the algorithm as initially proposed to select bins of a fixed number of blocks, rather than a fixed number of outputs to avoid the flaw described [here](https://github.com/monero-project/research-lab/issues/88#issuecomment-947481223)

# Discussion History
## SamsungGalaxyPlayer | 2021-10-14T20:21:21+00:00
Accounting for the locked outputs edge case is nice to consider, but it absolutely is an edge case.

How would selection occur if someone is trying to spend a previously-locked output?

## j-berman | 2021-10-14T23:31:42+00:00
> How would selection occur if someone is trying to spend a previously-locked output?

The output would be placed in a bin of outputs *created* around the same time. So if you lock an output for 1 year and spend it right when it unlocks, then it will be placed in a bin of outputs created 1 year prior.

This is basically the same way previously-locked outputs are treated by the algorithm today: in the gamma selection, output ages are assumed based on when the outputs are created, not based on when they unlock (including coinbase outputs).

If alternatively outputs are placed in a bin together with outputs that *unlock* around the same time, then as @UkoeHB highlighted in this ["possible poison attack"](https://github.com/monero-project/research-lab/issues/78#issuecomment-913046076), it introduces a vector for an attacker to gradually construct many outputs over time that unlock at a specific time in the future.

> Accounting for the locked outputs edge case is nice to consider, but it absolutely is an edge case.

I don't think there is a way to implement the algorithm today *without* accounting for them though. Alternatively this implementation could be kept on hold until *after* custom timelocks are deprecated (since deprecation seems to have wide support), but I don't see a safe way around *not* accounting for it in a binning algorithm today, even if the algorithm were to hypothetically go live in the same fork that would deprecate timelocks.

## iamamyth | 2021-10-15T00:54:19+00:00
> Accounting for the locked outputs edge case is nice to consider, but it absolutely is an edge case.

>> I don't think there is a way to implement the algorithm today without accounting for them

Yes, the final implementation must account for locks (though I think you've clearly sketched an outline of how they would be handled, which suffices for your PoC). Even if the algorithm were only deployed wallet-side, it's too easy for someone to throw a wrench into the works by timelocking a bunch of outputs (current usage has no impact on propensity for future mischief). In fact, not accounting for locks in any algorithm would be a great way to get more timelocked outputs.


## SamsungGalaxyPlayer | 2021-10-16T16:18:20+00:00
>  it's too easy for someone to throw a wrench into the works by timelocking a bunch of outputs

In what way is this more effective than simply spamming the same number of outputs, and then revealing these outputs publicly? The damage is already possible.

## iamamyth | 2021-10-16T19:07:38+00:00
> In what way is this more effective than simply spamming the same number of outputs, and then revealing these outputs publicly? The damage is already possible.

If the algorithm rejects locked outputs (which it must to avoid being possibly worse than existing ones in certain situations), then a bin could be "empty" and the whole construction might fail, depending on how much the implementer has ignored the issue. So, no, the plausible failure modes are not identical. I will simply add that often, for those devising or implementing an algorithm, accepting what seems like a simplifying assumption (or ignorable "corner case") actually complicates the work, as these sorts of assumptions tend to be leaky, making reasoning about the overall system more complex. For example, one could adopt all sorts of assumptions in making a wallet, but if they add up to "transaction failed" for the end user, figuring out which assumption broke and how to undo it can be much more complicated than not making the faulty assumption in the first place.

Edit: I should add that the wallet supports blacklisting outputs (in addition to auto-excluding locked ones), so if someone publishes a bunch of spent outputs, there's a mitigation (though certainly, as the current algorithm has various problems in normal operation, it wouldn't be surprising if the mitigation suffered from some).

## j-berman | 2021-10-16T20:34:04+00:00
Adding to the above: assume your real output is surrounded by many locked outputs. In order to construct a bin using the real, you would need to widen the bin in order to get unlocked outputs in the bin with your real in it.

Any observer would be able to tell from the final ring that one of the bins was widened, and can deduce which bin caused the widening based on which outputs in the ring are closer in proximity to locked outputs.

Therefore in order to avoid revealing that it’s the real output that caused widening of its bin, you need decoy outputs that can plausibly cause the bin to widen too.

Contrast this with today: if someone malicious surrounds an output with publicly known real spent outputs, it won't necessarily reveal when the surrounded output is spent because anyone else can still plausibly use that output as a decoy.

This thorn is why I included the "but" in this TODO in the algorithm:

```
  // TODO: if there aren't enough unlocked outputs to construct the ring, 2x the bin_width, and try again starting at step 2
  // but maintaining all unlocked outputs_for_bin_selection from step 3...
```
  
`outputs_for_bin_selection` are the outputs that are also gamma selected. The algorithm needs to retain those outputs when considering to widen the bin if those outputs are unlocked too.

Plaintext timelocks add these kinds of thorny edge cases to binning that the algorithm needs to account for. If we were to wait to release a binning algorithm until after plaintext timelocks were deprecated, we could choose a bin width wide enough that is guaranteed to select enough unlocked outputs every time, rather than need to dynamically widen it.

## j-berman | 2021-10-20T09:16:50+00:00
UPDATE from 10-29-21: the flaw described below was patched with the solution described. The algorithm described in the [OP](https://github.com/monero-project/research-lab/issues/88#issue-1025916968) implements the solution described below.

______

There is a flaw in the proposed algorithm: in the step where it randomly re-selects an output from a block (in order to mitigate a miner ordering a block to their advantage), it can potentially leak information that an output is a decoy in some circumstances.

In order to mitigate this completely, bins should be widened to reach block borders. This will be a relatively significant change to the proposed algorithm: instead of having bins span a set number of outputs, bins would span a set number of blocks.

Placing this proposal in WIP.

### The Flaw

```
[ = the start of a block
] = the end of the block

[0,1,2][3,4,5]
```

```
| = bin partitions

[|0,1|2][3|4,5|]
```

Assume output 2 is real (or is gamma selected). The algorithm as initially proposed would complete the bin associated with output 2 by randomly picking an output from the 2nd block. Assume the algorithm randomly picks output 4. Thus, the final bin looks like: `{2,4}`.

But if output 4 were real (or gamma selected), there would be no way for the algorithm to then select output 2 as a decoy. Thus, output 2 *must* be the starting output that was either real or gamma selected when the final bin is `{2, 4}`, and output 4 *must* be a decoy.

This flaw stems from the issue that when bins span multiple blocks, it could cause a circumstance where some outputs are guaranteed decoys. And the only safe way I see around this issue is by ensuring bins span entire blocks.

## j-berman | 2021-10-29T04:50:38+00:00
Updated the algorithm to make bins a fixed width *in blocks*, rather than a fixed # of outputs to account for the above flaw. I *believe* it's a simpler, safer, and stronger approach than was originally proposed, and handles the corner case of locked outputs much better.

## carrington1859 | 2021-11-09T23:57:15+00:00
Regarding BIN_WIDTH_IN_BLOCKS , it seems it would be useful to know from historic data how wide a window of empty blocks can be expected to be. I would assume that during events such as network upgrades there may have been long series of empty blocks. I also wonder how wide a bin can be before it starts to weaken the benefit of temporal proximity. Is a bin width of e.g. 50 blocks acceptable? When you zoom out to look at the whole chain, 50 blocks difference is still relatively near.

## j-berman | 2021-12-15T10:31:51+00:00
I figure the narrower the `BIN_WIDTH_IN_BLOCKS`:

PRO: the more effective binning will be in hindering timing analysis.
CON: the greater the damage an attacker spamming the chain with locked outputs can do.

### PRO: Edge circumstances where a narrower `BIN_WIDTH_IN_BLOCKS` hinders timing analysis

An edge case circumstance laid out by xfang in a hackerone submission where the intuition that "narrower hinders timing analysis" is clear: when constructing a split transfer to e.g. 30+ destinations, the wallet will submit multiple transactions that land in the chain adjacently in a block and look fairly similar (16-output tx's with 1 tx with some odd-sized remainder). Later on, when a user combines the change from those adjacent transactions into a single transaction, an observer can note multiple rings include outputs from adjacent transactions that can plausibly be "split transfers". A narrower `BIN_WIDTH_IN_BLOCKS` makes it more likely that people will select decoys from adjacent transactions, which provides cover for this edge case circumstance.

Here is another circumstance where "narrower" provides greater protection: if you start constructing multiple change outputs in transactions (as some wallets start to support this feature), and end up needing to combine outputs from the same transaction as inputs in a future single transaction, then again, a narrower `BIN_WIDTH_IN_BLOCKS` makes it more likely that people will select decoys from the same transaction. This would provide better cover for this action.

In both of the above circumstances, the wallet warns the user when combining outputs in this way, and these circumstances will likely become more rare with time and increased usage, but I figure ideally the algorithm would provide greater protection from the circumstance if possible.

I can't think of a circumstance that demonstrates that a wider window makes binning more effective at hindering timing analysis. Could be I'm missing something.

### CON: Narrower makes spamming the chain with locked outputs more damaging

So long as the unlock time feature remains as is, an attacker could spam the chain with blocks that are composed of many locked outputs (edit: clearer). Notably, the attacker can't control the unlock time on coinbase outputs, however, which [always unlock after 60 blocks](https://github.com/monero-project/monero/blob/cc9ca953a937979c3f4cb0a332db9ac44372191f/src/cryptonote_core/blockchain.cpp#L1363).

I chose a `BIN_WIDTH_IN_BLOCKS` of 2 in my example to match `NUM_BIN_MEMBERS` of 2, since this guarantees that all bins will have enough spendable outputs to construct rings after 60 blocks (when coinbase outputs unlock). I would think it may make sense to increase `BIN_WIDTH_IN_BLOCKS` to 10 to increase the chances honest unlocked outputs end up in the chain. But not seeing why it would be beneficial to increase to something as high as 50.

EDIT: small language change

# Action History
- Created by: j-berman | 2021-10-14T03:55:31+00:00
