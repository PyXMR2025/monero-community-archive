---
title: Wiping memory in Qt
source_url: https://github.com/monero-project/monero-gui/issues/1537
author: stoffu
assignees: []
labels: []
created_at: '2018-08-01T22:52:48+00:00'
updated_at: '2018-08-03T08:34:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Recently, the CLI code is moving towards erasing secret data (secret keys, seed, and password) from memory so that a malware etc. can't steal it, see https://github.com/monero-project/monero/pull/4131

At the heart of this scheme is a functionality to wipe data in the memory, implemented in https://github.com/monero-project/monero/blob/master/contrib/epee/src/memwipe.c

Is it possible to do the equivalent for the strings handled in the GUI?


# Discussion History
## sanderfoobar | 2018-08-02T20:20:08+00:00
 An example is the global variable `appWindow.walletPassword`:

#### Declaration:

```qml
ApplicationWindow {
    id: appWindow
    title: "Monero"
    [...]
    property var walletPassword
```

#### Assigment

https://github.com/monero-project/monero-gui/blob/2842c337592ab806303770ff927fb9751fe57c26/main.qml#L378-L383

Assigned after an `onWalletOpened` signal, emitted by:

https://github.com/monero-project/monero-gui/blob/4c2640d4b3519cede86f4392c4e3a29d6ee5a377/src/libwalletqt/WalletManager.cpp#L63-L76

So, basically whenever a wallet is opened.

#### Usage

`appWindow.walletPassword` usage in QML:

```
$ grep -ri --include="*.qml" "appwindow.walletPassword" 
./main.qml:            // console.log("opening wallet at: ", wallet_path, "with password: ", appWindow.walletPassword);
./main.qml:  appWindow.walletPassword = newPasswordDialog.password;
./wizard/WizardMain.qml:  appWindow.walletPassword = settings.wallet_password
./pages/Settings.qml:     walletManager.openWalletAsync(persistentSettings.wallet_path, appWindow.walletPassword,
./pages/Settings.qml:     if(appWindow.walletPassword === passwordDialog.password){
./pages/Settings.qml:     currentWallet.setPassword(appWindow.walletPassword)
./pages/Settings.qml:     walletManager.openWalletAsync(persistentSettings.wallet_path, appWindow.walletPassword,
```

#### Memory
Naively grepping memory for my wallet password:
```
015147d0: 0000 0000 0000 f0bf e887 41c9 6b55 0000  ..........A.kU..
015147e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
015147f0: 306c 41c9 6b55 0000 0888 41c9 6b55 0000  0lA.kU....A.kU..
01514800: 0600 0000 0000 0000 6669 6e64 6d65 0000  ........findme..
01514810: 4500 7200 7200 6f00 70d5 43c9 6b55 0000  E.r.r.o.p.C.kU..
```

Exposes wallet password `findme`

#### Solution

Create a method in WalletManager that can check a password and returns a boolean. With that, QML can decide to either prompt the user with password dialogs when it is required or cache a password result for X maximum amount of time.

Just thinking out loud. It might be more complex to solve.

## stoffu | 2018-08-03T06:18:27+00:00
@skftn 
I'm not sure we're on the same page. The main idea in the CLI is to replace `std::string` with `epee::wipeable_string` for the password's type, so that when it gets destructed at the end of scope, the memory area previously holding the string data is cleared using `memwipe()`.

In your code #1538, the string data passed from the Qt GUI is held in `const QString &password` which is then converted to `std::string` and passed to `WalletManager::openWallet()` (which then internally converts it to `epee::wipeable_string`). The concern here is that these normal string types `QString` & `std::string` don't care about wiping the memory, and the sensitive password data might remain in the memory afterwards. I think basically we don't want to use `QString::toStdString()`.

CC: @moneromooo-monero

# Action History
- Created by: stoffu | 2018-08-01T22:52:48+00:00
