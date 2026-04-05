---
title: runtime error
source_url: https://github.com/xmrig/xmrig/issues/370
author: danjw1
assignees: []
labels:
- bug
created_at: '2018-01-28T13:49:10+00:00'
updated_at: '2018-11-05T12:48:24+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:48:24+00:00'
---

# Original Description
I am seeing this exception quite a bit:
Unhandled exception at 0x00007FF9083E3FB8 in xmrig-nvidia.exe: Microsoft C++ exception: std::runtime_error at memory location 0x000000AFA2DFF6B8. occurred

I am running in Windows 10 x64 Pro version 1709.  The system is a Z77 with a i5-3570k, 16GB of memory Corsair CMZ16GX3M2A1600C10

 If there is any other information that would be useful in fixing this, please ask.

Variable that seems to be causing the problem:
```
-		ctx	0x00000261cdb7ed70 {device_id=0 device_name=0x00000261cdb63100 "GeForce GTX 1060 6GB" device_arch=0x00000261cdb7ed80 {...} ...}	nvid_ctx *
		device_id	0	int
+		device_name	0x00000261cdb63100 "GeForce GTX 1060 6GB"	const char *
+		device_arch	0x00000261cdb7ed80 {6, 1}	int[2]
		device_mpcount	10	int
		device_blocks	30	int
		device_threads	64	int
		device_bfactor	6	int
		device_bsleep	25	int
		device_clockRate	1784500	int
		device_memoryClockRate	4004000	int
		device_pciBusID	2	int
		device_pciDeviceID	0	int
		device_pciDomainID	0	int
+		d_input	0x00000007f4400000 {???}	unsigned int *
		inputlen	76	unsigned int
+		d_result_count	0x00000007f4400200 {???}	unsigned int *
+		d_result_nonce	0x00000007f4400400 {???}	unsigned int *
+		d_long_state	0x0000000703e00000 {???}	unsigned int *
+		d_ctx_state	0x00000007f3e00000 {???}	unsigned int *
+		d_ctx_a	0x00000007f4200000 {???}	unsigned int *
+		d_ctx_b	0x00000007f4207800 {???}	unsigned int *
+		d_ctx_key1	0x00000007f3e5dc00 {???}	unsigned int *
+		d_ctx_key2	0x00000007f3ea8c00 {???}	unsigned int *
+		d_ctx_text	0x00000007f4000000 {???}	unsigned int *
```


Call Stack:
```
 	KernelBase.dll!RaiseException()	Unknown	Non-user code. Symbols loaded.
 	[External Code]		Annotated Frame
>	xmrig-nvidia.exe!cryptonight_extra_cpu_final(nvid_ctx * ctx, unsigned int startNonce, unsigned __int64 target, unsigned int * rescount, unsigned int * resnonce) Line 232	C++	Symbols loaded.
 	xmrig-nvidia.exe!CudaWorker::start() Line 108	C++	Symbols loaded.
 	xmrig-nvidia.exe!Workers::onReady(void * arg) Line 233	C++	Symbols loaded.
 	[External Code]		Annotated Frame
```


# Discussion History
## ondradus | 2018-01-29T06:58:37+00:00
did you compile the build yourself or are you using  release?

## danjw1 | 2018-01-29T14:24:09+00:00
Compiled myself.  The release wouldn't run at all on my system.

I made one change to workers.cpp:
183c183
```
<     for (size_t i = 0; i < count; ++i) {
---
>     for (size_t i = 0; i < 1; ++i) { //change i < count to i < 1 to disable my 560 Ti dan

```
This was to disable the other card I have installed, since it was the cause of the failure.

## danjw1 | 2018-01-31T17:22:17+00:00
I have run without this exception for over a day, which is the longest I have managed, by setting Windows to never turn off the screen.  So, this seems to come from having that enabled.

## danjw1 | 2018-02-04T20:29:19+00:00
I just had this happen again with that setting not changed.  So, it can happen with it on or off, but it is much more rare when off.

## danjw1 | 2018-02-09T17:40:31+00:00
I also saw this when I hibernated my computer for a ~10 minutes. 

# Action History
- Created by: danjw1 | 2018-01-28T13:49:10+00:00
- Closed at: 2018-11-05T12:48:24+00:00
