---
title: View-only wallet creation leads to an avalanche of warnings and errors
source_url: https://github.com/monero-project/monero/issues/6759
author: OxMarco
assignees: []
labels: []
created_at: '2020-08-14T17:26:32+00:00'
updated_at: '2020-12-23T01:04:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After creating a view-only wallet with `generate_from_keys` I get a large amount of warnings and errors, mainly these three repeated several times. The RPC daemon becomes unresponsive to other calls.

```
E wrong number of additional derivations
W Transaction extra has unsupported format: <txid>
W Failed to generate key derivation from tx pubkey, skipping
```


# Discussion History
## moneromooo-monero | 2020-08-14T21:24:29+00:00
Those are fine, unless they're really many. Define many.
When the daemon becomes unresponsive, run this in gdb on the stuck process: thread apply all bt


## OxMarco | 2020-08-15T16:57:46+00:00
Here's a dump of Monero wallet rpc outputs

```
2020-08-15 16:53:02.823	W Transaction extra has unsupported format: <19435835c387fac0162ae2efcbc744751733ffa6c4932df354ede6846d4f0ece>
2020-08-15 16:53:02.825	W Transaction extra has unsupported format: <23ccce199ddf1d80833335b46f509ad12088aa47bfa68343db6a8469cc53cecb>
2020-08-15 16:53:02.825	W Transaction extra has unsupported format: <a5e50d89d4261036faf3d6d32f321e71ec8d810c64f268f321a3fe0cf8ee7968>
2020-08-15 16:53:02.904	W Public key wasn't found in the transaction extra. Skipping transaction <a5e50d89d4261036faf3d6d32f321e71ec8d810c64f268f321a3fe0cf8ee7968>
2020-08-15 16:53:02.904	W Public key wasn't found in the transaction extra. Skipping transaction <19435835c387fac0162ae2efcbc744751733ffa6c4932df354ede6846d4f0ece>
2020-08-15 16:53:02.904	W Public key wasn't found in the transaction extra. Skipping transaction <23ccce199ddf1d80833335b46f509ad12088aa47bfa68343db6a8469cc53cecb>
2020-08-15 16:53:43.553	W Public key wasn't found in the transaction extra. Skipping transaction <79c89de5700e796ea6dead9142741a8569ba0154841bf92b95a01064e4b946ad>
2020-08-15 16:53:43.553	W Public key wasn't found in the transaction extra. Skipping transaction <1f921152a002fb1dd8c3aeddfc8a984833646f7282e913747678ccaad068b818>
2020-08-15 16:53:43.553	W Public key wasn't found in the transaction extra. Skipping transaction <6245b9cabc214e4108c425de3a53a47663da2eb7ca09e9e71b74d3f627aa07b8>
2020-08-15 16:53:43.553	W Public key wasn't found in the transaction extra. Skipping transaction <4a9561e2c3fd7af05bda953c3fa7681dc859ded7482ecc1b577413e5e6a04d78>
2020-08-15 16:53:43.554	W Public key wasn't found in the transaction extra. Skipping transaction <6900ad86a1e352e1d0d234ef4e7e8722166f230cd9e2184d3242eb47219da6a6>
2020-08-15 16:53:43.554	W Public key wasn't found in the transaction extra. Skipping transaction <7444886d832c68000f7642e60683321708f4c113500f5c9fc06a6aa6ac4b9899>
2020-08-15 16:53:43.554	W Public key wasn't found in the transaction extra. Skipping transaction <4d49fd6c672dd18588312b5d94c2ddd131458265f8c5dc3fb674316113d519d6>
2020-08-15 16:53:43.554	W Public key wasn't found in the transaction extra. Skipping transaction <339bdfa7aa9ca78a170206cd62c9f512964503953d0c499fe8770fdc6e4ddd75>
2020-08-15 16:53:43.554	W Public key wasn't found in the transaction extra. Skipping transaction <cd9dcf9b14a1062e6580b025ce7a01cd815cb86e7f75b6b949a9af1b53396980>
2020-08-15 16:53:43.554	W Public key wasn't found in the transaction extra. Skipping transaction <fc073a50ef1085fdb4dfb4839a5bc39a533edb415018b6729aa19de1b0f5eff6>
2020-08-15 16:53:43.555	W Public key wasn't found in the transaction extra. Skipping transaction <b8bbb9795efe24213b43aa37f5cc04b19e93c7f46c7e59750af8310430cb9c2b>
2020-08-15 16:53:43.555	W Public key wasn't found in the transaction extra. Skipping transaction <48a035153cd7ceb41f551ba540cc49e7f0be080a65717f0e44adb92854557a58>
2020-08-15 16:53:43.555	W Public key wasn't found in the transaction extra. Skipping transaction <7031493c7256f89a62acf8036ed6982d6b5bc4eb6a4189e5f736d2585b3061bd>
2020-08-15 16:53:43.555	W Public key wasn't found in the transaction extra. Skipping transaction <a152ee9480b78503aca64ae2ea65d035697b14cfd7560e072aa582822bb07f11>
2020-08-15 16:53:43.556	W Public key wasn't found in the transaction extra. Skipping transaction <10771293ee5eee2545257e1d880baa8454959341d41c363054adc346d802d8b1>
2020-08-15 16:53:43.556	W Public key wasn't found in the transaction extra. Skipping transaction <47d4235e9bafc33e4b5f80825b1a8013fc6e78b1662b20694543857be854a716>
2020-08-15 16:53:43.556	W Public key wasn't found in the transaction extra. Skipping transaction <6bb4c933814d67f9e43ffb6cd6ed0338222df21044e69f93b6560df6ad32fef5>
2020-08-15 16:53:43.556	W Public key wasn't found in the transaction extra. Skipping transaction <5200004300cb8dc93ffaa2bc494cf6a7c2d967c12b60171898e5b1d21d381c71>
2020-08-15 16:53:43.556	W Public key wasn't found in the transaction extra. Skipping transaction <110acaa9ec066cd5c4a5718bd3af52a4907ccf3a2846d33585e8387760012fc2>
2020-08-15 16:53:43.557	W Public key wasn't found in the transaction extra. Skipping transaction <02a7d02e23bcc4e7a40e578a60a8f268f39cd6a0a1a1a7f1dd0029dddd188c2c>
2020-08-15 16:53:43.557	W Public key wasn't found in the transaction extra. Skipping transaction <6d0235fc661366bf571943e841d8f288fc14f80d797bf63d751a84194cf24de0>
2020-08-15 16:53:43.557	W Public key wasn't found in the transaction extra. Skipping transaction <c443e17e40060b64b03d11191cbf5ea8e9d1b91b09932c5fa58e785ba663b492>
2020-08-15 16:53:43.557	W Public key wasn't found in the transaction extra. Skipping transaction <46e0521142f26d32cbcf5773a2cdda554393f85d1aac7d0c16a1519072004a1c>
2020-08-15 16:53:43.557	W Public key wasn't found in the transaction extra. Skipping transaction <5ad3fe81aaa53da4ce8e7eddcb3d74464217f7ead0e6bf2808b85156aaeb248c>
2020-08-15 16:53:43.557	W Public key wasn't found in the transaction extra. Skipping transaction <d526f09bb9f674731d1ca63a55c8b11ecee0425f66ce0895a8b6102393224282>
2020-08-15 16:53:43.558	W Public key wasn't found in the transaction extra. Skipping transaction <8adcf94ad58b9bffe31d17e7ab3b2478046ef23b0c713f174db59795bc51e123>
2020-08-15 16:53:43.558	W Public key wasn't found in the transaction extra. Skipping transaction <77284e0581b4dd4aab3952d2fca221a8150b1a83cef939a68026d01d00450f6b>
2020-08-15 16:53:43.565	W Public key wasn't found in the transaction extra. Skipping transaction <c6ac23a0545117903e0a07c33edc29280fede98c86cabc298fc8ca5575f60941>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <f1144c97a12b3f2ff92c584955f8d69a274370eb69913f013468d06dafc268cc>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <96b2de3adb1be3c0a07a31cfc32069b3901e80fea487e49d7362075e41deb197>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <d7def21ac273d861bfa0d1a1d030fac54d7f99197c2759a1d1bfa0680eb3457b>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <c57da920ea38efc8a73ff978e322638c9f3a1f937f15b7cd4a5fdcfa50ec1437>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <191a805b2a46c95f1652c78cf211b447da588b8023cea7ab972ea0a2ec259a4c>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <710bcad7c537d4d5b3856489535ec5ffd4033810d14590216ff67dc1794192d7>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <bc015db20d1fbd1db8bd2f17648ddfce0791017c2dcff37f2b37b69dc22701b3>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <879efd91af91686098a443b6d9898f6b29011d68c82cff3452d8eb295d75169a>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <06b09758860386919ae864c981e76091c9c7f660aa8bb6a722fc7184dcf1a761>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <528201d5a326f881a655dc86d4a609207d408f653d9e07d7ae7966a3c36d6d19>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <5055836f151e780a2fcd8093f3692866846e2bb3df13d24867018ec402c2f2aa>
2020-08-15 16:53:43.566	W Public key wasn't found in the transaction extra. Skipping transaction <e55dd3db0b264cc10c36b38a0d03afd8a81dbce04751458836d5da714c7fb430>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <b2564734a5fd95e4b924ae1a2f808df7ae9d062d5584b2bc068c2c1efc3c2c4e>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <497ba29ce87e27192f52bb53aab2c2f0d9dffa6c276dc335e4d490ff2d8a22d8>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <2906aae5a07367360dbcbe57156b04b098bda45b0b08001ac1cfa373efe1ce83>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <9399b5e549295218f8e2fd58c8cc1aad0b0d981ce1c1c866ebb7f143976808ae>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <8f1399524c79ae57afce3b2b2b34682b2d52735af0f94951cc4dff1f7cf71b94>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <f8432eb9ebf86fefbc7a0ff4574bebf10c012aae687b07142c0cfd3ece32d358>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <32a2c3c37d2d32c5e9c5686bf3e4acbf0f9f8022ae2a9823cab117db99db707a>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <564a18e9f2fa04774d3d453f848bffc2bcb609168e976fba7d4ddb715740b0b4>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <ebc3bad957ef84b9b22e5f1446585f6e9ffbaa2fd0432b8f241b2a6e4329d6a4>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <55a3d7806cfc7c734f7143ecffecb0f175d4d955b6cea5739e4c3062992f67ce>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <8ff069694dca493794abad4dd55f059696487c40bbe3bda5295b4d1ae093b29a>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <90235649dfdc836b28e319d171b186861004564a86ff1e85027aa5c253c858fa>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <caeaf45142c16266affad0708c87be89e8b23b8e17f7da5589a5fa4957b3f204>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <4144a93e35e23c410bbe58d3117b91b1554ee6aa338746bcd236537117db6037>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <f1ad7e5e92402e44af4e0225aa3b23215f9309cf7dbc31ae548cba6b3ffdd9ed>
2020-08-15 16:53:43.567	W Public key wasn't found in the transaction extra. Skipping transaction <3878660f5c72ef12bdccd77f8069a71420aded166a3bd362984ca7284c075a2d>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <5c1ebb4ad62b948b55fc1b861463d3cffcb3b26d6f6c6d8b4f39c4173a09f655>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <46c8bc3eccc4ff9a7e795fa205bcd3bf0bde9fe62388cf21febfd828020ac913>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <31227785c5cd729575fe6ce808ebb0a30856e64acecd53ca32d9040af9a94a86>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <afa72ae977f4e548f9371fe7697045ca0f1e3ef349a995b5b3ed01183774543e>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <3c8c50de752f5c8b9d562a9799d5e2d8870fabc0a1ba49a5bb807bad216df5c8>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <eb7a24be7216ffce7236b5d82de500aa85ed814d187696cb64681e8e147d4272>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <a228811e63d58489bada3a434da5f82e93cdc6d4d05a16e2239bb421eb32c604>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <7cb884b31357a9bdd3fe85a60a8d9b689f074831aac0390ca2578788bd4b302c>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <4d08c2c013d53c59b34abd5ac4a83ee52d098fb0c868d6a7a23ac878f74888b8>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <5c2967755d2c9d14aa8dff6277564a7f12fd74a580abb71a19a6a47cbbf48db9>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <a57cc68074dbd9bd0c3392bedbe53d2990001a4c18ba37d8a212395427a3b3d2>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <515f0179e13cfa80aff387b470d6a5459ffbffaba7b08dd0e08de0d4e1e1e7bc>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <d5ede4a7d8f35c0463ea359a74916ef379531d56a29181bb9346bd9b45060d5c>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <a768a65ae23b6b5083733636c0edcdd4eedb7216b6cc2ab5cfc5c146139b1a0f>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <c0e563752e8c68ebb5bcff372c539a8823b118e4df7a05ecb98f3823e690fe3a>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <e9f5b7176c820509463db191884e9debdf907d442b0c77f51fa639b0a762dee1>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <f4fc117edb83feacb4af4914f887dc4379fa8b7aafd9fcc194b4eb878ca862ed>
2020-08-15 16:53:43.568	W Public key wasn't found in the transaction extra. Skipping transaction <b425e89eb6af4566d49ca89247a3d72c3cc0b084bcf0ba57ecde7dd8b9d4f669>
2020-08-15 16:53:43.569	W Public key wasn't found in the transaction extra. Skipping transaction <6ad8614bd793246df562b19bcdc6d6d647418c0f4ea0298d390d6b35b2da3548>
2020-08-15 16:53:43.569	W Public key wasn't found in the transaction extra. Skipping transaction <232e9741c8e0f231d0588c463a34d601e27d6929a711fc3606a1a63a5474d8ec>
2020-08-15 16:53:43.569	W Public key wasn't found in the transaction extra. Skipping transaction <5f617debce035c77c34fe2021f93db015d73ba7ad464032272d882586ca5f52e>
2020-08-15 16:53:43.571	W Public key wasn't found in the transaction extra. Skipping transaction <3dfbda7b288e727cbc88bab29f85a4e668d0fc4aeffb972994bd2e91a4ff53ef>
2020-08-15 16:53:43.571	W Public key wasn't found in the transaction extra. Skipping transaction <4b1338b22b7e782b0183e3d9d1d324f639c6c934b627bfdc5ea69af948b48780>
2020-08-15 16:53:43.571	W Public key wasn't found in the transaction extra. Skipping transaction <c57c383771091a1a80d7c6bdf3fbc71af590e40bac7fb60d34cb5a79df962f01>
2020-08-15 16:53:43.571	W Public key wasn't found in the transaction extra. Skipping transaction <cb1363e5f2905983b0a96efca9fb253946d47952a82bc0475658b0438fb9f0c6>
2020-08-15 16:53:43.571	W Public key wasn't found in the transaction extra. Skipping transaction <29bbbb539cf3db82cbb2e2eebcd64fbf750a3d01732c50272c61ef50cccf84e1>
2020-08-15 16:53:43.571	W Public key wasn't found in the transaction extra. Skipping transaction <46719332af25a28f103c53872a43df5d44bdd74e0aea2aee4b1bfbcc7ec975ac>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <5caf35ed5835726720ee66a69fa6b3e0fa6c14f74c675acf00bb462bc223044a>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <3ed14e4854f472b01569973a91a6628f28e7230993364d01b77925b470adedaa>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <eb394a05722c15810f7d3b28f2aae1702a099e8565b3c81073a5a596697c8c7e>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <36dcb181ce11a1a50327c99ddf30b910f518a650ceffb296c5b044f7f0115332>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <dc6b7c4145707a846afcf71a8d0863d3695236e495914db0b19a1b6903b95dd6>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <c10d31e3780a3149036bc7b85bdf3e180f8ffb470dd327594726f201c1e16f58>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <d7045ec4d301b682ad45ffbfeef930889caad49fb37b2a59d46f4ed36c5136a1>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <c65df4a35ab9b40fed65c8bde488f703b886914d1adc95855f4cb0ae246229cb>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <4a425e914fd7a743152b8b05213fbea3f2264e2ed708ae1b0760f76f72b60fe3>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <0f27a02815c04167ff1b6c20a8ada96553cfc87317f402706e4dcefddd8eeb8b>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <6b07a6c71e79d1eb718aed10e8f355eb17fced83cdd81c388f06b1c9fc333adf>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <817f4e4e4eef6751b3305fb43cac37eb38611e1f3363118d58f19db7700354f0>
2020-08-15 16:53:43.572	W Public key wasn't found in the transaction extra. Skipping transaction <a58aa0ab6f0367c7667be1e1d06c89afe3c9ba3f3c4be6455fb64046f668c95e>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <0acefa30619930d52a279df58a95c7f0a783e04b2e1cdc46c71a68403a853e9d>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <437950837302d5530d67172cad78b5f18f9dcaae85b64c985925c4a906c5045b>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <25afdf415f37090e3bc2880fcefda4bb39004e816acd5d67739c18ea8a37186e>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <6a19a22fd0d36c783c9afb450cb1f7375dd80cc1356d2e57e393844b15785a08>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <f2fe4077e6abee5ab91057d41b9bca92829c3f1b2c0590bf5e201392199ee77d>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <3b817026b876e0dbf1a3b18c0ed59324d189fb8fd82abdd2c30f6f3a9e2378ca>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <a59edf2ff6eaf96c806311311055d9bba0eab986bcc42a0b6c5819046c756026>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <2cef7ca24ae86e0faa9e4ec94b960d67e5a6f7479e492303c7b29d1f4ad9ecb5>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <c34c17ec126eb484cb8d70e2c953632555bf7a6caada0df2a81af2b78581a11c>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <773f7d3179f1877bc8a9308b1e8669441ed2fa56003f17a91ad90ac7d8e5129a>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <9e0a1dedd4ea35f1acd85ea178e6a01cdf6c5ce9c6997d98b55bb88328c1b2f1>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <024222da30118033f2512940602f7a13a1ea201ca5b1137a5b68bb1c8875f528>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <3a41817f44e64b37c6eec65b7b722d295183abdd790fe2ec150fb71ce727d220>
2020-08-15 16:53:43.573	W Public key wasn't found in the transaction extra. Skipping transaction <82e847a25811fd6ed09258b84dc9e098bc1ab8cbe6d7572de2328bda25acdbbb>
2020-08-15 16:53:43.574	W Public key wasn't found in the transaction extra. Skipping transaction <75a9d1dd7d944973e6a298430d1c532397245ced62b43682a1f05febad1928c1>
2020-08-15 16:53:43.574	W Public key wasn't found in the transaction extra. Skipping transaction <3bd4d7d02e0a997e7e970df39dad3f4182de5c6bacc8f6b9a95384fc61ac8341>
2020-08-15 16:53:43.574	W Public key wasn't found in the transaction extra. Skipping transaction <ec383a1b5bcd876364c72147aa2da45a6d8a1efba74805f3e621d9a5f448b62a>
2020-08-15 16:53:43.574	W Public key wasn't found in the transaction extra. Skipping transaction <258dfc05b24bab767be9a330310c83c8964d476ce909b900a83c081186dda9f8>
2020-08-15 16:53:43.574	W Public key wasn't found in the transaction extra. Skipping transaction <e8ad1dd7f9cf56153d0a754c2d132c9ff4401ad7cce86ac6ac1f5aeda6f69f7c>
2020-08-15 16:53:53.997	W Transaction extra has unsupported format: <d039f391f78faa393fd26c3a6a95a88008d8b61493693d770dc2570c45751506>
2020-08-15 16:53:53.998	W Transaction extra has unsupported format: <77df6e0a621f04ec84dfc27ae72a36114148c4755eb72afd826657ae4fafeab6>
2020-08-15 16:53:53.998	W Transaction extra has unsupported format: <21052db9dc6e857622d0a301ee79286414b526e9153f558c28ce18235053c55a>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <b88b3d4aa46b0532275869cfa8ee850b4ee7ee991261255a35aa62adafe78908>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <6f0cf47c595b353c6dc8a9368e83243dec08b06896feadd35d5e35f17186b645>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <269ef66cf4ce52744d45c173505113d103b668cb4269ffabee31444d4c3086b4>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <a99c4c7d32567d63114d667ee9db734429eeef63d0bfe542c7e6622b02005615>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <48b0a177883b034a866d2e2a77f15d5e502522e472620d5651fd421c6ab9d509>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <275180f67b76500973137a1b2cffc7807d5f31adb56638b75932cf99c268e67d>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <f3342aa61979ad9ab275ada3168642852beb1d498a4ba8ffbe87fc36926c0507>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <7a4cec54164efad5105ee010bf9cb0cbd2115c6a39f9e03c7deee3f457c8bee7>
2020-08-15 16:53:53.999	W Transaction extra has unsupported format: <fac03fd556cd0c6a95976b499af9f148febb147c9e9ae34ebe9779cc0e6cbf8d>
2020-08-15 16:53:54.012	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.016	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.017	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.018	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.019	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.020	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.020	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.020	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.024	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.024	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.053	E wrong number of additional derivations
2020-08-15 16:53:54.054	E wrong number of additional derivations
2020-08-15 16:53:54.054	E wrong number of additional derivations
2020-08-15 16:53:54.054	E wrong number of additional derivations
2020-08-15 16:53:54.055	E wrong number of additional derivations
2020-08-15 16:53:54.055	E wrong number of additional derivations
2020-08-15 16:53:54.056	E wrong number of additional derivations
2020-08-15 16:53:54.056	E wrong number of additional derivations
2020-08-15 16:53:54.057	E wrong number of additional derivations
2020-08-15 16:53:54.057	E wrong number of additional derivations
2020-08-15 16:53:54.057	E wrong number of additional derivations
2020-08-15 16:53:54.057	E wrong number of additional derivations
2020-08-15 16:53:54.059	E wrong number of additional derivations
2020-08-15 16:53:54.059	E wrong number of additional derivations
2020-08-15 16:53:54.060	E wrong number of additional derivations
2020-08-15 16:53:54.094	W Transaction extra has unsupported format: <7f2bf2c9d585e3b000ef5d05aa9184d1082edf5942d7bb383aa55848de2d661d>
2020-08-15 16:53:54.095	W Transaction extra has unsupported format: <2624361b6b0b4444dc577fc148aa19708bfc1a5084dd843dd237dc76cbd7f696>
2020-08-15 16:53:54.095	W Transaction extra has unsupported format: <051bc824aeca27f242a868dcc8084566edfe06f8348410d26ae7568c39c30984>
2020-08-15 16:53:54.112	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.112	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.155	E wrong number of additional derivations
2020-08-15 16:53:54.155	E wrong number of additional derivations
2020-08-15 16:53:54.155	E wrong number of additional derivations
2020-08-15 16:53:54.156	E wrong number of additional derivations
2020-08-15 16:53:54.156	E wrong number of additional derivations
2020-08-15 16:53:54.156	E wrong number of additional derivations
2020-08-15 16:53:54.156	E wrong number of additional derivations
2020-08-15 16:53:54.156	E wrong number of additional derivations
2020-08-15 16:53:54.157	E wrong number of additional derivations
2020-08-15 16:53:54.157	E wrong number of additional derivations
2020-08-15 16:53:54.181	W Transaction extra has unsupported format: <775adc5bee68fc139e3dce4b8adb330495a80608e23fd6227608195cf51934b4>
2020-08-15 16:53:54.223	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.223	W Failed to generate key derivation from tx pubkey, skipping
2020-08-15 16:53:54.242	E wrong number of additional derivations
2020-08-15 16:53:54.242	E wrong number of additional derivations
2020-08-15 16:53:56.580	W Transaction extra has unsupported format: <61c625f82c458f862cbd5e076443da7e9e371efa519f54fb3eab27ad99f3a86f>
2020-08-15 16:53:56.583	W Transaction extra has unsupported format: <93278cde512ceeb6d2a8f102d3014c7253d9208de2c63362e37d4a92ee520a7e>
2020-08-15 16:53:56.645	W Transaction extra has unsupported format: <61c625f82c458f862cbd5e076443da7e9e371efa519f54fb3eab27ad99f3a86f>
2020-08-15 16:53:56.645	W Public key wasn't found in the transaction extra. Skipping transaction <61c625f82c458f862cbd5e076443da7e9e371efa519f54fb3eab27ad99f3a86f>
2020-08-15 16:53:56.656	W Public key wasn't found in the transaction extra. Skipping transaction <93278cde512ceeb6d2a8f102d3014c7253d9208de2c63362e37d4a92ee520a7e>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <a0b390005ef201eae9faafc73f2c1b7c25b5aa7e7a131c7ae09d8b7cb71b60a6>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <e49d9f75c26ddbd444416a04d6eb625048aee6ee4a47a7b4c3eda7d07c2d1aed>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <a0ea1e1d85ed04e32a789d166823136b06188b314036652d55a0bfd4a63f4616>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <e26fa6796cf4164d6192a60b70bb4db557539511449c25a40cd364b457c4ea82>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <f450f5437abb6dc488c606f5f98f052f9ce007209aacfbdc944ed21ffbadda54>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <8701085fcf40028a7bcb7059b6b2425d9aae07d1d692c0c86068df03e1ceb2bd>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <904d7e2902ad6bb884d80301b16db2d524ffeec91024f4abeb8191746d3f503c>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <53a82b3ac61ba4ab019b7fdd9b89ce09cd8f2b6230994512b60e334b9b496a5d>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <1ba4f7675e586cea342db4075968ff2292364749b7fec91a0bc05a6389a24b3e>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <40a7ce639de552dd2c36915be46b447814f1fbc0462f1e9308d0f97356625798>
2020-08-15 16:54:03.909	W Transaction extra has unsupported format: <5bd4b7c5ec28d9b3dbbb0ae0b76a6696a8f043ef6dd67a3ad928c911c41e1845>
2020-08-15 16:54:03.910	W Transaction extra has unsupported format: <2a280afe01c3189a02197e9d2cb4e92807623a41da12d5c562603a9e1a7aca44>
2020-08-15 16:54:03.910	W Transaction extra has unsupported format: <345de8d15d4412df888e8bd84f85e0df07a871d83f28454233e4fd5b8e21480c>
2020-08-15 16:54:03.910	W Transaction extra has unsupported format: <9c927b75ffa999f4076e6d7c8e8621959f6635ea068b825d72f8ae3b168039e2>
2020-08-15 16:54:03.910	W Transaction extra has unsupported format: <48e7c7da511d5b813b0f8da65f590731c428dd3cd9c18e41796e04feae49c2c5>
2020-08-15 16:54:03.910	W Transaction extra has unsupported format: <888428e3ab679ab60e636e127a0d2b34a7c0d5d3d7fedd70b997dc0bc6d9e3cd>
2020-08-15 16:54:03.910	W Transaction extra has unsupported format: <1a994caa2d638facc4346df6a9fedb11a453965691e4df7bb743c7b38f8b78f2>
2020-08-15 16:54:03.969	W Transaction extra has unsupported format: <a0b390005ef201eae9faafc73f2c1b7c25b5aa7e7a131c7ae09d8b7cb71b60a6>
2020-08-15 16:54:03.970	W Public key wasn't found in the transaction extra. Skipping transaction <a0b390005ef201eae9faafc73f2c1b7c25b5aa7e7a131c7ae09d8b7cb71b60a6>
2020-08-15 16:54:03.970	W Transaction extra has unsupported format: <904d7e2902ad6bb884d80301b16db2d524ffeec91024f4abeb8191746d3f503c>
2020-08-15 16:54:03.970	W Public key wasn't found in the transaction extra. Skipping transaction <904d7e2902ad6bb884d80301b16db2d524ffeec91024f4abeb8191746d3f503c>
2020-08-15 16:54:03.970	W Transaction extra has unsupported format: <a0ea1e1d85ed04e32a789d166823136b06188b314036652d55a0bfd4a63f4616>
2020-08-15 16:54:03.970	W Public key wasn't found in the transaction extra. Skipping transaction <a0ea1e1d85ed04e32a789d166823136b06188b314036652d55a0bfd4a63f4616>
2020-08-15 16:54:03.970	W Transaction extra has unsupported format: <1a994caa2d638facc4346df6a9fedb11a453965691e4df7bb743c7b38f8b78f2>
2020-08-15 16:54:03.970	W Public key wasn't found in the transaction extra. Skipping transaction <1a994caa2d638facc4346df6a9fedb11a453965691e4df7bb743c7b38f8b78f2>
2020-08-15 16:54:03.970	W Transaction extra has unsupported format: <888428e3ab679ab60e636e127a0d2b34a7c0d5d3d7fedd70b997dc0bc6d9e3cd>
2020-08-15 16:54:03.970	W Public key wasn't found in the transaction extra. Skipping transaction <888428e3ab679ab60e636e127a0d2b34a7c0d5d3d7fedd70b997dc0bc6d9e3cd>
2020-08-15 16:54:03.971	W Transaction extra has unsupported format: <8701085fcf40028a7bcb7059b6b2425d9aae07d1d692c0c86068df03e1ceb2bd>
2020-08-15 16:54:03.971	W Public key wasn't found in the transaction extra. Skipping transaction <8701085fcf40028a7bcb7059b6b2425d9aae07d1d692c0c86068df03e1ceb2bd>
2020-08-15 16:54:03.971	W Transaction extra has unsupported format: <e49d9f75c26ddbd444416a04d6eb625048aee6ee4a47a7b4c3eda7d07c2d1aed>
2020-08-15 16:54:03.971	W Public key wasn't found in the transaction extra. Skipping transaction <e49d9f75c26ddbd444416a04d6eb625048aee6ee4a47a7b4c3eda7d07c2d1aed>
2020-08-15 16:54:03.971	W Transaction extra has unsupported format: <53a82b3ac61ba4ab019b7fdd9b89ce09cd8f2b6230994512b60e334b9b496a5d>
2020-08-15 16:54:03.971	W Public key wasn't found in the transaction extra. Skipping transaction <53a82b3ac61ba4ab019b7fdd9b89ce09cd8f2b6230994512b60e334b9b496a5d>
2020-08-15 16:54:03.971	W Transaction extra has unsupported format: <48e7c7da511d5b813b0f8da65f590731c428dd3cd9c18e41796e04feae49c2c5>
2020-08-15 16:54:03.971	W Public key wasn't found in the transaction extra. Skipping transaction <48e7c7da511d5b813b0f8da65f590731c428dd3cd9c18e41796e04feae49c2c5>
2020-08-15 16:54:03.971	W Transaction extra has unsupported format: <e26fa6796cf4164d6192a60b70bb4db557539511449c25a40cd364b457c4ea82>
2020-08-15 16:54:03.971	W Public key wasn't found in the transaction extra. Skipping transaction <e26fa6796cf4164d6192a60b70bb4db557539511449c25a40cd364b457c4ea82>
2020-08-15 16:54:03.971	W Transaction extra has unsupported format: <f450f5437abb6dc488c606f5f98f052f9ce007209aacfbdc944ed21ffbadda54>
2020-08-15 16:54:03.971	W Public key wasn't found in the transaction extra. Skipping transaction <f450f5437abb6dc488c606f5f98f052f9ce007209aacfbdc944ed21ffbadda54>
2020-08-15 16:54:03.972	W Transaction extra has unsupported format: <2a280afe01c3189a02197e9d2cb4e92807623a41da12d5c562603a9e1a7aca44>
2020-08-15 16:54:03.972	W Public key wasn't found in the transaction extra. Skipping transaction <2a280afe01c3189a02197e9d2cb4e92807623a41da12d5c562603a9e1a7aca44>
2020-08-15 16:54:03.972	W Transaction extra has unsupported format: <345de8d15d4412df888e8bd84f85e0df07a871d83f28454233e4fd5b8e21480c>
2020-08-15 16:54:03.972	W Public key wasn't found in the transaction extra. Skipping transaction <345de8d15d4412df888e8bd84f85e0df07a871d83f28454233e4fd5b8e21480c>
2020-08-15 16:54:03.972	W Transaction extra has unsupported format: <9c927b75ffa999f4076e6d7c8e8621959f6635ea068b825d72f8ae3b168039e2>
2020-08-15 16:54:03.972	W Public key wasn't found in the transaction extra. Skipping transaction <9c927b75ffa999f4076e6d7c8e8621959f6635ea068b825d72f8ae3b168039e2>
2020-08-15 16:54:03.973	W Transaction extra has unsupported format: <1ba4f7675e586cea342db4075968ff2292364749b7fec91a0bc05a6389a24b3e>
2020-08-15 16:54:03.973	W Public key wasn't found in the transaction extra. Skipping transaction <1ba4f7675e586cea342db4075968ff2292364749b7fec91a0bc05a6389a24b3e>
2020-08-15 16:54:03.973	W Transaction extra has unsupported format: <40a7ce639de552dd2c36915be46b447814f1fbc0462f1e9308d0f97356625798>
2020-08-15 16:54:03.973	W Public key wasn't found in the transaction extra. Skipping transaction <40a7ce639de552dd2c36915be46b447814f1fbc0462f1e9308d0f97356625798>
2020-08-15 16:54:03.973	W Transaction extra has unsupported format: <5bd4b7c5ec28d9b3dbbb0ae0b76a6696a8f043ef6dd67a3ad928c911c41e1845>
2020-08-15 16:54:03.973	W Public key wasn't found in the transaction extra. Skipping transaction <5bd4b7c5ec28d9b3dbbb0ae0b76a6696a8f043ef6dd67a3ad928c911c41e1845>
2020-08-15 16:54:27.277	W Transaction extra has unsupported format: <beed69e09d68440a844aa80b69107e4eb771b72ba4f861cf2facd602d62c8fe8>
2020-08-15 16:54:27.281	W Transaction extra has unsupported format: <60ea42c111c02f770cb5822a14407f2311aec04c8e8aa174df07dc724598dffd>
2020-08-15 16:54:27.281	W Transaction extra has unsupported format: <9b7720b8acabf8d1b8167d7944961866ac4376e984c31d626137c7cd15f3e2c6>
2020-08-15 16:54:27.281	W Transaction extra has unsupported format: <af9f0a9c83b1718ee0d48ddcc94ff9ad2897252d3334f74fc9b079dfbb215624>
2020-08-15 16:54:27.281	W Transaction extra has unsupported format: <b1a9e89d1583bb3fc0f99dbaa7c9f6b14ea6071cd33313db49655a33d1bedba8>
2020-08-15 16:54:27.367	W Transaction extra has unsupported format: <389d8c49b87384c8af9ab5df202a4e5859ef3eaf193c1f6e2d5066d27a925bae>
2020-08-15 16:54:27.367	W Transaction extra has unsupported format: <2a849815771db195125a236d6a3e60737ddcd18ab57de94e0b6234774dcfbbb9>
2020-08-15 16:54:27.367	W Transaction extra has unsupported format: <d07392c7c1c5bbe584f4e01353322f1f742f4bf321c91124fb605520ccdf1174>
2020-08-15 16:54:27.368	W Transaction extra has unsupported format: <d07286e94fae4e50ba6498cf95052245cec068fb3d23974e05ac2fd99e854cb3>
2020-08-15 16:54:28.049	E wrong number of additional derivations
```

## moneromooo-monero | 2020-08-15T18:43:10+00:00
I checked a couple txids in there, not found. Is this a monero fork ? Or testnet ?

## moneromooo-monero | 2020-08-15T18:43:48+00:00
Ah yes, testnet.

## moneromooo-monero | 2020-08-15T18:45:47+00:00
I checked a couple, and they do seem wonky. So all fine. That's a red herring AFAICT.

## OxMarco | 2020-08-16T13:29:46+00:00
Yes it's testnet. Ok I'll close the issue now, thanks for the info

## moneromooo-monero | 2020-08-16T16:52:41+00:00
Well, the daemon should not become unresponsive. Those errors are unrelated, but this is still a bug.

## moneromooo-monero | 2020-08-16T16:52:57+00:00
(so please get the data I asked for in my first comment if you can)

## OxMarco | 2020-08-22T08:32:20+00:00
Tested now, after the error `wrong number of additional derivations` the RPC executable became irresponsive for about 3 seconds giving timeout errors when receiving RPC commands. I'll try with gdb now and let you know.

## OxMarco | 2020-10-20T21:12:50+00:00
Getting back to this error `E wrong number of additional derivations`, it was triggered even with `finalize_multisig` on a _normal_ (non view-only) wallet. After this error the daemon becomes unresponsive to any JSON-RPC command.

## moneromooo-monero | 2020-10-29T15:52:01+00:00
That sounds unlikely, so give actual repro steps.

## OxMarco | 2020-10-31T22:10:26+00:00
Steps are as follows:
1. create a view-only wallet using curl interfacing with _monero-wallet-rpc_ executable built from source on Ubuntu 18.04 LTS
2. wallet is correctly created and appears in the wallet directory
3. error `E wrong number of additional derivations` and several warnings `W Transaction extra has unsupported format:` appear in the log
4. all subsequent RPC curl calls (say `open_wallet`, `get_balance` or `validate_address`) fail  with
`Unable to connect to http://127.0.0.1:18083/json_rpc Error: Operation timed out after 8000 milliseconds with 0 bytes received`
The only way to solve the issue is to stop and rerun _monero-wallet-rpc_

## moneromooo-monero | 2020-12-11T17:06:26+00:00
Are you sure it's finished scanning ?

## moneromooo-monero | 2020-12-11T17:07:25+00:00
I mean, open_wallet, get_balance or validate_address are wallet RPC. From your comments before the last one, you said daemon, which I had interpreted as the node, which was apparently incorrect. It now looks as if the wallet is just still busy syncing.

## OxMarco | 2020-12-12T00:45:19+00:00
Your explanation sounds reasonable, monero-wallet-rpc takes about 1 minute to sync. Is there a way to enqueue other RPC calls or detach the synchronisation to a separate thread?

## moneromooo-monero | 2020-12-23T01:04:04+00:00
If you use open_wallet etc, you should be able to call auto_refresh on the wallet first, and set enable to false. Then you can refresh manually when convenient for you.

# Action History
- Created by: OxMarco | 2020-08-14T17:26:32+00:00
