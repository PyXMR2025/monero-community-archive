---
title: Compiling Master Error
source_url: https://github.com/monero-project/monero/issues/6764
author: italocoin-project
assignees: []
labels: []
created_at: '2020-08-16T08:34:58+00:00'
updated_at: '2020-08-16T16:22:04+00:00'
type: issue
status: closed
closed_at: '2020-08-16T16:22:04+00:00'
---

# Original Description
When i compile the master i get this error

`[ 11%] Building CXX object external/qrcodegen/CMakeFiles/qrcodegen.dir/QrCode.cpp.o
In file included from /usr/include/c++/5/array:35:0,
                 from /root/monero/external/qrcodegen/QrCode.hpp:26,
                 from /root/monero/external/qrcodegen/QrCode.cpp:32:
/usr/include/c++/5/bits/c++0x_warning.h:32:2: error: #error This file requires compiler and library support for the ISO C++ 2011 standard. This support must be enabled with the -std=c++11 or -std=gnu++11 compiler options.
 #error This file requires compiler and library support \
`


# Discussion History
## selsta | 2020-08-16T09:44:00+00:00
Which compiler are you using?

## italocoin-project | 2020-08-16T09:49:57+00:00
> Which compiler are you using?

Hi, here is the compiler

`c++ (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
and cmake version 3.5.1`

## selsta | 2020-08-16T09:55:27+00:00
As an easy workaround use a newer compiler.

To properly fix this I think the CMake file needs a change.

## italocoin-project | 2020-08-16T10:21:27+00:00
> As an easy workaround use a newer compiler.
> 
> To properly fix this I think the CMake file needs a change.

i need this compiler so i can't change it

## sumogr | 2020-08-16T11:23:20+00:00
@italocoin-project at external/qrcodegen/CMakeLists.txt change this
`set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")`
into
`set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -std=c++11 -O2")`

## italocoin-project | 2020-08-16T12:32:37+00:00
> @italocoin-project at external/qrcodegen/CMakeLists.txt change this
> `set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")`
> into
> `set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -std=c++11 -O2")`

Hi thanks for the help, i know how to fix it i was just raising the issue to be fixed.

## sumogr | 2020-08-16T12:55:53+00:00
> > @italocoin-project at external/qrcodegen/CMakeLists.txt change this
> > `set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")`
> > into
> > `set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -std=c++11 -O2")`
> 
> Hi thanks for the help, i know how to fix it i was just raising the issue to be fixed.

open a PR then ;)

## italocoin-project | 2020-08-16T15:39:45+00:00
> > > @italocoin-project at external/qrcodegen/CMakeLists.txt change this
> > > `set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC")`
> > > into
> > > `set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -std=c++11 -O2")`
> > 
> > 
> > Hi thanks for the help, i know how to fix it i was just raising the issue to be fixed.
> 
> open a PR then ;)

i've fixed it exactly how you wrote it above, i don't know if it would work fine on other Cmake/c++ versions tho

## selsta | 2020-08-16T16:08:03+00:00
@italocoin-project 

Can you check if #6766 solves the issue?

## italocoin-project | 2020-08-16T16:22:03+00:00
> @italocoin-project
> 
> Can you check if #6766 solves the issue?

Works fine!

# Action History
- Created by: italocoin-project | 2020-08-16T08:34:58+00:00
- Closed at: 2020-08-16T16:22:04+00:00
