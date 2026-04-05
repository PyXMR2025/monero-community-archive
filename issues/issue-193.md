---
title: Formalizing `benches/`
source_url: https://github.com/Cuprate/cuprate/issues/193
author: hinto-janai
assignees: []
labels:
- C-proposal
- A-benches
created_at: '2024-06-25T21:22:35+00:00'
updated_at: '2024-11-25T20:10:44+00:00'
type: issue
status: closed
closed_at: '2024-11-25T20:10:43+00:00'
---

# Original Description
## What
I propose we have 2 categories of benchmarks:
- Micro (criterion)
- Macro (harness)

Micro benchmarks will use [Criterion](https://bheisler.github.io/criterion.rs/book/user_guide/advanced_configuration.html). They will time single functions, groups of functions, and generally be small in scope.

Macro benchmarks will operate under a custom made harness (just another crate we make, `cuprate-benchmark`). These will test sub-systems, or sections of a sub-system, e.g. the block downloader, the RPC server, the database, etc.

The harness does not need to be complex, it can be very simple, see `# How`.

## When
This proposal only sets the precedent moving forward.

I believe creating the macro benchmarks _after_ Cuprate's internals are relatively stable is best.

## Why
[Quoting myself:](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/456)

> Creating a bespoke benchmarking tool would be a project of its own, so Cuprate is planning to use the Criterion project.

I lied, but only a little bit. Creating a vast and extensive benchmarking tool would be a project of its own, but this proposal is only suggesting a very simple one, such that we at least have _something_ rather than nothing when it comes to (sub-)system performance / resource usage.

The main value in benchmarks for us is not necessarily measuring nominal speed, but rather, measuring the difference between current and future code.

Getting a baseline of current behavior allows us to actually measure differences in supposed improvements and/or see regressions.

## Where
| Sub-directory       | Purpose | Example |
|---------------------|---------|---------|
| `benches/criterion/cuprate-*` | Micro-benchmarks for crates (e.g. timings for a single function) | `benches/criterion/cuprate-json-rpc`, `benches/criterion/cuprate-database` |
| `benches/benchmark/cuprate-*` | Macro-benchmarks for _whole_ crates or sub-systems | `benches/benchmark/rpc` |
| `benches/benchmark/lib`       | The benchmarking library/trait all benchmarks implement
| `benches/benchmark/bin`       | The actual benchmarking binary linking all benchmarks together

## How
The `criterion` benchmarks are straightforward, they use `criterion` and measure small functions.

The custom harness can be as simple as:
```rust
// A benchmarking function and its inputs.
pub trait Benchmark {
    // Input to the main benchmarking function.
    type Input;

    // Setup function to generate the input.
    const SETUP: fn() -> Self::Input;

    // The main function to benchmark.
    const MAIN: fn(Self::Input);
}

#[cfg(feature = "rpc")]
use cuprate_benchmark_rpc::BenchmarkRpc as B;
#[cfg(feature = "...")]
use cuprate_benchmark_other::BenchmarkOther as B;
/* ... */

fn main() {
    let input = B::SETUP();
    let now = std::time::Instant::now();
    B::MAIN(input);
    println!("{}", now.elapsed().as_secs_f32());
}
```
The point of `trait Benchmark` is to standardize the behavior of all benchmarks, conceptually, it is just:
1. Set-up the benchmark
2. Start timer
3. Run benchmark
4. Print data

This also means that Cuprate's crates must be modular enough such that sub-systems like this can be created/instrumented. Doing this should already be a goal, but these benchmarks slightly enforce it.

For example, a very simple `cuprate_database` benchmark:
```rust
struct BenchmarkDatabase;
impl Benchmark for BenchmarkDatabase {
    type Input = ConcreteEnv;
    const SETUP: fn() -> Self::Input = /* ... */;
    const MAIN: fn(Self::Input) = |_| {
        // 1. Open table
        // 2. Write lots of data to it
        // 3. Return
    };
}
```
Now, before merging a large PR that changes `cuprate_database`, this benchmark is ran with and without the changes to measure differences.

This measurement is obviously not the most rigorous, but that is not the point. The point is to have quick and dirty benchmarks ready to go as a first pass "performance review".

It's worth noting I already create these type of benchmarks for stuff over and over again; storing them in-tree would be helpful.

## Future
This is out-of-scope for this proposal, but eventually we could setup @moo900 to run `benches/` automatically, e.g.:

1. PR is created
2. Allowed user comments `@moo900 bench <benchmark>`
3. @moo900 runs the benchmark on main and the PR branch
4. @moo900 comments pretty performance diffs

Ideally this is running on a completely quiet machine, the current VPS @moo900 is running on is not.


# Discussion History
# Action History
- Created by: hinto-janai | 2024-06-25T21:22:35+00:00
- Closed at: 2024-11-25T20:10:43+00:00
