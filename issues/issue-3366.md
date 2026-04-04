---
title: how to build monero with xcode??
source_url: https://github.com/monero-project/monero/issues/3366
author: '15963'
assignees: []
labels:
- invalid
created_at: '2018-03-07T09:53:51+00:00'
updated_at: '2019-04-16T23:25:29+00:00'
type: issue
status: closed
closed_at: '2019-04-16T23:25:28+00:00'
---

# Original Description
I try with cmake ./ -G "Xcode" . 
The project has been successfully created,but the compilation is wrong.
Help me , thank you !
Error info :

PhaseScriptExecution CMake\ Rules build_for_xcode/src/blockchain_utilities/monero.build/Release/blockchain_import.build/Script-3F7E2C46A49B4964A5A72EB6.sh
    cd /Users/fu/Desktop/work/monero
    /bin/sh -c /Users/fu/Desktop/work/monero/build_for_xcode/src/blockchain_utilities/monero.build/Release/blockchain_import.build/Script-3F7E2C46A49B4964A5A72EB6.sh

cd /Users/fu/Desktop/work/monero/src/blockchain_utilities && touch stub.c && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang -o stub.o -c stub.c
cd /Users/fu/Desktop/work/monero/src/blockchain_utilities && /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/ld -z noexecstack -z noexecheap -r -sectcreate __DATA __blocks_dat ../blocks/checkpoints.dat -o /Users/fu/Desktop/work/monero/build_for_xcode/src/blockchain_utilities/blocksdat.o stub.o && rm -f stub.*
ld: unknown option: -z
make: *** [/Users/fu/Desktop/work/monero/build_for_xcode/src/blockchain_utilities/blocksdat.o] Error 1
Command /bin/sh failed with exit code 2


# Discussion History
## jtgrassie | 2018-03-08T18:45:39+00:00
Firstly, building with the Xcode IDE is not a supported build method. Supported method is outlined in the README.

Secondly, if you must try and get the project into Xcode, I suggest you take a look in the Makefile to ensure you are passing the required options to cmake. Of note, you really need to do an out-of-source build (run cmake from a directory like build/release). But honestly, why bother at all. Just build from the command-line.

## moneromooo-monero | 2018-09-14T12:13:02+00:00
This looks like your linker does not like -z.
It might be necessary to update the option detection system.
Please paste the output of the following commands:

echo "int main(void){return 0;}" | gcc -c -x c -o a.o -
ld -z noexecheap a.o


## moneromooo-monero | 2019-04-16T23:08:07+00:00
No further info, reopen if supplied.

+invalid

# Action History
- Created by: 15963 | 2018-03-07T09:53:51+00:00
- Closed at: 2019-04-16T23:25:28+00:00
