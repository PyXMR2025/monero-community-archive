---
title: 'monerod loading checkpoint delay and warnings: probable dnsset cause '
source_url: https://github.com/monero-project/monero/issues/3070
author: smurfhat
assignees: []
labels:
- question
created_at: '2018-01-05T17:45:55+00:00'
updated_at: '2018-01-26T12:55:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
With my ISP default dns server set, monerod stalls for 7-10 minutes at the loading checkpoint phase (and there were other problems that I believe could have been related but I have not documented). I say "with my ISP" because when the dns server is changed from theirs to 8.8.8.8 or openNIC the problem(s) goes away. However I have tested that my ISP has configured dnsset using: dig +short +dnssec NS www.moneropulse.se, thus they are dnsset enabled and give a reasonable response to the query, at times giving all the data and sometimes more than other apparently 'working' dns servers (see below). However the responses to the same query vary, even with the same dns server!

Something specific in this variation of responses to dnsset queries seems to me likely the cause, some small detail of configuration to some specific query. Monero code may be at fault in not handling these alternative possible responses adequately. Here are two variant responses to the query above from the same ('not working') dns server at about the same time from two different machines my end:

(not working)

kip.ns.cloudflare.com.
beth.ns.cloudflare.com.
NS 13 2 86400 20180106182331 20180104162331 35273 moneropulse.se. AyArf7HpwWqYC0UBEsfxltN1sDEtX+tEURpS3n/HXj6avJj8p7zt5Jif 1bJCrBXXZUj/ZByAf3sw22UvUw0ykA==

or, (also from the same 'not working' dns server, but from a different machine)

getmonero.org. 
CNAME 13 3 300 20180106110509 20180104090509 35273 moneropulse.se. U0SQIr9GNzaRqqAxS+ySpfgec2x7rY2tH0j/73NQqXmCQ6Zx
AZsNTiB2 ZN20EAYlb+ZakJ/nOdspBfunQTld1w== 
beth.ns.cloudflare.com. 
kip.ns.cloudflare.com. 
NS 13 2 86400 20180106110509 20180104090509 35273 getmonero.org. GQVyN0Uivwdti+4zIMqG4K12y+uNnIZn+80gIXBbRw4iH6roWc
MnkIZp TaQh3JEzjvL4VkA4ZCNRbupwmVNiiA==

And from a 'working' dns server pretty much the same thing:

beth.ns.cloudflare.com.
kip.ns.cloudflare.com.
NS 13 2 86400 20180106110803 20180104090803 35273 moneropulse.se. 5gFDIhrP+hu2MmNMvuFf5UyAHJvkPSIcVlLu8elFMV56o+vMOOHPUXy5 wJ1n/kvCAXuYpwwW8acRy90yNQLU7Q==

So what's the problem?




# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:49:47+00:00
+question

## sammy007 | 2018-01-26T12:54:49+00:00
From where `monerod` does not work until checkpoints (stuck start) and `--check-updates` disabled (slow `exit`).

```
dig +short +dnssec NS www.moneropulse.se
```

```
getmonero.org.
CNAME 13 3 300 20180127135137 20180125115137 35273 moneropulse.se. D5DaHHPvPOjklhfojpEFyktHNb1jWjd0UxOsNZuqfws1z2Wx+j+eA4NO vQHJZgBCgnbVgi9BPjwplsJDZrVhiQ==
kip.ns.cloudflare.com.
beth.ns.cloudflare.com.
NS 13 2 86400 20180127134420 20180125114420 35273 getmonero.org. iUaaLXqSax0IVT0lta1/R+1CsU5oHuXP2dvR22IkxXpikoY7Mg6yKPB3 bcJZPr+Ja3gqKf9Yz8qvbLCv7GMQBQ==
```

From where it works:

```
getmonero.org.
CNAME 13 3 300 20180127135029 20180125115029 35273 moneropulse.se. dOW9Uw9VnkWRJLLVlyKrqQ1zMTfj1NYCz7F/XEesfTf6HVN+deIvoY8T Z7DVtY4i9WOqkSc019QyK7hGCCrO8Q==
beth.ns.cloudflare.com.
kip.ns.cloudflare.com.
NS 13 2 86400 20180127135029 20180125115029 35273 getmonero.org. K2QdnWlvKPF+apM0XkUWy6troNg3PnzbfLaa4qnTkL7Nio9UPHJ1m9mX kfW0mk95kuE4Tw91jC9RahVv8h4z0Q==
```

But it seems not related because responses are equal. Could be connectivity issues from my side.

# Action History
- Created by: smurfhat | 2018-01-05T17:45:55+00:00
