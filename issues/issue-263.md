---
title: Build fails on AARCH64
source_url: https://github.com/xmrig/xmrig/issues/263
author: gordan-bobic
assignees: []
labels:
- bug
- arm
created_at: '2017-12-13T20:35:54+00:00'
updated_at: '2019-02-03T20:08:35+00:00'
type: issue
status: closed
closed_at: '2019-02-03T20:08:34+00:00'
---

# Original Description
Building on aarch64 fails on CentOS 7 (tested with gcc 4.8.5, gcc 6.3.1).

It looks like the problem is that some SSE2NEON intrinsics aren't defined.

```
$ make
Scanning dependencies of target xmrig
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
[  5%] Building CXX object CMakeFiles/xmrig.dir/src/api/ApiState.cpp.o
[  7%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
[ 10%] Building CXX object CMakeFiles/xmrig.dir/src/App.cpp.o
In file included from /home/mock/xmr/xmrig/src/workers/Workers.h:34:0,
                 from /home/mock/xmr/xmrig/src/App.cpp:43:
/home/mock/xmr/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/mock/xmr/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 12%] Building CXX object CMakeFiles/xmrig.dir/src/Console.cpp.o
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/log/ConsoleLog.cpp.o
[ 17%] Building CXX object CMakeFiles/xmrig.dir/src/log/FileLog.cpp.o
[ 20%] Building CXX object CMakeFiles/xmrig.dir/src/log/Log.cpp.o
[ 22%] Building CXX object CMakeFiles/xmrig.dir/src/Mem.cpp.o
[ 25%] Building CXX object CMakeFiles/xmrig.dir/src/net/Client.cpp.o
In file included from /home/mock/xmr/xmrig/src/net/Client.cpp:44:0:
/home/mock/xmr/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/mock/xmr/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 27%] Building CXX object CMakeFiles/xmrig.dir/src/net/Job.cpp.o
[ 30%] Building CXX object CMakeFiles/xmrig.dir/src/net/Network.cpp.o
In file included from /home/mock/xmr/xmrig/src/workers/Workers.h:34:0,
                 from /home/mock/xmr/xmrig/src/net/Network.cpp:44:
/home/mock/xmr/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/mock/xmr/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 32%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/DonateStrategy.cpp.o
[ 35%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/FailoverStrategy.cpp.o
[ 37%] Building CXX object CMakeFiles/xmrig.dir/src/net/strategies/SinglePoolStrategy.cpp.o
[ 40%] Building CXX object CMakeFiles/xmrig.dir/src/net/SubmitResult.cpp.o
[ 42%] Building CXX object CMakeFiles/xmrig.dir/src/net/Url.cpp.o
[ 45%] Building CXX object CMakeFiles/xmrig.dir/src/Options.cpp.o
[ 47%] Building CXX object CMakeFiles/xmrig.dir/src/Platform.cpp.o
[ 50%] Building CXX object CMakeFiles/xmrig.dir/src/Summary.cpp.o
[ 52%] Building CXX object CMakeFiles/xmrig.dir/src/workers/DoubleWorker.cpp.o
In file included from /home/mock/xmr/xmrig/src/workers/DoubleWorker.h:30:0,
                 from /home/mock/xmr/xmrig/src/workers/DoubleWorker.cpp:29:
/home/mock/xmr/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/mock/xmr/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
/home/mock/xmr/xmrig/src/workers/DoubleWorker.cpp: In member function ‘virtual void DoubleWorker::start()’:
/home/mock/xmr/xmrig/src/workers/DoubleWorker.cpp:90:57: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
             if (*reinterpret_cast<uint64_t*>(m_hash + 24) < m_state->job.target()) {
                                                         ^
/home/mock/xmr/xmrig/src/workers/DoubleWorker.cpp:94:62: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
             if (*reinterpret_cast<uint64_t*>(m_hash + 32 + 24) < m_state->job.target()) {
                                                              ^
[ 55%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Handle.cpp.o
[ 57%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Hashrate.cpp.o
[ 60%] Building CXX object CMakeFiles/xmrig.dir/src/workers/SingleWorker.cpp.o
In file included from /home/mock/xmr/xmrig/src/workers/SingleWorker.h:29:0,
                 from /home/mock/xmr/xmrig/src/workers/SingleWorker.cpp:29:
/home/mock/xmr/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/mock/xmr/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 62%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Worker.cpp.o
[ 65%] Building CXX object CMakeFiles/xmrig.dir/src/workers/Workers.cpp.o
In file included from /home/mock/xmr/xmrig/src/workers/DoubleWorker.h:30:0,
                 from /home/mock/xmr/xmrig/src/workers/Workers.cpp:31:
/home/mock/xmr/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/mock/xmr/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
[ 67%] Building CXX object CMakeFiles/xmrig.dir/src/xmrig.cpp.o
[ 70%] Building CXX object CMakeFiles/xmrig.dir/src/App_unix.cpp.o
[ 72%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_unix.cpp.o
[ 75%] Building CXX object CMakeFiles/xmrig.dir/src/Mem_unix.cpp.o
[ 77%] Building CXX object CMakeFiles/xmrig.dir/src/Platform_unix.cpp.o
[ 80%] Building CXX object CMakeFiles/xmrig.dir/src/Cpu_arm.cpp.o
[ 82%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_keccak.c.o
[ 85%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_groestl.c.o
[ 87%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_blake256.c.o
[ 90%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_jh.c.o
[ 92%] Building C object CMakeFiles/xmrig.dir/src/crypto/c_skein.c.o
[ 95%] Building CXX object CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o
In file included from /home/mock/xmr/xmrig/src/crypto/soft_aes.h:31:0,
                 from /home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:37,
                 from /home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:28:
/home/mock/xmr/xmrig/src/crypto/soft_aes.h: In function ‘__m128i soft_aesenc(__m128i, __m128i)’:
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:95:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x1 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0x55));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:95:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x1 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0x55));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:95:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x1 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0x55));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:95:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x1 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0x55));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:96:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x2 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0xAA));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:96:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x2 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0xAA));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:96:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x2 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0xAA));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:96:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x2 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0xAA));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:97:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x3 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0xFF));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:97:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x3 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0xFF));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:97:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x3 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0xFF));
                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:97:43: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t x3 = _mm_cvtsi128_si32(_mm_shuffle_epi32(in, 0xFF));
                                           ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h: In function ‘__m128i soft_aeskeygenassist(__m128i)’:
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: note: (if you use ‘-fpermissive’, G++ will accept your code, but allowing the use of an undeclared name is deprecated)
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In function ‘void soft_aes_genkey_sub(__m128i*, __m128i*)’:
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: there are no arguments to ‘vdupq_laneq_s32’ that depend on a template parameter, so a declaration of ‘vdupq_laneq_s32’ must be available [-fpermissive]
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
In file included from /home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:28:0:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In function ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*)’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:209:61: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
         *x1 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x1), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:210:61: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
         *x2 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x2), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:211:61: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
         *x3 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x3), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:212:61: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
         *x4 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x4), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:213:61: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
         *x5 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x5), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:214:61: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
         *x6 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x6), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:215:61: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
         *x7 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x7), key));
                                                             ^
In file included from /home/mock/xmr/xmrig/src/crypto/soft_aes.h:31:0,
                 from /home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:37,
                 from /home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:28:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In function ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*)’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:79: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                               ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In function ‘void cryptonight_double_hash(const void*, size_t, void*, cryptonight_ctx*)’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:81: error: there are no arguments to ‘vaeseq_u8’ that depend on a template parameter, so a declaration of ‘vaeseq_u8’ must be available [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
In file included from /home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:35:0:
/home/mock/xmr/xmrig/src/net/JobResult.h: In member function ‘uint64_t JobResult::actualDiff() const’:
/home/mock/xmr/xmrig/src/net/JobResult.h:69:71: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
         return Job::toDiff(reinterpret_cast<const uint64_t*>(result)[3]);
                                                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp: In static member function ‘static bool CryptoNight::hash(const Job&, JobResult&, cryptonight_ctx*)’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:114:59: warning: dereferencing type-punned pointer will break strict-aliasing rules [-Wstrict-aliasing]
     return *reinterpret_cast<uint64_t*>(result.result + 24) < job.target();
                                                           ^
In file included from /home/mock/xmr/xmrig/src/crypto/soft_aes.h:31:0,
                 from /home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:37,
                 from /home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:28:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:79: error: ‘vaeseq_u8’ was not declared in this scope
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                               ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:80: error: ‘vaesmcq_u8’ was not declared in this scope
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void cryptonight_double_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:51:87:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: error: ‘vaeseq_u8’ was not declared in this scope
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:82: error: ‘vaesmcq_u8’ was not declared in this scope
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:81: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: note: ‘vaeseq_u8’ declared here, later in the translation unit
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:82: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:82: note: ‘vaesmcq_u8’ declared here, later in the translation unit
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = true; size_t = long unsigned int]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:57:79:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:79: error: ‘vaeseq_u8’ was not declared in this scope
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                               ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:80: error: ‘vaesmcq_u8’ was not declared in this scope
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void cryptonight_double_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = true; size_t = long unsigned int]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:62:86:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: error: ‘vaeseq_u8’ was not declared in this scope
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:82: error: ‘vaesmcq_u8’ was not declared in this scope
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:81: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: note: ‘vaeseq_u8’ declared here, later in the translation unit
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:82: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:82: note: ‘vaesmcq_u8’ declared here, later in the translation unit
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 262144ul; long unsigned int MEM = 1048576ul; long unsigned int MASK = 1048560ul; bool SOFT_AES = false; size_t = long unsigned int]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:69:84:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:79: error: ‘vaeseq_u8’ was not declared in this scope
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                               ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:80: error: ‘vaesmcq_u8’ was not declared in this scope
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void cryptonight_double_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 262144ul; long unsigned int MEM = 1048576ul; long unsigned int MASK = 1048560ul; bool SOFT_AES = false; size_t = long unsigned int]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:76:91:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: error: ‘vaeseq_u8’ was not declared in this scope
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:82: error: ‘vaesmcq_u8’ was not declared in this scope
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:81: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: note: ‘vaeseq_u8’ declared here, later in the translation unit
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:82: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:82: note: ‘vaesmcq_u8’ declared here, later in the translation unit
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 262144ul; long unsigned int MEM = 1048576ul; long unsigned int MASK = 1048560ul; bool SOFT_AES = true; size_t = long unsigned int]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:82:83:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:79: error: ‘vaeseq_u8’ was not declared in this scope
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                               ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:371:80: error: ‘vaesmcq_u8’ was not declared in this scope
             cx = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void cryptonight_double_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 262144ul; long unsigned int MEM = 1048576ul; long unsigned int MASK = 1048560ul; bool SOFT_AES = true; size_t = long unsigned int]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:87:90:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: error: ‘vaeseq_u8’ was not declared in this scope
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:82: error: ‘vaesmcq_u8’ was not declared in this scope
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:81: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:81: note: ‘vaeseq_u8’ declared here, later in the translation unit
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                 ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:438:82: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
             cx1 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx1, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah1, al1);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:437:82: note: ‘vaesmcq_u8’ declared here, later in the translation unit
             cx0 = vreinterpretq_m128i_u8(vaesmcq_u8(vaeseq_u8(cx0, vdupq_n_u8(0)))) ^ _mm_set_epi64x(ah0, al0);
                                                                                  ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:237:23: note: in definition of macro ‘vreinterpretq_m128i_u8’
  vreinterpretq_s32_u8(x)
                       ^
In file included from /home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:28:0:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:240:108:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: error: ‘vaeseq_u8’ was not declared in this scope
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: error: ‘vaesmcq_u8’ was not declared in this scope
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:209:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x1), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:209:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x1), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:210:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x2), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:210:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x2), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:211:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x3), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:211:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x3), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:212:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x4), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:212:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x4), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:213:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x5), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:213:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x5), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:214:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x6), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:214:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x6), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:215:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x7), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:215:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x7), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void aes_round(__m128i, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = true; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:240:108:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = true; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = true; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:57:79:   required from here
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: error: ‘vaeseq_u8’ was not declared in this scope
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: error: ‘vaesmcq_u8’ was not declared in this scope
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:209:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x1), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:209:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x1 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x1), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:210:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x2), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:210:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x2 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x2), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:211:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x3), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:211:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x3 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x3), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:212:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x4), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:212:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x4 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x4), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:213:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x5), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:213:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x5 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x5), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:214:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x6), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:214:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x6 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x6), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:215:61: error: ‘vaeseq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x7), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:61: note: ‘vaeseq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                             ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:215:62: error: ‘vaesmcq_u8’ was not declared in this scope, and no declarations were found by argument-dependent lookup at the point of instantiation [-fpermissive]
         *x7 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x7), key));
                                                              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:208:62: note: ‘vaesmcq_u8’ declared here, later in the translation unit
         *x0 = vaesmcq_u8(vaeseq_u8(*((uint8x16_t *) x0), key));
                                                              ^
In file included from /home/mock/xmr/xmrig/src/crypto/soft_aes.h:31:0,
                 from /home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:37,
                 from /home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:28:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void soft_aes_genkey_sub(__m128i*, __m128i*) [with unsigned char rcon = 1u; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:175:56:   required from ‘void aes_genkey(const __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:227:81:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void soft_aes_genkey_sub(__m128i*, __m128i*) [with unsigned char rcon = 2u; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:179:56:   required from ‘void aes_genkey(const __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:227:81:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void soft_aes_genkey_sub(__m128i*, __m128i*) [with unsigned char rcon = 4u; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:183:56:   required from ‘void aes_genkey(const __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:227:81:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h: In instantiation of ‘void soft_aes_genkey_sub(__m128i*, __m128i*) [with unsigned char rcon = 8u; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:187:56:   required from ‘void aes_genkey(const __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:227:81:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:157:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xFF); // see PSHUFD, set all elems to 4th elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:161:14: note: in expansion of macro ‘_mm_shuffle_epi32’
     xout1  = _mm_shuffle_epi32(xout1, 0xAA); // see PSHUFD, set all elems to 3rd elem
              ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h: In instantiation of ‘__m128i soft_aeskeygenassist(__m128i) [with unsigned char rcon = 1u; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:156:54:   required from ‘void soft_aes_genkey_sub(__m128i*, __m128i*) [with unsigned char rcon = 1u; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:175:56:   required from ‘void aes_genkey(const __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:227:81:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h: In instantiation of ‘__m128i soft_aeskeygenassist(__m128i) [with unsigned char rcon = 2u; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:156:54:   required from ‘void soft_aes_genkey_sub(__m128i*, __m128i*) [with unsigned char rcon = 2u; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:179:56:   required from ‘void aes_genkey(const __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:227:81:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h: In instantiation of ‘__m128i soft_aeskeygenassist(__m128i) [with unsigned char rcon = 4u; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:156:54:   required from ‘void soft_aes_genkey_sub(__m128i*, __m128i*) [with unsigned char rcon = 4u; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:183:56:   required from ‘void aes_genkey(const __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:227:81:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h: In instantiation of ‘__m128i soft_aeskeygenassist(__m128i) [with unsigned char rcon = 8u; __m128i = __vector(4) __builtin_aarch64_simd_si]’:
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:156:54:   required from ‘void soft_aes_genkey_sub(__m128i*, __m128i*) [with unsigned char rcon = 8u; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:187:56:   required from ‘void aes_genkey(const __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*, __m128i*) [with bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:227:81:   required from ‘void cn_explode_scratchpad(const __m128i*, __m128i*) [with long unsigned int MEM = 2097152ul; bool SOFT_AES = false; __m128i = __vector(4) __builtin_aarch64_simd_si]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight_arm.h:352:88:   required from ‘void cryptonight_hash(const void*, size_t, void*, cryptonight_ctx*) [with long unsigned int ITERATIONS = 524288ul; long unsigned int MEM = 2097152ul; long unsigned int MASK = 2097136ul; bool SOFT_AES = false; size_t = long unsigned int]’
/home/mock/xmr/xmrig/src/crypto/CryptoNight.cpp:44:80:   required from here
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:126:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X1 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0x55)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:802:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(0, 0, 0, 0): ret = _mm_shuffle_epi32_splat((a),0); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:803:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(1, 1, 1, 1): ret = _mm_shuffle_epi32_splat((a),1); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:804:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(2, 2, 2, 2): ret = _mm_shuffle_epi32_splat((a),2); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:776:75: error: ‘vdupq_laneq_s32’ was not declared in this scope
  vreinterpretq_m128i_s32(vdupq_laneq_s32(vreinterpretq_s32_m128i(a), (imm))); \
                                                                           ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:230:3: note: in definition of macro ‘vreinterpretq_m128i_s32’
  (x)
   ^
/home/mock/xmr/xmrig/src/crypto/SSE2NEON.h:805:39: note: in expansion of macro ‘_mm_shuffle_epi32_splat’
   case _MM_SHUFFLE(3, 3, 3, 3): ret = _mm_shuffle_epi32_splat((a),3); break; \
                                       ^
/home/mock/xmr/xmrig/src/crypto/soft_aes.h:127:52: note: in expansion of macro ‘_mm_shuffle_epi32’
     const uint32_t X3 = sub_word(_mm_cvtsi128_si32(_mm_shuffle_epi32(key, 0xFF)));
                                                    ^
make[2]: *** [CMakeFiles/xmrig.dir/src/crypto/CryptoNight.cpp.o] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2

```

# Discussion History
## jgillich | 2017-12-13T23:39:45+00:00
FWIW I just built it successfully using Fedora aarch64 on a Raspberry Pi 3, but running it results in:

```
Illegal instruction (core dumped)
```

## gordan-bobic | 2017-12-13T23:42:11+00:00
Sounds like you got further than me. What gcc version did you use to get it to compile?

## jgillich | 2017-12-13T23:44:47+00:00
GCC 7.2.1, using this Dockerfile:

```
FROM fedora:27

RUN dnf update -y && \
    dnf install -y git cmake gcc gcc-c++ libuv-static libstdc++-static libmicrohttpd-devel

RUN git clone https://github.com/xmrig/xmrig.git && \
    cd xmrig && \
    mkdir build && \
    cd build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release -DUV_LIBRARY=/usr/lib64/libuv.a && \
    make
```

## jgillich | 2017-12-13T23:55:13+00:00
The crash is fixed by the `--av 3` option (#230, #246). Getting a whopping 7 hashes per second, haha.

My guess is that CentOS doesn't support the NEON instructions right now, but I don't really know.

## xmrig | 2017-12-16T12:24:28+00:00
@gordan-bobic please add line `message("${CMAKE_SYSTEM_PROCESSOR}")` to end of [cmake/cpu.cmake](https://github.com/xmrig/xmrig/blob/master/cmake/cpu.cmake) file and show output of cmake.
Probably your CPU not named as `aarch64` in cmake, so right compilations flags not set.
Thank you.

## dan-and | 2017-12-20T12:42:42+00:00
Hi @xmrig,

I will step in: 
I have an ODROID-C2 ( aarch64 , armv8) and saw similar illegal instructions. 
message("${CMAKE_SYSTEM_PROCESSOR}") is reporting: aarch64 

I have nailed it down to following:

_**src/Cpu_arm.cpp**_ 
```
\#   if defined(XMRIG_ARMv8)
    m_flags |= X86_64;
    m_flags |= AES;
\#   endif
``` 

If I remove the `m_flags |= AES;` , I don't see any Illegal instructions. 




## asvos | 2017-12-21T14:16:33+00:00
Had the exact same issue on Centos.
GCC 4.8.5 does not have builtin crypto support (GCC 6 should). Even if you start covering the missing intrinsics, you will find yourself on a dead end because of the missing builtin instructions.
Installing gcc 4.9 (by hand - its the 1st version supposed to have builtin armv8 crypto) solves the problem (my guess is that all later versions should as well so its strange that you could not build with gcc 6).
The makefile uses specifically /usr/bin/c++ .
Just make that your new gcc version is also used by the makefile.
In my case, I kept backups of /usr/bin/cc & /usr/bin/c++ and created symlinks to the /usr/local/bin/c++ and gcc. The cmake then reported the new gcc version and make succeeded with the build.

P.S. To install gcc 4.9 just follow this: https://gist.github.com/craigminihan/b23c06afd9073ec32e0c

## cherso | 2017-12-28T17:24:41+00:00
cortex-a53 archlinux with kernel 4.9.70 and gcc 7.2
The build is clean tho

Program received signal SIGILL, Illegal instruction.
0x00000055555d1f78 in vaeseq_u8 (key=..., data=...)
    at /usr/lib/gcc/aarch64-unknown-linux-gnu/7.2.1/include/arm_neon.h:12428
12428     return __builtin_aarch64_crypto_aesev16qi_uuu (data, key);

I didn't have time to investigate it

## cezar1 | 2018-03-26T08:48:50+00:00
**RPI3 B Version 1.2 archlinux armv8 image**
Linux 4.15.11-1-ARCH #1 SMP Mon Mar 19 18:47:30 MDT 2018 aarch64 GNU/Linux
- on this config.json I have to set av=3 , it will crash with av=0

 * VERSIONS:     XMRig/2.5.2 libuv/1.19.2 gcc/7.2.1
 * HUGE PAGES:   available, disabled
 * CPU:          Unknown (1) x64 AES-NI
 * THREADS:      4, cryptonight, av=3, donate=1%
 * POOL #1:      xmr.pool.minergate.com:45560
 * COMMANDS:     hashrate, pause, resume
[2018-03-26 08:43:01] use pool xmr.pool.minergate.com:45560 78.46.23.253
[2018-03-26 08:43:01] new job from xmr.pool.minergate.com:45560 diff 1063
[2018-03-26 08:43:33] accepted (1/0) diff 1063 (36 ms)
[2018-03-26 08:44:04] speed 2.5s/60s/15m n/a 7.3 n/a H/s max: n/a H/s
[2018-03-26 08:44:37] new job from xmr.pool.minergate.com:45560 diff 500
[2018-03-26 08:45:04] speed 2.5s/60s/15m n/a 7.3 n/a H/s max: n/a H/s

**RPI3 B V1.3 (Plus) stretch lite image**
Linux 4.9.80-v7+ #1098 SMP Fri Mar 9 19:11:42 GMT 2018 armv7l GNU/Linux

 * VERSIONS:     XMRig/2.5.2 libuv/1.9.1 gcc/6.3.0
 * HUGE PAGES:   available, disabled
 * CPU:          Unknown (1) -x64 -AES-NI
 * THREADS:      4, cryptonight, av=3, donate=1%
 * POOL #1:      xmr.pool.minergate.com:45560
 * COMMANDS:     hashrate, pause, resume
[2018-03-26 08:22:27] use pool xmr.pool.minergate.com:45560 46.4.120.155
[2018-03-26 08:22:27] new job from xmr.pool.minergate.com:45560 diff 1063
[2018-03-26 08:22:39] accepted (1/0) diff 1063 (39 ms)
[2018-03-26 08:23:05] accepted (2/0) diff 1063 (40 ms)
[2018-03-26 08:23:30] speed 2.5s/60s/15m n/a 10.3 n/a H/s max: n/a H/s
[2018-03-26 08:23:46] accepted (3/0) diff 1063 (36 ms)
[2018-03-26 08:24:30] speed 2.5s/60s/15m n/a 9.8 n/a H/s max: n/a H/s
[2018-03-26 08:25:21] new job from xmr.pool.minergate.com:45560 diff 500


## xmrig | 2019-02-03T20:08:34+00:00
#749

# Action History
- Created by: gordan-bobic | 2017-12-13T20:35:54+00:00
- Closed at: 2019-02-03T20:08:34+00:00
