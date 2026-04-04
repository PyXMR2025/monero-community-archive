---
title: '[bug] Cold Signing not possible between 64-bit (ubuntu) and armv7(ubuntu)'
source_url: https://github.com/monero-project/monero/issues/3319
author: nasaWelder
assignees: []
labels: []
created_at: '2018-02-26T19:30:23+00:00'
updated_at: '2022-04-08T14:42:33+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:42:33+00:00'
---

# Original Description
The cli's on either machine reject the outputs and key images from the other machine.
"Error: Outputs from man_outs2 are for a different account"

On the 64-bit, cli can import/export outputs/key_images between a synced watch-only, and freshly made full wallet with no accounts setup, or subadresses made:

    [wallet 9wXvk8 (no daemon)]: import_outputs man_outs2
    44 outputs imported


on arm, 7 with a freshly made full wallet with no accounts setup, or subadresses made: 

    [wallet 9wXvk8 (no daemon)]: import_outputs man_outs2
    "Error: Outputs from man_outs2 are for a different account"


Hot setup:
Monero cli: Monero 'Helium Hydra' (v0.11.1.0-master-d4e728c)
(ubuntu mate) $ uname -a
Linux devarea-Inspiron-1545 4.13.0-36-generic #40~16.04.1-Ubuntu SMP Fri Feb 16 23:25:58 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

Cold setup:
Monero cli: Monero 'Helium Hydra' (v0.11.0.0-90bc15d)
(ubuntu mate)$ uname -a
Linux devarea2-desktop 4.4.38-v7+ #938 SMP Thu Dec 15 15:22:21 GMT 2016 armv7l armv7l armv7l GNU/Linux

# Discussion History
## stoffu | 2018-02-27T04:27:01+00:00
If you generate subaddresses on both computers, do you get the same results? Recently I realized that there's an endianness bug in the subaddress generation code. But it seems like the endianness is the same for both x86_64 and ARMv7?

## nasaWelder | 2018-02-27T05:00:57+00:00
Yes same error, I had used a wallet with subaddresses first before trying
with fresh wallets. The fresh 64 bit full wallet worked fine.

On Feb 26, 2018 9:27 PM, "Stoffu Noether" <notifications@github.com> wrote:

> If you generate subaddresses on both computers, do you get the same
> results? Recently I realized that there's an endianness bug in the
> subaddress generation code. But it seems like the endianness is the same
> for both x86_64 and ARMv7?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3319#issuecomment-368743462>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AgV3M3tvVoOctBf8ZiowGMm7vQfwGeRTks5tY4QfgaJpZM4STyuo>
> .
>


## stoffu | 2018-02-27T05:10:18+00:00
> Yes same error

Sorry for being unclear, but my question is: do you get the same *subaddress* for the same index on both computers, or not?


## nasaWelder | 2018-02-27T05:36:11+00:00
Just generated 6 subaddresses for accounts 0 to 3, all matched.

On Feb 26, 2018 10:10 PM, "Stoffu Noether" <notifications@github.com> wrote:

> Yes same error
>
> No, my question is: do you get the same *address*, or not?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3319#issuecomment-368749472>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AgV3M3OWd0cy5r8v5w2vTAkvjB1wrPmhks5tY45DgaJpZM4STyuo>
> .
>


## stoffu | 2018-02-27T05:49:25+00:00
That's what I expected, thanks. So the bug must be somewhere else.

The error seems like something obvious. Can you apply this patch and see what it prints?

```diff
diff --git a/src/simplewallet/simplewallet.cpp b/src/simplewallet/simplewallet.cpp
index c67a6bc6..b08f2648 100644
--- a/src/simplewallet/simplewallet.cpp
+++ b/src/simplewallet/simplewallet.cpp
@@ -6524,6 +6524,8 @@ bool simple_wallet::import_outputs(const std::vector<std::string> &args)
   if (public_spend_key != keys.m_spend_public_key || public_view_key != keys.m_view_public_key)
   {
     fail_msg_writer() << "Outputs from " << filename << " are for a different account";
+    fail_msg_writer() << "Public spend key: got " << public_spend_key << ", expected " << keys.m_spend_public_key;
+    fail_msg_writer() << "Public view key: got " << public_view_key << ", expected " << keys.m_view_public_key;
     return true;
   }
```
Do you see something funny?

## nasaWelder | 2018-02-27T06:02:19+00:00
Ooh l'll have to set up a dev environment to apply that. Perhaps I can crash course that this week. I was just using the latest successful build from build.getmonero.org for testing a Python gui/wrapper I made. (Above is all manually done as a human at CLI, though) so standby, I guess.

## moneromooo-monero | 2018-03-02T18:53:15+00:00
Do you get any exception reading the files ? They'd appear in the log only.

## nasaWelder | 2018-03-27T21:48:03+00:00
@moneromooo-monero There is nothing useful in the logs, even after `set_log 4`

> 2018-03-27 21:53:54.089	        76f83000	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: Outputs from /home/devarea2/Desktop/manual_outputs are for a different account

@stoffu I can't find a buidable armv7 commit to work from. I tried this:

`git reset --hard 7a9a4a666986589dff679d086b377a9dfaa99d69`

`make`

...


> [ 12%] Linking CXX static library libcncrypto.a
> make[3]: Leaving directory '/home/devarea2/dev/monero/build/release'
> [ 12%] Built target cncrypto
> make[3]: Entering directory '/home/devarea2/dev/monero/build/release'
> Scanning dependencies of target epee
> make[3]: Leaving directory '/home/devarea2/dev/monero/build/release'
> make[3]: Entering directory '/home/devarea2/dev/monero/build/release'
> [ 12%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/hex.cpp.o
> [ 12%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o
> c++: internal compiler error: Killed (program cc1plus)
> Please submit a full bug report,
> with preprocessed source if appropriate.
> See <file:///usr/share/doc/gcc-5/README.Bugs> for instructions.
> contrib/epee/src/CMakeFiles/epee.dir/build.make:86: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o' failed
> make[3]: *** [contrib/epee/src/CMakeFiles/epee.dir/http_auth.cpp.o] Error 4
> make[3]: Leaving directory '/home/devarea2/dev/monero/build/release'
> CMakeFiles/Makefile2:273: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/all' failed
> make[2]: *** [contrib/epee/src/CMakeFiles/epee.dir/all] Error 2
> make[2]: Leaving directory '/home/devarea2/dev/monero/build/release'
> Makefile:138: recipe for target 'all' failed
> make[1]: *** [all] Error 2
> make[1]: Leaving directory '/home/devarea2/dev/monero/build/release'
> Makefile:62: recipe for target 'release-all' failed
> make: *** [release-all] Error 2



## stoffu | 2018-03-27T23:23:11+00:00
> c++: internal compiler error: Killed (program cc1plus)

This error message probably means that your machine doesn't have enough memory for compiling the code. Try increasing the swap file size: https://github.com/monero-project/monero#on-the-raspberry-pi


## moneromooo-monero | 2018-08-15T11:41:03+00:00
> Error: Outputs from /home/devarea2/Desktop/manual_outputs are for a different account

This is odd. Are you sure it's the right wallet ? Keys are always little endian, 32 bytes, so reading/writing those should not depend on the arch.

## moneromooo-monero | 2018-10-02T18:46:19+00:00
For someone with both platforms to test with:

+hacktoberfest

## selsta | 2022-04-08T14:42:33+00:00
Should be fixed with #7321

If not, a new issue can be opened or I'll reopen this one.

# Action History
- Created by: nasaWelder | 2018-02-26T19:30:23+00:00
- Closed at: 2022-04-08T14:42:33+00:00
