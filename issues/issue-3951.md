---
title: CLI won't prompt for password
source_url: https://github.com/monero-project/monero/issues/3951
author: krtschmr
assignees: []
labels: []
created_at: '2018-06-07T05:55:37+00:00'
updated_at: '2022-04-08T15:52:12+00:00'
type: issue
status: closed
closed_at: '2022-04-08T15:52:12+00:00'
---

# Original Description
    [wallet 44hzXT]: transfer 4***Y 0.005
    Y
    Error: invalid password

also wallet creation with hardware wallet didn't prompt for password.


edit: 

```

[wallet 44hzXT]: transfer **** 0.005

Y
No payment id is included with this transaction. Is this okay?  (Y/Yes/N/No): Y

Transaction 1/1:
Spending from address index 0
Sending 0.005000000000.  The transaction fee is 0.002320500000
Is this okay?  (Y/Yes/N/No): Transaction successfully submitted, transaction <****>
You can check its status by using the `show_transfers` command.

```

i make the transfer command, then i have to press enter - but still nothing shows. then i pressed Y and then he prompted me for confirming no payment id.

weired.

# Discussion History
## moneromooo-monero | 2018-06-07T11:45:00+00:00
What architecture and OS ?

## moneromooo-monero | 2018-06-07T12:49:43+00:00
Does https://github.com/monero-project/monero/pull/3957 fix it ?

## krtschmr | 2018-06-07T15:27:08+00:00
i'll try later to compile and will come back to you.

Win10 

## moneromooo-monero | 2018-06-18T13:02:56+00:00
ping

## stoffu | 2018-06-28T13:44:18+00:00
As far as I tested with Windows 10 on my virtual machine, the issue is only encountered when using the MSYS2 console; the issue never showed up when using the default command prompt, regardless of the change in #3957. I've tested some older releases that are still downloadable, and confirmed the same behavior with the v0.9.0 release.

It's strange that such a basic issue was reported this recently. Maybe it's due to some internal changes in MSYS2? Can some other Windows users confirm? CC: @rbrunner7 


## rbrunner7 | 2018-06-28T13:56:05+00:00
Can't say anything about this password entry problem; in my work regarding charsets and encodings in the CLI wallet I carefully did *not* touch anything related to password entry. And the difference in bevaviour between MSYS2 console input and direct OS text window ("DOS Prompt") input that I encountered and mentioned in some comment only was about charsets / encodings.

## stoffu | 2018-06-28T14:04:45+00:00
@rbrunner7 
So in your case, the MSYS2 console just prints the `Enter the password: ` prompt message? In my case, the promot message is simply not printed. I have another desktop with Windows 10 and a laptop with Windows 8, so I’ll check if I see the same phenomenon with those.

## moneromooo-monero | 2018-06-28T15:56:22+00:00
stoffu, does the patch fix it for the MSYS2 console case ?

## rbrunner7 | 2018-06-28T18:20:32+00:00
Well, I just tried on my Windows 7 system: The MSYS2 console input for passwords with 0.12.2.0 (release) is indeed pretty f\*cked-up: The prompt does not show, and worse, the typed password shows in cleartext!

I must have noticed this before, but it seems my brain just filed this under "normal Windows weirdness" and then forgot it ...

## rbrunner7 | 2018-06-28T19:20:08+00:00
@moneromooo-monero: With "patch" you mean the (already merged) #3957? If yes, that improves nothing, just compiled HEAD with freshly updated MSYS2: Still no prompt, still password entry visible. Great to correct typos while entering a password however :)

## moneromooo-monero | 2018-06-28T19:39:47+00:00
Yes. You mean you see your password when you type ? If so, file a bug.

## krtschmr | 2018-06-28T23:48:55+00:00
> Yes. You mean you see your password when you type ? If so, file a bug.

that bug is related to the current one. 

indeed, if i use regular windows shell i do have password prompt. if i use any other windows shell i wont have it.

there is no prompt. and because i know, that there is one, but just not visible, i then type in my password. CLI takes the input as my password and goes on, but the windows shell didn't cover it, so it's there in cleartext


## rbrunner7 | 2018-06-29T05:40:56+00:00
> that bug is related to the current one.

Right, it's a bug with 2 aspects, occuring only within MSYS2 shell windows on Microsoft Windows:

* Password prompt does not show
* Password entry shows in cleartext

When I investigated a charset / encoding problem occurring in the MSYS2 shell I got the impression that this thing is pretty weird; I can imagine that these password prompting and input problems may be hard or even impossible to solve. If I remember correctly,  I did not even find a way to query "Am I running in the MSYS2 shell?" in order to do something differently, and I gave up pretty quickly then ...

## moneromooo-monero | 2018-06-29T07:51:21+00:00
Please try this patch on a failing case, and paste the resulting logs:

```
diff --git a/src/common/password.cpp b/src/common/password.cpp
index 3ce2ba4..7f14108 100644
--- a/src/common/password.cpp
+++ b/src/common/password.cpp
@@ -51,6 +51,7 @@ namespace
 #if defined(_WIN32)
   bool is_cin_tty() noexcept
   {
+MGINFO("is a tty: " << _isatty(_fileno(stdin)));
     return 0 != _isatty(_fileno(stdin));
   }
 
@@ -63,7 +64,8 @@ namespace
     DWORD mode_old;
     ::GetConsoleMode(h_cin, &mode_old);
     DWORD mode_new = mode_old & ~(ENABLE_ECHO_INPUT | ENABLE_LINE_INPUT);
-    ::SetConsoleMode(h_cin, mode_new);
+    BOOL ret = ::SetConsoleMode(h_cin, mode_new);
+MGINFO("SetConsoleMode1: " << ret);
 
     bool r = true;
     pass.reserve(tools::password_container::max_password_size);
@@ -95,7 +97,8 @@ namespace
       }
     }
 
-    ::SetConsoleMode(h_cin, mode_old);
+    ret = ::SetConsoleMode(h_cin, mode_old);
+    MGINFO("SetConsoleMode2: " << ret);
 
     return r;
   }
```

## stoffu | 2018-06-29T10:09:25+00:00
@moneromooo-monero 
> stoffu, does the patch fix it for the MSYS2 console case ?

As @rbrunner7 said above, the patch #3957 did not make any difference either when using the MSYS2 console or when using the default Command Prompt.

Your above patch gave this log with MSYS2
```
2018-06-29 09:59:46.947	6448	INFO 	global	src/common/password.cpp:55	is a tty: 0
```
while it gave this log with the default Command Prompt
```
2018-06-29 10:07:25.772	8912	INFO 	global	src/common/password.cpp:55	is a tty: 64
2018-06-29 10:07:25.773	8912	INFO 	global	src/common/password.cpp:69	SetConsoleMode1: 1
2018-06-29 10:07:29.660	8912	INFO 	global	src/common/password.cpp:102	SetConsoleMode2: 1
```


## krtschmr | 2018-06-29T11:57:55+00:00
> MSYS2 shell windows on Microsoft Windows

no idea what that shell is. I have the `git shell` which u get when u install git. additional i have `MobaXTerm Professional` which i sometimes used and both have same issue.

## moneromooo-monero | 2018-06-29T13:15:01+00:00
It looks like a bug in the libc then. Does the following patch fix it ? Please also test with --password-file as it will change that code path.

```
diff --git a/src/common/password.cpp b/src/common/password.cpp
index 3ce2ba4..e1ebdd4 100644
--- a/src/common/password.cpp
+++ b/src/common/password.cpp
@@ -51,7 +51,7 @@ namespace
 #if defined(_WIN32)
   bool is_cin_tty() noexcept
   {
-    return 0 != _isatty(_fileno(stdin));
+    return true;//0 != _isatty(_fileno(stdin));
   }
 
   bool read_from_tty(epee::wipeable_string& pass)
```

## rbrunner7 | 2018-06-29T18:08:14+00:00
Unfortunately, no luck with just forcing it to "it's a tty alright": Interactive password entry immediately fails, without any output visible on the console. Log level 4 gives the following:

```
2018-06-29 18:00:39.583 18252   INFO    msgwriter       src/common/scoped_message_writer.h:102  Wallet and key files found, loading...
2018-06-29 18:00:39.583 18252   ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: failed to read wallet password
2018-06-29 18:00:39.583 18252   ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:3224  failed to open account
2018-06-29 18:00:39.583 18252   ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:7648  Failed to initialize wallet
```

Both command line switches `--password` and `--password-file` work however.

## moneromooo-monero | 2018-06-29T18:35:24+00:00
Did you have the logs for SetConsoleMode on ?

## moneromooo-monero | 2018-06-29T18:45:30+00:00
Also, try this (while still forcing isatty to 1):

```
diff --git a/src/common/password.cpp b/src/common/password.cpp
index 3ce2ba4..bdac405 100644
--- a/src/common/password.cpp
+++ b/src/common/password.cpp
@@ -58,7 +58,10 @@ namespace
   {
     static constexpr const char BACKSPACE = 8;
 
-    HANDLE h_cin = ::GetStdHandle(STD_INPUT_HANDLE);
+    //HANDLE h_cin = ::GetStdHandle(STD_INPUT_HANDLE);
+    HANDLE h_cin = CreateFile("CONIN$", GENERIC_READ,
+        FILE_SHARE_READ | FILE_SHARE_WRITE,
+        NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
 
     DWORD mode_old;
     ::GetConsoleMode(h_cin, &mode_old);

```

Found somewhere on the internet :)

## rbrunner7 | 2018-06-29T19:12:37+00:00
After stoffu, I did not do the SetConsoleMode tests myself, expecting the same result.

That alternative way to create the standard input handle starts well - it correctly shows the password prompt - but quickly goes downhill: Password input shows in cleartext; somehow the Enter key does not seem to work anymore, I cannot submit the password, I am stuck at password input; and after I leave the CLI wallet there with ^Z it gets downright crazy: bash gets all my inputs again, i.e. the password and all my seemingly unsuccessful attempts at "Enter".

I think the most uncomfortable aspect of this bug hunt is this: We can't be sure that there is a way. After all, the MSYS2 environment is pretty minimalistic. Maybe they have just implemented all calls necessary for normal cleartext input, but not a iota more...


## rbrunner7 | 2018-06-29T19:19:41+00:00
Just checked the normal Windows 7 Powershell window as well: Still works with this change, with one quite important exception: Password entry is visible.

## moneromooo-monero | 2018-06-29T19:27:02+00:00
Then the best way to "fix" this is to time input in the file case. If the first byte is not seen within a millisecond, assume it's a console, and error out prining a "bad console, use --password or --password-file" message.

## rbrunner7 | 2018-06-29T19:49:41+00:00
Sounds reasonable to me.

## moneromooo-monero | 2018-10-21T09:50:21+00:00
There was a related fix in 0e33cf89d2e351b2306e66a7d23ede880208fbee which was ending lines on \r and \n, and Windows is sending both for a single newline.

## moneromooo-monero | 2018-10-26T09:16:00+00:00
That patch above might fix it, if console and file behave different wrt newlines. Can you try ?

## rbrunner7 | 2018-10-26T16:05:08+00:00
I compiled master HEAD (which contains that patch in question, if I looked correctly) on Windows today and checked: In a PowerShell window, output and both normal and password input all work as they should. In a MSYS2 terminal window, nothing works: Input seems to never reach the wallet, which also does not output anything anymore after the gretting.

But anyway: Release 0.13 does not work in an MSYS2 terminal either (identical startup behaviour) so I don't think it's *that* patch that broke it.

My gut feeling tells me that it may be impossible to make it work both in Cmd.exe/PowerShell windows *and* in the MSYS2 terminal *and* improve on the state we had before the "experiments" began.

## selsta | 2022-04-08T15:05:44+00:00
@rbrunner7 Is this still an issue?

## rbrunner7 | 2022-04-08T15:26:04+00:00
I just checked: Cmd.exe and Powershell work, MSYS2 console doesn't; the same I found back 2018 then.

However I think getting Monero command-line tools to work inside MSYS2 console is pretty unimportant. I would say close this poor issue :)

# Action History
- Created by: krtschmr | 2018-06-07T05:55:37+00:00
- Closed at: 2022-04-08T15:52:12+00:00
