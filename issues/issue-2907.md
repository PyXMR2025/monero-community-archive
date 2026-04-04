---
title: ubuntu 16.04 build failing
source_url: https://github.com/monero-project/monero-gui/issues/2907
author: LouisCyfer
assignees: []
labels: []
created_at: '2020-05-14T00:36:30+00:00'
updated_at: '2020-06-19T21:56:35+00:00'
type: issue
status: closed
closed_at: '2020-06-19T21:56:35+00:00'
---

# Original Description
having qt v5.9.7 installed gives following error:
```
../src/openpgp/openpgp.cpp: In static member function ‘static std::tuple<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, openpgp::s_expression, long unsigned int> openpgp::public_key_rsa::decode(epee::span<const unsigned char>)’:
../src/openpgp/openpgp.cpp:158:20: error: ‘algorithm’ is not a class, namespace, or enumeration
   if (algorithm != algorithm::rsa)
                    ^
../src/openpgp/openpgp.cpp:168:92: error: converting to ‘std::tuple<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, openpgp::s_expression, long unsigned int>’ from initializer list would use explicit constructor ‘constexpr std::tuple< <template-parameter-1-1> >::tuple(_UElements&& ...) [with _UElements = {std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, openpgp::s_expression, unsigned int}; <template-parameter-2-2> = void; _Elements = {std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, openpgp::s_expression, long unsigned int}]’
   return {std::move(user_id), std::move(expression), gcry_mpi_get_nbits(public_key_n.get())};
                                                                                            ^
../src/openpgp/openpgp.cpp: In static member function ‘static openpgp::signature_rsa openpgp::signature_rsa::from_buffer(epee::span<const unsigned char>)’:
../src/openpgp/openpgp.cpp:220:20: error: ‘algorithm’ is not a class, namespace, or enumeration
   if (algorithm != algorithm::rsa)
                    ^
Makefile:7076: die Regel für Ziel „openpgp.o“ scheiterte
make: *** [openpgp.o] Fehler 1
```
also I noticed there is no package "libnorm-dev" available in my distro.

What am I missing and can I do something about this?

# Discussion History
## selsta | 2020-05-14T00:37:52+00:00
Can you try to update your GCC version?

## LouisCyfer | 2020-05-14T01:05:13+00:00
`gcc --version` --> `gcc (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609`
which version I need for compiling? (and yes Updating to 18.04 is not an option yet for me)

EDIT:
I had to install `sudo apt install gccgo-6` (suggested), then `gcc-6 --version` --> `gcc-6 (Ubuntu 6.0.1-0ubuntu1) 6.0.0 20160414 (experimental) [trunk revision 234994]` compiling now and reporting back if it solves the issue.

EDIT2:
I reverted the previous and researched how to update my gcc. Then I applied the answer found [on askubuntu.com](https://askubuntu.com/a/746480). this gives me access to further versions. Reporting back if this can be closed.

EDIT3:
ok now this one is interesting. I installed gcc-6 and g++-6 and added 2 export lines before calling the build.sh:
```
export CC=/usr/bin/gcc-6
export CXX=/usr/bin/g++-6
```
it gives some error markers while compiling but stops at the end at the same position. attempting to use gcc-7 now.

EDIT4: nope exporting gcc-7 and g++7 did not help

EDIT5:
even after figuring how to switch gcc and g++ system wide to version 9 (so far on all versions/5-9) it fails to built the source

```
	'gcc --version'	--> 'gcc (Ubuntu 9.3.0-10ubuntu2~16.04) 9.3.0'
	'g++ --version'	--> 'g++ (Ubuntu 9.3.0-10ubuntu2~16.04) 9.3.0'

	using 'QT_SELECT=QT_5.9.7'
	QTTOOLDIR="/mypath/QT_BIN/Qt5.9.7/5.9.7/gcc_64/bin"
	QTTOOLDIR="/mypath/QT_BIN/Qt5.9.7/5.9.7/gcc_64/bin"

```
ended with a failed build

## xiphon | 2020-06-04T01:21:29+00:00
You can apply the patch from https://github.com/monero-project/monero-gui/pull/2933 PR, it fixes the issue

## LouisCyfer | 2020-06-04T05:25:19+00:00
well .. it fixes the openpgp issue, should I open a new issue with my current problem?

after applying your PR by clone your repo I get this error on Ubuntu 16.04:
```
/usr/bin/ld: cannot find -lwallet_merged
/usr/bin/ld: cannot find -lepee
/usr/bin/ld: cannot find -ludev
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libboost_thread.a(future.o): Die Umlagerung von 
/usr/lib/gcc/x86_64-linux-gnu/7/../../../x86_64-linux-gnu/libboost_thread.a: error adding symbols: Ungültiger Wert
collect2: error: ld returned 1 exit status
Makefile:697: die Regel für Ziel „release/bin/monero-wallet-gui“ scheiterte
make: *** [release/bin/monero-wallet-gui] Fehler 1
```

using environment:
```
	'gcc --version'	--> 'gcc (Ubuntu 7.5.0-3ubuntu1~16.04) 7.5.0'
	'g++ --version'	--> 'g++ (Ubuntu 7.5.0-3ubuntu1~16.04) 7.5.0'

	using 'QT_SELECT=QT_5.14.2'
	QTTOOLDIR="/mypath/QT_BIN/Qt5.14.2/5.14.2/gcc_64/bin"
```

## xiphon | 2020-06-04T17:08:51+00:00
> well .. it fixes the openpgp issue, should I open a new issue with my current problem?
> 
> after applying your PR by clone your repo I get this error on Ubuntu 16.04:

Could you provide the command you're running and the complete build output?

## LouisCyfer | 2020-06-05T06:28:09+00:00
> > well .. it fixes the openpgp issue, should I open a new issue with my current problem?
> > after applying your PR by clone your repo I get this error on Ubuntu 16.04:
> 
> Could you provide the command you're running and the complete build output?

yes, building right now, going to post it in this comment asap
EDIT: [build.log](https://gist.github.com/LouisCyfer/968f6512f7c50108fbfe28fff20ee798)

# Action History
- Created by: LouisCyfer | 2020-05-14T00:36:30+00:00
- Closed at: 2020-06-19T21:56:35+00:00
