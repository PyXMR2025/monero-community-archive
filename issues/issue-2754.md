---
title: Offer monero builds where all binaries are signed
source_url: https://github.com/monero-project/monero-gui/issues/2754
author: mcgroarty
assignees: []
labels: []
created_at: '2020-01-29T22:32:43+00:00'
updated_at: '2020-06-29T22:07:05+00:00'
type: issue
status: closed
closed_at: '2020-06-29T22:06:42+00:00'
---

# Original Description
Currently, most of the executables in a Monero install are unsigned. eg., on macOS:

```
$ find /Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras/ -type f -exec codesign --verify {} \; 
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-gen-trusted-multisig: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-depth: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-wallet-cli: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-ancestry: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-usage: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-gen-ssl-cert: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-prune-known-spent-data: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-wallet-rpc: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-mark-spent-outputs: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-stats: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-prune: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-export: code object is not signed at all
In architecture: x86_64
/Applications/Monero/monero-wallet-gui.app/Contents/MacOS/extras//monero-blockchain-import: code object is not signed at all
In architecture: x86_64
```

This is a big red flag for AntiVirus engines.

AntiVirus vendors typically rely on reputation associated with a code signing key when determining whether to trust a binary. It's far from the only heuristic they use, but it seems to be heavily weighted. Some vendors flat out flag all unsigned binaries as malware unless they come from companies which are large enough to create large support case loads.

Additionally, when malware installs Monero mining binaries, AntiVirus vendors may be talked into focusing on the unsigned binaries that install copies of a signed miner rather than flagging the miner itself.

# Discussion History
## selsta | 2020-01-29T23:01:15+00:00
Code signing + reproducible builds don’t mix well :/

## mcgroarty | 2020-01-29T23:53:08+00:00
That's an important consideration. To the best of my knowledge, code signatures are appended to the end of the file and the remainder of the file is unchanged.

Is anyone aware of a supported platform that handles that differently?

Is anyone aware of a comparison tool that can ignore the signature section and compare the remainder of an executable?

## selsta | 2020-01-31T14:17:30+00:00
AFAIK Bitcoin core found a workaround (at least on macOS), but the process is complicated and results in that the final signature can’t easily be verified.

## selsta | 2020-06-29T22:06:42+00:00
The macOS GUI binaries are now codesigned and will also be notarized in the future.

# Action History
- Created by: mcgroarty | 2020-01-29T22:32:43+00:00
- Closed at: 2020-06-29T22:06:42+00:00
