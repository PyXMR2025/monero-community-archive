---
title: monero-wallet-rpc does not handle json_rpc parameters properly
source_url: https://github.com/monero-project/monero/issues/8612
author: llacqie
assignees: []
labels: []
created_at: '2022-10-13T10:28:06+00:00'
updated_at: '2023-01-01T10:54:31+00:00'
type: issue
status: closed
closed_at: '2023-01-01T10:54:31+00:00'
---

# Original Description
Passing an object in the array as a parameter when calling the "set_daemon" json_rpc method leads to the error "Invalid ssl support mode", which obviously should not happen. Maybe this happens with other methods, I haven't checked.

![image](https://user-images.githubusercontent.com/46074473/195573097-4ce713a5-b3ae-4f25-b4f8-0c121d90d8f3.png)
![image](https://user-images.githubusercontent.com/46074473/195573141-56ac1149-6f03-4dd6-b665-197121c8afaf.png)


# Discussion History
## plowsof | 2022-10-14T00:20:10+00:00
why are we passing empty lists/arrays? 
https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#set_daemon (username/password undocumented)

sanity check
```
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"set_daemon","params": {"address":"http://127.0.0.1:18081","trusted":true}},' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
  }
}
```

when passing an array inside a list you get an error: but not when passing a empty params list . im wondering what your issue is about?
```
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"set_daemon","params": [{}]' -H 'Content-Type: application/json'
{
  "error": {
    "code": -38,
    "message": "Invalid ssl support mode"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

empty list (all options get defaulted)
```
curl http://127.0.0.1:18082/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"set_daemon","params": {}' -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
  }
}
```

## llacqie | 2022-10-14T09:02:22+00:00
> when passing an array inside a list you get an error: but not when passing a empty params list . im wondering what your issue is about?

My issue is primarily about the fact that the error message is not true, but it would be ideal if [{}] were handled as {}, which is possible and should not entail any problems.



## plowsof | 2022-10-14T11:36:13+00:00
Don't pass it a [list] with an [{empty array}] for absolutely no reason at all. Give me a use case where you need this? 

Perhaps if you created a function that 1/10 times will handle your rpc call incorrectly and pass a [{}] on purpose (because reasons) and you need to detect when that happens? 

## llacqie | 2022-10-14T11:56:27+00:00
> Don't pass it a [list] with an [{empty array}] for absolutely no reason at all. Give me a use case where you need this?
> 
> Perhaps if you created a function that 1/10 times will handle your rpc call incorrectly and pass a [{}] on purpose (because reasons) and you need to detect when that happens?

In my case, due to the specific implementation of the json_rpc client that I used (I can't call it incorrect, it's just not obvious how to use it correctly), while testing this method, I came across this error and spent a lot of time to understand what the reason is. If the error message was correct, it would greatly speed up the work. Also, since monero-wallet-rpc does not check the correctness of the parameters format, in this case it stopped at another check, but this check might not have happened and then it might have led to more serious consequences.

## plowsof | 2022-10-14T14:21:29+00:00
RTFM , it even has examples. If an example is broken/missing please report it on monero-site 
- https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#set_daemon
- https://github.com/monero-project/monero/blob/v0.18.1.0/src/wallet/wallet_rpc_server_commands_defs.h#L2660


## selsta | 2022-10-14T14:29:30+00:00
> Also, since monero-wallet-cli does not check the correctness of the parameters format

Do you mean monero-wallet-rpc?

## llacqie | 2022-10-14T14:49:21+00:00
> RTFM , it even has examples. If an example is broken/missing please report it on monero-site
> 
>     * https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#set_daemon
> 
>     * https://github.com/monero-project/monero/blob/v0.18.1.0/src/wallet/wallet_rpc_server_commands_defs.h#L2660

The problem is not that something doesn't work for me.
The problem is that when passing parameters in the wrong form, monero-wallet-rpc does not write about it in the error message, but writes about something else unrelated to the real error.


## llacqie | 2022-10-14T14:50:10+00:00
> > Also, since monero-wallet-cli does not check the correctness of the parameters format
> 
> Do you mean monero-wallet-rpc?

Yes, sorry.

## llacqie | 2022-10-14T15:06:22+00:00
> > RTFM , it even has examples. If an example is broken/missing please report it on monero-site
> > ```
> > * https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#set_daemon
> > 
> > * https://github.com/monero-project/monero/blob/v0.18.1.0/src/wallet/wallet_rpc_server_commands_defs.h#L2660
> > ```
> 
> The problem is not that something doesn't work for me. The problem is that when passing parameters in the wrong form, monero-wallet-rpc does not write about it in the error message, but writes about something else unrelated to the real error.

I said that I used the implementation of the json_rpc client made as a separate library. I gave this as an example, when you cannot immediately see that the request is incorrect, because you do not see the raw request being sent, without turning on tracing, and the error message does not indicate that something might be wrong with the way you send parameters.

## moneromooo-monero | 2023-01-01T09:51:31+00:00
I just looked and technically, it's correct :D The first thing it looks for in the parameters is the ssl mode, and it cannot find a valid one.
A check for an object in the json code would be a nice improvement.

## moneromooo-monero | 2023-01-01T10:11:56+00:00
https://github.com/monero-project/monero/pull/8692

# Action History
- Created by: llacqie | 2022-10-13T10:28:06+00:00
- Closed at: 2023-01-01T10:54:31+00:00
