---
title: 'Send page: displaying (all) in amount field is unspecific'
source_url: https://github.com/monero-project/monero-gui/issues/2466
author: rating89us
assignees: []
labels: []
created_at: '2019-11-23T22:25:12+00:00'
updated_at: '2019-12-01T12:49:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![image](https://user-images.githubusercontent.com/45968869/69486097-44a01f00-0e48-11ea-876e-9b84b56e2f40.png)

Displaying a text "(all)" isn't specific. The user may think "What is (all)? All balance in the wallet? All unlocked balance? All balance in the account?"

Solution: when clicking `All` button, it should just fill the `Amount` field with total balance of the account (value in XMR).

# Discussion History
## aids9345435345kek | 2019-11-26T20:08:46+00:00
> ![image](https://user-images.githubusercontent.com/45968869/69486097-44a01f00-0e48-11ea-876e-9b84b56e2f40.png)
> 
> Displaying a text "(all)" isn't specific. The user may think "What is (all)? All balance in the wallet? All unlocked balance? All balance in the account?"
> 
> Solution: when user clicks All button, it should just fill the amount field with total balance value (in XMR).

I agree with another user that replicating wasabi wallet functionality is desirable i.e the 'all' amount would be all minus the fee and would change dynamically as the user modifies the fee drop-down.

## rating89us | 2019-11-28T06:58:25+00:00
> the 'all' amount would be all minus the fee

And below amount field we could add a text like this:
_+ network fee of 0.000037 XMR (~0.01 USD)_

# Action History
- Created by: rating89us | 2019-11-23T22:25:12+00:00
