---
title: '求助:编译xmrig时出错，“_mm256_bslli_epi128”: 找不到标识符'
source_url: https://github.com/xmrig/xmrig/issues/962
author: ctqch
assignees: []
labels: []
created_at: '2019-03-01T05:26:35+00:00'
updated_at: '2025-06-06T16:46:04+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:04:07+00:00'
---

# Original Description
换了好几台机器都是这样。。怎么回事，请帮忙。

严重性	代码	说明	项目	文件	行
错误	C3861	“_mm256_bslli_epi128”: 找不到标识符	xmrig	D:\xmrig-2.11.0\src\crypto\cn_gpu_avx.cpp	123

# Discussion History
## xmrig | 2019-03-01T17:00:50+00:00
@ctqch What version of Visual Studio do you use? Minimum supported version is 2015.
Also you can disable `cn/gpu` support, `-DWITH_CN_GPU=OFF` for cmake.

## ctqch | 2019-03-02T00:09:04+00:00
@xmrig
thanks,问题解决了，可现在又出现了一个新的问题，我是用vs2015编译的。

4>  NetworkState.obj : 找到 MSIL .netmodule 或使用 /GL 编译的模块；正在使用 /LTCG 重新启动链接；将 /LTCG 添加到链接命令行以改进链接器性能
4>LINK : fatal error C1047: 对象或库文件“xmrig.dir\Release\NetworkState.obj”是使用比创建其他对象所用编译器旧的编译器创建的；请重新生成旧的对象和库
4>LINK : fatal error LNK1257: 代码生成失败
4>  命令已退出，代码为 1257。
4>已完成执行任务“Link”的操作 - 失败。
4>已完成在项目“xmrig.vcxproj”中生成目标“Link”的操作 - 失败。

## gostarain | 2019-03-08T08:02:29+00:00
I use vs2017,have same problem,
I find to use xmrig-deps-3.1 with -DWITH_TLS=OFF can avoid this error.

## MacroModel | 2025-06-06T16:46:03+00:00
msvc那坨扔了吧，老msvc那一坨系统根都不更新的。gcc clang老老实实用__builtin_ia32_pslldq512，避免头文件出错


# Action History
- Created by: ctqch | 2019-03-01T05:26:35+00:00
- Closed at: 2019-08-02T12:04:07+00:00
