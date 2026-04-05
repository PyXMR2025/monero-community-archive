---
title: BETA Branch - macOS Catalina can no longer build xmrig - Libcrypto Issue
source_url: https://github.com/xmrig/xmrig/issues/1271
author: realityworks
assignees: []
labels: []
created_at: '2019-11-09T16:16:20+00:00'
updated_at: '2019-11-18T16:12:54+00:00'
type: issue
status: closed
closed_at: '2019-11-18T16:12:54+00:00'
---

# Original Description
Recently from the Apple Developer forums :

Are you trying to use the OpenSSL libraries built in to macOS?  If so, that’s not something we support.  Those libraries were deprecated back in the 10.7 days.  Watch WWDC 2011 Session 212 Next-Generation Cryptographic Services for a full explanation as to why.
[Ironically, the replacement crypto API, Security Transforms, is now effectively deprecated as well, but there are other APIs you can use.  In fact, Apple’s crypto APIs are in a better shape today than they have ever been.]

As to how you should proceed, that depends on your goals:

- If you’re using libcrypto in your own code for basic cryptographic operations, rewrite that code to use one of Apple’s crypto APIs.  If you post details about what you need, I can point you in the right direction.

- If you’re not using libcrypto directly, but instead are using some other library (like OpenSSL) that depends on libcrypto, you have two choices:

1. You can tweak that library to use an Apple API directly.  IMO, most open source libraries would benefit from having a crypto abstraction layer, because crypto APIs vary wildly across platforms and it’s generally best to use the platform-specific API.
2. You can build libcrypto from source and include that in your product.

# Discussion History
## realityworks | 2019-11-15T03:43:00+00:00
@SChernykh How are you guys doing release builds for Mac given this issue?

## realityworks | 2019-11-15T03:55:25+00:00
Same thing happens in the master branch on 0.15.0.0

## xmrig | 2019-11-15T18:38:10+00:00
Did you check the build docs? https://github.com/xmrig/xmrig/wiki/macOS-Build it builds and works fine on macOS Catalina, Apple shipped OpenSSL is not used from beginning of time.
Thank you.

## realityworks | 2019-11-18T16:00:21+00:00
@xmrig this is what I get when following those instructions : 
<img width="1169" alt="image" src="https://user-images.githubusercontent.com/21374160/69065739-3e1d3c00-0a31-11ea-889c-ff2d847eca34.png">


## xmrig | 2019-11-18T16:11:22+00:00
Make sure you use cmake option `-DOPENSSL_ROOT_DIR=/usr/local/opt/openssl` also v5.0.1 now use static linking with openssl, updated docs how static link hwloc in progress.

## realityworks | 2019-11-18T16:12:54+00:00
Removed local folder, rebuilt and now it works on the master branch... For now we can close this issue.

# Action History
- Created by: realityworks | 2019-11-09T16:16:20+00:00
- Closed at: 2019-11-18T16:12:54+00:00
