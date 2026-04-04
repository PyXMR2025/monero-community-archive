---
title: 'wallet2_api.h: set proxy at runtime'
source_url: https://github.com/monero-project/monero/issues/8943
author: MrCyjaneK
assignees: []
labels: []
created_at: '2023-07-10T20:27:46+00:00'
updated_at: '2023-07-12T05:44:53+00:00'
type: issue
status: closed
closed_at: '2023-07-12T05:44:52+00:00'
---

# Original Description
Hey! I'm currently working on Anonero wallet, and I'm implementing a feature where user can switch nodes (.i2p or .onion) - and depending on which note user selects I'm setting the respective proxy.
The thing is - setProxy function appears to work only once - and then it returns 'true' despite the proxy still remaining unchanged (as can be seen in tor log - with many invalid requests to .i2p eepsites being logged).

I've tried everything I could figure out on my own before opening an issue for that.

This is the code that we use to set proxy
1)
```cpp
JNIEXPORT jboolean JNICALL
Java_com_m2049r_xmrwallet_model_WalletManager_setProxyJ(JNIEnv *env, jobject instance,
                                                       jstring address) {
    const char *_address = env->GetStringUTFChars(address, nullptr);
    bool rc =
            Monero::WalletManagerFactory::getWalletManager()->setProxy(std::string(_address));
    env->ReleaseStringUTFChars(address, _address);
    return rc;
}
// {...}
JNIEXPORT jboolean JNICALL
Java_com_m2049r_xmrwallet_model_Wallet_setProxyJ(JNIEnv *env, jobject instance,
                                                jstring address) {
    const char *_address = env->GetStringUTFChars(address, nullptr);
    Monero::Wallet *wallet = getHandle<Monero::Wallet>(env, instance);
    bool rc = wallet->setProxy(std::string(_address));
    env->ReleaseStringUTFChars(address, _address);
    return rc;
}
```

It is borrowed from the Monerujo wallet itself (as can be seen in function name)

First we use the Monero::WalletManager setProxy and then Monero::Wallet setProxy function - we also watch for errors using Monero::Wallet status() function - and it returns empty string, and both functions to setProxy return true when called.

While this is not an Issue report I'm just curious what is the proper way to use setProxy function - or if I'm missing something out.

After adding some logging this is what I get

```plain
D/NodeMethodCHannel.kt(25841): node url: ecnfc7oyzzw3jmwc2omxzccbik33wyyaofxsfow7342z6kjanq6a.b32.i2p
D/NodeMethodCHannel.kt(25841): proxy type: i2p
D/WalletManager.java(25841): setProxy(127.0.0.1:4447)
D/WalletManager.java(25841): setProxy(): success
```
despite the function being called with the I2p proxy address requests are still falling over to tor socks proxy.

# Discussion History
## selsta | 2023-07-11T16:59:11+00:00
Did you try if this works correctly in monero-gui? If yes, did you check monero-gui code?

https://github.com/monero-project/monero-gui/blob/master/src/libwalletqt/Wallet.cpp#L185-L200

## MrCyjaneK | 2023-07-12T05:44:52+00:00
Hey! This is turned out to be issue on our end - we have set node using WalletManager setDaemon function - which didn't change the connection that is already made. So proxy switched fine - I have just missidentified the issue to be with proxy and not node settings.

# Action History
- Created by: MrCyjaneK | 2023-07-10T20:27:46+00:00
- Closed at: 2023-07-12T05:44:52+00:00
