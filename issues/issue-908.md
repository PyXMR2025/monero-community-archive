---
title: Show actually used assembly instead of detection result (cnv2)
source_url: https://github.com/xmrig/xmrig/issues/908
author: YetAnotherRussian
assignees: []
labels:
- wontfix
created_at: '2019-01-16T07:05:21+00:00'
updated_at: '2019-08-02T12:58:22+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:58:22+00:00'
---

# Original Description
For Bulldozer CPUs there is no cnv2 double hash bundled assembly, so the sandy bridge one is used:

if (VARIANT == xmrig::VARIANT_2) {
        cnv2_double_mainloop_sandybridge_asm(ctx[0], ctx[1]);
    }

You should not print "ASSEMBLY: auto (bulldozer)" to UI as this is not true :) Same for other CPUs ofc.

Print "ASSEMBLY: default (sandy bridge)" or something like this.


# Discussion History
# Action History
- Created by: YetAnotherRussian | 2019-01-16T07:05:21+00:00
- Closed at: 2019-08-02T12:58:22+00:00
