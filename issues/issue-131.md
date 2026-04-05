---
title: Workspace lints
source_url: https://github.com/Cuprate/cuprate/issues/131
author: hinto-janai
assignees: []
labels:
- C-proposal
created_at: '2024-05-20T22:59:48+00:00'
updated_at: '2024-05-27T00:48:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
This issue is for discussing which initial [clippy](https://rust-lang.github.io/rust-clippy/master/index.html) and [rustc](https://doc.rust-lang.org/rustc/lints/index.html) lints will be added onto Cuprate's workspace.

Most discussion needed here is on the [`Lints (hot)`](#lints-hot) section.

## How
In the workspace `Cargo.toml`:
```toml
[workspace.lints.clippy]
clippy_lint = "deny"

[workspace.lints.rust]
rustc_lint = "deny"
```
Workspace crates must opt in to the lints, they can opt in to all like this:
```toml
[lints]
workspace = true
```

Crates can also inherit all workspace lints but allow some, like so:
```toml
# /crate/Cargo.toml
[lints]
workspace = true
```
```rust
// /crate/src/{lib,mod,file}.rs
#![allow(lint)]

// or

#[allow(lint)]
fn single_fn() {}
```

Anyway, this means the addition of lints can be separate PRs for each crate, adding lints to the workspace does nothing until opted into.

## Lints
Further below is an updated list of hand-picked lints and optional reasoning on why they should be used - all are set to `deny`.

There are 3 tables:
- cold: lints that are not contentious and/or fix small things like style
- hot: lints that cause more work for contributors and/or comes with tradeoffs
- warm: lints that are somewhat in the middle

## Adding
Since there are so many lints, I think the best method of adding them is:
1. Add all `cold/warm` lints to the workspace
1. Opt crates in gradually
1. See which lints cause unwanted changes
1. Remove the lint if deemed a net negative

This process would be repeated for any new lints.

`hot` lints can be discussed here before adding and/or be added on a per-crate basis.

## Removing
When a lint has too many false positives and/or has turned into a net negative, it can be discussed and removed in any PR.

## Fail on `rustc` warnings
Our CI currently fails on `clippy` warnings, but not `rustc` warnings, this includes things like:
- [unused_imports](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-imports)
- [unused_variables](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-variables) 
- [unused_mut](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-mut)
- [unused_allocation](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-allocation)

We could do this in a manually started CI for release binaries as they may be too annoying when testing/debugging. Another option is using the `github-actions` bot to occasionally create PRs with the errors, which can be fixed by someone else.

## Lints (cold)

| Lint | Reasoning |
|------|-----------|
| [`borrow_as_ptr`](https://rust-lang.github.io/rust-clippy/master/index.html#borrow_as_ptr) | |
| [`case_sensitive_file_extension_comparisons`](https://rust-lang.github.io/rust-clippy/master/index.html#case_sensitive_file_extension_comparisons) | |
| [`cast_lossless`](https://rust-lang.github.io/rust-clippy/master/index.html#cast_lossless) | Explicitness |
| [`cast_ptr_alignment`](https://rust-lang.github.io/rust-clippy/master/index.html#cast_ptr_alignment) | Explicitness, safety |
| [`checked_conversions`](https://rust-lang.github.io/rust-clippy/master/index.html#checked_conversions) | Explicitness |
| [`cloned_instead_of_copied`](https://rust-lang.github.io/rust-clippy/master/index.html#cloned_instead_of_copied) | |
| [`doc_link_with_quotes`](https://rust-lang.github.io/rust-clippy/master/index.html#doc_link_with_quotes) | |
| [`empty_enum`](https://rust-lang.github.io/rust-clippy/master/index.html#empty_enum) | Either use `!` in signatures or `std::convert::Infallible` |
| [`enum_glob_use`](https://rust-lang.github.io/rust-clippy/master/index.html#enum_glob_use) | |
| [`expl_impl_clone_on_copy`](https://rust-lang.github.io/rust-clippy/master/index.html#expl_impl_clone_on_copy) | |
| [`explicit_into_iter_loop`](https://rust-lang.github.io/rust-clippy/master/index.html#explicit_into_iter_loop) | |
| [`filter_map_next`](https://rust-lang.github.io/rust-clippy/master/index.html#filter_map_next) | |
| [`flat_map_option`](https://rust-lang.github.io/rust-clippy/master/index.html#flat_map_option) | |
| [`from_iter_instead_of_collect`](https://rust-lang.github.io/rust-clippy/master/index.html#from_iter_instead_of_collect) | |
| [`if_not_else`](https://rust-lang.github.io/rust-clippy/master/index.html#if_not_else) | Less double negatives
| [`ignored_unit_patterns`](https://rust-lang.github.io/rust-clippy/master/index.html#ignored_unit_patterns) | |
| [`inconsistent_struct_constructor`](https://rust-lang.github.io/rust-clippy/master/index.html#inconsistent_struct_constructor) | |
| [`index_refutable_slice`](https://rust-lang.github.io/rust-clippy/master/index.html#index_refutable_slice) | Safety |
| [`inefficient_to_string`](https://rust-lang.github.io/rust-clippy/master/index.html#inefficient_to_string) | Performance |
| [`invalid_upcast_comparisons`](https://rust-lang.github.io/rust-clippy/master/index.html#invalid_upcast_comparisons) | |
| [`iter_filter_is_ok`](https://rust-lang.github.io/rust-clippy/master/index.html#iter_filter_is_ok) | |
| [`iter_filter_is_some`](https://rust-lang.github.io/rust-clippy/master/index.html#iter_filter_is_some) | |
| [`implicit_clone`](https://rust-lang.github.io/rust-clippy/master/index.html#implicit_clone) | |
| [`manual_c_str_literals`](https://rust-lang.github.io/rust-clippy/master/index.html#manual_c_str_literals) | |
| [`manual_instant_elapsed`](https://rust-lang.github.io/rust-clippy/master/index.html#manual_instant_elapsed) | |
| [`manual_is_variant_and`](https://rust-lang.github.io/rust-clippy/master/index.html#manual_is_variant_and) | |
| [`manual_let_else`](https://rust-lang.github.io/rust-clippy/master/index.html#manual_let_else) | |
| [`manual_ok_or`](https://rust-lang.github.io/rust-clippy/master/index.html#manual_ok_or) | |
| [`manual_string_new`](https://rust-lang.github.io/rust-clippy/master/index.html#manual_string_new) | |
| [`map_unwrap_or`](https://rust-lang.github.io/rust-clippy/master/index.html#map_unwrap_or) | |
| [`match_bool`](https://rust-lang.github.io/rust-clippy/master/index.html#match_bool) | |
| [`match_same_arms`](https://rust-lang.github.io/rust-clippy/master/index.html#match_same_arms) | |
| [`match_wildcard_for_single_variants`](https://rust-lang.github.io/rust-clippy/master/index.html#match_wildcard_for_single_variants) | |
| [`mismatching_type_param_order`](https://rust-lang.github.io/rust-clippy/master/index.html#mismatching_type_param_order) | |
| [`mut_mut`](https://rust-lang.github.io/rust-clippy/master/index.html#mut_mut) | |
| [`needless_bitwise_bool`](https://rust-lang.github.io/rust-clippy/master/index.html#needless_bitwise_bool) | |
| [`needless_continue`](https://rust-lang.github.io/rust-clippy/master/index.html#needless_continue) | |
| [`needless_for_each`](https://rust-lang.github.io/rust-clippy/master/index.html#needless_for_each) | |
| [`needless_raw_string_hashes`](https://rust-lang.github.io/rust-clippy/master/index.html#needless_raw_string_hashes) | |
| [`no_effect_underscore_binding`](https://rust-lang.github.io/rust-clippy/master/index.html#no_effect_underscore_binding) | |
| [`no_mangle_with_rust_abi`](https://rust-lang.github.io/rust-clippy/master/index.html#no_mangle_with_rust_abi) | Rust ABI is not stable, should be used with `extern "C"` |
| [`option_as_ref_cloned`](https://rust-lang.github.io/rust-clippy/master/index.html#option_as_ref_cloned) | |
| [`option_option`](https://rust-lang.github.io/rust-clippy/master/index.html#option_option) | |
| [`ptr_as_ptr`](https://rust-lang.github.io/rust-clippy/master/index.html#ptr_as_ptr) | Explicitness, safety |
| [`ptr_cast_constness`](https://rust-lang.github.io/rust-clippy/master/index.html#ptr_cast_constness) | Explicitness, safety |
| [`pub_underscore_fields`](https://rust-lang.github.io/rust-clippy/master/index.html#pub_underscore_fields) | |
| [`redundant_closure_for_method_calls`](https://rust-lang.github.io/rust-clippy/master/index.html#redundant_closure_for_method_calls) | |
| [`ref_as_ptr`](https://rust-lang.github.io/rust-clippy/master/index.html#ref_as_ptr) | Explicitness, safety |
| [`ref_option_ref`](https://rust-lang.github.io/rust-clippy/master/index.html#ref_option_ref) | `Option<&T>` over `&Option<T>` |
| [`same_functions_in_if_condition`](https://rust-lang.github.io/rust-clippy/master/index.html#same_functions_in_if_condition) | |
| [`semicolon_if_nothing_returned`](https://rust-lang.github.io/rust-clippy/master/index.html#semicolon_if_nothing_returned) | |
| [`trivially_copy_pass_by_ref`](https://rust-lang.github.io/rust-clippy/master/index.html#trivially_copy_pass_by_ref) | Behavior desired more often than not |
| [`uninlined_format_args`](https://rust-lang.github.io/rust-clippy/master/index.html#uninlined_format_args) | `format!("{}", a)` -> `format!("{a}")` |
| [`unnecessary_join`](https://rust-lang.github.io/rust-clippy/master/index.html#unnecessary_join) | |
| [`unnested_or_patterns`](https://rust-lang.github.io/rust-clippy/master/index.html#unnested_or_patterns) | |
| [`unused_async`](https://rust-lang.github.io/rust-clippy/master/index.html#unused_async) | |
| [`unused_self`](https://rust-lang.github.io/rust-clippy/master/index.html#unused_self) | |
| [`used_underscore_binding`](https://rust-lang.github.io/rust-clippy/master/index.html#used_underscore_binding) | |
| [`zero_sized_map_values`](https://rust-lang.github.io/rust-clippy/master/index.html#zero_sized_map_values) | |
| [`as_ptr_cast_mut`](https://rust-lang.github.io/rust-clippy/master/index.html#as_ptr_cast_mut) | |
| [`clear_with_drain `](https://rust-lang.github.io/rust-clippy/master/index.html#clear_with_drain ) | |
| [`collection_is_never_read`](https://rust-lang.github.io/rust-clippy/master/index.html#collection_is_never_read) | |
| [`debug_assert_with_mut_call`](https://rust-lang.github.io/rust-clippy/master/index.html#debug_assert_with_mut_call) | |
| [`derive_partial_eq_without_eq`](https://rust-lang.github.io/rust-clippy/master/index.html#derive_partial_eq_without_eq) | |
| [`empty_line_after_doc_comments`](https://rust-lang.github.io/rust-clippy/master/index.html#empty_line_after_doc_comments) | |
| [`empty_line_after_outer_attr`](https://rust-lang.github.io/rust-clippy/master/index.html#empty_line_after_outer_attr) | |
| [`equatable_if_let`](https://rust-lang.github.io/rust-clippy/master/index.html#equatable_if_let) | |
| [`iter_on_empty_collections`](https://rust-lang.github.io/rust-clippy/master/index.html#iter_on_empty_collections) | |
| [`iter_on_single_items`](https://rust-lang.github.io/rust-clippy/master/index.html#iter_on_single_items) | |
| [`iter_with_drain`](https://rust-lang.github.io/rust-clippy/master/index.html#iter_with_drain) | |
| [`needless_collect`](https://rust-lang.github.io/rust-clippy/master/index.html#needless_collect) | |
| [`needless_pass_by_ref_mut`](https://rust-lang.github.io/rust-clippy/master/index.html#needless_pass_by_ref_mut) | |
| [`negative_feature_names`](https://rust-lang.github.io/rust-clippy/master/index.html#negative_feature_names) | Features should be additive |
| [`non_send_fields_in_send_ty`](https://rust-lang.github.io/rust-clippy/master/index.html#non_send_fields_in_send_ty) | Safety |
| [`nonstandard_macro_braces`](https://rust-lang.github.io/rust-clippy/master/index.html#nonstandard_macro_braces) | |
| [`path_buf_push_overwrite`](https://rust-lang.github.io/rust-clippy/master/index.html#path_buf_push_overwrite) | |
| [`read_zero_byte_vec`](https://rust-lang.github.io/rust-clippy/master/index.html#read_zero_byte_vec) | |
| [`redundant_clone`](https://rust-lang.github.io/rust-clippy/master/index.html#redundant_clone) | |
| [`redundant_feature_names`](https://rust-lang.github.io/rust-clippy/master/index.html#redundant_feature_names) | |
| [`trailing_empty_array`](https://rust-lang.github.io/rust-clippy/master/index.html#trailing_empty_array) | |
| [`trait_duplication_in_bounds`](https://rust-lang.github.io/rust-clippy/master/index.html#trait_duplication_in_bounds) | |
| [`type_repetition_in_bounds`](https://rust-lang.github.io/rust-clippy/master/index.html#type_repetition_in_bounds) | |
| [`uninhabited_references`](https://rust-lang.github.io/rust-clippy/master/index.html#uninhabited_references) | |
| [`unnecessary_struct_initialization`](https://rust-lang.github.io/rust-clippy/master/index.html#unnecessary_struct_initialization) | |
| [`unused_peekable`](https://rust-lang.github.io/rust-clippy/master/index.html#unused_peekable) | |
| [`unused_rounding`](https://rust-lang.github.io/rust-clippy/master/index.html#unused_rounding) | |
| [`use_self`](https://rust-lang.github.io/rust-clippy/master/index.html#use_self) | `impl Foo { fn new() -> Foo }` -> `impl Foo { fn new() -> Self }` |
| [`useless_let_if_seq`](https://rust-lang.github.io/rust-clippy/master/index.html#useless_let_if_seq) | |
| [`wildcard_dependencies`](https://rust-lang.github.io/rust-clippy/master/index.html#wildcard_dependencies) | All dependencies should have a specified version |
| [`absolute_paths_not_starting_with_crate`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#absolute-paths-not-starting-with-crate) | |
| [`explicit_outlives_requirements`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#explicit-outlives-requirements) | Legacy |
| [`keyword_idents`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#keyword-idents) | |
| [`missing_abi`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#missing-abi) | Explicitness |
| [`non_ascii_idents`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#non-ascii-idents) | |
| [`non_local_definitions`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#non-local-definitions) | `It may become deny-by-default in edition 2024 and higher, see the tracking issue https://github.com/rust-lang/rust/issues/120363.` |
| [`single_use_lifetimes`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#single-use-lifetimes) | `impl Struct<'a>` -> `impl Struct<'_>` |
| [`trivial_casts`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#trivial-casts) | |
| [`trivial_numeric_casts`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#trivial-numeric-casts) | |
| [`unsafe_op_in_unsafe_fn`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unsafe-op-in-unsafe-fn) | `This lint is "allow" by default on editions up to 2021, from 2024 it is "warn" by default` |
| [`unused_crate_dependencies`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unused-crate-dependencies) | |
| [`unused_import_braces`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unused-import-braces) | |
| [`unused_lifetimes`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unused-lifetimes) | |
| [`unused_macro_rules`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unused-macro-rules) | |
| [`ambiguous_glob_imports`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#ambiguous-glob-imports) | |
| [`infinite_loop`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#infinite_loop) | Infinite loops should be marked with `!` |
| [`redundant_type_annotations`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#redundant_type_annotations) | |
| [`rest_pat_in_fully_bound_structs`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#rest_pat_in_fully_bound_structs) | |
| [`unseparated_literal_suffix`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unseparated_literal_suffix) | `123i32` -> `123_i32` |
| [`string_to_string`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#string_to_string) | |
| [`tests_outside_test_module`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#tests_outside_test_module) | Tests should be in `#[cfg(test)] mod tests {}` |
| [`unnecessary_safety_comment`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unnecessary_safety_comment) | `// SAFETY` comments should only be above `unsafe` blocks |
| [`unnecessary_safety_doc`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unnecessary_safety_doc) | `# Safety` docs should only be on `unsafe` items |
| [`unnecessary_self_imports`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unnecessary_self_imports) | `use std::io::{self};` -> `use std::io;` |
| [`unused_unsafe`](https://doc.rust-lang.org/rustc/lints/listing/warn-by-default.html#unused-unsafe) | Blocks that don't need `unsafe` should not use the keyword |

## Lints (warm)
| Lint | Reasoning |
|------|-----------|
| [`cast_possible_truncation`](https://rust-lang.github.io/rust-clippy/master/index.html#cast_possible_truncation) | May happen more often than not on accident |
| [`cast_possible_wrap`](https://rust-lang.github.io/rust-clippy/master/index.html#cast_possible_wrap) |  May happen more often than not on accident |
| [`cast_precision_loss`](https://rust-lang.github.io/rust-clippy/master/index.html#cast_precision_loss) |  May happen more often than not on accident |
| [`cast_sign_loss`](https://rust-lang.github.io/rust-clippy/master/index.html#cast_sign_loss) | May happen more often than not on accident |
| [`copy_iterator`](https://rust-lang.github.io/rust-clippy/master/index.html#copy_iterator) | An `Iterator` being `Copy` is a bit confusing since it usually has consume semantics |
| [`doc_markdown`](https://rust-lang.github.io/rust-clippy/master/index.html#doc_markdown) | Makes documentation more readable but does _sometimes_ have false positives |
| [`explicit_deref_methods`](https://rust-lang.github.io/rust-clippy/master/index.html#explicit_deref_methods) | `.deref()` is less pretty but more clear than `*` sometimes |
| [`explicit_iter_loop`](https://rust-lang.github.io/rust-clippy/master/index.html#explicit_iter_loop) | Style
| [`float_cmp`](https://rust-lang.github.io/rust-clippy/master/index.html#float_cmp) | More precise but exact float precision may not be required |
| [`fn_params_excessive_bools`](https://rust-lang.github.io/rust-clippy/master/index.html#fn_params_excessive_bools) | Cleaner, more work for fn writers |
| [`into_iter_without_iter`](https://rust-lang.github.io/rust-clippy/master/index.html#into_iter_without_iter) | More idiomatic public API |
| [`iter_without_into_iter`](https://rust-lang.github.io/rust-clippy/master/index.html#iter_without_into_iter) | More idiomatic public API |
| [`iter_not_returning_iterator`](https://rust-lang.github.io/rust-clippy/master/index.html#iter_not_returning_iterator) | `.iter()` should return an `impl Iterator` |
| [`large_digit_groups`](https://rust-lang.github.io/rust-clippy/master/index.html#large_digit_groups) | Style |
| [`large_types_passed_by_value`](https://rust-lang.github.io/rust-clippy/master/index.html#large_types_passed_by_value) | May be desired behavior sometimes |
| [`manual_assert`](https://rust-lang.github.io/rust-clippy/master/index.html#manual_assert) | Style, but may be less clear sometimes |
| [`maybe_infinite_iter`](https://rust-lang.github.io/rust-clippy/master/index.html#maybe_infinite_iter) | Style, but may be less clear sometimes |
| [`missing_fields_in_debug `](https://rust-lang.github.io/rust-clippy/master/index.html#missing_fields_in_debug ) | May be desired behavior sometimes |
| [`needless_pass_by_value`](https://rust-lang.github.io/rust-clippy/master/index.html#needless_pass_by_value) | May be desired behavior sometimes |
| [`range_minus_one`](https://rust-lang.github.io/rust-clippy/master/index.html#range_minus_one) | Has issues depending on range type, may be less clear than `end - 1` |
| [`range_plus_one`](https://rust-lang.github.io/rust-clippy/master/index.html#range_plus_one) | Has issues depending on range type, may be less clear than `end + 1` |
| [`redundant_else`](https://rust-lang.github.io/rust-clippy/master/index.html#redundant_else) | Less indentation but may be less clear on short `if` blocks |
| [`ref_binding_to_reference`](https://rust-lang.github.io/rust-clippy/master/index.html#ref_binding_to_reference) | Style, `&` better than `ref`? |
| [`return_self_not_must_use`](https://rust-lang.github.io/rust-clippy/master/index.html#return_self_not_must_use) | Makes sure builder types are built |
| [`single_match_else`](https://rust-lang.github.io/rust-clippy/master/index.html#single_match_else) | Style |
| [`string_add_assign`](https://rust-lang.github.io/rust-clippy/master/index.html#string_add_assign) | Style |
| [`transmute_ptr_to_ptr`](https://rust-lang.github.io/rust-clippy/master/index.html#transmute_ptr_to_ptr ) | The `unsafe` section doing this should be explicitly marked with `#[allow]` |
| [`unchecked_duration_subtraction`](https://rust-lang.github.io/rust-clippy/master/index.html#unchecked_duration_subtraction) | |
| [`unnecessary_box_returns`](https://rust-lang.github.io/rust-clippy/master/index.html#unnecessary_box_returns) | May have false positives |
| [`unnecessary_wraps`](https://rust-lang.github.io/rust-clippy/master/index.html#unnecessary_wraps) | Desired behavior sometimes |
| [`branches_sharing_code`](https://rust-lang.github.io/rust-clippy/master/index.html#branches_sharing_code) | Doesn't check in-branch side-effects |
| [`fallible_impl_from`](https://rust-lang.github.io/rust-clippy/master/index.html#fallible_impl_from) | `From` should usually not be fallible |
| [`missing_const_for_fn`](https://rust-lang.github.io/rust-clippy/master/index.html#missing_const_for_fn) | Correct most of the time although does mean removing `const` will be a breaking API change |
| [`significant_drop_in_scrutinee`](https://rust-lang.github.io/rust-clippy/master/index.html#significant_drop_in_scrutinee) | Useful but many cases where it's okay |
| [`significant_drop_tightening`](https://rust-lang.github.io/rust-clippy/master/index.html#significant_drop_tightening) | Useful but many cases where it's okay |
| [`let_underscore_drop`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#let-underscore-drop) | Helps release resources faster but has false positives |
| [`unreachable_pub`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unreachable-pub) | Forces non-public APIs to be marked `pub(_)` instead of `pub` |
| [`unused_qualifications`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#unused_qualifications) | Using fully qualified names even when in scope may be desired sometimes |
| [`variant_size_differences`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#variant-size-differences) | `enum` variants shouldn't differ in size greatly |
| [`clone_on_ref_ptr`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#clone_on_ref_ptr) | Style, `Arc::clone(&arc)` over `arc.clone()` |
| [`empty_drop`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#empty_drop) | |
| [`empty_enum_variants_with_brackets`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#empty_enum_variants_with_brackets) | Style |
| [`empty_structs_with_brackets`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#empty_structs_with_brackets) | Style |
| [`error_impl_error`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#error_impl_error) | |
| [`get_unwrap`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#get_unwrap) | `x.get(0).unwrap()` -> `x.[0]` |
| [`impl_trait_in_params`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#impl_trait_in_params) | Turbofish (`::<>`) is a superset of `impl Trait`, which allows the user naming the type |
| [`iter_over_hash_type`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#iter_over_hash_type) | Hash types iteration is unordered, may not matter in some cases though |
| [`let_underscore_must_use`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#let_underscore_must_use) | `#[must_use]` types should usually not be ignored with `let _ =` |
| [`lossy_float_literal`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#lossy_float_literal) | Prevents float literals that will not be precise |
| [`try_err`](https://doc.rust-lang.org/rustc/lints/listing/allowed-by-default.html#try_err) | `Err(e)?` -> `return Err(e)` |


## Lints (hot)
| Lint | Reasoning |
|------|-----------|
| [`inline_always`](https://rust-lang.github.io/rust-clippy/master/index.html#inline_always) | Causes more problems than not, must be remembered to be updated alongside code changes. Should be considered if time is actively spent measuring and maintaining inline behavior (i.e. we have no time to maintain this). |
| [`large_futures`](https://rust-lang.github.io/rust-clippy/master/index.html#large_futures) | Prevent stack overflows |
| [`large_stack_arrays`](https://rust-lang.github.io/rust-clippy/master/index.html#large_stack_arrays) | Prevent stack overflows |
| [`linkedlist`](https://rust-lang.github.io/rust-clippy/master/index.html#linkedlist) | |
| [`missing_errors_doc`](https://rust-lang.github.io/rust-clippy/master/index.html#missing_errors_doc) | Public functions should declare to users how/why/when they error |
| [`missing_panics_doc`](https://rust-lang.github.io/rust-clippy/master/index.html#missing_panics_doc) | Same as above, but slightly more burdensome as some functions only panic on un-anticipated errors, `#[allow]` must be used here |
| [`should_panic_without_expect`](https://rust-lang.github.io/rust-clippy/master/index.html#should_panic_without_expect) | Assert panics messages are as expected  |
| [`similar_names`](https://rust-lang.github.io/rust-clippy/master/index.html#similar_names) | Readability, many false positives |
| [`too_many_lines`](https://rust-lang.github.io/rust-clippy/master/index.html#too_many_lines) | Prevents monster functions, but starts at a very small limit (100 LoC), can be raised |
| [`unreadable_literal`](https://rust-lang.github.io/rust-clippy/master/index.html#unreadable_literal) | `123456789` might be desired more often for copy+paste purposes rather than the readability of `123_456_789` |
| [`wildcard_imports`](https://rust-lang.github.io/rust-clippy/master/index.html#wildcard_imports) | Explicitness, at the cost of things like `rayon::prelude::*` not being allowed |
| [`missing_copy_implementations`](https://rust-lang.github.io/rust-clippy/master/index.html#missing-copy-implementations) | Types that can implement `Copy` usually should, but not always |
| [`missing_docs`](https://rust-lang.github.io/rust-clippy/master/index.html#missing-docs) | Public APIs should be documented |
| [`non_exhaustive_omitted_patterns`](https://rust-lang.github.io/rust-clippy/master/index.html#non-exhaustive-omitted-patterns) | Makes sure `#[non_exhaustive]` enums are at least handled in some manner |
| [`unused_results`](https://rust-lang.github.io/rust-clippy/master/index.html#unused-results) | `Result` should be handled (even if it means `unwrap/expect` or `let _ =`) |
| [`allow_attributes_without_reason`](https://rust-lang.github.io/rust-clippy/master/index.html#allow_attributes_without_reason ) | If something is `#[allow]`ed, it should be documented why with `#[allow(lint, reason = "reason")]` |
| [`missing_assert_message`](https://rust-lang.github.io/rust-clippy/master/index.html#missing_assert_message) | Assertions should document why they failed |
| [`missing_docs_in_private_items`](https://rust-lang.github.io/rust-clippy/master/index.html#missing_docs_in_private_items) | Makes sure internal items are documented as well |
| [`undocumented_unsafe_blocks`](https://rust-lang.github.io/rust-clippy/master/index.html#undocumented_unsafe_blocks) | All `unsafe` blocks should have a `// SAFETY: comment explaining why they are safe` |
| [`multiple_unsafe_ops_per_block`](https://rust-lang.github.io/rust-clippy/master/index.html#multiple_unsafe_ops_per_block) | `Combined with undocumented_unsafe_blocks, this lint ensures that each unsafe operation must be independently justified. Combined with unused_unsafe, this lint also ensures elimination of unnecessary unsafe blocks through refactoring.` |
| [`single_char_lifetime_names`](https://rust-lang.github.io/rust-clippy/master/index.html#single_char_lifetime_names) | Lifetimes should describe what they are, like variables |
| [`wildcard_enum_match_arm`](https://rust-lang.github.io/rust-clippy/master/index.html#wildcard_enum_match_arm) | All `enum` variants should be explicitly handled |

## Lints allowed for `#[cfg(any(test, debug_assertions))]`
Lints that are too annoying for testing/debugging can be `#[allow]`ed.

TODO: add lints

## Lints enabled for release builds
These lints may make sense to enable for release builds.

| Lint | Reasoning |
|------|-----------|
| [`print_stderr`](https://rust-lang.github.io/rust-clippy/master/index.html#print_stderr) | Catches debug prints |
| [`print_stdout`](https://rust-lang.github.io/rust-clippy/master/index.html#print_stdout) | Catches debug prints |
| [`todo`](https://rust-lang.github.io/rust-clippy/master/index.html#todo) | Catches `todo!()` |
| [`unimplemented`](https://rust-lang.github.io/rust-clippy/master/index.html#unimplemented) | Catches `unimplemented!()` |

# Discussion History
# Action History
- Created by: hinto-janai | 2024-05-20T22:59:48+00:00
