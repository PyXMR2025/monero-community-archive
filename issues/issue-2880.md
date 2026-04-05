---
title: OpenCL GPU error with MacOS
source_url: https://github.com/xmrig/xmrig/issues/2880
author: ahamel25
assignees: []
labels: []
created_at: '2022-01-20T12:54:11+00:00'
updated_at: '2022-04-10T04:43:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've tried many config and I always get back to this type of error. 

Using a macbook pro with an egpu AMD Radeon 580.  I had a similar issue with an ubutntu/hiveos build with a 1066 card

I used the basic config.json and the apps has made it's own version.

[2022-01-20 07:43:29.451]  opencl   GPU #1 compiling...
[2022-01-20 07:43:29.489]  opencl   GPU #1 compilation completed (38 ms)
[2022-01-20 07:43:29.512]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-01-20 07:43:29.527]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-01-20 07:43:29.529]  opencl   thread #2 failed with error CL_INVALID_PROGRAM
[2022-01-20 07:43:29.529]  opencl   GPU #1 compiling...
[2022-01-20 07:43:29.556]  opencl   thread #2 self-test failed
[2022-01-20 07:43:29.587]  opencl   GPU #1 compilation completed (57 ms)
[2022-01-20 07:43:29.587]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-01-20 07:43:29.587]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-01-20 07:43:29.587]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2022-01-20 07:43:29.589]  opencl   thread #1 self-test failed
[2022-01-20 07:43:29.590]  opencl   GPU #2 compiling...
[2022-01-20 07:43:29.596]  opencl   GPU #2 compilation completed (6 ms)
[2022-01-20 07:43:29.596]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-01-20 07:43:29.596]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-01-20 07:43:29.596]  opencl   thread #4 failed with error CL_INVALID_PROGRAM
[2022-01-20 07:43:29.597]  opencl   GPU #2 compiling...
[2022-01-20 07:43:29.598]  opencl   thread #4 self-test failed
[2022-01-20 07:43:29.602]  opencl   GPU #2 compilation completed (5 ms)
[2022-01-20 07:43:29.603]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-01-20 07:43:29.603]  opencl   error CL_INVALID_VALUE when calling clGetProgramInfo
[2022-01-20 07:43:29.603]  opencl   thread #3 failed with error CL_INVALID_PROGRAM
[2022-01-20 07:43:29.605]  opencl   GPU #0 compiling...
[2022-01-20 07:43:29.606]  opencl   thread #3 self-test failed
[2022-01-20 07:43:29.608]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:820:6: warning: no previous prototype for function 'get_byte32'
uint get_byte32(uint a,uint start_bit) { return (a>>start_bit)&0xFF; }
     ^
<program source>:1072:7: warning: no previous prototype for function 'rotr64'
ulong rotr64(ulong a,ulong shift) { return rotate(a,64-shift); }
      ^
<program source>:1096:6: warning: no previous prototype for function 'blake2b_512_process_single_block'
void blake2b_512_process_single_block(ulong *h,const ulong* m,uint blockTemplateSize)
     ^
<program source>:1157:6: warning: no previous prototype for function 'blake2b_512_process_double_block_32'
void blake2b_512_process_double_block_name(ulong *out,ulong* m,__global const ulong* in)
     ^
<program source>:1155:47: note: expanded from macro 'blake2b_512_process_double_block_name'
#define blake2b_512_process_double_block_name blake2b_512_process_double_block_32
                                              ^
<program source>:1234:6: warning: no previous prototype for function 'blake2b_512_process_double_block_64'
[2022-01-20 07:43:29.608]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2022-01-20 07:43:29.610]  opencl   thread #0 self-test failed
[2022-01-20 07:43:29.610]  opencl   disabled (failed to start threads)


# Discussion History
## hilga007 | 2022-01-21T04:00:36+00:00
How did you compile the miner? My discovery was that on everything from an Intel iGPU to Radeon GPU to M1 SOC, OpenCL performance was best with compiling using Xterm and having the latest [xQuartz](https://www.xquartz.org/) and [OpenCL Headers](https://github.com/KhronosGroup/OpenCL-Headers) installed. 

So the steps essentially for getting a more successful build have been: 


1) Install Homebrew (from HBrew page linked in Step 2):  `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`)
2) Install *all* the deps listed on the [Xmrig Rig macOS build page] as they will come in handy anyway + an extra: (https://xmrig.com/docs/miner/build/macos) so `brew install cmake libuv openssl hwloc wget automake libtool autoconf mesa`
3) Install [xQuartz](https://www.xquartz.org/)
4) Open xterm via Terminal with `xterm`
5) Install generic [OpenCL Headers](https://github.com/KhronosGroup/OpenCL-Headers) so `git clone https://github.com/KhronosGroup/OpenCL-Headers && cd OpenCL-Headers && mkdir build && cd build && cmake .. && sudo make install`
6) Log out then log back in. (Easiest. Or I think `exec zsh` *might* work, or Option+Quitting and re-launching your xterm/X11 session)
7) Follow the rest of the [advanced build guide](https://xmrig.com/docs/miner/build/macos), including building hwloc anyway haha. (Might need it lataz, I dunno. anyway.)
8) Boom XMRIG without worryin' about OpenCL headers, or not finding devices, etc. (This actually works on an old iMac 2009 with Core 2 Duo and a Radeon 2400 XT 256MB, and it sees the OpenCL device. That being said 256MB is not enough to mine with) 

With this strat I've had great success with OpenCL mining on Intel iGPU, Radeon dGPU, and Apple Silicon integrated GPU on macOS 10.15 through 12.1

Notice: Take this with a grain of salt. I don't know *why* it seems to work "better": but it does. (Maybe something with it being through the X11 windowing system with direct compute calls vs. going through whatever Apple's compositor and layers and wrappers and whatever are called??)

That being said: for compiling only. Running the program via sudo ./xterm in a normal terminal is fine for me with no noticeable difference in hash rate. Method of compiling, not execution is the only way I notice a difference in hashing power. 

(I just am an xmrig user, sharin' my troubleshooting steps for the same issues you are mentioning) 

## ahamel25 | 2022-01-21T20:28:27+00:00
I got almost there.  I got this error

[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o
In file included from /Users/user/xmrig/src/backend/opencl/kernels/rx/HashAesKernel.cpp:27:
In file included from /Users/user/xmrig/src/backend/opencl/wrappers/OclLib.h:26:
In file included from /Users/user/xmrig/src/3rdparty/cl.h:30:
/usr/local/include/OpenCL/cl.h:1864:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_mem CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1864:65: error: expected ';' after top level declarator
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_mem CL_API_CALL
                                                                ^
                                                                ;
/usr/local/include/OpenCL/cl.h:1874:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_mem CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1874:65: error: expected ';' after top level declarator
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_mem CL_API_CALL
                                                                ^
                                                                ;
/usr/local/include/OpenCL/cl.h:1886:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1886:65: error: expected ';' after top level declarator
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL
                                                                ^
                                                                ;
/usr/local/include/OpenCL/cl.h:1890:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1890:65: error: expected ';' after top level declarator
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL
                                                                ^
                                                                ;
/usr/local/include/OpenCL/cl.h:1895:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1895:65: error: expected ';' after top level declarator
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL
                                                                ^
                                                                ;
/usr/local/include/OpenCL/cl.h:1898:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1898:65: error: expected ';' after top level declarator
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL
                                                                ^
                                                                ;
/usr/local/include/OpenCL/cl.h:1901:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED void * CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1902:55: error: expected function body after function declarator
clGetExtensionFunctionAddress(const char * func_name) CL_API_SUFFIX__VERSION_1_1_DEPRECATED;
                                                      ^
/usr/local/include/OpenCL/cl.h:1905:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_2_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_command_queue CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1905:75: error: expected ';' after top level declarator
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_command_queue CL_API_CALL
                                                                          ^
                                                                          ;
/usr/local/include/OpenCL/cl.h:1911:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_2_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_sampler CL_API_CALL
                    ^
/usr/local/include/OpenCL/cl.h:1911:69: error: expected ';' after top level declarator
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_sampler CL_API_CALL
                                                                    ^
                                                                    ;
/usr/local/include/OpenCL/cl.h:1918:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_2_DEPRECATED'
extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_int CL_API_CALL
                    ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
[ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o
20 errors generated.
make[2]: *** [CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2


## varenc | 2022-01-29T21:20:44+00:00
I'm not an xmrig user, but I get the same OpenCL `CL_INVALID_PROGRAM` errors and think it's related to eGPU usage on a Macbook Pro with an integrated and discrete graphics card.  Adding the 3rd eGPU causes issues.

As far as I can tell, when you plug an eGPU into the system OpenCL will get into a busted state and nothing requiring it will work properly.  Apple has deprecated OpenCL in favor of Metal so this makes some sense.  Restarting and not plugging in the eGPU and things work fine, albeit no eGPU.  Or if you leave the eGPU in the system and fully reboot with the eGPU plugged in that also often fixes it for awhile, though it comes back.  I haven't found anyway to fix things besides a reboot.  (Logout/Login might work though haven't tried it)

## lyons88 | 2022-03-31T21:20:20+00:00
> I got almost there. I got this error
> 
> [ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/Json.cpp.o In file included from /Users/user/xmrig/src/backend/opencl/kernels/rx/HashAesKernel.cpp:27: In file included from /Users/user/xmrig/src/backend/opencl/wrappers/OclLib.h:26: In file included from /Users/user/xmrig/src/3rdparty/cl.h:30: /usr/local/include/OpenCL/cl.h:1864:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_mem CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1864:65: error: expected ';' after top level declarator extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_mem CL_API_CALL ^ ; /usr/local/include/OpenCL/cl.h:1874:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_mem CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1874:65: error: expected ';' after top level declarator extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_mem CL_API_CALL ^ ; /usr/local/include/OpenCL/cl.h:1886:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1886:65: error: expected ';' after top level declarator extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL ^ ; /usr/local/include/OpenCL/cl.h:1890:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1890:65: error: expected ';' after top level declarator extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL ^ ; /usr/local/include/OpenCL/cl.h:1895:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1895:65: error: expected ';' after top level declarator extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL ^ ; /usr/local/include/OpenCL/cl.h:1898:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1898:65: error: expected ';' after top level declarator extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED cl_int CL_API_CALL ^ ; /usr/local/include/OpenCL/cl.h:1901:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_1_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_1_DEPRECATED void * CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1902:55: error: expected function body after function declarator clGetExtensionFunctionAddress(const char * func_name) CL_API_SUFFIX__VERSION_1_1_DEPRECATED; ^ /usr/local/include/OpenCL/cl.h:1905:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_2_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_command_queue CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1905:75: error: expected ';' after top level declarator extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_command_queue CL_API_CALL ^ ; /usr/local/include/OpenCL/cl.h:1911:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_2_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_sampler CL_API_CALL ^ /usr/local/include/OpenCL/cl.h:1911:69: error: expected ';' after top level declarator extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_sampler CL_API_CALL ^ ; /usr/local/include/OpenCL/cl.h:1918:21: error: unknown type name 'CL_API_PREFIX__VERSION_1_2_DEPRECATED' extern CL_API_ENTRY CL_API_PREFIX__VERSION_1_2_DEPRECATED cl_int CL_API_CALL ^ fatal error: too many errors emitted, stopping now [-ferror-limit=] [ 18%] Building CXX object CMakeFiles/xmrig.dir/src/base/io/json/JsonChain.cpp.o 20 errors generated. make[2]: *** [CMakeFiles/xmrig.dir/src/backend/opencl/kernels/rx/HashAesKernel.cpp.o] Error 1 make[2]: *** Waiting for unfinished jobs.... make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2 make: *** [all] Error 2

You ever figure this out?

I have the same errors trying the advanced build and the rest of the guide posted by hilga007

## riegersan | 2022-04-09T20:36:10+00:00
I've got the exact same error :/

## Spudz76 | 2022-04-10T04:43:21+00:00
You could try cmake option `-DWITH_OPENCL_VERSION=120` to force OpenCL 1.2 which is all that Apple supports.

The CMake logic "should" always force that on Apple but maybe it doesn't work properly.  Default `WITH_OPENCL_VERSION` is 200 (OpenCL 2.0) otherwise but again "should" be ignored if Apple OS.

Other than that it appears to be using the system OpenCL headers (`/usr/local/include/OpenCL/...`) instead of the bundled OpenCL headers.  The Apple headers don't have the switchable-version capabilities the bundled headers (from Khronos, the people who oversee OpenCL) and then they don't work right.  But I think it's finding the system headers first because of the include path order, where the bundled includes are not looked for if the system has some of the same name.

# Action History
- Created by: ahamel25 | 2022-01-20T12:54:11+00:00
