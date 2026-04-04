---
title: error while loading shared libraries
source_url: https://github.com/monero-project/monero/issues/356
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-07-31T02:10:33+00:00'
updated_at: '2015-08-05T01:12:23+00:00'
type: issue
status: closed
closed_at: '2015-08-05T01:12:23+00:00'
---

# Original Description
So I'm going through the cold wallet instructions, and copy linux simplewallet bins onto the flashdrive etc. Also download the libboost1.55-dev package and put that on the drive.

Boot into the live USB. Install libboost 1.55. Run simplewallet. Get this:

> ubuntu@lubuntu:~/Desktop$ ./simplewallet 
> ./simplewallet: error while loading shared libraries: libboost_date_time.so.1.55.0: cannot open shared object file: No such file or directory
> lubuntu@lubuntu:~/Desktop$ 

I reboot, that fixes nothing. 

Then I think its because i didn't use apt-get, so I try apt-get install libboost1.55, tells me I already have it. 

I'm going to try one more reboot. Then I'll just make my tutorial video for how to compile head. 


# Discussion History
## warptangent | 2015-07-31T19:06:04+00:00
It looks like you need libboost-date-time1.55 too.
Try
`apt-get install libboost-date-time1.55`


## Gingeropolous | 2015-07-31T23:55:57+00:00
warptangent, yah know, for some reason i thought libboost dev woulda had date time in it. 


## Gingeropolous | 2015-08-05T01:12:23+00:00
old binaries. bah. 


# Action History
- Created by: Gingeropolous | 2015-07-31T02:10:33+00:00
- Closed at: 2015-08-05T01:12:23+00:00
