---
title: Wrong hashes produced by Keccak1600 implementation on big-endian platforms
source_url: https://github.com/monero-project/monero/issues/4392
author: AlexAltea
assignees: []
labels: []
created_at: '2018-09-17T02:45:29+00:00'
updated_at: '2018-09-21T18:45:35+00:00'
type: issue
status: closed
closed_at: '2018-09-21T18:45:35+00:00'
---

# Original Description
Issue is pretty much self-explanatory. The most likely culprit are unsafe pointer type casts, that appear in the implementation [`src/crypto/keccak.c`](https://github.com/monero-project/monero/blob/master/src/crypto/keccak.c). E.g.:

https://github.com/monero-project/monero/blob/master/src/crypto/keccak.c#L108
https://github.com/monero-project/monero/blob/master/src/crypto/keccak.c#L124

## Proof-of-concept
```c
int main()
{
    uint8_t hash[200];
    keccak1600("", 0, hash);
    hexdump(hash, 200);
    return 0;
}
```

Expected result (output on my x86 computer):
```
C5D2460186F7233C927E7DB2DCC703C0E500B653CA82273B7BFAD8045D85A4703DBB9A2CD87CA974B9A2B0EC61119BCB5CEDF9C0C411221F6141A25F17C60D82D24680ABBCBFBA815B762B24B751D5B1E85325BA5E6DF23C10725BFE986ACE3BA2D24535A79F7DBABB153BB0D33C0DFA09CEC712EBD7FE3B49A9194E859C82EBFF11A645651A5D1B726BE100F44641069FAB7164E13487FE3609BBEEBD88309CBAACB2A7ECB8E8DE2145CF1DB7623B16916D7210991B576BBE182362CF22FAB7D7AF9F77F71AFEA3
```
Output on big-endian machines:
```
4A3D5976EDD24A1A22F7FAE2985B3BD41798EB1176802B50E5612F3E739D3C97FD3980B0DDE09F15F7B03912A94091D65666F12BE92101C5D5473A2AAEF0715B1B8557865FEFC35FAF881B6130248A82657828CE691B6735E444A21B7E4FFD8E348AA2FCB438DF080DD77CEB98D486D2CB97A1C48152F1E5E0EB69D0C38305812883C1C67718879F81A607A48B12EBFD7AF50944B97FDD4C9C46C0CB353EA8C19F307B56FFA4EF8C1D8B7E9086C977E5C517A7AEA67EF838C925E9497A50DACBB6FC06228EBC4523
```

# Discussion History
## moneromooo-monero | 2018-09-17T07:31:36+00:00
Do you know if there's a way to run code on big endian machines somewhere on the internet (ie, without having an actual big endian machine around) ?

## AlexAltea | 2018-09-17T11:02:39+00:00
@moneromooo-monero There's several alternatives:

1. Most likely your router is a big-endian machine (many of them still run MIPS).
2. You can emulate a Linux kernel built for any big-endian architectures (e.g. SPARC, MIPS, PowerPC) with QEMU, then fetch and compile *keccak.c* within the emulator.
3. You can cross-compile *keccak.c* to big-endian architectures (e.g. SPARC, MIPS, PowerPC), and run the resulting binary with QEMU in userland mode.


## jtgrassie | 2018-09-17T14:10:10+00:00
There is a byte order safe version at https://github.com/mjosaarinen/tiny_sha3/blob/master/sha3.c. However, it's not just the Keccak code in Monero that is byte order dependent. I have raised this many times with people assuming a PPC port would be easy - it's not - there is just soo much that would need porting / checking.

## AlexAltea | 2018-09-17T14:36:28+00:00
@jtgrassie Thanks for pointing out that other implementation. I've just fixed Monero's *keccak.c*, with minimal changes by relying on *common/int-util.h*.

# Action History
- Created by: AlexAltea | 2018-09-17T02:45:29+00:00
- Closed at: 2018-09-21T18:45:35+00:00
