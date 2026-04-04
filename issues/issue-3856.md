---
title: Cannot build just "monero-wallet-gui" target, as it has strong dependency on
  target "daemon"
source_url: https://github.com/monero-project/monero-gui/issues/3856
author: jjakob
assignees: []
labels: []
created_at: '2022-03-10T16:46:58+00:00'
updated_at: '2022-04-01T07:49:56+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi. I am trying to make an ebuild for Gentoo that will would build only the monero-wallet-gui binary and not the entire monero daemon and all the targets that it provides, because those are already provided by the "monero" ebuild, which causes this ebuild to have conflicting binary files and thus fails to install.

Even when cloning this repository manually and running cmake as described in the readme, it still has the same dependencies.
I did a debug of dependencies in CMakeLists.txt: `set_property(GLOBAL PROPERTY GLOBAL_DEPENDS_DEBUG_MODE 1)`
The dependency list is in the cmake output:
[monero-gui-make-out.txt](https://github.com/monero-project/monero-gui/files/8225335/monero-gui-make-out.txt)

```
target 378 is [monero-wallet-gui]
  depends on target 107 [epee] (weak)
  depends on target 57 [easylogging] (weak)
  depends on target 125 [common] (weak)
  depends on target 133 [cncrypto] (weak)
  depends on target 71 [randomx] (weak)
  depends on target 200 [net] (weak)
  depends on target 266 [wallet_api] (weak)
  depends on target 256 [wallet] (weak)
  depends on target 232 [rpc_base] (weak)
  depends on target 192 [multisig] (weak)
  depends on target 150 [ringct] (weak)
  depends on target 168 [cryptonote_basic] (weak)
  depends on target 158 [checkpoints] (weak)
  depends on target 166 [cryptonote_format_utils_basic] (weak)
  depends on target 348 [device] (weak)
  depends on target 148 [ringct_basic] (weak)
  depends on target 140 [wallet-crypto] (weak)
  depends on target 117 [version] (weak)
  depends on target 340 [blocks] (weak)
  depends on target 176 [cryptonote_core] (weak)
  depends on target 216 [blockchain_db] (weak)
  depends on target 50 [lmdb] (weak)
  depends on target 208 [hardforks] (weak)
  depends on target 224 [mnemonics] (weak)
  depends on target 356 [device_trezor] (weak)
  depends on target 64 [qrcodegen] (weak)
  depends on target 394 [openpgp] (weak)
  depends on target 386 [qrdecoder] (weak)
  depends on target 363 [quirc] (weak)
  depends on target 370 [translations] (weak)
  depends on target 402 [zxcvbn] (weak)
  depends on target 318 [daemon] (strong)
  depends on target 385 [monero-wallet-gui_autogen] (strong)
```
```
target 385 is [monero-wallet-gui_autogen]
  depends on target 57 [easylogging] (strong)
  depends on target 64 [qrcodegen] (strong)
  depends on target 107 [epee] (strong)
  depends on target 125 [common] (strong)
  depends on target 200 [net] (strong)
  depends on target 266 [wallet_api] (strong)
  depends on target 370 [translations] (strong)
  depends on target 386 [qrdecoder] (strong)
  depends on target 394 [openpgp] (strong)
  depends on target 402 [zxcvbn] (strong)
target 386 is [qrdecoder]
  depends on target 363 [quirc] (weak)
  depends on target 393 [qrdecoder_autogen] (strong)
```

I suspect that the reason I can't produce just the monero-wallet-gui binary, is because it has a strong dependency on "daemon" which means that even if I run "make monero-wallet-gui" to build just that target, it will build all the daemon binaries.

I think it's entirely unnecessary to have to build everything that's then not needed as it wastes resources (especially for distributions like Gentoo where users build their own packages).

# Discussion History
## mj-xmr | 2022-04-01T07:49:56+00:00
Thanks for pointing it out. I'm on my way to handle it, but it will take a couple of iterations. The first PR in this direction is https://github.com/monero-project/monero-gui/pull/3858

# Action History
- Created by: jjakob | 2022-03-10T16:46:58+00:00
