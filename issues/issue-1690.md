---
title: Mac libuv error
source_url: https://github.com/xmrig/xmrig/issues/1690
author: '0xA1B2'
assignees: []
labels:
- need feedback
created_at: '2020-05-24T18:05:54+00:00'
updated_at: '2021-01-09T23:29:55+00:00'
type: issue
status: closed
closed_at: '2020-05-27T15:48:44+00:00'
---

# Original Description
Following the instructions here do not work anymore:

https://github.com/xmrig/xmrig/wiki/macOS-Build

No matter if any CMAKE parameters for libuv are set or not, the compile error is always the same.

-DUV_LIBRARY=/usr/local/opt/libuv/lib/libuv.a

Machine
Apple MacBook Pro 16-Inch "Core i7" 2.6 2019 (Scissor)

Error
Undefined symbols for architecture x86_64:
  "___darwin_check_fd_set_overflow", referenced from:
      _uv__stream_osx_select in libuv.a(libuv_la-stream.o)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [xmrig-notls] Error 1
make[1]: *** [CMakeFiles/xmrig-notls.dir/all] Error 2
make: *** [all] Error 2


# Discussion History
## xmrig | 2020-05-25T10:22:10+00:00
I was unable to reproduce this issue, on recent macOS and freshly updated homebrew it compiled without issues.

1. The path to libuv.a now is `/usr/local/lib/libuv.a`, but it detected automatically, doesn't need to specify `-DUV_LIBRARY`.
2. Wiki page outdated, notice about this on top of wiki page.
3. It should be not related, but you do not follow instructions exactly as is, because you try to build the miner without TLS support.

I suggest you remove build files and start from scratch, if issue still persist please show cmake output.
Thank you.

## 0xA1B2 | 2020-05-27T15:48:44+00:00
Tried again, other SSL issues now, I close the bug report as it works fine on Clear Linux and Mac is not worth the time anyways.

## jtchen2k | 2020-06-05T17:33:00+00:00
Same issue for me... Though not worth the time.

## StephaneLapierre | 2020-08-02T17:02:59+00:00
cannot compile with osx 10.15.6
here the log from terminal
Last login: Sun Aug  2 11:25:04 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
Stephanes-MacBook-Pro:~ stephanelapierre$   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
Password:
==> This script will install:
/usr/local/bin/brew
/usr/local/share/doc/homebrew
/usr/local/share/man/man1/brew.1
/usr/local/share/zsh/site-functions/_brew
/usr/local/etc/bash_completion.d/brew
/usr/local/Homebrew

Press RETURN to continue or any other key to abort
==> Downloading and installing Homebrew...
HEAD is now at 0369c0ae9 Merge pull request #8188 from dtrodrigues/config-branch
Already up-to-date.
==> Installation successful!

==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
Read the analytics documentation (and how to opt-out) here:
  https://docs.brew.sh/Analytics
No analytics data has been sent yet (or will be during this `install` run).

==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
  https://github.com/Homebrew/brew#donations

==> Next steps:
- Run `brew help` to get started
- Further documentation: 
    https://docs.brew.sh
Stephanes-MacBook-Pro:~ stephanelapierre$ chsh -s /bin/zsh
Changing shell for stephanelapierre.
Password for stephanelapierre: 
Stephanes-MacBook-Pro:~ stephanelapierre$ cd xmrig
Stephanes-MacBook-Pro:xmrig stephanelapierre$ cd build
Stephanes-MacBook-Pro:build stephanelapierre$ brew install cmake libuv libmicrohttpd openssl hwloc
Updating Homebrew...
Warning: cmake 3.18.1 is already installed and up-to-date
To reinstall 3.18.1, run `brew reinstall cmake`
Warning: libuv 1.38.1 is already installed and up-to-date
To reinstall 1.38.1, run `brew reinstall libuv`
Warning: libmicrohttpd 0.9.71 is already installed and up-to-date
To reinstall 0.9.71, run `brew reinstall libmicrohttpd`
Warning: openssl@1.1 1.1.1g is already installed and up-to-date
To reinstall 1.1.1g, run `brew reinstall openssl@1.1`
Warning: hwloc 2.2.0 is already installed and up-to-date
To reinstall 2.2.0, run `brew reinstall hwloc`
Stephanes-MacBook-Pro:build stephanelapierre$ cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl
-- WITH_MSR=OFF
-- argon2: detecting feature 'sse2'...
-- argon2: feature 'sse2' detected!
-- argon2: detecting feature 'ssse3'...
-- argon2: feature 'ssse3' detected!
-- argon2: detecting feature 'xop'...
-- argon2: detecting feature 'avx2'...
-- argon2: feature 'avx2' detected!
-- argon2: detecting feature 'avx512f'...
-- argon2: feature 'avx512f' detected!
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/stephanelapierre/xmrig/build
Stephanes-MacBook-Pro:build stephanelapierre$ make
[  2%] Built target xmrig-asm
[  3%] Built target ethash
[  4%] Built target argon2-avx512f
[  5%] Built target argon2-avx2
[  6%] Built target argon2-xop
[  6%] Built target argon2-sse2
[  7%] Built target argon2-ssse3
[ 10%] Built target argon2
[ 10%] Linking CXX executable xmrig
Undefined symbols for architecture x86_64:
  "___darwin_check_fd_set_overflow", referenced from:
      _uv__stream_osx_select in libuv.a(libuv_la-stream.o)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [xmrig] Error 1
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
make: *** [all] Error 2
Stephanes-MacBook-Pro:build stephanelapierre$ 


## PauleBertt | 2020-11-01T11:13:17+00:00
> cannot compile with osx 10.15.6
> here the log from terminal
> Last login: Sun Aug 2 11:25:04 on ttys000
> 
> The default interactive shell is now zsh.
> To update your account to use zsh, please run `chsh -s /bin/zsh`.
> For more details, please visit https://support.apple.com/kb/HT208050.
> Stephanes-MacBook-Pro:~ stephanelapierre$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
> Password:
> ==> This script will install:
> /usr/local/bin/brew
> /usr/local/share/doc/homebrew
> /usr/local/share/man/man1/brew.1
> /usr/local/share/zsh/site-functions/_brew
> /usr/local/etc/bash_completion.d/brew
> /usr/local/Homebrew
> 
> Press RETURN to continue or any other key to abort
> ==> Downloading and installing Homebrew...
> HEAD is now at 0369c0ae9 Merge pull request #8188 from dtrodrigues/config-branch
> Already up-to-date.
> ==> Installation successful!
> 
> ==> Homebrew has enabled anonymous aggregate formulae and cask analytics.
> Read the analytics documentation (and how to opt-out) here:
> https://docs.brew.sh/Analytics
> No analytics data has been sent yet (or will be during this `install` run).
> 
> ==> Homebrew is run entirely by unpaid volunteers. Please consider donating:
> https://github.com/Homebrew/brew#donations
> 
> ==> Next steps:
> 
> * Run `brew help` to get started
> * Further documentation:
>   https://docs.brew.sh
>   Stephanes-MacBook-Pro:~ stephanelapierre$ chsh -s /bin/zsh
>   Changing shell for stephanelapierre.
>   Password for stephanelapierre:
>   Stephanes-MacBook-Pro:~ stephanelapierre$ cd xmrig
>   Stephanes-MacBook-Pro:xmrig stephanelapierre$ cd build
>   Stephanes-MacBook-Pro:build stephanelapierre$ brew install cmake libuv libmicrohttpd openssl hwloc
>   Updating Homebrew...
>   Warning: cmake 3.18.1 is already installed and up-to-date
>   To reinstall 3.18.1, run `brew reinstall cmake`
>   Warning: libuv 1.38.1 is already installed and up-to-date
>   To reinstall 1.38.1, run `brew reinstall libuv`
>   Warning: libmicrohttpd 0.9.71 is already installed and up-to-date
>   To reinstall 0.9.71, run `brew reinstall libmicrohttpd`
>   Warning: openssl@1.1 1.1.1g is already installed and up-to-date
>   To reinstall 1.1.1g, run `brew reinstall openssl@1.1`
>   Warning: hwloc 2.2.0 is already installed and up-to-date
>   To reinstall 2.2.0, run `brew reinstall hwloc`
>   Stephanes-MacBook-Pro:build stephanelapierre$ cmake .. -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl
>   -- WITH_MSR=OFF
>   -- argon2: detecting feature 'sse2'...
>   -- argon2: feature 'sse2' detected!
>   -- argon2: detecting feature 'ssse3'...
>   -- argon2: feature 'ssse3' detected!
>   -- argon2: detecting feature 'xop'...
>   -- argon2: detecting feature 'avx2'...
>   -- argon2: feature 'avx2' detected!
>   -- argon2: detecting feature 'avx512f'...
>   -- argon2: feature 'avx512f' detected!
>   -- Configuring done
>   -- Generating done
>   -- Build files have been written to: /Users/stephanelapierre/xmrig/build
>   Stephanes-MacBook-Pro:build stephanelapierre$ make
>   [  2%] Built target xmrig-asm
>   [  3%] Built target ethash
>   [  4%] Built target argon2-avx512f
>   [  5%] Built target argon2-avx2
>   [  6%] Built target argon2-xop
>   [  6%] Built target argon2-sse2
>   [  7%] Built target argon2-ssse3
>   [ 10%] Built target argon2
>   [ 10%] Linking CXX executable xmrig
>   Undefined symbols for architecture x86_64:
>   "___darwin_check_fd_set_overflow", referenced from:
>   _uv__stream_osx_select in libuv.a(libuv_la-stream.o)
>   ld: symbol(s) not found for architecture x86_64
>   clang: error: linker command failed with exit code 1 (use -v to see invocation)
>   make[2]: *** [xmrig] Error 1
>   make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
>   make: *** [all] Error 2
>   Stephanes-MacBook-Pro:build stephanelapierre$

this is the same issue i have

## brad-anton | 2021-01-09T23:29:33+00:00
Have you tried building a linking libua manually? Note: these steps also manually build hwloc

```
cd scripts
bash build.hwloc.sh
bash build.uv.sh
cd ..
cmake . -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl -DHWLOC_INCLUDE_DIR=scripts/deps/include -DHWLOC_LIBRARY=scripts/deps/lib/libhwloc.a -DUV_LIBRARY=scripts/deps/lib/libuv.a
make -j$(sysctl -n hw.logicalcpu)
```

# Action History
- Created by: 0xA1B2 | 2020-05-24T18:05:54+00:00
- Closed at: 2020-05-27T15:48:44+00:00
