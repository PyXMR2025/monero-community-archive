---
title: RPC UX and safety improvements
source_url: https://github.com/Cuprate/cuprate/issues/72
author: SyntheticBird45
assignees:
- SyntheticBird45
labels:
- C-feature
- C-proposal
- A-rpc
created_at: '2024-02-24T01:11:02+00:00'
updated_at: '2024-06-04T01:22:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What

This issue is a proposal, and discussion of three improvements related to the daemon RPC.

## Multiple credentials

### Why 

monerod supports the use of username/password authentication for its RPC, which is helpful in preventing outsiders from using the node and adding an extra layer of security. However, due to the limitation of allowing only one set of credentials at a time, it becomes necessary to share them with other users, rather than enabling each user to have their individual credentials.

The proposal is as follows:
- Cuprate will support multiple credentials
- Credentials are stored in a text-based file in an appropriate folder (See Disk Location issue)

### How

Credentials are stored in a text file using this simple layout:
```
<USERNAME>:<PASSWORD>
<USERNAME>:<PASSWORD>
<USERNAME>:<PASSWORD>
<USERNAME>:<PASSWORD>
...
```

The configuration file is read during start-up. The remainder of the implementation depends on how the original system has been developed.

Q. What is the name of the file ?

Q. Is there a maximal amount of credentials ?

Q. Should we later add an RPC method to register new credentials at runtime ?

## Whitelisted RPC

### Why

In order to safely expose a Monero node to the world, monerod implements the `--restricted-rpc` flag, which has the following effects:
- Any RPC methods containing sensitive information for the node operator and users are not served (e.g., `get_connections` returns `method not found`).
- Some response fields of available RPC methods are modified to minimize the risk of exposing sensitive information.

These restrictions are intended to protect the anonymity of users, the node operator and reduce the attack surface, as many of the restricted information is unnecessary for the protocol. Currently, the restricted RPC methods serve mostly testing and debugging purposes.

However, given that the Monero community regards the network as inherently (and rightfully) untrustworthy, nearly everyone uses the `--restricted-rpc` flag by default. As a result, unrestricted RPC methods become essentially useless in practical applications, even though they may offer valuable functionality beyond basic testing scenarios.

The actual proper way for setting up a public node with a non-restricted rpc is the following:
- Set up the public, restricted rpc at port A with `--rpc-restricted-bind-port A`
- Set up the private, non-restricted rpc at port B with `--rpc-bind-port B`
- Avoid using `--restricted-rpc`, which would otherwise restrict RPC access to port B.
- Use external software or kernel network tables to restrict connections to port B.

The UX is poorly designed, but that's okay since it wasn't the original goal.

Here's the proposal: 
- Set Cuprate RPC as restricted by default.
- Implement a whitelist system that allows specific sources to access restricted methods and original responses.
- `--whitelist-all` as an option to whitelist any incoming connection (opposite of monerod's `--restricted-rpc`)
- `--whitelist-authenticated` as an option that automatically whitelist incoming authenticated connections 

### How

#### Whitelist Service

Assuming the RPC implementation follow the same architecture as other parts of Cuprate, the use of a simple `tower::Service` is sufficient.
The structure will contains a collection of whitelisted sources and booleans for the options `--whitelist-all` and `--whitelist-authenticated`.

```rust
#[derive(Clone)]
struct WhitelistService<S: Service<Request>, C: Source + Hash> {
	inner: S,
	sources: Arc<RwLock<HashSet<C>>>, // C here can be any type we wish to use to describe a client. eg. SocketAddr
	disabled: Arc<AtomicBool>,
	allow_authenticated: Arc<AtomicBool>,
}
```

If the request is coming from a whitelisted source and respect the prior logic, `WhitelistService` will forward the request to the RPC handler with the setting `RESTRICTED: false` (see `RPC Handlers` below). If the request is not whitelisted, `WhitelistService` will forward the request to the RPC handler with the setting `RESTRICTED: true`.

#### RPC Handlers

Since the restricted mode also need responses to be modified, it seems difficult to use a second `ResponseWhitelistService<C>` that could somehow collect informations about its original request from the intercepted response. (The destination isn't always the original source, behind a json-rpc forwarder for example).

I propose to use `const` generics to solve this puzzle. The layout would be the following:

```rust
pub fn get_info_handler<const RESTRICTED: bool>(req: Request) -> Response {
	let mut resp = Response::new();
	// Do some work...

	if RESTRICTED {
		// Modify fields...
		resp
	} else {
		// No need to modify fields...
		resp
	}
}
```

For hidden methods the layout is the following:

```rust
pub fn get_connections_handler<const RESTRICTED: bool>(req: Request) -> Response {
	if RESTRICTED {
		return Response::method_dont_exist();
	}
	
	// Do the work...
}
```

This will internally create two inlined variant of the handler. It is therefore branchless in that sense.

## RPC throttling

### Why

DDoS protection is usually handled by system's administrator through external softwares. But Cuprate is meant to be used for everyone. Adding an embedded rate limiter to cuprate is simple and would add a great security and stability benefit to the node.

### How

With the use of `tower::Service`, Cuprate could benefit from crate such as `tower-governor`. Unlike a basic `tower::limit` rate limiting service, the goal isn't to act as a boilerplate for the entire service but to limit the calls from one specific client.

`tower_governor` is backed by the `governor` crate that implement the [GCRA](https://en.wikipedia.org/wiki/Generic_cell_rate_algorithm) strategy. The key being used
to identify specific clients [need the following traits](https://docs.rs/tower_governor/latest/tower_governor/key_extractor/trait.KeyExtractor.html#associatedtype.Key).

It also support the use of a global key to set a hardlimit to the number of HTTP Request the node can handle. This is similar to the `tower::limit` service in that sense but just don't implement the same algorithm under the hood.

Making use of a global boilerplate through `tower::limit` or `governor`'s global key and `tower_governor` will add a little overhead but is worth the stability guarantee

# Discussion History
# Action History
- Created by: SyntheticBird45 | 2024-02-24T01:11:02+00:00
