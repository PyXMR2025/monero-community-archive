---
title: 'Discussion: Consider a non-home-directory for gui log file'
source_url: https://github.com/monero-project/monero-gui/issues/1690
author: ascandella
assignees: []
labels: []
created_at: '2018-10-21T13:47:41+00:00'
updated_at: '2018-12-29T21:02:29+00:00'
type: issue
status: closed
closed_at: '2018-12-29T21:02:29+00:00'
---

# Original Description
Not sure if I'm just super anal, but I hate having programs put stuff in my home directory. I'm aware of the flag, but I like being able to launch with `rofi` (or whatever graphical program people like). I've even gone so far as to install my own `.desktop` file to override.

I'm sure there's been discussion, but can't find it here. How about ~/.<something> -- or is the idea to keep things as user friendly as we can. (Similarly, I store my wallets in ~/.local/Monero

# Discussion History
## sanderfoobar | 2018-10-21T22:11:10+00:00
Agreed. So there are 3 platforms to consider; Windows/OSX/Linux.

Not sure where to store such a file on Windows. Probably in `%appdata%`? As for *nix; somewhere in (or at) `~/.` would be best.

For people that want to dive into it; the code responsible for determining the log path can be observed [here](https://github.com/monero-project/monero-gui/blob/master/Logger.cpp)

Pinging @pazos for opinions

## dEBRUYNE-1 | 2018-10-22T14:04:54+00:00
Why not stick with the old "write in the same directory as `monero-wallet-gui`"? 

## ascandella | 2018-10-22T15:59:21+00:00
> Why not stick with the old "write in the same directory as `monero-wallet-gui`"?

I think the problem with this is that some package managers (for example, I install via Arch) write the binary into `/usr/bin`, which isn't a good place for logs.

## ascandella | 2018-10-22T16:27:57+00:00
I'm more than happy to dive in the code (and test on linux/windows) if we
can come to an agreeable solution. I assume that's actually the sticking
point, otherwise this would have been done already :)

On Sun, Oct 21, 2018 at 3:11 PM xmrdsc <notifications@github.com> wrote:

> Agreed. So there are 3 platforms to consider; Windows/OSX/Linux.
>
> I have no idea where to store such a file on Windows. Probably somewhere
> in %appdata%?
>
> As for *nix; somewhere in (or at) ~/. would be best.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero-gui/issues/1690#issuecomment-431708723>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAF7PwxQBfvXRtB_NkrAUxiJurtE5Qt_ks5unPEBgaJpZM4Xyd9c>
> .
>


## scoobybejesus | 2018-10-25T17:32:45+00:00
What about keeping it with the blockchain? ~/.bitmonero/GUI-logs, or just ~/.bitmonero

## xiphon | 2018-10-25T21:25:24+00:00
> Not sure where to store such a file on Windows. Probably in `%appdata%`? 

Right, %APPDATA% is the correct place to keep the logs on Windows.



## ascandella | 2018-10-27T04:38:54+00:00
OK, so how do we proceed? I'm new to contributing, do I just make a pull request that changes it to ~/.bitmonero and %APPDATA%, or does somebody need to agree that this is a change that is desired, and not just my personal preference.

## pazos | 2018-10-28T15:39:04+00:00
@scoobybejesus 

> What about keeping it with the blockchain? ~/.bitmonero/GUI-logs, or just ~/.bitmonero

Can't remember if the folder is created if doesn't exists (like when running against a remote node)

@xiphon @sectioneight 
> OK, so how do we proceed? I'm new to contributing, do I just make a pull request that changes it to ~/.bitmonero and %APPDATA%, or does somebody need to agree that this is a change that is desired, and not just my personal preference.

for windows using QStandardPaths::standardLocations(QStandardPaths::AppDataLocation).at(0) (like we are doing for Android/iOS) should work. It will try to write the log on `C:/Users/<USER>/AppData/Roaming/<APPNAME>/<LOGNAME>`

for linux please test if it works with
`QStandardPaths::standardLocations(QStandardPaths::HomeLocation).at(0) + "/.bitmonero"` if that folder does not exists. If it doesn't work then we can try with 
`QStandardPaths::standardLocations(QStandardPaths::AppDataLocation).at(0)` like everything else. It should write the logs on `~/.local/share/<APPNAME>/<LOGNAME>`

Documentation is on http://doc.qt.io/qt-5/qstandardpaths.html. Please double check that the log is under home path since we don't allow other users to read our logfile, which should contain sensitive data.


## pazos | 2018-10-28T17:54:15+00:00
easiest patch will be:
```
diff --git a/Logger.cpp b/Logger.cpp
index 660bafc..28fdbb5 100644
--- a/Logger.cpp
+++ b/Logger.cpp
@@ -8,14 +8,10 @@
 
 // default log path by OS (should be writable)
 static const QString default_name = "monero-wallet-gui.log";
-#if defined(Q_OS_ANDROID) || defined(Q_OS_IOS)
-    static const QString osPath = QStandardPaths::standardLocations(QStandardPaths::AppDataLocation).at(0);
-#elif defined(Q_OS_WIN)
-    static const QString osPath = QCoreApplication::applicationDirPath();
-#elif defined(Q_OS_MAC)
+#if defined(Q_OS_MAC)
     static const QString osPath = QStandardPaths::standardLocations(QStandardPaths::HomeLocation).at(0) + "/Library/Logs";
-#else // linux + bsd
-    static const QString osPath = QStandardPaths::standardLocations(QStandardPaths::HomeLocation).at(0);
+#else
+    static const QString osPath = QStandardPaths::standardLocations(QStandardPaths::AppDataLocation).at(0);
 #endif
```

Please test this on windows/linux

## scoobybejesus | 2018-10-29T01:06:32+00:00
FYI, this is from the opening stdout sequence when starting monero-wallet-cli:

`Logging to ./monero-wallet-cli.log`  

EDIT: from Lubuntu 16.04

# Action History
- Created by: ascandella | 2018-10-21T13:47:41+00:00
- Closed at: 2018-12-29T21:02:29+00:00
