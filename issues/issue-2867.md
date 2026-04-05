---
title: Not able to utilise CPU for mining in M1
source_url: https://github.com/xmrig/xmrig/issues/2867
author: aldrineeinsteen
assignees: []
labels: []
created_at: '2022-01-16T17:58:44+00:00'
updated_at: '2022-01-20T15:27:14+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
When running on Mac M1, unable to utilise CPU. If CPU is enabled, reports the following:

>  cpu      disabled (no suitable configuration found)

**To Reproduce**
Run the latest xmrig on mac with m1 processor.

**Expected behavior**
Utilise both OpenCL and CPU for mining.

**Required data**
 - Miner log as text or screenshot
 - Config file or command line (without wallets)
 - OS: Mac Book Pro (M1)
 - For GPU related issues: information about GPUs and driver version.



# Discussion History
## Spudz76 | 2022-01-16T19:48:54+00:00
Some algos do not support CPU, like Kawpow doesn't.  What algo are you trying to use?

## aldrineeinsteen | 2022-01-16T21:30:07+00:00
I am using it for XMR, which does support CPU.On 16 Jan 2022 19:49, Tony Butler ***@***.***> wrote:
Some algos do not support CPU, like Kawpow doesn't.  What algo are you trying to use?

—Reply to this email directly, view it on GitHub, or unsubscribe.Triage notifications on the go with GitHub Mobile for iOS or Android.
You are receiving this because you authored the thread.Message ID: ***@***.***>

## SChernykh | 2022-01-17T00:30:28+00:00
> cpu disabled (no suitable configuration found)

This is most likely an error in the config.json. Try to regenerate it using https://xmrig.com/wizard

## aldrineeinsteen | 2022-01-17T08:44:24+00:00
Thank you @SChernykh.
I tried reinitiating the config from the wizard. 

Below is the new error :'( 
```
**[2022-01-17 08:42:11.208]  opencl   GPU #0 compiling...
UNSUPPORTED (log once): buildComputeProgram: cl2Metal failed**
[2022-01-17 08:42:11.366]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram

[2022-01-17 08:42:11.366]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
Compilation failed: 

program_source:1788:1: warning: comparison of integers of different signs: 'uint32_t' (aka 'unsigned int') and 'int'
update_max(latency,(last_memory_op_slot+WORKERS_PER_HASH)/WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1399:56: note: expanded from macro 'update_max'
#define update_max(value, next_value) do { if ((value) < (next_value)) (value) = (next_value); } while (0)
                                                ~~~~~  ^  ~~~~~~~~~~
program_source:1811:1: warning: comparison of integers of different signs: 'int32_t' (aka 'int') and 'unsigned int'
update_max(first_allowed_slot,latency*WORKERS_PER_HASH);
^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
program_source:1399:56: note: expanded from macro 'update_max'
[2022-01-17 08:42:11.366]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2022-01-17 08:42:11.366]  opencl   thread #0 self-test failed
[2022-01-17 08:42:11.366]  opencl   disabled (failed to start threads)
```

Config File:
```json
{
    "autosave": true,
    "cpu": true,
    "opencl": true,
    "cuda": false,
    "pools": [
        {
            "algo": "rx/0",
            "url": "monero.herominers.com:10191",
            "user": "",
            "pass": "MacOs",
            "keepalive": true,
            "tls": true
        }
    ]
}
```

## aldrineeinsteen | 2022-01-17T08:47:14+00:00
I believe the error is 
[2022-01-17 08:42:11.208]  opencl   GPU #0 compiling...
UNSUPPORTED (log once): **buildComputeProgram: cl2Metal failed**
[2022-01-17 08:42:11.366]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram

## SChernykh | 2022-01-17T08:53:02+00:00
This is GPU error. OpenCL support is terrible on Mac.

## aldrineeinsteen | 2022-01-17T08:55:24+00:00
I know, almost close to teary eyes...

Cuda is no longer supported, Open CL is bad. Metal is even more screwed up. Running out of options.

Do we have support for metal inherently or should I snoop around the code? Any suggestions 👍 

## Spudz76 | 2022-01-17T18:29:10+00:00
Well, that and RandomX is pointless on a GPU anyway even if it did work.

## aldrineeinsteen | 2022-01-19T20:38:54+00:00
I tried building the whole code again, Mac has screwed up OpenCL and there is a conversion... "cl2Metal" and this fails.

## Spudz76 | 2022-01-19T23:04:34+00:00
cl2metal has been there for several OS releases it's not (specifically) to blame.

More that OpenCL has been abandoned so it will just keep getting worse as the OS changes, because they aren't making sure OpenCL still works *on everything* when changes occur.  Aside from the problem there always was, it's real picky about code.

## Spudz76 | 2022-01-19T23:13:58+00:00
Also I guess the title should say `GPU` and this would be slightly less confusing.  Since the CPU works fine as far as anyone knows.

## aldrineeinsteen | 2022-01-20T15:27:13+00:00
@Spudz76 Hi Tony, Initially the issue was about CPU configuration not working. Then after refreshing the configuration it got transformed into a GPU issue.

# Action History
- Created by: aldrineeinsteen | 2022-01-16T17:58:44+00:00
