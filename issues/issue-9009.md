---
title: mms auto_config bitmessage json has binary
source_url: https://github.com/monero-project/monero/issues/9009
author: lacdael
assignees: []
labels:
- bug
- pending review
created_at: '2023-09-28T22:58:27+00:00'
updated_at: '2023-12-07T20:18:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
mms auto_config is failing because the JSON sent via bitmessage JSON can't deserialize 

```
$ ./monero-wallet-cli --version
Monero 'Fluorine Fermi' (v0.18.2.2-release)
```

```
2023-09-28 22:56:17.590     7f8c8ffb76c0        ERROR   default contrib/epee/include/storages/portable_storage_from_json.h:88   Wrong JSON character at: BM-2cT3rK2mqxVNbWAmk5MdU2Wz28TsvoYggC
2023-09-28 22:56:17.590     7f8c8ffb76c0        ERROR   default contrib/epee/include/storages/portable_storage_from_json.h:403  Failed to parse json, what: Wrong JSON character at: BM-2cT3rK2mqxVNbWAmk5MdU2Wz28TsvoYggC
2023-09-28 22:56:17.590     7f8c8ffb76c0        ERROR   wallet.mms      src/wallet/message_transporter.cpp:124  Failed to deserialize messages
```

from testnet wallets:

```
{
  "content": "g,'8*$BR\"mIUW_vqF#e:ߧ_ ofe?H\bcdKTikD`V@su",
  "destination_monero_address": {
    "m_spend_public_key": "��������������������������������",
    "m_view_public_key": "��������������������������������"
  },
  "destination_transport_address": "BM-2cSrgeeXv5oEvBLMzTaX7zmvVGJV1XanWz",
  "encryption_public_key": "fK\/6dG=>�*\v)g)2",
  "hash": "q).U\"HSUv&lQ",
  "iv": "9eMi",
  "round": 0,
  "signature": ")ez'8=&LITx\tt\vc\t8\v}ܹ+򇅚.Yoz\n",
  "signature_count": 0,
  "source_monero_address": {
    "m_spend_public_key": "\v#pݕLZSzҙ!BI",
    "m_view_public_key": "r-o@�7EfKaU,+{>"
  },
  "source_transport_address": "BM-2cXibCmyMyGBsCt1RN5DBsiUkWWpr1FtnV",
  "subject": "MMS V0 2023-09-28 22:31:59",
  "timestamp": 1695940319,
  "transport_id": "",
  "type": 7
}
```

# Discussion History
## selsta | 2023-09-29T11:50:48+00:00
@rbrunner7 any idea?

## rbrunner7 | 2023-09-29T11:52:18+00:00
That JSON looks ok. Maybe surprisingly so, but the JSON serializer / deserializer used just puts binary data into string values in JSON, and that's why this sample looks so strange.

But this is not the JSON of the message that failed, I would say, because that Bitmessage address in the error messages does not appear in it. Any chance that we get to see the message that causes the error?

The problem looks strange to me, by the way, no idea why suddenly there should be errors with something as basic and true-and-tried as JSON parsing.

## lacdael | 2023-10-03T15:23:01+00:00
Hi, sorry, I should mention this was done with --testnet,

alice:
```
>mms init 2/2 alice BM-XXXXXXXXXXXXXXXXX
>mms signer 2 bob
>mms start_autoconfig
```

bob: 
```
>mms init 2/2 bob BM-XXXXXXXXXXXXXXX
>mms auto config mmsxxxxxx
```

Message:

```
ew0KICAiY29udGVudCI6ICKpkp77ec5pfd7pcJcyDyZnaqYy1qj9Vnjar8ehXC+zXVRYzSAxPTVcblhiYKOdBAWFgN4FGfFcZmDXkOQZmlx0H1kH2PxSHrsTS/bCXGbigqoCHCk0vamI6EefB3jLtcRPrTNuHuflB8ctmtsDlo4dIiwNCiAgImRlc3RpbmF0aW9uX21vbmVyb19hZGRyZXNzIjogew0KICAgICJtX3NwZW5kX3B1YmxpY19rZXkiOiAiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAiLA0KICAgICJtX3ZpZXdfcHVibGljX2tleSI6ICIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACINCiAgfSwNCiAgImRlc3RpbmF0aW9uX3RyYW5zcG9ydF9hZGRyZXNzIjogIkJNLTJjVEw1ODZZTmhOOFQ2eVlqcjJpU1R0SEFzV2g5TVB4ZGEiLA0KICAiZW5jcnlwdGlvbl9wdWJsaWNfa2V5IjogIiVz9RiwSFlccpmZD+dOZpaJMtWe3Nby+oivIBQYXC8wSxQiLA0KICAiaGFzaCI6ICKlAAOJ1Z2V+upLeFJwWG/eqVx0o9FLX3yOsVn6AxlcXFwixSIsDQogICJpdiI6ICJVfhUdQ/Cb2yIsDQogICJyb3VuZCI6IDAsDQogICJzaWduYXR1cmUiOiAi0uZ/kaeLET7iPecmtzHZibVIkOJddFLUnINfo5l99gHi1IVzvm1f9aJHlxm69ErdFl41ia285kPlRLgPPiNJBSIsDQogICJzaWduYXR1cmVfY291bnQiOiAwLA0KICAic291cmNlX21vbmVyb19hZGRyZXNzIjogew0KICAgICJtX3NwZW5kX3B1YmxpY19rZXkiOiAiRQGEXGKsMnL6TR7QHveDrB3F0LY4v/8UY+O5q56d4jPUIiwNCiAgICAibV92aWV3X3B1YmxpY19rZXkiOiAiOgQ+tYNCctr5D47ZXHRsRk9Je12a6gARyMLamj9AvpRrIg0KICB9LA0KICAic291cmNlX3RyYW5zcG9ydF9hZGRyZXNzIjogIkJNLTJjWDJjY0R3WUZyQTJ3SllhY2pRUm9xNFR3Zzk0UUY5TEwiLA0KICAic3ViamVjdCI6ICJNTVMgVjAgMjAyMy0xMC0wMyAxNToyMTowNyIsDQogICJ0aW1lc3RhbXAiOiAxNjk2MzQ2NDY3LA0KICAidHJhbnNwb3J0X2lkIjogIiIsDQogICJ0eXBlIjogNw0KfQ==
```

## rbrunner7 | 2023-10-03T17:07:34+00:00
Thanks, but I meant something different:

In your post you show the decrypted JSON of a certain message. Not sure how you got hold of that, I assumed that you used a debugger to stop the program at the right point to grab that out of some string variable, but maybe I am wrong.

The listed error messages however don't seem to correspond with the JSON that you show, because the Bitmessage address from the error messages, `BM-2cT3rK2mqxVNbWAmk5MdU2Wz28TsvoYggC`, does not appear in the JSON as far as I can see. That's what I meant: Maybe the JSON meant for *another* message has a problem, and it would be interesting to see *that* JSON.

## vtnerd | 2023-10-11T14:49:27+00:00
I _think_ what @lacdael is pointing out is that JSON is supposed to be UTF8, and the current encoder will dump non-utf8 binary. Some areas of the code manually convert binary to hex, and the new serialization I wrote has built-in support for binary reading/writing (which converts to hex for JSON).

Given that BitMessage is dead, is this worth fixing?

## rbrunner7 | 2023-10-11T18:38:04+00:00
> is that JSON is supposed to be UTF8

Yeah, of course that JSON is pretty strange, but A) PyBitmessage never sees that as JSON, but only hexed after encryption, and B) the MMS worked for me for literally hundreds of messages like those.

But maybe there is some small hole in our JSON code that you only trigger if the binary data by pure chance contains a very specific character sequence. Maybe there is some case of escaping that does not work right, if the value contains some combination of double quotes " and backslashes \\. How does that sound?

## vtnerd | 2023-10-11T22:20:26+00:00
> Maybe there is some case of escaping that does not work right, if the value contains some combination of double quotes " and backslashes \.

That would be my guess.

But again, since BitMessage is not being maintained, is this issue worth tracking down? I believe most situations don't use binary in a string like this.

# Action History
- Created by: lacdael | 2023-09-28T22:58:27+00:00
