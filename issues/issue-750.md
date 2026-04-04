---
title: 'mac osx 10.11.4 : build fails'
source_url: https://github.com/monero-project/monero/issues/750
author: schnerchi
assignees: []
labels: []
created_at: '2016-03-23T09:05:51+00:00'
updated_at: '2016-03-25T13:38:24+00:00'
type: issue
status: closed
closed_at: '2016-03-25T13:38:24+00:00'
---

# Original Description
After updating to 10.11.4 yesterday the build fails... 10.11.3 worked yesterday :

Desktop/Dev/bitmonero/contrib/epee/include/storages/portable_storage_template_helper.h:75:14: error: 
      moving a local object in a return statement prevents copy elision [-Werror,-Wpessimizing-move]
      return std::move(json_buff);
             ^
Desktop/Dev/bitmonero/contrib/epee/include/storages/portable_storage_template_helper.h:75:14: note: 
      remove std::move call here
      return std::move(json_buff);
             ^~~~~~~~~~         ~
Desktop/Dev/bitmonero/contrib/epee/include/storages/portable_storage_template_helper.h:120:14: error: 
      moving a local object in a return statement prevents copy elision [-Werror,-Wpessimizing-move]
      return std::move(binary_buff);
             ^
Desktop/Dev/bitmonero/contrib/epee/include/storages/portable_storage_template_helper.h:120:14: note: 
      remove std::move call here
      return std::move(binary_buff);
             ^~~~~~~~~~           ~


# Discussion History
## antanst | 2016-03-25T13:37:08+00:00
Same on my Mac.


## fluffypony | 2016-03-25T13:38:24+00:00
Fixed - pull latest from github and try again:)


# Action History
- Created by: schnerchi | 2016-03-23T09:05:51+00:00
- Closed at: 2016-03-25T13:38:24+00:00
