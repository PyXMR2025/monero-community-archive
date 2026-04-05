---
title: Unable to mine RVN / KawPow on 4 GB GPU due to error CL_INVALID_BUFFER_SIZE
source_url: https://github.com/xmrig/xmrig/issues/2955
author: ghost
assignees: []
labels: []
created_at: '2022-03-05T04:02:33+00:00'
updated_at: '2022-03-15T06:38:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
GPU: XFX RX 470

xmrig:
` error CL_INVALID_BUFFER_SIZE when calling clCreateBuffer with buffer size 3506438144`

clinfo:
`Global memory size                              4294967296 (4GiB)`

`Global free memory (AMD)                        4128768 (3.938GiB) 3866624 (3.688GiB)`

`Max memory allocation                           3422552064 (3.188GiB)`

`Device Version                                  OpenCL 2.0 AMD-APP (3302.5)`

`Driver Version                                  3302.5 (PAL,HSAIL)`

How do I change `Max memory allocation                           3422552064 (3.188GiB)` ?

# Discussion History
## Spudz76 | 2022-03-06T04:20:30+00:00
21.30 doesn't really work right for Ellesmere or Vega10

I have good luck with 20.30 on both.  The Vega10 still doesn't work right unless I use `dkms remove -m amdgpu/5.6.5.24-1109583 --all` to force using the standard kernel amdgpu driver (while keeping the OpenCL stack from amdgpu-pro).  Apt won't allow the installation of the opencl parts without pulling in the driver, but removing the module afterward is an easy workaround.  Dkms will keep rebuilding it on kernel upgrades and such, remember to again remove it.

To make the installation complete, because the initial pass will crash the dkms build and leave the apt packages in broken state, apply the attached patch with `cd /usr/src/amdgpu-5.6.5.24-1109583 && patch -p1 < patch_no_pci_platform_rom.diff.txt` and then `apt install -f` to continue/retry the build, then remove the result as above (patch and build is only to make apt happy, then we throw the result away).

[patch_no_pci_platform_rom.diff.txt](https://github.com/xmrig/xmrig/files/8191946/patch_no_pci_platform_rom.diff.txt)

## ghost | 2022-03-12T12:09:51+00:00
@Spudz76 
Could you list the steps I should be following one by one please? If I'm to use version 20.30 then should I be using Ubuntu 20.04.1? A little more background and detail would really help

## Spudz76 | 2022-03-12T16:21:22+00:00
Yes, Ubuntu 20.04.4 is perfect and the 20.30.  Install two things:
```
apt install amdgpu-pro-pin
apt install opencl-amdgpu-pro
```
and then after that do:
```
dkms remove -m amdgpu/5.6.5.24-1109583 --all
```

## ghost | 2022-03-13T12:30:20+00:00
@Spudz76 
```
$ sudo apt install ./amdgpu-pro-pin_20.30-1109583_all.deb 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting 'amdgpu-pro-pin' instead of './amdgpu-pro-pin_20.30-1109583_all.deb'
The following packages were automatically installed and are no longer required:
  dctrl-tools dkms
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  amdgpu-pro-pin
0 upgraded, 1 newly installed, 0 to remove and 47 not upgraded.
Need to get 0 B/6,032 B of archives.
After this operation, 33.8 kB of additional disk space will be used.
Get:1 /home/l/Downloads/amdgpu-pro-20.30-1109583-ubuntu-20.04/amdgpu-pro-pin_20.30-1109583_all.deb amdgpu-pro-pin all 20.30-1109583 [6,032 B]
Selecting previously unselected package amdgpu-pro-pin.
(Reading database ... 183388 files and directories currently installed.)
Preparing to unpack .../amdgpu-pro-pin_20.30-1109583_all.deb ...
Unpacking amdgpu-pro-pin (20.30-1109583) ...
Setting up amdgpu-pro-pin (20.30-1109583) ...


$ sudo apt install ./opencl-amdgpu-pro_20.30-1109583_amd64.deb 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting 'opencl-amdgpu-pro' instead of './opencl-amdgpu-pro_20.30-1109583_amd64.deb'
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 opencl-amdgpu-pro : Depends: amdgpu-pro-core but it is not installable
                     Depends: amdgpu-dkms (= 1:5.6.5.24-1109583) but it is not installable
                     Depends: libdrm2-amdgpu (= 1:2.4.100-1109583) but it is not installable
                     Depends: libdrm-amdgpu-amdgpu1 (= 1:2.4.100-1109583) but it is not installable
                     Depends: libdrm-amdgpu-common (= 1.0.0-1109583) but it is not installable
                     Depends: clinfo-amdgpu-pro (= 20.30-1109583) but it is not installable
                     Depends: opencl-orca-amdgpu-pro-icd (= 20.30-1109583) but it is not installable
                     Depends: ocl-icd-libopencl1-amdgpu-pro (= 20.30-1109583) but it is not installable
                     Depends: opencl-amdgpu-pro-icd (= 20.30-1109583) but it is not installable
E: Unable to correct problems, you have held broken packages.


$ sudo apt install ./amdgpu-dkms_5.6.5.24-1109583_all.deb 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting 'amdgpu-dkms' instead of './amdgpu-dkms_5.6.5.24-1109583_all.deb'
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 amdgpu-dkms : PreDepends: amdgpu-dkms-firmware (= 1:5.6.5.24-1109583) but it is not installable
E: Unable to correct problems, you have held broken packages.```


$ sudo apt install ./amdgpu-dkms-firmware_5.6.5.24-1109583_all.deb 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting 'amdgpu-dkms-firmware' instead of './amdgpu-dkms-firmware_5.6.5.24-1109583_all.deb'
The following packages were automatically installed and are no longer required:
  dctrl-tools dkms
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  amdgpu-dkms-firmware
0 upgraded, 1 newly installed, 0 to remove and 47 not upgraded.
Need to get 0 B/5,028 kB of archives.
After this operation, 41.3 MB of additional disk space will be used.
Get:1 /home/l/Downloads/amdgpu-pro-20.30-1109583-ubuntu-20.04/amdgpu-dkms-firmware_5.6.5.24-1109583_all.deb amdgpu-dkms-firmware all 1:5.6.5.24-1109583 [5,028 kB]
Selecting previously unselected package amdgpu-dkms-firmware.
(Reading database ... 183402 files and directories currently installed.)
Preparing to unpack .../amdgpu-dkms-firmware_5.6.5.24-1109583_all.deb ...
Unpacking amdgpu-dkms-firmware (1:5.6.5.24-1109583) ...
Setting up amdgpu-dkms-firmware (1:5.6.5.24-1109583) ...


$ sudo apt install ./amdgpu-dkms_5.6.5.24-1109583_all.deb 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Note, selecting 'amdgpu-dkms' instead of './amdgpu-dkms_5.6.5.24-1109583_all.deb'
The following NEW packages will be installed:
  amdgpu-dkms
0 upgraded, 1 newly installed, 0 to remove and 47 not upgraded.
Need to get 0 B/5,602 kB of archives.
After this operation, 187 MB of additional disk space will be used.
Get:1 /home/l/Downloads/amdgpu-pro-20.30-1109583-ubuntu-20.04/amdgpu-dkms_5.6.5.24-1109583_all.deb amdgpu-dkms all 1:5.6.5.24-1109583 [5,602 kB]
Selecting previously unselected package amdgpu-dkms.
(Reading database ... 183793 files and directories currently installed.)
Preparing to unpack .../amdgpu-dkms_5.6.5.24-1109583_all.deb ...
Unpacking amdgpu-dkms (1:5.6.5.24-1109583) ...
Setting up amdgpu-dkms (1:5.6.5.24-1109583) ...
Loading new amdgpu-5.6.5.24-1109583 DKMS files...
Building for 5.13.0-35-generic
Building for architecture x86_64
Building initial module for 5.13.0-35-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/amdgpu-dkms.0.crash'
Error! Bad return status for module build on kernel: 5.13.0-35-generic (x86_64)
Consult /var/lib/dkms/amdgpu/5.6.5.24-1109583/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit 
status 10
Errors were encountered while processing:
 amdgpu-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

Files from:
https://drivers.amd.com/drivers/linux/amdgpu-pro-20.30-1109583-ubuntu-20.04.tar.xz
at
https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-20-30

## Spudz76 | 2022-03-13T18:57:20+00:00
When you have a raw deb package file you use `dpkg -i <file.deb>` not `apt install`

It's been a while since I used the bundle method, I expand the bundle onto a mirror server and then configure a normal apt sources entry for that mirror, and install things with apt like normal. But if I recall correctly all the bundle does is put all the files in `/var/` somewhere and then make an apt sources entry for that local mirror which would end up working similarly.

Although I might be confusing the AMD bundle with the nvidia bundle.  Either way I converted to using my own mirrors long ago.

## ghost | 2022-03-15T06:37:13+00:00
@Spudz76 
dpkg -i Doesn't work either... last resort is using Windows but I don't wanna xD

# Action History
- Created by: ghost | 2022-03-05T04:02:33+00:00
