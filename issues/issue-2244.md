---
title: '[Trezor] Confirmation is asked twice on Trezor (macOS)'
source_url: https://github.com/monero-project/monero-gui/issues/2244
author: rating89us
assignees: []
labels:
- resolved
created_at: '2019-07-01T19:31:37+00:00'
updated_at: '2019-09-05T21:36:34+00:00'
type: issue
status: closed
closed_at: '2019-09-05T21:36:34+00:00'
---

# Original Description
Latest GUI (0.14.1 beta)
Trezor Model T (firmware v2.1.1)
macOS 10.14.3 (Mojave)

- After authorizing the transaction on Trezor, the device signs it normally.
- GUI opens last confirmation window "Please confirm transaction" normally.
- "Proceed to device" window appears for a second time (unexpectedly).
- Trezor asks for authorization again (unexpectedly), same transaction amount and fee.

@ph4r05 

# Discussion History
## ph4r05 | 2019-07-01T19:44:16+00:00
Which confirmation is the second one displayed? If its just a refresh confirmation prompt it is OK. Refresh confirmations will be required only once in new firmware versions.

## rating89us | 2019-07-01T19:47:54+00:00
It's not a refresh confirmation, it's the transaction signing confirmation that is being displayed 2x (showing destination address, amount and fee + hold to confirm prompt).

## ph4r05 | 2019-07-02T20:06:20+00:00
Thats quite a strange behaviour I've never experienced during the testing. I will take a look. 
Would it be possible for you to produce a log from such run?

Thanks!

## rating89us | 2019-07-02T20:15:49+00:00
If you can help me, sure. I don't know where GUI stores log files on macOS.

## ph4r05 | 2019-07-03T15:20:31+00:00
Hmm I think the problem can be in the Trezor UI, we will look into it and let you know.

## ph4r05 | 2019-07-03T15:27:43+00:00
@rating89us is the problem you are experiencing with the screen below?

![Screenshot 2019-07-03 at 17 14 00](https://user-images.githubusercontent.com/1052761/60604366-d46d0000-9db7-11e9-97bf-036aea6e3196.png)

Are you stuck on this confirmation screen? Can you move to the next one or it is not possible?

## rating89us | 2019-07-03T17:26:28+00:00
This screen you posted is displayed two times on Trezor, but it's not stuck. 

What happens:
1) "Proceed to device" window appears on GUI.
2) My Trezor opens this "Confirm send" request. I confirm (hold to confirm). It works normally as expected.
3) Then GUI opens last confirmation window "Please confirm transaction".
4) "Proceed to device" window appears on GUI **again**.
5) My Trezor opens this "Confirm send" request **again**. I hold to confirm. It works normally.

If I cancel the second Trezor confirmation, it doesn't confirm. I must confirm both requests for the transaction to work.

## ph4r05 | 2019-07-08T14:30:24+00:00
The application logs to standard output. You can see the logs by running the GUI from the terminal:

```
MONERO_LOG_LEVEL=4 monero-gui-v0.14.1.0/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui 
```

I could not reproduce the bug, when using official monero-gui-v0.14.1.0 build and the Trezor firmware 2.1.1, from `release/2019-06` branch. 

Could you possibly take a photo of the confirmation from step 5? Trezor can legitimately ask you to confirm blockchain refresh once the operation is signed - thus the second confirmation. It is perfectly OK and intended. If the confirmation from step 5 is amount confirmation, then it is a bug.

Pls check if you see some errors in the log file. Without further information I am not able to diagnose the error.

Thanks!

## rating89us | 2019-07-08T19:09:48+00:00
I tried to reproduce the bug today, but it was not happening anymore (I didn't update GUI wallet ou Trezor firmware during this period).

But I could recover the log file from the day I got the error. Maybe it's useful.

The following error lines appear a lot (hundreds of times):
```
2019-07-01 19:22:27.360	  0x70000895c000	ERROR	cn	src/cryptonote_basic/cryptonote_format_utils.cpp:184	Failed to parse transaction from blob
2019-07-01 19:22:27.360	  0x70000895c000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:935	Invalid tx data
```

The remaining log is below:
```
2019-07-01 19:12:22.096	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///wizard/WizardController.qml:270:9: QML Flickable: Binding loop detected for property "contentHeight"
2019-07-01 19:12:34.466	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///wizard/WizardController.qml:270:9: QML Flickable: Binding loop detected for property "contentHeight"
2019-07-01 19:12:36.023	     0x11223f5c0	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:5513	error removing file: /var/folders/50/yf0rf4s916d_7c_5x1cxhsvc0000gn/T/monero-core.RDH744.address.txt
2019-07-01 19:12:36.073	     0x11223f5c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-07-01 19:12:36.080	  0x7000088d9000	INFO	global	contrib/epee/src/net_ssl.cpp:124	Generating SSL certificate
2019-07-01 19:12:36.082	  0x700009d00000	INFO	global	contrib/epee/src/net_ssl.cpp:124	Generating SSL certificate
2019-07-01 19:15:06.957	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Keys.qml:123: TypeError: Cannot read property 'walletCreationHeight' of undefined
2019-07-01 19:15:20.149	  0x70000895c000	WARNING	device.trezor	src/device_trezor/device_trezor.cpp:448	KI computation state change failed, started: 0, e: Device state not initialized
2019-07-01 19:15:20.193	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///wizard/WizardCreateWallet1.qml:154: TypeError: Cannot read property 'walletCreationHeight' of null
2019-07-01 19:15:20.194	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Keys.qml:123: TypeError: Cannot read property 'walletCreationHeight' of undefined
2019-07-01 19:15:20.199	     0x11223f5c0	ERROR	frontend	src/wallet/api/wallet.cpp:414	Trying to close non existing wallet  QObject(0x0)
2019-07-01 19:15:20.199	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///wizard/WizardCreateWallet1.qml:154: TypeError: Cannot read property 'walletCreationHeight' of undefined
2019-07-01 19:15:20.200	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Receive.qml:169:39: Unable to assign [undefined] to QString
2019-07-01 19:15:20.200	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Account.qml:245:39: Unable to assign [undefined] to QString
2019-07-01 19:15:22.599	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///wizard/WizardController.qml:270:9: QML Flickable: Binding loop detected for property "contentHeight"
2019-07-01 19:15:31.822	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Receive.qml:169:39: Unable to assign [undefined] to QString
2019-07-01 19:15:31.823	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Account.qml:245:39: Unable to assign [undefined] to QString
2019-07-01 19:15:31.823	     0x11223f5c0	INFO	logging	contrib/epee/src/mlog.cpp:273	New log categories: *:WARNING,net:FATAL,net.http:FATAL,net.ssl:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,serialization:FATAL,stacktrace:INFO,logging:INFO,msgwriter:INFO
2019-07-01 19:15:31.829	  0x700008750000	INFO	global	contrib/epee/src/net_ssl.cpp:124	Generating SSL certificate
2019-07-01 19:15:31.930	  0x70000895c000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:4008	Account on device. Initing device...
2019-07-01 19:15:38.419	  0x70000895c000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:4023	Device inited...
2019-07-01 19:15:38.470	  0x70000895c000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5246	Loaded wallet keys file, with public address: (hidden)
2019-07-01 19:15:38.493	  0x70000895c000	ERROR	wallet.mms	src/wallet/message_store.cpp:735	No message store file found: /Users/myuser/Monero/wallets/myuser/myuser.mms
2019-07-01 19:15:38.495	  0x700008750000	INFO	global	contrib/epee/src/net_ssl.cpp:124	Generating SSL certificate
2019-07-01 19:15:49.993	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Receive.qml:169:39: Unable to assign [undefined] to QString
2019-07-01 19:15:49.993	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Account.qml:245:39: Unable to assign [undefined] to QString
2019-07-01 19:15:50.774	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Account.qml:245:39: Unable to assign [undefined] to QString
2019-07-01 19:17:20.889	  0x700008beb000	WARNING	device.trezor	src/device_trezor/device_trezor.cpp:448	KI computation state change failed, started: 0, e: Device state not initialized
2019-07-01 19:17:20.896	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Keys.qml:123: TypeError: Cannot read property 'walletCreationHeight' of null
2019-07-01 19:17:20.941	  0x700008750000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:4008	Account on device. Initing device...
2019-07-01 19:17:26.817	  0x700008750000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:4023	Device inited...
2019-07-01 19:17:26.865	  0x700008750000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5246	Loaded wallet keys file, with public address: (hidden)
2019-07-01 19:17:26.865	  0x700008750000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:5255	file not found: /Users/myuser/Monero/wallets/myuser/myuser, starting with empty blockchain
2019-07-01 19:17:26.887	  0x700008750000	ERROR	wallet.mms	src/wallet/message_store.cpp:735	No message store file found: /Users/myuser/Monero/wallets/myuser/myuser.mms
2019-07-01 19:17:26.899	  0x700008750000	INFO	global	contrib/epee/src/net_ssl.cpp:124	Generating SSL certificate
2019-07-01 19:18:48.552	  0x70000895c000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:2533	Failed to generate key derivation from tx pubkey, skipping
2019-07-01 19:25:00.124	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	Data set on unsupported clipboard mode. QMimeData object will be deleted.
2019-07-01 19:25:13.486	  0x700009d00000	WARNING	net.dns	src/common/dns_utils.cpp:568	WARNING: no two valid DNS TXT records were received
2019-07-01 19:25:13.868	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:3332	Failed to request output distribution: no connection to daemon
2019-07-01 19:25:17.183	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:25:17.183	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:25:17.195	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:25:17.195	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:25:17.207	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:25:17.208	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:25:17.340	  0x700008beb000	WARNING	net.dns	src/common/dns_utils.cpp:568	WARNING: no two valid DNS TXT records were received
2019-07-01 19:25:17.460	  0x700008beb000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:3332	Failed to request output distribution: no connection to daemon
2019-07-01 19:25:19.748	  0x700008beb000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:25:19.748	  0x700008beb000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:25:19.759	  0x700008beb000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:25:19.760	  0x700008beb000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:25:19.771	  0x700008beb000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:25:19.771	  0x700008beb000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:26:01.792	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:10058	{
  "version": 2, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 0, 
        "key_offsets": [ 4063346, 139407, 4997057, 710463, 855183, 345366, 6550, 5948, 1483, 209, 3703
        ], 
        "k_image": "a2e02d0b4b46d8e43c5c27b5986d491079cdecf43dc5104b8253fce1b7b504bc"
      }
    }, {
      "key": {
        "amount": 0, 
        "key_offsets": [ 5751296, 1232158, 2540784, 618968, 622026, 159538, 196014, 10960, 1402, 1881, 809
        ], 
        "k_image": "a1d87959e8dca258ea3fe588adfa97c9441c37758d2fe71537ac5e023911d319"
      }
    }
  ], 
  "vout": [ {
      "amount": 0, 
      "target": {
        "key": "c72a4033dd184cc1b2dd9ba549bdd3ed58d8d21991b3254f9bd53bd148c4b325"
      }
    }, {
      "amount": 0, 
      "target": {
        "key": "d5fff6f89071e7071424ff06b85110edd4db0ac1cdb839d0d21f12e3b1179e64"
      }
    }
  ], 
  "extra": [ 1, 104, 45, 56, 168, 100, 249, 243, 33, 169, 40, 241, 60, 4, 220, 117, 132, 127, 218, 67, 84, 233, 134, 18, 186, 165, 150, 254, 118, 115, 211, 251, 88, 2, 9, 1, 136, 179, 26, 101, 79, 80, 178, 161
  ], 
  "rct_signatures": {
    "type": 4, 
    "txnFee": 45530000, 
    "ecdhInfo": [ {
        "amount": "2869199a697b1abc"
      }, {
        "amount": "e1e46c0ba5077f63"
      }], 
    "outPk": [ "1644d0aaa8bd80efe1acb2b27938336eb223092ccb01d7e6afab75f8a03f31c3", "bfb3e4f70d56aa2719821414e7f615fb488bb92d57ea108cac655a9a7bc7b16c"]
  }, 
  "rctsig_prunable": {
    "nbp": 1, 
    "bp": [ {
        "A": "260c12d56f86c9578ce16ad7e70cf0d88c4c7b3d4e9eb0744c0ec7fc52610b20", 
        "S": "0212c5a617c0572611c40d1720bc42dbdbc72884eb477c416fd025228215d97d", 
        "T1": "530d356b4da5be684ed89df33c818eb2dee2f1980541bc2d92936be721d57e79", 
        "T2": "78adb59a497d32ae7fbb99c2719c3231a6dd40de4dd6be68cb9c8fde090ed3c8", 
        "taux": "33d5b04e95f7e96d9c833e75298772b0e31f111a39ceae6b5e915c6d5a36dd0a", 
        "mu": "01d802b47b79443883ac1a818403c51a621bd84c87f4be24f57d49be2afa9802", 
        "L": [ "4af6734a8e06d5ef2674b6166fb115e58a4ad6d2f4559fbac564b98331f445f1", "70015a161012abc6e416d4530a8738a3fcfbfc74e3deba8d49c9c821a9d9a2f9", "cafe3d2c9195b0f7864d25257cc6ad0a1972c6b949b739b1fc8f6078cb0907de", "3e7d04119149af7ebc90cee84e496c9169341fea036326ad8ec05ae59775d0c0", "08b22f994b7cdeba47e3ee4de84976cad767de8b5ef5bdb507fa0a48f2e5be51", "d836da97d933d829c949173776af2a5c75bf25e09743ae45a30944bdc04d9b88", "956121489bc1f643438c650e9c3dcda620410d180a8b59f9a624fc881ef31072"
        ], 
        "R": [ "616b7a5a1409f05d56ab8546151885d37b67c79d22fd69b63828cd6908527e8e", "a27882f301cd56a0dbc950cb10ec6ca480136d286ce74d8d72fa8ec0be889887", "096e57c0d582680de439da26b4803dac9e7e523ba535a06f8c1cbf2b1cc03279", "3d9303d3594679a4f7700ad737569e91c47f9d17573b203f54af4f5ad5eea8a2", "1273135b09fe94b9feeba60ee844825c5c78b6df6b0e9e379d0665b74b8804dd", "e4f34dbfbf7602242806900e314b5694325b4aa3f7c74b959475e558fc2531d6", "12e407ef64eb567c66610e1359923ac805626d0edee79280cbfc72e747d72fe9"
        ], 
        "a": "52c9379a19c75c1e8f13ea7137d2b31657784312f9324af3835f0284e03cec0a", 
        "b": "30d7955eddaae31e3db21dd6550b4d55e05ad037ef0f94154955042220a37d02", 
        "t": "0977efff944ebcb233ee845ce42acf339bdbc54a258e851002c55bc0e343930a"
      }
    ], 
    "MGs": [ {
        "ss": [ [ "d4a6dc6b230d4bfa5f6c74640a7d303509dbe8dc6c6757b368a312dab3270409", "40ab0e6c7cb4dd0f551845eaa06ff39f22e6d0e23b5f242af0d98163206ab30d"], [ "3e3839964cef52edc8ff2f50b162f3df73f7b21c292d41558a88ce5e4979c60a", "f37f95710d3997181e59b48cc6d940d0fc96835d448d6952909a31dc51ce6504"], [ "e43cfdbc69d12d175b5c7ec3c4689dc6cad974f52c7a8ee8d9a8ee477928e806", "38d93c819920f52c446f22c0ff7e8817a11d7b56f33c03688b447eb171a65d08"], [ "74c0756099aa57eea6f9b5d3078007a9080870449cce15eccab601f8d729be0c", "46907b68cfa46c505b579ab7df233f455a0c04f07990d8b5ac548bcb58b89703"], [ "28188604ef3819e5730fce9ba847a5eca19253ffba062797ad8ad4b4ce156208", "16f4f2db90ea26468921fb6264dd2c7fcaa25e184619f9d6bba7d9dd491db80f"], [ "154ea04383bbde2d24efbfa136f40c588a9fbefea16985a2894b959c273f380c", "f41ea5c418f3b22e09b9c818a74dfe297aa495b01a93aca492ac26fab6530601"], [ "efb341b4e081bcdc6020ddfbd445dfe8075db5d9fe18d0cb447e1ead9a302a04", "f5aa94f8a5b953197903c70bf4653af6297d3d77a097d7d77b138e2aceb6ae0d"], [ "2ad9b5ef5d1fc25504494008cf7fc3e6d119c6ba96187e2b77500f9a65f4220c", "a8527620b5391b9b92c95318557e73caa0e5889512eae27dfb3f7c5372b7d101"], [ "c5b9e129960e3561533642a7621c5c8b7baaef7ff3d18415e044f9e953bfd00c", "c8836ad2bec036cfaa5c3bd17669e7eda06cf6682407f3f10cebc583626c7c09"], [ "a8060e2308527552292a9b6f9e85842de99b256c0c62c73dd5ebcfed940ca108", "69649322a7da9f122b3d7f9c95567fdf6d9e4b781a9b86037ccb31255999720b"], [ "9ac38e09fc0f63211cc57b43d392717e008095e306e228f6a2adb824016cb509", "596d0748a651b15a0482f31831b3c3bf414f17923fc8a1ae0c272b04a28b2c0d"]], 
        "cc": "0dd90d3515faa5e9856457cf088472e7df98308fa3e6f1f59ed69898519e2b0f"
      }, {
        "ss": [ [ "8d22704417bdbfbaf6d7464326c5438624e13c6e64dda2ec3f17b395d1310c0b", "d9fecbe5e6c296a4fd230de9be6b72cae6d958175741c8a09b7f2febfa94120e"], [ "91ae818f0d3d41f067fdf42889e74d828c7a3e99ffdfa815f780d8d135e3a407", "c59e346ed361255c0d88b7042a3a6f108bc5ac974962e5d326552ea407fcb905"], [ "ea554a3c181f0c6406df76aa0d61c794f53be059941b7148b91f0a42991fdd0b", "b73eeda6af9fe50baad39a2f79ecafa51906fe4ba23486abf92a5410d1593c00"], [ "ffca5cfb7835e1c7f0ba76d4be5ea24cbfacb5c930e9630cd7418d39b99a9e0b", "d7913a86b34cc916c6645ff39e5bd06bbc2a296b3729a12c97b0aa1bbbad9606"], [ "0244297f3ae09fd973965a0f3bb612b55e718d48811ffcac556cbd1b82ecaa08", "3aca15f95d052fb8a5985187a7b366e4be083caea7b89190971e4be677378e05"], [ "98fc77eedcb67588629b077d5d0b4cf7e9edd9e10317a34c6050e473e37ced07", "2552e724ca701ec1d0c860799267c994e438045de90c02eb4f562dbfec595b05"], [ "23a8c6682ec41089c4b3b96ecd02a7a7aeb26980e6240690608ac0da7e581a07", "dcbc07be610eb9848ada8ce792a36e95e3e0b0dc9f23a231fa8ca6ec46ba400e"], [ "c372f31cec779b6575ec086eba7288c21df7a0f3827f40af030391b66d5d4a0c", "e39566490953b0a7e93fbfd6049ee3d5d6879e503ef1453c14cee9d24e6b5e05"], [ "1511aa6562554b61cef35ef14b6cdc8924f47432ec39c2ec1c5b6de1368a390c", "9448db02fb045e504d311093216ce94befb520ffc105487092e223f36329e20f"], [ "c3625db366164593f21b33e7f431d72c88505e5a9140b732591bc63c353d690e", "a12dc6b2384f5d5939a943269f416532aaab9e5af6dc04a383b25dcb77dc880b"], [ "7b532462d44de16629b5a70ef757bf364298b57af2114a31817cc40a6e47f70d", "ac9c282fa28570b535b84c08aef26316759499793c90b54c2b0fc60bda9d8c0f"]], 
        "cc": "2a0a1f2bd8c22b37ebec035eb00c437ddf2734782443744a9f7d47e4c6cdfb0b"
      }], 
    "pseudoOuts": [ "ce42daafafc32ab1b7290fd14254e82b111355b63fbf9a3463ecd578d245f1df", "75c00d69fb6500bbf694435a183b00d864c1e435747803de08cbfc27d11fd3ae"]
  }
}
2019-07-01 19:26:01.792	  0x700009d00000	WARNING	frontend	src/wallet/api/wallet.cpp:410	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x600000051800), parent's thread is QThread(0x600003f7ca40), current thread is QThread(0x600002f38000)
2019-07-01 19:26:40.877	  0x700008beb000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:10058	{
  "version": 2, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 0, 
        "key_offsets": [ 4063346, 139407, 4997057, 710463, 855183, 345366, 6550, 5948, 1483, 209, 3703
        ], 
        "k_image": "a2e02d0b4b46d8e43c5c27b5986d491079cdecf43dc5104b8253fce1b7b504bc"
      }
    }, {
      "key": {
        "amount": 0, 
        "key_offsets": [ 5751296, 1232158, 2540784, 618968, 622026, 159538, 196014, 10960, 1402, 1881, 809
        ], 
        "k_image": "a1d87959e8dca258ea3fe588adfa97c9441c37758d2fe71537ac5e023911d319"
      }
    }
  ], 
  "vout": [ {
      "amount": 0, 
      "target": {
        "key": "170a2d8501b463bb0b8797e0a18a98615501d48483182f46bd14a9018510aca7"
      }
    }, {
      "amount": 0, 
      "target": {
        "key": "5713e30620481c7c8dc26b809dab52af602ecb16dde29b022703779aff056553"
      }
    }
  ], 
  "extra": [ 1, 254, 193, 219, 20, 189, 193, 170, 217, 217, 79, 171, 82, 199, 75, 126, 247, 62, 252, 129, 120, 99, 1, 173, 142, 87, 228, 92, 59, 137, 162, 213, 78, 2, 9, 1, 98, 64, 253, 16, 26, 201, 56, 132
  ], 
  "rct_signatures": {
    "type": 4, 
    "txnFee": 45530000, 
    "ecdhInfo": [ {
        "amount": "66a5dc05c6ca2ea2"
      }, {
        "amount": "9e84872d49b7009b"
      }], 
    "outPk": [ "f5630a0be525b3e0df845ebe9cfee0551cf51e0e7f847866a99c503b1f80833f", "07adce9f4b650c8440bfe5dab0ff478c0c9d741632f032948b9c29782d648942"]
  }, 
  "rctsig_prunable": {
    "nbp": 1, 
    "bp": [ {
        "A": "ae6f69f1a80c90358353f0a130839b5bb2d5ff3516f898b8418f5c30390d29e6", 
        "S": "9d71f28b453abf3d857676e58341f36f2d5f9fa984a07e440c2c4716f6ef33fc", 
        "T1": "58963612c7469d766e1eb52f80aacb899c923381c6c7f9af4ca65f83342decfb", 
        "T2": "e38689f671a9da3307331d2e85733b6f70bd088487f408fbf75fd70023024a46", 
        "taux": "ab3bf2fd1b3c453e47dc6fb319c6c525e5988a8848218b01b13e78a55cb2db08", 
        "mu": "dedac30c2059fe3619894eb440ac678bbdc198e86497f778ca3c89029651560d", 
        "L": [ "e3d532265dde691ef460d8725f0b6b601eb59e30582ba054c46160ccf13ecdc4", "6a5c6c87d2f72753a07e01f5632be2bc8e444b1c6bb8822aac941eded83993ff", "e9653588fa739ddcc40c0eeadce7bd25a1b87659c0ed203ce124b78f0805a21a", "38853d26726b309648cd5bf1fdf50d5de2dbd962d803e6f5f1503495215d75f9", "046a0d5faae38dd30b05cd962e05f76c88eef3ac30278cf30bcafefd6be3e444", "b9686061c7ec62fb88ccb4d18416dc090d51096f94a0dce16105c8d4d4c7bb6f", "46abcd1aea3ec412531378dddd0349c3d2d12dc38823b28049db69a09d1c5504"
        ], 
        "R": [ "8a8976f4bd8a8417292cd2a2fd622b052fc5f138598afa5e803c6ca563ef0a4a", "255429219b8d65d45fa1a14336a5182581575dc2a7de1d95dbed76cbe9bf7c1f", "10de7fc110deee3d7bda0e9a002f45b0120c1138a24c9e34174a1620cffec334", "717a80d25d137189b3e823343dd543ebf17fddae65c6604681c3eb38fee0d45b", "ed89c6972c79bdc92d96cce42fea8ff0f36e5ed6e1b94dea505ab2ae54837f81", "cdc64749b89917debf05bb2cdbc09c1eae613a35dcc9a5b05e91a4dd9beb9e40", "68b887840daf853f000aa7395bef2b514e632b64b7454f5ef125c6f2dd5c6cac"
        ], 
        "a": "c894edabb33886b6e70f2bd561a95dacddac7560db449eb42f407fd889a42604", 
        "b": "6662b9974ffc10b3d56b217b292500532915db6cdc565f3e01b7bc1198ca1b07", 
        "t": "e6a42c70ff73eed635ee32226cb7a1f076542a6029ea3064c86f2246f7202a0a"
      }
    ], 
    "MGs": [ {
        "ss": [ [ "66a36ca89eb7508785885bc25b59ef728a8b6140484e1d4f6d79e88f3f967608", "789f7384ee086a59c16f10f791bf89254b91d4aa6b8cf13aa255a87d7853ad0b"], [ "38b011c697a0d01ab1ef8d5d71d8cc639803fb54e7bf4d3d4ff630e261131e0a", "9600d8f20826629f7aa51a1eb5a2b158a69d2eab4cc14ce2e7ae84873c9f2009"], [ "0fc449d0337b9306a9f5bfc16d0aeaf86d64382a1540a37be3f502eab3312e06", "9d02089bcab094b783c93cfaa11ecd46b0fb77120d291248e68063668418f702"], [ "ad86188f74a3a24f23bea856ad29a3dfacdcef3602cb1b71ae4e4698f889b20d", "d638b1f5ea2217129d2570fb8b4d1c6d26887071bb53df5a1337234819eed708"], [ "7f213bb46d5e2cbcbaf28f38d51045c98c28ca89e0267405751d9c95689c3b01", "0150e76ec8e02bcebda230f2ed6d48d01e0813bb2c69943d6559f4caae842700"], [ "070ec3cc850430c24a337586ee135641b0e1cdf0b080e9b367b1b56188855c01", "a53722e179f7c81c62b701e267ece5107b64049858cddff2eb357f1538254600"], [ "fa8adb2a03c958530b5aa000661ed401552dcb982b8612bd29a6d769f33da900", "4d36178b60df0c66cddfc4da63a387008b817798ec921f792d55fa2cc243bf05"], [ "e73be957d9d1a9edb64d9a2a0ad8c45a2dc8bf57df918135c14e5bda7a1fe80f", "fc1418c8810ec45a86d85b93fe37225e8a0cc0270dd419936c87aceafc3df904"], [ "2f24aec76d119c63f0999587e01d44b35a491374d695244795c9bea24c72ea01", "4c8c03981d09ec7f8f3cafb24ad924f030cba338228b41202e5d6c667b869305"], [ "4269f2388cf8df0e6e16dd21e1faf678cf054c0afeb5ff7ecae08da94cbfaf08", "1c056614f93cbb293901d471445269ec734f83a8ae873261784be49a0b26b50e"], [ "7776a962e178b705a7adf906fe9ce9352ac71e244eca2251cded68dceab3b708", "84ae134c365183755e481c9ecc5d2f8628da862b69d2d34cf65d792e82359b02"]], 
        "cc": "780e9d86ab84a33132b60e7c064d8cec08ba9b2e9523030394b3351f583e2300"
      }, {
        "ss": [ [ "0dcfc3735ff7858080bc4f56da65781b7a7e8a4c80845378fa429abe24a3940b", "7541830407268db582e7bba9f0f59c4dae881305797f95fdf6e94b589c7ff50c"], [ "3554dda0f674d686459475ede755f2273339609f2fc67f413985dd861dd3800f", "d99b8eb9635a88c2793272f260f4c0088678071bfa2554010a6caf1e058d2e04"], [ "1f6626ddfb9c7b1a8401e866f687af2c4846d02cdd9a006043ef8eae471d180a", "49a995f353f415bc3ea15a015c2c5cc70f759a1ce8963789b3be8ee9ffd2f60e"], [ "59252073d000e655ab96470c8e2cf223c463ebd1f0e99132102fd5c58d7d1a06", "57d97d70a8c65f5c4d6a527e112ee9045ba257e07fe6691d08c80846285cb706"], [ "903bc32895fa519947ac50495cb479fa7d9c811b78f2c3d8ba3ce5e3b9a3df07", "cce5063e72038da1e79a947bc7cc53fb0af1f456999c3074758d6adc57cec50d"], [ "740bbc966c56c02f6db710cdfa41618893cd00e51c9ee07c7b56ba7e52d25d02", "43d8a15052ba73675af00d2a9049164d75e5b17ef369547cccfe712f0ac69606"], [ "99472711e897afe1b08d30ba101932024f1f45a470e91b2598bfc4304d212407", "ba961bb62e592775d55e4ad6cb17a848053ee19bab151f77d47333155537060b"], [ "f4c0cbd544ece868974b9caa7e633ad66e4323190a54e583bf91a5dad938e00f", "656f3420f901a5da2033d2ef5491e06415f3b18d0ec4c3d9c9ca9159d70b9300"], [ "5208a29e3b984120659ea0658c836632a45c19c37afff72b7b3162702a0b4204", "c17dab1c9458714a6fc57b5fd9c6608b3ed757e83aca21b80deed086aa093708"], [ "ddefb16279e697363c08b9220f4fa615db6cf88e3ee327c5519e1ad4e4c9300a", "caae0a08eadd40fbd253c8d72f9b5eb99aa33f77887a0780d584e52db2186a0a"], [ "142958d8b019aac6d15d81d2d411d583b9713f5494650dda3b2e1a95d5ad560f", "c479a71bf601412eaccd89f7dcd1d62d64e3188323b0bc4ffbd4428ee9d74105"]], 
        "cc": "f78acb0208cdb4697d9e35444839bffe3c958fc58bfd99d0d384ba47b3438b00"
      }], 
    "pseudoOuts": [ "f191c415b3dbd58e4edd3c74e76c6f85ea1dcbc8a4a0dd668a0c65ffd983d554", "bc1cfe64bbee82907c9eaa26981c6123bcad377421e530e93fe60e3b365f3269"]
  }
}
2019-07-01 19:26:40.877	  0x700008beb000	WARNING	frontend	src/wallet/api/wallet.cpp:410	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x600000051800), parent's thread is QThread(0x600003f7ca40), current thread is QThread(0x60000322b450)
2019-07-01 19:26:48.977	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Receive.qml:169:39: Unable to assign [undefined] to QString
2019-07-01 19:26:50.150	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Receive.qml:169:39: Unable to assign [undefined] to QString
2019-07-01 19:26:53.251	  0x700009c7d000	WARNING	net.dns	src/common/dns_utils.cpp:568	WARNING: no two valid DNS TXT records were received
2019-07-01 19:26:53.860	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:3332	Failed to request output distribution: no connection to daemon
2019-07-01 19:26:57.096	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:26:57.096	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:26:57.586	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:26:57.586	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:26:57.856	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:26:57.856	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:27:25.042	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:10058	{
  "version": 2, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 0, 
        "key_offsets": [ 4063346, 139407, 4997057, 710463, 855183, 345366, 6550, 5948, 1483, 209, 3703
        ], 
        "k_image": "a2e02d0b4b46d8e43c5c27b5986d491079cdecf43dc5104b8253fce1b7b504bc"
      }
    }, {
      "key": {
        "amount": 0, 
        "key_offsets": [ 5751296, 1232158, 2540784, 618968, 622026, 159538, 196014, 10960, 1402, 1881, 809
        ], 
        "k_image": "a1d87959e8dca258ea3fe588adfa97c9441c37758d2fe71537ac5e023911d319"
      }
    }
  ], 
  "vout": [ {
      "amount": 0, 
      "target": {
        "key": "c122402ba1274ce4644327abf008d8d6ad67889e774189dd807cb22f388e2ce3"
      }
    }, {
      "amount": 0, 
      "target": {
        "key": "df129f7727ccb3a7e8e5eaae294d45e3a60de16f8b5a7cfa21cf6ded41cce510"
      }
    }
  ], 
  "extra": [ 1, 104, 31, 74, 124, 123, 78, 73, 92, 204, 47, 164, 208, 23, 78, 187, 236, 188, 135, 31, 64, 122, 83, 186, 234, 47, 28, 60, 13, 242, 237, 68, 67, 2, 9, 1, 106, 64, 243, 18, 83, 57, 235, 44
  ], 
  "rct_signatures": {
    "type": 4, 
    "txnFee": 45530000, 
    "ecdhInfo": [ {
        "amount": "22869d4150755121"
      }, {
        "amount": "60db5b5b7f8a6393"
      }], 
    "outPk": [ "f30e39a78c024ba729a2523e56c333dcfc6f9d06572f846b97cd3a434d633afe", "9d77cfa34b2f6b51caca75124b3f6e0fe3c3a832be7ad968f65fa3153af43f9a"]
  }, 
  "rctsig_prunable": {
    "nbp": 1, 
    "bp": [ {
        "A": "4d372e2175fe3b2cef38a474bbaf8bf80c0aeadcc1bef8a278ce3ec4b9c62b3b", 
        "S": "928d81f5406565f40831f9c8d385d197d8c363d7dfe12bc3df81987fb71ceaa9", 
        "T1": "6f8f4750d8618703bedf4066ff0e097f294617cbcc151932aebca2edfc78eba9", 
        "T2": "09794c90e6f778860ab793e55bbfab81c3cdfc43eb7e6d40cbb10757deaa5039", 
        "taux": "715f57ee2adc3089563580ff898f641cd0b80d3ca1885216ce0abc3963b8b10b", 
        "mu": "95f992b68ece4e44015303316dfe9d11460e9675059a16438bbee47ffcf3280f", 
        "L": [ "988c235f106ffe690dbda2bdabb71555ad7e31574fef48510da73997b2dfcc7b", "4c781455e3de6b6f07b1e0d8d95987698709b5bb5a02ebd265640c5810c1b6d6", "26f8067be53c2c0c79adb2ecbbef5ae43b9184b1cbc30baa3e13754bd67b26a6", "330baee0f7535c0061fd004603945537927c04fe7e92c6214860388c3510b185", "da26b559a13d612d7e1e10d7470e5c3c1b964ec4518f546b3cf881f4c8ab48cb", "d5ddae641045a16043a20c7a92c9a0274a95632263636a0911c019a2c68f4ef6", "8fdbff99e595a2ea112b419add019913f9516fd71934ea2983a7efffa41552e6"
        ], 
        "R": [ "1d59b08d5e907de68974185d0f741ae135cb465e62fe1234204221f1f93be7ee", "3b2af2f14cff71caae01b1ed532bca69f0643c6014fdf0be6bb5bd74e1d855dd", "177f3a28b3ffd0bd5bf6ab22c4208e28970a8d0673ca8893624ee943f4be8bed", "3d8e64f82d6805d9b00417796eaa46e55094af0f04c23ca10550bffdd6008fbf", "328a9e895382da8070d91e02b36e1a2e9f85f5144f3227d23f183cc460649693", "55354633631be9b3bf4e34b1986ba1b8f154fc8d792842a7fe26d3e159e3d745", "d96289740cdef34c3766ac155986740b099504061c1d9538eb17c73d0732a723"
        ], 
        "a": "260dd2c82464d8b3787765cc3db352e3bbd171e06225f4bc9d8f2de0656e9100", 
        "b": "8d70b8064baece038cfa552a1e4dc2b0326d426099928f2e1a46f7b1f80e5109", 
        "t": "c1a35ed1f91228ff4856f291af4daaee20c6a44c43cfcf56dc9232eb5277d60b"
      }
    ], 
    "MGs": [ {
        "ss": [ [ "522681b79d3c5c956e27b43ae164906c2263be770ce21e045c50246d6095f90a", "bc821f1275debb3c00d61a04c8d10da4ec5adecf03eab1a4bb947a158e85550d"], [ "98efdc271ed5b412cef1797e3f8777f5540fb49f683e3fba43450f31d9bcfc0f", "c5e51a39fde5be1c3a4685ec2ddaf8ef7fcac0eb45e3b0bff3954f96a8ddea06"], [ "8b63c77c5da3cde124da7e9670c56f2418a521bd9fd2d695ba91fa9e0b8f0808", "42371e383d7d0e7121a9f7a16efe68479c42e07d4f1c814edbf9549b37976f07"], [ "3ac7db302f4d839f8fc92186a904c3d3d524e3351ad7d8743c138ae0dd48680b", "98d14b0ccd8fdaace4643273864e211264db77e7ac3f0a0406e5a07272fc5e05"], [ "3bf2d32c9a46c91a945e8833a3bc1a691241790542674cc237f24b8d4afeae07", "d8c29a801b8493a704d225a556c002014e94b5db3e3bd363e7514fa5b5b6860f"], [ "e11e70847b504b4f1ceaa9b4a2cf21a5c9cecd854a683a8b8b6aae6955d67807", "286bf2cdd4f8a184b43f4090432b36c757970cba555838055b591294f1cdf90a"], [ "203f7d3b3a350c36eea3b3332a1e0945db51aaba933107518204067bf3429e01", "5d34457c4a5e190aeba7152282424304657c2d26a9ca6eb8d8e0e00df5c5c20e"], [ "4a67c127d417fe82d306c16c7ed94100bf6a58e0354eff6ae98051d099e83309", "3cf3216a338d0fc7a46adaa8a41e9d3344497b18f6721cf021c0aa4da55ebd0d"], [ "ea81ee41e8318b87d3bb1a3cbdca53d52e623dcd8961c0d3791333d640f58a03", "afbaaee46a92367a1c0ad4209741f063dc6ba65e0485a968f78fa02191a95c00"], [ "be1d63f706af4472c3e3239513cb2fecfb53816755e47ccc05c6111e4f1d1509", "f50ba2865b162568cfe28db7bc2475dd9948da8f82bb40239865fb65804bf601"], [ "4145b872c50c2d1717762fca84273d9da7879cdd0584a972fb7f08c4f787120c", "07e49f6454e2be0dedaa3c76b65b15383d84c9dbde0448d0db08922cbcd9b608"]], 
        "cc": "d6fb5a018eae37189f4b31b704dcb4b5400adaa2f88c4bcbb1f907b50decf102"
      }, {
        "ss": [ [ "c23a69b01c18e49878a81b64e87334d3d98799ae9de50c0afe2553267ac8aa0e", "8a6f4612bbc978f6b071138a1b06d66aa888d50af2cf416ce902cda7f3fb5b0c"], [ "60350a0c0ae39df0094bc1821178635b95c96020d6bd5736cc41a17e767e7402", "794b84519d77766b794f18fe7ad3ca07d666c4a19d5c909470d78fd90189960e"], [ "89456446431b6a71f35ec08a929ec3c3c37343f4e9230fb4c6c0a58e13604402", "5305614dbeacace13c5f63b110335d242709daeb8961855e4cedfd55cf963003"], [ "09403819437eac0b43e52cd7f556eef541e5d5be9686cd0837661898bf5d620b", "721a5f5a3e0c099141ad416f35dc72202d3344cb257547eccfc01fa4afda7c0b"], [ "9780d8083055dac4fe490a255fcd5d50374b9b01ea7aed996664a60975eb7a00", "7cf8eb2e6c373d34c99078532f1de05a2d658b9597aedcd3d421b76e2903e705"], [ "afa005a3a03b923c58b21ee38c8df166f813f082fe71c9cb5c8dba7fae1ef506", "906f3d6a135fd32460614a140fde1ccfed78c0d81b52c523cc989366bddaa70f"], [ "951168612ec8614fe093ce87727d6c6860521f983d30a45640af22020f210307", "df7f92f1aab12a1b0aec7f10655e5d203967f91149bd7ecf62e94a6e78d90400"], [ "5d73330346988e03408f97fdd7beb865c6977b13077a5f612b9b3273e594bb0d", "804d71e0dd365a4036e17ae03334acffab2ce40fb0f6244bd416e84316e2e50c"], [ "93fd3ae0995221a039006ab9ec23dcf4ddbc41e1c10844c22017dab6c60fd907", "c27094d1d387a448fd265155e5e4744aaeef810fe238b229745ac28c7c03ab01"], [ "fb440aaf49dc5ec32db81ee31249274f0a881638cffeeee988786eee6463dd01", "fb1c11c49b9e8acc793013a6833c8b394553b2f86a3063d5f54f37d03b3f720f"], [ "855b20987153ab28fc84dff309ba63bfe6f986d40af394debb2041592285be08", "fedd55cbdbf2432eba6c97d2ab62803b40379dd09312eefb4ecfa7a68b3c6c06"]], 
        "cc": "1c58ec1959de12b10aeceb2fe43d60a4be33db2a104b7be12ea5798525ae6005"
      }], 
    "pseudoOuts": [ "80ca2eb767e9fe6efc7cc03fd30b7e6e6c607179497059425adf5641c3302500", "6679dca22a6c52811a2b0094f35b46ebfa91786991117f9ef74b636963c4e807"]
  }
}
2019-07-01 19:27:25.042	  0x700009c7d000	WARNING	frontend	src/wallet/api/wallet.cpp:410	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x600000051800), parent's thread is QThread(0x600003f7ca40), current thread is QThread(0x60000301ac40)
2019-07-01 19:27:25.856	  0x700009d00000	WARNING	net.dns	src/common/dns_utils.cpp:568	WARNING: no two valid DNS TXT records were received
2019-07-01 19:27:26.018	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:3332	Failed to request output distribution: no connection to daemon
2019-07-01 19:27:28.211	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:27:28.211	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:27:28.223	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:27:28.223	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:27:28.234	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:27:28.234	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:27:29.619	  0x70000895c000	
2019-07-01 19:27:41.893	  0x700009d00000	WARNING	frontend	src/wallet/api/wallet.cpp:410	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x600000051800), parent's thread is QThread(0x600003f7ca40), current thread is QThread(0x600002f38000)
2019-07-01 19:27:41.902	     0x11223f5c0	ERROR	frontend	src/wallet/api/wallet.cpp:414	Can't create transaction:  unexpected error: Trezor returned failure: code=4, message=Cancelled
2019-07-01 19:27:43.397	  0x70000895c000	
2019-07-01 19:27:47.995	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///js/Utils.js:115: TypeError: Cannot call method 'match' of undefined
2019-07-01 19:27:55.363	  0x70000895c000	
2019-07-01 19:32:20.917	  0x700009c7d000	WARNING	net.dns	src/common/dns_utils.cpp:568	WARNING: no two valid DNS TXT records were received
2019-07-01 19:32:21.746	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:3332	Failed to request output distribution: no connection to daemon
2019-07-01 19:32:23.720	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:32:23.720	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:32:23.911	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:32:23.912	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:32:23.923	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:32:23.924	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:32:23.993	  0x700009d00000	WARNING	net.dns	src/common/dns_utils.cpp:568	WARNING: no two valid DNS TXT records were received
2019-07-01 19:32:24.155	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:3332	Failed to request output distribution: no connection to daemon
2019-07-01 19:32:26.148	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:32:26.148	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:32:26.161	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:32:26.161	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:32:26.174	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.012000000000, real_output=4, real_output_in_tx_index=0, indexes: 4063346 4202753 9199810 9910273 10765456 11110822 11117372 11123320 11124803 11125012 11128715 
2019-07-01 19:32:26.174	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.h:2060	amount=0.014000000000, real_output=4, real_output_in_tx_index=0, indexes: 5751296 6983454 9524238 10143206 10765232 10924770 11120784 11131744 11133146 11135027 11135836 
2019-07-01 19:32:55.758	  0x700009c7d000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:10058	{
  "version": 2, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 0, 
        "key_offsets": [ 4063346, 139407, 4997057, 710463, 855183, 345366, 6550, 5948, 1483, 209, 3703
        ], 
        "k_image": "a2e02d0b4b46d8e43c5c27b5986d491079cdecf43dc5104b8253fce1b7b504bc"
      }
    }, {
      "key": {
        "amount": 0, 
        "key_offsets": [ 5751296, 1232158, 2540784, 618968, 622026, 159538, 196014, 10960, 1402, 1881, 809
        ], 
        "k_image": "a1d87959e8dca258ea3fe588adfa97c9441c37758d2fe71537ac5e023911d319"
      }
    }
  ], 
  "vout": [ {
      "amount": 0, 
      "target": {
        "key": "233baf05ca5a6a728a482d73bae6edd20ca5a59d6f597fd771dac40e50163d8b"
      }
    }, {
      "amount": 0, 
      "target": {
        "key": "fbd8bcdfbf2c1bdf0427a940ce9844836174e52c120621c8ea9c783d3dc089b9"
      }
    }
  ], 
  "extra": [ 1, 4, 38, 46, 173, 48, 136, 24, 188, 26, 221, 81, 210, 210, 47, 40, 30, 164, 166, 26, 130, 138, 118, 190, 39, 105, 188, 99, 108, 211, 73, 79, 80, 2, 9, 1, 177, 21, 231, 2, 111, 103, 83, 157
  ], 
  "rct_signatures": {
    "type": 4, 
    "txnFee": 45530000, 
    "ecdhInfo": [ {
        "amount": "a2e56dbb6d64ecfc"
      }, {
        "amount": "5854143b18016316"
      }], 
    "outPk": [ "d6c7ea09ee17d99d855ce52698f9f5681d2458aaebe57c36cd68eef1abc4de20", "680e49981d27f530d6b832f5925fe6f2bd8ebfe467d6958e5f912ed5ebf91a8a"]
  }, 
  "rctsig_prunable": {
    "nbp": 1, 
    "bp": [ {
        "A": "9a06193a8b79e05f8fcf9afb3430f542e0765a1ffa91c118fded21e7b9c2452d", 
        "S": "247ae60ac0d9b215a1ce9e4f81993c0dc3d2997de6c30cdf6373468b47516651", 
        "T1": "21abd8d9676171b8691f66b93fc42a8c9380e7f52c81a6f07a7f4d5d7e2638dd", 
        "T2": "85a85e37f0dfae670776cf637ee76d7c2257954aa82b26b8100bad229323e642", 
        "taux": "e9db1e16e480d4e0e5d198610f88e1cce3b7cd9d024351149119f05265c6280a", 
        "mu": "22bb979cbdf4ba878d6754355ab2b68173bdc29c7a8df36dc45b4518132b2209", 
        "L": [ "245588ec22889411d6eb47d370b7fffc05aab29418b2fe369c30f09edb47ff49", "1095586bafc985394aa4904adc3d7f1c0ac52ec687c3921e035db828af94a944", "01ff8be017dd6614a47e68773d07fdd9da0fb2d7e41f9b78bbd742b190d7cab9", "2d3410521e9d82b0c52e79242d3b31a84f1351847b319865698a1527b1da8150", "c27ddcb38ab9112e225bb1102d5abd27b54c41d00db59f214a1bb975b9ff441d", "8659ce9db728b4111cf928155fc7efb64a5a7ea180ca50f3530170f2dcd4d4b5", "a026d72386f9f522bb180e6eb256b04fabf4e168ef1281bed334279914096429"
        ], 
        "R": [ "8f708b78ecb0e30e4b161831f0cf76a88a20e8bb3e287c269a540dbfd27ff7a9", "25bd108ac58da8220e3b8393842341ad226f3b02a5be14773b27a0cf9a7b22db", "a6dfb92eb461b08232d998caf9c9e44980101e9d45fb18929eaac631be3bd47a", "bf1f4c1049a7350c38f5259867712b549b0fabdc8532b04300bc3f1194950d6f", "1e85cb67639da3edd531b4e5185e2940317cfabea04262e69f54f124809751dd", "3b5f8bede24fc26cad8422856b2788f41982dc3350d5e86010a1beb3dab33376", "563800a0b19503595a29bf980e641a029ad78e3cdfd0c6fd2a4c1cbf95403eb5"
        ], 
        "a": "9d2dae9f41dd57f82d746c8004dbf7af35abaf2171beb849aac78cfe37344102", 
        "b": "cb3aa47bcce7e418efa9824d96dc27a7315f423a8a8b1b64d1ef870d5c29a80b", 
        "t": "0d8562a9b65c580637044a4297f4088bca4d4e2c931aa15b873a3aa6cb8f2002"
      }
    ], 
    "MGs": [ {
        "ss": [ [ "7092036efebf7fba911b2541c15750987e6b044ddf2b75432eab06ca6fa57705", "6ec702148ad7473cc4a28247af78e72bb3443a8fc528885c19645cfbb5d7f900"], [ "0659937eb662a461c11f37a495359248e1dfe83b5acbcdf64daa86d8c374ac06", "031204761940ea41d720591ed1efbe0097a2de8758caa20f72e98d38ada57304"], [ "b2399f5b325d036becac6bc58873b956aca0240a11722b4bff46d6bb8c261806", "4c3b60f5769e8864e8d7e3a064eb7bc1a2117726f288c8f54a1dacea54a31001"], [ "9e27950305c5223fc32b61b0982c76977dca2d0d4b1a239f8f4672d8903b6104", "b5198b238c5473b21132092b0d5eb1706b248c2e8a73a0163eb402671d0dab01"], [ "807da54c4a3b3c986f4395a34a89b6ad3d9c7ee964085b4f5005ff7c0306a50c", "828bec4903b3e87e0cde930bc48f3f2cfef76e39ed4854791a90f51ca9111a09"], [ "0a1dca3b0762ed2893034037fc5914f287b52eb7231495e48aacfaa2a2b82609", "861a4af5726d4f18bb7e135d99cccaccd687660afb01ba79f72dfcdc5ccc520e"], [ "08ba117a7c2a2ccf95f6e5da97ac0fd8cf2ca5f5ec533facdd4888ea506d6f05", "f2b85492b86534e888c6dc15551673e772f38feb0c88ae6344dea54eace75b04"], [ "af82764c9e8ad8695112816a12930632f928154b51733df7368a37be7ba05e00", "04ffa9483d618a2ff41ec7031b93f233d17746267f8b31daaad99815679e2707"], [ "847f22bf9f30c30d5cfd333257061d5b1288eb54173b3436e5671c3afef3c504", "45bf9f3dac18b9697f68778eac1249dd797ea21034e5cd3cc6dde12027d23d0e"], [ "54a969049dff20368b31cc91266babad4be49be5f43bf1a352033bacb80e5c04", "e978bd5d616555a2ae3fd264fdb70c9c649d2da2977685ec99aa5553eb4a0e09"], [ "3b20576b0774a06dd45d6dffdd97e498cda3e6c7bf29c54e4e0632879edaf104", "e82ca8dee11b13a211d2d4cfa1de0c96c7b36b9db4f3d28d662a443b34e49006"]], 
        "cc": "fbc36b058859888d693e58ccc0efa3fd519f654ead4e714d33c0b8977fc63507"
      }, {
        "ss": [ [ "766186cf75448130227b83a075b6c75fdf2a456e99c538796e813c42b265ed03", "869935350271f49c6048b026b645f052d8cde5ee63a36c9d35c682064fa68008"], [ "f85e0215298c8fa1ba041b860651bf1952a6a2a8103b8e35e29d20f2990e9504", "4e988ac4010a6f2a5a9d0d97378f60c294f98b988e036099ead255b0c378a70c"], [ "20b9731a08306bb0bce563e8c9a6a33af6739a54f7a265aa2de7f51574eeb402", "9d66ef4377fae6d55320ed02e6a2c4fa684168e8e4b0c359a7dcc2bc56a42300"], [ "da7296cc59031ed6af858915a6a0ba2eb5e1986963216f87884dbaebd1ffd201", "c6b2a5036c6156c8d664b41b95beadb04686621f719aeab497825c6b40a8b809"], [ "fa20c4b55f90666ebf6e9cef90e2a677e9e89ac45fce3edcc6a912778f9e8709", "b64a940acacf52cfdabb6e356830b9c7cf3d946ef80f6329cd4fe61ce4017a09"], [ "12a1115916cfa34e11be3ffea812ce8045e7bfe47895b7c8262221d85c3da203", "708f87a66bc3702d90e08ed703e031b3c056973c77a55ec67cd12c2db605f502"], [ "dba158eb66cf7fc3d8f9d57495441b6ec6bea896bc26bcf8a47547f724dada03", "4c852650f3e1d490f35b50e46d119bd378c56ff4664a408b67a4658ca1e77609"], [ "1f5f6281fb297133aa76c2045ef10b53186393bb09206b70ada58c28f0f12f05", "c2f7e56518d60b75113d7af3c539edb6aa33ed100bfa4740fc07e21acf62560a"], [ "ff93e5890c8b0530733b7fe2fc31809d2dc2fc3372ce1e7d703a6de59fa9e606", "4c4f5203442e240c508f10408feab11b501fbcbaafa5182d7564f3c81a04ed00"], [ "d58b35d5da7d737d5aa7f0264d922048d45ca888dd35f3c941b58b4994939605", "4186fe4f65ac8492ad8e956b5d2820c75924d604a9217b1a6d1c333ebd93b20f"], [ "f2c238d4c4c17423e64c38b1ca931a84623496608a33ce206c763e6dd49fb60c", "28d81b39874b2353b21328f6dbe4a78b0ddc16f476f693fd3ee452a34e14b70a"]], 
        "cc": "1dede48abd931247e98f50d40525c021e842f5651adfdc9c5660c6ea62d8ec00"
      }], 
    "pseudoOuts": [ "f152030b33caf75db8af8769741f24e3ef4f3949727cae27dc46f220b7adc5ac", "2c2543bc1786e9683b4634f4d952331a8c471344d21ba63b845328a17df36295"]
  }
}
2019-07-01 19:32:55.758	  0x700009c7d000	WARNING	frontend	src/wallet/api/wallet.cpp:410	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x600000051800), parent's thread is QThread(0x600003f7ca40), current thread is QThread(0x60000301ac40)
2019-07-01 19:33:31.217	  0x700009d00000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:10058	{
  "version": 2, 
  "unlock_time": 0, 
  "vin": [ {
      "key": {
        "amount": 0, 
        "key_offsets": [ 4063346, 139407, 4997057, 710463, 855183, 345366, 6550, 5948, 1483, 209, 3703
        ], 
        "k_image": "a2e02d0b4b46d8e43c5c27b5986d491079cdecf43dc5104b8253fce1b7b504bc"
      }
    }, {
      "key": {
        "amount": 0, 
        "key_offsets": [ 5751296, 1232158, 2540784, 618968, 622026, 159538, 196014, 10960, 1402, 1881, 809
        ], 
        "k_image": "a1d87959e8dca258ea3fe588adfa97c9441c37758d2fe71537ac5e023911d319"
      }
    }
  ], 
  "vout": [ {
      "amount": 0, 
      "target": {
        "key": "661c8a793401c4ffca6dbd62e197ce8457e95a1d7d6ef7c0ac4aa2cc9eb84182"
      }
    }, {
      "amount": 0, 
      "target": {
        "key": "dea7d57e089a4ab965ee26a60bb0d3f4b9d065ef0d4dfc95314a34b2cab4e89f"
      }
    }
  ], 
  "extra": [ 1, 219, 13, 115, 48, 212, 219, 59, 107, 213, 42, 51, 161, 209, 101, 18, 100, 189, 235, 251, 103, 29, 105, 76, 29, 188, 142, 26, 157, 27, 89, 111, 232, 2, 9, 1, 229, 228, 253, 166, 151, 80, 47, 39
  ], 
  "rct_signatures": {
    "type": 4, 
    "txnFee": 45530000, 
    "ecdhInfo": [ {
        "amount": "e63e4bcc1bc0a990"
      }, {
        "amount": "9a68999772609c64"
      }], 
    "outPk": [ "9ab1705e64d0ac0777c3901610c08d5c44be58c73cd267eb3cb12ad3f3546bc0", "9b8e8f97c8ff94660fc8727fd762526611a841ac58605acfaee64e868980a0b8"]
  }, 
  "rctsig_prunable": {
    "nbp": 1, 
    "bp": [ {
        "A": "b950911242ed62dc87b9b45171d297d7ad86601402b1f481b4e7d61a1f584207", 
        "S": "741166b079fc2645624ea9d8c67ce0fedb4e2917639fb7087dddafb9d002eeb4", 
        "T1": "e6fe9b9e30f0c14b034916c79014e43a3430e867f597f9121e372754511e4df7", 
        "T2": "bc351f645a3d9c2e18bd0f5e0b491ea2311a8fcac231a979b9e42bcc7333eefa", 
        "taux": "4cb1e93e8e6f2646b0485bc83a8cdfafe0e58ec75f41cb1a7e98e06a8e408e0b", 
        "mu": "68a988d94fd6f0edf81195187e91c4344ea6d8b630559540b405b24b04859802", 
        "L": [ "3edf7435caedba7f6e5c5a21505cb47356404b5df2205d9dd2596f46fe9db866", "b784b05fe10e03b4ca369ce1a0f1d388ca3e26d211d17015bd8fd2bfbcfc32a3", "0d64efd2d5b8af8924a1fbc861ebc1ac333b570f8089ea31b41dc84d745da452", "53237dfabf1d325c1e946d580fcee0048e04273129c7e9732b34ff4852c4776e", "b6c84505f56841589152c37fe6bae03d1c2aea5e5c1f8de05e0588f53c93637f", "e806935dccaacd77c024163073acf7e201b707784350fcc8f11cfdb592aab802", "41c94b8fb39dea8a5aa94da00325725e58c5f68dda06e757900fdcc99fdc8939"
        ], 
        "R": [ "863d3704700f82d40d1e6882ed06a664a5c92cb4828ddd581da1039690be7833", "7ac88ae63469baa69e7497ff0ef6b079090d69e2a04f467ed3f82eacf065abbc", "a5cf838d440454ab2c9685466f3d668b2fbcbcac105e5b6e2414ae9b21bf3f80", "0943e5bc8ce2360f0ddbfa727ab27bbffa36332c78479091ea67cb322a6c59a4", "3168ab518fb2e55fc26a1eb9d7be168601257b7ec2dd8e725fd7a9bfbae476cd", "786f96f91af11cd5afd5fdc090f419906b21d6244782e33b06ea73494e1fd9ed", "3be20cf47ba48a10905b3a18af1984545061eca789744ca5c7e67e52edd94dac"
        ], 
        "a": "d6e49093845e318ccbdf699415180f00218d74e7f17edd1697b341e6fa349e0c", 
        "b": "483a913ba107e919e907ef800c09d499ecfa9e58ecc176f39a463f3a4c299a03", 
        "t": "ccf013711dff09e883973236989cd1ac74771bdfb7bc64072224b44a37566a0d"
      }
    ], 
    "MGs": [ {
        "ss": [ [ "ff0c4a9e313bd14295262f9ff6be9f402792617263b9824e41d60c5e6b762104", "cc2ae66c1865e1fe4c9a4d493c1dbd152ebf98bc7a862d423f398558f833fd0d"], [ "037f8ef8defb9935c0a19285013ddb09bf609bb2872f4d6b5fab740898cd9d0c", "75162a69e777019906833d1811a0751c2135bc4fdc7d6f5988ae22fc34ba0e0a"], [ "c6ff40119a6df3b689c06be1c9dce6b28b1503c1e6517272046b0d739ff0cf0d", "04e36a126a4aa923200fd8e1cc6b92599b80d74b4672c11ec5bd7461cf24b70b"], [ "26c602590bc07f1d3d78cf01bb93612477f59a694bbfc6f4daad3a4517c4d20b", "6f034d123f57447b4463fcd26304e01f982545988a205fa9ed2f78e3915a410a"], [ "914327ec02c6b02966e716abd1d9a576b8529386bff1da7af5a1ec71aba6e102", "fc47af8d46dc91cf5931daa38f0430a1323d3db6d1f701ebdaab91102335de06"], [ "27378f55927e2294bf26ac2e3b5e7419e4de0dca53b5bba2e29c3bb2b5a2290e", "57b85f2b94262b5b181a685f64873bb16a6c4419817f9ad3d4adcb30f8b69202"], [ "6479b1d5a2507b846aa578884adb51116611f43e1e84048ce072325f0ef56100", "4ba28a063698f309da498842672eeb39f8e843a97fd0dd906e42be2346d10308"], [ "e5e1695a75a53dd99bfc23f15af48626576a26335c370516e7ecbe124a949f07", "350fbb4f61fcd71863bd6fd9ea7c5c8c39c901f90b29561ef8c065abb9867a01"], [ "6dca829d0c7382e44b28436b81313b5321d4244f7ae8e4b1c52b7101dc33a90b", "021b95931f7806fc7e6f133b8b1255237ba9d9589512811920b692cd818e1c0d"], [ "ab8f6dae7d4a0d15536f7f06280c96c90504ffb7f540239360b2740df658990a", "84731b877a79c41badf262ba35ac6323ce43be9c315a5417ac4501a2e7dfce01"], [ "f60d2553a94b82ba5df9c3eab29b5f1fb79ee84c48f51af26e2d5d3986940304", "4833a2fc3c6650e2e573a9798f354d651ac0009e77ae823eb6622a5a49f62909"]], 
        "cc": "db85eae3bbf205833d18a11fe5b4e58bd1bbdef187a7977103040bd19446cb06"
      }, {
        "ss": [ [ "ca10ddc17097a609f93b658c00f7bd492beecd95e5b4c9ffdac25e93cd733b0d", "6b88e8a1a7cd230d622ab6e59ad75e70bfd75771ee7ca4c6a1ca91e874a5a909"], [ "6899f6268e933e2014fbd49f57166ca7d6190f14bac4eff7f2ea3c6668a4e405", "bf6a5ff0270966a10616f1f84376a654c7c6d4f18b8c1530c2a7235f74937108"], [ "66dab0b7a2a2918bd09121ee4d08573f2fc6ecd962fc80bcfdbf9241986bbd08", "04bff73e69de0241d7f3377bf79d61195085d85aa7c987e79563b34ed9558904"], [ "79102b7fb7bb62c9384cec495b7b99f4e0e4962a9dc17731eaf588b52d436406", "78194a2289ed23714127d7d70c2e9c986fe58fa8b069ec2df2d18bf6443a180a"], [ "d3e4057cb3f4058e84e06479285d6ad19d9ad4e6a0c3ecbe69b38c9046ac7101", "808f80482a10563f66cacff7ccb32c6b58b22b1c2ac2134d0587acca2eb7660a"], [ "cb490359256ef339a77d41312ef3ff459566263ad67ee146b93a3b077a1ddd02", "17b81dabd9098fccc0928255bae476690dfc277c4791408fd881761b1e3fa100"], [ "a7cab883509b5dbe5529e44c243471f3c7d514f80a0b1b59dd95b99910b6730f", "efbb7292460395d824638426fee5555c6fc1b56182c0c2ce8e7f66dc6cbd1d01"], [ "40a94deb762a36c3099707ad197b072328bebc3dc50fb568c2318a8557e8cd01", "17c76b31fbf226f6e7ee0811dec2ebd2809516c6a43a20a3c314b11487cce90b"], [ "07765b0d74c400709fbadb3c3867d99aa28e5eacac3dfdcb40f6f7b927381201", "f43f7ba87f460d6fbd1281cbe16c64fb40fada47842fa72418e78d7c3c203402"], [ "db7a0e651f8abd9a4bdea8508dbefc6819a39e9d79f22b30892d53d979d3bb03", "9f4dd906305c6283304f1855aa925470521b723f7604df53bee447f19139900f"], [ "d1a0fed0a8a21736950258a09df1dcda0f10d3992f4ab80313813bc5cc37eb0f", "d904ba7a616947c3c12ce9b94aecd0d5c3084317100d0ea004096527d8552300"]], 
        "cc": "f85738ef7b6ce14b485665590720c68b513d0bc4f1b4858cdd1634a486fb580d"
      }], 
    "pseudoOuts": [ "116f0aafc4010e49b36cc7d916bc43c4229cca68996d43adcae44e24a6237e7a", "1acca908c0555c54ab5cb395086b7c074042b1262969167556462c6b5ba4a35a"]
  }
}
2019-07-01 19:33:31.221	  0x700009d00000	WARNING	frontend	src/wallet/api/wallet.cpp:410	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x600000051800), parent's thread is QThread(0x600003f7ca40), current thread is QThread(0x600002f38000)
2019-07-01 19:34:59.929	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	Data set on unsupported clipboard mode. QMimeData object will be deleted.
2019-07-01 19:35:01.785	  0x700009c7d000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:10433	!get_pruned_tx(res.txs[0], tx, tx_hash). THROW EXCEPTION: error::wallet_internal_error
2019-07-01 19:35:02.278	  0x700009d00000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:10433	!get_pruned_tx(res.txs[0], tx, tx_hash). THROW EXCEPTION: error::wallet_internal_error
2019-07-01 19:35:08.081	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	Data set on unsupported clipboard mode. QMimeData object will be deleted.
2019-07-01 19:35:19.743	  0x700008750000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:10433	!get_pruned_tx(res.txs[0], tx, tx_hash). THROW EXCEPTION: error::wallet_internal_error
2019-07-01 19:35:19.995	  0x700009d00000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:10433	!get_pruned_tx(res.txs[0], tx, tx_hash). THROW EXCEPTION: error::wallet_internal_error
2019-07-01 19:40:17.997	  0x70000895c000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:2020	Received money: 0.025954470000, with tx: <06a423e96b1d7256f6955a010a9b486a705496997b7046ace24b9e53dcf744ab>
2019-07-01 19:40:17.997	  0x70000895c000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:2141	Spent money: 0.012000000000, with tx: <06a423e96b1d7256f6955a010a9b486a705496997b7046ace24b9e53dcf744ab>
2019-07-01 19:40:17.997	  0x70000895c000	WARNING	wallet.wallet2	src/wallet/wallet2.cpp:2141	Spent money: 0.014000000000, with tx: <06a423e96b1d7256f6955a010a9b486a705496997b7046ace24b9e53dcf744ab>
2019-07-01 19:42:27.088	  0x700008750000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:10433	!get_pruned_tx(res.txs[0], tx, tx_hash). THROW EXCEPTION: error::wallet_internal_error
2019-07-01 19:42:27.863	  0x700009c7d000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:10433	!get_pruned_tx(res.txs[0], tx, tx_hash). THROW EXCEPTION: error::wallet_internal_error
2019-07-01 19:46:09.177	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	Data set on unsupported clipboard mode. QMimeData object will be deleted.
2019-07-01 19:46:17.922	  0x700008beb000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:9730	unlocked_balance(subaddr_account) == 0. THROW EXCEPTION: error::wallet_internal_error
2019-07-01 19:46:17.922	  0x700008beb000	WARNING	frontend	src/wallet/api/wallet.cpp:410	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x600000051800), parent's thread is QThread(0x600003f7ca40), current thread is QThread(0x60000322b450)
2019-07-01 19:46:17.932	     0x11223f5c0	ERROR	frontend	src/wallet/api/wallet.cpp:414	Can't create transaction:  internal error: No unlocked balance in the entire wallet
2019-07-01 19:46:18.856	  0x700009d00000	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:9730	unlocked_balance(subaddr_account) == 0. THROW EXCEPTION: error::wallet_internal_error
2019-07-01 19:46:18.856	  0x700009d00000	WARNING	frontend	src/wallet/api/wallet.cpp:410	QObject: Cannot create children for a parent that is in a different thread.
(Parent is Wallet(0x600000051800), parent's thread is QThread(0x600003f7ca40), current thread is QThread(0x600002f38000)
2019-07-01 19:46:18.857	     0x11223f5c0	ERROR	frontend	src/wallet/api/wallet.cpp:414	Can't create transaction:  internal error: No unlocked balance in the entire wallet
2019-07-01 19:46:27.601	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	Data set on unsupported clipboard mode. QMimeData object will be deleted.
2019-07-01 19:46:38.202	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	Data set on unsupported clipboard mode. QMimeData object will be deleted.
2019-07-01 19:51:53.896	     0x11223f5c0	WARNING	frontend	src/wallet/api/wallet.cpp:410	qrc:///pages/Keys.qml:123: TypeError: Cannot read property 'walletCreationHeight' of null
```

## rating89us | 2019-07-08T19:25:40+00:00
The 2nd confirmation was an amount confirmation request, not a "refresh blockchain" request.

## selsta | 2019-09-01T01:22:22+00:00
Can this be closed seeing that you can’t reproduce it anymore?

## selsta | 2019-09-05T21:32:47+00:00
Please comment if this problem still occurs.

+resolved

# Action History
- Created by: rating89us | 2019-07-01T19:31:37+00:00
- Closed at: 2019-09-05T21:36:34+00:00
