---
title: Load wallet file very slow
source_url: https://github.com/monero-project/monero/issues/8740
author: EWIT521
assignees: []
labels: []
created_at: '2023-02-11T10:34:11+00:00'
updated_at: '2023-02-23T13:55:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The process of serializing the contents of the wallet file into memory objects during the wallet file loading process at program startup is very slow, and a 600M file takes two hours.
Why is this taking so long? Is this normal? If not, what is causing the delay?

# Discussion History
## selsta | 2023-02-11T12:05:32+00:00
What kind of hardware do you have? I don't have a 600MB wallet cache file but a 60MB one takes less than a second to load. Two hours is definitely not normal.

## selsta | 2023-02-11T13:40:58+00:00
I have tried a 600MB wallet file now, doesn't take more than 2-3 seconds. Are you sure that you have enough free RAM?

## EWIT521 | 2023-02-12T06:17:55+00:00
The machine has 32 GB of memory, and during the serialization process there seems to be an issue. Can you provide any insight or suggestion as to what might be causing this?
log:
2023-02-12 02:18:32.202	    7f1bda7e7640	INFO	wallet.wallet2	src/wallet/wallet2.cpp:5474	Trying to decrypt cache data
2023-02-12 02:18:32.497	    7f1bda7e7640	INFO	wallet.wallet2	src/wallet/wallet2.cpp:5478	wallet2::load----serialization::parse_binary end size :626166864
2023-02-12 02:18:43.950	    7f1bda7e7640	INFO	wallet.wallet2	src/wallet/wallet2.cpp:5482	wallet2::load---- cache_data--decrypt end
2023-02-12 02:18:43.951	    7f1bda7e7640	INFO	wallet.wallet2	src/wallet/wallet2.cpp:5489	wallet2::load---- cache_data-- serialize 111
![image](https://user-images.githubusercontent.com/22743089/218296214-25ab6f1a-a951-431f-b4f8-f20b9165edb6.png)



## selsta | 2023-02-12T16:27:21+00:00
Which wallet are you using? Which version are you using? Where did you get the binaries?

## EWIT521 | 2023-02-13T02:30:30+00:00
Problems with slow file loading:
The loaded file is a data wallet file containing transaction information; 
monero-wallet-cli,The version is monero-x86_64-linux-gnu-v0.18.0.0;
The file source is the monero-wallet-cli  export

## selsta | 2023-02-13T02:32:45+00:00
Does the same issue exist with v0.18.1.2?

## EWIT521 | 2023-02-13T02:36:21+00:00
Not tried  v0.18.1.2

## EWIT521 | 2023-02-13T02:51:49+00:00
Using version is  v0.18.0.0 ,Have not tried v0.18.1.2 

## EWIT521 | 2023-02-14T01:52:13+00:00
The reason for the slow loading of the wallet has been found. It is because m_subaddresses and m_subaddress_labels have 10.7 million records each, while the actual subaddress is only more than 50,000. How should it be optimized?

## selsta | 2023-02-14T02:54:29+00:00
Is this an exchange wallet?

## EWIT521 | 2023-02-14T04:47:10+00:00
Only one wallet file that contains all wallet addresses, self-created and exchange

## moneromooo-monero | 2023-02-14T14:59:33+00:00
https://github.com/monero-project/monero/pull/5370 is likely to speedup loads, it uses a flat vector to store subaddresses. Doesn't do anything for labels, but since most labels are probably empty, I'll make another patch that omits those altogether.
5370 is years old, doesn't apply anymore, I'll push a fresh version soon.

## moneromooo-monero | 2023-02-14T16:56:20+00:00
5370 is now rebased to current master. Let us know if you get any speedup. I'll look at what we can do for labels now.

## moneromooo-monero | 2023-02-14T17:06:35+00:00
BTW, this will make your wallet cache incompatible with current master or release, so only use this on a COPY of your wallet cache.

## moneromooo-monero | 2023-02-14T17:27:17+00:00
Oh, and you want to try loading it with this code after it's been saved with this code, so it then loads the new format, not the old one plus conversion.

## moneromooo-monero | 2023-02-14T17:56:10+00:00
Pushed again with serialization fixes, serialization changed to use monero instead of boost since 2019.

## rbrunner7 | 2023-02-14T18:21:02+00:00
> The reason for the slow loading of the wallet has been found. It is because m_subaddresses and m_subaddress_labels have 10.7 million records each, while the actual subaddress is only more than 50,000. How should it be optimized?

I don't understand. Do you mean you definitely do not have 10 million subaddresses, not even remotely that many, only somewhat over 50,000, yet if you look at the map and the vector, they have 10 million elements each?

If yes, something does not square here, if you ask me.

## moneromooo-monero | 2023-02-15T08:52:13+00:00
Actually, it doesn't work yet, can't load old wallet caches. I'll fix.

## moneromooo-monero | 2023-02-15T09:13:17+00:00
Fixed.

## moneromooo-monero | 2023-02-15T09:15:40+00:00
That said, I tried with a 900 MB cache (5k accounts, 5k subaddresses per account), and it loads in less than 30 seconds with current master. So that doesn't seem to be your problem.
Run "sudo perf top -a" while loading, paste the first dozen lines after waiting for it to settle.

## moneromooo-monero | 2023-02-15T09:26:25+00:00
In fact, on that 5k/5k wallet, loading the subaddress data takes very little time in the first place, after adding timing code.

## moneromooo-monero | 2023-02-15T22:22:34+00:00
I tried a similar thing for labels, but it turns out it gains nothing, as labels are already implicitely optimized out.

## EWIT521 | 2023-02-16T02:00:45+00:00
Thanks for all the replies above，I'll run the test again and see the result

## EWIT521 | 2023-02-17T09:40:20+00:00
Using Java to invoke an  xmr so library to load a wallet file and serialize 100 million sub-addresses is very slow.

## moneromooo-monero | 2023-02-17T09:44:49+00:00
Wait. Is it our code you're using or someone else's ? Just making sure :D

## EWIT521 | 2023-02-17T17:30:13+00:00
you have a Discord account for convenient Do chatting? 

## moneromooo-monero | 2023-02-17T22:38:24+00:00
No, IRC on the libera.chat network in #monero is appropriate. It's accessible via matrix.

## EWIT521 | 2023-02-20T06:21:19+00:00
Modify the monero code compilation output  a Library ,then java integration that ,loading  monero wallet very slow 

## EWIT521 | 2023-02-21T03:00:35+00:00
When the Java calls monero  library of SO to load the wallet file, the prompt loading failed malloc. Memory allocation failed, then through ulimit to modify the max lockmemory size, change 64 to 102400. After modification, the wallet can be loaded normally, but it is very slow when serializing 10 million sub-addresses.


## EWIT521 | 2023-02-21T03:02:52+00:00
system's The memory is adequate.

## EWIT521 | 2023-02-23T13:02:54+00:00
The program started running, and the process of serializing 10 million subaddresses while loading the wallet was very slow, taking 2 hours and 9 minutes
Here is the code and log
When serializing 10 million sub-addresses, print the first ten logs and the last ten logs
The first and last ten times take 1 millisecond respectively
Why is serialization so slow?
Is there a problem with the serialization process? 
Is there a problem with the stored data of the subaddress?

![image](https://user-images.githubusercontent.com/22743089/220913733-c129204d-bdee-4542-a62d-2009571f8b7d.png)

![1lNHEcGast](https://user-images.githubusercontent.com/22743089/220913787-6897cfe4-0e64-4de5-85a9-08503c949e0c.jpg)


## moneromooo-monero | 2023-02-23T13:55:02+00:00
You were asked two things (try with the patch linked, and post the output of perf top), which you ignored. Asking the same thing again will not help. The perf top output is likely the one most likely to help determine where the issue lies.

# Action History
- Created by: EWIT521 | 2023-02-11T10:34:11+00:00
