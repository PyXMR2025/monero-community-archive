---
title: Monero GUI Wallet (Android) Local Node Won't Start/Has Error
source_url: https://github.com/monero-project/monero-gui/issues/3492
author: ghost
assignees: []
labels: []
created_at: '2021-05-21T02:05:13+00:00'
updated_at: '2021-07-06T00:03:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I ran the Android build for the Monero GUI wallet, loaded it on my phone, and, while the remote node is working fine, I'm unable to get the local node to work.  

(Issue 1?) When I press 'Start Daemon', an error screen pops up saying the Monerod executable is missing: 
![image](https://user-images.githubusercontent.com/84093240/119070263-4307d680-b9ad-11eb-9f09-79d986c2c399.png)

(Issue 2) Additionally, and this may or may not be related, when I click 'Blockchain Location (Change)', and I press the 'Select this Folder' button in my phone (the external drive folder), I get prompted by Android to 'Allow this app to access current and future content in this folder', and when I press OK, I get this screen in the GUI: 
![image](https://user-images.githubusercontent.com/84093240/119070392-85311800-b9ad-11eb-9f02-7581607ec82e.png)

(Issue 3) This was the case without choosing a folder as well as choosing the folder.  Beyond that, selecting a folder doesn't make the text in the text in the input below 'Blockchain location' to change.  It remains as (default) no matter what folder I select in the Android File UI.  

Just want to say that I was thrilled to see that these build instructions were available in the repo (thank you, guys!), and I know there are numerous people who would be spinning up a full node on their Android phones if there was a simple way to make this happen (The GUI is 95% of the way there and would totally solve this).  Looking forward to creating and distributing how-to content on this process.  


# Discussion History
## selsta | 2021-05-21T02:06:55+00:00
AFAIK Android only supports remote node currently. We should disable local node option on Android until support for it has been added.

## ghost | 2021-05-21T02:49:49+00:00
It's probably not that big of a deal as it's not easy to acquire the APK at the moment (and not really much reason to), but I will say that there are likely a Lot of people with old phones that would definitely be able to add full/pruned nodes to the network if there were an easy way to do this, and none of the major wallets (cake, monerujo, mymonero) support that ability.  Would love to see Monero GUI be able to fill that role.  

As an aside, the local node seems to start magically kind of 'working' (at least it shows connectivity and load bars appearing in the sidebar) if I have Monerod running totally separately in Termux on the phone.

## NacJidtyd6op | 2021-06-10T14:59:53+00:00
Hi!
sed -i 's/monerod"/monerod_arm64-v8a.so"/g' src/daemon/DaemonManager.cpp

on dockerfile u add 

&& rm /monero-gui/build/Android/release/android-build/build/outputs/apk/debug/android-build-debug.apk \
&& mv /monero-gui/build/Android/release/android-build/libs/arm64-v8a/monerod /monero-gui/build/Android/release/android-build/libs/arm64-v8a/monerod_arm64-v8a.so \
&& ./gradlew assembleDebug

WIll be perfect if anyone knows how to compile qt6 for android.

Size of apk will be smaller(useful for old smartphones) and execution much faster.



## NacJidtyd6op | 2021-06-10T15:02:23+00:00
u'll need sd >= 128gb

i tried and works.

## ghost | 2021-07-06T00:03:12+00:00
@selsta @NacJidtyd6op Just want to confirm that this solution is working for me as well.  My last few lines of the Dockerfile.android file: 

```
    && PATH=${HOST_PATH} make generate_translations_header \
    && make -j${THREADS} -C src \
    && mv /monero-gui/build/Android/release/android-build/libs/arm64-v8a/monerod /monero-gui/build/Android/release/android-build/libs/arm64-v8a/monerod_arm64-v8a.so \
    && make -j${THREADS} apk \
```
I'm able to install the monero-gui.apk on my phone and the GUI is synchronizing as usual- no errors.   

# Action History
- Created by: ghost | 2021-05-21T02:05:13+00:00
