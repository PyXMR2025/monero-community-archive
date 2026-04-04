---
title: '15.0.0 Error: Unerwarteter Fehler:boost::too_many_args: format-string referred
  to fewer arguments than were passed '
source_url: https://github.com/monero-project/monero/issues/6136
author: elrippo
assignees: []
labels: []
created_at: '2019-11-14T22:00:46+00:00'
updated_at: '2022-02-19T04:49:41+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:49:41+00:00'
---

# Original Description
Dear all,

running Kubuntu 16.04 64bit, updated from 14.1.0 to 15.0.0 on 12.11.2019 via the downloaded binaries from getmonero.org cli only.
While triying to do  a payment via XMR.to and copy pasting the transfer command for the cli in the format [transfer address ammount] after entering the password for the wallet i get the error [Error: Unerwarteter Fehler:boost::too_many_args: format-string referred to fewer arguments than were passed]

Switching back to the 14.1.0 binaries with the same transfer command from XMR.to the payment is successfuly done.

If you need any additional info or debug info, please let me know how to do this and i will be happy to provide.

Kind regards,
elrippo

# Discussion History
## moneromooo-monero | 2019-11-14T23:01:22+00:00
Do you have file/line ? It might be in the log file, in an exception stack trace.

## elrippo | 2019-11-15T07:40:15+00:00
Dear moneromooo-monero,
i did the same again with loglevel -4 on the wallet, if you need the whole log file, let me know.

`2019-11-15 07:35:54.577     7f3c283e8780        ERROR   wallet.simplewallet     src/simplewallet/simplewallet.cpp:624   unexpected error: boost::too_many_args: format-string referred to fewer arguments than were passed
2019-11-15 07:35:54.577     7f3c283e8780        ERROR   msgwriter       src/common/scoped_message_writer.h:102  Error: Unerwarteter Fehler:boost::too_many_args: format-string`

## elrippo | 2019-11-15T10:01:23+00:00
Just got a notification, and i have to express, that i am using the cli wallet, not the gui wallet, so which wizzard should i open?

---quote---
Go to the wizard, select "Change wallet mode" and then select Advanced mode.

Open you wallet again, go to Settings -> Node -> Select remote node and enter the following:

Address: uwillrunanodesoon.moneroworld.com
Port: 18089

This should work.
---unquote---

## selsta | 2019-11-15T10:19:34+00:00
I commented on the wrong issue, sorry :)

## elrippo | 2019-11-15T10:33:01+00:00
Ok

## moneromooo-monero | 2019-11-15T11:43:10+00:00
Does it happen if you with with "LANG=C" (ie, run in default english) ?

## elrippo | 2019-11-15T12:13:22+00:00
No, if i turn LANG=C the transaction is done. Default on my system is "de_AT.utf8"

## moneromooo-monero | 2019-11-15T13:06:59+00:00
Then one of the de_AT translations messed up a format strings. Please run again with the default and log level 2, then paste the last dozen lines of the log before the error. You can take out any private info in there, I'm interested in finding out where wallet2 stopped running.

## moneromooo-monero | 2019-11-15T13:07:30+00:00
Actually nvm I can do that here.

## moneromooo-monero | 2019-11-15T13:25:27+00:00
Actually I cannot. I can send a tx with the monero_de.ts translations.

## elrippo | 2019-11-15T14:52:55+00:00
Here you go
[monero-wallet-cli-boost.log](https://github.com/monero-project/monero/files/3852001/monero-wallet-cli-boost.log)


## moneromooo-monero | 2019-11-15T15:20:12+00:00
This might fix it:
```
diff --git a/translations/monero_de.ts b/translations/monero_de.ts
index 8d25c4795..68a134a45 100644
--- a/translations/monero_de.ts
+++ b/translations/monero_de.ts
@@ -3446,7 +3446,7 @@ By using &apos;sync&apos; processing of waiting messages with multisig sync info
         <source>
 Input %llu/%llu (%s): amount=%s</source>
         <translation>
-Eingabe &amp;llu/%llu (%s): Betrag=%s</translation>
+Eingabe %lu/%llu (%s): Betrag=%s</translation>
     </message>
     <message>
         <location filename="../src/simplewallet/simplewallet.cpp" line="5814"/>
```

After applying, you need to apply #6139 too. Then:
mv translations/ready translations/notready
./utils/translations/build-translations.sh
mv translations/notready translations/ready

## moneromooo-monero | 2019-11-19T11:11:19+00:00
ping

## elrippo | 2019-11-20T00:09:39+00:00
Sorry, had a quite high workload.
Thank you for your offer, but i believe i quite do not understand everything i should do, so maybe you could tell me what this means, were and when i should do this.

index 8d25c4795..68a134a45 100644
--- a/translations/monero_de.ts
+++ b/translations/monero_de.ts
@@ -3446,7 +3446,7 @@ By using &apos;sync&apos; processing of waiting messages with multisig sync info
         <source>
 Input %llu/%llu (%s): amount=%s</source>
         <translation>
-Eingabe &amp;llu/%llu (%s): Betrag=%s</translation>
+Eingabe %lu/%llu (%s): Betrag=%s</translation>
     </message>
     <message>
         <location filename="../src/simplewallet/simplewallet.cpp" line="5814"/>


and this one
mv translations/ready translations/notready
./utils/translations/build-translations.sh
mv translations/notready translations/ready


## moneromooo-monero | 2019-11-20T15:09:41+00:00
You apply the patch with:

- save the patch into a file, say "format.diff"
- run: patch -p1 < format.diff
- run: mv translations/ready translations/notready
- run: ./utils/translations/build-translations.sh
- run: mv translations/notready translations/ready
- build again
- run the wallet
- do what command used to break


## elrippo | 2019-11-24T13:31:36+00:00
If i execute diff` --git a/translations/monero_de.ts b/translations/monero_de.ts i get the error Unknown option: --diff


## elrippo | 2019-12-03T05:45:56+00:00
ping

## moneromooo-monero | 2019-12-03T12:05:29+00:00
Well, why are you executing this in the first place ? It's not something I asked you to do, and it's not a valid command, so...

## elrippo | 2019-12-04T05:47:54+00:00
Well, then tell me how to save the patch, then we would be faster with this...

## dEBRUYNE-1 | 2019-12-04T07:50:53+00:00
@elrippo - See first point of this comment:

https://github.com/monero-project/monero/issues/6136#issuecomment-556045133

## moneromooo-monero | 2019-12-04T10:18:54+00:00
Run an editor, paste the patch into it, save, select a filename. Exact steps will depend on your editor.


## moneromooo-monero | 2019-12-05T14:07:57+00:00
Oh, I see why you tried to run that command, it's the first line of the patch :)
You don't run it, you apply it, by following the steps in my comment above.
You run the resulting binary as normal.

## moneromooo-monero | 2020-05-16T16:14:37+00:00
Guess this could be closed until someone trips on it again ?

# Action History
- Created by: elrippo | 2019-11-14T22:00:46+00:00
- Closed at: 2022-02-19T04:49:41+00:00
