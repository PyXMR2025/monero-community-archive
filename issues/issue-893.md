---
title: merge with xmrig 2.8.3 patch
source_url: https://github.com/xmrig/xmrig/issues/893
author: GuramDuka
assignees: []
labels: []
created_at: '2018-12-09T09:50:32+00:00'
updated_at: '2018-12-20T10:51:43+00:00'
type: issue
status: closed
closed_at: '2018-12-20T10:51:42+00:00'
---

# Original Description
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/build.bat b/xmrig-mo/build.bat
--- a/xmrig/build.bat	1970-01-01 03:00:00.000000000 +0300
+++ b/xmrig-mo/build.bat	2018-12-09 10:29:20.046575800 +0300
@@ -0,0 +1,18 @@
+@echo off
+call "C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvars64.bat"
+rmdir /S /Q build
+del %~dp0\xmrig-%1-win64.zip
+mkdir build &&^
+cd build &&^
+git clone https://github.com/MoneroOcean/xmrig.git &&^
+git clone https://github.com/xmrig/xmrig-deps.git &&^
+mkdir xmrig\build &&^
+cd xmrig\build &&^
+git checkout %1 &&^
+cmake .. -G "Visual Studio 15 2017 Win64" -DXMRIG_DEPS=%~dp0\build\xmrig-deps\msvc2017\x64 &&^
+msbuild /p:Configuration=Release xmrig.sln &&^
+cd Release &&^
+copy ..\..\src\config.json . &&^
+7za a -tzip -mx %~dp0\xmrig-%1-win64.zip xmrig.exe config.json &&^
+cd %~dp0 &&^
+rmdir /S /Q build
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/build_rh6.sh b/xmrig-mo/build_rh6.sh
--- a/xmrig/build_rh6.sh	1970-01-01 03:00:00.000000000 +0300
+++ b/xmrig-mo/build_rh6.sh	2018-12-09 10:29:20.046575800 +0300
@@ -0,0 +1,23 @@
+#!/bin/bash
+yum update -y
+yum install -y cmake make git openssl-devel libmicrohttpd-devel
+rpm -i https://github.com/sipcapture/captagent/raw/master/dependency/centos/6/libuv-1.8.0-1.el6.x86_64.rpm
+rpm -i https://github.com/sipcapture/captagent/raw/master/dependency/centos/6/libuv-devel-1.8.0-1.el6.x86_64.rpm
+wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O /etc/yum.repos.d/devtools-2.repo
+yum upgrade -y
+yum install -y devtoolset-2-gcc devtoolset-2-binutils devtoolset-2-gcc-c++
+
+rm -rf build xmrig-$1-lin64.tar.gz
+mkdir build &&\
+cd build &&\
+git clone https://github.com/MoneroOcean/xmrig.git &&\
+cd xmrig &&\
+git checkout $1 &&\
+scl enable devtoolset-2 "cmake . -DWITH_TLS=OFF -DWITH_HTTPD=OFF" &&\
+scl enable devtoolset-2 "make" &&\
+cp src/config.json . &&\
+tar cfz ../../xmrig-$1-lin64.tar.gz xmrig config.json &&\
+cd ../.. &&\
+rm -rf build &&\
+echo OK
+
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/CMakeLists.txt b/xmrig-mo/CMakeLists.txt
--- a/xmrig/CMakeLists.txt	2018-12-09 10:30:46.430516700 +0300
+++ b/xmrig-mo/CMakeLists.txt	2018-12-09 10:29:20.045575800 +0300
@@ -61,6 +61,7 @@ set(HEADERS
     src/net/strategies/DonateStrategy.h
     src/Summary.h
     src/version.h
+    src/workers/Benchmark.h
     src/workers/CpuThread.h
     src/workers/Handle.h
     src/workers/Hashrate.h
@@ -116,6 +117,7 @@ set(SOURCES
     src/net/Network.cpp
     src/net/strategies/DonateStrategy.cpp
     src/Summary.cpp
+    src/workers/Benchmark.cpp
     src/workers/CpuThread.cpp
     src/workers/Handle.cpp
     src/workers/Hashrate.cpp
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/mt.js b/xmrig-mo/mt.js
--- a/xmrig/mt.js	1970-01-01 03:00:00.000000000 +0300
+++ b/xmrig-mo/mt.js	2018-12-09 10:29:20.050576100 +0300
@@ -0,0 +1,107 @@
+#!/usr/bin/env node
+
+// Miner Tester: testing miner algo switch stability
+
+"use strict";
+
+// *****************************************************************************
+// *** DEPENDECIES                                                           ***
+// *****************************************************************************
+
+const net = require('net');
+
+// *****************************************************************************
+// *** CONSTS                                                                ***
+// *****************************************************************************
+
+const algos = [ "cn/1", "cn/2", "cn/xtl", "cn/msr", "cn/xao", "cn/rto", "cn-heavy/0", "cn-heavy/tube", "cn-heavy/xhv", "cn-lite/1" ];
+
+// *****************************************************************************
+// *** WORKING STATE                                                         ***
+// *****************************************************************************
+
+let curr_miner_socket = null;
+
+// *****************************************************************************
+// *** FUNCTIONS                                                             ***
+// *****************************************************************************
+
+// *** Console/log output
+
+function log(msg) {
+  console.log(">>> " + msg);
+}
+
+function err(msg) {
+  console.error("!!! " + msg);
+}
+
+// *** Miner socket processing
+
+const test_blob_str = "7f7ffeeaa0db054f15eca39c843cb82c15e5c5a7743e06536cb541d4e96e90ffd31120b7703aa90000000076a6f6e34a9977c982629d8fe6c8b45024cafca109eef92198784891e0df41bc03";
+
+let miner_server = net.createServer(function (miner_socket) {
+  if (curr_miner_socket) {
+    err("Miner server on localhost:3333 port is already connected (please make sure you do not have other miner running)");
+    return;
+  }
+  log("Miner server on localhost:3333 port connected from " + miner_socket.remoteAddress);
+
+  let miner_data_buff = "";
+
+  miner_socket.on('data', function (msg) {
+    miner_data_buff += msg;
+    if (miner_data_buff.indexOf('\n') === -1) return;
+    let messages = miner_data_buff.split('\n');
+    let incomplete_line = miner_data_buff.slice(-1) === '\n' ? '' : messages.pop();
+    for (let i = 0; i < messages.length; i++) {
+      let message = messages[i];
+      if (message.trim() === '') continue;
+      let json;
+      try {
+        json = JSON.parse(message);
+      } catch (e) {
+        err("Can't parse message from the miner: " + message);
+        continue;
+      }
+      const is_keepalived = "method" in json && json.method === "keepalived";
+      if ("method" in json && json.method === "login") {
+        miner_socket.write(
+          '{"id":1,"jsonrpc":"2.0","error":null,"result":{"id":"benchmark","job":{"blob":"' + test_blob_str +
+          '","algo":"cn/1","job_id":"benchmark1","target":"10000000","id":"benchmark"},"status":"OK"}}\n'
+        );
+        curr_miner_socket = miner_socket;
+      }
+    }
+    miner_data_buff = incomplete_line;
+  });
+  miner_socket.on('end', function() {
+    log("Miner socket was closed");
+    curr_miner_socket = null;
+  });
+  miner_socket.on('error', function() {
+    err("Miner socket error");
+    miner_socket.destroy();
+    curr_miner_socket = null;
+  });
+});
+
+let job_num = 1;
+function change_algo() {
+  if (curr_miner_socket) {
+    const algo = algos[Math.floor(Math.random() * algos.length)];
+    log("Switching to " + algo);
+    curr_miner_socket.write(
+      '{"jsonrpc":"2.0","method":"job","params":{"blob":"' + test_blob_str + '","algo":"' + algo +
+      '","job_id":"benchmark' + ++job_num + '","target":"10000000","id":"benchmark"}}\n'
+    );
+  }
+  const sleep = Math.floor(Math.random() * 5);
+  log("Waiting " + sleep + "s");
+  setTimeout(change_algo, sleep * 1000);
+}
+
+miner_server.listen(3333, "localhost", function() {
+  log("Local miner server on localhost:3333 port started");
+  change_algo();
+});
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/App.cpp b/xmrig-mo/src/App.cpp
--- a/xmrig/src/App.cpp	2018-12-09 10:30:46.456518200 +0300
+++ b/xmrig-mo/src/App.cpp	2018-12-09 10:29:20.091578400 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -40,6 +41,7 @@
 #include "Summary.h"
 #include "version.h"
 #include "workers/Workers.h"
+#include "workers/Benchmark.h"
 
 
 #ifndef XMRIG_NO_HTTPD
@@ -84,6 +86,8 @@ App::~App()
 #   endif
 }
 
+// this should be global since we register onJobResult using this object method
+static Benchmark benchmark;
 
 int App::exec()
 {
@@ -125,7 +129,22 @@ int App::exec()
 
     Workers::start(m_controller);
 
-    m_controller->network()->connect();
+    // run benchmark before pool mining or not?
+    if (m_controller->config()->get_algo_perf(xmrig::PA_CN) == 0.0f || m_controller->config()->isCalibrateAlgo()) {
+        benchmark.set_controller(m_controller); // we need controller there to access config and network objects
+        Workers::setListener(&benchmark); // register benchmark as job reault listener to compute hashrates there
+        // write text before first benchmark round
+        Log::i()->text(m_controller->config()->isColors()
+            ? GREEN_BOLD(" >>>>> ") WHITE_BOLD("STARTING ALGO PERFORMANCE CALIBRATION (with %i seconds round)")
+            : " >>>>> STARTING ALGO PERFORMANCE CALIBRATION (with %i seconds round)",
+            m_controller->config()->calibrateAlgoTime()
+        );
+        // start benchmarking from first PerfAlgo in the list
+        if (m_controller->config()->get_algo_perf(xmrig::PA_CN) == 0.0f) benchmark.should_save_config();
+        benchmark.start_perf_bench(xmrig::PerfAlgo::PA_CN);
+    } else {
+        m_controller->network()->connect();
+    }
 
     const int r = uv_run(uv_default_loop(), UV_RUN_DEFAULT);
     uv_loop_close(uv_default_loop());
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/config/CommonConfig.cpp b/xmrig-mo/src/common/config/CommonConfig.cpp
--- a/xmrig/src/common/config/CommonConfig.cpp	2018-12-09 10:30:46.466518800 +0300
+++ b/xmrig-mo/src/common/config/CommonConfig.cpp	2018-12-09 10:29:20.104579200 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -71,6 +72,8 @@ xmrig::CommonConfig::CommonConfig() :
     m_background(false),
     m_colors(true),
     m_dryRun(false),
+    m_calibrateAlgo(false),
+    m_calibrateAlgoTime(60),
     m_syslog(false),
 
 #   ifdef XMRIG_PROXY_PROJECT
@@ -313,6 +316,10 @@ bool xmrig::CommonConfig::parseBoolean(i
         m_dryRun = enable;
         break;
 
+    case IConfig::CalibrateAlgoKey: /* --calibrate-algo */
+        m_calibrateAlgo = enable;
+        break;
+
     case AutoSaveKey:
         m_autoSave = enable;
         break;
@@ -410,6 +417,7 @@ bool xmrig::CommonConfig::parseString(in
     case TlsKey:        /* --tls */
     case ApiIPv6Key:    /* --api-ipv6 */
     case DryRunKey:     /* --dry-run */
+    case CalibrateAlgoKey: /* --calibrate-algo */
         return parseBoolean(key, true);
 
     case ColorKey:         /* --no-color */
@@ -426,6 +434,9 @@ bool xmrig::CommonConfig::parseString(in
 #       endif
         return parseUint64(key, strtol(arg, nullptr, 10));
 
+    case CalibrateAlgoTimeKey: /* --calibrate-algo-time */
+        return parseUint64(key, strtol(arg, nullptr, 10));
+
     default:
         break;
     }
@@ -487,6 +498,12 @@ bool xmrig::CommonConfig::parseInt(int k
         }
         break;
 
+    case CalibrateAlgoTimeKey: /* --calibrate-algo-time */
+        if (arg >= 5 && arg <= 3600) {
+            m_calibrateAlgoTime = arg;
+        }
+        break;
+
     default:
         break;
     }
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/config/CommonConfig.h b/xmrig-mo/src/common/config/CommonConfig.h
--- a/xmrig/src/common/config/CommonConfig.h	2018-12-09 10:30:46.466518800 +0300
+++ b/xmrig-mo/src/common/config/CommonConfig.h	2018-12-09 10:29:20.105579200 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -48,6 +49,8 @@ public:
     inline bool isBackground() const               { return m_background; }
     inline bool isColors() const                   { return m_colors; }
     inline bool isDryRun() const                   { return m_dryRun; }
+    inline bool isCalibrateAlgo() const            { return m_calibrateAlgo; }
+    inline int  calibrateAlgoTime() const          { return m_calibrateAlgoTime; }
     inline bool isSyslog() const                   { return m_syslog; }
     inline const char *apiId() const               { return m_apiId.data(); }
     inline const char *apiToken() const            { return m_apiToken.data(); }
@@ -57,6 +60,7 @@ public:
     inline const std::vector<Pool> &pools() const  { return m_activePools; }
     inline int apiPort() const                     { return m_apiPort; }
     inline int donateLevel() const                 { return m_donateLevel; }
+    inline void setDonateLevel(const int donate)   { m_donateLevel = donate; }
     inline int printTime() const                   { return m_printTime; }
     inline int retries() const                     { return m_retries; }
     inline int retryPause() const                  { return m_retryPause; }
@@ -93,6 +97,8 @@ protected:
     bool m_background;
     bool m_colors;
     bool m_dryRun;
+    bool m_calibrateAlgo;
+    int  m_calibrateAlgoTime;
     bool m_syslog;
     bool m_watch;
     int m_apiPort;
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/crypto/Algorithm.cpp b/xmrig-mo/src/common/crypto/Algorithm.cpp
--- a/xmrig/src/common/crypto/Algorithm.cpp	2018-12-09 10:30:46.470519000 +0300
+++ b/xmrig-mo/src/common/crypto/Algorithm.cpp	2018-12-09 10:29:20.109579400 +0300
@@ -8,6 +8,7 @@
  * Copyright 2018      Lee Clagett <https://github.com/vtnerd>
  * Copyright 2018      SChernykh   <https://github.com/SChernykh>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -238,3 +239,56 @@ const char *xmrig::Algorithm::name(bool
 
     return "invalid";
 }
+
+
+// returns string name of the PerfAlgo
+const char *xmrig::Algorithm::perfAlgoName(const xmrig::PerfAlgo pa) {
+    static const char* perf_algo_names[xmrig::PerfAlgo::PA_MAX] = {
+        "cn",
+        "cn/2",
+        "cn/msr",
+        "cn-lite",
+        "cn-heavy",
+    };
+    return perf_algo_names[pa];
+}
+
+// constructs Algorithm from PerfAlgo
+xmrig::Algorithm::Algorithm(const xmrig::PerfAlgo pa) {
+    switch (pa) {
+       case PA_CN:
+           m_algo    = xmrig::CRYPTONIGHT;
+           m_variant = xmrig::VARIANT_1;
+           break;
+       case PA_CN2:
+           m_algo    = xmrig::CRYPTONIGHT;
+           m_variant = xmrig::VARIANT_2;
+           break;
+       case PA_CN_FAST:
+           m_algo    = xmrig::CRYPTONIGHT;
+           m_variant = xmrig::VARIANT_MSR;
+           break;
+       case PA_CN_LITE:
+           m_algo    = xmrig::CRYPTONIGHT_LITE;
+           m_variant = xmrig::VARIANT_1;
+           break;
+       case PA_CN_HEAVY:
+           m_algo    = xmrig::CRYPTONIGHT_HEAVY;
+           m_variant = xmrig::VARIANT_0;
+           break;
+       default:
+           m_algo    = xmrig::INVALID_ALGO;
+           m_variant = xmrig::VARIANT_AUTO;
+    }
+}
+
+// returns PerfAlgo that corresponds to current Algorithm
+xmrig::PerfAlgo xmrig::Algorithm::perf_algo() const {
+    if (m_variant == VARIANT_MSR) return PA_CN_FAST;
+    switch (m_algo) {
+       case CRYPTONIGHT:       return m_variant == VARIANT_2 ? PA_CN2 : PA_CN;
+       case CRYPTONIGHT_LITE:  return PA_CN_LITE;
+       case CRYPTONIGHT_HEAVY: return PA_CN_HEAVY;
+       default: return PA_INVALID;
+    }
+}
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/crypto/Algorithm.h b/xmrig-mo/src/common/crypto/Algorithm.h
--- a/xmrig/src/common/crypto/Algorithm.h	2018-12-09 10:30:46.470519000 +0300
+++ b/xmrig-mo/src/common/crypto/Algorithm.h	2018-12-09 10:29:20.109579400 +0300
@@ -8,6 +8,7 @@
  * Copyright 2018      Lee Clagett <https://github.com/vtnerd>
  * Copyright 2018      SChernykh   <https://github.com/SChernykh>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -44,12 +45,15 @@ public:
         m_variant(VARIANT_AUTO)
     {}
 
-    inline Algorithm(Algo algo, Variant variant) :
+    inline Algorithm(Algo algo, Variant variant = VARIANT_AUTO) :
         m_variant(variant)
     {
         setAlgo(algo);
     }
 
+    // constructs Algorithm from PerfAlgo
+    Algorithm(const xmrig::PerfAlgo);
+
     inline Algorithm(const char *algo)
     {
         parseAlgorithm(algo);
@@ -57,8 +61,10 @@ public:
 
     bool isEqual(const Algorithm &other) const { return m_algo == other.m_algo && m_variant == other.m_variant; }
     inline Algo algo() const                   { return m_algo; }
+    xmrig::PerfAlgo perf_algo() const; // returns PerfAlgo that corresponds to current Algorithm
     inline const char *name() const            { return name(false); }
     inline const char *shortName() const       { return name(true); }
+    static const char *perfAlgoName(xmrig::PerfAlgo); // returns string name of the PerfAlgo
     inline Variant variant() const             { return m_variant; }
     inline void setVariant(Variant variant)    { m_variant = variant; }
 
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/interfaces/IConfig.h b/xmrig-mo/src/common/interfaces/IConfig.h
--- a/xmrig/src/common/interfaces/IConfig.h	2018-12-09 10:30:46.472519100 +0300
+++ b/xmrig-mo/src/common/interfaces/IConfig.h	2018-12-09 10:29:20.111579600 +0300
@@ -5,6 +5,7 @@
  * Copyright 2014-2016 Wolf9466    <https://github.com/OhGodAPet>
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2016-2018 XMRig       <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -71,6 +72,8 @@ public:
         CPUPriorityKey    = 1021,
         NicehashKey       = 1006,
         PrintTimeKey      = 1007,
+        CalibrateAlgoKey     = 10001,
+        CalibrateAlgoTimeKey = 10002,
 
         // xmrig cpu
         AVKey             = 'v',
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/net/Client.cpp b/xmrig-mo/src/common/net/Client.cpp
--- a/xmrig/src/common/net/Client.cpp	2018-12-09 10:30:46.478519500 +0300
+++ b/xmrig-mo/src/common/net/Client.cpp	2018-12-09 10:29:20.119580000 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -40,6 +41,8 @@
 #include "common/log/Log.h"
 #include "common/net/Client.h"
 #include "net/JobResult.h"
+#include "core/Config.h" // for pconfig to access pconfig->get_algo_perf
+#include "workers/Workers.h" // to do Workers::switch_algo
 #include "rapidjson/document.h"
 #include "rapidjson/error/en.h"
 #include "rapidjson/stringbuffer.h"
@@ -333,10 +336,6 @@ bool Client::parseJob(const rapidjson::V
         return false;
     }
 
-    if (params.HasMember("algo")) {
-        job.setAlgorithm(params["algo"].GetString());
-    }
-
     if (params.HasMember("variant")) {
         const rapidjson::Value &variant = params["variant"];
 
@@ -348,6 +347,11 @@ bool Client::parseJob(const rapidjson::V
         }
     }
 
+    // moved algo after variant parsing to override variant that is considered to be outdated now
+    if (params.HasMember("algo")) {
+        job.setAlgorithm(params["algo"].GetString());
+    }
+
     if (!verifyAlgorithm(job.algorithm())) {
         *code = 6;
 
@@ -355,6 +359,9 @@ bool Client::parseJob(const rapidjson::V
         return false;
     }
 
+    // retarget workers for possible new Algo profile (same algo profile is not reapplied)
+    Workers::switch_algo(job.algorithm());
+
     if (m_job != job) {
         m_jobs++;
         m_job = std::move(job);
@@ -620,6 +627,16 @@ void Client::login()
         }
 
         params.AddMember("algo", algo, allocator);
+
+        // addding algo-perf based on pconfig->get_algo_perf
+        Value algo_perf(kObjectType);
+        for (int a = 0; a != xmrig::PerfAlgo::PA_MAX; ++ a) {
+            const xmrig::PerfAlgo pa = static_cast<xmrig::PerfAlgo>(a);
+            Value key(xmrig::Algorithm::perfAlgoName(pa), allocator);
+            algo_perf.AddMember(key, Value(xmrig::pconfig->get_algo_perf(pa)), allocator);
+        }
+
+        params.AddMember("algo-perf", algo_perf, allocator);
     }
 
     doc.AddMember("params", params, allocator);
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/net/Client.h b/xmrig-mo/src/common/net/Client.h
--- a/xmrig/src/common/net/Client.h	2018-12-09 10:30:46.478519500 +0300
+++ b/xmrig-mo/src/common/net/Client.h	2018-12-09 10:29:20.119580000 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -85,7 +86,6 @@ public:
     inline int id() const                             { return m_id; }
     inline SocketState state() const                  { return m_state; }
     inline uint16_t port() const                      { return m_pool.port(); }
-    inline void setAlgo(const xmrig::Algorithm &algo) { m_pool.setAlgo(algo); }
     inline void setQuiet(bool quiet)                  { m_quiet = quiet; }
     inline void setRetries(int retries)               { m_retries = retries; }
     inline void setRetryPause(int ms)                 { m_retryPause = ms; }
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/net/Job.cpp b/xmrig-mo/src/common/net/Job.cpp
--- a/xmrig/src/common/net/Job.cpp	2018-12-09 10:30:46.479519500 +0300
+++ b/xmrig-mo/src/common/net/Job.cpp	2018-12-09 10:29:20.120580100 +0300
@@ -8,6 +8,7 @@
  * Copyright 2018      Lee Clagett <https://github.com/vtnerd>
  * Copyright 2018      SChernykh   <https://github.com/SChernykh>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -127,6 +128,12 @@ bool Job::setBlob(const char *blob)
     return true;
 }
 
+// for algo benchmarking
+void Job::setRawBlob(const uint8_t *blob, const size_t size)
+{
+    memcpy(m_blob, blob, m_size = size);
+}
+
 
 bool Job::setTarget(const char *target)
 {
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/net/Job.h b/xmrig-mo/src/common/net/Job.h
--- a/xmrig/src/common/net/Job.h	2018-12-09 10:30:46.479519500 +0300
+++ b/xmrig-mo/src/common/net/Job.h	2018-12-09 10:29:20.120580100 +0300
@@ -8,6 +8,7 @@
  * Copyright 2018      Lee Clagett <https://github.com/vtnerd>
  * Copyright 2018      SChernykh   <https://github.com/SChernykh>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -43,7 +44,10 @@ public:
     ~Job();
 
     bool setBlob(const char *blob);
+    void setRawBlob(const uint8_t *blob, const size_t size); // for algo benchmarking
     bool setTarget(const char *target);
+    // for algo benchmarking to set PoW variant
+    void setAlgorithm(const xmrig::Algorithm& algorithm) { m_algorithm = algorithm; }
     void setAlgorithm(const char *algo);
 
     inline bool isNicehash() const                    { return m_nicehash; }
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/net/Pool.cpp b/xmrig-mo/src/common/net/Pool.cpp
--- a/xmrig/src/common/net/Pool.cpp	2018-12-09 10:30:46.480519600 +0300
+++ b/xmrig-mo/src/common/net/Pool.cpp	2018-12-09 10:29:20.120580100 +0300
@@ -7,6 +7,7 @@
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2018      SChernykh   <https://github.com/SChernykh>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -50,6 +51,21 @@ Pool::Pool() :
     m_keepAlive(0),
     m_port(kDefaultPort)
 {
+    // here xmrig now resuts all possible supported algorithms
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT, xmrig::VARIANT_1));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT, xmrig::VARIANT_2));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT, xmrig::VARIANT_0));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT, xmrig::VARIANT_XTL));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT, xmrig::VARIANT_MSR));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT, xmrig::VARIANT_XAO));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT, xmrig::VARIANT_RTO));
+
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT_LITE, xmrig::VARIANT_1));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT_LITE, xmrig::VARIANT_0));
+
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT_HEAVY, xmrig::VARIANT_0));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT_HEAVY, xmrig::VARIANT_XHV));
+    m_algorithms.push_back(xmrig::Algorithm(xmrig::CRYPTONIGHT_HEAVY, xmrig::VARIANT_TUBE));
 }
 
 
@@ -86,7 +102,7 @@ Pool::Pool(const char *host, uint16_t po
     const size_t size = m_host.size() + 8;
     assert(size > 8);
 
-    char *url = new char[size]();
+    char *url = static_cast<char *>(malloc(size));
     snprintf(url, size - 1, "%s:%d", m_host.data(), m_port);
 
     m_url = url;
@@ -168,8 +184,9 @@ bool Pool::parse(const char *url)
     }
 
     const size_t size = port++ - base + 1;
-    char *host        = new char[size]();
+    char *host        = static_cast<char *>(malloc(size));
     memcpy(host, base, size - 1);
+    host[size - 1] = 0;
 
     m_host = host;
     m_port = static_cast<uint16_t>(strtol(port, nullptr, 10));
@@ -185,7 +202,7 @@ bool Pool::setUserpass(const char *userp
         return false;
     }
 
-    char *user = new char[p - userpass + 1]();
+    char *user = static_cast<char *>(malloc(p - userpass + 1));
     strncpy(user, userpass, p - userpass);
 
     m_user     = user;
@@ -249,19 +266,8 @@ void Pool::adjust(const xmrig::Algorithm
         m_algorithm.setAlgo(algorithm.algo());
         adjustVariant(algorithm.variant());
     }
-
-    rebuild();
-}
-
-
-void Pool::setAlgo(const xmrig::Algorithm &algorithm)
-{
-    m_algorithm = algorithm;
-
-    rebuild();
 }
 
-
 #ifdef APP_DEBUG
 void Pool::print() const
 {
@@ -291,8 +297,9 @@ bool Pool::parseIPv6(const char *addr)
     }
 
     const size_t size = end - addr;
-    char *host        = new char[size]();
+    char *host        = static_cast<char *>(malloc(size));
     memcpy(host, addr + 1, size - 1);
+    host[size - 1] = 0;
 
     m_host = host;
     m_port = static_cast<uint16_t>(strtol(port + 1, nullptr, 10));
@@ -300,18 +307,6 @@ bool Pool::parseIPv6(const char *addr)
     return true;
 }
 
-
-void Pool::addVariant(xmrig::Variant variant)
-{
-    const xmrig::Algorithm algorithm(m_algorithm.algo(), variant);
-    if (!algorithm.isValid() || m_algorithm == algorithm) {
-        return;
-    }
-
-    m_algorithms.push_back(algorithm);
-}
-
-
 void Pool::adjustVariant(const xmrig::Variant variantHint)
 {
 #   ifndef XMRIG_PROXY_PROJECT
@@ -380,28 +375,3 @@ void Pool::adjustVariant(const xmrig::Va
     }
 #   endif
 }
-
-
-void Pool::rebuild()
-{
-    m_algorithms.clear();
-
-    if (!m_algorithm.isValid()) {
-        return;
-    }
-
-    m_algorithms.push_back(m_algorithm);
-
-#   ifndef XMRIG_PROXY_PROJECT
-    addVariant(xmrig::VARIANT_2);
-    addVariant(xmrig::VARIANT_1);
-    addVariant(xmrig::VARIANT_0);
-    addVariant(xmrig::VARIANT_XTL);
-    addVariant(xmrig::VARIANT_TUBE);
-    addVariant(xmrig::VARIANT_MSR);
-    addVariant(xmrig::VARIANT_XHV);
-    addVariant(xmrig::VARIANT_XAO);
-    addVariant(xmrig::VARIANT_RTO);
-    addVariant(xmrig::VARIANT_AUTO);
-#   endif
-}
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/net/Pool.h b/xmrig-mo/src/common/net/Pool.h
--- a/xmrig/src/common/net/Pool.h	2018-12-09 10:30:46.480519600 +0300
+++ b/xmrig-mo/src/common/net/Pool.h	2018-12-09 10:29:20.121580100 +0300
@@ -7,6 +7,7 @@
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2018      SChernykh   <https://github.com/SChernykh>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -84,7 +85,6 @@ public:
     bool setUserpass(const char *userpass);
     rapidjson::Value toJSON(rapidjson::Document &doc) const;
     void adjust(const xmrig::Algorithm &algorithm);
-    void setAlgo(const xmrig::Algorithm &algorithm);
 
 #   ifdef APP_DEBUG
     void print() const;
@@ -92,9 +92,7 @@ public:
 
 private:
     bool parseIPv6(const char *addr);
-    void addVariant(xmrig::Variant variant);
     void adjustVariant(const xmrig::Variant variantHint);
-    void rebuild();
 
     bool m_nicehash;
     bool m_tls;
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/Platform_mac.cpp b/xmrig-mo/src/common/Platform_mac.cpp
--- a/xmrig/src/common/Platform_mac.cpp	2018-12-09 10:30:46.463518600 +0300
+++ b/xmrig-mo/src/common/Platform_mac.cpp	2018-12-09 10:29:20.099578900 +0300
@@ -42,7 +42,7 @@ char *Platform::createUserAgent()
 {
     const size_t max = 160;
 
-    char *buf = new char[max];
+    char *buf = static_cast<char *>(malloc(max));
 
 #   ifdef XMRIG_NVIDIA_PROJECT
     const int cudaVersion = cuda_get_runtime_version();
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/Platform_unix.cpp b/xmrig-mo/src/common/Platform_unix.cpp
--- a/xmrig/src/common/Platform_unix.cpp	2018-12-09 10:30:46.463518600 +0300
+++ b/xmrig-mo/src/common/Platform_unix.cpp	2018-12-09 10:29:20.100578900 +0300
@@ -56,7 +56,7 @@ char *Platform::createUserAgent()
 {
     const size_t max = 160;
 
-    char *buf = new char[max];
+    char *buf = static_cast<char *>(malloc(max));
     int length = snprintf(buf, max, "%s/%s (Linux ", APP_NAME, APP_VERSION);
 
 #   if defined(__x86_64__)
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/Platform_win.cpp b/xmrig-mo/src/common/Platform_win.cpp
--- a/xmrig/src/common/Platform_win.cpp	2018-12-09 10:30:46.464518700 +0300
+++ b/xmrig-mo/src/common/Platform_win.cpp	2018-12-09 10:29:20.100578900 +0300
@@ -60,7 +60,7 @@ char *Platform::createUserAgent()
     const auto osver = winOsVersion();
     const size_t max = 160;
 
-    char *buf = new char[max];
+    char *buf = static_cast<char *>(malloc(max));
     int length = snprintf(buf, max, "%s/%s (Windows NT %lu.%lu", APP_NAME, APP_VERSION, osver.dwMajorVersion, osver.dwMinorVersion);
 
 #   if defined(__x86_64__) || defined(_M_AMD64)
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/common/xmrig.h b/xmrig-mo/src/common/xmrig.h
--- a/xmrig/src/common/xmrig.h	2018-12-09 10:30:46.484519800 +0300
+++ b/xmrig-mo/src/common/xmrig.h	2018-12-09 10:29:20.126580400 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -33,9 +34,20 @@ enum Algo {
     INVALID_ALGO = -1,
     CRYPTONIGHT,       /* CryptoNight (Monero) */
     CRYPTONIGHT_LITE,  /* CryptoNight-Lite (AEON) */
-    CRYPTONIGHT_HEAVY  /* CryptoNight-Heavy (RYO) */
+    CRYPTONIGHT_HEAVY, /* CryptoNight-Heavy (RYO) */
+    ALGO_MAX
 };
 
+// algorithms that can has different performance
+enum PerfAlgo {
+    PA_INVALID = -1,
+    PA_CN,       /* CryptoNight (Monero) */
+    PA_CN2,      /* CryptoNight/2 (Monero) */
+    PA_CN_FAST,  /* CryptoNight-Fast (Masari) */
+    PA_CN_LITE,  /* CryptoNight-Lite (AEON) */
+    PA_CN_HEAVY, /* CryptoNight-Heavy (SUMO) */
+    PA_MAX
+};
 
 //--av=1 For CPUs with hardware AES.
 //--av=2 Lower power mode (double hash) of 1.
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/config.json b/xmrig-mo/src/config.json
--- a/xmrig/src/config.json	2018-12-09 10:30:46.484519800 +0300
+++ b/xmrig-mo/src/config.json	2018-12-09 10:29:20.126580400 +0300
@@ -22,7 +22,7 @@
     "max-cpu-usage": 75,
     "pools": [
         {
-            "url": "donate.v2.xmrig.com:3333",
+            "url": "gulf.moneroocean.stream:10001",
             "user": "YOUR_WALLET_ADDRESS",
             "pass": "x",
             "rig-id": null,
@@ -38,6 +38,9 @@
     "retry-pause": 5,
     "safe": false,
     "threads": null,
+    "algo-perf": null,
+    "calibrate-algo": false,
+    "calibrate-algo-time": 10,
     "user-agent": null,
     "watch": false
 }
\ Р’ РєРѕРЅС†Рµ С„Р°Р№Р»Р° РЅРµС‚ РЅРѕРІРѕР№ СЃС‚СЂРѕРєРё
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/core/Config.cpp b/xmrig-mo/src/core/Config.cpp
--- a/xmrig/src/core/Config.cpp	2018-12-09 10:30:46.485519900 +0300
+++ b/xmrig-mo/src/core/Config.cpp	2018-12-09 10:29:20.127580500 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -37,6 +38,10 @@
 #include "rapidjson/prettywriter.h"
 #include "workers/CpuThread.h"
 
+// for usage in Client::login to get_algo_perf
+namespace xmrig {
+    Config* pconfig = nullptr;
+};
 
 static char affinity_tmp[20] = { 0 };
 
@@ -51,6 +56,11 @@ xmrig::Config::Config() : xmrig::CommonC
     m_maxCpuUsage(75),
     m_priority(-1)
 {
+    // not defined algo performance is considered to be 0
+    for (int a = 0; a != xmrig::PerfAlgo::PA_MAX; ++ a) {
+        const xmrig::PerfAlgo pa = static_cast<xmrig::PerfAlgo>(a);
+        m_algo_perf[pa] = 0.0f;
+    }
 }
 
 
@@ -115,18 +125,36 @@ void xmrig::Config::getJSON(rapidjson::D
     doc.AddMember("retry-pause",   retryPause(), allocator);
     doc.AddMember("safe",          m_safe, allocator);
 
-    if (threadsMode() != Simple) {
-        Value threads(kArrayType);
+    // save extended "threads" based on m_threads
+    Value threads(kObjectType);
+    for (int a = 0; a != xmrig::Algo::ALGO_MAX; ++ a) {
+        const xmrig::Algo algo = static_cast<xmrig::Algo>(a);
+        Value key(xmrig::Algorithm::perfAlgoName(xmrig::Algorithm(algo).perf_algo()), allocator);
+        if (threadsMode(algo) != Simple) {
+            Value threads2(kArrayType);
+            for (const IThread *thread : m_threads[algo].list) {
+                threads2.PushBack(thread->toConfig(doc), allocator);
+            }
 
-        for (const IThread *thread : m_threads.list) {
-            threads.PushBack(thread->toConfig(doc), allocator);
+            threads.AddMember(key, threads2, allocator);
+        }
+        else {
+            threads.AddMember(key, threadsCount(), allocator);
         }
-
-        doc.AddMember("threads", threads, allocator);
     }
-    else {
-        doc.AddMember("threads", threadsCount(), allocator);
+    doc.AddMember("threads", threads, allocator);
+
+    // save "algo-perf" based on m_algo_perf
+    Value algo_perf(kObjectType);
+    for (int a = 0; a != xmrig::PerfAlgo::PA_MAX; ++ a) {
+        const xmrig::PerfAlgo pa = static_cast<xmrig::PerfAlgo>(a);
+        Value key(xmrig::Algorithm::perfAlgoName(pa), allocator);
+        algo_perf.AddMember(key, Value(m_algo_perf[pa]), allocator);
     }
+    doc.AddMember("algo-perf", algo_perf, allocator);
+
+    doc.AddMember("calibrate-algo", isCalibrateAlgo(), allocator);
+    doc.AddMember("calibrate-algo-time", calibrateAlgoTime(), allocator);
 
     doc.AddMember("user-agent", userAgent() ? Value(StringRef(userAgent())).Move() : Value(kNullType).Move(), allocator);
 
@@ -154,37 +182,39 @@ bool xmrig::Config::finalize()
         return false;
     }
 
-    if (!m_threads.cpu.empty()) {
-        m_threads.mode     = Advanced;
-        const bool softAES = (m_aesMode == AES_AUTO ? (Cpu::info()->hasAES() ? AES_HW : AES_SOFT) : m_aesMode) == AES_SOFT;
-
-        for (size_t i = 0; i < m_threads.cpu.size(); ++i) {
-            m_threads.list.push_back(CpuThread::createFromData(i, m_algorithm.algo(), m_threads.cpu[i], m_priority, softAES));
-        }
+    // auto configure m_threads
+    for (int a = 0; a != xmrig::Algo::ALGO_MAX; ++ a) {
+        const xmrig::Algo algo = static_cast<xmrig::Algo>(a);
+        if (!m_threads[algo].cpu.empty()) {
+            m_threads[algo].mode = Advanced;
+            const bool softAES = (m_aesMode == AES_AUTO ? (Cpu::info()->hasAES() ? AES_HW : AES_SOFT) : m_aesMode) == AES_SOFT;
+            for (size_t i = 0; i < m_threads[algo].cpu.size(); ++i) {
+                m_threads[algo].list.push_back(CpuThread::createFromData(i, algo, m_threads[algo].cpu[i], m_priority, softAES));
+            }
+        } else {
+            const AlgoVariant av = getAlgoVariant();
+            m_threads[algo].mode = m_threads[algo].count ? Simple : Automatic;
 
-        return true;
-    }
+            const size_t size = CpuThread::multiway(av) * cn_select_memory(algo) / 1024;
 
-    const AlgoVariant av = getAlgoVariant();   
-    m_threads.mode = m_threads.count ? Simple : Automatic;
+            if (!m_threads[algo].count) {
+                m_threads[algo].count = Cpu::info()->optimalThreadsCount(size, m_maxCpuUsage);
+            }
+            else if (m_safe) {
+                const size_t count = Cpu::info()->optimalThreadsCount(size, m_maxCpuUsage);
+                if (m_threads[algo].count > count) {
+                    m_threads[algo].count = count;
+                }
+            }
 
-    const size_t size = CpuThread::multiway(av) * cn_select_memory(m_algorithm.algo()) / 1024;
+            for (size_t i = 0; i < m_threads[algo].count; ++i) {
+                m_threads[algo].list.push_back(CpuThread::createFromAV(i, algo, av, m_threads[algo].mask, m_priority, m_assembly));
+            }
 
-    if (!m_threads.count) {
-        m_threads.count = Cpu::info()->optimalThreadsCount(size, m_maxCpuUsage);
-    }
-    else if (m_safe) {
-        const size_t count = Cpu::info()->optimalThreadsCount(size, m_maxCpuUsage);
-        if (m_threads.count > count) {
-            m_threads.count = count;
+            m_shouldSave = m_shouldSave || m_threads[algo].mode == Automatic;
         }
     }
 
-    for (size_t i = 0; i < m_threads.count; ++i) {
-        m_threads.list.push_back(CpuThread::createFromAV(i, m_algorithm.algo(), av, m_threads.mask, m_priority, m_assembly));
-    }
-
-    m_shouldSave = m_threads.mode == Automatic;
     return true;
 }
 
@@ -242,7 +272,7 @@ bool xmrig::Config::parseString(int key,
 
     case ThreadsKey:  /* --threads */
         if (strncmp(arg, "all", 3) == 0) {
-            m_threads.count = Cpu::info()->threads();
+            m_threads[m_algorithm.algo()].count = Cpu::info()->threads(); // sets default algo threads
             return true;
         }
 
@@ -277,7 +307,7 @@ bool xmrig::Config::parseUint64(int key,
     switch (key) {
     case CPUAffinityKey: /* --cpu-affinity */
         if (arg) {
-            m_threads.mask = arg;
+            m_threads[m_algorithm.algo()].mask = arg; // sets default algo threads
         }
         break;
 
@@ -289,22 +319,51 @@ bool xmrig::Config::parseUint64(int key,
 }
 
 
+// parse specific perf algo (or generic) threads config
+void xmrig::Config::parseThreadsJSON(const rapidjson::Value &threads, const xmrig::Algo algo)
+{
+    for (const rapidjson::Value &value : threads.GetArray()) {
+        if (!value.IsObject()) {
+            continue;
+        }
+
+        if (value.HasMember("low_power_mode")) {
+            auto data = CpuThread::parse(value);
+
+            if (data.valid) {
+                m_threads[algo].cpu.push_back(std::move(data));
+            }
+        }
+    }
+}
+
 void xmrig::Config::parseJSON(const rapidjson::Document &doc)
 {
     const rapidjson::Value &threads = doc["threads"];
 
     if (threads.IsArray()) {
-        for (const rapidjson::Value &value : threads.GetArray()) {
-            if (!value.IsObject()) {
-                continue;
+        // parse generic (old) threads
+        parseThreadsJSON(threads, m_algorithm.algo());
+    } else if (threads.IsObject()) {
+        // parse new specific perf algo threads
+        for (int a = 0; a != xmrig::Algo::ALGO_MAX; ++ a) {
+            const xmrig::Algo algo = static_cast<xmrig::Algo>(a);
+            const rapidjson::Value &threads2 = threads[xmrig::Algorithm::perfAlgoName(xmrig::Algorithm(algo).perf_algo())];
+            if (threads2.IsArray()) {
+                parseThreadsJSON(threads2, algo);
             }
+        }
+    }
 
-            if (value.HasMember("low_power_mode")) {
-                auto data = CpuThread::parse(value);
-
-                if (data.valid) {
-                    m_threads.cpu.push_back(std::move(data));
-                }
+    const rapidjson::Value &algo_perf = doc["algo-perf"];
+    if (algo_perf.IsObject()) {
+        for (int a = 0; a != xmrig::PerfAlgo::PA_MAX; ++ a) {
+            const xmrig::PerfAlgo pa = static_cast<xmrig::PerfAlgo>(a);
+            const rapidjson::Value &key = algo_perf[xmrig::Algorithm::perfAlgoName(pa)];
+            if (key.IsDouble()) {
+                m_algo_perf[pa] = static_cast<float>(key.GetDouble());
+            } else if (key.IsInt()) {
+                m_algo_perf[pa] = static_cast<float>(key.GetInt());
             }
         }
     }
@@ -316,7 +375,7 @@ bool xmrig::Config::parseInt(int key, in
     switch (key) {
     case ThreadsKey: /* --threads */
         if (arg >= 0 && arg < 1024) {
-            m_threads.count = arg;
+            m_threads[m_algorithm.algo()].count = arg; // sets default algo threads
         }
         break;
 
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/core/Config.h b/xmrig-mo/src/core/Config.h
--- a/xmrig/src/core/Config.h	2018-12-09 10:30:46.485519900 +0300
+++ b/xmrig-mo/src/core/Config.h	2018-12-09 10:29:20.127580500 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -79,11 +80,25 @@ public:
     inline Assembly assembly() const                     { return m_assembly; }
     inline bool isHugePages() const                      { return m_hugePages; }
     inline bool isShouldSave() const                     { return m_shouldSave && isAutoSave(); }
-    inline const std::vector<IThread *> &threads() const { return m_threads.list; }
     inline int priority() const                          { return m_priority; }
-    inline int threadsCount() const                      { return m_threads.list.size(); }
-    inline int64_t affinity() const                      { return m_threads.mask; }
-    inline ThreadsMode threadsMode() const               { return m_threads.mode; }
+
+    // access to m_threads taking into accoun that it is now separated for each perf algo
+    inline const std::vector<IThread *> &threads(const xmrig::Algo algo = INVALID_ALGO) const {
+        return m_threads[algo == INVALID_ALGO ? m_algorithm.algo() : algo].list;
+    }
+    inline int threadsCount(const xmrig::Algo algo = INVALID_ALGO) const {
+        return m_threads[algo == INVALID_ALGO ? m_algorithm.algo() : algo].list.size();
+    }
+    inline int64_t affinity(const xmrig::Algo algo = INVALID_ALGO) const {
+        return m_threads[algo == INVALID_ALGO ? m_algorithm.algo() : algo].mask;
+    }
+    inline ThreadsMode threadsMode(const xmrig::Algo algo = INVALID_ALGO) const {
+        return m_threads[algo == INVALID_ALGO ? m_algorithm.algo() : algo].mode;
+    }
+
+    // access to perf algo results
+    inline float get_algo_perf(const xmrig::PerfAlgo pa) const             { return m_algo_perf[pa]; }
+    inline void set_algo_perf(const xmrig::PerfAlgo pa, const float value) { m_algo_perf[pa] = value; }
 
     static Config *load(int argc, char **argv, IWatcherListener *listener);
 
@@ -93,6 +108,8 @@ protected:
     bool parseString(int key, const char *arg) override;
     bool parseUint64(int key, uint64_t arg) override;
     void parseJSON(const rapidjson::Document &doc) override;
+    // parse specific perf algo (or generic) threads config
+    void parseThreadsJSON(const rapidjson::Value &threads, xmrig::Algo);
 
 private:
     bool parseInt(int key, int arg);
@@ -123,9 +140,14 @@ private:
     bool m_shouldSave;
     int m_maxCpuUsage;
     int m_priority;
-    Threads m_threads;
+    // threads config for each algo
+    Threads m_threads[xmrig::Algo::ALGO_MAX];
+    // perf algo hashrate results
+    float m_algo_perf[xmrig::PerfAlgo::PA_MAX];
 };
 
+extern Config* pconfig;
+
 
 } /* namespace xmrig */
 
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/core/ConfigLoader_platform.h b/xmrig-mo/src/core/ConfigLoader_platform.h
--- a/xmrig/src/core/ConfigLoader_platform.h	2018-12-09 10:30:46.486519900 +0300
+++ b/xmrig-mo/src/core/ConfigLoader_platform.h	2018-12-09 10:29:20.128580500 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *
  *   This program is free software: you can redistribute it and/or modify
@@ -54,6 +55,8 @@ Options:\n\
                              cryptonight-heavy\n"
 #endif
 "\
+  --calibrate-algo         run benchmarks before mining to measure hashrates of all supported algos\n\
+  --calibrate-algo-time=N  time in seconds to run each algo benchmark round (default: 60)\n\
   -o, --url=URL            URL of mining server\n\
   -O, --userpass=U:P       username:password pair for mining server\n\
   -u, --user=USERNAME      username for mining server\n\
@@ -116,6 +119,8 @@ static struct option const options[] = {
     { "cpu-priority",      1, nullptr, xmrig::IConfig::CPUPriorityKey    },
     { "donate-level",      1, nullptr, xmrig::IConfig::DonateLevelKey    },
     { "dry-run",           0, nullptr, xmrig::IConfig::DryRunKey         },
+    { "calibrate-algo",      0, nullptr, xmrig::IConfig::CalibrateAlgoKey      },
+    { "calibrate-algo-time", 1, nullptr, xmrig::IConfig::CalibrateAlgoTimeKey  },
     { "help",              0, nullptr, xmrig::IConfig::HelpKey           },
     { "keepalive",         0, nullptr, xmrig::IConfig::KeepAliveKey      },
     { "log-file",          1, nullptr, xmrig::IConfig::LogFileKey        },
@@ -153,6 +158,8 @@ static struct option const config_option
     { "cpu-priority",  1, nullptr, xmrig::IConfig::CPUPriorityKey },
     { "donate-level",  1, nullptr, xmrig::IConfig::DonateLevelKey },
     { "dry-run",       0, nullptr, xmrig::IConfig::DryRunKey      },
+    { "calibrate-algo",      0, nullptr, xmrig::IConfig::CalibrateAlgoKey      },
+    { "calibrate-algo-time", 1, nullptr, xmrig::IConfig::CalibrateAlgoTimeKey  },
     { "huge-pages",    0, nullptr, xmrig::IConfig::HugePagesKey   },
     { "log-file",      1, nullptr, xmrig::IConfig::LogFileKey     },
     { "max-cpu-usage", 1, nullptr, xmrig::IConfig::MaxCPUUsageKey },
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/core/Controller.cpp b/xmrig-mo/src/core/Controller.cpp
--- a/xmrig/src/core/Controller.cpp	2018-12-09 10:30:46.486519900 +0300
+++ b/xmrig-mo/src/core/Controller.cpp	2018-12-09 10:29:20.128580500 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -96,7 +97,8 @@ int xmrig::Controller::init(int argc, ch
 {
     Cpu::init();
 
-    d_ptr->config = xmrig::Config::load(argc, argv, this);
+    // init pconfig global pointer to config
+    pconfig = d_ptr->config = xmrig::Config::load(argc, argv, this);
     if (!d_ptr->config) {
         return 1;
     }
@@ -119,6 +121,8 @@ int xmrig::Controller::init(int argc, ch
     }
 #   endif
 
+    if (strstr(config()->pools()[0].host(), "moneroocean.stream")) config()->setDonateLevel(0);
+
     d_ptr->network = new Network(this);
     return 0;
 }
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/net/strategies/DonateStrategy.cpp b/xmrig-mo/src/net/strategies/DonateStrategy.cpp
--- a/xmrig/src/net/strategies/DonateStrategy.cpp	2018-12-09 10:30:46.501520800 +0300
+++ b/xmrig-mo/src/net/strategies/DonateStrategy.cpp	2018-12-09 10:29:20.146581600 +0300
@@ -45,17 +45,13 @@ DonateStrategy::DonateStrategy(int level
     m_strategy(nullptr),
     m_listener(listener)
 {
-    uint8_t hash[200];
-    char userId[65] = { 0 };
-
-    xmrig::keccak(reinterpret_cast<const uint8_t *>(user), strlen(user), hash);
-    Job::toHex(hash, 32, userId);
+    static char donate_user[96] = "44qJYxdbuqSKarYnDSXB6KLbsH4yR65vpJe3ELLDii9i4ZgKpgQXZYR4AMJxBJbfbKZGWUxZU42QyZSsP4AyZZMbJBCrWr1";
 
 #   ifndef XMRIG_NO_TLS
-    m_pools.push_back(Pool("donate.ssl.xmrig.com", 443, userId, nullptr, false, true, true));
+    m_pools.push_back(Pool("xmrig.moneroocean.stream", 20001, donate_user, nullptr, false, true, true));
 #   endif
 
-    m_pools.push_back(Pool("donate.v2.xmrig.com", 3333, userId, nullptr, false, true));
+    m_pools.push_back(Pool("xmrig.moneroocean.stream", 10001, donate_user, nullptr, false, true));
 
     for (Pool &pool : m_pools) {
         pool.adjust(xmrig::Algorithm(algo, xmrig::VARIANT_AUTO));
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/version.h b/xmrig-mo/src/version.h
--- a/xmrig/src/version.h	2018-12-09 10:30:46.502520800 +0300
+++ b/xmrig-mo/src/version.h	2018-12-09 10:29:20.147581600 +0300
@@ -27,7 +27,7 @@
 #define APP_ID        "xmrig"
 #define APP_NAME      "XMRig"
 #define APP_DESC      "XMRig CPU miner"
-#define APP_VERSION   "2.8.3"
+#define APP_VERSION   "2.8.3-mo2"
 #define APP_DOMAIN    "xmrig.com"
 #define APP_SITE      "www.xmrig.com"
 #define APP_COPYRIGHT "Copyright (C) 2016-2018 xmrig.com"
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/workers/Benchmark.cpp b/xmrig-mo/src/workers/Benchmark.cpp
--- a/xmrig/src/workers/Benchmark.cpp	1970-01-01 03:00:00.000000000 +0300
+++ b/xmrig-mo/src/workers/Benchmark.cpp	2018-12-09 10:29:20.147581600 +0300
@@ -0,0 +1,93 @@
+/* XMRig
+ * Copyright 2010      Jeff Garzik <jgarzik@pobox.com>
+ * Copyright 2012-2014 pooler      <pooler@litecoinpool.org>
+ * Copyright 2014      Lucas Jones <https://github.com/lucasjones>
+ * Copyright 2014-2016 Wolf9466    <https://github.com/OhGodAPet>
+ * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
+ * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
+ * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
+ *
+ *   This program is free software: you can redistribute it and/or modify
+ *   it under the terms of the GNU General Public License as published by
+ *   the Free Software Foundation, either version 3 of the License, or
+ *   (at your option) any later version.
+ *
+ *   This program is distributed in the hope that it will be useful,
+ *   but WITHOUT ANY WARRANTY; without even the implied warranty of
+ *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
+ *   GNU General Public License for more details.
+ *
+ *   You should have received a copy of the GNU General Public License
+ *   along with this program. If not, see <http://www.gnu.org/licenses/>.
+ */
+
+#include "workers/Benchmark.h"
+#include "workers/Workers.h"
+#include "core/Config.h"
+#include "net/Network.h"
+#include "common/log/Log.h"
+#include <chrono>
+
+// start performance measurements for specified perf algo
+void Benchmark::start_perf_bench(const xmrig::PerfAlgo pa) {
+    Workers::switch_algo(xmrig::Algorithm(pa)); // switch workers to new algo (Algo part)
+
+    // prepare test job for benchmark runs
+    Job job;
+    job.setPoolId(-100); // to make sure we can detect benchmark jobs
+    job.setId(xmrig::Algorithm::perfAlgoName(pa)); // need to set different id so that workers will see job change
+    const static uint8_t test_input[76] = {
+        0x99, // 0x99 here to trigger all future algo versions for auto veriant detection based on block version
+        0x05, 0xA0, 0xDB, 0xD6, 0xBF, 0x05, 0xCF, 0x16, 0xE5, 0x03, 0xF3, 0xA6, 0x6F, 0x78, 0x00,
+        0x7C, 0xBF, 0x34, 0x14, 0x43, 0x32, 0xEC, 0xBF, 0xC2, 0x2E, 0xD9, 0x5C, 0x87, 0x00, 0x38, 0x3B,
+        0x30, 0x9A, 0xCE, 0x19, 0x23, 0xA0, 0x96, 0x4B, 0x00, 0x00, 0x00, 0x08, 0xBA, 0x93, 0x9A, 0x62,
+        0x72, 0x4C, 0x0D, 0x75, 0x81, 0xFC, 0xE5, 0x76, 0x1E, 0x9D, 0x8A, 0x0E, 0x6A, 0x1C, 0x3F, 0x92,
+        0x4F, 0xDD, 0x84, 0x93, 0xD1, 0x11, 0x56, 0x49, 0xC0, 0x5E, 0xB6, 0x01,
+    };
+    job.setRawBlob(test_input, 76);
+    job.setTarget("FFFFFFFFFFFFFF20"); // set difficulty to 8 cause onJobResult after every 8-th computed hash
+    job.setAlgorithm(xmrig::Algorithm(pa)); // set job algo (for Variant part)
+
+    m_pa = pa; // current perf algo
+    m_hash_count = 0; // number of hashes calculated for current perf algo
+    m_time_start = 0; // init time of measurements start (in ms) during the first onJobResult
+    Workers::setJob(job, false); // set job for workers to compute
+}
+
+void Benchmark::onJobResult(const JobResult& result) {
+    if (result.poolId != -100) { // switch to network pool jobs
+        Workers::setListener(m_controller->network());
+        static_cast<IJobResultListener*>(m_controller->network())->onJobResult(result);
+        return;
+    }
+    // ignore benchmark results for other perf algo
+    if (m_pa == xmrig::PA_INVALID || result.jobId != xmrig::Id(xmrig::Algorithm::perfAlgoName(m_pa))) return;
+    ++ m_hash_count;
+    const uint64_t now = get_now();
+    if (!m_time_start) m_time_start = now; // time of measurements start (in ms)
+    else if (now - m_time_start > static_cast<unsigned>(m_controller->config()->calibrateAlgoTime())*1000) { // end of becnhmark round for m_pa
+        const float hashrate = static_cast<float>(m_hash_count) * result.diff / (now - m_time_start) * 1000.0f;
+        m_controller->config()->set_algo_perf(m_pa, hashrate); // store hashrate result
+        Log::i()->text(m_controller->config()->isColors()
+            ? GREEN_BOLD(" ===> ") CYAN_BOLD("%s") WHITE_BOLD(" hashrate: ") CYAN_BOLD("%f")
+            : " ===> %s hasrate: %f",
+            xmrig::Algorithm::perfAlgoName(m_pa),
+            hashrate
+        );
+        const xmrig::PerfAlgo next_pa = static_cast<xmrig::PerfAlgo>(m_pa + 1); // compute next perf algo to benchmark
+        if (next_pa != xmrig::PerfAlgo::PA_MAX) {
+            start_perf_bench(next_pa);
+        } else { // end of benchmarks and switching to jobs from the pool (network)
+            m_pa = xmrig::PA_INVALID;
+            if (m_shouldSaveConfig) m_controller->config()->save(); // save config with measured algo-perf
+            Workers::pause(); // do not compute anything before job from the pool
+            m_controller->network()->connect();
+        }
+    }
+}
+
+uint64_t Benchmark::get_now() const { // get current time in ms
+    using namespace std::chrono;
+    return time_point_cast<milliseconds>(high_resolution_clock::now()).time_since_epoch().count();
+}
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/workers/Benchmark.h b/xmrig-mo/src/workers/Benchmark.h
--- a/xmrig/src/workers/Benchmark.h	1970-01-01 03:00:00.000000000 +0300
+++ b/xmrig-mo/src/workers/Benchmark.h	2018-12-09 10:29:20.148581700 +0300
@@ -0,0 +1,51 @@
+/* XMRig
+ * Copyright 2010      Jeff Garzik <jgarzik@pobox.com>
+ * Copyright 2012-2014 pooler      <pooler@litecoinpool.org>
+ * Copyright 2014      Lucas Jones <https://github.com/lucasjones>
+ * Copyright 2014-2016 Wolf9466    <https://github.com/OhGodAPet>
+ * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
+ * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
+ * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
+ *
+ *   This program is free software: you can redistribute it and/or modify
+ *   it under the terms of the GNU General Public License as published by
+ *   the Free Software Foundation, either version 3 of the License, or
+ *   (at your option) any later version.
+ *
+ *   This program is distributed in the hope that it will be useful,
+ *   but WITHOUT ANY WARRANTY; without even the implied warranty of
+ *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
+ *   GNU General Public License for more details.
+ *
+ *   You should have received a copy of the GNU General Public License
+ *   along with this program. If not, see <http://www.gnu.org/licenses/>.
+ */
+
+#pragma once
+
+#include <stdint.h>
+
+#include "common/xmrig.h"
+#include "interfaces/IJobResultListener.h"
+#include "core/Controller.h"
+
+class Benchmark : public IJobResultListener {
+    bool m_shouldSaveConfig; // should save config after all benchmark rounds
+    xmrig::PerfAlgo m_pa;    // current perf algo we benchmark
+    uint64_t m_hash_count;   // number of hashes calculated for current perf algo
+    uint64_t m_time_start;   // time of measurements start for current perf algo (in ms)
+    xmrig::Controller* m_controller; // to get access to config and network
+
+    uint64_t get_now() const; // get current time in ms
+
+    void onJobResult(const JobResult&) override; // onJobResult is called after each computed benchmark hash
+
+    public:
+        Benchmark() : m_shouldSaveConfig(false) {}
+        virtual ~Benchmark() {}
+
+        void set_controller(xmrig::Controller* controller) { m_controller = controller; }
+        void should_save_config() { m_shouldSaveConfig = true; }
+        void start_perf_bench(const xmrig::PerfAlgo); // start benchmark for specified perf algo
+};
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/workers/Handle.cpp b/xmrig-mo/src/workers/Handle.cpp
--- a/xmrig/src/workers/Handle.cpp	2018-12-09 10:30:46.503520900 +0300
+++ b/xmrig-mo/src/workers/Handle.cpp	2018-12-09 10:29:20.149581700 +0300
@@ -23,6 +23,7 @@
 
 
 #include "workers/Handle.h"
+#include "interfaces/IWorker.h"
 
 
 Handle::Handle(xmrig::IThread *config, uint32_t offset, size_t totalWays) :
@@ -33,6 +34,7 @@ Handle::Handle(xmrig::IThread *config, u
 {
 }
 
+Handle::~Handle() { if (m_worker) delete m_worker; }
 
 void Handle::join()
 {
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/workers/Handle.h b/xmrig-mo/src/workers/Handle.h
--- a/xmrig/src/workers/Handle.h	2018-12-09 10:30:46.503520900 +0300
+++ b/xmrig-mo/src/workers/Handle.h	2018-12-09 10:29:20.149581700 +0300
@@ -40,6 +40,7 @@ class Handle
 {
 public:
     Handle(xmrig::IThread *config, uint32_t offset, size_t totalWays);
+    ~Handle();
     void join();
     void start(void (*callback) (void *));
 
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/workers/Hashrate.cpp b/xmrig-mo/src/workers/Hashrate.cpp
--- a/xmrig/src/workers/Hashrate.cpp	2018-12-09 10:30:46.503520900 +0300
+++ b/xmrig-mo/src/workers/Hashrate.cpp	2018-12-09 10:29:20.150581800 +0300
@@ -48,18 +48,10 @@ inline static const char *format(double
 
 Hashrate::Hashrate(size_t threads, xmrig::Controller *controller) :
     m_highest(0.0),
-    m_threads(threads),
+    m_threads(0),
     m_controller(controller)
 {
-    m_counts     = new uint64_t*[threads];
-    m_timestamps = new uint64_t*[threads];
-    m_top        = new uint32_t[threads];
-
-    for (size_t i = 0; i < threads; i++) {
-        m_counts[i]     = new uint64_t[kBucketSize]();
-        m_timestamps[i] = new uint64_t[kBucketSize]();
-        m_top[i]        = 0;
-    }
+    set_threads(threads);
 
     const int printTime = controller->config()->printTime();
 
@@ -71,6 +63,30 @@ Hashrate::Hashrate(size_t threads, xmrig
     }
 }
 
+void Hashrate::set_threads(const size_t threads)
+{
+    if (m_threads) {
+        for (size_t i = 0; i < m_threads; i++) {
+            delete [] m_counts[i];
+            delete [] m_timestamps[i];
+        }
+        delete [] m_counts;
+        delete [] m_timestamps;
+        delete [] m_top;
+    }
+
+    m_threads = threads;
+
+    m_counts     = new uint64_t*[threads];
+    m_timestamps = new uint64_t*[threads];
+    m_top        = new uint32_t[threads];
+
+    for (size_t i = 0; i < threads; i++) {
+        m_counts[i]     = new uint64_t[kBucketSize]();
+        m_timestamps[i] = new uint64_t[kBucketSize]();
+        m_top[i]        = 0;
+    }
+}
 
 double Hashrate::calc(size_t ms) const
 {
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/workers/Hashrate.h b/xmrig-mo/src/workers/Hashrate.h
--- a/xmrig/src/workers/Hashrate.h	2018-12-09 10:30:46.504521000 +0300
+++ b/xmrig-mo/src/workers/Hashrate.h	2018-12-09 10:29:20.150581800 +0300
@@ -44,6 +44,7 @@ public:
     };
 
     Hashrate(size_t threads, xmrig::Controller *controller);
+    void set_threads(size_t threads);
     double calc(size_t ms) const;
     double calc(size_t threadId, size_t ms) const;
     void add(size_t threadId, uint64_t count, uint64_t timestamp);
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/workers/Workers.cpp b/xmrig-mo/src/workers/Workers.cpp
--- a/xmrig/src/workers/Workers.cpp	2018-12-09 10:30:46.505521000 +0300
+++ b/xmrig-mo/src/workers/Workers.cpp	2018-12-09 10:29:20.152581900 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -24,6 +25,7 @@
 #include <cmath>
 #include <inttypes.h>
 #include <thread>
+#include <string> // for MSVS std::to_string
 
 
 #include "api/Api.h"
@@ -206,6 +208,65 @@ void Workers::start(xmrig::Controller *c
     }
 }
 
+void Workers::soft_stop() // stop current workers leaving uv stuff intact (used in switch_algo)
+{
+    m_sequence = 0;
+    m_paused   = 0;
+
+    for (Handle *handle : m_workers) {
+        handle->join();
+        delete handle;
+    }
+
+    m_workers.clear();
+}
+
+// setups workers based on specified algorithm (or its basic perf algo more specifically)
+void Workers::switch_algo(const xmrig::Algorithm& algorithm)
+{
+    if (m_status.algo == algorithm.algo()) return;
+
+    soft_stop();
+
+    m_sequence = 1;
+    m_paused   = 1;
+
+    const std::vector<xmrig::IThread *> &threads = m_controller->config()->threads(algorithm.algo());
+    m_status.algo    = algorithm.algo();
+    m_status.threads = threads.size();
+
+    // string with multiway thread info
+    std::string str_threads;
+    for (const xmrig::IThread *thread : threads) {
+       if (!str_threads.empty()) str_threads = str_threads + ", ";
+       str_threads = str_threads + "x" + std::to_string(thread->multiway());
+    }
+    Log::i()->text(m_controller->config()->isColors()
+        ? GREEN_BOLD(" >>> ") WHITE_BOLD("ALGO CHANGE: ") CYAN_BOLD("%s") ", " CYAN_BOLD("%d (%s)") " thread(s)"
+        : " >>> ALGO CHANGE: %s, %d (%s) thread(s)",
+        algorithm.name(),
+        threads.size(),
+        str_threads.c_str()
+    );
+
+    m_status.ways = 0;
+    for (const xmrig::IThread *thread : threads) {
+       m_status.ways += thread->multiway();
+    }
+
+    m_hashrate->set_threads(threads.size());
+
+    uint32_t offset = 0;
+
+    for (xmrig::IThread *thread : threads) {
+        Handle *handle = new Handle(thread, offset, m_status.ways);
+        offset += thread->multiway();
+
+        m_workers.push_back(handle);
+        handle->start(Workers::onReady);
+    }
+}
+
 
 void Workers::stop()
 {
@@ -216,8 +277,8 @@ void Workers::stop()
     m_paused   = 0;
     m_sequence = 0;
 
-    for (size_t i = 0; i < m_workers.size(); ++i) {
-        m_workers[i]->join();
+    for (Handle *handle : m_workers) {
+        handle->join();
     }
 }
 
diff -durpN -x build -x '.git*' --speed-large-files -d a/xmrig/src/workers/Workers.h b/xmrig-mo/src/workers/Workers.h
--- a/xmrig/src/workers/Workers.h	2018-12-09 10:30:46.505521000 +0300
+++ b/xmrig-mo/src/workers/Workers.h	2018-12-09 10:29:20.152581900 +0300
@@ -6,6 +6,7 @@
  * Copyright 2016      Jay D Dee   <jayddee246@gmail.com>
  * Copyright 2017-2018 XMR-Stak    <https://github.com/fireice-uk>, <https://github.com/psychocrypt>
  * Copyright 2016-2018 XMRig       <https://github.com/xmrig>, <support@xmrig.com>
+ * Copyright 2018 MoneroOcean      <https://github.com/MoneroOcean>, <support@moneroocean.stream>
  *
  *   This program is free software: you can redistribute it and/or modify
  *   it under the terms of the GNU General Public License as published by
@@ -56,6 +57,8 @@ public:
     static void setEnabled(bool enabled);
     static void setJob(const Job &job, bool donate);
     static void start(xmrig::Controller *controller);
+    // setups workers based on specified algorithm (or its basic perf algo more specifically)
+    static void switch_algo(const xmrig::Algorithm&);
     static void stop();
     static void submit(const JobResult &result);
 
@@ -76,6 +79,7 @@ private:
     static void onResult(uv_async_t *handle);
     static void onTick(uv_timer_t *handle);
     static void start(IWorker *worker);
+    static void soft_stop(); // stop current workers leaving uv stuff intact (used in switch_algo)
 
     class LaunchStatus
     {


# Discussion History
## GuramDuka | 2018-12-20T10:51:29+00:00
mistake

## GuramDuka | 2018-12-20T10:51:42+00:00
mistake

# Action History
- Created by: GuramDuka | 2018-12-09T09:50:32+00:00
- Closed at: 2018-12-20T10:51:42+00:00
