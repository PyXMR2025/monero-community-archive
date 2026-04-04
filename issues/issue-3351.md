---
title: 'PR #3303 and #3350 Mac build failing'
source_url: https://github.com/monero-project/monero/issues/3351
author: jtgrassie
assignees: []
labels: []
created_at: '2018-03-05T14:18:14+00:00'
updated_at: '2018-03-05T18:21:32+00:00'
type: issue
status: closed
closed_at: '2018-03-05T18:21:32+00:00'
---

# Original Description
```
/monero/src/device/device_default.cpp:343:22: error: no matching member function for call to 'insert'
            registry.insert(std::make_pair("default",default_core_device));
            ~~~~~~~~~^~~~~~
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/map:1086:9: note: candidate function not viable: no known
      conversion from 'pair<typename __make_pair_return<char const (&)[8]>::type, typename __make_pair_return<device_default *&>::type>' to
      'const pair<const key_type, mapped_type>' for 1st argument
        insert(const value_type& __v) {return __tree_.__insert_unique(__v);}
        ^
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/map:1115:10: note: candidate function not viable: no known
      conversion from 'pair<typename __make_pair_return<char const (&)[8]>::type, typename __make_pair_return<device_default *&>::type>'
      (aka 'pair<const char *, hw::core::device_default *>') to 'initializer_list<value_type>' (aka 'initializer_list<pair<const std::__1::basic_string<char>,
      std::__1::unique_ptr<hw::device, std::__1::default_delete<hw::device> > > >') for 1st argument
    void insert(initializer_list<value_type> __il)
         ^
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/map:1071:42: note: candidate template ignored: disabled by
      'enable_if' [with _Pp = std::__1::pair<const char *, hw::core::device_default *>]
              class = typename enable_if<is_constructible<value_type, _Pp>::value>::type>
                                         ^
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/map:1079:18: note: candidate function template not viable:
      requires 2 arguments, but 1 was provided
        iterator insert(const_iterator __pos, _Pp&& __p)
                 ^
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/map:1106:14: note: candidate function template not viable:
      requires 2 arguments, but 1 was provided
        void insert(_InputIterator __f, _InputIterator __l)
             ^
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/../include/c++/v1/map:1090:9: note: candidate function not viable: requires 2
      arguments, but 1 was provided
        insert(const_iterator __p, const value_type& __v)
```

EDIT: add more output and change title.

# Discussion History
## stoffu | 2018-03-05T15:02:46+00:00
#3346 seems to solve this, please check. Strange though that I'm also with Mac and I don't get this error. 

## jtgrassie | 2018-03-05T18:19:02+00:00
@stoffu yes that fixes it. @fluffypony can we get this #3346 added for next release. Thanks.

# Action History
- Created by: jtgrassie | 2018-03-05T14:18:14+00:00
- Closed at: 2018-03-05T18:21:32+00:00
