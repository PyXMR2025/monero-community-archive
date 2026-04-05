---
title: RPC design proposal
source_url: https://github.com/Cuprate/cuprate/issues/106
author: yamabiiko
assignees: []
labels:
- C-proposal
- A-rpc
created_at: '2024-04-08T09:01:16+00:00'
updated_at: '2024-06-05T14:35:09+00:00'
type: issue
status: closed
closed_at: '2024-06-05T14:35:09+00:00'
---

# Original Description
This issue is meant to initiate a discussion on the high-level design of Cuprate's daemon RPC.
The main focus is on defining the interface and  handling parsing methods/params and responses, so I abstracted away all interactions with other Cuprate's parts for now and the actual daemon.

## Overview

[Monerod's daemon RPC](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html)  has three kinds of RPC calls: 

- JSON RPC methods, called at the endpoint `/json_rpc`
- general RPC methods called at their own endpoints (eg. `/get_height`)
- binary (epee format) RPC methods called at their own endpoints ending in .bin (eg.`/get_blocks.bin`)

Given the above it seems natural to split the daemon into three different Services / Layers.

![cuprate](https://github.com/Cuprate/cuprate/assets/30393429/e6204778-a16a-4beb-96ca-b5c09f623dbf)


## (Core) RPC Service
This is the actual service responsible for calling the methods (and interfacing with the necessary Cuprate crates such as the db), it implements `Service<Rpc>` and returns a `method::Response`. 
enum/struct example:
```rust
pub enum Rpc {
    TestMethod(crate::param::TestMethod),
    ...
}
// crate::param
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct TestMethod {
    number: u8,
}

epee_object!(
    TestMethod,
    number: u8,
);
```
```rust
//method::Response
#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
struct BaseResponse {
    credits: u64,
    status: String,
    top_hash: String,
    untrusted: bool,
}

epee_object!(
    BaseResponse,
    credits: u64,
    status: String,
    top_hash: String,
    untrusted: bool,
);

#[derive(Clone, Serialize, Deserialize)]
pub enum Response {
    TestMethod(TestResponse)
}

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct TestResponse {
    base: BaseResponse,
    pub test: u8
}

epee_object!(
    TestResponse,
    base: BaseResponse,
    test: u8,
);
```
## Middleware Service
This service is mainly responsible for parsing the parameters of the RPC call so that we can construct the struct related to the specific RPC method and deserializing the response into the proper type (`Value`, `JsonResponse`, `Bytes` in epee format).
Errors regarding method name and parameters are caught and handled before calling the core service.
It has different implementations based on the RPC call type, specifically ` JsonRequest` and `RpcRequest<Bytes>`, `RpcRequest<RawValue>`, where `RpcRequest` is a struct  with the given method by the URI and  the given params, so something like
```rust
pub struct RpcRequest<'a, T> {
    pub method: Cow<'a, str>,
    pub params: T
}
```
Macro example for JSON RPC:
```rust
macro_rules! call_json_rpc {

    ($method:ident, $request:expr, $self:expr, $param:ty) => {{
        let id = $request.id.map(|id| id.into_owned());

        let Some(Ok(param)) = $request.params
            .map(|params| serde_json::from_str::<$param>(params.get())) else {
            return async move { Ok(JsonResponse::invalid_params(id)) }.boxed()
        };

        async move {
            let result = $self.core_rpc.call(crate::method::Rpc::$method(param)).await;
            if let Ok(result) = result {
                let result = serde_json::to_value(&result).unwrap();
                return Ok(JsonResponse::result(Cow::Owned(result), id))
            } else {
                return Ok(JsonResponse::invalid_params(id))
            }
        }.boxed()
    }};
}
```
## HTTP Service
This `hyper::service` (as the name suggests) is responsible for handling all the HTTP related things.
It will parse the body, match the URI so that it knows which Middleware service to call and it wraps the result of those to the body of the hyper::response.





# Discussion History
## SyntheticBird45 | 2024-04-08T11:26:17+00:00
I would like to add that some methods in `/json_rpc` endpoint does return epee binary responses, or a mix of json response with some of its field containing raw binary. There are only `txpool_backlog` and `get_output_histogram` iirc.

## Boog900 | 2024-04-25T18:55:44+00:00
Thanks for this and sorry for not commenting sooner.

I like the overall design, I have some comments though.

I think it might be a good idea to use [axum](https://docs.rs/axum/latest/axum/), it seems like it would cleanly fit into this design. I would also recommend keeping the `(Core) RPC Service` abstract i.e. just leaving it as a service that needs to be provided to the RPC module and this service's types probably shouldn't exactly match the RPC requests(s), this might have been what you meant in the design just wanted to explicitly say it.

> I would like to add that some methods in /json_rpc endpoint does return epee binary responses, or a mix of json response with some of its field containing raw binary. There are only txpool_backlog and get_output_histogram iirc.

This is not great, IIRC json5 supports this so we may need to use a json5 serde lib for these types 

## Boog900 | 2024-05-06T00:47:46+00:00
Adding some more details about my ideas:

The "inner-request handler" is a Service that gives the actual responses for requests, I think this should be passed into the RPC crate and not defined in it. 

The RPC crate would define all the RPC types, the axum handlers, etc. It would handle all of the RPC protocol, setting limits, disallowing certain requests in restricted mode and calling the inner request handler.

Doing this would allow reusing the actual RPC server with different internal handlers, Cuprate being the main target but potentially we could build a top block cacher like discussed in our first meeting.

 The inner handler should not be responsible for anything except turning requests into responses, this isn't to say it can't do anything more, like load shedding, just that it should not be relied upon in the RPC crate.
 
 Practically this means when a request comes in, the handler for that request (we would have a handler per endpoint, for example "/json_rpc") would check the request is allowed, size or if restricted, then it would pass it to the inner request handler to return the response.
 
 The RPC crate shouldn't start the server instead it should expose a [Router](https://docs.rs/axum/0.7.5/axum/struct.Router.html) which users would start. The exposed router would be something like `Router<State>` which `State` being roughly:
 
 ```rust
 #[derive(Clone)]
 struct State<S> {
     /// A bool for if this server a restricted RPC server.
     restricted: bool,
     /// The inner handler.
     inner_handler: S
 }
 ```
 
 Setting a type of `State` means users have to provide it: https://docs.rs/axum/0.7.5/axum/struct.Router.html#what-s-in-routers-means
 
 Returning the router allows user to set middleware on the server as well, allowing finer control for different use cases.
 
 For binary requests we would impl [FromRequest]( https://docs.rs/axum/0.7.5/axum/extract/trait.FromRequest.html) using our epee_encoding crate. Also keep in mind axum sets a [default size limit](https://docs.rs/axum/0.7.5/axum/extract/index.html#request-body-limits)



## hinto-janai | 2024-05-24T16:46:34+00:00
> The "inner-request handler" is a Service [...] we would have a handler per endpoint

How did you want to do this? It would get a bit unwieldy since there are many ['other' endpoints](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#other-daemon-rpc-calls). Would a trait object that represents a type that contains all the handlers work here? Similar to `cuprate_database`'s `impl Tables` object:

```rust
pub trait EndpointHandler {
    fn json(&self) -> &impl Service<JsonRpcRequest>;
    fn bin(&self) -> &impl Service<BinaryRpcRequest>;
    fn get_height(&self) -> &impl Service<()>;
    // ...and all 'other' RPC methods
}
```
where-then the user of this RPC interface lib passes their handlers along with any custom state and retrieves a corresponding `Router`:
```rust
// the one big state object passed to the `Router`
pub struct RpcServerState<S: /* some custom state? */, H: EndpointHandler> {
    pub state: S, // config that sets limits, etc?
    pub restricted: bool,
    pub handlers: H,
}

pub fn create_router<S, H>(state: RpcServerState<S, H>) -> Router<Arc<RpcServerState<S, H>>> {
    let state = Arc::new(state); // could box leak
    Router::new()
        .route(
            "/json_rpc",
            get({
                let state = state.clone();
                move |request| route_json_rpc(request, state)
            }),
        )
        .route(
            "/*bin",
            get({
                let state = state.clone();
                move |request| route_binary_rpc(request, state)
            }),
        )
        .route(
            "/get_height",
            get({
                let state = state.clone();
                move |request| route_get_height(request, state)
            }),
        ) // ...and all 'other' RPC methods
}
```

> would check the request is allowed, size or if restricted, then it would pass it to the inner request handler to return the response

like so?:
```rust
#[derive(Deserialize)]
struct JsonRpcRequest {/* ... */}
#[derive(Deserialize)]
struct JsonRpcResponse {/* ... */}

async fn route_json_rpc<S, H>(
    Json(request): Json<JsonRpcRequest>,
    state: Arc<RpcServerState<S, H>>
) -> Result<Json<JsonRpcResponse>, StatusCode> // matches the `Service` response type
{
    /* do checks */

    self.handlers.json().call(/*...*/).await
}
```

## Boog900 | 2024-05-24T20:35:47+00:00
> How did you want to do this? It would get a bit unwieldy since there are many ['other' endpoints](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#other-daemon-rpc-calls). Would a trait object that represents a type that contains all the handlers work here? Similar to cuprate_database's impl Tables object:

By handler I meant [axum handlers](https://docs.rs/axum/0.7.5/axum/index.html#handlers), not separate inner request handlers. I think there should only be 1 inner request handler.

---

> where-then the user of this RPC interface lib passes their handlers along with any custom state and retrieves a corresponding Router

I think we should use the [State extractor](https://docs.rs/axum/0.7.5/axum/index.html#using-the-state-extractor) which means it would look something like:

```rust
// the one big state object passed to the `Router`
pub struct RpcServerState<S: /* some custom state? */, H> {
    pub state: S, // config that sets limits, etc?
    pub restricted: bool,
    pub handler: H,
}

// Returning a `Router<S>` means the user has to provide `S`
pub fn create_router<S, H>() -> Router<RpcServerState<S, H>> {
    Router::new()
        .route(
            "/json_rpc",
            get(route_json_rpc),
        )
        .route(
            "/*bin",
            get(route_binary_rpc),
        )
        .route(
            "/get_height",
            get(route_get_height),
        ) // ...and all 'other' RPC methods
}
```
And then users have to do something like: 

```rust
let state = RpcServerState::new();

let router = create_router().with_state(state);
```

Things to note:
- create_router returns a `Router<S>` so the users have to provide the `S` and we don't take it in.
- RpcServerState is not wrapped in an `Arc` as the inner request service should be clone (need `&mut` access)
- The handlers given to the `route` functions (`route_json_rpc`, etc)[must declare the app state type first](https://docs.rs/axum/0.7.5/axum/extract/index.html#the-order-of-extractors)

--- 

> like so?:

Pretty much but you may need to do mappings on the response type for json/ binary with just 1 inner request handler, unless we require all types be serde + epee encode-able which I would be ok with.

Also the previous thing about argument order.

## hinto-janai | 2024-05-27T20:25:52+00:00
> you may need to do mappings on the response type for json/ binary with just 1 inner request handler

The interface and user's request/response types must agree, would the library itself define `Response/Request` and require the user's handler to implement `Service` using those types?

```rust
//--- code inside the cuprate RPC interface lib

enum Request {
    Json(JsonRequestEnum),
    Bin(BinRequestEnum),
    Other(OtherRequestEnum),
}

enum Response {
    Json(JsonResponseEnum),
    Bin(BinResponseEnum),
    Other(OtherResponseEnum),
}

enum Error {/*...*/}

pub fn create_router<S, H>() -> Router<RpcServerState<S, H>>
where
    H: tower::Service<Request>,
    H: <H as Service>::Response: Into<Response>,
    H: <H as Service>::Error: Into<Error>,
{/*...*/}
```

> By handler I meant [axum handlers](https://docs.rs/axum/0.7.5/axum/index.html#handlers), not separate inner request handlers. I think there should only be 1 inner request handler.

Ah, I think I see, the single handler is a `tower::Service` with request/response's enums that can handle all routes?:
```rust
//--- code inside the cuprate RPC interface lib

async fn route_json_rpc<S, H>(
    state: Arc<RpcServerState<S, H>>
    Json(request): Json<JsonRpcRequest>,
) -> Result<Json<JsonResponse>, Error>
{
    /* do checks */

    // this `tower::Service` is provided by the user, not us
    let Response::Json(resp) = self.handler.call(/*...*/).await? else {
        panic!("bad resp from server"); // or return err
    };

    Ok(Json(resp))
}

```
```rust
//--- code outside of the cuprate RPC interface lib, provided by the user

struct RpcHandler {/*...*/}

impl Service for RpcHandler {
    /*...*/

    fn call(/*...*/, request: Request) -> Result<Response, /*...*/> {
        match req {
            Request::Json(json_req) => match json_req {
                JsonRequest::GetInfo => /* handler function defined somewhere */,
                JsonRequest::GetBlock => /*...*/,
                /* handle all json calls */
            },
            Request::Bin(bin_req) => match bin_req {
                BinRequest::GetBlocks => /*...*/
                /* handle all binary calls */
            },
            Request::Other(other_req) => match other_req {
                OtherRequest::GetHeight => /*...*/
                /* handle all other calls */
            },
        },
    }
}
```

## Boog900 | 2024-05-31T00:03:50+00:00
> The interface and user's request/response types must agree, would the library itself define Response/Request and require the user's handler to implement Service using those types?

Yeah, you have split the enum into 3 for each interface but you could also just have 1 enum for all and require that all types in the enum are serde/ epee-encodeable 

I don't really mind either way.


> Ah, I think I see, the single handler is a tower::Service with request/response's enums that can handle all routes?:

Yes




 

# Action History
- Created by: yamabiiko | 2024-04-08T09:01:16+00:00
- Closed at: 2024-06-05T14:35:09+00:00
