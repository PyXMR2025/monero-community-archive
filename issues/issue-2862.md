---
title: Support Metal besides OpenCL
source_url: https://github.com/xmrig/xmrig/issues/2862
author: aldrineeinsteen
assignees: []
labels: []
created_at: '2022-01-12T13:49:01+00:00'
updated_at: '2025-11-12T13:46:20+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Since mac has withdrawn OpenCL support, integrate with metal libraries as an alternative.

# Discussion History
## risner | 2022-03-08T23:46:26+00:00
https://developer.apple.com/documentation/metal/migrating_opengl_code_to_metal

This looks new?

Or: https://developer.apple.com/documentation/metal/basic_tasks_and_concepts/performing_calculations_on_a_gpu?preferredLanguage=occ

https://developer.apple.com/metal/cpp/

@Spudz76 Is this already being used in the opencl-to-metal translator?

## Spudz76 | 2022-03-09T05:15:19+00:00
Seems like it's still missing a `double` type but I think the CUDA code already uses FP32 (`float`) because only high end Tesla compute cards have FP64 (`double`).  And Metal seems to have FP32.  So then porting the CUDA kernels may be ironically more straight forward if they are already avoiding use of true `double` types in an optimized way.

If there is some way with debug tools to grab the resulting Metal binary from the cl2metal phase used by Apple OpenCL stack and then decompile that it might be an alternate vector (it must emulate the FP64 somehow such as with two floats and polyfill, maybe that's why it ends up always 33%-50% as fast as the same AMD card on Linux with the AMD stack, but reversed might be able to be hand-optimized).

That top link is for Open*GL* which is not applicable.  Although to give a Metal shader (aka kernel) some array of data you still use "textures" even if they aren't image data.

Also unclear if any of it works from a normal C++ interface or if it requires Swift or Obj-C, but regardless it should be fine using a similar backend plugin styling as the CUDA uses which is probably preferred anyway.

## risner | 2022-03-13T14:43:53+00:00
I tried to look for cl2metal in Xmrig. I’ve got a test Makefile to compile a sample metal in c++. I’ll look at translation of astrobwt.

## risner | 2022-03-13T14:45:05+00:00
@Spudz76 so where exactly is cl2metal being invoked?

## Spudz76 | 2022-03-13T18:51:24+00:00
Automatically behind the OpenCL stack when runtime compilation happens.  Usually not obvious except when it fails to compile and the error comes from `cl2metal`.  So it's never invoked directly by xmrig, but the OS just uses it somewhere hidden behind regular OpenCL calls.

## aldrineeinsteen | 2022-03-14T16:38:33+00:00
But the same runs fine in a non m1 mac. And fails with m1 processor; as they removed support.
I tried building it. But all my debugging was pointing towards not compatible types.

When rubber hits the road; i have end up at https://developer.apple.com/documentation/metal/basic_tasks_and_concepts/performing_calculations_on_a_gpu

However, I am clueless.

program_source:1788:1: warning: comparison of integers of different signs: 'uint32_t' (aka 'unsigned int') and 'int'
update_max(latency,(last_memory_op_slot+WORKERS_PER_HASH)/WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1399:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1811:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,latency*WORKERS_PER_HASH);


## aldrineeinsteen | 2022-03-14T16:56:00+00:00
Found sth strange when trying to debug the execution.

The Following works: `./xmrig --coin=RVN --no-cpu --opencl --opencl-platform=0 -o stratum+tcp://stratum.ravenpool.ninja:3333`

However, `./xmrig --coin=XMR --no-cpu --opencl --opencl-platform=0 -o stratum+tcp://monero.herominers.com:10191` fails.

I am not sure how the algorithm is picked up. Both of them are executed with opencl. 


## risner | 2022-03-14T16:58:56+00:00
> Automatically behind the OpenCL stack when runtime compilation happens. Usually not obvious except when it fails to compile and the error comes from `cl2metal`. So it's never invoked directly by xmrig, but the OS just uses it somewhere hidden behind regular OpenCL calls.

Found it. There is no cl2metal command, but it is running openclc inside the OpenGL framework. I’m experimenting with its —migrate command to see if I can get metal code to compare.

## risner | 2022-03-14T17:00:42+00:00
@aldrineeinsteen OpenCL works for me on M1 max mini, M1 iMac, and M1 Max MacBook pro. Maybe something else is going on? 

## aldrineeinsteen | 2022-03-14T17:03:14+00:00
> @aldrineeinsteen OpenCL works for me on M1 max mini, M1 iMac, and M1 Max MacBook pro. Maybe something else is going on?

@risner It works for kawpow and fails for rx/0.

## aldrineeinsteen | 2022-03-14T17:04:08+00:00
I am unable to figure out where we are selecting rx/0 and where the OpenGL computation is initated.

## risner | 2022-03-14T17:06:11+00:00
I don’t think rx/0 is possible on gpu?


## aldrineeinsteen | 2022-03-14T17:10:58+00:00
Oh, XMR documentation says it can be mined using CPU/GPU.
Monero mining doesn’t require you to purchase an ASIC. Instead, Monero mining can be carried out using your computer’s [CPU](https://en.wikipedia.org/wiki/Central_processing_unit)/[GPU](https://en.wikipedia.org/wiki/Graphics_processing_unit).

Are we selecting the wrong algorithm then?

## Spudz76 | 2022-03-14T18:25:21+00:00
The goal is to have every possible supported algorithm also working with Apple.

Yes most of them work, but the ones that don't require some repair.  And possibly all could be optimized such as by writing native Metal code.

## aldrineeinsteen | 2022-03-24T17:26:01+00:00
I literally stared at the code; I couldn't figure out where cl2metal is being called. I don't see any hook points.

Are we forced to write native code for Apple M1?



## risner | 2022-03-24T17:34:41+00:00
> I literally stared at the code; I couldn't figure out where cl2metal is being called. I don't see any hook points.
> 
> Are we forced to write native code for Apple M1?

The openCL library calls openclc behind the scene. It says cl2metal when it runs but there is no command called that.

Eventually yes, native code will need to be written. The advantage is most code tends to perform better written natively in metal. Possible exception being 64 bit fp.


## regulad | 2025-11-11T21:28:46+00:00
> But the same runs fine in a non m1 mac. And fails with m1 processor; as they removed support. I tried building it. But all my debugging was pointing towards not compatible types.
> 
> When rubber hits the road; i have end up at https://developer.apple.com/documentation/metal/basic_tasks_and_concepts/performing_calculations_on_a_gpu
> 
> However, I am clueless.
> 
> program_source:1788:1: warning: comparison of integers of different signs: 'uint32_t' (aka 'unsigned int') and 'int' update_max(latency,(last_memory_op_slot+WORKERS_PER_HASH)/WORKERS_PER_HASH); ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ program_source:1399:56: note: expanded from macro 'update_max' #define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0) ~~~~~ ^ ~~~~~~~~~~ program_source:1811:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int' update_max(first_allowed_slot,latency*WORKERS_PER_HASH);

I still encounter this issue on an M1 MacBook air.

# Action History
- Created by: aldrineeinsteen | 2022-01-12T13:49:01+00:00
