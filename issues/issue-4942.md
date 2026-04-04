---
title: wallet files seem to not work on nfs mounted directories
source_url: https://github.com/monero-project/monero/issues/4942
author: ghost
assignees: []
labels: []
created_at: '2018-12-05T04:11:53+00:00'
updated_at: '2019-01-01T14:25:00+00:00'
type: issue
status: closed
closed_at: '2019-01-01T14:25:00+00:00'
---

# Original Description
monero version 0.13.0.4:

Error: failed to load wallet: internal error: "???.keys" is opened by another wallet program.

If the wallet is copied to a local directory, there's no error. If the wallet is copied back to nfs, with a different name, the error occurs again.

# Discussion History
## Jorropo | 2018-12-05T10:42:50+00:00
Please can you do an :
```sh
lsof | grep [name of your key file].keys
```
so we can see where is opened ?

## ghost | 2018-12-05T11:22:37+00:00
nothing, except for some `lsof: no pwd entry for UID 61932` noise.

## moneromooo-monero | 2018-12-05T12:08:32+00:00
Indeed, flock does not work on NFS.
Do you have a "Failed to lock" message in the logs when you run with --log-level 0 ? If so, paste the full line.

## moneromooo-monero | 2018-12-05T12:09:14+00:00
Alternatively, a "Failed to open" message.

## ghost | 2018-12-05T12:13:54+00:00
No such errors with --log-level 0 to 3

## moneromooo-monero | 2018-12-05T12:18:15+00:00
Could it be that you still have a lock file from an earlier run and you got disconnected ?

## moneromooo-monero | 2018-12-05T12:21:52+00:00
Looks like flock should actually work on NFS with Linux >= 2.6.12, which should be common enough. Is the NFS server Linux ? If so, >= 2.6.12 ?

## ghost | 2018-12-05T12:31:39+00:00
It was a newly generated wallet file from seed locally, tested, then transferred to the NFS mounted directory. I don't think it's been opened by another program.

The wallet with the NFS mounted directory is on linux 4.19.2, the NFS server is on 4.18.10.

## ghost | 2018-12-05T12:32:52+00:00
My network is a bit flaky, as my hub just died a few minutes ago. 

## moneromooo-monero | 2018-12-05T12:37:25+00:00
It is very odd you don't get these logs while getting that message. Look again. If still nothing, run with strace (strace -o wallet.strace monero-wallet-cli etc etc), and grep flock.

## ghost | 2018-12-05T12:39:21+00:00
OK, I'll run it later tomorrow.

## ghost | 2018-12-05T12:50:12+00:00
Oh, I was looking at stdout, stupid.

Here's the error in the log:

```
2018-12-05 12:49:02.108     7fb02d1f9000        INFO    msgwriter       src/common/scoped_message_writer.h:102  Monero 'Beryllium Bullet' (v0.13.0.4-unknown)                                                      
2018-12-05 12:49:02.108     7fb02d1f9000        INFO    msgwriter       src/common/scoped_message_writer.h:102  Logging to monero-wallet-cli.log                                                                   
2018-12-05 12:49:02.419     7fb02d1f9000        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4582     !is_keys_file_locked(). THROW EXCEPTION: error::wallet_internal_error                                      
2018-12-05 12:49:02.419     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: tools::error::wallet_internal_error                                                             
2018-12-05 12:49:02.419     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:                                                                                        
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [1] monero-wallet-cli:__cxa_throw+0x10d [0x55d946383bed]                                               
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::wallet_internal_error, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::__cxx11::basic_string<char, std::char_traits<char>,
std::allocator<char> > const&)+0x16c [0x55d94626308c]
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] monero-wallet-cli:tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&)+0x329 [0x55d94622d239]
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [4] monero-wallet-cli:tools::wallet2::make_from_file(boost::program_options::variables_map const&, bool, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<boost::optional<tools::password_container> (char const*, bool)> const&)+0x110 [0x55d94622f1a0]              
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [5] monero-wallet-cli:cryptonote::simple_wallet::open_wallet(boost::program_options::variables_map const&)+0x12c [0x55d9460e915c]
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [6] monero-wallet-cli:cryptonote::simple_wallet::init(boost::program_options::variables_map const&)+0x3b8 [0x55d9460f9c68]
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [7] monero-wallet-cli:main+0x681 [0x55d9460b5401]                                                      
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /nix/store/g2yk54hifqlsjiha3szr4q3ccmdzyrdv-glibc-2.27/lib/libc.so.6:__libc_start_main+0xee [0x7fb029c76b8e]
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172      [9] monero-wallet-cli:_start+0x2a [0x55d9460c37ba]                                                     
2018-12-05 12:49:02.421     7fb02d1f9000        INFO    stacktrace      src/common/stack_trace.cpp:172
2018-12-05 12:49:02.421     7fb02d1f9000        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: failed to load wallet: internal error: "/mnt/ws/wallet/monero/test.keys" is opened by another wallet program
2018-12-05 12:49:02.421     7fb02d1f9000        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:3436  failed to open account                                                                     
2018-12-05 12:49:02.421     7fb02d1f9000        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:8152  Failed to initialize wallet       
```

## moneromooo-monero | 2018-12-05T12:56:13+00:00
OK. I do not understand why you don't get a message prior to that. Apply this patch, and try again, it'll show what code is being run:

<pre>
diff --git a/src/common/util.cpp b/src/common/util.cpp
index 58b0d8210..1804d7aa9 100644
--- a/src/common/util.cpp
+++ b/src/common/util.cpp
@@ -205,6 +205,7 @@ namespace tools
 
   file_locker::file_locker(const std::string &filename)
   {
+MGINFO("trace");
 #ifdef WIN32
     m_fd = INVALID_HANDLE_VALUE;
     std::wstring filename_wide;
@@ -234,29 +235,38 @@ namespace tools
       MERROR("Failed to open " << filename << ": " << std::error_code(GetLastError(), std::system_category()));
     }
 #else
+MGINFO("trace");
     m_fd = open(filename.c_str(), O_RDONLY | O_CREAT | O_CLOEXEC, 0666);
+MGINFO("trace: m_fd " << m_fd);
     if (m_fd != -1)
     {
+MGINFO("trace");
       if (flock(m_fd, LOCK_EX | LOCK_NB) == -1)
       {
+MGINFO("trace");
         MERROR("Failed to lock " << filename << ": " << std::strerror(errno));
         close(m_fd);
+MGINFO("trace");
         m_fd = -1;
       }
     }
     else
     {
+MGINFO("trace");
       MERROR("Failed to open " << filename << ": " << std::strerror(errno));
     }
 #endif
+MGINFO("trace");
   }
   file_locker::~file_locker()
   {
+MGINFO("trace");
     if (locked())
     {
 #ifdef WIN32
       CloseHandle(m_fd);
 #else
+MGINFO("trace");
       close(m_fd);
 #endif
     }
@@ -266,6 +276,7 @@ namespace tools
 #ifdef WIN32
     return m_fd != INVALID_HANDLE_VALUE;
 #else
+MGINFO("trace: m_fd: " << m_fd);
     return m_fd != -1;
 #endif
   }
</pre>

## ghost | 2018-12-05T13:33:15+00:00
Log with the patch:

```
2018-12-05 13:31:41.800     7f0dd0c1d000        INFO    msgwriter       src/common/scoped_message_writer.h:102  Logging to monero-wallet-cli.log                                                                   
2018-12-05 13:31:42.644     7f0dd0c1d000        INFO    global  src/common/util.cpp:208 trace
2018-12-05 13:31:42.644     7f0dd0c1d000        INFO    global  src/common/util.cpp:238 trace
2018-12-05 13:31:42.645     7f0dd0c1d000        INFO    global  src/common/util.cpp:240 trace: m_fd 10
2018-12-05 13:31:42.645     7f0dd0c1d000        INFO    global  src/common/util.cpp:243 trace
2018-12-05 13:31:42.645     7f0dd0c1d000        INFO    global  src/common/util.cpp:246 trace
2018-12-05 13:31:42.646     7f0dd0c1d000        INFO    global  src/common/util.cpp:249 trace
2018-12-05 13:31:42.646     7f0dd0c1d000        INFO    global  src/common/util.cpp:259 trace
2018-12-05 13:31:42.646     7f0dd0c1d000        INFO    global  src/common/util.cpp:279 trace: m_fd: -1
2018-12-05 13:31:42.646     7f0dd0c1d000        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4582     !is_keys_file_locked(). THROW EXCEPTION: error::wallet_internal_error                                      
2018-12-05 13:31:42.646     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: tools::error::wallet_internal_error                                                             
2018-12-05 13:31:42.646     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:                                                                                        
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [1] monero-wallet-cli:__cxa_throw+0x10d [0x562937f686cd]                                               
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::wallet_internal_error, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::__cxx11::basic_string<char, std::char_traits<char>,
std::allocator<char> > const&)+0x16c [0x562937e4709c]
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] monero-wallet-cli:tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&)+0x329 [0x562937e11249]
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [4] monero-wallet-cli:tools::wallet2::make_from_file(boost::program_options::variables_map const&, bool, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<boost::optional<tools::password_container> (char const*, bool)> const&)+0x110 [0x562937e131b0]              
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [5] monero-wallet-cli:cryptonote::simple_wallet::open_wallet(boost::program_options::variables_map const&)+0x12c [0x562937ccd16c]
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [6] monero-wallet-cli:cryptonote::simple_wallet::init(boost::program_options::variables_map const&)+0x3b8 [0x562937cddc78]
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [7] monero-wallet-cli:main+0x681 [0x562937c99411]                                                      
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /nix/store/g2yk54hifqlsjiha3szr4q3ccmdzyrdv-glibc-2.27/lib/libc.so.6:__libc_start_main+0xee [0x7f0dcd69ab8e]
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172      [9] monero-wallet-cli:_start+0x2a [0x562937ca77ca]                                                     
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    stacktrace      src/common/stack_trace.cpp:172
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    global  src/common/util.cpp:263 trace
2018-12-05 13:31:42.648     7f0dd0c1d000        INFO    global  src/common/util.cpp:279 trace: m_fd: -1
2018-12-05 13:31:42.648     7f0dd0c1d000        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: failed to load wallet: internal error: "/mnt/ws/wallet/monero/test.keys" is opened by another wallet program
2018-12-05 13:31:42.648     7f0dd0c1d000        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:3436  failed to open account                                                                     
2018-12-05 13:31:42.648     7f0dd0c1d000        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:8152  Failed to initialize wallet   
```

## moneromooo-monero | 2018-12-05T13:39:34+00:00
The logs were sent to the wrong category, that's why they didn't show up. Try with this:
<pre>
diff --git a/src/common/util.cpp b/src/common/util.cpp
index 58b0d8210..860b794fa 100644
--- a/src/common/util.cpp
+++ b/src/common/util.cpp
@@ -81,6 +81,9 @@ using namespace epee;
 #include <boost/asio.hpp>
 #include <openssl/sha.h>
 
+#undef MONERO_DEFAULT_LOG_CATEGORY
+#define MONERO_DEFAULT_LOG_CATEGORY "util"
+
 namespace tools
 {
   std::function<void(int)> signal_handler::m_handler;
</pre>

## ghost | 2018-12-05T14:05:20+00:00
log with the new patch:

```
2018-12-05 14:04:33.373     7f02847e6000        INFO    msgwriter       src/common/scoped_message_writer.h:102  Monero 'Beryllium Bullet' (v0.13.0.4-unknown)                                                      
2018-12-05 14:04:33.373     7f02847e6000        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:207  Setting log level = 1                                                                                      
2018-12-05 14:04:33.373     7f02847e6000        INFO    wallet.wallet2  src/wallet/wallet_args.cpp:210  Logging to: monero-wallet-cli.log                                                                          
2018-12-05 14:04:33.373     7f02847e6000        INFO    msgwriter       src/common/scoped_message_writer.h:102  Logging to monero-wallet-cli.log                                                                   
2018-12-05 14:04:36.389     7f02847e6000        INFO    wallet.wallet2  src/wallet/wallet2.cpp:300      Daemon is local, assuming trusted                                                                          
2018-12-05 14:04:36.389     7f02847e6000        INFO    wallet.wallet2  src/wallet/wallet2.cpp:6307     ringdb path set to /home/fuwa/.shared-ringdb                                                            
2018-12-05 14:04:36.405     7f02847e6000        INFO    global  src/common/util.cpp:211 trace
2018-12-05 14:04:36.405     7f02847e6000        INFO    global  src/common/util.cpp:241 trace
2018-12-05 14:04:36.406     7f02847e6000        INFO    global  src/common/util.cpp:243 trace: m_fd 10
2018-12-05 14:04:36.406     7f02847e6000        INFO    global  src/common/util.cpp:246 trace
2018-12-05 14:04:36.406     7f02847e6000        INFO    global  src/common/util.cpp:249 trace
2018-12-05 14:04:36.406     7f02847e6000        ERROR   util    src/common/util.cpp:250 Failed to lock /mnt/ws/wallet/monero/test.keys: Bad file descriptor                                                        
2018-12-05 14:04:36.406     7f02847e6000        INFO    global  src/common/util.cpp:252 trace
2018-12-05 14:04:36.406     7f02847e6000        INFO    global  src/common/util.cpp:262 trace
2018-12-05 14:04:36.406     7f02847e6000        INFO    global  src/common/util.cpp:282 trace: m_fd: -1
2018-12-05 14:04:36.406     7f02847e6000        ERROR   wallet.wallet2  src/wallet/wallet2.cpp:4582     !is_keys_file_locked(). THROW EXCEPTION: error::wallet_internal_error                                      
2018-12-05 14:04:36.406     7f02847e6000        WARN    net.http        src/wallet/wallet_errors.h:814  /build/monero-8a5b134/src/wallet/wallet2.cpp:4582:N5tools5error21wallet_internal_errorE: internal error: "/mnt/ws/wallet/monero/test.keys" is opened by another wallet program
2018-12-05 14:04:36.406     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: tools::error::wallet_internal_error                                                             
2018-12-05 14:04:36.406     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:134  Unwound call stack:                                                                                        
2018-12-05 14:04:36.407     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [1] monero-wallet-cli:__cxa_throw+0x10d [0x55ac8659f6cd]                                               
2018-12-05 14:04:36.407     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [2] monero-wallet-cli:void tools::error::throw_wallet_ex<tools::error::wallet_internal_error, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&&, std::__cxx11::basic_string<char, std::char_traits<char>,
std::allocator<char> > const&)+0x16c [0x55ac8647e09c]
2018-12-05 14:04:36.407     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [3] monero-wallet-cli:tools::wallet2::load(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&)+0x329 [0x55ac86448249]
2018-12-05 14:04:36.408     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [4] monero-wallet-cli:tools::wallet2::make_from_file(boost::program_options::variables_map const&, bool, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::function<boost::optional<tools::password_container> (char const*, bool)> const&)+0x110 [0x55ac8644a1b0]              
2018-12-05 14:04:36.408     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [5] monero-wallet-cli:cryptonote::simple_wallet::open_wallet(boost::program_options::variables_map const&)+0x12c [0x55ac8630416c]
2018-12-05 14:04:36.408     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [6] monero-wallet-cli:cryptonote::simple_wallet::init(boost::program_options::variables_map const&)+0x3b8 [0x55ac86314c78]
2018-12-05 14:04:36.408     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [7] monero-wallet-cli:main+0x681 [0x55ac862d0411]                                                      
2018-12-05 14:04:36.408     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [8] /nix/store/g2yk54hifqlsjiha3szr4q3ccmdzyrdv-glibc-2.27/lib/libc.so.6:__libc_start_main+0xee [0x7f0281263b8e]
2018-12-05 14:04:36.408     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172      [9] monero-wallet-cli:_start+0x2a [0x55ac862de7ca]                                                     
2018-12-05 14:04:36.408     7f02847e6000        INFO    stacktrace      src/common/stack_trace.cpp:172
2018-12-05 14:04:36.408     7f02847e6000        INFO    global  src/common/util.cpp:266 trace
2018-12-05 14:04:36.408     7f02847e6000        INFO    global  src/common/util.cpp:282 trace: m_fd: -1
2018-12-05 14:04:36.408     7f02847e6000        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: failed to load wallet: internal error: "/mnt/ws/wallet/monero/test.keys" is opened by another wallet program
2018-12-05 14:04:36.408     7f02847e6000        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:3436  failed to open account                                                                     
2018-12-05 14:04:36.408     7f02847e6000        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:8152  Failed to initialize wallet    
```

## moneromooo-monero | 2018-12-05T14:54:55+00:00
https://github.com/monero-project/monero/pull/4944 should fix it.

## ghost | 2018-12-06T05:10:53+00:00
Yes, that fixed it.

## moneromooo-monero | 2019-01-01T14:09:42+00:00
+resolved

# Action History
- Created by: ghost | 2018-12-05T04:11:53+00:00
- Closed at: 2019-01-01T14:25:00+00:00
