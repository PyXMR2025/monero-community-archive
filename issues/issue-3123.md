---
title: Neox Invalid address
source_url: https://github.com/xmrig/xmrig/issues/3123
author: dawidmosk
assignees: []
labels: []
created_at: '2022-09-17T22:26:47+00:00'
updated_at: '2022-09-18T11:37:09+00:00'
type: issue
status: closed
closed_at: '2022-09-18T11:37:09+00:00'
---

# Original Description
After compile and run I'm getting error:

`[2022-09-18 00:24:21.089]  net      neox.2miners.com:4040 Invalid address`

but when I set xmr it's working?
Any ideas?


# Discussion History
## Spudz76 | 2022-09-18T00:35:05+00:00
Neoxa appears to use kawpow for its PoW piece.  Set algorithm to `kawpow` and that's only available with a GPU.

## dawidmosk | 2022-09-18T11:37:09+00:00
Not working. I did try to command line and json file. I did tried without coin, only algo, only ip.
Changed to xmr. address and working. 
```

   "pools": [
        {
            "algo": "kawpow",
            "coin": "",
            "url": "162.19.139.119:4040",
            "user": "neoxa:GTJB7yi6rVARh98KH3HMxFEXX5CYWUpuXL",
            "pass": "x",

```

Now i changed to ssl port with disabled option and working. Thank You.



# Action History
- Created by: dawidmosk | 2022-09-17T22:26:47+00:00
- Closed at: 2022-09-18T11:37:09+00:00
