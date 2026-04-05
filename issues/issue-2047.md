---
title: How does XMRig print the compiler used?
source_url: https://github.com/xmrig/xmrig/issues/2047
author: saloniamatteo
assignees: []
labels:
- question
created_at: '2021-01-18T17:40:08+00:00'
updated_at: '2021-03-02T20:00:02+00:00'
type: issue
status: closed
closed_at: '2021-03-02T20:00:02+00:00'
---

# Original Description
![104851621-c6a89e00-58bb-11eb-93dc-a1163dd898c4](https://user-images.githubusercontent.com/28765699/104947517-28503180-59bc-11eb-8551-a3df4b284f59.JPG)
In the image above (taken from #2046) you can see "XMRig/6.7.2 MSVC/2019". I'm interested in the "MSVC/2019" part.

In C, I know I can print the compiler's full version by using the predefined macro `__VERSION__`, but what about the compiler name?

# Discussion History
## jaga3421 | 2021-01-18T19:50:13+00:00
I am also interested in the XMRig/6.7.2 part. I changed the name in 'https://github.com/xmrig/xmrig/blob/master/res/app.rc#L27' still the name is not changed

@GoDzM4TT3O @xmrig 

## Spudz76 | 2021-01-18T20:10:38+00:00
It's right here, duh.

https://github.com/xmrig/xmrig/blob/master/src/base/kernel/config/BaseConfig.cpp#L138

## Spudz76 | 2021-01-18T20:15:55+00:00
@jaga3421 If you had followed the define from the app.rc back to version.h then that's where it comes from, everywhere it's used.

https://github.com/xmrig/xmrig/blob/master/src/version.h#L29

grep grep grep omg

## jaga3421 | 2021-01-19T07:15:24+00:00
Thank you very much @Spudz76 

## saloniamatteo | 2021-01-19T11:40:12+00:00
> It's right here, duh.
> 
> https://github.com/xmrig/xmrig/blob/master/src/base/kernel/config/BaseConfig.cpp#L138

I thought it was doing some magic, but in reality it's just checking if compiler-specific predefined macros exist.

For example, if compiling with GCC, it will check if `__GNUC__` is defined, or if compiling with CLang, it will check if `__clang__` is defined, etc.

However, isn't there a more straightforward way to just print the compiler name without checking for all of the existing C compilers? (Around 52 compilers, taken from [Wikipedia](https://en.m.wikipedia.org/wiki/List_of_compilers#C_compilers))

Thanks!

## Spudz76 | 2021-01-21T22:01:37+00:00
No, there is no standard for doing that.  Have to detect at compile time based on what the compiler has defined and "fingerprinting" as such.

# Action History
- Created by: saloniamatteo | 2021-01-18T17:40:08+00:00
- Closed at: 2021-03-02T20:00:02+00:00
