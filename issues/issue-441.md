---
title: The CryptoNight init() function should use the same memory allocation functions
  as the main code
source_url: https://github.com/xmrig/xmrig/issues/441
author: ehoffman2
assignees: []
labels: []
created_at: '2018-03-12T11:54:48+00:00'
updated_at: '2018-11-05T12:57:44+00:00'
type: issue
status: closed
closed_at: '2018-11-05T12:57:44+00:00'
---

# Original Description
Prior to doing the run, there is a self-test during initialization of the CryptoNight class.

The CryptoNight::selfTest() function does a simple _mm_malloc() for it's scratchpad, and run one round of hash to determine if the setup is sane.

However, the main code does initialize the scratchpad memory using the Mem::allocate() function, which will try to allocate memory using huge pages, and fallback to a simple _mm_alloc() if that fails.

I know that the initial point of the selfTest was more to verify if the specified algorithm (mainly the use of hardware AES or not) is correct for the target CPU, but I think the other parameters should stay the same between the selfTest and the main run.

For example, maybe there could be an issue with the memory allocated with Mem::allocate(), which would not be detected with the selfTest.  But more importantly, this does decentralize the memory allocation.  For example, if one would wish for some reason to customize the memory allocation, maybe to use other attributes, such as DMA-accessible memory, or non-cacheable memory (for whatever reason/project someone might want/need), then the selfTest() function would not be in measure to detect any issue.

Regards,
Eric


# Discussion History
## xmrig | 2018-03-12T12:14:47+00:00
Self test primary used to verify hash implementation is correct, not contains programmer error or not ruined by compiler optimization int that case `_mm_alloc()` is enough. Self test not used for detect AES.
Thank you.

## ehoffman2 | 2018-03-12T21:38:18+00:00
Sorry, it's just a question of point of view...  Yes, you are right, there are no bugs in the current implementation.  It makes no difference between the different memory allocation for the current implementation, as the point is just to verify that the selected algorithm is correct for the implementation (for example, if the user force HW AES and the platform does not support it).  I do know that it's not used as a detection code.

However, my point was that apart from ensuring that the platform does support the selected algorithm, there may be other points which may (for whatever reason) make the system behave differently if the memory allocation is different (although I do agree that it's more for consistency and good measure for now).  I don't know, maybe the user system has a bug with locked memory, which does not occur with normal memory.  The point is not figuring out why this could occur, but just to illustrate that when the selfTest function is called, we are basically asking it "Are you OK with this setting?".  If after that, we don't run with the same settings, then there may be things that the selfTest function simply could not be able to detect.

I know, it's all good measures, but imagine someone doing a hardware-assisted cryptoNight (FPGA or other hardware accelerator for example), and for that, the memory need to be allocated at a specific region (maybe in a mapped memory segment build from internal FPGA resources), with a specific address range and flags.  Then the logical place to arrange for this memory allocation would be in Mem::allocate().  However, if the selfTest() on it's side just decide to bypass the Mem::allocate() function, and allocate from the main DRAM, then selfTest() would not be able to get proper result from the hardware assisted crypto (which would require memory allocated from it's internals).

That's just one scenario, although a very plausible one, if one would port xmrig for the latest FPGA (with plenty of internal RAM and integrated ARM processor).

Best regards,
Eric


## xmrig | 2018-03-13T14:09:19+00:00
Self test can be executed on each miner thread, with exactly same memory which will be used later, right, it may be reasonable. About FPGA, I not sure, but I think will be need change a lot of things and self test will be smallest piece.
Thank you.

# Action History
- Created by: ehoffman2 | 2018-03-12T11:54:48+00:00
- Closed at: 2018-11-05T12:57:44+00:00
