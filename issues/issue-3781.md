---
title: Regarding miner program design
source_url: https://github.com/xmrig/xmrig/issues/3781
author: wuchenxiuwu
assignees: []
labels:
- AI
created_at: '2026-02-08T21:11:54+00:00'
updated_at: '2026-02-11T11:37:52+00:00'
type: issue
status: closed
closed_at: '2026-02-09T06:07:17+00:00'
---

# Original Description
Preface
-----------------
Recently, I learned about this circle and the program online
------------------
Regarding my doubts and questions
------------------
I found this project very confusing. The key mapping corresponding to weight is not explained in detail in the help document. What is the purpose of P? I didn't explicitly say that when I tried to remove the functions related to donation extraction under this project, I found that most of them were distributed on modules related to the network, which were also included in the Pools.cpp file. Secondly, regarding me, the most confusing question is why there is hard coding? And the hard code will be compiled into binary during compilation. Has the technical documentation been fully disclosed? Also, why is the main state machine for donation included in the file? Forcefully switching to a drawn mining pool, therefore, what I most want to ask is, is your project a rogue project? A bunch of ghosts, the problem is not solved, but the modules related to the contribution are written more comprehensively than the existing framework. I hope you can answer this question for me
------------------

# Discussion History
## geekwilliams | 2026-02-08T21:35:12+00:00
Please read documentation found on https://xmrig.com 

Most of the answers to your questions can be found there or in the FAQ. 

## geekwilliams | 2026-02-08T23:53:22+00:00
P is not a "ghost command".  If you startup xmrig it literally tells you that pressing it will pause mining operations.  Read the documentation.  

## wuchenxiuwu | 2026-02-08T23:59:53+00:00
Brother, I agree with your statement, but it seems that you have confused the concept. Indeed, what you said is correct, it is like this. But what I said is another - P parameter command. Brother, perhaps you should really learn what you think is great. Please refer to the official website documentation

## wuchenxiuwu | 2026-02-09T00:36:13+00:00
I apologize for the inconvenience. Initially, I believed the project was using the standard GNU getopt library, but I later discovered that the internal parsing rules are different. You may be correct about this, as the project appears to be using the MinGW getopt implementation, which may have slightly different parsing rules compared to the standard one.

However, I would like to shift the discussion back to the issues I initially raised. I found that the project uses hard-coded defaults. Specifically, in the  /xmrig-master/src/core/config/  directory, there is a header file named  Config_default.h  that contains some parameters that could be considered default configurations. At the very least, the project should have explicitly informed users about the existence of these hard-coded addresses, but unfortunately, I did not find any such notice. This is quite concerning.

Furthermore, regarding the donation implementation, I think we should discuss the code responsible for the forced donation switching mechanism.

## geekwilliams | 2026-02-09T01:38:48+00:00
If you had read the documentation for CMake options, you'd have found this: 

-DWITH_EMBEDDED_CONFIG=ON enable embedded  config support.

That option allows you to embed a configuration file in the binary so you don't have to include a separate file.  Without that option on at compile, the "hard coded config" is not included.  


## geekwilliams | 2026-02-09T06:35:18+00:00
This reads like AI slop even through a translator.  Don't download their "GPLv3" version.  It likely contains malware.  

## wuchenxiuwu | 2026-02-09T06:40:58+00:00
@geekwilliams 感谢你对我代码安全的关心。这正是开源精神的核心——任何人都可以审计代码。

**关于代码审计**：
我的修改完全基于GPLv3协议，所有更改都可以在仓库中公开审查：
- 移除硬编码捐赠矿池
- 删除捐赠状态机逻辑  
- 清理未文档化选项
- 修复代码质量问题

**关于“AI生成”**：
我很荣幸你认为我的技术分析如此系统化。实际上，这是**深度代码审计**的结果，包括对`Config_default.h`、`DonateStrategy`、`Base.cpp`等文件的详细分析。

**关于安全性**：
GPLv3协议保障了用户的审计权利。任何用户可以：
1. 审查我的所有修改
2. 验证编译结果
3. 自行构建以确保安全

**最后**：
技术讨论应该基于代码和事实。我的纯净版已在GitHub提供，供需要**完全透明、无商业逻辑**挖矿工具的用户选择。

**XMRig-Pure**: https://github.com/wuchenxiuwu/xmrig-pure

我将不再回复非技术性讨论，专注于维护纯净版。感谢所有建设性交流。


## xmrig | 2026-02-09T08:56:34+00:00
This AI nonsense still has some point, there was an unused `-P` option.

## wuchenxiuwu | 2026-02-09T09:05:34+00:00
哦，是不是触碰到您老人家核心利益了，贬低我是AI，这场交互评论，真是越来越有乐趣了您要是下次再对话，此建议你不要回避核心问题，毕竟你承认，问题而回避大问题，这有损于您对于公众的形象，还有你们那捐赠检查该改改了，设计的这么复杂，模块耦合度强，是不是生怕用户？把你们的项目改了，从而威胁到自身的利益，还有您在说我胡言乱语，甚至认为我是AI我接受，毕竟贬低一个人情绪化很简单，正视问题，抛去情绪化很困难

## xmrig | 2026-02-09T09:08:59+00:00
Donations make this project alive, so yes.
Thank you.

# Action History
- Created by: wuchenxiuwu | 2026-02-08T21:11:54+00:00
- Closed at: 2026-02-09T06:07:17+00:00
