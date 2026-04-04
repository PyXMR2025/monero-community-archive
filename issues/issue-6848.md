---
title: Aarch64 error
source_url: https://github.com/monero-project/monero/issues/6848
author: Edan3blov
assignees: []
labels: []
created_at: '2020-09-27T00:31:51+00:00'
updated_at: '2020-11-19T12:34:14+00:00'
type: issue
status: closed
closed_at: '2020-11-19T12:34:14+00:00'
---

# Original Description
Hello,

I have some error on compiling for android aarch64 architecture


make[3]: Entering directory '/src/build/release/translations'
[ 50%] Building C object CMakeFiles/generate_translations_header.dir/generate_translations_header.c.o
[100%] Linking C executable generate_translations_header
Generating embedded translations header
: not foundtranslations_header: 1: ELF�@�*@@@@@�~~@@-@-��pp-p��Q�tdR�td@@-@-��/system/bin/linker6�Androidr21d6528147
./generate_translations_header: 2: 


                                   �D@@
                                       �4��d��_WBE�����: not found
./generate_translations_header: 2: j�: not found
./generate_translations_header: 1: ��0���0X
                                           d: not found
��/d: not foundslations_header: 2: c
./generate_translations_header: 2: cannot open �
                                                0?9�1RF���0]@�-�/P-0z�/�/�/�/�/��/: No such file
����@������: not founds_header: 2: 2b���qXҩ,r��W./generate_translations_header: 1: 9�
./generate_translations_header: 2: �R�: not found
./generate_translations_header: 3: *�{D��C��_�translation_files.hw#ifndef: not found
./generate_translations_header: 8: rbstatic: not found
./generate_translations_header: 9: static: not found
./generate_translations_header: 4: �{����G�B: not found
./generate_translations_header: 1: Syntax error: word unexpected (expecting ")")
make[3]: *** [CMakeFiles/generate_translations_header.dir/build.make:86: generate_translations_header] Error 2
make[3]: *** Deleting file 'generate_translations_header'
make[3]: Leaving directory '/src/build/release/translations'
make[2]: *** [CMakeFiles/Makefile2:73: CMakeFiles/generate_translations_header.dir/all] Error 2
make[2]: Leaving directory '/src/build/release/translations'
make[1]: Leaving directory '/src/build/release/translations'
make[1]: *** [Makefile:84: all] Error 2
make: *** [Makefile:130: release-static-android-armv8] Error 2


Is strange that with NDK17 compile works without any error but with NDK21 not.

# Discussion History
# Action History
- Created by: Edan3blov | 2020-09-27T00:31:51+00:00
- Closed at: 2020-11-19T12:34:14+00:00
