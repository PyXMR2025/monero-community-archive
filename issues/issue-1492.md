---
title: OSX Version 10.13.5 Linking Issues
source_url: https://github.com/monero-project/monero-gui/issues/1492
author: skaht
assignees: []
labels:
- resolved
created_at: '2018-07-04T03:24:04+00:00'
updated_at: '2018-12-27T15:36:30+00:00'
type: issue
status: closed
closed_at: '2018-12-27T15:36:30+00:00'
---

# Original Description
Two points:
1. ```% xcrun --show-sdk-path```
**/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk**
2. Explicitly setting **DYLD_LIBRARY_PATH** to correct library **Homebrew** paths has no impact

Snippet where linking dies:

/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++ -stdlib=libc++ -fstack-protector -pie -headerpad_max_install_names  -arch x86_64 -Wl,-syslibroot,/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk -mmacosx-version-min=10.11 -Wl,-rpath,@executable_path/Frameworks -o release/bin/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o SubaddressModel.o Subaddress.o zxcvbn.o UnsignedTransaction.o Logger.o MainApp.o DaemonManager.o qrc_translations.o qrc_qml_qmlcache.o RightPanel_qml.o LeftPanel_qml.o version_js.o MiddlePanel_qml.o main_qml.o wizard_WizardConfigure_qml.o wizard_WizardDaemonSettings_qml.o wizard_WizardCreateViewOnlyWallet_qml.o wizard_WizardPassword_qml.o wizard_WizardPasswordInput_qml.o wizard_WizardMain_qml.o wizard_WizardRecoveryWallet_qml.o wizard_WizardOptions_qml.o wizard_WizardManageWalletUI_qml.o wizard_WizardMemoTextInput_qml.o wizard_utils_js.o wizard_WizardWelcome_qml.o wizard_WizardCreateWallet_qml.o wizard_WizardFinish_qml.o wizard_WizardDonation_qml.o wizard_WizardPasswordUI_qml.o tabs_Twitter_qml.o tabs_tweetSearch_js.o tabs_TweetsModel_qml.o components_TipItem_qml.o components_PrivacyLevelSmall_qml.o components_DaemonConsole_qml.o components_RadioButton_qml.o components_InlineButton_qml.o components_DaemonManagerDialog_qml.o components_TickDelegate_qml.o components_TitleBar_qml.o components_NetworkStatusItem_qml.o components_LabelButton_qml.o components_MobileHeader_qml.o components_NewPasswordDialog_qml.o components_PasswordDialog_qml.o components_Scroll_qml.o components_TableDropdown_qml.o components_CheckBox_qml.o components_StandardDialog_qml.o components_PrivacyLevel_qml.o components_Style_qml.o components_LabelSubheader_qml.o components_TableHeader_qml.o components_InputDialog_qml.o components_IconButton_qml.o components_LineEdit_qml.o components_DashboardTable_qml.o components_HistoryTableInnerColumn_qml.o components_Label_qml.o components_DatePicker_qml.o components_StandardDropdown_qml.o components_HistoryTable_qml.o components_SearchInput_qml.o components_InputMulti_qml.o components_ProcessingSplash_qml.o components_RemoteNodeEdit_qml.o components_TextBlock_qml.o components_StandardButton_qml.o components_Notifier_qml.o components_AddressBookTable_qml.o components_HistoryTableMobile_qml.o components_ProgressBar_qml.o components_MenuButton_qml.o components_LineEditMulti_qml.o components_CheckBox2_qml.o components_QRCodeScanner_qml.o components_Input_qml.o js_Windows_js.o js_Utils_js.o js_TxUtils_js.o pages_Transfer_qml.o pages_Mining_qml.o pages_Sign_qml.o pages_AddressBook_qml.o pages_Dashboard_qml.o pages_Settings_qml.o pages_Keys_qml.o pages_History_qml.o pages_SharedRingDB_qml.o pages_Receive_qml.o pages_TxKey_qml.o qmlcache_loader.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_NetworkType.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_SubaddressModel.o moc_Subaddress.o moc_UnsignedTransaction.o moc_MainApp.o moc_DaemonManager.o   -F/Users/Scott/usr2/local/homebrew/Cellar/qt/5.11.1/lib -L/Users/Scott/Projects/Monero/monero-0.12.2.0/monero-gui/monero/lib -lwallet_merged -llmdb -lepee -lunbound -leasylogging -L/usr/local/lib -L/usr/local/opt/openssl/lib -L/usr/local/opt/boost/lib -lboost_serialization -lboost_thread-mt -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -lcrypto -ldl -framework PCSC -framework QtQuick -framework QtGui -framework QtCore -framework DiskArbitration -framework IOKit -framework QtQml -framework QtNetwork -framework QtWidgets -framework OpenGL -framework AGL 
clang: warning: argument unused during compilation: '-pie' [-Wunused-command-line-argument]
ld: warning: directory not found for option '-L/usr/local/opt/openssl/lib'
ld: warning: directory not found for option '-L/usr/local/opt/boost/lib'
ld: warning: directory not found for option '-L/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/**MacOSX10.12.sdk**/usr/lib'
ld: library not found for -lunbound
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [release/bin/monero-wallet-gui.app/Contents/MacOS/monero-wallet-gui] Error 1


# Discussion History
## skaht | 2018-07-06T19:22:13+00:00
Resolved:

1. ld: warning: directory not found for option '-L/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.12.sdk/usr/lib' by:
\# OPAM configuration
```source ~/.opam/opam-init/init.csh >& /dev/null || true```
```setenv LIBRARY_PATH      `xcrun --show-sdk-path` ```
```setenv C_INCLUDE_PATH `xcrun --show-sdk-path | sed 's/$/\/usr\/include/'` ```

2. ld: warning: directory not found for option '-L/usr/local/opt/openssl/lib' and 
    ld: warning: directory not found for option '-L/usr/local/opt/boost/lib'
Resolved by using sudo to establish soft links to the non-standard Homebrew locations.

3. ld: library not found for -lunbound 
Resolved by a ```brew upgrade unbound```

However, **get_libwallet_api.sh** appears to never complete.

## BigslimVdub | 2018-09-13T02:52:47+00:00
I get this error. Still can't compile via terminal though using high sierra 10.13.6 after upgrading unbound. 
get_libwallet_api.sh builds gui but it is only 20 something MB not the 200 it normally is. 


## sanderfoobar | 2018-11-18T16:59:55+00:00
Please use [fpaste](https://paste.fedoraproject.org/) for your logs.

## dEBRUYNE-1 | 2018-12-17T08:15:25+00:00
Are you still experiencing this particular issue? 

## dEBRUYNE-1 | 2018-12-27T15:09:21+00:00
Author has not responded and therefore I am going to close this issue. 



## dEBRUYNE-1 | 2018-12-27T15:09:25+00:00
+resolved

# Action History
- Created by: skaht | 2018-07-04T03:24:04+00:00
- Closed at: 2018-12-27T15:36:30+00:00
