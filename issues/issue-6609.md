---
title: 'build broken with boost 1.58: no member named ''placeholders'' in namespace
  ''boost'''
source_url: https://github.com/monero-project/monero/issues/6609
author: m2049r
assignees: []
labels: []
created_at: '2020-05-31T12:42:32+00:00'
updated_at: '2020-06-02T07:07:14+00:00'
type: issue
status: closed
closed_at: '2020-06-02T07:07:14+00:00'
---

# Original Description
#6532 breaks build with boost 1.58:

```
/monero/src/checkpoints/checkpoints.cpp:138:103: error: no member named 'placeholders' in namespace
      'boost'
                         ( boost::bind(&std::map< uint64_t, crypto::hash >::value_type::first, boost::placeholders::_1) <
                                                                                               ~~~~~~~^
```

# Discussion History
## trasherdk | 2020-05-31T13:15:19+00:00
Check #6531 also.
`boost 1.59` also left behind.
Hopefully @vtnerd has the solution.

## moneromooo-monero | 2020-05-31T16:34:07+00:00
Does this fix it ?

```
diff --git a/contrib/epee/include/console_handler.h b/contrib/epee/include/console_handler.h
index a58850557..a00ec624d 100644
--- a/contrib/epee/include/console_handler.h
+++ b/contrib/epee/include/console_handler.h
@@ -465,7 +465,7 @@ eof:
   bool run_default_console_handler_no_srv_param(t_server* ptsrv, t_handler handlr, std::function<std::string(void)> prompt, const std::string& usage = "")
   {
     async_console_handler console_handler;
-    return console_handler.run(ptsrv, boost::bind<bool>(no_srv_param_adapter<t_server, t_handler>, boost::placeholders::_1, boost::placeholders::_2, handlr), prompt, usage);
+    return console_handler.run(ptsrv, boost::bind<bool>(no_srv_param_adapter<t_server, t_handler>, BOOST_PLACEHOLDERS::_1, BOOST_PLACEHOLDERS::_2, handlr), prompt, usage);
   }
 
   template<class t_server, class t_handler>
@@ -634,7 +634,7 @@ eof:
 
     bool run_handling(std::function<std::string(void)> prompt, const std::string& usage_string, std::function<void(void)> exit_handler = NULL)
     {
-      return m_console_handler.run(boost::bind(&console_handlers_binder::process_command_str, this, boost::placeholders::_1), prompt, usage_string, exit_handler);
+      return m_console_handler.run(boost::bind(&console_handlers_binder::process_command_str, this, BOOST_PLACEHOLDERS::_1), prompt, usage_string, exit_handler);
     }
 
     void print_prompt()
diff --git a/contrib/epee/include/misc_language.h b/contrib/epee/include/misc_language.h
index 5f7202150..36445f296 100644
--- a/contrib/epee/include/misc_language.h
+++ b/contrib/epee/include/misc_language.h
@@ -29,8 +29,16 @@
 #pragma once
 
 #include <limits>
+#include <boost/version.hpp>
 #include <boost/thread.hpp>
 #include <boost/utility/value_init.hpp>
+
+#if BOOST_VERSION >= 107300
+#define BOOST_PLACEHOLDERS boost::placeholders
+#else
+#define BOOST_PLACEHOLDERS
+#endif
+
 namespace epee
 {
 #define STD_TRY_BEGIN() try {
diff --git a/contrib/epee/include/storages/levin_abstract_invoke2.h b/contrib/epee/include/storages/levin_abstract_invoke2.h
index de8107781..9f68de001 100644
--- a/contrib/epee/include/storages/levin_abstract_invoke2.h
+++ b/contrib/epee/include/storages/levin_abstract_invoke2.h
@@ -294,20 +294,20 @@ namespace epee
 
 #define HANDLE_INVOKE2(command_id, func, type_name_in, typename_out) \
   if(!is_notify && command_id == command) \
-  {handled=true;return epee::net_utils::buff_to_t_adapter<internal_owner_type_name, type_name_in, typename_out>(this, command, in_buff, buff_out, boost::bind(func, this, boost::placeholders::_1, boost::placeholders::_2, boost::placeholders::_3, boost::placeholders::_4), context);}
+  {handled=true;return epee::net_utils::buff_to_t_adapter<internal_owner_type_name, type_name_in, typename_out>(this, command, in_buff, buff_out, boost::bind(func, this, BOOST_PLACEHOLDERS::_1, BOOST_PLACEHOLDERS::_2, BOOST_PLACEHOLDERS::_3, BOOST_PLACEHOLDERS::_4), context);}
 
 #define HANDLE_INVOKE_T2(COMMAND, func) \
   if(!is_notify && COMMAND::ID == command) \
-  {handled=true;return epee::net_utils::buff_to_t_adapter<internal_owner_type_name, typename COMMAND::request, typename COMMAND::response>(command, in_buff, buff_out, boost::bind(func, this, boost::placeholders::_1, boost::placeholders::_2, boost::placeholders::_3, boost::placeholders::_4), context);}
+  {handled=true;return epee::net_utils::buff_to_t_adapter<internal_owner_type_name, typename COMMAND::request, typename COMMAND::response>(command, in_buff, buff_out, boost::bind(func, this, BOOST_PLACEHOLDERS::_1, BOOST_PLACEHOLDERS::_2, BOOST_PLACEHOLDERS::_3, BOOST_PLACEHOLDERS::_4), context);}
 
 
 #define HANDLE_NOTIFY2(command_id, func, type_name_in) \
   if(is_notify && command_id == command) \
-  {handled=true;return epee::net_utils::buff_to_t_adapter<internal_owner_type_name, type_name_in>(this, command, in_buff, boost::bind(func, this, boost::placeholders::_1, boost::placeholders::_2, boost::placeholders::_3), context);}
+  {handled=true;return epee::net_utils::buff_to_t_adapter<internal_owner_type_name, type_name_in>(this, command, in_buff, boost::bind(func, this, BOOST_PLACEHOLDERS::_1, BOOST_PLACEHOLDERS::_2, BOOST_PLACEHOLDERS::_3), context);}
 
 #define HANDLE_NOTIFY_T2(NOTIFY, func) \
   if(is_notify && NOTIFY::ID == command) \
-  {handled=true;return epee::net_utils::buff_to_t_adapter<internal_owner_type_name, typename NOTIFY::request>(this, command, in_buff, boost::bind(func, this, boost::placeholders::_1, boost::placeholders::_2, boost::placeholders::_3), context);}
+  {handled=true;return epee::net_utils::buff_to_t_adapter<internal_owner_type_name, typename NOTIFY::request>(this, command, in_buff, boost::bind(func, this, BOOST_PLACEHOLDERS::_1, BOOST_PLACEHOLDERS::_2, BOOST_PLACEHOLDERS::_3), context);}
 
 
 #define CHAIN_INVOKE_MAP2(func) \
diff --git a/external/randomx b/external/randomx
--- a/external/randomx
+++ b/external/randomx
@@ -1 +1 @@
-Subproject commit 7567cef4c6192fb5356bbdd7db802be77be0439b
+Subproject commit 7567cef4c6192fb5356bbdd7db802be77be0439b-dirty
diff --git a/src/checkpoints/checkpoints.cpp b/src/checkpoints/checkpoints.cpp
index 852e21318..09735fb29 100644
--- a/src/checkpoints/checkpoints.cpp
+++ b/src/checkpoints/checkpoints.cpp
@@ -135,8 +135,8 @@ namespace cryptonote
   {
     std::map< uint64_t, crypto::hash >::const_iterator highest = 
         std::max_element( m_points.begin(), m_points.end(),
-                         ( boost::bind(&std::map< uint64_t, crypto::hash >::value_type::first, boost::placeholders::_1) <
-                           boost::bind(&std::map< uint64_t, crypto::hash >::value_type::first, boost::placeholders::_2 ) ) );
+                         ( boost::bind(&std::map< uint64_t, crypto::hash >::value_type::first, BOOST_PLACEHOLDERS::_1) <
+                           boost::bind(&std::map< uint64_t, crypto::hash >::value_type::first, BOOST_PLACEHOLDERS::_2 ) ) );
     return highest->first;
   }
   //---------------------------------------------------------------------------
diff --git a/src/device_trezor/trezor/transport.cpp b/src/device_trezor/trezor/transport.cpp
index 51396d90a..21efbed75 100644
--- a/src/device_trezor/trezor/transport.cpp
+++ b/src/device_trezor/trezor/transport.cpp
@@ -711,7 +711,7 @@ namespace trezor{
     // Start the asynchronous operation itself. The handle_receive function
     // used as a callback will update the ec and length variables.
     m_socket->async_receive_from(boost::asio::buffer(buffer), m_endpoint,
-                                 boost::bind(&UdpTransport::handle_receive, boost::placeholders::_1, boost::placeholders::_2, &ec, &length));
+                                 boost::bind(&UdpTransport::handle_receive, BOOST_PLACEHOLDERS::_1, BOOST_PLACEHOLDERS::_2, &ec, &length));
 
     // Block until the asynchronous operation has completed.
     do {
diff --git a/tests/core_tests/chaingen.h b/tests/core_tests/chaingen.h
index 49001e486..676cde4b1 100644
--- a/tests/core_tests/chaingen.h
+++ b/tests/core_tests/chaingen.h
@@ -856,10 +856,10 @@ inline bool do_replay_file(const std::string& filename)
 }
 
 #define REGISTER_CALLBACK(CB_NAME, CLBACK) \
-  register_callback(CB_NAME, boost::bind(&CLBACK, this, boost::placeholders::_1, boost::placeholders::_2, boost::placeholders::_3));
+  register_callback(CB_NAME, boost::bind(&CLBACK, this, BOOST_PLACEHOLDERS::_1, BOOST_PLACEHOLDERS::_2, BOOST_PLACEHOLDERS::_3));
 
 #define REGISTER_CALLBACK_METHOD(CLASS, METHOD) \
-  register_callback(#METHOD, boost::bind(&CLASS::METHOD, this, boost::placeholders::_1, boost::placeholders::_2, boost::placeholders::_3));
+  register_callback(#METHOD, boost::bind(&CLASS::METHOD, this, BOOST_PLACEHOLDERS::_1, BOOST_PLACEHOLDERS::_2, BOOST_PLACEHOLDERS::_3));
 
 #define MAKE_GENESIS_BLOCK(VEC_EVENTS, BLK_NAME, MINER_ACC, TS)                       \
   test_generator generator;                                                           \
```

## vtnerd | 2020-05-31T16:39:57+00:00
That should work. The other technique is:

```c++
namespace placeholders
{
#if BOOST_VERSION < 106000
  using ::_1;
  using ::_2;
  using ::_3;
#else
  using namespace boost::placeholders;
#endif
}
```
And I would reduce the boost version to 1.60, everything after that version should have the new namespace.

## vtnerd | 2020-05-31T16:41:43+00:00
Also, that's a random header for the macro. I wasn't sure where to place this fix myself.

## moneromooo-monero | 2020-05-31T16:44:08+00:00
It seemed the least random given the defines already in it. I'm fine moving it elsewhere if you see something better suited. A new header maybe ?

## vtnerd | 2020-05-31T17:00:09+00:00
That was my thought. But it also just occurred to me that that `std::bind` and `std::placeholders` exist in C++11 and have (nearly) an identical set of features. We don't use the operator extensions from boost. There might be a slight compile-time improvement since boost supports C++03 mode which is a bit slower. We probably still leak `<boost/bind.hpp>` everywhere though.

## vtnerd | 2020-05-31T17:06:40+00:00
And I lied, there's an `operator<` usage in `checkpoints.cpp`, nevermind.

## vtnerd | 2020-05-31T17:17:47+00:00
FWIW (since I'm spamming everyone), thats the only call that breaks with `std::bind` and `std::placeholders`. So the macro can be limited to that file for now.

## moneromooo-monero | 2020-05-31T17:42:16+00:00
Well, make a patch with your preferred fix. If not, I'll push mine.

## ghost | 2020-05-31T17:47:51+00:00
If it's for android, I think you can upgrade to boot 1.71 without a problem.

## vtnerd | 2020-05-31T23:39:18+00:00
Ok, I have a candidate that fixes all the warnings from boost 1.73 being displayed too, waiting to see if this compiles with boost 1.58 too.

## moneromooo-monero | 2020-06-02T07:07:14+00:00
Fixed.

# Action History
- Created by: m2049r | 2020-05-31T12:42:32+00:00
- Closed at: 2020-06-02T07:07:14+00:00
