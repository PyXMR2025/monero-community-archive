---
title: Monero OpenRPC Specification
source_url: https://github.com/monero-project/monero/issues/9186
author: kilianmh
assignees: []
labels:
- question
- low priority
- proposal
- documentation
- discussion
created_at: '2024-02-20T06:54:11+00:00'
updated_at: '2024-03-16T19:29:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[OpenRPC](https://open-rpc.org/) is a (human and) machine-readable, programming language-agnostic [JSON-RPC](https://www.jsonrpc.org/) API interface description standard.

Having such a document could facilitate e.g. specification driven development, interactive documentation, code generation (documentation / clients), and automation of test cases.

Here is the [post on bounties.monero](https://bounties.monero.social/posts/104/1-000m-monero-openrpc-specification).

Do you guys think such a specification could/should be part of the of this [repository](https://github.com/monero-project/monero), another [monero-project](https://github.com/monero-project) repository, or an external repository?

# Discussion History
## SamsungGalaxyPlayer | 2024-02-20T15:57:32+00:00
@kilianmh you can use https://github.com/MAGICGrants/getmonero.dev if you want

## vtnerd | 2024-02-21T22:04:53+00:00
As an FYI, I tried to get the new serialization system I wrote to auto-generate schemas. I failed to get it working, without changing the interface a bit. Perhaps if the new serialization gets merged in (its moving very slowly), I could have some cycles on how to add this with minimal overhead (the overhead was always the problem with implementing it in the past).

For those curious, instead of writing the entire schema "by hand", this would auto-generate the initial process, with the exception of the "description" fields.

## vtnerd | 2024-02-21T22:07:22+00:00
And to clarify - I think having the schemas would be useful, but writing one for all JSON-RPC endpoints would take a while. Certainly a big effort. I'm curious what `bitcoind` does, because they seem to have nice documentation with their endpoints.

## kilianmh | 2024-02-22T04:42:07+00:00
@SamsungGalaxyPlayer getmonero.dev seems like a good option

@vtnerd 
- I'm not well versed with `c++` so auto-generation from code is out of reach for me. The schema generation should probably be handled by a third-party library. However, the `description` fields are quite important, especially if we use the schema for generating documentation. 
- For now my plan was to write it "by hand" since changes/additions to the `JSON-RPC` are not that numerous (is that true?). 
- For Bitcoin I created the [schema](https://codeberg.org/kilianmh/bitcoin-core-openrpc/src/branch/master/openrpc.json) also by hand.

One more question: Should there be a unified schema or one for`wallet-rpc` and one for `daemon-rpc`?

## vtnerd | 2024-02-22T16:36:52+00:00
We should have different schemes for `wallet-rpc` and `daemon-rpc`. The schemas don't change often, but the developers will have to be nudged to remember to update the schema when possible.

## jeffro256 | 2024-02-23T02:27:29+00:00
One of the biggest problems with the RPC documentation right now is that it is pretty outdated, and there is no mechanism to enforce that us lazy developers update the documentation (and it's in a different repo anyways). Perhaps a CI action could be added that checks `WALLET_RPC_VERSION_{MAJOR/MINOR}` and `CORE_RPC_VERSION_{MAJOR/MINOR}` against some internal version field of the corresponding OpenRPC specification. It would be nice to have a testable RPC documentation, especially for the wallet, for the upcoming Seraphis migration. 

## SyntheticBird45 | 2024-02-25T12:57:22+00:00
hi, plowsof notified me that this issue exist. Hopefully vtnerd will be able to get his serlization system working. I'm trying to write it by hand at the moment in this repo: https://github.com/SyntheticBird45/monero-open-rpc. I plan to first write the daemon rpc, test it and verify what is outdated/deprecated. I'll then jump on the wallet rpc.

## SyntheticBird45 | 2024-02-28T22:34:14+00:00
I've finished first iteration of the core RPC openRPC document: https://github.com/SyntheticBird45/monero-open-rpc/blob/main/daemon/openrpc.json. To see, copy paste it in https://playground.open-rpc.org. 

The document only contains the JSON-RPC interface and do not integrate nor document *other /rpc methods*. Since it isn't OpenAPI, there are no native way to express these endpoints. The `servers` field could be used.

For methods that could send JSON field in epee encoding format, the schema show a string, but description is precising that this is binary form.

A fair number of field description are not provided since I don't understand what are their meanings. Looking through monerod's `core_rpc_server.cpp` is time-consuming but I plan on make another trip and add more descriptions to the `components/schema` section.

I would like some directive on the *other /rpc methods* topic before jumping on the wallet RPC document

## SyntheticBird45 | 2024-02-29T22:55:38+00:00
> Perhaps a CI action could be added that checks WALLET_RPC_VERSION_{MAJOR/MINOR} and CORE_RPC_VERSION_{MAJOR/MINOR} against some internal version field of the corresponding OpenRPC specification.

Added :
```json
"x-wallet-rpc-version": {
	"major":1,
	"minor":27
}
```
to wallet/openrpc.json. and:
```json
"x-core-rpc-version": {
	"major":3,
	"minor":13
}
```
to daemon/openrpc.json

## plowsof | 2024-03-01T10:00:10+00:00
> One of the biggest problems with the RPC documentation right now is that it is pretty outdated, and there is no mechanism to enforce that us lazy developers update the documentation (and it's in a different repo anyways). Perhaps a CI action could be added that checks `WALLET_RPC_VERSION_{MAJOR/MINOR}` and `CORE_RPC_VERSION_{MAJOR/MINOR}` against some internal version field of the corresponding OpenRPC specification. It would be nice to have a testable RPC documentation, especially for the wallet, for the upcoming Seraphis migration.

I went through the RPC docs a ~year ago and updated pretty much everything.. apart from a few occurrences of ringsize:7 they are kept up to date now. Automation ofcourse is preferred, but i / others attend to any issue made on -site reg docs.

## SyntheticBird45 | 2024-03-01T11:17:27+00:00
> I went through the RPC docs a ~year ago and updated pretty much everything.

For reference, here what I found out of date in the core RPC:
- `get_connections` lacked in his response field `connections` the fields `address_type`, `rpc_credits_per_hash` and `rpc_port`
- `get_version` lacked in his response the fields `current_height` and `hard_forks` array (as well as its underlying object)
- `get_output_distribution` lacked in his parameters the field `binary` (for disabling epee encoding) and `compress` (for disabling compression)

There are also methods like `sync_info` that did not contain in their outputs the `top_hash`, `credits` or `untrusted` fields.

## kilianmh | 2024-03-01T23:06:20+00:00
@SyntheticBird45 Great to see what you did so far! 
One improvement could be to use references for recurring parameters where all fields are identical (including "description" and "required"). An example would be `fill_pow_hash`.

## kilianmh | 2024-03-01T23:13:44+00:00
One general question to the collaborators: Was/is there already an issue with the topic of replacing the _other /rpc methods_ with conforming JSON-RPC methods? If no, then do you think such an issue should be created?

## kilianmh | 2024-03-02T11:27:01+00:00
@SyntheticBird45  Also some methods use the `paramStructure` `by-position` instead of `by-name`. Examples are `on_get_block_hash`, and `submit_block`, but there might be more.

## yamabiiko | 2024-03-16T07:54:20+00:00
> One general question to the collaborators: Was/is there already an issue with the topic of replacing the _other /rpc methods_ with conforming JSON-RPC methods? If no, then do you think such an issue should be created?

I also wonder this, as I am currently working on Cuprate's RPC server and only having JSON-RPC methods would be cleaner

## jeffro256 | 2024-03-16T13:49:39+00:00
We could *add* those JSONRPC methods to match the behavior of the /* endpoints, but we shouldn't remove the /* endpoints. 

## vtnerd | 2024-03-16T19:29:52+00:00
A quick counter-argument to JSON-RPC: DOMless parsing is faster in the REST-style endpoints compared to the JSON-RPC endpoints. The problem is that the `params` field either has to be skipped then re-parsed on a second pass, OR it has to be put into a DOM (the very thing trying to be removed).

# Action History
- Created by: kilianmh | 2024-02-20T06:54:11+00:00
