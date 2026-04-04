---
title: Monero-wallet-rpc ignores --max-log-files
source_url: https://github.com/monero-project/monero/issues/7049
author: normoes
assignees: []
labels: []
created_at: '2020-12-01T08:15:55+00:00'
updated_at: '2022-02-20T13:17:53+00:00'
type: issue
status: closed
closed_at: '2022-02-19T01:03:23+00:00'
---

# Original Description
Hi,

I am talking about `monero-wallet-rpc`, version `v0.17.1.5`.


I am using the cli option `--max-log-files 3` to reduce the number of log files.

I noticed that `monero-wallet-rpc` is ignoring this option - It happily keeps on creating log files.

This option works when used with `monerod`.

---

I noticed this behaviour in combination with [this issue](https://github.com/monero-project/monero/issues/7048).

Initialising this wallet seems to produce a LOT of logs.

# Discussion History
## moneromooo-monero | 2020-12-07T01:18:13+00:00
Works for me. You can try this patch to see what it does:

```
diff --git a/contrib/epee/src/mlog.cpp b/contrib/epee/src/mlog.cpp
index bcde215be..4cc287cef 100644
--- a/contrib/epee/src/mlog.cpp
+++ b/contrib/epee/src/mlog.cpp
@@ -164,6 +164,7 @@ void mlog_configure(const std::string &filename_base, bool console, const std::s
   el::Loggers::addFlag(el::LoggingFlag::ColoredTerminalOutput);
   el::Loggers::addFlag(el::LoggingFlag::StrictLogFileSizeCheck);
   el::Helpers::installPreRollOutCallback([filename_base, max_log_files](const char *name, size_t){
+printf("rollout: %s\n", name);
     std::string rname = generate_log_filename(filename_base.c_str());
     int ret = rename(name, rname.c_str());
     if (ret < 0)
@@ -171,6 +172,7 @@ void mlog_configure(const std::string &filename_base, bool console, const std::s
       // can't log a failure, but don't do the file removal below
       return;
     }
+printf("max_log_files: %zu\n", max_log_files);
     if (max_log_files != 0)
     {
       std::vector<boost::filesystem::path> found_files;
@@ -185,6 +187,7 @@ void mlog_configure(const std::string &filename_base, bool console, const std::s
           found_files.push_back(iter->path());
         }
       }
+printf("%zu found with base %s\n", found_files.size(), filename_base.c_str());
       if (found_files.size() >= max_log_files)
       {
         std::sort(found_files.begin(), found_files.end(), [](const boost::filesystem::path &a, const boost::filesystem::path &b) {
@@ -208,6 +211,7 @@ void mlog_configure(const std::string &filename_base, bool console, const std::s
         {
           try
           {
+printf("removing %s\n", found_files[i].c_str());
             boost::system::error_code ec;
             boost::filesystem::remove(found_files[i], ec);
             if (ec)
```

## moneromooo-monero | 2020-12-07T01:18:52+00:00
I used: --max-log-files 2 --max-log-file-size 4096 --log-level 2

## selsta | 2022-02-19T01:03:23+00:00
Closing as there was no reply from the issue creator.

## normoes | 2022-02-20T13:17:52+00:00
It's fine now.

Thanks for the reminder.

# Action History
- Created by: normoes | 2020-12-01T08:15:55+00:00
- Closed at: 2022-02-19T01:03:23+00:00
