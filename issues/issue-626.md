---
title: Too small font sizes in some places
source_url: https://github.com/monero-project/monero-gui/issues/626
author: villabacho
assignees: []
labels:
- resolved
created_at: '2017-03-28T08:11:37+00:00'
updated_at: '2018-12-18T10:09:31+00:00'
type: issue
status: closed
closed_at: '2018-12-18T10:09:31+00:00'
---

# Original Description
These are the places where I observed this:

![image](https://cloud.githubusercontent.com/assets/6043551/24395102/bb214f20-139e-11e7-9d92-5e3b5e78fd54.png)

![image](https://cloud.githubusercontent.com/assets/6043551/24395117/cc22d92e-139e-11e7-9710-852110b4fb2b.png)

![image](https://cloud.githubusercontent.com/assets/6043551/24395126/dacfb6fe-139e-11e7-8fce-405de10180e7.png)

![image](https://cloud.githubusercontent.com/assets/6043551/24395137/e62bba20-139e-11e7-8186-bc1cfbbb9151.png)


# Discussion History
## villabacho | 2017-03-28T08:12:10+00:00
Observed on OpenSuSE 42.2 with QT_SCALE_FACTOR=0.7

## Jaqueeee | 2017-03-28T14:43:36+00:00
Thanks for reporting this. Seem to be some issues with certain GPU's and high DPI scaling. 
What's your graphics card and screen resolution? @villabacho 

## Jaqueeee | 2017-03-28T14:47:58+00:00
@villabacho And. If you built yourself, which Qt version do you have installed? Do you have any issues with other Qt applications?

## villabacho | 2017-03-28T15:37:10+00:00
@Jaqueeee These screenshots were made using the 2560x1440 external display on my notebook.
The notebook is a Lenovo X250 with Intel graphics (Intel HD 5500). As said earlier, I'm running OpenSuSE 42.2, and I use the Xfce desktop if that matters. I'm not running other Qt5 applications, only Qt4 stuff as far as I can tell.

I did not compile myself, I downloaded the build from the link that you provided list night in #monero-dev.

I saw that some font libraries are dynamically linked instead of statically, maybe that's a problem? Here's the output of "ldd monero-wallet-gui" on my system:

	linux-vdso.so.1 (0x00007ffda52c7000)
	libxcb-glx.so.0 => /usr/lib64/libxcb-glx.so.0 (0x00007f632a2bd000)
	libX11-xcb.so.1 => /usr/lib64/libX11-xcb.so.1 (0x00007f632a0bb000)
	libxcb.so.1 => /usr/lib64/libxcb.so.1 (0x00007f6329e9a000)
	libfontconfig.so.1 => /usr/lib64/libfontconfig.so.1 (0x00007f6329c5c000)
	libfreetype.so.6 => /usr/lib64/libfreetype.so.6 (0x00007f63299bf000)
	libX11.so.6 => /usr/lib64/libX11.so.6 (0x00007f6329680000)
	libEGL.so.1 => /usr/lib64/libEGL.so.1 (0x00007f6329450000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007f632924c000)
	librt.so.1 => /lib64/librt.so.1 (0x00007f6329043000)
	libGL.so.1 => /usr/lib64/libGL.so.1 (0x00007f6328dd9000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f6328bbc000)
	libm.so.6 => /lib64/libm.so.6 (0x00007f63288be000)
	libc.so.6 => /lib64/libc.so.6 (0x00007f632851b000)
	/lib64/ld-linux-x86-64.so.2 (0x000055577de19000)
	libXau.so.6 => /usr/lib64/libXau.so.6 (0x00007f6328317000)
	libexpat.so.1 => /usr/lib64/libexpat.so.1 (0x00007f63280ec000)
	libz.so.1 => /lib64/libz.so.1 (0x00007f6327ed6000)
	libbz2.so.1 => /usr/lib64/libbz2.so.1 (0x00007f6327cc7000)
	libpng16.so.16 => /usr/lib64/libpng16.so.16 (0x00007f6327a89000)
	libxcb-dri2.so.0 => /usr/lib64/libxcb-dri2.so.0 (0x00007f6327884000)
	libxcb-dri3.so.0 => /usr/lib64/libxcb-dri3.so.0 (0x00007f6327681000)
	libxcb-present.so.0 => /usr/lib64/libxcb-present.so.0 (0x00007f632747d000)
	libxcb-xfixes.so.0 => /usr/lib64/libxcb-xfixes.so.0 (0x00007f6327276000)
	libxcb-sync.so.1 => /usr/lib64/libxcb-sync.so.1 (0x00007f6327070000)
	libxshmfence.so.1 => /usr/lib64/libxshmfence.so.1 (0x00007f6326e6c000)
	libgbm.so.1 => /usr/lib64/libgbm.so.1 (0x00007f6326c5e000)
	libwayland-client.so.0 => /usr/lib64/libwayland-client.so.0 (0x00007f6326a50000)
	libwayland-server.so.0 => /usr/lib64/libwayland-server.so.0 (0x00007f632683d000)
	libdrm.so.2 => /usr/lib64/libdrm.so.2 (0x00007f632662e000)
	libglapi.so.0 => /usr/lib64/libglapi.so.0 (0x00007f63263ff000)
	libXext.so.6 => /usr/lib64/libXext.so.6 (0x00007f63261ed000)
	libXdamage.so.1 => /usr/lib64/libXdamage.so.1 (0x00007f6325fea000)
	libXfixes.so.3 => /usr/lib64/libXfixes.so.3 (0x00007f6325de4000)
	libXxf86vm.so.1 => /usr/lib64/libXxf86vm.so.1 (0x00007f6325bdd000)
	libffi.so.4 => /usr/lib64/libffi.so.4 (0x00007f63259d4000)


## sanderfoobar | 2018-12-18T10:07:03+00:00
Old issue.

+resolved

# Action History
- Created by: villabacho | 2017-03-28T08:11:37+00:00
- Closed at: 2018-12-18T10:09:31+00:00
