---
title: CLI wallet stuck at creating wallet with windows10 new console
source_url: https://github.com/monero-project/monero/issues/3401
author: Lafudoci
assignees: []
labels: []
created_at: '2018-03-14T13:48:49+00:00'
updated_at: '2018-03-28T10:00:54+00:00'
type: issue
status: closed
closed_at: '2018-03-28T10:00:54+00:00'
---

# Original Description
The screen hanged at creating wallet while listing seed languages

![cmd stuck](https://user-images.githubusercontent.com/10460270/37405459-9e34dea4-27cf-11e8-88f3-3b31676fad1a.PNG)

But I found if I switch the cmd to legacy console, it works without this issue.
(this pic is from web, mine is in Chinese)
![legacy-cmd-console](https://user-images.githubusercontent.com/10460270/37405643-2133fb3c-27d0-11e8-87b0-a29f4cc63ff8.png)
![cmd no stuck](https://user-images.githubusercontent.com/10460270/37405668-30d405d2-27d0-11e8-8dfd-c058dad9f829.PNG)

I believe it's about screen (output?) issue. Because if I press 1 and enter, it can still generate wallet file. 
Here is the log while stuck: https://pastebin.mozilla.org/9079987
OS: Win10 x64 1709

# Discussion History
## moneromooo-monero | 2018-03-14T14:11:13+00:00
You mean it seems to work normally, except there's no output after the startup ?
Seed languages have some non ASCII characters, that might confuse it if it misinterprets them (ie, it thinks it's control codes and not UTF-8).

## Lafudoci | 2018-03-14T14:17:09+00:00
Yes, it seems works (observe by the log) if I blindly type command. I tried switch to UTF-8 but same issue.

## Lafudoci | 2018-03-14T14:20:42+00:00
BTW, if I open an existing wallet, it works normally. This issue only happens in generating wallet for me.  I have 2+ friends replicated the same issue on their win10.

## moneromooo-monero | 2018-03-14T15:09:07+00:00
See if this patches fixes it. It avoids printing the language names on the screen:

```
diff --git a/src/simplewallet/simplewallet.cpp b/src/simplewallet/simplewallet.cpp
index edfb05d..737b41c 100644
--- a/src/simplewallet/simplewallet.cpp
+++ b/src/simplewallet/simplewallet.cpp
@@ -3100,7 +3100,7 @@ std::string simple_wallet::get_mnemonic_language()
   std::vector<std::string>::iterator it;
   for (it = language_list.begin(), ii = 0; it != language_list.end(); it++, ii++)
   {
-    std::cout << ii << " : " << *it << std::endl;
+    //std::cout << ii << " : " << *it << std::endl;
   }
   while (language_number < 0)
   {

```


## Lafudoci | 2018-03-14T16:15:58+00:00
Yes, that change fixes it.

## moneromooo-monero | 2018-03-17T10:44:24+00:00
If you undo the test change above, and revert 430268224d71bfc6a359f20c6db712462ce0bb25 ("git revert 430268224d71bfc6a359f20c6db712462ce0bb25"), does this fix it too ?

## moneromooo-monero | 2018-03-17T23:18:06+00:00
In the meantime, there is a workaround in https://github.com/monero-project/monero/pull/3426

## Lafudoci | 2018-03-18T14:09:52+00:00
The git revert 4302682 doesn't fix. I'll try the workaround.

## Lafudoci | 2018-03-28T03:10:01+00:00
The workaround in #3426 works good.

## moneromooo-monero | 2018-03-28T09:56:51+00:00
Thanks. It's been merged already. A long term fix will be needed, if we find a windows coder who gets the problem.

+resolved


# Action History
- Created by: Lafudoci | 2018-03-14T13:48:49+00:00
- Closed at: 2018-03-28T10:00:54+00:00
