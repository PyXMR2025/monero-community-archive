---
title: can't build file
source_url: https://github.com/xmrig/xmrig/issues/2167
author: andylehti
assignees: []
labels:
- question
created_at: '2021-03-09T22:08:02+00:00'
updated_at: '2021-04-12T14:05:40+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:05:40+00:00'
---

# Original Description
I have multiple programs saying that .h files are missing. Is this not a complete source code?

# Discussion History
## Spudz76 | 2021-03-11T16:50:31+00:00
What error messages?  yes it's complete source I build it multiple times a week

## andylehti | 2021-03-13T05:15:51+00:00
That was my bad. I didn't download the dependencies on this computer. However, now CMAKE is giving me issues. I have updated the path files. I can run CMAKE to compile other programs. It will not work for XMRIG though. I keep getting "No CMAKE_CXX_COMPILER could be found" 

## andylehti | 2021-03-13T05:19:08+00:00
A way around it was opening the CMAKELISTS with Visual Studio, and it finds the CXX compiler, but then I get the error "is not able to compile a simple test program" which is weird because it compiles everything else just fine. Just wondering if you ran into anything of the sort and if you had a solution. 

## xmrig | 2021-03-13T05:21:24+00:00
https://xmrig.com/docs/miner/build/windows

## andylehti | 2021-03-13T05:41:40+00:00
yes, that's the one giving me errors. I am reinstalling VS right now to see if there was an issue with the installation. 

## andylehti | 2021-03-13T06:15:56+00:00
reinstalling fixed the issue

## andylehti | 2021-03-13T06:27:36+00:00
A question though. I built Kawpow, but it only shows me its dependencies like Ethash and Keccak. I guess I am a bit confused as I am not familiar with Kawpow. I am trying to study the algorithm. Can you tell me which file is used to start the Kawpow algorithm, and what main function is called? 

## andylehti | 2021-03-13T06:36:17+00:00
Found it. I didn't realize it built multiple projects. My bad. I am a java/PHP programmer. Just learning C++ lol

## browolf | 2021-03-23T09:02:15+00:00
I've got that error  "No CMAKE_CXX_COMPILER could be found"  using msys.   

## browolf | 2021-03-23T23:17:35+00:00
> I've got that error "No CMAKE_CXX_COMPILER could be found" using msys.

Figured out this happens from just running msys2 exe. 

whereas it works if you run the mingw64 shell which is either a shortcut in the start menu or 
\msys64\msys2_shell.cmd -mingw64

## Spudz76 | 2021-03-26T19:33:51+00:00
Note KawPow does not actually mine in the CPU miner, it is only there to be able to verify results from GPU backends and avoid sending invalids to the pool.

# Action History
- Created by: andylehti | 2021-03-09T22:08:02+00:00
- Closed at: 2021-04-12T14:05:40+00:00
