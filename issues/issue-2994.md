---
title: Optimize for Ryzen platform (5k series)
source_url: https://github.com/xmrig/xmrig/issues/2994
author: mooleshacat
assignees: []
labels: []
created_at: '2022-03-27T01:49:45+00:00'
updated_at: '2022-03-27T13:55:22+00:00'
type: issue
status: closed
closed_at: '2022-03-27T13:55:22+00:00'
---

# Original Description
Would like to see optimization for Zen 3 on the 5950x and other 5k series Ryzen

There is no mention of Zen specific optimization. Maybe update the readme to mention whether it is there or not.

# Discussion History
## Spudz76 | 2022-03-27T02:10:49+00:00
```
      --asm=ASM                 ASM optimizations, possible values: auto, none, intel, ryzen, bulldozer
```

Ryzen is listed right there?

## Spudz76 | 2022-03-27T02:11:56+00:00
There were no code-based changes between Zen2 and Zen3

Zen2 is better by slight margin than Zen3 but that was due to some internal/physical changes which can't be coded around.

## SChernykh | 2022-03-27T10:55:58+00:00
RandomX MSR mod has specific settings for Zen3, also cn/heavy has optimized code for Zen3. When something can be made faster on a specific CPU, it is taken care of.

## mooleshacat | 2022-03-27T13:54:12+00:00
> Ryzen is listed right there?

Thank you Sir/Madam!

I never saw that, because I was looking at the readme... It would be nice to see this information in the readme, because otherwise you have to git clone, compile, and then execute with --help flag to find it.

Closing ...

# Action History
- Created by: mooleshacat | 2022-03-27T01:49:45+00:00
- Closed at: 2022-03-27T13:55:22+00:00
