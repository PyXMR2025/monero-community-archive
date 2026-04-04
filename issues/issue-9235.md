---
title: 'monerod: rpc_request fails when rpc-login set'
source_url: https://github.com/monero-project/monero/issues/9235
author: ml-
assignees: []
labels:
- bug
created_at: '2024-03-10T21:49:35+00:00'
updated_at: '2024-08-14T11:47:18+00:00'
type: issue
status: closed
closed_at: '2024-03-11T23:40:49+00:00'
---

# Original Description
v0.18.3.2 broke sending rpc_request with `monerod [daemon_command]` when `rpc-login` is set in `bitmonero.conf`. Issue is on the client side, curl requests to the daemon still work.

```bash
$ monerod --stagenet status
2024-03-10 21:34:39.273	I Monero 'Fluorine Fermi' (v0.18.3.2-release)
2024-03-10 21:34:39.276	E Client has incorrect username/password for server requiring authentication
2024-03-10 21:34:39.276	I Failed to invoke http request to  /getinfo
Error: Problem fetching info-- rpc_request: 


# Still works with curl!
$ curl --digest -u usr:pw --json '{"jsonrpc":"2.0", "id":"0", "method":"get_info"}' http://127.0.0.1:38081/json_rpc
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "adjusted_time": 1710105095,
    "alt_blocks_count": 0,
    "   <snip>   ": 69,
    "version": "0.18.3.2-release",
    "was_bootstrap_ever_used": false,
    "white_peerlist_size": 49,
    "wide_cumulative_difficulty": "0x5617c07e23",
    "wide_difficulty": "0x124b23e"
  }
}

# Old monerod (v0.18.3.1) --to--> new monerod (v0.18.3.2) also works
$ ./monerod.old --stagenet status
2024-03-10 21:34:43.652	I Monero 'Fluorine Fermi' (v0.18.3.1-release)
Height: 1563499/1563499 (100.0%) on stagenet, not mining, net hash 159.74 kH/s, v16, 12(out)+26(in) connections, uptime 0d 1h 14m 38s
```

Related?
https://github.com/monero-project/monero/commit/e0b2123c324ae80177fd7c6b0516a9f8840803d9

**Edit:** It seems to happen **only when rpc-login is set** in the `bitmonero.conf`. No issues when no auth is used.

# Discussion History
## selsta | 2024-03-10T21:54:50+00:00
```
./monerod status
```

works for me without RPC password, but I have seen a similar wrong password error in the GUI recently that was only showing up sporadically.

## ml- | 2024-03-10T22:13:13+00:00
@selsta Thanks for this info. It indeed only happens when rpc-login is set. Edited issue.

## nahuhh | 2024-03-10T23:15:06+00:00
@ml- 
```
 monerod --stagenet status --rpc-login=username:password
```

update: comparing behavior on 18.3.1 vs 18.3.2, using flags as above, and was able to reproduce OPs issues 
`monerod [command] --rpc-login=username:pass`
returns "Client has incorrect username/password"

## selsta | 2024-03-11T00:16:29+00:00
Can confirm that reverting https://github.com/monero-project/monero/commit/e0b2123c324ae80177fd7c6b0516a9f8840803d9 solves the issue.

## 0xFFFC0000 | 2024-03-11T02:34:08+00:00
Take this patch as example: 


```
diff --git a/contrib/epee/include/net/http_client.h b/contrib/epee/include/net/http_client.h
index ecbceb566..1e74cdafb 100644
--- a/contrib/epee/include/net/http_client.h
+++ b/contrib/epee/include/net/http_client.h
@@ -220,6 +220,8 @@ namespace net_utils
                                        add_field(req_buff, field);
 
                                {
+                                       __TRY_CONNECTING_AGAIN:
+                                       const std::size_t initial_size = req_buff.size();                                       
                                        const auto auth = m_auth.get_auth_field(method, uri);
                                        if (auth)
                                                add_field(req_buff, *auth);
@@ -254,11 +256,17 @@ namespace net_utils
                                                return true;
                                        }
 
-                                       if (m_auth.handle_401(m_response_info) == http_client_auth::kParseFailure)
+                                       switch (m_auth.handle_401(m_response_info))
                                        {
+                                       case http_client_auth::kSuccess:
+                                               req_buff.resize(initial_size); // rollback for new auth generation                                              
+                                               goto __TRY_CONNECTING_AGAIN;
+                                               break;
+                                       default:
+                                       case http_client_auth::kParseFailure:
                                                LOG_ERROR("Bad server response for authentication");
                                                return false;
-                                       }
+                                       }                                       
                                }
                                LOG_ERROR("Client has incorrect username/password for server requiring authentication");
                                return false;
```

This does fix the bug for the moment.


## jeffro256 | 2024-03-11T03:43:18+00:00
Yes, that will fix the bug. Although it could be more efficient if we know that we will be trying with a login later, then we don't send the body now. 

## jeffro256 | 2024-03-11T04:02:25+00:00
Let's just revert and I'll redo it since a release is coming soon. 

## nahuhh | 2024-03-11T04:04:04+00:00
We already released. Were re-releasing

## jeffro256 | 2024-03-11T04:10:58+00:00
I'm sorry about that, I don't know how I overlooked that aspect of the HTTP digest auth process.

## selsta | 2024-03-11T23:40:49+00:00
We reverted this commit and will soon release a new version.

## thisIsNotTheFoxUrLookingFor | 2024-08-14T11:27:33+00:00
~~Is it fixed? i have rpc-login set and I'm getting 401 in v0.18.3.3~~

Oh, I had to set SSL enabled instead of auto-detect and then it worked... I am binding to 0.0.0.0 inside the docker container so it thinks it is an external bind but it is not. i wish it would not baby us so much.

## selsta | 2024-08-14T11:46:11+00:00
@tortxoFFoxtrot yes, the issue was fixed. can you share more information what you are trying to do?

## thisIsNotTheFoxUrLookingFor | 2024-08-14T11:47:17+00:00
@selsta seems because I am binding to 0.0.0.0 inside the docker container it treats it as an external bind and if it does not have SSL set enabled it just gives 401 nomatter what. When I set SSL enabled instead of autodetect it is working now.

# Action History
- Created by: ml- | 2024-03-10T21:49:35+00:00
- Closed at: 2024-03-11T23:40:49+00:00
