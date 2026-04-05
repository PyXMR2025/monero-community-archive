---
title: 'Enhancement Request: Intel Relaxed Allocation Limits or CL_MEM_ALLOW_UNRESTRICTED_SIZE_INTEL '
source_url: https://github.com/xmrig/xmrig/issues/3257
author: iamhumanipromise
assignees: []
labels:
- review later
- opencl
created_at: '2023-04-20T23:08:30+00:00'
updated_at: '2025-06-18T22:36:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This started because of an issue with Stable Diffusion... but it applies to XMRIG also! Based on the conversation below, it looks like the Intel Compute Runtime permits CL kernel sizes over 4GB but needs 

`CL_MEM_ALLOW_UNRESTRICTED_SIZE_INTEL`
which needs to the compile flag `-cl-intel-greater-than-4GB-buffer-required` 

But they reccomend using the ["Relax Allocation Limits" control to automatically do that](https://github.com/intel/opencl-intercept-layer/blob/main/docs/controls.md#relaxallocationlimits-bool)

[Original Suggestion](https://github.com/intel/compute-runtime/issues/627?notification_referrer_id=NT_kwDOBkWThbQ1ODU2NzQyNzkxOjEwNTIyMzA0NQ&notifications_query=reason%3Aparticipating#issuecomment-1510139885)

# Discussion History
## Spudz76 | 2023-04-21T01:21:56+00:00
Looked at it all and summarize:

Kernel RTC should detect vendor Intel && algo needs >4GB,
then add both flags; there "is a cost" to them when not needed but nobody said what cost (assume it hurts speed?)

The "recommended" method affects every OpenCL program on the user/machine depending where you put the setting, and back to the "cost" that must not be best practice although it is globalized.  Not clear how to enable the "Intercept" layer anyway, which it requires.  Also for Windows it goes in the registry and for Linux it goes in a config file -- thus IMO a user-supplied action.  Although xmrig does already poke the registry to reduce the user actions required to enable hugepages so it would be possible.  Unsure if tweaking or creating local config files on Linux that are outside the working directory is a good thing or not, feels bad but so does touching registry for hugepages.  It feels worse repeating how to enable hugepages on Windows hundreds of times in that case, so doing it for them made sense, and there aren't any apparent "costs" to having hugepages permissions.

# Action History
- Created by: iamhumanipromise | 2023-04-20T23:08:30+00:00
