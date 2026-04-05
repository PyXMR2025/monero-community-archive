---
title: Question regarding xmrig in VM - failed to find sysfs cpu topology directory
source_url: https://github.com/xmrig/xmrig/issues/3487
author: tcgziarxfhkeqmbjylltc
assignees: []
labels: []
created_at: '2024-05-31T02:43:07+00:00'
updated_at: '2025-06-18T22:12:10+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:12:10+00:00'
---

# Original Description
Hi there, I am running xmrig in a virtual machine. Currently the system fails with error:

hwloc/linux: failed to find sysfs cpu topology directory, " "aborting linux discovery.\\nSegmentation fault\\n

This seems to be caused by "hwloc-ls", with strace, it seems to try to open files under "/sys/devices/system/cpu/cpu0/topology/" but my "cpu/cpu0" folder is empty due to virtualization. (While "lscpu" would give some generic info).

Any thoughts how to skip this hwloc-ls step, and have it use some default value? Given the "topology of cpu" isn't available in this virtual environment?

Thanks and wish all the best!

# Discussion History
## geekwilliams | 2024-05-31T04:18:10+00:00
Can you give more info about what type of virtual environment you're running in?  I've been able to run the general release in a windows and Linux hyper-v vm without issues 

## Spudz76 | 2024-05-31T12:06:39+00:00
That path exists under QEMU, you might be in a container (LXC) rather than real VM?

## SChernykh | 2024-05-31T20:39:55+00:00
> Any thoughts how to skip this hwloc-ls step, and have it use some default value?

Well, you could compile XMRig without HWLoc (add `-DWITH_HWLOC=OFF` to cmake command line). HWLoc will not work properly on your system anyway.

# Action History
- Created by: tcgziarxfhkeqmbjylltc | 2024-05-31T02:43:07+00:00
- Closed at: 2025-06-18T22:12:10+00:00
