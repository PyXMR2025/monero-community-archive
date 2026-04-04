---
title: Failing test for fcf_protection & fstack_clash_protection on branch release-v0.13
source_url: https://github.com/monero-project/monero/issues/4451
author: drhile
assignees: []
labels: []
created_at: '2018-09-26T05:10:20+00:00'
updated_at: '2018-10-04T16:27:16+00:00'
type: issue
status: closed
closed_at: '2018-10-04T16:27:16+00:00'
---

# Original Description
For branch `release-v0.12`, the tests for fcf_protection and fstack_clash_protection succeeds but not on branch `release-v0.13`. Information for system is below as well as logs of building procedures for each branch. Please duplicate scenario if possible and respond. Thank you.

[release-v0.12.log](https://github.com/monero-project/monero/files/2418169/release-v0.12.log)
[release-v0.13.log](https://github.com/monero-project/monero/files/2418170/release-v0.13.log)


OS: Linux
Distro: Ubuntu 18.04.1 LTS
Arch: x86_64
Kernel: 4.15.0-33-generic

Installed dependencies:
-  build-essential
-  cmake
-  doxygen
-  libboost-all-dev
-  libssl-dev
-  libzmq3-dev
-  libunbound-dev
-  libsodium-dev
-  libunwind8-dev
-  liblzma-dev
-  libreadline6-dev
-  libldns-dev
-  libexpat1-dev
-  pkg-config
-  libpcsclite-dev
-  libpgm-dev

# Discussion History
## moneromooo-monero | 2018-09-26T08:35:51+00:00
How did you merge that patch to 0.12 ? The log you posted for 0.12 does not show it being tested for.

Are you sure your compiler supports those options ?

## drhile | 2018-09-26T23:02:34+00:00
Sorry for the delayed response. I'm not sure what patch you're referring to but I know that installing `libpgm-dev` fixed it on branch `release-v0.12`.

## moneromooo-monero | 2018-09-27T07:44:23+00:00
I mean the patch which adds the compiler options. You said it works in 0.12, but those aren't in 0.12, so you presumably backported those ? Or it could be you just asumed they were in 0.12 ?

It should have nothing to do with libpgm-dev, since the detection is just running the compiler without the monero source to check for error messages.


## xiphon | 2018-09-27T12:28:11+00:00
@drhile 

> For branch `release-v0.12`, the tests for fcf_protection and fstack_clash_protection succeeds

`release-v0.12` doesn't have any tests for `fcf_protection` and `fstack_clash_protection`, please take a closer look at the output

## drhile | 2018-09-28T04:13:20+00:00
@xiphon thanks for explaining I'll take a look and respond when I can or can't find something.

## drhile | 2018-09-28T04:14:36+00:00
Sorry I accidentally closed it.

## moneromooo-monero | 2018-10-01T11:41:36+00:00
You might have missed my question, so:

> Are you sure your compiler supports those options ?


## drhile | 2018-10-04T00:30:54+00:00
I'm not sure. Is there a quick way to check and report it back to you?

## moneromooo-monero | 2018-10-04T10:35:09+00:00
Run this:

<pre>
echo "int main(){return 0;}" | g++ -fcf-protection=full -x c++ -
</pre>

## drhile | 2018-10-04T15:32:18+00:00
> 
> 
> Run this:
> 
> echo "int main(){return 0;}" | g++ -fcf-protection=full -x c++ -

The result:

david@admin:~$ `echo "int main(){return 0;}" | g++ -fcf- protection=full -x c++ -`
`g++: error: protection=full: No such file or directory`
`g++: error: unrecognized command line option ‘-fcf-’; did you mean ‘-fXf=’?`

## moneromooo-monero | 2018-10-04T15:35:03+00:00
My command does not have a space in the middle of the option. Your does.

## drhile | 2018-10-04T16:05:17+00:00
Sorry about that. The results:

david@admin:~$ `echo "int main(){return 0;}" | g++ -fcf-protection=full -x c++ -`
`g++: error: unrecognized command line option ‘-fcf-protection=full’; did you mean ‘-fstack-protector-all’?`

## moneromooo-monero | 2018-10-04T16:15:50+00:00
Then your compiler does not support that option, and therefore the cmake machinery worked correctly.


## drhile | 2018-10-04T16:27:16+00:00
If that's the case, I can close this since this is not a code but an user issue. Thank you for your assistance.

# Action History
- Created by: drhile | 2018-09-26T05:10:20+00:00
- Closed at: 2018-10-04T16:27:16+00:00
