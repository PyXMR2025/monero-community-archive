---
title: 'span.h:141:24: error: ‘is_standard_layout_v’ is not a member of ‘std’; did
  you mean ‘is_standard_layout’?'
source_url: https://github.com/monero-project/monero/issues/9572
author: l29ah
assignees: []
labels:
- reproduction needed
created_at: '2024-11-15T16:20:04+00:00'
updated_at: '2024-11-19T11:11:24+00:00'
type: issue
status: closed
closed_at: '2024-11-19T11:11:23+00:00'
---

# Original Description
I'm trying to build monero-0.18.3.4 on Gentoo Lignux and getting the following errors. It used to build well in august, so perhaps some dep updated? What could be done about this?
```
In file included from /var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/byte_slice.h:37,
                 from /var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/src/byte_slice.cpp:36:
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h: In function ‘epee::span<const unsigned char> epee::to_byte_span(span<const T>)’:
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:141:24: error: ‘is_standard_layout_v’ is not a member of ‘std’; did you mean ‘is_standard_layout’?
  141 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                        ^~~~~~~~~~~~~~~~~~~~
      |                        is_standard_layout
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:141:46: error: expected primary-expression before ‘>’ token
  141 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                                              ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:141:47: error: expected primary-expression before ‘,’ token
  141 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                                               ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:142:24: error: ‘has_unique_object_representations_v’ is not a member of ‘std’
  142 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:142:61: error: expected primary-expression before ‘>’ token
  142 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                                                             ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:142:62: error: expected primary-expression before ‘,’ token
  142 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                                                              ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h: In function ‘constexpr epee::span<unsigned char> epee::to_mut_byte_span(T&)’:
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:152:24: error: ‘is_standard_layout_v’ is not a member of ‘std’; did you mean ‘is_standard_layout’?
  152 |     static_assert(std::is_standard_layout_v<value_type>, "value type must have standard layout");
      |                        ^~~~~~~~~~~~~~~~~~~~
      |                        is_standard_layout
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:152:55: error: expected primary-expression before ‘>’ token
  152 |     static_assert(std::is_standard_layout_v<value_type>, "value type must have standard layout");
      |                                                       ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:152:56: error: expected primary-expression before ‘,’ token
  152 |     static_assert(std::is_standard_layout_v<value_type>, "value type must have standard layout");
      |                                                        ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:153:24: error: ‘has_unique_object_representations_v’ is not a member of ‘std’
  153 |     static_assert(std::has_unique_object_representations_v<value_type>, "value type must be trivially copyable with no padding");
      |                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:153:70: error: expected primary-expression before ‘>’ token
  153 |     static_assert(std::has_unique_object_representations_v<value_type>, "value type must be trivially copyable with no padding");
      |                                                                      ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:153:71: error: expected primary-expression before ‘,’ token
  153 |     static_assert(std::has_unique_object_representations_v<value_type>, "value type must be trivially copyable with no padding");
      |                                                                       ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h: In function ‘epee::span<const unsigned char> epee::as_byte_span(const T&)’:
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:162:24: error: ‘is_standard_layout_v’ is not a member of ‘std’; did you mean ‘is_standard_layout’?
  162 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                        ^~~~~~~~~~~~~~~~~~~~
      |                        is_standard_layout
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:162:46: error: expected primary-expression before ‘>’ token
  162 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                                              ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:162:47: error: expected primary-expression before ‘,’ token
  162 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                                               ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:163:24: error: ‘has_unique_object_representations_v’ is not a member of ‘std’
  163 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:163:61: error: expected primary-expression before ‘>’ token
  163 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                                                             ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:163:62: error: expected primary-expression before ‘,’ token
  163 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                                                              ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h: In function ‘epee::span<unsigned char> epee::as_mut_byte_span(T&)’:
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:172:24: error: ‘is_standard_layout_v’ is not a member of ‘std’; did you mean ‘is_standard_layout’?
  172 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                        ^~~~~~~~~~~~~~~~~~~~
      |                        is_standard_layout
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:172:46: error: expected primary-expression before ‘>’ token
  172 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                                              ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:172:47: error: expected primary-expression before ‘,’ token
  172 |     static_assert(std::is_standard_layout_v<T>, "type must have standard layout");
      |                                               ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:173:24: error: ‘has_unique_object_representations_v’ is not a member of ‘std’
  173 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:173:61: error: expected primary-expression before ‘>’ token
  173 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                                                             ^
/var/tmp/portage/net-p2p/monero-0.18.3.4-r1/work/monero-0.18.3.4/contrib/epee/include/span.h:173:62: error: expected primary-expression before ‘,’ token
  173 |     static_assert(std::has_unique_object_representations_v<T>, "type must be trivially copyable with no padding");
      |                                                              ^
```

# Discussion History
## 0xFFFC0000 | 2024-11-16T08:18:52+00:00
What is the compiler ( version ) you using?

## l29ah | 2024-11-16T12:20:07+00:00
g++ (Gentoo Hardened 13.2.1_p20240503 p15) 13.2.1 20240503

## vtnerd | 2024-11-17T18:39:08+00:00
This should be the `master` branch, I'm not seeing `_v` usage on the release branch.

## l29ah | 2024-11-17T19:33:00+00:00
> This should be the `master` branch, I'm not seeing `_v` usage on the release branch.

Yes, i have applied ed955bf751e304569cd4c04f558360154e19610e so that it would hopefully build against my boost 1.86.0. Should have mentioned it, sorry.

## vtnerd | 2024-11-19T00:12:39+00:00
#9462 is the patch you want for the 0.18 branch. This is already been applied to `release-v0.18` so you can use that (but have no tag to verify).

## l29ah | 2024-11-19T11:11:23+00:00
It built with #9462, thank you.

# Action History
- Created by: l29ah | 2024-11-15T16:20:04+00:00
- Closed at: 2024-11-19T11:11:23+00:00
