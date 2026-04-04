---
title: SHA256 signatures not matching github-published values
source_url: https://github.com/monero-project/monero-gui/issues/1281
author: calfer
assignees: []
labels:
- bug
- resolved
created_at: '2018-04-06T14:11:11+00:00'
updated_at: '2018-04-08T02:39:30+00:00'
type: issue
status: closed
closed_at: '2018-04-07T13:54:17+00:00'
---

# Original Description
When computing the SHA256 hash for monero-gui-mac-x64-v0.12.0.0.tar.bz2 as downloaded from github.com, I get the following:

0c 84 57 e3 d1 e5 28 b7 1e 8e 9e bb 3a 04 fe 24 1f 53 d6 fa 06 30 94 85 a0 7b ad be 28 a5 fa a6

This does not match the github-published hash:

f7 4c 10 8d 16 bd 70 b6 f0 05 2b a4 b3 ce 91 fa 3c a5 96 22 a0 ae e7 d5 23 a1 f4 39 67 81 4c 12

The same file downloaded from the Official Download Link for Mac on the github page outputs the correct hash:

f7 4c 10 8d 16 bd 70 b6 f0 05 2b a4 b3 ce 91 fa 3c a5 96 22 a0 ae e7 d5 23 a1 f4 39 67 81 4c 12

Hashes were computed multiple times using files from above-stated sources up until the time of this submission.

Thoughts?

# Discussion History
## qubenix | 2018-04-06T16:29:41+00:00
I can repro:

```
user@host:~$ wget -O monero-gui-mac-x64-v0.12.0.0.tar.bz2 "https://downloads.getmonero.org/gui/mac64"
--2018-04-06 10:13:44--  https://downloads.getmonero.org/gui/mac64
Resolving downloads.getmonero.org (downloads.getmonero.org)... 148.253.246.207, 148.253.246.80
Connecting to downloads.getmonero.org (downloads.getmonero.org)|148.253.246.207|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://dlsrc.getmonero.org/gui/monero-gui-mac-x64-v0.12.0.0.tar.bz2 [following]
--2018-04-06 10:13:50--  https://dlsrc.getmonero.org/gui/monero-gui-mac-x64-v0.12.0.0.tar.bz2
Resolving dlsrc.getmonero.org (dlsrc.getmonero.org)... 104.24.28.115, 104.24.27.115, 2400:cb00:2048:1::6818:1c73, ...
Connecting to dlsrc.getmonero.org (dlsrc.getmonero.org)|104.24.28.115|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 84546994 (81M) [application/octet-stream]
Saving to: ‘monero-gui-mac-x64-v0.12.0.0.tar.bz2’

monero-gui-mac-x64- 100%[===================>]  80.63M   451KB/s    in 2m 48s  

2018-04-06 10:16:44 (492 KB/s) - ‘monero-gui-mac-x64-v0.12.0.0.tar.bz2’ saved [84546994/84546994]

user@host:~$ shasum -a 256 monero-gui-mac-x64-v0.12.0.0.tar.bz2 
f74c108d16bd70b6f0052ba4b3ce91fa3ca59622a0aee7d523a1f43967814c12  monero-gui-mac-x64-v0.12.0.0.tar.bz2
user@host:~$ wget -O github-monero-gui-mac-x64-v0.12.0.0.tar.bz2 "https://github.com/monero-project/monero-gui/releases/download/v0.12.0.0/monero-gui-mac-x64-v0.12.0.0.tar.bz2"
--2018-04-06 10:18:40--  https://github.com/monero-project/monero-gui/releases/download/v0.12.0.0/monero-gui-mac-x64-v0.12.0.0.tar.bz2
Resolving github.com (github.com)... 192.30.253.112, 192.30.253.113
Connecting to github.com (github.com)|192.30.253.112|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://github-production-release-asset-2e65be.s3.amazonaws.com/33237663/27447b2e-37a6-11e8-8788-221bfb96bc8f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180406%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180406T161846Z&X-Amz-Expires=300&X-Amz-Signature=c8554119325795ec6c5368ca53362fe80d23aa02a2c89b9ff0d5dbb6ed344fb7&X-Amz-SignedHeaders=host&actor_id=0&response-content-disposition=attachment%3B%20filename%3Dmonero-gui-mac-x64-v0.12.0.0.tar.bz2&response-content-type=application%2Foctet-stream [following]
--2018-04-06 10:18:46--  https://github-production-release-asset-2e65be.s3.amazonaws.com/33237663/27447b2e-37a6-11e8-8788-221bfb96bc8f?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIWNJYAX4CSVEH53A%2F20180406%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180406T161846Z&X-Amz-Expires=300&X-Amz-Signature=c8554119325795ec6c5368ca53362fe80d23aa02a2c89b9ff0d5dbb6ed344fb7&X-Amz-SignedHeaders=host&actor_id=0&response-content-disposition=attachment%3B%20filename%3Dmonero-gui-mac-x64-v0.12.0.0.tar.bz2&response-content-type=application%2Foctet-stream
Resolving github-production-release-asset-2e65be.s3.amazonaws.com (github-production-release-asset-2e65be.s3.amazonaws.com)... 52.216.100.187
Connecting to github-production-release-asset-2e65be.s3.amazonaws.com (github-production-release-asset-2e65be.s3.amazonaws.com)|52.216.100.187|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 84654355 (81M) [application/octet-stream]
Saving to: ‘github-monero-gui-mac-x64-v0.12.0.0.tar.bz2’

github-monero-gui-m 100%[===================>]  80.73M   726KB/s    in 97s     

2018-04-06 10:20:28 (855 KB/s) - ‘github-monero-gui-mac-x64-v0.12.0.0.tar.bz2’ saved [84654355/84654355]

user@host:~$ shasum -a 256 github-monero-gui-mac-x64-v0.12.0.0.tar.bz2 
0c8457e3d1e528b71e8e9ebb3a04fe241f53d6fa06309485a07badbe28a5faa6  github-monero-gui-mac-x64-v0.12.0.0.tar.bz2
```

The files are different length even: 

Github length: `84654355`

Getmonero length: `84546994`

## dEBRUYNE-1 | 2018-04-06T19:19:48+00:00
The GUI Mac OS X binaries were updated, because there were some issues with the daemon (`monerod`) that was included. `f7 4c..4c 12` is the SHA256 hash of the new and correct GUI Mac OS X binaries, whereas `0c 84..fa a6` is the SHA256 hash of the old and incorrect GUI Mac OS X binaries. 

It seems like the Github download link was not properly updated to accommodate the new binaries. 

Pinging @fluffypony 

## dEBRUYNE-1 | 2018-04-06T19:19:56+00:00
+bug

## dEBRUYNE-1 | 2018-04-06T19:50:53+00:00
@qubenix @calfer - The Github link should contain the correct binaries now. 

## dEBRUYNE-1 | 2018-04-07T13:53:39+00:00
+resolved

## qubenix | 2018-04-07T14:33:42+00:00
Confirmed, github download has correct hash now.

## calfer | 2018-04-08T02:39:30+00:00
Thank you all.

# Action History
- Created by: calfer | 2018-04-06T14:11:11+00:00
- Closed at: 2018-04-07T13:54:17+00:00
