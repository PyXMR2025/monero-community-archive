---
title: Haiku OS R1 / Can't compile / hwloc issue
source_url: https://github.com/xmrig/xmrig/issues/3231
author: FSOL-XDAG
assignees: []
labels: []
created_at: '2023-03-24T22:09:47+00:00'
updated_at: '2025-11-14T07:30:55+00:00'
type: issue
status: closed
closed_at: '2023-03-28T08:48:45+00:00'
---

# Original Description
Hi everybody ! 

G33k challenge : I've try to compile XMRig 6.19.1 on Haiku OS (BeOS fork). Very nice OS if you want to discover something different than Windows & Linux.

Here are the commands I typed:

```
pkgman install cmake automake libtool autoconf
mkdir temp && cd temp
git clone https://github.com/xmrig/xmrig.git
mkdir xmrig/build && cd xmrig/scripts
./build_deps.sh && cd ../build
```

It crash on 'hwloc' : 

![image](https://user-images.githubusercontent.com/128682335/227652171-a1f8fef0-12d2-4926-a448-d2b9edc002ca.png)

Before that, I was informed about this possible issue : 

![image](https://user-images.githubusercontent.com/128682335/227651933-347e676d-c040-4ab2-a331-3bca9089510b.png)

On Haiku forum, someone tell me : 

> You can try to install hwloc from the depot aswell, maybe the build system allows select system provided libs instead of the in-tree version.

Please find complete log beside. 

[haiku_log.txt](https://github.com/xmrig/xmrig/files/11066898/haiku_log.txt)
Does anybody knows ? How to "install hwloc from the deposit" ? 

Thanks for your help ! Best regards.

# Discussion History
## SChernykh | 2023-03-25T07:17:59+00:00
If hwloc doesn't support it, it will probably not work even if you manage to compile it. It's better to compile XMRig without hwloc - remove hwloc related lines from build_deps.sh and run `cmake .. -DWITH_HWLOC=OFF` when building XMRig.

## FSOL-XDAG | 2023-03-27T08:43:36+00:00
Ok, hwloc is ignore. But another problem occured with OpenSSL. 

![image](https://user-images.githubusercontent.com/128682335/227889939-398594a5-9ffb-4cb6-910b-64759ffda1fc.png)

Don't you have any idea about this ?


## SChernykh | 2023-03-27T09:13:06+00:00
It's OpenSSL config script that fails, so it's not supported too. Remove OpenSSL from build_deps.sh and try `-DWITH_TLS=OFF` when building XMRig.

## FSOL-XDAG | 2023-03-27T13:12:53+00:00
First of all, I sought some help from the Haiku community. Apparently, the hwloc and openssl libs are already installed in the system, although it crashes at compile time (check 's' before their name) : 

![image](https://user-images.githubusercontent.com/128682335/227945636-57a2819c-3ddd-496a-86a9-8a7f6b5f2e92.png)

Nevertheless, I applied your advice. I removed hwloc & openssl from build_deps.sh : 

![image](https://user-images.githubusercontent.com/128682335/227946180-e95a7111-885c-46cb-897c-d5f1d5551b50.png)

Then I run build_deps.sh but something went wrong ...

Check this logfile : [xmrigscripts .build_deps_log.txt](https://github.com/xmrig/xmrig/files/11078890/xmrigscripts.build_deps_log.txt)

Nevertheless, I run `cmake .. -DWITH_TLS=OFF -DWITH_DHWLOC` and it's fails :

![image](https://user-images.githubusercontent.com/128682335/227947769-d98043aa-2711-4338-b9a3-f00485d1b916.png)

May I conclude "mission impossible to compile XMRig on this OS" ?
 

## SChernykh | 2023-03-27T13:21:13+00:00
But did you also add `-DXMRIG_DEPS=scripts/deps` to cmake command line? It's in the [instructions](https://xmrig.com/docs/miner/build/ubuntu) for the advanced build with build_deps.sh

And you should run `cmake .. -DWITH_TLS=OFF -DWITH_HWLOC=OFF -DXMRIG_DEPS=scripts/deps` from xmrig/build folder, not from scripts folder.

## FSOL-XDAG | 2023-03-27T13:36:37+00:00
Oh my bad, I correct theses. So cmake ok, then make have issue : 

![image](https://user-images.githubusercontent.com/128682335/227954277-4a868b8f-6b97-4f7e-a398-488203f18a0b.png)



## SChernykh | 2023-03-27T14:02:53+00:00
This is what I expected. XMRig doesn't know this OS, so it defaults to code that has never been compiled before. To remove all references to byteswap.h, add `-DWITH_KAWPOW=OFF -DWITH_HTTP=OFF` to cmake command line.

## FSOL-XDAG | 2023-03-27T14:16:29+00:00
Yes, this OS is very "uncommon", but very very pretty & light ! You can find it freely here : [Haiku download page](https://www.haiku-os.org/get-haiku/r1beta4/)

So things are better, but ... 

![image](https://user-images.githubusercontent.com/128682335/227972005-1666701e-1881-4548-ba75-5bd65264d23b.png)

This is the result log : 

[cmake_make_haiku.txt](https://github.com/xmrig/xmrig/files/11079625/cmake_make_haiku.txt)


## SChernykh | 2023-03-27T16:05:24+00:00
It looks like you're out of luck at this point. Basically any OS-dependent code in XMRig fails to compile, and XMRig uses a lot of it to optimize performance.

## FSOL-XDAG | 2023-03-27T19:00:37+00:00
What is your advice? Should I give up? I suppose that for your team there is no interest in studying this operating system ready to port XMRig, yet it has all the right features. It's a shame. I would have been proud to open it to CPU mining. 

## SChernykh | 2023-03-27T19:03:32+00:00
It will definitely require a big rewrite to make it compile.

## FSOL-XDAG | 2023-03-28T08:48:45+00:00
All right, so there's no need to waste time on that. Thanks for trying to help me! Much appreciated. 👍 

## Begasus | 2025-11-14T07:30:55+00:00
With latest support by user @user0-07161 it's possible to launch xmrig now on Haiku, thanks for taking a look at us! 👍 

<img width="897" height="549" alt="Image" src="https://github.com/user-attachments/assets/691f84da-1f77-49db-beea-7bbd43b29387" />

# Action History
- Created by: FSOL-XDAG | 2023-03-24T22:09:47+00:00
- Closed at: 2023-03-28T08:48:45+00:00
