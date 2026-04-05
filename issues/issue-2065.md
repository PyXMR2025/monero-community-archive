---
title: Compile Error with -DWITH_ARGON2=OFF
source_url: https://github.com/xmrig/xmrig/issues/2065
author: johanneshahn
assignees: []
labels:
- bug
created_at: '2021-01-28T13:08:58+00:00'
updated_at: '2021-04-12T14:18:58+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:18:58+00:00'
---

# Original Description
If you compile with Option "-DWITH_ARGON2=OFF" i got following error:

`/src/core/config/ConfigTransform.cpp:153:55: error: no member named 'kArgon2Impl' in 'xmrig::CpuConfig'`

there is simple missing a "ifdef XMRIG_ALGO_ARGON2" around the code lines

```
#   ifdef XMRIG_ALGO_ARGON2
    case IConfig::Argon2ImplKey: /* --argon2-impl */
        return set(doc, CpuConfig::kField, CpuConfig::kArgon2Impl, arg);
#   endif
```


# Discussion History
## SChernykh | 2021-01-28T13:35:44+00:00
That option is really off only when you also use `-DWITH_RANDOMX=OFF` because RandomX uses Argon2 for dataset initialization. I checked with just `-DWITH_ARGON2=OFF` and it compiles fine because RandomX enables it back again.

## SChernykh | 2021-01-28T13:39:07+00:00
Should be fixed in https://github.com/xmrig/xmrig/pull/2067

# Action History
- Created by: johanneshahn | 2021-01-28T13:08:58+00:00
- Closed at: 2021-04-12T14:18:58+00:00
