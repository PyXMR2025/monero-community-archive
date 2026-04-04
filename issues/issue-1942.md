---
title: './monero-wallet-gui'': double free or corruption (fasttop): 0x0000000005989cf0 '
source_url: https://github.com/monero-project/monero/issues/1942
author: grigio
assignees: []
labels: []
created_at: '2017-03-29T22:49:00+00:00'
updated_at: '2017-04-02T10:59:49+00:00'
type: issue
status: closed
closed_at: '2017-04-02T10:59:49+00:00'
---

# Original Description
Hi, I got this from Monero GUI beta2 on Linux x64 while I switched from a wallet file to another one.

```
2017-03-30 00:40:48.812	    7efe0cae9700	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:1392	!r. THROW EXCEPTION: error::no_connection_to_daemon
*** Error in `./monero-wallet-gui': double free or corruption (fasttop): 0x0000000005989cf0 ***
======= Backtrace: =========
/lib/x86_64-linux-gnu/libc.so.6(+0x777e5)[0x7efe224b87e5]
/lib/x86_64-linux-gnu/libc.so.6(+0x7fe0a)[0x7efe224c0e0a]
/lib/x86_64-linux-gnu/libc.so.6(cfree+0x4c)[0x7efe224c498c]
./monero-wallet-gui[0x1bd438f]
./monero-wallet-gui[0x1bc9172]
./monero-wallet-gui[0x459089]
./monero-wallet-gui[0x1c307c3]
./monero-wallet-gui[0x1c39b82]
./monero-wallet-gui[0x432a55]
./monero-wallet-gui[0x432ad9]
./monero-wallet-gui[0x429120]
./monero-wallet-gui[0x42e54d]
./monero-wallet-gui[0x1a4117b]
./monero-wallet-gui[0x1a44b95]
/lib/x86_64-linux-gnu/libpthread.so.0(+0x76ba)[0x7efe22b1a6ba]
/lib/x86_64-linux-gnu/libc.so.6(clone+0x6d)[0x7efe2254782d]
======= Memory map: ========
00400000-02aa6000 r-xp 00000000 fc:00 66195756                           /home/grigio/Apps/monero-gui-0.10.3.1-beta2/monero-wallet-gui
02ca6000-02d7a000 r--p 026a6000 fc:00 66195756                           /home/grigio/Apps/monero-gui-0.10.3.1-beta2/monero-wallet-gui
02d7a000-02d92000 rw-p 0277a000 fc:00 66195756                           /home/grigio/Apps/monero-gui-0.10.3.1-beta2/monero-wallet-gui
02d92000-02db0000 rw-p 00000000 00:00 0 
037b3000-05bfa000 rw-p 00000000 00:00 0                                  [heap]
7efdd8000000-7efdd8021000 rw-p 00000000 00:00 0 
7efdd8021000-7efddc000000 ---p 00000000 00:00 0 
7efddc000000-7efdde25d000 rw-p 00000000 00:00 0 
7efdde25d000-7efde0000000 ---p 00000000 00:00 0 
7efde0000000-7efde2273000 rw-p 00000000 00:00 0 
7efde2273000-7efde4000000 ---p 00000000 00:00 0 
7efde4000000-7efde4021000 rw-p 00000000 00:00 0 
7efde4021000-7efde8000000 ---p 00000000 00:00 0 
7efdec000000-7efdecb9f000 rw-p 00000000 00:00 0 
7efdecb9f000-7efdf0000000 ---p 00000000 00:00 0 
7efdf77ff000-7efdf7800000 ---p 00000000 00:00 0 
7efdf7800000-7efdf8000000 rw-p 00000000 00:00 0 
7efdf8000000-7efdfa019000 rw-p 00000000 00:00 0 
7efdfa019000-7efdfc000000 ---p 00000000 00:00 0 
7efdfc074000-7efdfc075000 ---p 00000000 00:00 0 
7efdfc075000-7efdfc875000 rw-p 00000000 00:00 0 
7efdfc875000-7efdfc876000 ---p 00000000 00:00 0 
7efdfc876000-7efdfd076000 rw-p 00000000 00:00 0 
7efdfd076000-7efdfd077000 ---p 00000000 00:00 0 
7efdfd077000-7efdfd877000 rw-p 00000000 00:00 0 
7efdfd877000-7efdfd878000 ---p 00000000 00:00 0 
7efdfd878000-7efdfe078000 rw-p 00000000 00:00 0 
7efdfe07d000-7efdfe07e000 rw-s 11d85e000 00:06 249                       /dev/dri/card0
7efdfe07e000-7efdff260000 r--p 00000000 fc:00 28576021                   /usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc
7efdff2ed000-7efdff3ed000 rw-s 10d5f5000 00:06 249                       /dev/dri/card0
7efdff3ed000-7efdff3ee000 rw-s 11ab67000 00:06 249                       /dev/dri/card0
7efdff465000-7efdff466000 rw-s 10604b000 00:06 249                       /dev/dri/card0
7efdff4cd000-7efdff5cd000 rw-s 12399f000 00:06 249                       /dev/dri/card0
7efdff5cd000-7efdff6c9000 rw-s 00000000 00:05 10190881                   /SYSV00000000 (deleted)
7efdff6ec000-7efdff760000 rw-s 00000000 00:05 10321938                   /SYSV00000000 (deleted)
7efdff760000-7efdff763000 rw-s 11141c000 00:06 249                       /dev/dri/card0
7efdff763000-7efdff765000 rw-s 11141a000 00:06 249                       /dev/dri/card0
7efdff7c9000-7efdff7e0000 r-xp 00000000 fc:00 73143530                   /lib/x86_64-linux-gnu/libresolv-2.23.so
7efdff7e0000-7efdff9e0000 ---p 00017000 fc:00 73143530                   /lib/x86_64-linux-gnu/libresolv-2.23.so
7efdff9e0000-7efdff9e1000 r--p 00017000 fc:00 73143530                   /lib/x86_64-linux-gnu/libresolv-2.23.so
7efdff9e1000-7efdff9e2000 rw-p 00018000 fc:00 73143530                   /lib/x86_64-linux-gnu/libresolv-2.23.so
7efdff9e2000-7efdff9e4000 rw-p 00000000 00:00 0 
7efdff9e4000-7efdff9e9000 r-xp 00000000 fc:00 73143573                   /lib/x86_64-linux-gnu/libnss_dns-2.23.so
7efdff9e9000-7efdffbe9000 ---p 00005000 fc:00 73143573                   /lib/x86_64-linux-gnu/libnss_dns-2.23.so
7efdffbe9000-7efdffbea000 r--p 00005000 fc:00 73143573                   /lib/x86_64-linux-gnu/libnss_dns-2.23.so
7efdffbea000-7efdffbeb000 rw-p 00006000 fc:00 73143573                   /lib/x86_64-linux-gnu/libnss_dns-2.23.so
7efdffbeb000-7efdffbed000 r-xp 00000000 fc:00 73142682                   /lib/x86_64-linux-gnu/libnss_mdns4_minimal.so.2
7efdffbed000-7efdffdec000 ---p 00002000 fc:00 73142682                   /lib/x86_64-linux-gnu/libnss_mdns4_minimal.so.2
7efdffdec000-7efdffded000 r--p 00001000 fc:00 73142682                   /lib/x86_64-linux-gnu/libnss_mdns4_minimal.so.2
7efdffded000-7efdffdee000 rw-p 00002000 fc:00 73142682                   /lib/x86_64-linux-gnu/libnss_mdns4_minimal.so.2
7efdffdee000-7efdffdf9000 r-xp 00000000 fc:00 73142920                   /lib/x86_64-linux-gnu/libnss_files-2.23.so
7efdffdf9000-7efdffff8000 ---p 0000b000 fc:00 73142920                   /lib/x86_64-linux-gnu/libnss_files-2.23.so
7efdffff8000-7efdffff9000 r--p 0000a000 fc:00 73142920                   /lib/x86_64-linux-gnu/libnss_files-2.23.so
7efdffff9000-7efdffffa000 rw-p 0000b000 fc:00 73142920                   /lib/x86_64-linux-gnu/libnss_files-2.23.so
7efdffffa000-7efe00000000 rw-p 00000000 00:00 0 
7efe00000000-7efe0002c000 rw-p 00000000 00:00 0 
7efe0002c000-7efe04000000 ---p 00000000 00:00 0 
7efe04000000-7efe04031000 rw-p 00000000 00:00 0 
7efe04031000-7efe08000000 ---p 00000000 00:00 0 
7efe08000000-7efe0802d000 rw-p 00000000 00:00 0 
7efe0802d000-7efe0c000000 ---p 00000000 00:00 0 
7efe0c000000-7efe0c001000 rw-s 10604a000 00:06 249                       /dev/dri/card0
7efe0c00f000-7efe0c010000 rw-s 10aced000 00:06 249                       /dev/dri/card0
7efe0c010000-7efe0c014000 rw-s 10ace9000 00:06 249                       /dev/dri/card0
7efe0c014000-7efe0c015000 rw-s 10ace8000 00:06 249                       /dev/dri/card0
7efe0c017000-7efe0c018000 rw-s 11d7f9000 00:06 249                       /dev/dri/card0
7efe0c01c000-7efe0c01d000 rw-p 00000000 00:00 0 
7efe0c01d000-7efe0c01e000 rw-s 10ace7000 00:06 249                       /dev/dri/card0
7efe0c02e000-7efe0c030000 rw-s 10a105000 00:06 249                       /dev/dri/card0
7efe0c030000-7efe0c033000 rw-s 121939000 00:06 249                       /dev/dri/card0
7efe0c033000-7efe0c03c000 rw-s 1167a4000 00:06 249                       /dev/dri/card0
7efe0c03c000-7efe0c03e000 rw-s 10d5f3000 00:06 249                       /dev/dri/card0
7efe0c03e000-7efe0c040000 rw-s 10d2a3000 00:06 249                       /dev/dri/card0
7efe0c040000-7efe0c045000 rw-s 10d4ee000 00:06 249                       /dev/dri/card0
7efe0c045000-7efe0c046000 rw-s 10bcff000 00:06 249                       /dev/dri/card0
7efe0c046000-7efe0c049000 rw-s 121936000 00:06 249                       /dev/dri/card0
7efe0c049000-7efe0c04b000 rw-s 10b98a000 00:06 249                       /dev/dri/card0
7efe0c04b000-7efe0c04d000 rw-s 10b988000 00:06 249                       /dev/dri/card0
7efe0c04d000-7efe0c04f000 rw-s 10f32c000 00:06 249                       /dev/dri/card0
7efe0c04f000-7efe0c050000 rw-s 11dac3000 00:06 249                       /dev/dri/card0
7efe0c052000-7efe0c055000 rw-s 121933000 00:06 249                       /dev/dri/card0
7efe0c055000-7efe0c071000 r--s 00000000 fc:00 29114761                   /usr/share/icons/gnome/icon-theme.cache
7efe0c071000-7efe0c081000 rw-s 11b75e000 00:06 249                       /dev/dri/card0
7efe0c081000-7efe0c083000 rw-s 10ba89000 00:06 249                       /dev/dri/card0
7efe0c083000-7efe0c085000 rw-s 10ba87000 00:06 249                       /dev/dri/card0
7efe0c087000-7efe0c088000 rw-s 11075e000 00:06 249                       /dev/dri/card0
7efe0c088000-7efe0c08a000 rw-s 121236000 00:06 249                       /dev/dri/card0
7efe0c08a000-7efe0c08c000 rw-s 10f35a000 00:06 249                       /dev/dri/card0
7efe0c08c000-7efe0c090000 rw-s 1167ad000 00:06 249                       /dev/dri/card0
7efe0c090000-7efe0c095000 rw-s 10f355000 00:06 249                       /dev/dri/card0
7efe0c095000-7efe0c0ae000 r--s 00000000 fc:00 29098871                   /usr/share/icons/Adwaita/icon-theme.cache
7efe0c0ae000-7efe0c0b0000 rw-s 121eba000 00:06 249                       /dev/dri/card0
7efe0c0b0000-7efe0c0b2000 rw-s 121234000 00:06 249                       /dev/dri/card0
7efe0c0b3000-7efe0c0b5000 rw-s 10b996000 00:06 249                       /dev/dri/card0
7efe0c0b5000-7efe0c0b7000 rw-s 10bcf8000 00:06 249                       /dev/dri/card0
7efe0c0b7000-7efe0c0be000 r--s 00000000 fc:00 29114671                   /usr/share/icons/hicolor/icon-theme.cache
7efe0c0be000-7efe0c0c0000 rw-s 121057000 00:06 249                       /dev/dri/card0
7efe0c0c0000-7efe0c0c2000 rw-s 12084f000 00:06 249                       /dev/dri/card0
7efe0c0c3000-7efe0c0c5000 rw-s 121ec2000 00:06 249                       /dev/dri/card0
7efe0c0c5000-7efe0c0c7000 rw-s 122a57000 00:06 249                       /dev/dri/card0
7efe0c0c7000-7efe0c0c8000 rw-s 11da11000 00:06 249                       /dev/dri/card0
7efe0c0c8000-7efe0c0c9000 rw-s 10a6d4000 00:06 249                       /dev/dri/card0
7efe0c0ca000-7efe0c0cc000 rw-s 10aa61000 00:06 249                       /dev/dri/card0
7efe0c0cc000-7efe0c0cd000 rw-s 10dc53000 00:06 249                       /dev/dri/card0
7efe0c0cd000-7efe0c0ce000 rw-s 12074a000 00:06 249                       /dev/dri/card0
7efe0c0cf000-7efe0c0d1000 rw-s 10bbe8000 00:06 249                       /dev/dri/card0
7efe0c0d1000-7efe0c0d3000 rw-s 11d627000 00:06 249                       /dev/dri/card0
7efe0c0d4000-7efe0c0d6000 rw-s 10bcef000 00:06 249                       /dev/dri/card0
7efe0c0d6000-7efe0c0d8000 rw-s 121fc9000 00:06 249                       /dev/dri/card0
7efe0c0d8000-7efe0c0e8000 rwxp 00000000 00:00 0 
7efe0c0e8000-7efe0c2e9000 rw-p 00000000 00:00 0 
7efe0c2e9000-7efe0c2ea000 ---p 00000000 00:00 0 
7efe0c2ea000-7efe0caea000 rw-p 00000000 00:00 0 
7efe0caea000-7efe0caeb000 ---p 00000000 00:00 0 
7efe0caeb000-7efe0d2ec000 rw-p 00000000 00:00 0 
7efe0d2ec000-7efe0d2ee000 rw-s 121fd2000 00:06 249                       /dev/dri/card0
7efe0d2ee000-7efe0d2f0000 rw-s 10b98c000 00:06 249                       /dev/dri/card0
7efe0d2f0000-7efe0d2f1000 rw-s 120748000 00:06 249                       /dev/dri/card0
7efe0d2f1000-7efe0d2f3000 rw-s 10dd38000 00:06 249                       /dev/dri/card0
7efe0d2f3000-7efe0d2f4000 rw-s 10dc3f000 00:06 249                       /dev/dri/card0
7efe0d2f5000-7efe0d2f7000 rw-s 121fc7000 00:06 249                       /dev/dri/card0
7efe0d2f7000-7efe0d2f9000 rw-s 11e33b000 00:06 249                       /dev/dri/card0
7efe0d2f9000-7efe0d2fa000 rw-s 10b826000 00:06 249                       /dev/dri/card0
7efe0d2fa000-7efe0d2fb000 rw-s 120740000 00:06 249                       /dev/dri/card0
7efe0d2fb000-7efe0d2fc000 rw-s 10a576000 00:06 249                       /dev/dri/card0
7efe0d2fc000-7efe0d2fe000 rw-s 10a573000 00:06 249                       /dev/dri/card0
7efe0d2fe000-7efe0d300000 rw-s 1201a7000 00:06 249                       /dev/dri/card0
7efe0d300000-7efe0d301000 rw-p 00000000 00:00 0 
7efe0d301000-7efe0d302000 rw-s 11679e000 00:06 249                       /dev/dri/card0
7efe0d302000-7efe0d303000 rw-s 116792000 00:06 249                       /dev/dri/card0
7efe0d303000-7efe0d304000 rw-s 121932000 00:06 249                       /dev/dri/card0
7efe0d304000-7efe0d306000 rw-s 10b880000 00:06 249                       /dev/dri/card0
7efe0d306000-7efe0d308000 rw-s 10aa5a000 00:06 249                       /dev/dri/card0
7efe0d308000-7efe0d30a000 rw-s 121fc3000 00:06 249                       /dev/dri/card0
7efe0d30a000-7efe0d30c000 rw-s 10b986000 00:06 249                       /dev/dri/card0
7efe0d30c000-7efe0d30e000 rw-s 1060c2000 00:06 249                       /dev/dri/card0
7efe0d30e000-7efe0d310000 rw-p 00000000 00:00 0 
7efe0d310000-7efe0d311000 rw-s 10ba84000 00:06 249                       /dev/dri/card0
7efe0d311000-7efe0d312000 rw-s 121931000 00:06 249                       /dev/dri/card0
7efe0d312000-7efe0d313000 rw-s 11f7fc000 00:06 249                       /dev/dri/card0
7efe0d313000-7efe0d314000 rw-s 11a9b6000 00:06 249                       /dev/dri/card0
7efe0d314000-7efe0d315000 rw-s 10bbe0000 00:06 249                       /dev/dri/card0
7efe0d315000-7efe0d316000 rw-s 120f55000 00:06 249                       /dev/dri/card0
7efe0d316000-7efe0d317000 rw-s 110960000 00:06 249                       /dev/dri/card0
7efe0d317000-7efe0d318000 rw-s 11e4e1000 00:06 249                       /dev/dri/card0
7efe0d318000-7efe0d319000 rw-s 121fc6000 00:06 249                       /dev/dri/card0
7efe0d319000-7efe0d31a000 rw-s 11a9b2000 00:06 249                       /dev/dri/card0
7efe0d31a000-7efe0d31b000 rw-s 120f54000 00:06 249                       /dev/dri/card0
7efe0d31b000-7efe0d31c000 rw-s 10aa51000 00:06 249                       /dev/dri/card0
7efe0d31c000-7efe0d31d000 rw-s 121fc5000 00:06 249                       /dev/dri/card0
7efe0d31d000-7efe0d31f000 rw-s 1167b1000 00:06 249                       /dev/dri/card0
7efe0d31f000-7efe0d320000 rw-s 10aa50000 00:06 249                       /dev/dri/card0
7efe0d320000-7efe0d32b000 r-xp 00000000 00:00 0 
7efe0d32b000-7efe0d4f9000 rw-p 00000000 00:00 0 
7efe0d4f9000-7efe0d4fa000 ---p 00000000 00:00 0 
7efe0d4fa000-7efe0dd3c000 rw-p 00000000 00:00 0 
7efe0dd3c000-7efe0dde8000 r--p 00000000 fc:00 28576079                   /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
7efe0dde8000-7efe0ddf8000 rw-p 00000000 00:00 0 
7efe0ddf8000-7efe0de1a000 r--p 00000000 fc:00 28576120                   /usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf
7efe0de1a000-7efe0de25000 r-xp 00000000 00:00 0 
7efe0de25000-7efe0e026000 rw-p 00000000 00:00 0 
7efe0e026000-7efe0e028000 r-xp 00000000 00:00 0 
7efe0e028000-7efe0e093000 rw-p 00000000 00:00 0 
7efe0e093000-7efe0e094000 ---p 00000000 00:00 0 
7efe0e094000-7efe0eba0000 rw-p 00000000 00:00 0 
7efe0eba0000-7efe0ebc3000 r--p 00000000 fc:00 28576123                   /usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf
7efe0ebc3000-7efe0ec7c000 r--p 00000000 fc:00 28576080                   /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
7efe0ec7c000-7efe0ec87000 r--s 00000000 fc:00 33816682                   /var/cache/fontconfig/945677eb7aeaf62f1d50efc3fb3ec7d8-le64.cache-6
7efe0ec87000-7efe0ec8d000 r--s 00000000 fc:00 33827221                   /var/cache/fontconfig/2cd17615ca594fa2959ae173292e504c-le64.cache-6
7efe0ec8d000-7efe0ec8e000 r--s 00000000 fc:00 33827220                   /var/cache/fontconfig/0d8c3b2ac0904cb8a57a757ad11a4a08-le64.cache-6
7efe0ec8e000-7efe0eca3000 r--s 00000000 fc:00 33827207                   /var/cache/fontconfig/04aabc0a78ac019cf9454389977116d2-le64.cache-6
7efe0eca3000-7efe0eca4000 r--s 00000000 fc:00 33827204                   /var/cache/fontconfig/1ac9eb803944fde146138c791f5cc56a-le64.cache-6
7efe0eca4000-7efe0eca8000 r--s 00000000 fc:00 33827203                   /var/cache/fontconfig/385c0604a188198f04d133e54aba7fe7-le64.cache-6
7efe0eca8000-7efe0ecad000 r--s 00000000 fc:00 33827167                   /var/cache/fontconfig/8801497958630a81b71ace7c5f9b32a8-le64.cache-6
7efe0ecad000-7efe0ecb4000 r--s 00000000 fc:00 33826891                   /var/cache/fontconfig/3047814df9a2f067bd2d96a2b9c36e5a-le64.cache-6
7efe0ecb4000-7efe0ecc7000 r--s 00000000 fc:00 33825753                   /var/cache/fontconfig/d52a8644073d54c13679302ca1180695-le64.cache-6
7efe0ecc7000-7efe0ed35000 r-xp 00000000 fc:00 73142707                   /lib/x86_64-linux-gnu/libpcre.so.3.13.2
7efe0ed35000-7efe0ef35000 ---p 0006e000 fc:00 73142707                   /lib/x86_64-linux-gnu/libpcre.so.3.13.2
7efe0ef35000-7efe0ef36000 r--p 0006e000 fc:00 73142707                   /lib/x86_64-linux-gnu/libpcre.so.3.13.2
7efe0ef36000-7efe0ef37000 rw-p 0006f000 fc:00 73142707                   /lib/x86_64-linux-gnu/libpcre.so.3.13.2
7efe0ef37000-7efe0ef58000 r-xp 00000000 fc:00 73142646                   /lib/x86_64-linux-gnu/liblzma.so.5.0.0
7efe0ef58000-7efe0f157000 ---p 00021000 fc:00 73142646                   /lib/x86_64-linux-gnu/liblzma.so.5.0.0
7efe0f157000-7efe0f158000 r--p 00020000 fc:00 73142646                   /lib/x86_64-linux-gnu/liblzma.so.5.0.0
7efe0f158000-7efe0f159000 rw-p 00021000 fc:00 73142646                   /lib/x86_64-linux-gnu/liblzma.so.5.0.0
7efe0f159000-7efe0f178000 r-xp 00000000 fc:00 73142736                   /lib/x86_64-linux-gnu/libselinux.so.1
7efe0f178000-7efe0f377000 ---p 0001f000 fc:00 73142736                   /lib/x86_64-linux-gnu/libselinux.so.1
7efe0f377000-7efe0f378000 r--p 0001e000 fc:00 73142736                   /lib/x86_64-linux-gnu/libselinux.so.1
7efe0f378000-7efe0f379000 rw-p 0001f000 fc:00 73142736                   /lib/x86_64-linux-gnu/libselinux.so.1
7efe0f379000-7efe0f37b000 rw-p 00000000 00:00 0 
7efe0f37b000-7efe0f3c5000 r-xp 00000000 fc:00 73142536                   /lib/x86_64-linux-gnu/libdbus-1.so.3.14.6
7efe0f3c5000-7efe0f5c5000 ---p 0004a000 fc:00 73142536                   /lib/x86_64-linux-gnu/libdbus-1.so.3.14.6
7efe0f5c5000-7efe0f5c6000 r--p 0004a000 fc:00 73142536                   /lib/x86_64-linux-gnu/libdbus-1.so.3.14.6
7efe0f5c6000-7efe0f5c7000 rw-p 0004b000 fc:00 73142536                   /lib/x86_64-linux-gnu/libdbus-1.so.3.14.6
7efe0f5c7000-7efe0f5c8000 ---p 00000000 00:00 0 
7efe0f5c8000-7efe0fdc8000 rw-p 00000000 00:00 0 
7efe0fdc8000-7efe0fdff000 r-xp 00000000 fc:00 27534568                   /usr/lib/x86_64-linux-gnu/libtxc_dxtn_s2tc.so.0.0.0
7efe0fdff000-7efe0fffe000 ---p 00037000 fc:00 27534568                   /usr/lib/x86_64-linux-gnu/libtxc_dxtn_s2tc.so.0.0.0
7efe0fffe000-7efe0ffff000 r--p 00036000 fc:00 27534568                   /usr/lib/x86_64-linux-gnu/libtxc_dxtn_s2tc.so.0.0.0
7efe0ffff000-7efe10000000 rw-p 00037000 fc:00 27534568                   /usr/lib/x86_64-linux-gnu/libtxc_dxtn_s2tc.so.0.0.0
7efe10000000-7efe1069c000 rw-p 00000000 00:00 0 
7efe1069c000-7efe14000000 ---p 00000000 00:00 0 
7efe14000000-7efe14001000 r--s 00000000 fc:00 33827183                   /var/cache/fontconfig/dc05db6664285cc2f12bf69c139ae4c3-le64.cache-6./start-gui.sh: riga 5: 17692 Annullato               (core dump creato) ./monero-wallet-gui
```

# Discussion History
## ghost | 2017-03-31T00:45:11+00:00
If this pertains to the GUI, the correct Github is here: https://github.com/monero-project/monero-core

## grigio | 2017-03-31T07:39:15+00:00
I run GUI but the error is raised from https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L1392

## moneromooo-monero | 2017-04-02T08:25:08+00:00
Pretty likely due to the use of a wallet object in two separate threads without locking. Please file in the GUI repo as xmr-eric said.

# Action History
- Created by: grigio | 2017-03-29T22:49:00+00:00
- Closed at: 2017-04-02T10:59:49+00:00
