---
title: CMake Error at CMakeLists.txt:82 (add_subdirectory)
source_url: https://github.com/monero-project/monero/issues/5846
author: pallabkarmakar
assignees: []
labels:
- invalid
created_at: '2019-08-23T13:21:41+00:00'
updated_at: '2019-08-27T15:26:01+00:00'
type: issue
status: closed
closed_at: '2019-08-27T15:26:01+00:00'
---

# Original Description
I am trying to build XGboost at linux system. While doing cmake received error like 

 CMake Error at CMakeLists.txt:82 (add_subdirectory):
  The source directory

    <project path>/dmlc-core

  does not contain a CMakeLists.txt file.


CMake Error at CMakeLists.txt:83 (set_target_properties):
  set_target_properties Can not find target to add properties to: dmlc

However CMakeLists.txt present at the project path. What is wrong here. Not able to resolve


# Discussion History
## moneromooo-monero | 2019-08-23T19:49:46+00:00
Wrong repo ? We do not have anything called dmlc-core.

## moneromooo-monero | 2019-08-27T15:21:55+00:00
Apparently filed on the wrong repo, closing :)

+invalid


# Action History
- Created by: pallabkarmakar | 2019-08-23T13:21:41+00:00
- Closed at: 2019-08-27T15:26:01+00:00
