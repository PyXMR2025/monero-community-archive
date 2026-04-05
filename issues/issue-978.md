---
title: Miner mines in background...miner is malware if downloaded via link to this
  page...must manually type in github address to navigate to page securely
source_url: https://github.com/xmrig/xmrig/issues/978
author: bakd247
assignees: []
labels:
- av
created_at: '2019-03-09T13:08:29+00:00'
updated_at: '2019-03-09T16:50:47+00:00'
type: issue
status: closed
closed_at: '2019-03-09T14:08:59+00:00'
---

# Original Description
this is malware....if you navigate to this page via link...please be aware that there are no verifiable hashes in the description of the miner so there is no way to know what your getting...

# Discussion History
## xmrig | 2019-03-09T13:31:45+00:00
https://github.com/xmrig/xmrig/issues?q=label%3Aav+is%3Aclosed

## el00ruobuob | 2019-03-09T14:05:02+00:00
Blame the malware dev who embedded xmrig, not the open source miner a large legit community use @bakd247

## bakd247 | 2019-03-09T14:08:59+00:00
no it was apparently the link at monerohash.com that lead me to a false page or something because I went to the page manually and it works fine...also on a diff machine it works fine as well..there is a bad link at monerohash.com....or someone intercepted my packets and redirected me....thats all I can figure becasue I got everything working now since I used a diff. download and install method

previous comment re

## bakd247 | 2019-03-09T14:11:06+00:00
I cant verify this install because they gave NO VERIFIABLE HASHES!!!!

wouldn't have had any issues from the start if the developer would have done this in the description of the post

## snipeTR | 2019-03-09T16:27:39+00:00
@xmrig please share sha1 checksum.

## xmrig | 2019-03-09T16:50:47+00:00
SHA256
```
0f66c7229aa4245940187a2f8bff8276239c96b26d46985e662fdc2e8cdd12b5 *xmrig-2.14.1-gcc-win32\xmrig-2.14.1\config.json
9554e811347798d784bbe0ed5fa212e95dc8783a34cbc298454805f0988cb577 *xmrig-2.14.1-gcc-win32\xmrig-2.14.1\start.cmd
a0c6a35297988ece4b83c2d46af8c2f94dae2efd929d94aabdce67ffb3936388 *xmrig-2.14.1-gcc-win32\xmrig-2.14.1\xmrig-notls.exe
8a9dbb6fd700030cb18199be926e71823bf975f30e06cd90e9414e03bbe19d37 *xmrig-2.14.1-gcc-win32\xmrig-2.14.1\xmrig.exe
0f66c7229aa4245940187a2f8bff8276239c96b26d46985e662fdc2e8cdd12b5 *xmrig-2.14.1-gcc-win64\xmrig-2.14.1\config.json
9554e811347798d784bbe0ed5fa212e95dc8783a34cbc298454805f0988cb577 *xmrig-2.14.1-gcc-win64\xmrig-2.14.1\start.cmd
672feac7a3c5b0410e9889ed07420eca89f0e33f200563c7ce209618eb0d1c69 *xmrig-2.14.1-gcc-win64\xmrig-2.14.1\xmrig-notls.exe
c213492008177ae1cda8903a46fb1b766f41c58051f1527237a597243885a87e *xmrig-2.14.1-gcc-win64\xmrig-2.14.1\xmrig.exe
0f66c7229aa4245940187a2f8bff8276239c96b26d46985e662fdc2e8cdd12b5 *xmrig-2.14.1-msvc-win64\xmrig-2.14.1\config.json
9554e811347798d784bbe0ed5fa212e95dc8783a34cbc298454805f0988cb577 *xmrig-2.14.1-msvc-win64\xmrig-2.14.1\start.cmd
1b7b6a1c9ee839633d0db1e8d80cfc94fc2d92d45031a9f21ed8d27d6fe52f69 *xmrig-2.14.1-msvc-win64\xmrig-2.14.1\xmrig-notls.exe
80191b2ef8618bd33ca674664cd1cceb4b1145bb9c17587f7590c2983720d1a4 *xmrig-2.14.1-msvc-win64\xmrig-2.14.1\xmrig.exe
```

SHA1
```
91758f90e908c16a33d1989e09582ef7461701d6 *xmrig-2.14.1-gcc-win32\xmrig-2.14.1\config.json
c2740b6e8a535176e3df92c0417ef1a4d5e1bc46 *xmrig-2.14.1-gcc-win32\xmrig-2.14.1\start.cmd
7c53b8be7fc30bfe8dea697e586a3f2b752a8db7 *xmrig-2.14.1-gcc-win32\xmrig-2.14.1\xmrig-notls.exe
ea1ed2ca636c09ac93a58ed7204182693895ebf0 *xmrig-2.14.1-gcc-win32\xmrig-2.14.1\xmrig.exe
91758f90e908c16a33d1989e09582ef7461701d6 *xmrig-2.14.1-gcc-win64\xmrig-2.14.1\config.json
c2740b6e8a535176e3df92c0417ef1a4d5e1bc46 *xmrig-2.14.1-gcc-win64\xmrig-2.14.1\start.cmd
4d56bd9d81033dcfd8a0d6fac1a65ee202ba8835 *xmrig-2.14.1-gcc-win64\xmrig-2.14.1\xmrig-notls.exe
282239c7d8e8606c88b15f7f2c7f30b5ec1b7fd4 *xmrig-2.14.1-gcc-win64\xmrig-2.14.1\xmrig.exe
91758f90e908c16a33d1989e09582ef7461701d6 *xmrig-2.14.1-msvc-win64\xmrig-2.14.1\config.json
c2740b6e8a535176e3df92c0417ef1a4d5e1bc46 *xmrig-2.14.1-msvc-win64\xmrig-2.14.1\start.cmd
f04bf7f64d98f3b73eaea27b0af80c91dd7fee1c *xmrig-2.14.1-msvc-win64\xmrig-2.14.1\xmrig-notls.exe
42d86d35f696f73d1b8af83f86b63c8e1e5bfd0b *xmrig-2.14.1-msvc-win64\xmrig-2.14.1\xmrig.exe
```

# Action History
- Created by: bakd247 | 2019-03-09T13:08:29+00:00
- Closed at: 2019-03-09T14:08:59+00:00
