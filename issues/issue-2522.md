---
title: 'Receive page: can''t rename Primary address'
source_url: https://github.com/monero-project/monero-gui/issues/2522
author: rating89us
assignees: []
labels: []
created_at: '2019-11-27T19:38:20+00:00'
updated_at: '2021-05-22T01:01:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Current:**
* It's possible to rename all accounts in Accounts page (even the Primary account)
* It's not possible to rename the Primary address in Receive page 
* It's possible to rename all subaddresses in Receive page

Sure, it's important that users learn that the address starting with 4... is their wallet's Primary address, but they still should be able to rename it.

![image](https://user-images.githubusercontent.com/45968869/69753443-ea5ad300-1153-11ea-8755-42175c459afe.png)

**My suggestion:**
* Allow renaming Primary address
* Add "(Primary address)" after user's custom name
* Instead of adding "(Subaddress)" to all subaddresses, indent them below the Primary address, to display that they're a like a branch from it
![image](https://user-images.githubusercontent.com/45968869/69754158-7e796a00-1155-11ea-923a-90d3bd8c599f.png)


# Discussion History
## boogerlad | 2021-05-22T01:01:18+00:00
For the "primary address" that starts with a "4", perhaps it should be indicated it's the only address that's valid for solo mining.

For all other "primary addresses" that start with an "8", it definitely doesn't make sense to be hardcoded as primary address. They should definitely be editable and have no label by default, since they're no different than subsequent subaddresses.


# Action History
- Created by: rating89us | 2019-11-27T19:38:20+00:00
