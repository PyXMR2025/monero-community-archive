---
title: Wrong cache size on i7-3930K with HT off
source_url: https://github.com/xmrig/xmrig/issues/184
author: pinanew
assignees: []
labels:
- bug
created_at: '2017-11-02T13:59:22+00:00'
updated_at: '2017-11-27T00:39:27+00:00'
type: issue
status: closed
closed_at: '2017-11-02T16:46:08+00:00'
---

# Original Description
What I see in Cpu::initCommon():
data.total_logical_cpus == 6, data.num_logical_cpus == 12 --> m_sockets == 0, L2/L3 cache = 0;
If I turn on HT, data.total_logical_cpus == 12, data.num_logical_cpus == 12 --> all OK.

Full struct *data*:
```
+		vendor_str	0x000000b17cbef750 "GenuineIntel"	char[16]
+		brand_str	0x000000b17cbef760 "Intel(R) Core(TM) i7-3930K CPU @ 3.20GHz"	char[64]
		vendor	VENDOR_INTEL (0)	cpu_vendor_t
+		flags	0x000000b17cbef7a4 "\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1"	unsigned char[128]
		family	6	int
		model	13	int
		stepping	7	int
		ext_family	6	int
		ext_model	45	int
		num_cores	6	int
		num_logical_cpus	12	int
		total_logical_cpus	6	int
		l1_data_cache	32	int
		l1_instruction_cache	32	int
		l2_cache	256	int
		l3_cache	12288	int
		l4_cache	-1	int
		l1_assoc	8	int
		l2_assoc	8	int
		l3_assoc	16	int
		l4_assoc	-1	int
		l1_cacheline	64	int
		l2_cacheline	64	int
		l3_cacheline	64	int
		l4_cacheline	-1	int
+		cpu_codename	0x000000b17cbef878 ""	char[64]
		sse_size	128	int
+		detection_hints	0x000000b17cbef8bc ""	unsigned char[16]
+		sgx	{present=0 max_enclave_32bit=0 '\0' max_enclave_64bit=0 '\0' ...}	cpu_sgx_t
```

# Discussion History
## xmrig | 2017-11-02T15:07:13+00:00
I have plans to replace libcpuid to hwloc, it more precise #86
I need check it, actually newer try disable HT.
Thank you.

## xmrig | 2017-11-02T15:14:20+00:00
I confirm it on i7 6700.
Thank you.

## xmrig | 2017-11-02T16:46:08+00:00
Fixed, not so good fix, but working. One more reason now to switch to hwloc.
Close #86 

# Action History
- Created by: pinanew | 2017-11-02T13:59:22+00:00
- Closed at: 2017-11-02T16:46:08+00:00
