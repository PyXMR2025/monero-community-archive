---
title: Advanced build Install Problem
source_url: https://github.com/xmrig/xmrig/issues/3158
author: k7n2g
assignees: []
labels:
- question
created_at: '2022-11-07T15:14:52+00:00'
updated_at: '2022-12-13T14:14:02+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:14:02+00:00'
---

# Original Description
[Spudz76]   Advanced build gives this  ERROR: cannot verify github.com's certificate, issued by ‘CN=DigiCert TLS Hybrid ECC SHA384 2020 CA1,O=DigiCert Inc,C=US’:  tried it with --no-check-certificate  no luck
Tried ./build_deps.sh --no-check-certificate. not work.  is there another command  or is the workaround to download individually each package OpenSSL/hwloc/LibUV if so what versions do you recommend don't want to use system devel packages if possible

# Discussion History
## Spudz76 | 2022-11-07T15:25:25+00:00
Those scripts unfortunately do not take options nor pass them through to the sub-scripts (`build_deps.sh` just calls the three other scripts, `build.uv.sh`/`build.hwloc.sh`/`build.openssl.sh`)

So to get the effect of that option you have to edit `scripts/build.uv.sh` and find the wget command and insert the `--no-check-certificate` there.

I have had to do so before when there were connection problems with the openssl source url (unreachable on IPv6 from where I was, so I had to add `-4` so it would force IPv4).

Once you've edited the files the next `git pull` will complain, simply undo the changes with `git checkout scripts/build.*` and then it will pull clean (and if the cert is still broken put the option back in).


## Spudz76 | 2022-11-07T15:29:41+00:00
Also I don't have that error so perhaps your `ca-certificates` is out of date (Ubuntu? and older one?)

## k7n2g | 2022-11-07T15:41:34+00:00
thanks guy I will work my way through that,  

## Spudz76 | 2022-11-07T15:41:45+00:00
[This says](https://knowledge.digicert.com/alerts/DigiCert-ICA-Update.html) they updated that one June 2021, so if your `ca-certificates` package is older than that you'll have problems getting to any site anywhere that uses that CA until you update it.

Note some versions of Ubuntu get moved to the "old versions" mirror and are taken off the main mirror, so if your `apt update` has errors about downloading new lists you may need to swap to the other mirror to get updates.  Especially the non-LTS versions... Debian does similar stuff but usually not until after it's older than "oldoldstable", truly antique.  Ubuntu moved `groovy` around when `jazzy` was released.

## Spudz76 | 2022-11-07T15:47:43+00:00
If it's really old and breaks the https on the mirror sites (so you can't use apt to update it) then you can go manually get the actual `.deb` file and install it with `dpkg -i` and then https should start working again (and let apt upgrade the rest of things).

I ran into that once with an old forgotten install.

What does your `lsb_release -a` say?

## k7n2g | 2022-11-07T15:48:35+00:00
Thanks for that think i have sorted it out now it was my cert, my bad should have realized this may be the problem 

## k7n2g | 2022-11-07T16:08:04+00:00
Updated all certs not work,  added,  scripts/build.uv.sh  the wget command the --no-check-certificate
okay downloads then i get this ERROR: cannot verify download.open-mpi.org's certificate, issued by ‘CN=Amazon,OU=Server CA 1B,O=Amazon,C=US’:
  Unable to locally verify the issuer's authority.
To connect to download.open-mpi.org insecurely, use `--no-check-certificate'. where would i find this one  once i get it installed and running i will try to correct it all my side

## Spudz76 | 2022-11-07T23:29:42+00:00
That one is in `build.hwloc.sh` do the same sort of edit there

## Spudz76 | 2022-11-07T23:30:59+00:00
And you might as well do the `build.openssl.sh` one too, it'll probably fail since your `ca-certificates` package is very broken.

## QbitNetwork | 2022-11-09T10:26:23+00:00
thanks spudz76 sorted now

# Action History
- Created by: k7n2g | 2022-11-07T15:14:52+00:00
- Closed at: 2022-12-13T14:14:02+00:00
