---
title: CLI v0.17.2.3-release monerod errors
source_url: https://github.com/monero-project/monero/issues/7918
author: tikwanleap
assignees: []
labels: []
created_at: '2021-09-02T17:29:15+00:00'
updated_at: '2021-09-02T21:27:06+00:00'
type: issue
status: closed
closed_at: '2021-09-02T21:27:06+00:00'
---

# Original Description
Getting a ton of "failed to find transaction input in key images." errors when I run monerod.exe (CLI v0.17.2.3-release).

I looked up a few of the transaction id's in a block explorer and it looks like the key images actually does exist. So not sure why I'm seeing these errors.

https://localmonero.co/blocks/search/d4f3cce3aa39d0f8df3d54ab365b8bda9d9748497f1de07df5e1e932b00e5803

```
C:\monero\monero-x86_64-w64-mingw32-v0.17.2.3>monerod.exe --db-sync-mode=safe --data-dir D:\ProgramData\bitmonero
2021-09-02 17:17:04.874 I Monero 'Oxygen Orion' (v0.17.2.3-release)
2021-09-02 17:17:04.874 I Initializing cryptonote protocol...
2021-09-02 17:17:04.874 I Cryptonote protocol initialized OK
2021-09-02 17:17:04.874 I Initializing core...
2021-09-02 17:17:04.874 I Loading blockchain from folder D:\ProgramData\bitmonero\lmdb ...
2021-09-02 17:17:52.434 E failed to find transaction input in key images. img=<cc6ecbdfdf65b1bcaed89b100f7be9abea5f695222d9e19159bc57fe3d79f66d>
2021-09-02 17:17:52.435 E transaction id = <d4f3cce3aa39d0f8df3d54ab365b8bda9d9748497f1de07df5e1e932b00e5803>
2021-09-02 17:17:52.522 E failed to find transaction input in key images. img=<f408a9e708d060bfac0fd666f75b1f50abee552afb90a78c71e33fed5058f90b>
2021-09-02 17:17:52.524 E transaction id = <f00d083c3ef3b6ed2e8cb492eca192c811c532744b1eca6e670312810b0df00b>
2021-09-02 17:17:52.652 E failed to find transaction input in key images. img=<1cf71b70e51921a3477901a5e91b67350bd1994c7fa1973760c1e0a139cdd334>
2021-09-02 17:17:52.653 E transaction id = <081ef18fce2ac4be0b996ff6901d5ec800be7e4d6f7a63b4be1dbf657b4f000e>
2021-09-02 17:17:52.768 E failed to find transaction input in key images. img=<543402fd2136ca4a9f33f730d3e5bf2707f7f49e2aa526cdb75d8a1699a3543b>
2021-09-02 17:17:52.770 E transaction id = <ad8fcb764db5bd70ac8be195b9f34a1b07b08c785d11f6f3afff6ebd52aede0f>
2021-09-02 17:17:52.876 E failed to find transaction input in key images. img=<c3f77f4f21865af3ad8ddd3da7b287024314dee735f474f5e1500a0cf42983a3>
2021-09-02 17:17:52.878 E transaction id = <48d5e1db41014985c9d0f98eb4b5ece684b0b9857bca38163cc746b33ac7fc11>
2021-09-02 17:17:52.993 E failed to find transaction input in key images. img=<651be52dd53a27fc27e2afdaf278e9ca90e170865fe2dc556d44119c882839ab>
2021-09-02 17:17:52.995 E transaction id = <69b40051b077b5aa9dd81dc1697212e84b8da329e5bae0a92b9934b34141eb12>
2021-09-02 17:17:53.101 E failed to find transaction input in key images. img=<6aa13507c7bfe4ec8c37181dd01a146eb75193777d86cc8f11f5371c0b7da11a>
2021-09-02 17:17:53.103 E transaction id = <15530841068bbce67a7b083176b3d7591be0139d3baae199ddff3fa021722214>
2021-09-02 17:17:53.193 E failed to find transaction input in key images. img=<f5c14692acc3695a1f1851878a0a2bfb6463492b0b13c673324c48789a04778d>
2021-09-02 17:17:53.195 E transaction id = <ad1671b41c85145135ed7207b6da894c409c037c3d95b13dbfd9d205ea97bb14>
2021-09-02 17:17:53.287 E failed to find transaction input in key images. img=<ed81fc228f1e693cd7ffd361ba7f71eda807278387b45b782d1c7677bd82e93c>
2021-09-02 17:17:53.289 E transaction id = <c1ae7638cfe9665751db5d3f77beb7eb392d3ed42a65a9375fc617027725f314>
2021-09-02 17:17:53.385 E failed to find transaction input in key images. img=<c62b78103e5e80063ccc8407ec02a3db6f432500cff575da8618a6a1c263954a>
2021-09-02 17:17:53.386 E transaction id = <9b56f733a43017f633fdb08bcdf97ed8b9717d105ee6254dec8f7113f03ddf1c>
2021-09-02 17:17:53.484 E failed to find transaction input in key images. img=<8349614602315f674e35a1d82202f3135b5fa453f402bc9cac350af5e9c093ca>
2021-09-02 17:17:53.486 E transaction id = <91a71077d4810ed9a3464be6af6b50c630fd319b38284cf0a0d657d8aeb5061e>
2021-09-02 17:17:53.593 E failed to find transaction input in key images. img=<1dfc488fe772ad677460d56f05f44832642c4f9241fc90cf4be06d2725df880f>
2021-09-02 17:17:53.595 E transaction id = <b3f8c8698da0161b710473845123c0ecf2efbf0242ce8ce22480b8563973271f>
2021-09-02 17:17:53.667 E failed to find transaction input in key images. img=<9527d13aac67db583f975349a0305078acf3e74d779d87dc62f58747bb68e884>
2021-09-02 17:17:53.668 E transaction id = <343033daf2c00d7dab569ccaf3531790342c78fff401a3f543f9da0b611b1324>
2021-09-02 17:17:53.750 E failed to find transaction input in key images. img=<98d0179d5ed5585d0db7d1e59d58966c44c3bca219d254f8a108f94faa6bd713>
2021-09-02 17:17:53.752 E transaction id = <63471805934c6af82e1827634a83f8e359f002dbfcbbda17e5018ef515014a31>
2021-09-02 17:17:53.842 E failed to find transaction input in key images. img=<1d2bd43b947a8d68222bbf882a63b712b2408b243df80295d3584907ecb97c27>
2021-09-02 17:17:53.843 E transaction id = <833532b25a8dd6ae26800c921fe777787f362cb8e26000143bbeac97af6f5131>
2021-09-02 17:17:53.942 E failed to find transaction input in key images. img=<969d9c67cc0cf246b3e6ee6e297d7acf270ce2c95712aabfa3349f06721b6f8a>
2021-09-02 17:17:53.944 E transaction id = <c73fee48f2859389015573c50c07438d2e0d7c74319b2a972002ec271a4a9336>
2021-09-02 17:17:54.033 E failed to find transaction input in key images. img=<e31c9d590aaa37444ceb8377f254267d3c7d231ad2741c7ebb7429ac80a8bebe>
2021-09-02 17:17:54.035 E transaction id = <f677d8609cc49b05aedfca3d1ecedb3ad88ebda5ea9efabdc029fae5e429ef36>
2021-09-02 17:17:54.117 E failed to find transaction input in key images. img=<7da4af0b6d6422996226527a48ffb1ca4f30d1e4c87d3c334d4f4132b5f41c2b>
2021-09-02 17:17:54.119 E transaction id = <8898fc942ce2dcd24a55e21f41435c01577aaab4aec7b26a81400ded5f889c38>
2021-09-02 17:17:54.208 E failed to find transaction input in key images. img=<aafd5d3a03a3ad90a96d060f1e03b2a9e96ad42e9bfd1936f71f6910b516341b>
2021-09-02 17:17:54.210 E transaction id = <c192fcd93182644ad9533829853ca19f6687a02b003c6807dce8eebb99081d3a>
2021-09-02 17:17:54.292 E failed to find transaction input in key images. img=<b2c962477cdbf33ee02f8b83e98600353ee02b4c10aa2968b27b36196fbc9fca>
2021-09-02 17:17:54.293 E transaction id = <f8b889c9d807b6ff8075ab9e73671c800750bbf72f76a5b5acde6e7914087a3b>
2021-09-02 17:17:54.400 E failed to find transaction input in key images. img=<4bb182501f7ae97814186170a7a3dd8ffa0d061f7e0a6ecccab623c0fc53397e>
2021-09-02 17:17:54.401 E transaction id = <a1c1859381329206e8bd1e0908cfcfb5aaa0d6ef8c621334e62fcbe57fe5ce41>
2021-09-02 17:17:54.484 E failed to find transaction input in key images. img=<5764b5029cd92615ef8d5005024f21c3dc4a9dac355cf81ed937504ccf2c0de0>
2021-09-02 17:17:54.485 E transaction id = <3038d5d402aca4590ee4fc996370618116f7ae99efd5adbf9e74f3e9aaf43445>
2021-09-02 17:17:54.575 E failed to find transaction input in key images. img=<c5fddc286707d45b56f44f0f4b6419e02d7b70394ec55547821b0d6e454755da>
2021-09-02 17:17:54.577 E transaction id = <172fb2b4e3e0efd4ae122322b130e445971e402b4bd0e7c62a990760a2756846>
2021-09-02 17:17:54.667 E failed to find transaction input in key images. img=<7f5d2f054fac8a3c1b8302dc87f94d4f91115133f20e5c48c9280ecced34e610>
2021-09-02 17:17:54.669 E transaction id = <dcd1626876cc62ee03c265e9288442aa2c0980e70375d90e7f4232c28ea68e47>
2021-09-02 17:17:54.742 E failed to find transaction input in key images. img=<cd940f7d9f93c11b3955a5487b64bbe000ca601d8e5d19732a99c3366c568854>
2021-09-02 17:17:54.743 E transaction id = <05119d3a949d85c7836d94ebbaa8a9b382075ec07340d760ec511be991f4ba48>
2021-09-02 17:17:54.842 E failed to find transaction input in key images. img=<bf08308e6624d26ab268cea775aef9e7c2ec5232341dd55393ac1ffa2b82761f>
2021-09-02 17:17:54.843 E transaction id = <eaaa733cfc5dc4f794e38af8af81880f6e2ea691503e0bd7c41a15958c38a349>
2021-09-02 17:17:54.941 E failed to find transaction input in key images. img=<e37f2d9addadabc103f8643e7a59be798bbfaf5d57d71c296d00ff794288c70b>
2021-09-02 17:17:54.943 E transaction id = <b110130ce3404d221f7d91fab497216bf5b5dab9ad0cbb6ac21c5da55740c04a>
2021-09-02 17:17:55.034 E failed to find transaction input in key images. img=<e04030c43ae2b490a2af3e9e1c11da27051643beb4581b9f63ca18d19fe41007>
2021-09-02 17:17:55.036 E transaction id = <e0128de4e030d5dc02508ced62648dfc36a3e35be2b097809aab199f32c3ee4c>
2021-09-02 17:17:55.117 E failed to find transaction input in key images. img=<55bb962fca901f63fc46fdcc4b171cb025134fdeb2a937b94e6ba2717e8abab1>
2021-09-02 17:17:55.118 E transaction id = <b157fecdfb364dc47f51299a70d776ffd1ab961bf587542029b06f3cfb4b944f>
2021-09-02 17:17:55.190 E failed to find transaction input in key images. img=<e51692a4e4cb9f5d5424ebd5e9d49d60bf34d60638c6b57afd5d729dee03b61f>
2021-09-02 17:17:55.192 E transaction id = <430562c5709402f19160a489226055f1adf2a9ebd5cc9676aeeef77f1504ad51>
2021-09-02 17:17:55.275 E failed to find transaction input in key images. img=<8f6c0331bb00dac8e42f3c702a518d2ec28983b1b92b708651c1415d947ca4bd>
2021-09-02 17:17:55.277 E transaction id = <4955c09aa149579ab91f17769f3b5b3422bad61d08166a60ac7171a2ffb6f653>
2021-09-02 17:17:55.358 E failed to find transaction input in key images. img=<cee5eea68689db151804337474816ea3f9db52ea44ac1205c8272dc01a1c1e34>
2021-09-02 17:17:55.360 E transaction id = <1be636f158cb2637a30b07e4202d43f17db49ab53295aea07f8974912e9d0c55>
2021-09-02 17:17:55.433 E failed to find transaction input in key images. img=<8505af12def7599352577eac92f1a035d26cc3478f81dd5f9488323f02007e8e>
2021-09-02 17:17:55.435 E transaction id = <5390c861e70d53b9fc1a31a2b7695e75bfb1f63c33c2bd0eae80543e198b7d55>
2021-09-02 17:17:55.525 E failed to find transaction input in key images. img=<59788075a08940b3c0498985722af17e98ec135c8562f5bb6da21560b9034e40>
2021-09-02 17:17:55.526 E transaction id = <3546ce37dab2b3e4a6075f3413510d0c8093d0b34669385ce99f45cebc22a75b>
2021-09-02 17:17:55.617 E failed to find transaction input in key images. img=<181f5f22af10b30c022ca82b0149d3ab5281db455b7f9773a1c50d3594e10120>
2021-09-02 17:17:55.618 E transaction id = <9e748ac7492ce5e3058d33279ae49c7a658a82ea3230347139c64da64456965d>
2021-09-02 17:17:55.717 E failed to find transaction input in key images. img=<941208eeb5ac61cddf233132680184e07c3a97982749e3d52135ff935bb396ee>
2021-09-02 17:17:55.718 E transaction id = <ef9182be7769666f1980bbc77e56887d150b2f1378a5581f5b2236e974fd8861>
2021-09-02 17:17:55.800 E failed to find transaction input in key images. img=<c0be051ec71d623cd0218528a2326adc6ef033c370c07905af677f13151fcc2f>
2021-09-02 17:17:55.801 E transaction id = <e0cced238bfdf9bdc728e4bd58ce2aef756d755a14fd8c37b73f74af5b962b66>
2021-09-02 17:17:55.891 E failed to find transaction input in key images. img=<599ca30547a72556602c7bfa6d32aa545b17226fb098f80d4e8654b020ac6256>
2021-09-02 17:17:55.895 E transaction id = <6f314403d62f0df7abfb90914c74ba49a06fc60b53c92056843377973001ce6e>
2021-09-02 17:17:55.975 E failed to find transaction input in key images. img=<8f331f53bed7e1ca1ccb6cec016c6c63f8929384e0807ef191f2fb985d9fc40c>
2021-09-02 17:17:55.977 E transaction id = <f09b469d53c367d89926b5893d892a04ce849b96637e4646e0ad98f3b048c776>
2021-09-02 17:17:56.075 E failed to find transaction input in key images. img=<93a965568f80debded7301074ad11039870b1aa2d74faa26f2567c4ad992043e>
2021-09-02 17:17:56.077 E transaction id = <c3f5c052afa069af05aecfb2478f24eefdf9ea2458dae10b6e720757c2b5ab78>
2021-09-02 17:17:56.159 E failed to find transaction input in key images. img=<cba232b7472b0832cfc3991e950f7773e92584dd3de0d6dc04a31906adb95d9d>
2021-09-02 17:17:56.160 E transaction id = <43a9dd2c6b274e8449e1abc95c5545e4e396515e256a1ee9c216385d4a20617b>
2021-09-02 17:17:56.242 E failed to find transaction input in key images. img=<bc5518b67c10c1678be8c411a17ea2d77d2bfd3f1e871afc3ec21cee7b32fd7c>
2021-09-02 17:17:56.245 E transaction id = <4a08ab09b8701380d7193d88d818ed51a30ef5e7dd6b8f77d13c15de8f94367f>
2021-09-02 17:17:56.325 E failed to find transaction input in key images. img=<5ed2eac0b0b71f55497757b186a88e4dea2d34212a8c3130eeb704ed28f046ec>
2021-09-02 17:17:56.327 E transaction id = <37f37eb0be048f9965d9fdd2014b369a3d306ff326faa15a57bc7a39283f5380>
2021-09-02 17:17:56.408 E failed to find transaction input in key images. img=<2ea136b6ada480ee164ff532e8720de8789804a90130e84a67d82853a74a51e6>
2021-09-02 17:17:56.411 E transaction id = <753f770a97c260e404e85c8107e12dac70ca3f2b198f0178006a807f201c1f88>
2021-09-02 17:17:56.483 E failed to find transaction input in key images. img=<c66614458ec2a81f71db5fde4fdcb93eb47932cfed9e72d81e57a0df50ccfb5c>
2021-09-02 17:17:56.486 E transaction id = <35c934ee1a5bef4ab5e5985f4c49cb4d62f54d6418bee654eb106b1bcf092088>
2021-09-02 17:17:56.600 E failed to find transaction input in key images. img=<ebf08b3b41a319a35da57658b9ba5759487698303c1ef0a1eb5b3493a93b79c5>
2021-09-02 17:17:56.602 E transaction id = <bea0a4a6ef34d8b2cb93e837d0094a9ab2bc9dc33194f6aa7974eab17dace690>
2021-09-02 17:17:56.711 E failed to find transaction input in key images. img=<309adaccab8f88c40bd7665cc87bdbaac8a1d21c062a29d0f5d214dee80f1533>
2021-09-02 17:17:56.713 E transaction id = <0f46db919880ebc4670dcba0f26ca885ebceb44583aa2b7743e5970709c4fa90>
2021-09-02 17:17:56.835 E failed to find transaction input in key images. img=<e873a49c3972205fb8413f3c33b1ed02a80233cc65b328bdb0603bbca8a974c7>
2021-09-02 17:17:56.837 E transaction id = <64bd27aeb6bfa642cfd1e54bc040904f133a5788016b792e446f3d3c6510c991>
2021-09-02 17:17:56.942 E failed to find transaction input in key images. img=<0ec658a3badeede65e7958134dcc9bc4fa0ed42b929e0f20552f49fbd91c6315>
2021-09-02 17:17:56.945 E transaction id = <3a26a078ba05b0b25ca1d55d3f0e2759e116f14111f854e37212048ee8e10992>
2021-09-02 17:17:57.061 E failed to find transaction input in key images. img=<c513ee7a741a7487d69a4540a505c00c20bdecd1e1ae38e258c2f57a946fea83>
2021-09-02 17:17:57.063 E transaction id = <b37cf0b8f3e7d07fcd922db9767396239d01e3717afc5af0cd5454365aef0d95>
2021-09-02 17:17:57.169 E failed to find transaction input in key images. img=<068e6d240e93f7840e332d64db080c81199b88db2eee010303859f261bf87f41>
2021-09-02 17:17:57.171 E transaction id = <6740480377eac1fbf93cc051413defe669dfd0d4a06826f39170c0004e4e7795>
2021-09-02 17:17:57.280 E failed to find transaction input in key images. img=<8041c18badb236b6c8bf36d01af50ec5b41346942e7415e39ba008a9ec0c9574>
2021-09-02 17:17:57.282 E transaction id = <a6220ba73da3ce8e0dc0a2230aabf942bfabd50e66f614cc3f131f208603c898>
2021-09-02 17:17:57.404 E failed to find transaction input in key images. img=<77a38571c098b7feb07c341f4b7d817a57d36b486f0a773a7fd8ca757fef9767>
2021-09-02 17:17:57.407 E transaction id = <dbaaa4e3018a82431c13775493f3e4a7d1efb263b2f5b7f32cb15afa39fb069a>
2021-09-02 17:17:57.510 E failed to find transaction input in key images. img=<c40d78bc29a3fa9886b5a468818c3a5dbe73c0555ddbbc6817d5c265ed4b4d06>
2021-09-02 17:17:57.512 E transaction id = <dc4eb6a6694dd0c5edacb57ee5d4ed0d8117e27e3e084bbf4a4c29e6ae65079d>
2021-09-02 17:17:57.629 E failed to find transaction input in key images. img=<eae181b794c196f303dd468a7316f59dca0d5fc33b7ed7842d9fd9d033db1fd4>
2021-09-02 17:17:57.631 E transaction id = <d14b5a41084a6aedf858fec5f0761284b49c3552046d8355311307c3d57fc89d>
2021-09-02 17:17:57.743 E failed to find transaction input in key images. img=<9623d5a25a32f26c224639e2b599fcb59910f3cbf99a6ad8414be76c41dcbc7c>
2021-09-02 17:17:57.745 E transaction id = <7a285cf9fe04c77b6bea8ace16bc9f0ef650b94a97624b75d9604dfea858eba3>
2021-09-02 17:17:57.844 E failed to find transaction input in key images. img=<9665331147bdf704edf0a6d903b8b3c694759872d4988f87d476f726ed47af6f>
2021-09-02 17:17:57.846 E transaction id = <5aee73fbc43ac33eb618b99b46f7a7cadc309491833478cf73eb9d3a57292fa5>
2021-09-02 17:17:57.944 E failed to find transaction input in key images. img=<c96c4b0654369ca7d58fd557d71bd787e05c90a3eb9e648f323b5f954da69726>
2021-09-02 17:17:57.947 E transaction id = <dece34bc9c220845ba853f74887c53d36ab37606612ef0c3a260984998939fa6>
2021-09-02 17:17:58.061 E failed to find transaction input in key images. img=<795ffc6588f2c468a5cbdad3de18fcb378a99d12f6d461437ae9ec37154aca5d>
2021-09-02 17:17:58.064 E transaction id = <f07e448c555f4c2766485a69fa0d6e347bf837b31ec18b29c4802a0f2e4814a9>
2021-09-02 17:17:58.184 E failed to find transaction input in key images. img=<7c9ba83ff93cd0a7ae59a71953abaee617c35f5886fc8bbd844480fec6785d59>
2021-09-02 17:17:58.186 E transaction id = <b218aed41e6e2e34a998d5723acd7b1e1503a052837cb224a75829dc315552ac>
2021-09-02 17:17:58.302 E failed to find transaction input in key images. img=<bee9dd201744e83c2c89c366fab910e8c4d5f7024643828528c9750c564be4fa>
2021-09-02 17:17:58.305 E transaction id = <3340434886de1b105ddee4879e2ccb17c4172462196729e459df2fdbc14d1baf>
2021-09-02 17:17:58.409 E failed to find transaction input in key images. img=<6bbb59bb16bc976625ff1fcf4b57d7d79ada513c84624412c4d922641cf5d2de>
2021-09-02 17:17:58.411 E transaction id = <0036953670bf844cc127e82618df78a6576affacead6c944a1ddc5d2cc02f9b3>
2021-09-02 17:17:58.508 E failed to find transaction input in key images. img=<cfdc95fff865b639974c78181a93ad3668a64db7b55bfd360f35117f3bc2012c>
2021-09-02 17:17:58.510 E transaction id = <3da2a6ca5764101b8138dc9f8e4d14dc60494c046c4dc8137e418e018398dfb6>
2021-09-02 17:17:58.667 E failed to find transaction input in key images. img=<c45accecb188cd601b632766c6fedf61cbe20c66fecc1d607d12d4d8a8ad7eed>
2021-09-02 17:17:58.669 E transaction id = <d489dc0273aed6bed5d4851faceeed9c5ca93b4df05dc1f65201d3be7b2e3bb7>
2021-09-02 17:17:58.775 E failed to find transaction input in key images. img=<1495eda90a1985cc54d6fb6692285ec4f954d55d8d6b2423d729d5e390bf1695>
2021-09-02 17:17:58.777 E transaction id = <1d3e6433e368c66ed7d4fe0b3b4396e8a7c0dba62b019c7fe28d60c96ef0f0b9>
2021-09-02 17:17:58.875 E failed to find transaction input in key images. img=<ec22ff9ff85bd6220edf434af0a6e87da65a4651b09515f994f34010457a8f1e>
2021-09-02 17:17:58.877 E transaction id = <8debcecb51d8d9d0d45cdf598ad05d4840f706d28546c76b4ddf6e3662f807bb>
2021-09-02 17:17:58.974 E failed to find transaction input in key images. img=<fe52ebf98e48a9c9ea29f31c3c6a15bde9b10870977fc373b51a3e24c1151017>
2021-09-02 17:17:58.977 E transaction id = <a183906b1588092eb20fc82213af682ee5d9e135646f279e94956715839881bb>
2021-09-02 17:17:59.075 E failed to find transaction input in key images. img=<e68a831c612242664a8eb14e7bf925d367b7a0252d8180712b9f8ed4d5d43d59>
2021-09-02 17:17:59.077 E transaction id = <9a5e39bedac31f20631d5c3da28904dde52e7cfa8ab9853915d52dc8dcac9abf>
2021-09-02 17:17:59.183 E failed to find transaction input in key images. img=<2559127800c0d471146766d3898bf091311e34f8f96d2602438040ab6317da83>
2021-09-02 17:17:59.186 E transaction id = <054c4dda0dd9968c3b24dcb53a06706b0db762c56457892178d871b7a47d66c0>
2021-09-02 17:17:59.284 E failed to find transaction input in key images. img=<bb0b4500638756068f15cbc6629e78761be8835ee6294a18f33a8773b9af4e85>
2021-09-02 17:17:59.286 E transaction id = <69edb74145a65b2abb7561c52c69b02cc38b24f29607c609ba54e6de733168c1>
2021-09-02 17:17:59.375 E failed to find transaction input in key images. img=<fb7889494b963226f4be5f4d68a0bd55f5c7545e1c48750aa9a797031cccdc2a>
2021-09-02 17:17:59.377 E transaction id = <97bb9e865e15189c40e678752ce1383a7a9829f71405b2dea0515ca1bc9934c2>
2021-09-02 17:17:59.483 E failed to find transaction input in key images. img=<51743aa038fbfef7feaa3dc052aa28f18a318c099b0e2bb85df45e573e8dabd2>
2021-09-02 17:17:59.485 E transaction id = <0aeec508872eb0cdc02df90b91c5f9709ffa7861e6e35f26812797ec890b43c5>
2021-09-02 17:17:59.592 E failed to find transaction input in key images. img=<eb79b545cbc585901047d48527bbad9af5f4b463432627a66e074fc2db637d89>
2021-09-02 17:17:59.594 E transaction id = <01f88335f59b849338e0b2c6cffb85c81dc17c88301d119a013ded37aadbf4c7>
2021-09-02 17:17:59.692 E failed to find transaction input in key images. img=<3aa7caaa2fe037701a7f0af96af1ed4ea550c7b75d6ad0ec410255f5904e14bd>
2021-09-02 17:17:59.694 E transaction id = <7079466f239995702f80b62c45f3e2847b78fc749ed09b796f9b1a38a60762cb>
2021-09-02 17:17:59.785 E failed to find transaction input in key images. img=<e77125b2778acb9ccc5a6916a48ac9b4943cb657830c70448a46b12c96e895ed>
2021-09-02 17:17:59.787 E transaction id = <4210fbe53535aac96c57ef62976f2f65ff9922fd4bdc4ffb7b940fe4b5f65bcf>
2021-09-02 17:17:59.892 E failed to find transaction input in key images. img=<2ca2ff429bbe30516b5134e9fb50cd855ae531c898734db1f6a0d8a73438d526>
2021-09-02 17:17:59.894 E transaction id = <0e958b9e2ca05113cc760d55f3c089d2a75595d5b7ac43776508ec4623f273d1>
2021-09-02 17:18:00.000 E failed to find transaction input in key images. img=<c04506f48cdd06945644d3c24ade365caa764775964d19b622c2087f21f9dce5>
2021-09-02 17:18:00.002 E transaction id = <7918ba804ecb895d1e56a7a1cffe5fd733e2679793d2975656dd6b4b4a05a9d5>
2021-09-02 17:18:00.125 E failed to find transaction input in key images. img=<eccc635f870be5b29aa653d5219211052b08136eb241285b3bea5d7a477ba2eb>
2021-09-02 17:18:00.133 E transaction id = <29ace4538abd2e71acf5319c9d59512ae0c839eaa8062dc5d569bb38ff1a0fda>
2021-09-02 17:18:00.225 E failed to find transaction input in key images. img=<4c12527a999a8eee5a769507fd3118acb29ae0e86a2ef38c460919ddc5a18bc5>
2021-09-02 17:18:00.228 E transaction id = <95c2c28a4be63135c4f92d273cf9a8621f24a7d981f2fc0ba9f9da46fffd18da>
2021-09-02 17:18:00.316 E failed to find transaction input in key images. img=<fdafeacf856b1242c14bc5b833df7e15c2529125256aee6e100f10b94462aba7>
2021-09-02 17:18:00.318 E transaction id = <626db48f4a313afcb30b8cf3f354fb3a949b28999588aef35c92c015b84f51da>
2021-09-02 17:18:00.417 E failed to find transaction input in key images. img=<7e7d4b22598c1e7ffe331c79b5a2d8b9876646577682beba1e06b975f6c31702>
2021-09-02 17:18:00.418 E transaction id = <6ad1d6cfa78f6c1b9e190708aa701a04cac82ccd23ed11867824c5fafa01ece7>
2021-09-02 17:18:00.499 E failed to find transaction input in key images. img=<a688d754cabe4a7481692686b37e62aef6353a51723b217793aabb2b575a6804>
2021-09-02 17:18:00.501 E transaction id = <d0e9169a00719d4ac8df9c1eefe2acd1e46820f511b6adc059c38224e084aeef>
2021-09-02 17:18:00.600 E failed to find transaction input in key images. img=<d400e31ccdb3c37373bec7f02d58b6ed7c15c64e95de9be370702f88051ac333>
2021-09-02 17:18:00.603 E transaction id = <bd7d32f8c0f7cfe50409127880805dca184fe359fbc7c776d5e64216704708f0>
2021-09-02 17:18:00.683 E failed to find transaction input in key images. img=<4fb6502cea180230c9331d30f88dbf14e2f5cd3778de63e21e2941bef12b3509>
2021-09-02 17:18:00.686 E transaction id = <5b94d12e5281c801eefa212caa28dc77e9623e0341b7a0375c6bee9c8785f9f2>
2021-09-02 17:18:00.758 E failed to find transaction input in key images. img=<82a2d124ca7898825ace4aa2a978caf7c2d019827e67ae5472ba39873ee14d30>
2021-09-02 17:18:00.761 E transaction id = <a2a4f6af8c34c2098dcbfe0d2ac1a29c94c2a734a17db03174b13624b4a221f4>
2021-09-02 17:18:00.849 E failed to find transaction input in key images. img=<45405e3c1649ecae7c0f68613c0ad5834b1d07cc5e4a5e474bf757c0aef44c0a>
2021-09-02 17:18:00.851 E transaction id = <132113bf86978a2398452170bfc0f2e0d7d2c65113d922b95fe2598b6f3082fd>
2021-09-02 17:18:00.925 E failed to find transaction input in key images. img=<ae10975d22cd976d36d475615bde2c8c80425f5d7ac0e235852c9a0108e8df68>
2021-09-02 17:18:00.927 E transaction id = <7bab515e942217cc6aeedd107c11589802a9c1bf73281d39edfa123f1ac781fe>
2021-09-02 17:18:38.726 I Loading checkpoints
2021-09-02 17:18:38.899 I Core initialized OK
2021-09-02 17:18:38.901 I Initializing p2p server...
2021-09-02 17:18:38.943 I p2p server initialized OK
2021-09-02 17:18:38.946 I Initializing core RPC server...
2021-09-02 17:18:38.949 I Binding on 127.0.0.1 (IPv4):18081
2021-09-02 17:18:40.311 I core RPC server initialized OK on port: 18081
2021-09-02 17:18:40.324 I Starting core RPC server...
2021-09-02 17:18:40.327 I core RPC server started ok
2021-09-02 17:18:40.330 I Starting p2p net loop...
2021-09-02 17:18:41.335 I
2021-09-02 17:18:41.339 I **********************************************************************
2021-09-02 17:18:41.341 I The daemon will start synchronizing with the network. This may take a long time to complete.
2021-09-02 17:18:41.348 I
2021-09-02 17:18:41.350 I You can set the level of process detailization through "set_log <level|categories>" command,
2021-09-02 17:18:41.357 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2021-09-02 17:18:41.359 I
2021-09-02 17:18:41.360 I Use the "help" command to see the list of available commands.
2021-09-02 17:18:41.365 I Use "help <command>" to see a command's documentation.
2021-09-02 17:18:41.374 I **********************************************************************
2021-09-02 17:18:42.845 I [162.218.65.40:18180 OUT] Sync data returned a new top block candidate: 2424118 -> 2440708 [Your node is 16590 blocks (23.0 days) behind]
2021-09-02 17:18:42.848 I SYNCHRONIZATION started
2021-09-02 17:21:23.753 I Synced 2424138/2440710 (99%, 16572 left, 0% of total synced, estimated 1.3 days left)
```

# Discussion History
## selsta | 2021-09-02T18:06:06+00:00
Does it continue to sync fine?

## tikwanleap | 2021-09-02T21:07:14+00:00
Yes, it seems to be syncing normally after the errors. See snippet below:
```
2021-09-02 20:31:54.088 I Synced 2430358/2440836 (99%, 10478 left)
2021-09-02 20:32:42.287 I Synced 2430378/2440837 (99%, 10459 left, 37% of total synced, estimated 5.4 hours left)
2021-09-02 20:33:37.253 I Synced 2430398/2440837 (99%, 10439 left)
2021-09-02 20:34:32.458 I Synced 2430418/2440837 (99%, 10419 left)
2021-09-02 20:35:18.718 I Synced 2430438/2440837 (99%, 10399 left, 37% of total synced, estimated 5.4 hours left)
2021-09-02 20:36:36.917 I Synced 2430458/2440838 (99%, 10380 left)
2021-09-02 20:37:25.486 I Synced 2430478/2440839 (99%, 10361 left, 38% of total synced, estimated 5.4 hours left)
2021-09-02 20:38:22.216 I Synced 2430498/2440841 (99%, 10343 left)
2021-09-02 20:39:24.716 I Synced 2430518/2440841 (99%, 10323 left)
2021-09-02 20:40:11.250 I Synced 2430538/2440842 (99%, 10304 left, 38% of total synced, estimated 5.4 hours left)
2021-09-02 20:41:07.300 I Synced 2430558/2440842 (99%, 10284 left)
2021-09-02 20:41:57.284 I Synced 2430578/2440842 (99%, 10264 left)
2021-09-02 20:42:38.167 I Synced 2430598/2440842 (99%, 10244 left, 38% of total synced, estimated 5.4 hours left)
2021-09-02 20:43:41.915 I Synced 2430618/2440845 (99%, 10227 left)
2021-09-02 20:44:29.383 I Synced 2430638/2440847 (99%, 10209 left)
2021-09-02 20:45:41.144 I Synced 2430658/2440847 (99%, 10189 left, 39% of total synced, estimated 5.4 hours left)
2021-09-02 20:46:30.114 I [batch] DB resize needed
2021-09-02 20:46:30.114 I Synced 2430678/2440847 (99%, 10169 left)
2021-09-02 20:46:30.729 I LMDB Mapsize increased.  Old: 125566MiB, New: 126590MiB
2021-09-02 20:47:17.298 I Synced 2430698/2440847 (99%, 10149 left)
2021-09-02 20:48:09.770 I Synced 2430718/2440847 (99%, 10129 left, 39% of total synced, estimated 5.3 hours left)
2021-09-02 20:48:47.081 I Synced 2430738/2440848 (99%, 10110 left)
2021-09-02 20:49:43.497 I Synced 2430758/2440848 (99%, 10090 left)
2021-09-02 20:50:23.743 I Synced 2430778/2440848 (99%, 10070 left, 39% of total synced, estimated 5.3 hours left)
2021-09-02 20:51:04.027 I Synced 2430798/2440848 (99%, 10050 left)
2021-09-02 20:51:35.955 I Synced 2430818/2440848 (99%, 10030 left)
```

**Another interesting datapoint:**
I was bored and looked up all the transaction id's and they are all in either block 2424118 or 2424119.

I also noticed that the blockchain sync started at 2424118, so maybe there was a consensus reorg on block 2424118 and I just happened to have the non-consensus version of block 2424118 when I previously shut-down monerod.exe.

`
2021-09-02 17:18:42.845 I [162.218.65.40:18180 OUT] Sync data returned a new top block candidate: 2424118 -> 2440708 [Your node is 16590 blocks (23.0 days) behind]
`


## selsta | 2021-09-02T21:13:07+00:00
If everything else works as expected I would ignore it.

## tikwanleap | 2021-09-02T21:27:06+00:00
Ok sounds good. Closing this issue.

# Action History
- Created by: tikwanleap | 2021-09-02T17:29:15+00:00
- Closed at: 2021-09-02T21:27:06+00:00
