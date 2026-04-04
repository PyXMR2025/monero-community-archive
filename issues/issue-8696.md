---
title: monero 0.18.1.2 regression build failure
source_url: https://github.com/monero-project/monero/issues/8696
author: chenrui333
assignees: []
labels: []
created_at: '2023-01-01T17:15:30+00:00'
updated_at: '2023-01-01T17:24:34+00:00'
type: issue
status: closed
closed_at: '2023-01-01T17:24:34+00:00'
---

# Original Description
👋 when [regression build against boost 1.81.0](https://github.com/Homebrew/homebrew-core/pull/119529), we found the build failure as below

<details>
<summary>build issue</summary>

```
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:517:35: error: expected '(' for function-style cast or type construction
  std::vector<std::set<std::string> > records;
                       ~~~~~~~~~~~^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:517:20: error: no member named 'set' in namespace 'std'
  std::vector<std::set<std::string> > records;
              ~~~~~^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:517:37: error: expected unqualified-id
  std::vector<std::set<std::string> > records;
                                    ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:518:3: error: use of undeclared identifier 'records'
  records.resize(dns_urls.size());
  ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:528:41: error: use of undeclared identifier 'records'
    tpool.submit(&waiter,[n, dns_urls, &records, &avail, &valid](){
                                        ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:531:10: error: use of undeclared identifier 'records'
         records[n].insert(s);
         ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:542:7: error: use of undeclared identifier 'records'
      records[cur_index].clear();
      ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:547:7: error: use of undeclared identifier 'records'
      records[cur_index].clear();
      ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:560:33: error: use of undeclared identifier 'records'
  for( const auto& record_set : records)
                                ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:574:40: error: expected '(' for function-style cast or type construction
  typedef std::map<std::set<std::string>, uint32_t> map_t;
                            ~~~~~~~~~~~^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:574:25: error: no member named 'set' in namespace 'std'
  typedef std::map<std::set<std::string>, uint32_t> map_t;
                   ~~~~~^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:574:41: error: expected unqualified-id
  typedef std::map<std::set<std::string>, uint32_t> map_t;
                                        ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:575:3: error: unknown type name 'map_t'
  map_t record_count;
  ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:576:23: error: use of undeclared identifier 'records'
  for (const auto &e: records)
                      ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:582:3: error: use of undeclared identifier 'map_t'
  map_t::const_iterator good_record = record_count.end();
  ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:582:25: error: use of undeclared identifier 'good_record'; did you mean 'good_records'?
  map_t::const_iterator good_record = record_count.end();
                        ^~~~~~~~~~~
                        good_records
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:512:58: note: 'good_records' declared here
bool load_txt_records_from_dns(std::vector<std::string> &good_records, const std::vector<std::string> &dns_urls)
                                                         ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:583:8: error: use of undeclared identifier 'map_t'
  for (map_t::const_iterator i = record_count.begin(); i != record_count.end(); ++i)
       ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:585:9: error: use of undeclared identifier 'good_record'; did you mean 'good_records'?
    if (good_record == record_count.end() || i->second > good_record->second)
        ^~~~~~~~~~~
        good_records
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:512:58: note: 'good_records' declared here
bool load_txt_records_from_dns(std::vector<std::string> &good_records, const std::vector<std::string> &dns_urls)
                                                         ^
/tmp/monero-20230101-17100-1gvtdyp/src/common/dns_utils.cpp:585:58: error: use of undeclared identifier 'good_record'
    if (good_record == record_count.end() || i->second > good_record->second)
                                                         ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 errors generated.
```


</details>


# Discussion History
## selsta | 2023-01-01T17:17:32+00:00
Should be solved by https://github.com/monero-project/monero/pull/8682

## chenrui333 | 2023-01-01T17:19:09+00:00
Was thinking about the same thing, thanks for confirming it! Gonna try the patch now.

## chenrui333 | 2023-01-01T17:24:26+00:00
works for me, thanks for the fix!

# Action History
- Created by: chenrui333 | 2023-01-01T17:15:30+00:00
- Closed at: 2023-01-01T17:24:34+00:00
