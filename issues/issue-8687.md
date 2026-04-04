---
title: Removing the "trap" of not importing 'serialization/string.h' when using 'binary_archive'
  serialization
source_url: https://github.com/monero-project/monero/issues/8687
author: rbrunner7
assignees: []
labels:
- enhancement
- request
created_at: '2022-12-26T18:00:15+00:00'
updated_at: '2024-01-18T23:00:48+00:00'
type: issue
status: closed
closed_at: '2024-01-18T23:00:48+00:00'
---

# Original Description
I am talking here about using `binary_archive` to serialize data structures into strings or files by adding "intrumentation" to structures in the form of references to certain macros which looks like this:

    struct sample_struct {
      std::string standard_string;
    
      BEGIN_SERIALIZE_OBJECT()
        FIELD(standard_string)
      END_SERIALIZE()
    };

You make the macros available by importing this in your .h file:

    #include "serialization/serialization.h"

What you have to know however that this alone is **not** sufficient to serialize everything. Already for the very mundane `std::string` used in the example you need one more import:

    #include "serialization/string.h"

`wallet2.h` seems to have the full list of such imports:

    #include "serialization/crypto.h"
    #include "serialization/string.h"
    #include "serialization/pair.h"
    #include "serialization/tuple.h"
    #include "serialization/containers.h"

Thing is: If you forget to import `string.h`, or if you only import it in the .cpp file but not in your .h file, **it compiles**, but the wrong templates match, and the resulting serialization code sometimes produces an endless recursion. With debug compilation, you may get the recursion when running; with release compilation the top-level call to `serialize` can get replaced by the smallest possible endless loop that looks like that with x86 instructions:

    JMP -2

It took me several hours of trial-and-error and debugging until I found that out. (I was on a wrong track and suspecting a bug in the code generator that wrongly resulted in emitting merely two bytes for that endless loop into the code.)

This splitting into several .h files and strictly only importing the needed ones may have made sense with much slower machines back in 2014, but I think today we could remove this "trap" by letting `serialization.h` already import all those specialized .h files.

If people agree I could make a small PR that does that.

Or maybe there is an simple way to make the code un-compilable if you forget one of the necessary .h files?


# Discussion History
# Action History
- Created by: rbrunner7 | 2022-12-26T18:00:15+00:00
- Closed at: 2024-01-18T23:00:48+00:00
