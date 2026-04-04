---
title: trouble building on ArchLinux
source_url: https://github.com/monero-project/monero-gui/issues/4118
author: dbear496
assignees: []
labels: []
created_at: '2023-02-16T04:55:25+00:00'
updated_at: '2023-02-16T16:35:30+00:00'
type: issue
status: closed
closed_at: '2023-02-16T16:35:30+00:00'
---

# Original Description
I'm getting a compile error when building on ArchLinux. What am I missing?

Here's what I did step-by-step:
```
sudo pacman -Syu base-devel cmake boost openssl zeromq libpgm unbound libsodium libunwind xz readline expat gtest python3 ccache doxygen graphviz qt5-tools hidapi libusb protobuf systemd # turns out I already had all the packages
git clone --recursive https://github.com/monero-project/monero-gui.git
cd monero-gui
git checkout v0.18.1.2
git submodule sync --recursive
git submodule update --recursive
make release
```

Then I get this stream of errors:
```
In file included from .../monero-gui/monero/src/common/dns_utils.cpp:35:
.../monero-gui/monero/src/common/threadpool.h:96:10: error: ‘deque’ in namespace ‘std’ does not name a template type
   96 |     std::deque<entry> queue;  
      |          ^~~~~
.../monero-gui/monero/src/common/threadpool.h:33:1: note: ‘std::deque’ is defined in header ‘<deque>’; did you forget to ‘#include <deque>’?
   32 | #include <boost/thread/thread.hpp>
  +++ |+#include <deque>
   33 | #include <cstddef>
.../monero-gui/monero/src/common/dns_utils.cpp: In function ‘bool tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char> >&, const std::vector<std::__cxx11::basic_string<char> >&)’:
.../monero-gui/monero/src/common/dns_utils.cpp:517:20: error: ‘set’ is not a member of ‘std’
  517 |   std::vector<std::set<std::string> > records;
      |                    ^~~
.../monero-gui/monero/src/common/dns_utils.cpp:39:1: note: ‘std::set’ is defined in header ‘<set>’; did you forget to ‘#include <set>’?
   38 | #include <boost/algorithm/string/join.hpp>
  +++ |+#include <set>
   39 | #include <boost/optional.hpp> 
.../monero-gui/monero/src/common/dns_utils.cpp:517:20: error: ‘set’ is not a member of ‘std’
  517 |   std::vector<std::set<std::string> > records;
      |                    ^~~
.../monero-gui/monero/src/common/dns_utils.cpp:517:20: note: ‘std::set’ is defined in header ‘<set>’; did you forget to ‘#include <set>’?
.../monero-gui/monero/src/common/dns_utils.cpp:517:35: error: template argument 1 is invalid
  517 |   std::vector<std::set<std::string> > records;
      |                                   ^
.../monero-gui/monero/src/common/dns_utils.cpp:517:35: error: template argument 2 is invalid
.../monero-gui/monero/src/common/dns_utils.cpp:517:37: error: expected unqualified-id before ‘>’ token
  517 |   std::vector<std::set<std::string> > records;
      |                                     ^
.../monero-gui/monero/src/common/dns_utils.cpp:518:3: error: ‘records’ was not declared in this scope
  518 |   records.resize(dns_urls.size());
      |   ^~~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:523:8: error: ‘deque’ is not a member of ‘std’
  523 |   std::deque<bool> avail(dns_urls.size(), false), valid(dns_urls.size(), false);
      |        ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:39:1: note: ‘std::deque’ is defined in header ‘<deque>’; did you forget to ‘#include <deque>’?
   38 | #include <boost/algorithm/string/join.hpp>
  +++ |+#include <deque>
   39 | #include <boost/optional.hpp> 
.../monero-gui/monero/src/common/dns_utils.cpp:523:14: error: expected primary-expression before ‘bool’
  523 |   std::deque<bool> avail(dns_urls.size(), false), valid(dns_urls.size(), false);
      |              ^~~~
.../monero-gui/monero/src/common/dns_utils.cpp:528:51: error: ‘avail’ was not declared in this scope
  528 |     tpool.submit(&waiter,[n, dns_urls, &records, &avail, &valid](){
      |                                                   ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:528:59: error: ‘valid’ was not declared in this scope
  528 |     tpool.submit(&waiter,[n, dns_urls, &records, &avail, &valid](){
      |                                                           ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp: In lambda function:
.../monero-gui/monero/src/common/dns_utils.cpp:529:84: error: ‘avail’ is not captured
  529 |        const auto res = tools::DNSResolver::instance().get_txt_record(dns_urls[n], avail[n], valid[n]);
      |                                                                                    ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:528:64: note: the lambda has no capture-default
  528 |     tpool.submit(&waiter,[n, dns_urls, &records, &avail, &valid](){
      |                                                                ^
.../monero-gui/monero/src/common/dns_utils.cpp:528:51: note: ‘<typeprefixerror>avail’ declared here
  528 |     tpool.submit(&waiter,[n, dns_urls, &records, &avail, &valid](){
      |                                                   ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:529:94: error: ‘valid’ is not captured
  529 |        const auto res = tools::DNSResolver::instance().get_txt_record(dns_urls[n], avail[n], valid[n]);
      |                                                                                              ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:528:64: note: the lambda has no capture-default
  528 |     tpool.submit(&waiter,[n, dns_urls, &records, &avail, &valid](){
      |                                                                ^
.../monero-gui/monero/src/common/dns_utils.cpp:528:59: note: ‘<typeprefixerror>valid’ declared here
  528 |     tpool.submit(&waiter,[n, dns_urls, &records, &avail, &valid](){
      |                                                           ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:531:10: error: ‘records’ is not captured
  531 |          records[n].insert(s);
      |          ^~~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:528:64: note: the lambda has no capture-default
  528 |     tpool.submit(&waiter,[n, dns_urls, &records, &avail, &valid](){
      |                                                                ^
.../monero-gui/monero/src/common/dns_utils.cpp:518:3: note: ‘<typeprefixerror>records’ declared here
  518 |   records.resize(dns_urls.size());
      |   ^~~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp: In function ‘bool tools::dns_utils::load_txt_records_from_dns(std::vector<std::__cxx11::basic_string<char> >&, const std::vector<std::__cxx11::basic_string<char> >&)’:
.../monero-gui/monero/src/common/dns_utils.cpp:540:10: error: ‘avail’ was not declared in this scope
  540 |     if (!avail[cur_index])
      |          ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:545:10: error: ‘valid’ was not declared in this scope
  545 |     if (!valid[cur_index])
      |          ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:574:25: error: ‘set’ is not a member of ‘std’
  574 |   typedef std::map<std::set<std::string>, uint32_t> map_t;
      |                         ^~~   
.../monero-gui/monero/src/common/dns_utils.cpp:574:25: note: ‘std::set’ is defined in header ‘<set>’; did you forget to ‘#include <set>’?
.../monero-gui/monero/src/common/dns_utils.cpp:574:25: error: ‘set’ is not a member of ‘std’
.../monero-gui/monero/src/common/dns_utils.cpp:574:25: note: ‘std::set’ is defined in header ‘<set>’; did you forget to ‘#include <set>’?
.../monero-gui/monero/src/common/dns_utils.cpp:574:40: error: wrong number of template arguments (1, should be at least 2)
  574 |   typedef std::map<std::set<std::string>, uint32_t> map_t;
      |                                        ^
In file included from /usr/include/c++/12.2.1/map:61,
                 from .../monero-gui/monero/external/easylogging++/easylogging++.h:405,
                 from .../monero-gui/monero/contrib/epee/include/misc_log_ex.h:35,
                 from .../monero-gui/monero/contrib/epee/include/include_base_utils.h:32,
                 from .../monero-gui/monero/src/common/dns_utils.cpp:34:
/usr/include/c++/12.2.1/bits/stl_map.h:100:11: note: provided for ‘template<class _Key, class _Tp, class _Compare, class _Alloc> class std::map’
  100 |     class map
      |           ^~~
.../monero-gui/monero/src/common/dns_utils.cpp:574:41: error: expected unqualified-id before ‘,’ token
  574 |   typedef std::map<std::set<std::string>, uint32_t> map_t;
      |                                         ^
.../monero-gui/monero/src/common/dns_utils.cpp:574:51: error: expected initializer before ‘>’ token
  574 |   typedef std::map<std::set<std::string>, uint32_t> map_t;
      |                                                   ^
.../monero-gui/monero/src/common/dns_utils.cpp:575:3: error: ‘map_t’ was not declared in this scope
  575 |   map_t record_count;
      |   ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:579:9: error: ‘record_count’ was not declared in this scope
  579 |       ++record_count[e];
      |         ^~~~~~~~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:582:3: error: ‘map_t’ is not a class, namespace, or enumeration
  582 |   map_t::const_iterator good_record = record_count.end();
      |   ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:583:8: error: ‘map_t’ is not a class, namespace, or enumeration
  583 |   for (map_t::const_iterator i = record_count.begin(); i != record_count.end(); ++i)
      |        ^~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:583:56: error: ‘i’ was not declared in this scope
  583 |   for (map_t::const_iterator i = record_count.begin(); i != record_count.end(); ++i)
      |                                                        ^
.../monero-gui/monero/src/common/dns_utils.cpp:583:61: error: ‘record_count’ was not declared in this scope
  583 |   for (map_t::const_iterator i = record_count.begin(); i != record_count.end(); ++i)
      |                                                             ^~~~~~~~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:585:9: error: ‘good_record’ was not declared in this scope; did you mean ‘good_records’?
  585 |     if (good_record == record_count.end() || i->second > good_record->second)
      |         ^~~~~~~~~~~
      |         good_records
.../monero-gui/monero/src/common/dns_utils.cpp:589:23: error: ‘good_record’ was not declared in this scope; did you mean ‘good_records’?
  589 |   MDEBUG("Found " << (good_record == record_count.end() ? 0 : good_record->second) << "/" << dns_urls.size() << " matching records from " << num_valid_records << " valid records");
      |                       ^~~~~~~~~~~
.../monero-gui/monero/contrib/epee/include/misc_log_ex.h:45:93: note: in definition of macro ‘MCLOG_TYPE’
   45 |       el::base::Writer(level, color, __FILE__, __LINE__, ELPP_FUNC, type).construct(cat) << x; \
      |                                                                                             ^
.../monero-gui/monero/contrib/epee/include/misc_log_ex.h:56:24: note: in expansion of macro ‘MCLOG’
   56 | #define MCDEBUG(cat,x) MCLOG(el::Level::Debug,cat, el::Color::Default, x)
      |                        ^~~~~  
.../monero-gui/monero/contrib/epee/include/misc_log_ex.h:78:19: note: in expansion of macro ‘MCDEBUG’
   78 | #define MDEBUG(x) MCDEBUG(MONERO_DEFAULT_LOG_CATEGORY,x)
      |                   ^~~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:589:3: note: in expansion of macro ‘MDEBUG’
  589 |   MDEBUG("Found " << (good_record == record_count.end() ? 0 : good_record->second) << "/" << dns_urls.size() << " matching records from " << num_valid_records << " valid records");
      |   ^~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:589:38: error: ‘record_count’ was not declared in this scope
  589 |   MDEBUG("Found " << (good_record == record_count.end() ? 0 : good_record->second) << "/" << dns_urls.size() << " matching records from " << num_valid_records << " valid records");
      |                                      ^~~~~~~~~~~~
.../monero-gui/monero/contrib/epee/include/misc_log_ex.h:45:93: note: in definition of macro ‘MCLOG_TYPE’
   45 |       el::base::Writer(level, color, __FILE__, __LINE__, ELPP_FUNC, type).construct(cat) << x; \
      |                                                                                             ^
.../monero-gui/monero/contrib/epee/include/misc_log_ex.h:56:24: note: in expansion of macro ‘MCLOG’
   56 | #define MCDEBUG(cat,x) MCLOG(el::Level::Debug,cat, el::Color::Default, x)
      |                        ^~~~~  
.../monero-gui/monero/contrib/epee/include/misc_log_ex.h:78:19: note: in expansion of macro ‘MCDEBUG’
   78 | #define MDEBUG(x) MCDEBUG(MONERO_DEFAULT_LOG_CATEGORY,x)
      |                   ^~~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:589:3: note: in expansion of macro ‘MDEBUG’
  589 |   MDEBUG("Found " << (good_record == record_count.end() ? 0 : good_record->second) << "/" << dns_urls.size() << " matching records from " << num_valid_records << " valid records");
      |   ^~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:590:7: error: ‘good_record’ was not declared in this scope; did you mean ‘good_records’?
  590 |   if (good_record == record_count.end() || good_record->second < dns_urls.size() / 2 + 1)
      |       ^~~~~~~~~~~
      |       good_records
.../monero-gui/monero/src/common/dns_utils.cpp:590:22: error: ‘record_count’ was not declared in this scope
  590 |   if (good_record == record_count.end() || good_record->second < dns_urls.size() / 2 + 1)
      |                      ^~~~~~~~~~~~
.../monero-gui/monero/src/common/dns_utils.cpp:597:23: error: ‘good_record’ was not declared in this scope; did you mean ‘good_records’?
  597 |   for (const auto &s: good_record->first)
      |                       ^~~~~~~~~~~
      |                       good_records
make[3]: *** [monero/src/common/CMakeFiles/obj_common.dir/build.make:104: monero/src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o] Error 1
make[2]: *** [CMakeFiles/Makefile2:1808: monero/src/common/CMakeFiles/obj_common.dir/all] Error 2
make[1]: *** [Makefile:136: all] Error 2
make[1]: Leaving directory '.../monero-gui/build/release'
make: *** [Makefile:48: release] Error 2
```

# Discussion History
## selsta | 2023-02-16T11:21:25+00:00
Please see #4117

## dbear496 | 2023-02-16T16:35:30+00:00
Thanks for the quick response. I was able to work around the issue by following the instructions in #4117.

# Action History
- Created by: dbear496 | 2023-02-16T04:55:25+00:00
- Closed at: 2023-02-16T16:35:30+00:00
