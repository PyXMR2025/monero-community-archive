---
title: please update root-zone trust-anchors in dns_utils.cpp
source_url: https://github.com/monero-project/monero/issues/4287
author: RoyArends
assignees: []
labels: []
created_at: '2018-08-21T01:10:27+00:00'
updated_at: '2018-09-14T11:40:57+00:00'
type: issue
status: closed
closed_at: '2018-09-14T11:40:57+00:00'
---

# Original Description
Users of your software that enable DNSSEC will not be able to validate DNS after October the 11th 2018.

Your repository contains a dns_utils.cpp file without the new DNSSEC trust-anchors:

. IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5
It should also include:

. IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

More information can be found at: https://www.icann.org/resources/pages/ksk-rollover

Please don’t hesitate to get in touch.

Warmly,

Roy Arends
ICANN


# Discussion History
## moneromooo-monero | 2018-08-21T11:02:35+00:00
When should "IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5" become untrusted (we'll likely have both in use in next release) ?


## moneromooo-monero | 2018-08-28T11:31:01+00:00
https://github.com/monero-project/monero/pull/4309

## mweinberg | 2018-08-31T21:09:09+00:00
IF the client performs DNSSEC validation, THEN the client will not be able to perform DNS lookups against any signed records.  For example, I see that the client make TXT queries to updates.moneropulse.(net|org|se|co).  If the code performs DNSSEC validation (unclear to me), then this query will fail after the root zone is signed with KSK-2017 on Oct 11.  

## moneromooo-monero | 2018-08-31T22:10:16+00:00
Do you mean before the patch, or also after it ?

## mweinberg | 2018-08-31T23:02:28+00:00
If nothing changes in the code, then starting on Oct 11 the client will not be able to do DNS queries on signed records IF DNSSEC validation is enforced.  If you add the second DS record (per Roy's recommendation above), then you won't have any problems on Oct 11 or afterward.

If you do not enforce DNSSEC validation, then nothing breaks.  But you should add the second DS record no matter what (good DNS hygiene).   

## moneromooo-monero | 2018-08-31T23:08:02+00:00
Do you mean if nothing changes in the code with the patch, or if nothing changes in the code without the patch ?

## mweinberg | 2018-08-31T23:10:19+00:00
If you do not add the second DS record to dns_utils.cpp, then starting on Oct 11 the client will not be able to do DNS queries on signed records IF DNSSEC validation is enforced. 

Does the code enforce DNSSEC validation?

## moneromooo-monero | 2018-08-31T23:15:12+00:00
OK, I'll take this to mean it's fine rather than infinite loop on this.

The code does enforce validation if there is a DNSSEC signature, but accepts unsigned data IIRC.


## mweinberg | 2018-08-31T23:17:51+00:00
Then you will have a problem starting Oct 11.  For example, queries for updates.moneropulse.(net|org|se|co) will fail because this record is DNSSEC-signed.  I don't know what other important DNS queries are made by the client?  

Happy to help further as needed.  

## moneromooo-monero | 2018-08-31T23:23:54+00:00
Then why do you try not to answer my questions above about whether the patch above is sufficient (at least theoretically) ?

## mweinberg | 2018-08-31T23:26:52+00:00
Sorry, I'm trying to be helpful and am supportive of Monero.  I now see:  https://github.com/monero-project/monero/pull/4309/commits/5083614ffa84109fccd754ee5509b25030bec9a6

Yes, this patch will fix the problem if it's applied to all clients before Oct 11.  Any client that is not patched will have the problem.

## moneromooo-monero | 2018-08-31T23:27:54+00:00
OK, thanks. Since I can't test whether this actually works, it's blind :)
There should be a release in time, since we're forking on the 18th, a week later.



## mweinberg | 2018-08-31T23:29:05+00:00
OK, good luck.  I'd stress to users that the forthcoming patch is important.  :-)  Go Monero!

## moneromooo-monero | 2018-09-14T11:25:13+00:00
+resolved

# Action History
- Created by: RoyArends | 2018-08-21T01:10:27+00:00
- Closed at: 2018-09-14T11:40:57+00:00
