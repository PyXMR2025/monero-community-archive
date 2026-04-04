---
title: 'Bug: alt currencies do not display'
source_url: https://github.com/monero-project/monero-gui/issues/2857
author: Elyytscha
assignees: []
labels: []
created_at: '2020-04-25T11:41:14+00:00'
updated_at: '2025-08-20T07:28:42+00:00'
type: issue
status: closed
closed_at: '2020-04-25T11:42:50+00:00'
---

# Original Description
![image](https://user-images.githubusercontent.com/10408311/80278858-f3979e00-86f9-11ea-9ce6-be2d16197991.png)

basically this is my issue, i can select what i want,

coingecko, kraken or cryptocompare, eur or usd, everthing with this result:

i also tried switching language to english, same result

the version i run is:
![image](https://user-images.githubusercontent.com/10408311/80278891-29d51d80-86fa-11ea-870d-508749c43374.png)

my operating system is:
```
# lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04 LTS
Release:        20.04
Codename:       focal
```

# Discussion History
## selsta | 2020-04-25T11:42:50+00:00
Yep, known bug in linux version of v0.15.0.4, will be fixed in v0.15.1.0 which should be out in 1 to 2 weeks.

## rnhmjoj | 2025-08-20T07:28:42+00:00
I still have this issue as of 0.18.4.1. I tried with different sources and currencies, but the balance is always shown as "?.??".

# Action History
- Created by: Elyytscha | 2020-04-25T11:41:14+00:00
- Closed at: 2020-04-25T11:42:50+00:00
