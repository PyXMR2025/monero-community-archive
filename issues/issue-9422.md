---
title: '[Proposal] Deprecate RPC binary strings'
source_url: https://github.com/monero-project/monero/issues/9422
author: hinto-janai
assignees: []
labels:
- proposal
- discussion
created_at: '2024-08-05T00:17:48+00:00'
updated_at: '2025-06-06T18:45:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
This is a proposal to deprecate binary string usage in `monerod`'s daemon RPC interface.

Binary strings are JSON strings that appear in `monerod`'s daemon RPC output that contain raw binary data.

There are 3 requests whose responses contain these binary strings:
- [`get_txpool_backlog`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_txpool_backlog) (`backlog` field)
- [`get_output_distribution`](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_output_distribution) (`distributions` field)
- `/get_transaction_pool_hashes.bin` (same as `/get_transaction_pool_hashes` except `tx_hashes`)

## Example
For example, the output of `get_txpool_backlog`:
```bash
curl \
    http://127.0.0.1:18081/json_rpc \
    -d '{"jsonrpc":"2.0","id":"0","method":"get_txpool_backlog"}' \
    -H 'Content-Type: application/json' \
    --output -
```
is:
```json
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "backlog": "�\r��5G\n�������\v��9E\n�������\b`k*6\n������@�8\n������S6\n������jdL\n��������~mE\n�������\b�~*A\n�������\b���\n;\n�������@��B\n�������\b@�6\n������:\r@S\t;\n��������mK\n�������N6\n������",
    "credits": 0,
    "status": "OK",
    "top_hash": "",
    "untrusted": false
  }
}
```
The `backlog` field is a JSON string containing raw binary data.

## Problem
The main problem with these binary strings is that when represented as a string, they do not always contain valid Unicode or escape characters. [This is against the JSON specification](https://datatracker.ietf.org/doc/html/rfc8259#autoid-11).

Any sane JSON parser will reject this mixed format, for example:

<details><summary>jq</summary>

```bash
# jq: parse error: Invalid escape at line 1, column 418

echo '{"backlog": "�\r��5G\n�������\v��9E\n�������\b`k*6\n������@�8\n������S6\n������jdL\n��������~mE\n�������\b�~*A\n�������\b���\n;\n�������@��B\n�������\b@�6\n������:\r@S\t;\n��������mK\n�������N6\n������"}' | jq
```

</details>

<details><summary>Python</summary>

```python
# Traceback (most recent call last):
#   File "/tmp/a/a.py", line 4, in <module>
#     json.loads(backlog)
#   File "/usr/lib/python3.12/json/__init__.py", line 346, in loads
#     return _default_decoder.decode(s)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/lib/python3.12/json/decoder.py", line 337, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/usr/lib/python3.12/json/decoder.py", line 353, in raw_decode
#     obj, end = self.scan_once(s, idx)
#                ^^^^^^^^^^^^^^^^^^^^^^
# json.decoder.JSONDecodeError: Invalid control character at: line 1 column 15 (char 14)

import json

backlog = '{"backlog": "�\r��5G\n�������\v��9E\n�������\b`k*6\n������@�8\n������S6\n������jdL\n��������~mE\n�������\b�~*A\n�������\b���\n;\n�������@��B\n�������\b@�6\n������:\r@S\t;\n��������mK\n�������N6\n������"}'
json.loads(backlog)
```

</details>

<details><summary>C++</summary>

```cpp
/// main: rapidjson/document.h:1359:
///     rapidjson::GenericValue<Encoding, Allocator>::MemberIterator
/// 	rapidjson::GenericValue<Encoding, Allocator>::FindMember(const rapidjson::GenericValue<Encoding, SourceAllocator>&)
/// 	[
/// 		with
/// 		    SourceAllocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>;
/// 			Encoding = rapidjson::UTF8<>;
/// 			Allocator = rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>;
/// 			MemberIterator = rapidjson::GenericMemberIterator<
/// 			    false,
/// 				rapidjson::UTF8<>,
/// 				rapidjson::MemoryPoolAllocator<rapidjson::CrtAllocator>
/// 			>
/// 	]: Assertion `IsObject()' failed.
///
/// Aborted (core dumped)

#include "rapidjson/document.h"

using namespace rapidjson;

int main() {
    const char* json = "{\"backlog\": \"�\r��5G\n�������\v��9E\n�������\b`k*6\n������@�8\n������S6\n������jdL\n��������~mE\n�������\b�~*A\n�������\b���\n;\n�������@��B\n�������\b@�6\n������:\
r@S\t;\n��������mK\n�������N6\n������\"}";

    Document document;
    document.Parse(json);
    document["backlog"].GetString();
}
```

</details>

<details><summary>Rust</summary>

```rust
/// thread 'main' panicked at src/main.rs:11:46:
/// called `Result::unwrap()` on an `Err` value: Error("invalid escape", line: 2, column: 54)
/// note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

#[derive(serde::Deserialize, serde::Serialize)]
struct Json {
    backlog: String,
}

const JSON: &str = r#"{"backlog": "�\r��5G\n�������\v��9E\n�������\b`k*6\n������@�8\n������S6\n������jdL\n��������~mE\n�������\b�~*A\n�������\b���\n;\n�������@��B\n�������\b@�6\n������:\r@S\t;\n��������mK\n�������N6\n������"}"#;

fn main() {
    serde_json::from_str::<Json>(JSON).unwrap();
}
```

</details>

Mixing binary and JSON in this manner means that users of these RPC calls must essentially implement a custom JSON parser themselves that can parse this format (including Monero itself).

## Replacements
I propose that Monero replaces these binary strings with one of the following options:

1. Full JSON
1. Full binary
1. Hexadecimal encoded binary within JSON

### Full JSON
RPC output that have binary strings can be replaced with regular JSON output, for example:
```json
{
  "backlog": [
    {
      "blob_size": 0,
      "fee": 0,
      "time_in_pool": 0
    }
  ]
}
```

Full JSON could be viable depending on how often these RPC call are used. It may not be if these methods are called frequently.

### Full binary
The current JSON-RPC methods can be deprecated in favor of `.bin` endpoints (e.g. `/get_txpool_backlog.bin`) that expect full binary rather than the mixed format.

It is worth noting that an un-documented [binary version of `get_output_distribution` is already used by `wallet2`](https://github.com/monero-project/monero/blob/caa62bc9ea1c5f2ffe3ffa440ad230e1de509bfd/src/wallet/wallet2.cpp#L4260), in favor of the mixed version.

### Hexadecimal encoded binary within JSON
Similar to other methods/endpoints, Monero could encode this binary information in hexadecimal before serialization instead of embedding raw binary, for example:
```json
{
  "backlog": "efbfbd...defbfbd"
}
```

## Steps
If this proposal moves forward, the steps towards completion would be:

1. Modify `monerod`'s RPC (de)serialization
1. Update any call-sites (e.g. `wallet2`)
1. Update `monero-site` documentation

# Discussion History
## kayabaNerve | 2024-08-06T00:36:04+00:00
The custom binary string is encoded how exactly? I'd guess as raw binary, yet then it'd have a 1/256 chance of being `"`, which would mark the termination of its field. Is there some custom encoding to avoid `"`, or how is it intended to detect the end of the field?

## iamamyth | 2024-08-07T00:10:17+00:00
If memory serves me, other endpoints previously had this behavior and were converted to "[h]exadecimal encoded binary within JSON". So, that should probably be done with these endpoints.

## hinto-janai | 2024-08-07T00:53:15+00:00
> The custom binary string is encoded how exactly?

For `get_txpool_backlog`, raw binary.

For `get_output_distribution`, depending on if the `binary` and `compress` flags are used:

https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2481-L2488

it'll be raw binary or [a compressed format](https://github.com/monero-project/monero/blob/caa62bc9ea1c5f2ffe3ffa440ad230e1de509bfd/src/rpc/core_rpc_server_commands_defs.h#L45-L72). If `{"binary":false}` is given as a parameter, `get_output_distribution` will output a JSON array of the bytes (not a `distribution` object), although this is [undocumented](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#get_output_distribution) and [not the default](https://github.com/monero-project/monero/blob/cc73fe71162d564ffda8e549b79a350bca53c454/src/rpc/core_rpc_server_commands_defs.h#L2462).

> 1/256 chance of being "

The bytes can be any Unicode code point (valid or not) instead of just ASCII, so I believe the chances would be much lower than this.

> how is it intended to detect the end of the field?

I can't assert how binary string deserialization works.

## iamamyth | 2024-08-07T15:29:33+00:00
> For get_output_distribution, depending on if the binary and compress flags are used:

Then it would seem `get_output_distribution` may be one of the endpoints I mentioned which was subsequently fixed: The binary flag lets all new callers request and receive valid data, but the default maintains backwards compatibility (as it should) by returning the possibly broken JSON. It might make sense to eventually eliminate the broken JSON option here by introducing a new version of the endpoint and establishing a deprecation timeline.

## j-berman | 2024-08-07T18:04:22+00:00
> I  propose that Monero replaces these binary strings with one of the following options:
> 1. Full JSON
> 2. Full binary
> 3. Hexadecimal encoded binary within JSON

How about following this model:

A new `get_txpool_backlog_v2` endpoint returns full JSON by default, and hexadecimal encoded binary within JSON if request param `as_hex` is set to true.

`get_txpool_backlog.bin` returns full binary.

`get_txpool_backlog` can be set to be deprecated on a timeline of 12 months

## hinto-janai | 2024-08-08T21:24:23+00:00
Sounds good but is there a reason to add `as_hex` alongside a binary version? I would assume most users would use the JSON version and Monero would use `.bin` internally. 

Would the same model apply to `get_output_distribution`? Make `get_output_distribution_v2` output JSON, leave the current `/get_output_distribution.bin` as is, deprecate `get_output_distribution` in 12 months?

## j-berman | 2024-08-08T22:52:33+00:00
> Sounds good but is there a reason to add `as_hex` alongside a binary version?

Agree, would seem like a nice to have if someone requests it, not a required feature, especially considering the `.bin` endpoint.

> Would the same model apply to `get_output_distribution`? Make `get_output_distribution_v2` output JSON, leave the current `/get_output_distribution.bin` as is, deprecate `get_output_distribution` in 12 months?

Seems a reasonable approach to me

## hinto-janai | 2024-11-27T14:35:27+00:00
Update: there's an draft impl in https://github.com/Cuprate/cuprate/pull/349 although after re-reading https://github.com/monero-project/meta/issues/1053 I remembered that these endpoints will be changing/deprecated with FCMP++ so Cuprate will be awaiting on changes in `monerod`.

Consensus in that meeting seemed to be in favor of something like https://github.com/monero-project/monero/issues/9422#issuecomment-2274036892.

# Action History
- Created by: hinto-janai | 2024-08-05T00:17:48+00:00
