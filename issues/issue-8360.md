---
title: RPC error codes and http status codes
source_url: https://github.com/monero-project/monero/issues/8360
author: freebeego
assignees: []
labels: []
created_at: '2022-05-28T20:56:19+00:00'
updated_at: '2022-10-11T09:16:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Respond of money-wallet-rpc always have HTTP 200 OK status. Even if it responded an error.
if you use create_wallet or open_wallet methods and it has responded error it always have error code -1.

Why?
How I can figure out if a wallet doesn't exist or it has not been open?

Responses for example:

`{
    "error": {
        "code": -1,
        "message": "Unknown language: Englishs"
    },
    "id": "curltest",
    "jsonrpc": "2.0"
}`

`{
  "error": {
    "code": -1,
    "message": "Failed to open wallet"
  },
  "id": "curltest",
  "jsonrpc": "2.0"
}`

# Discussion History
## jeffro256 | 2022-05-29T02:12:55+00:00
A list of RPC error codes can be found here: https://github.com/monero-project/monero/blob/9750e1fa103539b3e533455500610aae76e253a5/src/rpc/core_rpc_server_error_codes.h#L34

error code -1 is returned for invalid parameters

What do you mean by "or it has not been open"?

## freebeego | 2022-05-29T11:20:33+00:00
Are you sure? I saw it here:
https://github.com/monero-project/monero/blob/9750e1fa103539b3e533455500610aae76e253a5/src/wallet/wallet_rpc_server_error_codes.h#L34

Why the server always returns 200 http code?
How I can understand if a wallet exists?

`{ "error": { "code": -1, "message": "Failed to open wallet" }, "id": "curltest", "jsonrpc": "2.0" }`

What does it mean? The wallet does not exist or password is wrong?

## selsta | 2022-05-29T19:19:07+00:00
I'm quite sure that the HTTP code is not the same as the return code?

Also can you show what command you are executing?

## freebeego | 2022-05-29T19:58:19+00:00
I'm quite sure that the HTTP code is not the same as the return code?
yes. there are http codes and rpc error codes(when errors happen)

but http response code is always 200 even if there is an error.
=))

## freebeego | 2022-05-29T20:05:02+00:00
Also I showed two examples of response and both of them have the error code equals to "-1" Although they are different

## selsta | 2022-05-29T21:53:06+00:00
> but http response code is always 200 even if there is an error.

https://softwareengineering.stackexchange.com/a/305294

Seeing that this is an application related error (monero-wallet-rpc being the application), I don't think using a different HTTP status code would make sense, see also this comment:

> I agree. There is nothing wrong with an application-layer error being reported in an HTTP 200 response. The 200 indicates that the HTTP request/response itself was successful, without saying anything about its content or the application-layer semantics being invoked at the time.

## selsta | 2022-05-29T22:12:52+00:00
Also again, please post the input examples, not only response.

## freebeego | 2022-05-30T11:26:39+00:00
Hi, @selsta 
Thank you so much. I think you are right. It's good approach to divide the protocol layer and the data layer.

About methods. How I can figure out if my wallet file is exist? In order to decide whether I should open it or create?
What is the store method doing? What exactly does it save?

## plowsof | 2022-05-30T20:14:18+00:00
@freebeego you will have to use some scripting such as bash / python / cpp to check if a wallet exists or not (really depends on what you are doing) for example, here i have a loop which creates a wallet and polls / waits for the existance of wallet file then continues [link](https://github.com/plowsof/flipstarter-waas-wip/blob/32cd2628a4285437eaf698e8ee52b77e948e79ef/app/setup_wallets.py#L369)
Im not exactly what store is saving, but i use it to save the restore height of the wallet file [here](https://github.com/plowsof/flipstarter-waas-wip/blob/32cd2628a4285437eaf698e8ee52b77e948e79ef/app/setup_wallets.py#L185)

# Action History
- Created by: freebeego | 2022-05-28T20:56:19+00:00
