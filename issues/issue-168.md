---
title: succesful checkpoints during polling should not be log 0
source_url: https://github.com/monero-project/monero/issues/168
author: iamsmooth
assignees: []
labels: []
created_at: '2014-10-03T03:49:08+00:00'
updated_at: '2014-10-03T06:05:52+00:00'
type: issue
status: closed
closed_at: '2014-10-03T06:05:52+00:00'
---

# Original Description
The fact that checkpoints were successfully checked during polling and the fact that the optional json checkpoing file does not exist are both normal conditions that should not be looged at level 0 (or perhaps at all). The result is that any actual log messages generated are scrolled off.

Checkpoints passed during sync are reasonable to show, as would be new checkpoints added from DNS (that didn't already exist).

2014-Oct-02 20:44:54.311214 [P2P1]Blockchain checkpoints file not found
2014-Oct-02 20:44:54.311766 [P2P1]CHECKPOINT PASSED FOR HEIGHT 1 <771fbcd656ec1464d3a02ead5e18644030007a0fc664c0a964d30922821a8148>
2014-Oct-02 20:44:54.312081 [P2P1]CHECKPOINT PASSED FOR HEIGHT 10 <c0e3b387e47042f72d8ccdca88071ff96bff1ac7cde09ae113dbb7ad3fe92381>
2014-Oct-02 20:44:54.312388 [P2P1]CHECKPOINT PASSED FOR HEIGHT 100 <ac3e11ca545e57c49fca2b4e8c48c03c23be047c43e471e1394528b1f9f80b2d>
2014-Oct-02 20:44:54.312738 [P2P1]CHECKPOINT PASSED FOR HEIGHT 1000 <5acfc45acffd2b2e7345caf42fa02308c5793f15ec33946e969e829f40b03876>
2014-Oct-02 20:44:54.313049 [P2P1]CHECKPOINT PASSED FOR HEIGHT 10000 <c758b7c81f928be3295d45e230646de8b852ec96a821eac3fea4daf3fcac0ca2>
2014-Oct-02 20:44:54.313369 [P2P1]CHECKPOINT PASSED FOR HEIGHT 22231 <7cb10e29d67e1c069e6e11b17d30b809724255fee2f6868dc14cfc6ed44dfb25>
2014-Oct-02 20:44:54.313665 [P2P1]CHECKPOINT PASSED FOR HEIGHT 29556 <53c484a8ed91e4da621bb2fa88106dbde426fe90d7ef07b9c1e5127fb6f3a7f6>
2014-Oct-02 20:44:54.313960 [P2P1]CHECKPOINT PASSED FOR HEIGHT 50000 <0fe8758ab06a8b9cb35b7328fd4f757af530a5d37759f9d3e421023231f7b31c>
2014-Oct-02 20:44:54.314255 [P2P1]CHECKPOINT PASSED FOR HEIGHT 80000 <a62dcd7b536f22e003ebae8726e9e7276f63d594e264b6f0cd7aab27b66e75e3>
2014-Oct-02 20:44:54.315808 [P2P1]CHECKPOINT PASSED FOR HEIGHT 202612 <bbd604d2ba11ba27935e006ed39c9bfdd99b76bf4a50654bc1e1e61217962698>
2014-Oct-02 20:44:54.315991 [P2P1]CHECKPOINT PASSED FOR HEIGHT 202613 <e2aa337e78df1f98f462b3b1e560c6b914dec47b610698b7b7d1e3e86b6197c2>
2014-Oct-02 20:44:54.316155 [P2P1]CHECKPOINT PASSED FOR HEIGHT 202614 <c29e3dc37d8da3e72e506e31a213a58771b24450144305bcba9e70fa4d6ea6fb>
2014-Oct-02 20:44:54.316347 [P2P1]CHECKPOINT PASSED FOR HEIGHT 205000 <5d3d7a26e6dc7535e34f03def711daa8c263785f73ec1fadef8a45880fde8063>
2014-Oct-02 20:44:54.316485 [P2P1]CHECKPOINT PASSED FOR HEIGHT 220000 <9613f455933c00e3e33ac315cc6b455ee8aa0c567163836858c2d9caff111553>
2014-Oct-02 20:44:54.316641 [P2P1]CHECKPOINT PASSED FOR HEIGHT 230300 <bae7a80c46859db355556e3a9204a337ae8f24309926a1312323fdecf1920e61>
2014-Oct-02 20:44:54.316774 [P2P1]CHECKPOINT PASSED FOR HEIGHT 230700 <93e631240ceac831da1aebfc5dac8f722c430463024763ebafa888796ceaeedf>
2014-Oct-02 20:44:54.316918 [P2P1]CHECKPOINT PASSED FOR HEIGHT 231350 <b5add137199b820e1ea26640e5c3e121fd85faa86a1e39cf7e6cc097bdeb1131>
2014-Oct-02 20:44:54.317052 [P2P1]CHECKPOINT PASSED FOR HEIGHT 232150 <955de8e6b6508af2c24f7334f97beeea651d78e9ade3ab18fec3763be3201aa8>


# Discussion History
## tewinget | 2014-10-03T05:01:47+00:00
iirc this change is incoming.  I do agree with your assertion here.
On Oct 2, 2014 11:49 PM, "iamsmooth" notifications@github.com wrote:

> The fact that checkpoints were successfully checked during polling and the
> fact that the optional json checkpoing file does not exist are both normal
> conditions that should not be looged at level 0 (or perhaps at all). The
> result is that any actual log messages generated are scrolled off.
> 
> Checkpoints passed during sync are reasonable to show, as would be new
> checkpoints added from DNS (that didn't already exist).
> 
> 2014-Oct-02 20:44:54.311214 [P2P1]Blockchain checkpoints file not found
> 2014-Oct-02 20:44:54.311766 [P2P1]CHECKPOINT PASSED FOR HEIGHT 1
> 2014-Oct-02 20:44:54.312081 [P2P1]CHECKPOINT PASSED FOR HEIGHT 10
> 2014-Oct-02 20:44:54.312388 [P2P1]CHECKPOINT PASSED FOR HEIGHT 100
> 2014-Oct-02 20:44:54.312738 [P2P1]CHECKPOINT PASSED FOR HEIGHT 1000
> 2014-Oct-02 20:44:54.313049 [P2P1]CHECKPOINT PASSED FOR HEIGHT 10000
> 2014-Oct-02 20:44:54.313369 [P2P1]CHECKPOINT PASSED FOR HEIGHT 22231
> 2014-Oct-02 20:44:54.313665 [P2P1]CHECKPOINT PASSED FOR HEIGHT 29556
> 2014-Oct-02 20:44:54.313960 [P2P1]CHECKPOINT PASSED FOR HEIGHT 50000
> 2014-Oct-02 20:44:54.314255 [P2P1]CHECKPOINT PASSED FOR HEIGHT 80000
> 2014-Oct-02 20:44:54.315808 [P2P1]CHECKPOINT PASSED FOR HEIGHT 202612
> 2014-Oct-02 20:44:54.315991 [P2P1]CHECKPOINT PASSED FOR HEIGHT 202613
> 2014-Oct-02 20:44:54.316155 [P2P1]CHECKPOINT PASSED FOR HEIGHT 202614
> 2014-Oct-02 20:44:54.316347 [P2P1]CHECKPOINT PASSED FOR HEIGHT 205000
> 2014-Oct-02 20:44:54.316485 [P2P1]CHECKPOINT PASSED FOR HEIGHT 220000
> 2014-Oct-02 20:44:54.316641 [P2P1]CHECKPOINT PASSED FOR HEIGHT 230300
> 2014-Oct-02 20:44:54.316774 [P2P1]CHECKPOINT PASSED FOR HEIGHT 230700
> 2014-Oct-02 20:44:54.316918 [P2P1]CHECKPOINT PASSED FOR HEIGHT 231350
> 2014-Oct-02 20:44:54.317052 [P2P1]CHECKPOINT PASSED FOR HEIGHT 232150
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/monero-project/bitmonero/issues/168.


## fluffypony | 2014-10-03T06:05:43+00:00
Done here - https://github.com/fluffypony/bitmonero/commit/6f7ed13b72096ecb582ef4ab5553396b9335a134 and here - https://github.com/fluffypony/bitmonero/commit/3e644c25c4cd90fb2fd4602a00389f11f7aee42e

It'll be merged when I've finished fixing the static build issues


# Action History
- Created by: iamsmooth | 2014-10-03T03:49:08+00:00
- Closed at: 2014-10-03T06:05:52+00:00
