---
title: Compile problem
source_url: https://github.com/monero-project/monero/issues/52
author: spr0cker
assignees: []
labels: []
created_at: '2014-06-23T23:12:20+00:00'
updated_at: '2014-07-16T15:08:47+00:00'
type: issue
status: closed
closed_at: '2014-06-25T16:14:39+00:00'
---

# Original Description
very long text message, ends with words:
`(.rodata._ZTVN5boost15program_options20invalid_option_valueE[_ZTVN5boost15program_options20invalid_option_valueE]+0x30): undefined reference to`boost::program_options::error_with_option_name::substitute_placeholders(std::string const&) const'
collect2: error: ld returned 1 exit status
make[3]: **\* [src/connectivity_tool] error`

system Ubuntu 12.04


# Discussion History
## v4l3r10 | 2014-07-16T15:08:47+00:00
+1


# Action History
- Created by: spr0cker | 2014-06-23T23:12:20+00:00
- Closed at: 2014-06-25T16:14:39+00:00
