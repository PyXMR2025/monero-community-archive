---
title: '[WIP] Trezor integration roadmap'
source_url: https://github.com/monero-project/monero/issues/4810
author: ph4r05
assignees: []
labels: []
created_at: '2018-11-06T11:51:25+00:00'
updated_at: '2022-07-20T20:20:38+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:20:37+00:00'
---

# Original Description
This issue aims to track progress and road map of the further TREZOR integration. Builds on already merged PR https://github.com/monero-project/monero/pull/4241. Issue can also collect feedback / feature requests for Trezor.

### Merged:

#### https://github.com/monero-project/monero/pull/4241 TREZOR: initial integration proposal
- First PR adding Trezor support.

#### https://github.com/monero-project/monero/pull/4824 device/trezor: webusb transport added, cmake fixes
- [x] Add compile time option to exclude Trezor from Monero build.
- [x] CMake refactoring, graceful Trezor support disabling when protobuf fails or other dependency fails. 
- [x] Add WebUSB device transport. Depends on libusb, enables direct connection to Trezor without Bridge.
- [x] Simplify message protocol, prepare for testing (callback on Trezor events, e.g., button request, pin entry request)

#### https://github.com/monero-project/monero/pull/4839 device/trezor: trezor improvements
- [x] Automatic key images sync after wallet recovery from Trezor (required to perform after wallet restore for already used wallets, i.e., wallet spent something before restore)
- [x] Passphrase entry on host (so far only device-based passphrase entry is supported)
- [x] Enable to use multiple wallets derived from the primary device seed. I.e., command line argument `--hw-device-wallet-code` for [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) / [SLIP-10](https://github.com/satoshilabs/slips/blob/master/slip-0010.md) wallet derivation algorithm. Enables to maintain multiple independent Monero wallet with one device. 
- [x] UDP transport disabled by default (on production)

#### #4945 Build: protobuf fixes for docker, cross-compilation
- [x] Docker build fixes
- [x] Protobuf dependency fixes, compilation test in the cmake (to make sure the real compilation passes)
- [x] Dependencies for GUI compilation

#### #4977 device/trezor: integration tests
- [x] Add debug link (*!!only in testing mode!! Not compiled in release mode. Production Trezor firmware does not support debug link*. Debug connection to Trezor, automatically press confirm button in emulator during test cases)
  - [x] wipe + init + load seed
- [x] Add transaction signing test cases
  - [x] Various transaction scenarios for testing (# of UTXO, outputs, mixins, sub-addresses, payment_id)
  - [x] Support code to facilitate Trezor testing (scenarios, chain generation, RCT transaction testing)
  - [x] Verification of Trezor signed transaction (hashes, serialization, rangeproof, MLSAG) 

#### #4889 wallet: rescan bc with preserving key images
- [x] Spent check with untrusted node. Key image sync, key image import and rescan_spent can be performed with untrusted node now using new command (idea: rescan blockchain for transactions while preserving previous key images)

#### #5211 device/trezor: HF10 protocol upgrade
  - [x] HF 10 protocol upgrade (v2 Bulletproof)
 - [x] get_tx_key functionality 
 - [x] live refresh (compute KI on the fly during foreground refresh, eliminates need for key image sync)
 - [x] tx_proof
 - [x] wallet API for transaction cold signing, KI sync

#### GUI https://github.com/monero-project/monero-gui/pull/2019 device: Trezor support added 
 - [x] Initial Trezor GUI support

#### GUI https://github.com/monero-project/monero-gui/pull/2037 Async device open and create from device, passphrase entry 
- [x] Passphrase entry for GUI wallet. As passphrase entry on host is a security risk we won't support this method.


#### https://github.com/monero-project/monero/pull/5355 wallet: early listener set 
 - [x] Early listener set for passphrase entry in Wallet::API and GUI 

#### #5398 Trezor: test fixes and improvements
 - Test fixes 

#### https://github.com/monero-project/monero/pull/5477
 - Correct key image live refresh notification ended sending

#### https://github.com/monero-project/monero/pull/5476
 - Disable T1 support (was enabled by default)
 - Enable to sort Trezor device lists by TREZOR_PATH - usable for GUI

#### https://github.com/monero-project/monero-gui/pull/2147
 - Async TX commit.

### In PR:

### Work in progress:
 
### ToDo

#### Web wallet, mymonero
- [ ] Pick and implement viable device transport method
- [ ] Transpile Trezor related code
- [ ] Implement missing Trezor related code

### Backlog, not on the main roadmap:
I have a design done for the following, however, implementation is not planned at the moment. I can help/supervise if somebody wants to implement this. It's not hard, just takes time which I don't have right now:

- [ ] spend_proof
- [ ] reserve_proof

#### Multisig
The multisig is half-designed and would require ETA 1-4 weeks of work. I am open to consultacy for volunteers :) 

## Usage

```bash
sudo apt-get install protobuf-compiler libprotobuf-dev  libusb-1.0-0-dev  # ubuntu
brew install protobuf  libusb  # OSX

./monero-wallet-cli --hw-device Trezor --generate-from-device ~/wallet_file --restore-height 10000 --log-file ~/monero.log  --log-level 3
```

## Troubleshooting

If you experience `Bad offset calculation` error when creating a transaction the remote node you are using is probably running too old version. Use either local up-to-date daemon or trusted remote node.

The code is known to work with version `131076`. For testing purposes, try node `173.255.205.142:18089`, it should work smoothly (do not trust the node, better run own).


# Discussion History
## sedited | 2018-11-07T19:03:22+00:00
I'd suggest to make building with Trezor support optional. It does add another dependency and another way to communicate with the client, which might be undesired in some cases. 
The device class detection for example as currently done for Ledger in device/device.hpp (which is already included) seems suitable for this. 

## ph4r05 | 2018-11-07T19:27:34+00:00
> I'd suggest to make building with Trezor support optional. It does add another dependency and another way to communicate with the client, which might be undesired in some cases.
> The device class detection for example as currently done for Ledger in device/device.hpp (which is already included) seems suitable for this.

I am not sure I understood correctly but the Trezor support is built in only if the dependency is met. Moreover, the Monero binaries do not interact differently with the environment (as before the Trezor) unless you exlicitly use `--hw-device Trezor` command line arg.   

But sure, I can make the same thing as Ledger has (below) with default value enabled, but it would support to exclude it from the build. I will add this to the ToDo list.

```
#ifndef USE_DEVICE_LEDGER
#define USE_DEVICE_LEDGER 1
#endif

#if !defined(HAVE_HIDAPI) 
#undef  USE_DEVICE_LEDGER
#define USE_DEVICE_LEDGER 0
#endif
```

Is that what you have in mind?

## sedited | 2018-11-07T19:40:33+00:00
Currently when you run cmake and have protobuf, but not the pip protobuf package, cmake will pass, but the build will fail. Cmake should never pass on a failing build. 

## ph4r05 | 2018-11-07T19:43:33+00:00
> Currently when you run cmake and have protobuf, but not the pip protobuf package, cmake will pass, but the build will fail. Cmake should never pass on a failing build.

Thats true, I will fix this cmake problem. Do you have a cmake log from this? Trezor support is built only if messages were generated successfully (`TREZOR_PROTOBUF_GENERATED` variable), but there must be some problem with cmake failing if `execute_process` returns non-zero code. I do print warning message if protobuf build failed, but it should not fail the whole build, just disable Trezor support.

## sedited | 2018-11-07T19:49:32+00:00
Build log: https://paste.debian.net/1050822/

## paulshapiro | 2018-11-07T23:04:57+00:00
@ph4r05 - super exciting. Just want to chime in here to let you know I'll shortly be looking at adding the C++ -> JS generalized bridge which would be necessary for hw device support in transpiled C++ to talk to any stuff in JS (such as transport code). (It looks like the same sort of bridge will be useful for us moving the last tiny part of our send-funds routing to C++ as it integrates with network requests and it's good to let those remain independent.) Please feel free to reach out to me at any time to chat about implementation details. Very happy to help. Ledger support is also coming to core-js before very long so any work that ends up happening here by the time that really gets under way will probably be a massive help. 💥

## ph4r05 | 2018-11-08T09:03:25+00:00
> Build log: https://paste.debian.net/1050822/

I've just checked it, the protobuf python library is not required (it was before but on current master it is without it)

The build log did not give reason why it failed 😕 
I am working on PR with more pedantic cmake rules so if something breaks Trezor is not built.

## ph4r05 | 2018-11-09T12:18:00+00:00
@TheCharlatan, does PR https://github.com/monero-project/monero/pull/4824 fixes the problem you are experiencing?

## sedited | 2018-11-10T11:23:41+00:00
@ph4r05 It does handle it more gracefully. I noticed too now, that the python lib is not required (lol). I have my protoc executable at a non-standard location. CMake correctly detects this, because I set the PROTOBUF_PROTOC_EXECUTABLE variable. This variable is not passed into the python script though. I think this is easily fixable by just passing the variable from the CMakeLists in src/trezor to build_protob.py and from there to pb2py in the submodule. Would such a change to the submodule be acceptable?

## ph4r05 | 2018-11-11T14:10:53+00:00
@TheCharlatan I've updated the PR. Cmake sets corresponding protobuf variables to the ENV vars, the python script then checks for env vars and uses them if set. Now it should work for you, if you want to give it a try. 

## janjilek | 2018-11-28T07:31:16+00:00
Hello, I just tried send transaction to few exchanges and all of them lost my transaction due wrong payment id. I think, that there is something broken with Trezor T integration and payment id computation.

## ph4r05 | 2018-11-28T08:21:32+00:00
> Hello, I just tried send transaction to few exchanges and all of them lost my transaction due wrong payment id. I think, that there is something broken with Trezor T integration and payment id computation.

Unfortunately, you are right. Yesterday we detected there is a problem with the payment ID computation and we are working on it since then.

More technical details on this problem:
https://github.com/trezor/trezor-core/pull/426

We are working on fixes and mitigation. I am also implementing the check to the Monero client. We are deeply sorry for caused problems. 

## ph4r05 | 2018-11-28T09:24:46+00:00
update: the client-side check will be implemented today. It will reject all transactions with short payment IDs on firmware v2.0.9 and lower.

Trezor firmware v2.0.9 does not correctly encrypt short payment ID in outgoing transactions. This firmware version should not be used for sending transactions with short payment IDs and integrated addresses (more than 95 characters). No funds are lost but a recipient of your payment will have problems pairing the payment (e.g., exchanges). Please update the firmware as soon as it becomes available. 

We are also working on extensive Monero integration tests directly in Monero C++ codebase.

## janjilek | 2018-11-28T11:44:47+00:00
Thank you!

Yeah, I use split_integrated_address wallet rpc call to get address and payment id from integrated address. Other temporal solution is to create new wallet in monero-wallet-cli and transfer some funds there. There is no issue with transfer to integrated address in cli without trezor :-)

Anyway, thanks for the updates and good luck with the integration!
 

## ph4r05 | 2018-11-29T12:24:40+00:00
Mitigation added to https://github.com/monero-project/monero/pull/4839

## jeliman1 | 2018-12-04T11:49:49+00:00
Hello ph4r05!
I have a question. Can you tell me when monero wallet will be in Trezor T without needing linux?  I am waiting for it and can not wait. Thank you very much. Good job!

## ph4r05 | 2018-12-04T18:18:46+00:00
@jeliman1 if you can build windows binaries with Trezor support on linux (mingw) I think you could use that. Otherwise, you need to wait for Monero official release with Trezor support (windows binary).

Regarding GUI and Webwallets - no ETA, work in progress. We definitelly won't make it this year, but GUI hopefully Q1 2019, webwallets.

## dEBRUYNE-1 | 2018-12-04T18:44:43+00:00
@ph4r05 - Would he be able to use a buildbot binary from master if the buildbot has the necessary dependencies installed? 

## ph4r05 | 2018-12-04T18:46:11+00:00
@dEBRUYNE-1 I think it could be possible but it one needs to try it.

## ph4r05 | 2018-12-04T20:36:04+00:00
@dEBRUYNE-1 I've just checked and the win buildbot is missing protobuf. If we can add it it might be quite helpful :)
Maybe also the libusb for Win, but that is not required. 

## dEBRUYNE-1 | 2018-12-04T20:39:51+00:00
Thanks for checking. 

Pinging @danrmiller, could you please add protobuf to the win buildbot? 

## danrmiller | 2018-12-06T20:38:08+00:00
I've built and installed protobuf on win64 msys2 and re-run the build for PR #4839 

https://build.getmonero.org/builders/monero-static-win64/builds/6208

```
-- Found Protobuf: C:/msys64/mingw64/lib/libprotobuf.a (found version "3.6.1") 
-- Trezor protobuf messages regenerated 
```

I'll look into libusb.

## ph4r05 | 2018-12-06T21:55:34+00:00
great! The #4945 then fixes protobuf and libusb for docker builds.
I am fixing libusb on docker osx, it works on all other machines (protobuf+libusb)

## dEBRUYNE-1 | 2018-12-17T16:31:08+00:00
@ph4r05 - I'd personally prefer for the 'advanced' features (reserve proof, spend proof, multisig) to be put at the bottom of the priority list (even after web wallet / mymonero integration). Whilst beneficial, those features are scarcely used. Furthermore, I think the Monero ecosystem would currently benefit more from having Trezor integrated with the GUI and MyMonero. 

P.S. Thanks for all the awesome work you've done so far :+1: 

## ph4r05 | 2018-12-17T16:32:45+00:00
@dEBRUYNE-1 I agree. Advanced features are on backlog. It has the lowest priority. I will reorder it in the main description. And thanks for the support! I appreciate it.

## dEBRUYNE-1 | 2018-12-17T17:46:56+00:00
You're welcome and the edit is certainly beneficial. 

## dEBRUYNE-1 | 2019-02-12T16:45:37+00:00
@ph4r05 - As GUI integration is on the roadmap, the GUI contributors would like to discuss how to best integrate this functionality (i.e. creating and using a Trezor Monero wallet with the GUI). Would you perhaps be able to join us on IRC (I noticed you are already present in the GUI channel) for a discussion  some time this week?

## prusnak | 2019-02-12T17:00:49+00:00
@dEBRUYNE-1 What is the timeline for the next Monero major release? Can we make sure to have the Trezor GUI ready by then?

## dEBRUYNE-1 | 2019-02-12T18:04:42+00:00
@prusnak - The schedule has changed slightly due to the decision to bring forward the scheduled protocol upgrade of April to the beginning of March (to preserve ASIC resistance). 

https://www.reddit.com/r/Monero/comments/apkvym/asic_resistance_hashrate_discussion_thread/

Essentially, the upcoming major release (0.14 - intended to be released within two weeks) will be the `release-v0.13` branch plus the planned consensus changes. The subsequent point release (presumably 0.14.1 -intended to be released a few weeks later) will be build off master and thus include full Trezor support for the CLI. 

With respect to the GUI, the release schedule is similar (typically CLI and GUI binaries are released in conjunction). Thus, we've got about 4 to 6 weeks left to include full Trezor support in the GUI. Now, the GUI already shares a lot of code with the CLI. Additionally, I *think* some of the Ledger code can be utilized. Thus, in my opinion, including full Trezor support in the GUI should be feasible within the remaining time.  

P.S. In the past, a Ledger Monero wallet generated by the CLI would work properly in the GUI (even when the GUI did not have the ability to directly generate a Ledger Monero wallet). I'd expect this to be similar for a Trezor Monero wallet, although I am not entirely certain. 

## mariodian | 2019-03-26T01:53:10+00:00
> Passphrase entry for GUI wallet. As passphrase entry on host is a security risk we won't support this method.

You already support passphrase entry on host via monero-wallet-cli. Why is it a security issue suddenly? 

## ta32 | 2019-03-26T06:09:15+00:00
> Passphrase entry for GUI wallet. As passphrase entry on host is a security risk we won't support this method.

In the trezor wallet there is an option to enter passphrase on the host. The passphrase protects the seed so even if a keylogger captures it, that is is off no significance. Furthermore on the trezor one, that is the only way you can enter the passphrase.

This might force a user, to not use a passphrase for their monero account (if its complex with special characters), which is obviously less secure than entering a passphrase on the host.

so please consider giving a user the option to enter their passphrase from the host 


## ph4r05 | 2019-03-26T07:58:07+00:00
> You already support passphrase entry on host via monero-wallet-cli. Why is it a security issue suddenly?

The opinios are my own, Trezor/SatoshiLabs may have a different view on this particular matter.

It is a security issue also in `monero-wallet-cli` and users are advised to prefer device-based entry. 

Implementing passphrase entry on the host for Monero GUI is technically difficult, a lot of refactoring would be required so I decided to drop the support for following releases for the sake of having Trezor support released soon. And as I perceive host-entry as a risk, the feature drop was quite easy decision.

The support may be added in further releases, but it would require additional work and thinking how to do it properly so the user is aware of all risks of this entry method. 

Monero GUI is more user-friendly and with host-based entry enabled inexperienced users could choose this less secure variant. The passphrase should be entered on device. 

> Furthermore on the trezor one, that is the only way you can enter the passphrase.

This is currently not relevant as T1 is not supported at the moment.

> The passphrase protects the seed so even if a keylogger captures it, that is is off no significance. 

I disagree. In my opinion, host-based entry is a security risk as it makes targetted attack easier (especially if user uses GUI on the ordinary workstation for every daywork).

> This might force a user, to not use a passphrase for their monero account (if its complex with special characters), which is obviously less secure than entering a passphrase on the host.

Having some passphrase is definitely better than no passphrase, true. Choosing a different passphrase changes the wallet so I would recommend choosing a strong passphrase that can be entered on device and transfer the Monero funds there. Command line wallet has host-based entry so this conversion should be easy as existing user had to compile master to use it anyway.

> so please consider giving a user the option to enter their passphrase from the host

The feature may be implemented in future releases, depends on the view of the Trezor and community.

## prusnak | 2019-03-26T11:13:36+00:00
I agree with all of the above, let's not enter the passphrase on the host for now.

## mariodian | 2019-04-01T05:45:56+00:00
> let's not enter the passphrase on the host **_for now_**.

I agree. But it should be added in the future if for nothing else then to be consistent from the UX point of view with the CLI and even your own web wallet for other cryptos. 

## jeliman1 | 2019-05-10T08:42:45+00:00
Hi guys, what's state? Will be monero in Trezor T within a month? Thank you!

## dEBRUYNE-1 | 2019-05-10T13:28:11+00:00
@jeliman1 - There will be a new release soon that features full Trezor support (for both the GUI and the CLI).

## JochananCZ | 2019-06-23T21:06:05+00:00
I was able to type a passphrase on the host (monero gui application). I thought that have been turned off. @ph4r05 @dEBRUYNE-1 
(passphrase and after that i have typed wallet password - I am using Win64 buildbot version)

## ph4r05 | 2019-06-23T21:22:32+00:00
Passphrase host entry is enabled

## dEBRUYNE-1 | 2019-06-23T21:22:40+00:00
@JochananCZ - The option was enabled in a later pull request (which is included in both the CLI v0.14.1.0 and the upcoming GUI v0.14.1.0 release). 

## jeliman1 | 2019-08-06T11:14:53+00:00
Hi @ph4r05, when will be enable trezor t in mymonero.com online wallet please? Waiting for it with my friends. Thank you for reply!

## prusnak | 2019-08-06T11:44:10+00:00
@jeliman1 using Monero with an online wallet is a very bad idea

## jeliman1 | 2019-08-06T11:46:40+00:00
@prusnak Is not like a go to etherwallet by TREZOR T? I think yes.

## prusnak | 2019-08-06T19:21:57+00:00
The only reason why would one want to use Monero is privacy. With web wallet you lose that only property.

## paulshapiro | 2019-08-06T19:30:34+00:00
> The only reason why would one want to use Monero is privacy. With web wallet you lose that only property.

That's not totally true. If a person runs OpenMonero for their web wallet, how is it a loss? Plus, the same basic code to enable hw wallet integration for web wallets (via mymonero-core-cpp/js) would enable hw wallet integration in every other light wallet, e.g. desktop and mobile, and with those, you don't even need to host a web wallet as you can just use a normal lightweight wallet client and specify the URL of the server you want to connect to.

## paulshapiro | 2019-08-06T19:33:01+00:00
> Hi @ph4r05, when will be enable trezor t in mymonero.com online wallet please? Waiting for it with my friends. Thank you for reply!

We've been trying to work on hw wallet support in lightwallets (in other words, mymonero-core-cpp) via partnership but at the moment we cannot prioritize it even though the amount of effort to add it is very, very low, since we already work with the same code that supports hw wallets in the official Monero apps. If Trezor support is desired in this considerably wider range of applications then it's a very low hanging fruit.

Secondly, in terms of the security of web wallets, anyone using mymonero.com can also use SecureBrowse (https://securebrowse.gitlab.io/securebrowse) in order to (as far as we know) 100% prevent the possibility of the execution of hypothetical potential compromised code. 

## paulshapiro | 2019-08-06T19:34:54+00:00
No reason not to have hardware wallet support in a web wallet .. we can do the transport very easily and extensibly through the existing browser / plugin support for these ... and since hybrid mode is coming so soon (a singular API for flipping a wallet between lightweight and fullweight mode so you can stream blocks and scan them on your device - *considerably* more efficient for teams to integrate with and maintain - I think it'll be the future) then there is literally no privacy or security model difference except, afaik, as regards the fact executable code still must be downloaded and the technique for ensuring its integrity differs.

## Cactii1 | 2022-07-20T20:18:41+00:00
Monero is now fully supported on a Trezor T.

Propose to close.

## selsta | 2022-07-20T20:20:37+00:00
While some of the `ToDo` items are not implemented yet, it's unclear when or if they will get implemented and I don't think we have to keep this open.

# Action History
- Created by: ph4r05 | 2018-11-06T11:51:25+00:00
- Closed at: 2022-07-20T20:20:37+00:00
