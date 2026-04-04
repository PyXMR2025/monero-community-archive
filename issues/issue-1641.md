---
title: gui for armv8 android
source_url: https://github.com/monero-project/monero-gui/issues/1641
author: twiuglufosfa
assignees: []
labels: []
created_at: '2018-10-12T16:06:42+00:00'
updated_at: '2018-10-23T12:48:55+00:00'
type: issue
status: closed
closed_at: '2018-10-23T12:48:55+00:00'
---

# Original Description
i add some things for armv8 and try to compile but no success.

/opt/android/android-ndk-r17b/toolchains/llvm/prebuilt/linux-x86_64/bin/clang++ -D__ANDROID_API__=21 -target aarch64-none-linux-android -gcc-toolchain /opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64 -Wl,--exclude-libs,libgcc.a --sysroot=/opt/android/android-ndk-r17b/platforms/android-21/arch-arm64/ -fstack-protector -fstack-protector-strong -static-libgcc -static-libstdc++ -pie -Wl,-z,relro -Wl,-z,now -Wl,-z,noexecstack -Wl,-soname,libmonero-wallet-gui.so -Wl,--no-undefined -Wl,-z,noexecstack -shared -o release/bin/libmonero-wallet-gui.so main.o filter.o clipboardAdapter.o oscursor.o WalletManager.o Wallet.o PendingTransaction.o TransactionHistory.o TransactionInfo.o QRCodeImageProvider.o oshelper.o TranslationManager.o TransactionHistoryModel.o TransactionHistorySortFilterModel.o BitBuffer.o QrCode.o QrSegment.o AddressBookModel.o AddressBook.o SubaddressModel.o Subaddress.o UnsignedTransaction.o Logger.o MainApp.o DaemonManager.o QrScanThread.o QrCodeScanner.o qrc_translations.o qrc_qml_qmlcache.o RightPanel_qml.o LeftPanel_qml.o version_js.o MiddlePanel_qml.o main_qml.o wizard_WizardConfigure_qml.o wizard_WizardDaemonSettings_qml.o wizard_WizardCreateViewOnlyWallet_qml.o wizard_WizardPassword_qml.o wizard_WizardPasswordInput_qml.o wizard_WizardMain_qml.o wizard_WizardRecoveryWallet_qml.o wizard_WizardOptions_qml.o wizard_WizardCreateWalletFromDevice_qml.o wizard_WizardManageWalletUI_qml.o wizard_WizardMemoTextInput_qml.o wizard_utils_js.o wizard_WizardWelcome_qml.o wizard_WizardCreateWallet_qml.o wizard_WizardFinish_qml.o wizard_WizardDonation_qml.o wizard_WizardPasswordUI_qml.o tabs_Twitter_qml.o tabs_tweetSearch_js.o tabs_TweetsModel_qml.o components_TipItem_qml.o components_PrivacyLevelSmall_qml.o components_DaemonConsole_qml.o components_RadioButton_qml.o components_InlineButton_qml.o components_DaemonManagerDialog_qml.o components_TickDelegate_qml.o components_TitleBar_qml.o components_NetworkStatusItem_qml.o components_LabelButton_qml.o components_MobileHeader_qml.o components_NewPasswordDialog_qml.o components_PasswordDialog_qml.o components_Scroll_qml.o components_TableDropdown_qml.o components_CheckBox_qml.o components_StandardDialog_qml.o components_PrivacyLevel_qml.o components_Style_qml.o components_LabelSubheader_qml.o components_WarningBox_qml.o components_TableHeader_qml.o components_InputDialog_qml.o components_IconButton_qml.o components_LineEdit_qml.o components_DashboardTable_qml.o components_HistoryTableInnerColumn_qml.o components_Label_qml.o components_DatePicker_qml.o components_StandardDropdown_qml.o components_HistoryTable_qml.o components_SearchInput_qml.o components_InputMulti_qml.o components_ProcessingSplash_qml.o components_RemoteNodeEdit_qml.o components_TextBlock_qml.o components_StandardButton_qml.o components_Notifier_qml.o components_AddressBookTable_qml.o components_HistoryTableMobile_qml.o components_ProgressBar_qml.o components_MenuButton_qml.o components_LineEditMulti_qml.o components_CheckBox2_qml.o components_QRCodeScanner_qml.o components_Input_qml.o js_Windows_js.o js_Utils_js.o js_TxUtils_js.o pages_Transfer_qml.o pages_Mining_qml.o pages_Sign_qml.o pages_AddressBook_qml.o pages_Dashboard_qml.o pages_Keys_qml.o pages_History_qml.o pages_SharedRingDB_qml.o pages_Receive_qml.o pages_TxKey_qml.o pages_settings_SettingsInfo_qml.o pages_settings_Navbar_qml.o pages_settings_Settings_qml.o pages_settings_SettingsLog_qml.o pages_settings_SettingsLayout_qml.o pages_settings_SettingsWallet_qml.o pages_settings_SettingsNode_qml.o qmlcache_loader.o moc_filter.o moc_clipboardAdapter.o moc_oscursor.o moc_WalletManager.o moc_Wallet.o moc_PendingTransaction.o moc_TransactionHistory.o moc_TransactionInfo.o moc_Transfer.o moc_NetworkType.o moc_oshelper.o moc_TranslationManager.o moc_TransactionHistoryModel.o moc_TransactionHistorySortFilterModel.o moc_AddressBookModel.o moc_AddressBook.o moc_SubaddressModel.o moc_Subaddress.o moc_UnsignedTransaction.o moc_MainApp.o moc_DaemonManager.o moc_QrScanThread.o moc_QrCodeScanner.o   -L/opt/android/android-ndk-r17b/sources/cxx-stl/llvm-libc++/libs/arm64-v8a -L/opt/android/monero-gui/monero/lib -lwallet_merged -lepee -leasylogging -lzbarjni -liconv -Wl,-Bstatic -lunbound -lboost_serialization -lboost_thread -lboost_system -lboost_date_time -lboost_filesystem -lboost_regex -lboost_chrono -lboost_program_options -lssl -llmdb -lcrypto -Wl,-Bdynamic -lunwind -L/opt/android/Qt-5.11/lib -lQt5Quick -lQt5Widgets -lQt5Multimedia -lQt5Gui -lQt5Qml -lQt5Network -lQt5Core -lGLESv2 -lc++ -llog -lz -lm -ldl -lc
[91mclang++: warning: argument unused during compilation: '-pie' [-Wunused-command-line-argument]
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lwallet_merged
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lepee
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -leasylogging
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lunbound
/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lboost_serialization
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lboost_thread
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lboost_system
/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lboost_date_time
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lboost_filesystem
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lboost_regex
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lboost_chrono
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lboost_program_options
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lssl
/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -llmdb
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lcrypto
[0m[91m/opt/android/android-ndk-r17b/toolchains/aarch64-linux-android-4.9/prebuilt/linux-x86_64/lib/gcc/aarch64-linux-android/4.9.x/../../../../aarch64-linux-android/bin/ld: cannot find -lunwind
[0m[91mclang++: error: linker command failed with exit code 1 (use -v to see invocation)
[0m[91mmake: *** [release/bin/libmonero-wallet-gui.so] Error 1
[0mMakefile:564: recipe for target 'release/bin/libmonero-wallet-gui.so' failed
The command '/bin/sh -c cd ${WORKDIR}/monero-gui     && CMAKE_INCLUDE_PATH="${PREFIX}/include"        CMAKE_LIBRARY_PATH="${PREFIX}/lib"        ANDROID_STANDALONE_TOOLCHAIN_PATH=${TOOLCHAIN_DIR}        PATH=${HOST_PATH}        GIT_STRATEGY="none"            ./build.sh release-static-android-armv8' returned a non-zero code: 2



all output

https://pastebin.com/9ANPAYHu



# Discussion History
## dEBRUYNE-1 | 2018-10-13T08:07:25+00:00
Have you tried with #1571? 

## twiuglufosfa | 2018-10-13T10:04:31+00:00
yes i add https://github.com/monero-project/monero-gui/pull/1571

u can c on logs 

## dEBRUYNE-1 | 2018-10-14T14:50:47+00:00
Perhaps @MoroccanMalinois has an idea. 

# Action History
- Created by: twiuglufosfa | 2018-10-12T16:06:42+00:00
- Closed at: 2018-10-23T12:48:55+00:00
