---
title: 'Suggestion: nodes using --public-node aren''t currently usable by browser-based
  Monero apps.  Let''s fix that.  '
source_url: https://github.com/monero-project/monero/issues/8346
author: CryptoGrampy
assignees: []
labels: []
created_at: '2022-05-22T15:43:25+00:00'
updated_at: '2023-05-04T21:45:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There are many opportunities for browser-based Monero solutions that don't yet exist (web3, ecommerce, authentication, etc) but it's difficult to bootstrap these apps without more public Monero nodes that support direct browser access.  I've seen a number of devs express concern about this, and have run into the issue myself while developing HotShop.

Any browser-based wallet, webapp, or extension (HotShop, Xmr.gift, TipXMR,  himitsu, Spirobel's web3 extension etc) that directly points at a _public_ Monero node also requires that node to have ```--rpc-access-control-origins=*``` or there will be CORS errors in the browser and failed http requests (even using Tor browser and onion nodes).  Since we've just allowed this flag to be set to wildcard without needing ```rpc-login``` to be set as of the latest Monero release, I propose that any nodes using the ```public-node``` flag also must have the ```--rpc-access-control-origins``` set to wildcard or they have an warning/error in Monerod startup.  

If we want to encourage more browser-based development, we absolutely need more nodes that support browser usage.

# Discussion History
## selsta | 2022-05-22T15:44:55+00:00
To clarify, this is not a bug but intentional behavior. Can you edit the title to suggestion or something?

## CryptoGrampy | 2022-05-22T15:47:19+00:00
Is it really intentional behavior to block browsers from accessing public nodes?

## selsta | 2022-05-22T15:47:37+00:00
Yes, it is intentional behavior.

## selsta | 2022-05-22T15:53:24+00:00
I'd recommend someone to simply make a list with nodes that have `--rpc-access-control-origins=*` set. I think @plowsof was working on that.

## plowsof | 2022-05-22T18:26:16+00:00
Yes, i have a script to search peer lists for those nodes. so far i have only found 2. One of them from Seth.. and the 2nd from Seth ^^. I will reach out to [ditatompel](https://www.ditatompel.com/monero) to perhaps add another column to his server list which will show if they're compatible. This would at least raise awareness / volunteers to support browser apps. 
```Python
def check_cors(node):
  headers = {
  'Content-type': 'application/json', 
  'Accept': 'text/plain',
  'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:71.0) Gecko/20100101 Firefox/71.0",
  "Origin": "https://foo.example"
  }

  data={"jsonrpc":"2.0","id":"0","method":"get_info","params":{}}
  try:
    r = requests.post(f"http://{node}/gettransactions", json=data, headers=headers,timeout=2)
  except:
    return
  resp_headers = r.headers
  if resp_headers.get("Access-Control-Allow-Origin"):
    print(f"Allows hotshop {node}")
```
So we could raise awareness / have a public list of these nodes 

## lalanza808 | 2023-05-04T21:45:17+00:00
I maintain a list of web compatible nodes here: https://monero.fail/?chain=monero&network=mainnet&cors=on

# Action History
- Created by: CryptoGrampy | 2022-05-22T15:43:25+00:00
