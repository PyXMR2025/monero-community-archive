---
title: Website isn't detecting browser/OS language
source_url: https://github.com/monero-project/monero-site/issues/903
author: erciccione
assignees: []
labels:
- feature
created_at: '2020-04-12T09:07:48+00:00'
updated_at: '2024-03-24T08:19:26+00:00'
type: issue
status: closed
closed_at: '2024-03-24T08:19:26+00:00'
---

# Original Description
*Issue originally created by @asdrub*

*This issue was created on gitlab and then migrated here. Only the original post was migrated, not the comments. Please take a look at the discussions on the original Gitlab issue before commenting here: https://repo.getmonero.org/monero-project/monero-site/-/issues/1030*

---
The website doesn't change automatically to the language of the Browser or OS, even when there is a translated version available. The user must always select the language in the menu.

# Discussion History
## erciccione | 2020-09-13T09:29:43+00:00
I did some research on this. Without using javascript, autodetecting a language is quite annoying. There are other solutions, like serving a cookie and use PHP, but this would be more complex from a legal point of view.

I'm by no mean an expert in this, if somebody has deeper knowledge about this or have a solution in mind, please share your thoughts.

## 00-matt | 2020-09-13T09:34:24+00:00
We can look at the user's Accept-Language header in nginx and redirect appropriately. Maybe something like this:

```conf
map $http_accept_language $lang {
    default en;
    ~es es;
    ~fr fr;
    # ...
}

...

rewrite (.*) $lang/$1;
```

We could also store a cookie when a user selects a language (without PHP), and then redirect them next time based on that.

## erciccione | 2020-09-13T09:43:46+00:00
> We can look at the user's Accept-Language header in nginx

Yes, that's probably the best solution.

> We could also store a cookie when a user selects a language 

That would create problems from a legal point of view and will force us to show an annoying disclaimer. As i just wrote on #monero-site:

> i really don't see auto detection as an important feature to have, so i wouldn't really bother with anything more complex than tweaking nginx (i'm referring to using cookies)
> complex from a legal point of view

## erciccione | 2021-05-17T10:45:50+00:00
I'm looking into this. I asked suggestions to pigeons.

## XfedeX | 2022-05-16T20:53:29+00:00
Aren't cookie disclaimers needed by the GDPR only if cookies can uniquely identify your browser or are used for tracking reasons?

As Regulation (EU) 2016/679 of the European Parlament and of the council of 27 April 2016 states:
```
Natural persons may be associated with online identifiers provided by their devices, applications, tools and protocols, such as internet protocol addresses, cookie identifiers or other identifiers such as radio frequency identification tags. This may leave traces which, in particular when combined with unique identifiers and other information received by the servers, may be used to create profiles of the natural persons and identify them.
```
If I am correct, a language cookie cannot be used to identify you. For this reason I do not think that a disclaimer would be needed.

# Action History
- Created by: erciccione | 2020-04-12T09:07:48+00:00
- Closed at: 2024-03-24T08:19:26+00:00
