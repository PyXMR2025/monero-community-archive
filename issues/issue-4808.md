---
title: How many outputs can we have in a transaction?
source_url: https://github.com/monero-project/monero/issues/4808
author: Pei116
assignees: []
labels:
- invalid
created_at: '2018-11-05T18:14:23+00:00'
updated_at: '2018-11-05T20:25:05+00:00'
type: issue
status: closed
closed_at: '2018-11-05T20:25:05+00:00'
---

# Original Description
So I've been trying to send XMR to multiple addresses via RPC calls. I saw in several places that there's no technical limit in number of output addresses in a transaction.
Though, when I put more than 15 addresses in transfer method, it's failing with an error as following:
```
{
  "error": {
    "code": -4,
    "message": "sv\/gamma are too large"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```

The post body is something like following:
```
{
    "method": "transfer",
    "id": "0",
    "jsonrpc": "2.0",
    "params": {
        "account_index": 0,
        "destinations": [
            {
                "amount": 100000000000,
                "address": "58HZBZB9Xb67AdLJnHDDEpR1aWGoDfTcxjiYNAYLV3kFKSayJ1dd77BcRZcfe2DinScsdd58U2HWmVA1mnZxVrvbJRgsyqr"
            },
            {
                "amount": 100000000000,
                "address": "56dmCeEp8xRht2gHnEBg71LwAEmeU1nFhADSeasTCQA4BsBQMWmdDC33VWKEZuQ5m6PzuS3ZKShNzWRQqWuhUh1S619uK93"
            },
            {
                "amount": 100000000000,
                "address": "53shxswJjPTZZeGZRAu3fGb2Db2h46qZA6N9eEp38buW9LV7cmuq4MkVWd5v352tfxDec7tYcE2mCMGReFtk4dSUFCBresy"
            },
            {
                "amount": 100000000000,
                "address": "56x4ZqhKBKTeheQmxXVZGRbVxpUTwtWsVcw34pLGGfbQHmU4HzskZDk367pkvEHYpybgEe9g6KUAFLHqptaByJPq92btCZ7"
            },
            {
                "amount": 100000000000,
                "address": "51wP6nAZg4CgwnFha7k2sKBnmWzYbiNKgTDiZFgwrs1ejXk4rjNfaLpR5yJee7pJ6nTgdxUVK4L2NXPYRgWvEyeq1KUiKEX"
            },
            {
                "amount": 100000000000,
                "address": "572w1CbXPn481aJLMm6rfVFpXkY85UiS6RRvxkjSbN664q84xEBnptJNdsijomaLsE6gLnSesk7YCX5UgDXm1tdpUjZmdA8"
            },
            {
                "amount": 100000000000,
                "address": "559AFaqYCag7UDf49jwvxsUaAWvi1oQTcdV3B753FERqEoaiiXKJtbveaazpAetUw1MQvs4Ex1ZczcGZxF64eQxLAdazSnz"
            },
            {
                "amount": 100000000000,
                "address": "588b3XJzcDm68xewdos66kLRsmaRfTULYRabsPvpWoYdiUhxgp7UFp1RgVZCzXbJdngRVMLR8FtJxg7PcPTToqPPUp5sFjd"
            },
            {
                "amount": 100000000000,
                "address": "53uNbiJ2yjwSoD4SdA9qRpZ9yUTvs4FQxWbVvCgQddpT715niKaSLLTLiMuZyV8tHtF3kuWz38aN7fFQLmZPv2iz26Au1fS"
            },
            {
                "amount": 100000000000,
                "address": "53LNicCbtKHEQrJtf2bDswJv6eDx8dHzE8i2kmudufLpJsPqvoYwup2aW1kvzowB9vbpYbcy8Ju7gbA4vdKDKt9XJEzGVjR"
            },
            {
                "amount": 100000000000,
                "address": "52gHCEuYpbnXG64gvXJyjMQ3JAGkkjo1QZYa69c6D6aUXenvPFcqjmKaFuerek4T48Sp685ocaze9CGiTVmRQMN99mQQ3Cv"
            },
            {
                "amount": 100000000000,
                "address": "56uXxu4M7W5QdyYCd1RAkjMrxJHu7LQh6gWgNHwz1xLWGCy68xUgVCR4m4cPie7fr1XjQocU6KPJLVcA3HGHLGFPEm9gp7t"
            },
            {
                "amount": 100000000000,
                "address": "54CgkL4bmyCJkeTyuxqVqUEZ1K9iVEx4ccRWNyEg74Z2f7u2By6hWE9BSr3zBupAAJUKzLJgD3pD7NEsCgGbZSWa75adbS4"
            },
            {
                "amount": 100000000000,
                "address": "5AwKCSQ3tv5GDm2zu8oYLUFFrqinsiUvP17VKSupqexCLaXCK9Ja1igQTRyVQDW7UtVmh3WePyhbWK44NssqRRyJ8MhiQuD"
            },
            {
                "amount": 100000000000,
                "address": "56vGmi9JH1gJmvFVkdsJb5V39KHWme2xy93mZZ1vx1PxVxtPfaDCnZsgqGQrJxrv6sQPoVQ2wZx6zAw3pBWb64uKVThRaVH"
            },
            {
                "amount": 100000000000,
                "address": "5Ako7rp44KiUAn2JhaQAaocX3HM9ssTDtiNoxZL3GGKFXR8RgNocqJWZihsc711MsSh2EdxHNDAXkHrRf3kNdawPGtqzzqH"
            }
        ]
    }
}
```

# Discussion History
## moneromooo-monero | 2018-11-05T20:20:11+00:00
As it tells you, 16 now.

+invalid


## Pei116 | 2018-11-05T20:22:19+00:00
I've found a constant for that which is initiated as 16 in the code. Can we customize it to make it bigger?

# Action History
- Created by: Pei116 | 2018-11-05T18:14:23+00:00
- Closed at: 2018-11-05T20:25:05+00:00
