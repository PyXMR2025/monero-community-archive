---
title: No longer able to build for macOS (Ventura 13.2)
source_url: https://github.com/monero-project/monero-gui/issues/4117
author: rfpm
assignees: []
labels: []
created_at: '2023-02-12T18:52:23+00:00'
updated_at: '2023-02-26T19:52:03+00:00'
type: issue
status: closed
closed_at: '2023-02-26T19:51:31+00:00'
---

# Original Description
I'm on macOS Ventura 13.2 on an Apple Silicon machine. I am building the GUI myself as the developers still don't provide an Apple Silicon Native ARM build so it has to be done manually.

As of macOS 13.2 the make fails due to errors listed below, all the dependencies, etc are up-to-date, all are installed and functioning as intended. The previous build I made in an older version of macOS Ventura now also no longer launches and will crash when attempting to open the app, below is also the details reported when it crashes.

### **Make Issues**

> CMake Warning (dev) at /opt/homebrew/Cellar/cmake/3.25.2/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:438 (message):
>   The package name passed to `find_package_handle_standard_args` (MiniUPnPc)
>   does not match the name of the calling package (Miniupnpc).  This can lead
>   to problems in calling code that expects `find_package` result variables
>   (e.g., `_FOUND`) to follow a certain pattern.
>
> Call Stack (most recent call first):
>   monero/cmake/FindMiniupnpc.cmake:39 (find_package_handle_standard_args)
>   monero/external/CMakeLists.txt:38 (find_package)
>
> This warning is for project developers.  Use -Wno-dev to suppress it.

---------------------------------------

> CMake Warning (dev) at monero/CMakeLists.txt:1245 (option):
>   Policy CMP0077 is not set: option() honors normal variables.  Run "cmake
>   --help-policy CMP0077" for policy details.  Use the cmake_policy command to
>   set the policy and suppress this warning.
> 
>   For compatibility with older versions of CMake, option is clearing the
>   normal variable 'BUILD_GUI_DEPS'.
> This warning is for project developers.  Use -Wno-dev to suppress it.

---------------------------------------

> [ 24%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-jh.c.o
> /Users/user/monero-gui/monero/src/crypto/hash-extra-jh.c:40:7: warning: unused variable 'r' [-Wunused-variable]
>   int r = jh_hash(HASH_SIZE * 8, data, 8 * length, (uint8_t*)hash);
>       ^
> 1 warning generated.
> [ 24%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hash-extra-skein.c.o
> /Users/user/monero-gui/monero/src/crypto/hash-extra-skein.c:38:7: warning: unused variable 'r' [-Wunused-variable]
>   int r = skein_hash(8 * HASH_SIZE, data, 8 * length, (uint8_t*)hash);
>       ^
> 1 warning generated.
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:517:35: error: expected '(' for function-style cast or type construction
>   std::vector<std::set<std::string> > records;
>                        ~~~~~~~~~~~^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:517:20: error: no member named 'set' in namespace 'std'
>   std::vector<std::set<std::string> > records;
>               ~~~~~^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:517:37: error: expected unqualified-id
>   std::vector<std::set<std::string> > records;
>                                     ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:518:3: error: use of undeclared identifier 'records'
>   records.resize(dns_urls.size());
>   ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:528:41: error: use of undeclared identifier 'records'
>     tpool.submit(&waiter,{n, dns_urls, &records, &avail, &valid}(){
>                                         ^
> [ 24%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hash.c.o
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:531:10: error: use of undeclared identifier 'records'
>          records[n].insert(s);
>          ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:542:7: error: use of undeclared identifier 'records'
>       records[cur_index].clear();
>       ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:547:7: error: use of undeclared identifier 'records'
>       records[cur_index].clear();
>       ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:560:33: error: use of undeclared identifier 'records'
>   for( const auto& record_set : records)
>                                 ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:574:40: error: expected '(' for function-style cast or type construction
>   typedef std::map<std::set<std::string>, uint32_t> map_t;
>                             ~~~~~~~~~~~^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:574:25: error: no member named 'set' in namespace 'std'
>   typedef std::map<std::set<std::string>, uint32_t> map_t;
>                    ~~~~~^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:574:41: error: expected unqualified-id
>   typedef std::map<std::set<std::string>, uint32_t> map_t;
>                                         ^
> [ 24%] Building C object monero/src/crypto/CMakeFiles/obj_cncrypto.dir/hmac-keccak.c.o
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:575:3: error: unknown type name 'map_t'
>   map_t record_count;
>   ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:576:23: error: use of undeclared identifier 'records'
>   for (const auto &e: records)
>                       ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:582:3: error: use of undeclared identifier 'map_t'
>   map_t::const_iterator good_record = record_count.end();
>   ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:582:25: error: use of undeclared identifier 'good_record'; did you mean 'good_records'?
>   map_t::const_iterator good_record = record_count.end();
>                         ^~~~~~~~~~~
>                         good_records
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:512:58: note: 'good_records' declared here
> bool load_txt_records_from_dns(std::vector<std::string> &good_records, const std::vector<std::string> &dns_urls)
>                                                          ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:583:8: error: use of undeclared identifier 'map_t'
>   for (map_t::const_iterator i = record_count.begin(); i != record_count.end(); ++i)
>        ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:585:9: error: use of undeclared identifier 'good_record'; did you mean 'good_records'?
>     if (good_record == record_count.end() || i->second > good_record->second)
>         ^~~~~~~~~~~
>         good_records
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:512:58: note: 'good_records' declared here
> bool load_txt_records_from_dns(std::vector<std::string> &good_records, const std::vector<std::string> &dns_urls)
>                                                          ^
> /Users/user/monero-gui/monero/src/common/dns_utils.cpp:585:58: error: use of undeclared identifier 'good_record'
>     if (good_record == record_count.end() || i->second > good_record->second)
>                                                          ^
> fatal error: too many errors emitted, stopping now [-ferror-limit=]
> 20 errors generated.
> make[3]: *** [monero/src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o] Error 1
> make[3]: *** Waiting for unfinished jobs....
> 

---------------------------------------

> [ 30%] Building CXX object monero/external/randomx/CMakeFiles/randomx.dir/src/instruction.cpp.o
> /Users/user/monero-gui/monero/src/crypto/CryptonightR_JIT.c:17:22: warning: unused variable 'prologue' [-Wunused-const-variable]
> static const uint8_t prologue[] = {
>                      ^
> /Users/user/monero-gui/monero/src/crypto/CryptonightR_JIT.c:36:22: warning: unused variable 'epilogue' [-Wunused-const-variable]
> static const uint8_t epilogue[] = {
>                      ^
> 2 warnings generated.
> 

---------------------------------------

> [ 33%] Linking CXX static library librandomx.a
> [ 33%] Built target randomx
> make[2]: *** [monero/src/common/CMakeFiles/obj_common.dir/all] Error 2
> make[2]: *** Waiting for unfinished jobs....

---------------------------------------

> [ 37%] Building CXX object monero/contrib/epee/src/CMakeFiles/obj_epee.dir/file_io_utils.cpp.o
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:80:7: warning: 'RSA_free' is deprecated [-Wdeprecated-declarations]
>       RSA_free(ptr);
>       ^
> /opt/homebrew/opt/openssl@3/include/openssl/rsa.h:293:1: note: 'RSA_free' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0 void RSA_free(RSA *r);
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:98:7: warning: 'EC_KEY_free' is deprecated [-Wdeprecated-declarations]
>       EC_KEY_free(ptr);
>       ^
> /opt/homebrew/opt/openssl@3/include/openssl/ec.h:1003:1: note: 'EC_KEY_free' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0 void EC_KEY_free(EC_KEY *key);
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:146:19: warning: 'RSA_new' is deprecated [-Wdeprecated-declarations]
>   openssl_rsa rsa{RSA_new()};
>                   ^
> /opt/homebrew/opt/openssl@3/include/openssl/rsa.h:201:1: note: 'RSA_new' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0 RSA *RSA_new(void);
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:162:7: warning: 'RSA_generate_key_ex' is deprecated [-Wdeprecated-declarations]
>   if (RSA_generate_key_ex(rsa.get(), 4096, exponent.get(), nullptr) != 1)
>       ^
> /opt/homebrew/opt/openssl@3/include/openssl/rsa.h:260:1: note: 'RSA_generate_key_ex' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0 int RSA_generate_key_ex(RSA *rsa, int bits, BIGNUM *e,
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:168:7: warning: 'EVP_PKEY_assign' is deprecated [-Wdeprecated-declarations]
>   if (EVP_PKEY_assign_RSA(pkey, rsa.get()) <= 0)
>       ^
> /opt/homebrew/opt/openssl@3/include/openssl/evp.h:496:41: note: expanded from macro 'EVP_PKEY_assign_RSA'
>   define EVP_PKEY_assign_RSA(pkey,rsa) EVP_PKEY_assign((pkey),EVP_PKEY_RSA,\
>                                         ^
> /opt/homebrew/opt/openssl@3/include/openssl/evp.h:1327:1: note: 'EVP_PKEY_assign' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:216:25: warning: 'EC_KEY_new' is deprecated [-Wdeprecated-declarations]
>   openssl_ec_key ec_key{EC_KEY_new()};
>                         ^
> /opt/homebrew/opt/openssl@3/include/openssl/ec.h:968:1: note: 'EC_KEY_new' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0 EC_KEY *EC_KEY_new(void);
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:239:7: warning: 'EC_KEY_set_group' is deprecated [-Wdeprecated-declarations]
>   if (EC_KEY_set_group(ec_key.get(), group) != 1)
>       ^
> /opt/homebrew/opt/openssl@3/include/openssl/ec.h:1042:1: note: 'EC_KEY_set_group' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0 int EC_KEY_set_group(EC_KEY *key, const EC_GROUP *group);
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:244:7: warning: 'EC_KEY_generate_key' is deprecated [-Wdeprecated-declarations]
>   if (EC_KEY_generate_key(ec_key.get()) != 1)
>       ^
> /opt/homebrew/opt/openssl@3/include/openssl/ec.h:1101:1: note: 'EC_KEY_generate_key' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0 int EC_KEY_generate_key(EC_KEY *key);
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> /Users/user/monero-gui/monero/contrib/epee/src/net_ssl.cpp:249:7: warning: 'EVP_PKEY_assign' is deprecated [-Wdeprecated-declarations]
>   if (EVP_PKEY_assign_EC_KEY(pkey, ec_key.get()) <= 0)
>       ^
> /opt/homebrew/opt/openssl@3/include/openssl/evp.h:512:9: note: expanded from macro 'EVP_PKEY_assign_EC_KEY'
>         EVP_PKEY_assign((pkey), EVP_PKEY_EC, (eckey))
>         ^
> /opt/homebrew/opt/openssl@3/include/openssl/evp.h:1327:1: note: 'EVP_PKEY_assign' has been explicitly marked deprecated here
> OSSL_DEPRECATEDIN_3_0
> ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:182:49: note: expanded from macro 'OSSL_DEPRECATEDIN_3_0'
>    define OSSL_DEPRECATEDIN_3_0                OSSL_DEPRECATED(3.0)
>                                                 ^
> /opt/homebrew/opt/openssl@3/include/openssl/macros.h:62:52: note: expanded from macro 'OSSL_DEPRECATED'
>      define OSSL_DEPRECATED(since) __attribute__((deprecated))
>                                                    ^
> [ 37%] Building CXX object monero/contrib/epee/src/CMakeFiles/obj_epee.dir/net_parse_helpers.cpp.o
> [ 37%] Building CXX object monero/contrib/epee/src/CMakeFiles/obj_epee.dir/http_base.cpp.o
> 9 warnings generated.
> [ 37%] Built target obj_epee
> make[1]: *** [all] Error 2
> make: *** [release] Error 2

### At this point the make aborts and fails.

### **This is the crash report from the build of Monero GUI I had made in a previous version of macOS Ventura when attempting to open the app**

> Translated Report (Full Report Below)
> 
> Process:               monero-wallet-gui [38931]
> Path:                  /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
> Identifier:            org.monero-project.monero-wallet-gui
> Version:               0.18.1.2 ()
> Code Type:             ARM-64 (Native)
> Parent Process:        launchd [1]
> User ID:               501
> 
> Date/Time:             2023-02-12 18:07:14.2973 +0000
> OS Version:            macOS 13.2 (22D49)
> Report Version:        12
> Anonymous UUID:        C01AC81F-77BB-91A0-4C6A-7FDB8274CE84
> 
> Sleep/Wake UUID:       715E6813-39BF-46E2-B9D6-ED6B5311EC8D
> 
> Time Awake Since Boot: 120000 seconds
> Time Since Wake:       8417 seconds
> 
> System Integrity Protection: enabled
> 
> Crashed Thread:        0
> 
> Exception Type:        EXC_CRASH (SIGABRT)
> Exception Codes:       0x0000000000000000, 0x0000000000000000
> 
> Termination Reason:    Namespace DYLD, Code 4 Symbol missing
> Symbol not found: __ZN5boost10filesystem4path9append_v3ERKS1_
> Referenced from: <5776890F-0F99-33CB-99C5-D0EFCD2BA9CC> /Applications/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui
> Expected in:     <2893729A-0B2A-3506-B492-63EC517A7BFD> /opt/homebrew/*/libboost_filesystem-mt.dylib
> (terminated at launch; ignore backtrace)
> 
> Thread 0 Crashed:
> 0   dyld                          	       0x1899b7190 __abort_with_payload + 8
> 1   dyld                          	       0x1899c1a00 abort_with_payload_wrapper_internal + 104
> 2   dyld                          	       0x1899c1a34 abort_with_payload + 16
> 3   dyld                          	       0x1899500a4 dyld4::halt(char const*) + 328
> 4   dyld                          	       0x18994d098 dyld4::prepare(dyld4::APIs&, dyld3::MachOAnalyzer const*) + 4204
> 5   dyld                          	       0x18994bdc4 start + 2404
> 
> 
> Thread 0 crashed with ARM Thread State (64-bit):
>     x0: 0x0000000000000006   x1: 0x0000000000000004   x2: 0x000000016bced490   x3: 0x00000000000000ca
>     x4: 0x000000016bced090   x5: 0x0000000000000000   x6: 0x0000000000000000   x7: 0x000000016bceca78
>     x8: 0x0000000000000020   x9: 0x0000000000000009  x10: 0x0000000000000001  x11: 0x000000000000000a
>    x12: 0x0000000000000000  x13: 0x0000000000000033  x14: 0x000000010564969e  x15: 0x0000000000008000
>    x16: 0x0000000000000209  x17: 0x0000000189949344  x18: 0x0000000000000000  x19: 0x0000000000000000
>    x20: 0x000000016bced090  x21: 0x00000000000000ca  x22: 0x000000016bced490  x23: 0x0000000000000004
>    x24: 0x0000000000000006  x25: 0x000000016bcef3a0  x26: 0x0000000000000001  x27: 0x000000010549b770
>    x28: 0x0000000000000000   fp: 0x000000016bced060   lr: 0x00000001899c1a00
>     sp: 0x000000016bced020   pc: 0x00000001899b7190 cpsr: 0x00001000
>    far: 0x000000010551c000  esr: 0x56000080  Address size fault
> 
> Binary Images:
>        0x189946000 -        0x1899d0ba3 dyld (*) <fe8a9d9e-f65d-34ca-942c-175b99c0601b> /usr/lib/dyld
> 
> External Modification Summary:
>   Calls made by other processes targeting this process:
>     task_for_pid: 0
>     thread_create: 0
>     thread_set_state: 0
>   Calls made by this process:
>     task_for_pid: 0
>     thread_create: 0
>     thread_set_state: 0
>   Calls made by all processes on this machine:
>     task_for_pid: 0
>     thread_create: 0
>     thread_set_state: 0
> 
> VM Region Summary:
> ReadOnly portion of Libraries: Total=1.0G resident=0K(0%) swapped_out_or_unallocated=1.0G(100%)
> Writable regions: Total=9504K written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=9504K(100%)
> 
> VIRTUAL   REGION 
> REGION TYPE                        SIZE    COUNT (non-coalesced) 
> ===========                     =======  ======= 
> STACK GUARD                       56.0M        1 
> Stack                             8176K        1 
> VM_ALLOCATE                         16K        1 
> __AUTH                             572K      132 
> __AUTH_CONST                      10.3M      276 
> __DATA                            4508K      301 
> __DATA_CONST                      15.4M      311 
> __DATA_DIRTY                       678K       97 
> __FONT_DATA                        2352        1 
> __LINKEDIT                       781.3M       35 
> __OBJC_CONST                      1161K      107 
> __OBJC_RO                         65.5M        1 
> __OBJC_RW                         1988K        1 
> __TEXT                           244.7M      325 
> dyld private memory                512K        2 
> ===========                     =======  ======= 
> TOTAL                              1.2G     1592 
> 
> 
> 
> Full Report
> 
> {"app_name":"monero-wallet-gui","timestamp":"2023-02-12 18:07:14.00 +0000","app_version":"0.18.1.2","slice_uuid":"5776890f-0f99-33cb-99c5-d0efcd2ba9cc","build_version":"","platform":1,"bundleID":"org.monero-project.monero-wallet-gui","share_with_app_devs":0,"is_first_party":0,"bug_type":"309","os_version":"macOS 13.2 (22D49)","roots_installed":0,"name":"monero-wallet-gui","incident_id":"131DD7E6-D98F-4C5D-BF18-7D2DC470B24F"}
> {
>   "uptime" : 120000,
>   "procRole" : "Default",
>   "version" : 2,
>   "userID" : 501,
>   "deployVersion" : 210,
>   "modelCode" : "MacBookPro18,2",
>   "coalitionID" : 9378,
>   "osVersion" : {
>     "train" : "macOS 13.2",
>     "build" : "22D49",
>     "releaseType" : "User"
>   },
>   "captureTime" : "2023-02-12 18:07:14.2973 +0000",
>   "incident" : "131DD7E6-D98F-4C5D-BF18-7D2DC470B24F",
>   "pid" : 38931,
>   "translated" : false,
>   "cpuType" : "ARM-64",
>   "roots_installed" : 0,
>   "bug_type" : "309",
>   "procLaunch" : "2023-02-12 18:07:14.2029 +0000",
>   "procStartAbsTime" : 2885642806764,
>   "procExitAbsTime" : 2885644479808,
>   "procName" : "monero-wallet-gui",
>   "procPath" : "\/Applications\/monero-wallet-gui.app\/Contents\/MacOS\/monero-wallet-gui",
>   "bundleInfo" : {"CFBundleShortVersionString":"0.18.1.2","CFBundleVersion":"","CFBundleIdentifier":"org.monero-project.monero-wallet-gui"},
>   "storeInfo" : {"deviceIdentifierForVendor":"920D7D45-DB04-5EF1-8DD4-80D2D4149599","thirdParty":true},
>   "parentProc" : "launchd",
>   "parentPid" : 1,
>   "coalitionName" : "org.monero-project.monero-wallet-gui",
>   "crashReporterKey" : "C01AC81F-77BB-91A0-4C6A-7FDB8274CE84",
>   "throttleTimeout" : 2147483647,
>   "wakeTime" : 8417,
>   "sleepWakeUUID" : "715E6813-39BF-46E2-B9D6-ED6B5311EC8D",
>   "sip" : "enabled",
>   "exception" : {"codes":"0x0000000000000000, 0x0000000000000000","rawCodes":[0,0],"type":"EXC_CRASH","signal":"SIGABRT"},
>   "termination" : {"code":4,"flags":518,"namespace":"DYLD","indicator":"Symbol missing","details":["(terminated at launch; ignore backtrace)"],"reasons":["Symbol not found: __ZN5boost10filesystem4path9append_v3ERKS1_","Referenced from: <5776890F-0F99-33CB-99C5-D0EFCD2BA9CC> \/Applications\/monero-wallet-gui.app\/Contents\/MacOS\/monero-wallet-gui","Expected in:     <2893729A-0B2A-3506-B492-63EC517A7BFD> \/opt\/homebrew\/*\/libboost_filesystem-mt.dylib"]},
>   "extMods" : {"caller":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"system":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"targeted":{"thread_create":0,"thread_set_state":0,"task_for_pid":0},"warnings":0},
>   "faultingThread" : 0,
>   "threads" : [{"triggered":true,"id":931174,"threadState":{"x":[{"value":6},{"value":4},{"value":6103684240},{"value":202},{"value":6103683216},{"value":0},{"value":0},{"value":6103681656},{"value":32},{"value":9},{"value":1},{"value":10},{"value":0},{"value":51},{"value":4385445534},{"value":32768},{"value":521},{"value":6603182916,"symbolLocation":392,"symbol":"__simple_bprintf"},{"value":0},{"value":0},{"value":6103683216},{"value":202},{"value":6103684240},{"value":4},{"value":6},{"value":6103692192},{"value":1},{"value":4383684464},{"value":0}],"flavor":"ARM_THREAD_STATE64","lr":{"value":6603676160},"cpsr":{"value":4096},"fp":{"value":6103683168},"sp":{"value":6103683104},"esr":{"value":1442840704,"description":" Address size fault"},"pc":{"value":6603633040,"matchesCrashFrame":1},"far":{"value":4384210944}},"frames":[{"imageOffset":463248,"symbol":"__abort_with_payload","symbolLocation":8,"imageIndex":0},{"imageOffset":506368,"symbol":"abort_with_payload_wrapper_internal","symbolLocation":104,"imageIndex":0},{"imageOffset":506420,"symbol":"abort_with_payload","symbolLocation":16,"imageIndex":0},{"imageOffset":41124,"symbol":"dyld4::halt(char const*)","symbolLocation":328,"imageIndex":0},{"imageOffset":28824,"symbol":"dyld4::prepare(dyld4::APIs&, dyld3::MachOAnalyzer const*)","symbolLocation":4204,"imageIndex":0},{"imageOffset":24004,"symbol":"start","symbolLocation":2404,"imageIndex":0}]}],
>   "usedImages" : [
>   {
>     "source" : "P",
>     "arch" : "arm64e",
>     "base" : 6603169792,
>     "size" : 568228,
>     "uuid" : "fe8a9d9e-f65d-34ca-942c-175b99c0601b",
>     "path" : "\/usr\/lib\/dyld",
>     "name" : "dyld"
>   }
> ],
>   "sharedCache" : {
>   "base" : 6602522624,
>   "size" : 3447406592,
>   "uuid" : "3366b98c-6b8a-3546-8233-dc167320439f"
> },
>   "vmSummary" : "ReadOnly portion of Libraries: Total=1.0G resident=0K(0%) swapped_out_or_unallocated=1.0G(100%)\nWritable regions: Total=9504K written=0K(0%) resident=0K(0%) swapped_out=0K(0%) unallocated=9504K(100%)\n\n                                VIRTUAL   REGION \nREGION TYPE                        SIZE    COUNT (non-coalesced) \n===========                     =======  ======= \nSTACK GUARD                       56.0M        1 \nStack                             8176K        1 \nVM_ALLOCATE                         16K        1 \n__AUTH                             572K      132 \n__AUTH_CONST                      10.3M      276 \n__DATA                            4508K      301 \n__DATA_CONST                      15.4M      311 \n__DATA_DIRTY                       678K       97 \n__FONT_DATA                        2352        1 \n__LINKEDIT                       781.3M       35 \n__OBJC_CONST                      1161K      107 \n__OBJC_RO                         65.5M        1 \n__OBJC_RW                         1988K        1 \n__TEXT                           244.7M      325 \ndyld private memory                512K        2 \n===========                     =======  ======= \nTOTAL                              1.2G     1592 \n",
>   "legacyInfo" : {
>   "threadTriggered" : {
> 
>   }
> },
>   "trialInfo" : {
>   "rollouts" : [
>     {
>       "rolloutId" : "62cdf63ddb3b7109d6d765cc",
>       "factorPackIds" : {
>         "SIRI_UNDERSTANDING_TMDC" : "62cdf6dddb3b7109d6d765cd"
>       },
>       "deploymentId" : 240000007
>     },
>     {
>       "rolloutId" : "60356660bbe37970735c5624",
>       "factorPackIds" : {
>       },
>       "deploymentId" : 240000027
>     }
>   ],
>   "experiments" : [
> 
>   ]
> }
> }
> 
> Model: MacBookPro18,2, BootROM 8419.80.7, proc 10:8:2 processors, 64 GB, SMC 
> Graphics: Apple M1 Max, Apple M1 Max, Built-In
> Display: Color LCD, 3456 x 2234 Retina, Main, MirrorOff, Online
> Display: 27GL850, 1440 x 2560, MirrorOff, Online
> Memory Module: LPDDR5, Hynix
> AirPort: spairport_wireless_card_type_wifi (0x14E4, 0x4387), wl0: Nov 30 2022 02:17:16 version 20.10.965.13.8.7.131 FWID 01-1251c18d
> Bluetooth: Version (null), 0 services, 0 devices, 0 incoming serial ports
> Network Service: USB 10/100/1G/2.5G LAN, Ethernet, en10
> Network Service: Wi-Fi, AirPort, en0
> USB Device: USB31Bus
> USB Device: USB31Bus
> USB Device: USB31Bus
> USB Device: USB 10/100/1G/2.5G LAN
> Thunderbolt Bus: MacBook Pro, Apple Inc.
> Thunderbolt Bus: MacBook Pro, Apple Inc.
> Thunderbolt Bus: MacBook Pro, Apple Inc.

# Discussion History
## selsta | 2023-02-12T18:55:47+00:00
This will be fixed in the next version (should be out in the coming days). In the meantime you can do:

```
cd monero-gui
cd monero
git fetch origin
git reset --hard origin/release-v0.18
cd ..
rm -rf build
MANUAL_SUBMODULES=1 make -j8
```

Note that this will delete your existing build folder for a clean build.

## rfpm | 2023-02-12T19:03:30+00:00
> This will be fixed in the next version (should be out in the coming days). In the meantime you can do:
> 
> ```
> cd monero-gui
> cd monero
> git fetch origin
> git reset --hard origin/release-v0.18
> cd ..
> rm -rf build
> MANUAL_SUBMODULES=1 make -j8
> ```
> 
> Note that this will delete your existing build folder for a clean build.

Woah, extremely quick response, thank you. Thanks for the information, I'll wait for the next version in the coming days and confirm it as working then.

## selsta | 2023-02-26T19:51:31+00:00
Resolved in #4120

Build latest `master` or `v0.18.2.0` tag.

# Action History
- Created by: rfpm | 2023-02-12T18:52:23+00:00
- Closed at: 2023-02-26T19:51:31+00:00
