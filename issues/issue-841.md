---
title: 'json_rpc: method getblock returns invalid json'
source_url: https://github.com/monero-project/monero/issues/841
author: FelixWeis
assignees: []
labels: []
created_at: '2016-05-14T21:52:13+00:00'
updated_at: '2016-07-07T20:00:39+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:00:39+00:00'
---

# Original Description
The JSON result contains a section `result.blob` which is raw binary. This is obviously not allowed in normal JSON and should be encoded in hex. 


# Discussion History
## FelixWeis | 2016-05-14T21:55:26+00:00
to replicate this behaviour:

```
curl -v -X POST 127.0.0.1:18081/json_rpc -d '{"id":"0","jsonrpc":"2.0","method":"getblock","params":{}}' | jq .
```

[jq](https://stedolan.github.io/jq/) is a JSON cli tool.


## moneromooo-monero | 2016-06-09T20:50:14+00:00
https://github.com/monero-project/bitmonero/pull/863

The "json" field has an escaped string, which is not super useful either. I'll look to see if it can be set unescaped.


## moneromooo-monero | 2016-06-09T21:23:01+00:00
In fact, I think adding this json field was a stupid idea. There doesn't seem to be a way to save it as is, and I'm realizing that it'd need to be re-parsed in order for it to work in code, so that probably explains why existing code did not include raw txes/blocks/etc.


## moneromooo-monero | 2016-06-10T16:08:01+00:00
I've looked at properly displaying those as json, but AFAICT it's a differnet serialization system (KV_BEGIN_SERIALIZE_MAP vs BEGIN_SERIALIZE_OBJECT) and I got stopped at the boost::variant stuff. Any opinions on whether these dumps are worth spending time on ?


## fluffypony | 2016-07-07T20:00:39+00:00
Fixed


# Action History
- Created by: FelixWeis | 2016-05-14T21:52:13+00:00
- Closed at: 2016-07-07T20:00:39+00:00
