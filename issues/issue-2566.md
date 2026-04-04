---
title: 'Send page: wrong sent amount in error message'
source_url: https://github.com/monero-project/monero-gui/issues/2566
author: rating89us
assignees: []
labels: []
created_at: '2019-12-08T10:52:33+00:00'
updated_at: '2019-12-08T10:54:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I have a wallet with a total/unlocked balance of 0.018685273717 XMR.

When I created this transaction with the amount filled with (all) button and using the highest fee,
![image](https://user-images.githubusercontent.com/45968869/70388308-2b52b300-19b0-11ea-860c-41a0a4278233.png)

I got this error:
![image](https://user-images.githubusercontent.com/45968869/70388310-2e4da380-19b0-11ea-970c-a5983b96fa16.png)

When I entered all amount manually and set the highest fee again,
![image](https://user-images.githubusercontent.com/45968869/70388323-69e86d80-19b0-11ea-8c58-49123ae3c319.png)

I got this different error:
![image](https://user-images.githubusercontent.com/45968869/70388325-78368980-19b0-11ea-9ade-0e1c7ce45da1.png)

I was expecting an error message with a sent amount higher than my wallet's balance.


# Discussion History
# Action History
- Created by: rating89us | 2019-12-08T10:52:33+00:00
