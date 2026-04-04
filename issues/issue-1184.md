---
title: '[proposal] add `monero_node:` to the URI spec'
source_url: https://github.com/monero-project/meta/issues/1184
author: nahuhh
assignees: []
labels: []
created_at: '2025-04-05T01:39:07+00:00'
updated_at: '2025-12-30T00:04:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Cake Wallet and the Monero Nodo project currently utilize a URI for sharing node parameters, but the URI doesn't match the style of other [monero based URIs](https://github.com/monero-project/monero/wiki/URI-Formatting).

This proposal is to standardize the URI for adding/sharing nodes (so all interested parties can be compatible).

The proposed URI is:
```
monero_node:[host=]<host>?port=<port>[&protocol=<string>][&username=<username>&password=<password>][&trusted=<bool>][&label=<label>] 
```

Everything in square brackets is optional.

The below would be appended to the URI doc [here](https://github.com/monero-project/monero/wiki/URI-Formatting)

---

## Node Sharing Scheme
The following scheme is proposed as a means of sharing node parameters.

```
monero_node:[host=]<host>?port=<port>[&param=<param>][&param2=<param2]
```

| Parameter      | Type    | Optional | Requires      | Description |
|:---------------|:-------:|:--------:|:------------- |:------------|
| `host`         | String  | n        | `port`        | Domain or IP address of node |
| `port`         | String  | n        | `host`        | Port which the RPC is bound  |
| `protocol`     | String  | y        | `host`,`port` | Set transport protocol       |
| `username`     | String  | y        | `host`,`port` | Username of the RPC login    |
| `password`     | String  | y        | `host`,`port` | Password of the RPC login    |
| `trusted`      | Bool    | y        | `host`,`port` | Mark the node as trusted     |
| `label`        | String  | y        | `host`,`port` | Specify a label for the node |

The resulting URI for sharing node parameters may look like this:
```
monero_node:192.168.1.1?port=18089&protocol=https&trusted=true
```
or
```
monero_node:192.168.1.1?port=18089&username=monero&password=xmr&trusted=true&label=My%20Node
```

# Discussion History
## acx-usernamealreadyused | 2025-04-05T08:48:37+00:00
I support this proposal.  

The only concern I have is with the `tls` field - do you think it might be a good idea to replace it with `[&schema=http/https]` (or something like `protocol`) instead?  
It seems to me that this would make the uri more generic, allowing us to use protocols other than http(s) in the future.

## detherminal | 2025-11-04T19:34:43+00:00
Needed for better UX, I support this.

## iamamyth | 2025-12-30T00:02:01+00:00
Following RFC 3986 would make the URIs much easier to parse/analyze:
`monerorpc[+<protocol>]://[<user>:<password>@]<host>[:<port>]#[param [&param]]`

where param is one of: `trusted` and `label`.

The motivating examples become:
```
monerorpc+https://192.168.1.1:18089#trusted=true
monerorpc://monero:xmr@192.168.1.1:18089#trusted=true&label=My%20Node
```

# Action History
- Created by: nahuhh | 2025-04-05T01:39:07+00:00
