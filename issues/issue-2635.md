---
title: 'basic_filebuf::underflow error reading the file: iostream error'
source_url: https://github.com/xmrig/xmrig/issues/2635
author: gravisxv
assignees: []
labels: []
created_at: '2021-10-17T08:07:57+00:00'
updated_at: '2021-10-18T06:59:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello i am trying to mine ravencoin on 290x card. All the settings are ok, i simply start mining correctly until this message appear:
basic_filebuf::underflow error reading the file: iostream error

I have not found any workaround. The problem is not related to the videocard or Os as nanominer is working ok.

Currently im using Manjaro 20.1 and 20.45 amdgpu drivers.



# Discussion History
## Spudz76 | 2021-10-17T20:24:25+00:00
I wouldn't use newer than 20.30-1109583 on anything Hawaii or older.  But not likely the problem.

Never, ever, ever seen that error before, are you sure it's from xmrig?

## gravisxv | 2021-10-18T06:14:55+00:00
Yep, but i just fixed it. I build the source directly in the menu. It seems the binaries in the download section are not compatible with Manjaro or with Kawpow algo.

## Spudz76 | 2021-10-18T06:59:34+00:00
Ah, yes, those are for Ubuntu/Debian mostly.  Who knows what might be different... probably glibc where all that filestream stuff lives...

# Action History
- Created by: gravisxv | 2021-10-17T08:07:57+00:00
