---
title: Compile monerod for SunOS (SmartOS) - failures - MAP_HUGETLB undeclared
source_url: https://github.com/monero-project/monero/issues/5801
author: kayront
assignees: []
labels: []
created_at: '2019-08-10T13:57:15+00:00'
updated_at: '2019-08-10T18:12:41+00:00'
type: issue
status: closed
closed_at: '2019-08-10T18:12:41+00:00'
---

# Original Description
```
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/random.c.o
[ 15%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/skein.c.o
[ 16%] Building C object src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o
/home/admin/src/monero/src/crypto/slow-hash.c: In function 'slow_hash_allocate_state':
/home/admin/src/monero/src/crypto/slow-hash.c:761:51: error: 'MAP_HUGETLB' undeclared (first use in this function)
                     MAP_PRIVATE | MAP_ANONYMOUS | MAP_HUGETLB, -1, 0);
                                                   ^~~~~~~~~~~
/home/admin/src/monero/src/crypto/slow-hash.c:761:51: note: each undeclared identifier is reported only once for each function it appears in                                                                                                 
/home/admin/src/monero/src/crypto/slow-hash.c:788:23: warning: pointer targets in assignment from 'caddr_t' {aka 'char *'} to 'uint8_t *' {aka 'unsigned char *'} differ in signedness [-Wpointer-sign]                                      
     hp_jitfunc_memory = mmap(0, 4096 + 4096, PROT_READ | PROT_WRITE | PROT_EXEC,
                       ^
/home/admin/src/monero/src/crypto/slow-hash.c: In function 'slow_hash_free_state':
/home/admin/src/monero/src/crypto/slow-hash.c:819:16: warning: pointer targets in passing argument 1 of 'munmap' differ in signedness [-Wpointer-sign]                                                                                       
         munmap(hp_state, MEMORY);
                ^~~~~~~~
In file included from /home/admin/src/monero/src/crypto/slow-hash.c:369:
/usr/include/sys/mman.h:245:12: note: expected 'caddr_t' {aka 'char *'} but argument is of type 'uint8_t *' {aka 'unsigned char *'}                                                                                                          
 extern int munmap(caddr_t, size_t);
            ^~~~~~
/home/admin/src/monero/src/crypto/slow-hash.c:830:16: warning: pointer targets in passing argument 1 of 'munmap' differ in signedness [-Wpointer-sign]                                                                                       
         munmap(hp_jitfunc_memory, 4096 + 4095);
                ^~~~~~~~~~~~~~~~~
In file included from /home/admin/src/monero/src/crypto/slow-hash.c:369:
/usr/include/sys/mman.h:245:12: note: expected 'caddr_t' {aka 'char *'} but argument is of type 'uint8_t *' {aka 'unsigned char *'}                                                                                                          
 extern int munmap(caddr_t, size_t);
            ^~~~~~
make[2]: *** [src/crypto/CMakeFiles/obj_cncrypto.dir/build.make:297: src/crypto/CMakeFiles/obj_cncrypto.dir/slow-hash.c.o] Error 1                                                                                                           
make[1]: *** [CMakeFiles/Makefile2:807: src/crypto/CMakeFiles/obj_cncrypto.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
```

# Discussion History
## kayront | 2019-08-10T14:11:45+00:00
Simply removing MAP_HUGETLB from that line allows compilation to proceed. Unsure about the impact of doing so.

Leaving the issue open for further review by someone knowledgeable in this matter.

## thomasvaughan | 2019-08-10T14:34:07+00:00
Five lines up from MAP_HUGETLB, there's a

    #if defined(__APPLE__) || defined(__FreeBSD__) || defined(__OpenBSD__) || \
      defined(__DragonFly__) || defined(__NetBSD__)

Should you be tacking a ` || defined(__sun)` on to the end if it, seeing as SmartOS is more BSDish than Linuxish? (And *not* deleting `MAP_HUGETLB`!)

I draw your attention to [http://www.netbsd.org/docs/pkgsrc/fixes.html#fixes.build.cpp](http://www.netbsd.org/docs/pkgsrc/fixes.html#fixes.build.cpp).

I may be wrong, though.

## Toasterson | 2019-08-10T16:54:29+00:00
@thomasvaughan smartOS is an Illumos based OS thus it is very BSDish or rather very solarish :)


## kayront | 2019-08-10T18:12:36+00:00
You're right @thomasvaughan, outright deleting the text was just a bruteforce test, let's say.

When the time comes to submit patches, I will use your suggestion - thanks.

Closing this issue.

# Action History
- Created by: kayront | 2019-08-10T13:57:15+00:00
- Closed at: 2019-08-10T18:12:41+00:00
