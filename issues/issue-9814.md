---
title: Syntax Error
source_url: https://github.com/monero-project/monero/issues/9814
author: batterhour
assignees: []
labels: []
created_at: '2025-02-23T15:32:20+00:00'
updated_at: '2025-02-23T20:14:58+00:00'
type: issue
status: closed
closed_at: '2025-02-23T20:14:58+00:00'
---

# Original Description
file:
src/debug_utilities/dns_checks.cpp


line 140
`lookup(LOOKUP_TXT, {"testpoints.moneropulse.org", "testpoints.moneropulse.net", "testpoints.moneropulse.co", "testpoints.moneropulse.se");`

Error, there is no closing } , is this how it should be?

# Discussion History
## selsta | 2025-02-23T15:50:37+00:00
That code is basically commented out. Did you use some kind of static analysis tool to find it or how did you run into this?

## batterhour | 2025-02-23T16:09:50+00:00
> Этот код в основном закомментирован. Вы использовали какой-то инструмент статического анализа, чтобы найти его, или как вы с этим столкнулись?

![Image](https://github.com/user-attachments/assets/ef92c9d5-8459-4059-a5b6-6811349723ef)

## selsta | 2025-02-23T16:20:53+00:00
`#if 0` basically means the code is commented out. If someone were to add that code back, they would have to fix the syntax. Since it's not code that gets compiled, it is not neccesary to change it at this point.

# Action History
- Created by: batterhour | 2025-02-23T15:32:20+00:00
- Closed at: 2025-02-23T20:14:58+00:00
