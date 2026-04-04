---
title: TOR GetMonero sub-domain address does not work
source_url: https://github.com/monero-project/monero-site/issues/2566
author: One-horse-wagon
assignees: []
labels: []
created_at: '2025-11-18T17:54:08+00:00'
updated_at: '2025-11-18T23:17:45+00:00'
type: issue
status: closed
closed_at: '2025-11-18T22:24:44+00:00'
---

# Original Description
The sub-domain address given in getmonero.org/onion.txt does not work.  When it is entered into the latest TOR browser, all that comes up is a blank page.

I don't know if it's really necessary because when you get to the GetMonero.org site using the main TOR address, the web-site appears to work fine.

In any case, please fix the address or eliminate it from the onion.txt page to avoid confusion.

# Discussion History
## nahuhh | 2025-11-18T18:11:03+00:00
It does work. The download subdomain isnt a website, its the onion where files are hosted

example http://dlmonerotqz47bjuthtko2k7ik2ths4w2rmboddyxw4tz4adebsmijid.onion/gui/linux64

Which is found on http://monerotoruzizulg5ttgat2emf4d6fbmiea25detrmmy7erypseyteyd.onion/downloads/



## nahuhh | 2025-11-18T18:11:05+00:00
It does work. The download subdomain isnt a website, its the onion where files are hosted

example http://dlmonerotqz47bjuthtko2k7ik2ths4w2rmboddyxw4tz4adebsmijid.onion/gui/linux64

Which is found on http://monerotoruzizulg5ttgat2emf4d6fbmiea25detrmmy7erypseyteyd.onion/downloads/



## One-horse-wagon | 2025-11-18T21:40:55+00:00
O.K.  I see the problem now.  You need to add what downloads you want to the sub-domain address.  

# Action History
- Created by: One-horse-wagon | 2025-11-18T17:54:08+00:00
- Closed at: 2025-11-18T22:24:44+00:00
