---
title: name convention?
source_url: https://github.com/monero-project/monero/issues/4737
author: calidion
assignees: []
labels:
- wontfix
created_at: '2018-10-27T14:29:36+00:00'
updated_at: '2019-01-20T20:24:45+00:00'
type: issue
status: closed
closed_at: '2019-01-18T18:57:17+00:00'
---

# Original Description
Currently types are using names like public_key,  ec_point, private_key.

which is very hard to distinguish them from variables.

And some even confusing  types are `secret_keyV`.

It seems there is no rule for how to define a clear class, struct, function, variable?

# Discussion History
## calidion | 2018-10-27T14:39:22+00:00
for structs.

1. struct type one: full lower case

```
  struct block_complete_entry
  {
    blobdata block;
    std::vector<blobdata> txs;
    BEGIN_KV_SERIALIZE_MAP()
      KV_SERIALIZE(block)
      KV_SERIALIZE(txs)
    END_KV_SERIALIZE_MAP()
  };
```

2. struct type two: full upper case
```
  struct NOTIFY_NEW_BLOCK
  {
    const static int ID = BC_COMMANDS_POOL_BASE + 1;

    struct request
    {
      block_complete_entry b;
      uint64_t current_blockchain_height;

      BEGIN_KV_SERIALIZE_MAP()
        KV_SERIALIZE(b)
        KV_SERIALIZE(current_blockchain_height)
      END_KV_SERIALIZE_MAP()
    };
  };
```


## moneromooo-monero | 2018-10-27T14:42:10+00:00
There is indeed no such hard convention, but foo_bar is usually used, and preferred, though if you define new types in a series, such as a new message type, follow the existing code.
A fairly common thing is to add "_t" at the end of a type when a typical variable is going to collide often, but that's usually for short types.


## calidion | 2018-10-27T14:45:50+00:00
It would be much better if `_t` is added.

## moneromooo-monero | 2018-10-27T14:48:19+00:00
Please don't send such a patch :) Though if you need to add new types, that'd be fine.

## fluffypony | 2018-10-27T18:12:43+00:00
I think we’re generally fine with refactor as you go. If you have a PR that interacts with a poorly named struct then by a means rename it, but don’t rename for renaming’s sake.

## moneromooo-monero | 2018-10-27T18:19:03+00:00
If it's local, sure. If it involve renamings in random other places, I would say no. But hey, depends on the particulars.

## fluffypony | 2018-10-27T18:22:14+00:00
Maybe put the renaming in a separate commit that you can nuke if the consensus is that it’s too invasive?

## calidion | 2018-11-05T03:58:48+00:00
I have renamed a lot of types from the original cryptonote code.
The process is made easy with the bash script:

https://github.com/vigcoin/coin/blob/master/replace-types.sh

Feel free to use it when necessary:)

## moneromooo-monero | 2019-01-18T18:55:15+00:00
+wontfix

## Gingeropolous | 2019-01-20T20:24:45+00:00
@moneromooo-monero , is there a doc that explains / details the conventions so they can be refactored-as-u-go?

# Action History
- Created by: calidion | 2018-10-27T14:29:36+00:00
- Closed at: 2019-01-18T18:57:17+00:00
