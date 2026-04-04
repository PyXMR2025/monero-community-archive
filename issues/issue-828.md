---
title: 'Simplewallet RPC log error: "failed to deserialize extra field"'
source_url: https://github.com/monero-project/monero/issues/828
author: bobfeldbauer
assignees: []
labels: []
created_at: '2016-04-29T05:51:59+00:00'
updated_at: '2016-07-07T20:01:49+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:01:49+00:00'
---

# Original Description
In simplewallet's log, I'm seeing the following:

2016-Apr-29 01:43:12.834831 [RPC0]failed to deserialize extra field. extra = 01da322886e9ac6120d0a3a025874f5ecce62cfd86dd2074bc0cfed11d4641d755de20bae23e97571b90a2d798
be6dbb3925148f56c3fa3460d30037947755652cb0240221005541a8f4ef8e4b45e89f0471464a30a13d6a3ee3797cc364d919636d92cc3f6c
2016-Apr-29 01:43:12.834895 [RPC0]Transaction extra has unsupported format: <46d342520b15c58083ded6fde58533a084bbbb0254601592ce68a19e8910c9a2>


# Discussion History
## moneromooo-monero | 2016-04-29T20:58:38+00:00
Looks like that tx has a pubkey field with data that's larger than a pubkey. So it looks like whoever is building this tx is doing it wrong.


## Gingeropolous | 2016-04-29T22:04:38+00:00
2016-Apr-29 16:04:04.531549 [RPC0]Transaction extra has unsupported format: <132                                                                                        6a75fcf5393e5b740fe44ffbeaf2eef388725c58df817f8aad9f984eba071>
2016-Apr-29 16:05:04.976844 [RPC0]failed to deserialize extra field. extra = 01e                                                                                        1b8fad3c8d2d3d33f6f6fde422eac49306f9a5fc906563d9890a967e62c1cb1de20a631c6488889a                                                                                        623839efa9287602bdd77e0c353b3c22da72cc318ec5b9f79b202210000000000000000000000000                                                                                        00000000000000000000000000000000000113691
2016-Apr-29 16:05:04.976902 [RPC0]Transaction extra has unsupported format: <cc1                                                                                        4b32d70dfb84e33b721ba0c395db52e66d3cb39a0aeb38d1d03b6be2f66a4>
2016-Apr-29 16:08:26.329813 [RPC0]failed to deserialize extra field. extra = 011                                                                                        554ca4546b8fffbc960249e03068cbcffd9e4e4847cae3b0d622324a04a3ae6de2033478ece9f849                                                                                        d1a84db29e45b7b9e03609e4fbec79b160ba1362b216052955a02210056fdfe37aa10c0f1962bb36                                                                                        3f0f63bf81f50d98749809713e4fa85d76de98d19
2016-Apr-29 16:08:26.330033 [RPC0]Transaction extra has unsupported format: <05f                                                                                        b30fd0dec77c8eb333091c6d6ac64d2233fd2953ff25d2132985cfde1286a>
2016-Apr-29 16:37:39.645947 [RPC0]failed to deserialize extra field. extra = 01f                                                                                        b6d30fa8e276af8192829b87c7310bfc85cfe43e9eb18e2f22b579fece026cbde209808c552e6f15                                                                                        0aae9586e22e883dc5e9e9b526e18324b244d5ce71cbaa1b3ce022100513c2ff706a499dab4e4598                                                                                        496e2c0601b1a094af19e666cde83496660376f2b
2016-Apr-29 16:37:39.646133 [RPC0]Transaction extra has unsupported format: <b8a                                                                                        8ff44bbf89ef0945306ae00d98aa0bc763b40866878961c277f99a007c0dd>
2016-Apr-29 17:00:28.608001 [RPC0]failed to deserialize extra field. extra = 01e                                                                                        f45848b536b716e7f3c154e597680478a6d430512e9f60025aad63839313398de20df528e4ab554b                                                                                        d0c1949ed3669f5fb7d7b61bb787a78a65b67068fe5c65c1e9c02210075e03ca8d5cb81b6ebf61c0                                                                                        c108feff64d7892077d20ee6ca63b3484413303a5
2016-Apr-29 17:00:28.608057 [RPC0]Transaction extra has unsupported format: <330                                                                                        be3e44f33270d7f768d4c525460f1f6ec0112b67c8581100f4c20fef516d8>


## moneroexamples | 2016-04-30T09:29:02+00:00
Just noticed this issue after I made new one regarding the same problem:

https://github.com/monero-project/bitmonero/issues/829

However, I provide more info there, with specific tx causing the problem. Maybe useful to get more info about the parsing error.


## fluffypony | 2016-07-07T20:01:49+00:00
Fixed


# Action History
- Created by: bobfeldbauer | 2016-04-29T05:51:59+00:00
- Closed at: 2016-07-07T20:01:49+00:00
