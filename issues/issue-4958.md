---
title: software upadte system
source_url: https://github.com/monero-project/monero/issues/4958
author: Jasonhcwong
assignees: []
labels: []
created_at: '2018-12-08T14:34:07+00:00'
updated_at: '2018-12-21T20:29:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This issue tries to compare the attacks that TUF and monero's existing software update system(using DNSSEC) can protect against and to see if there is anything we can do to improve monero.  

### Possible attacks:  
According to [TUF spec](https://github.com/theupdateframework/specification/blob/master/tuf-spec.md#the-update-framework-specification) its goal is to protect against the following attacks:

1. Arbitrary installation attacks. An attacker cannot install anything they want on the client system. That is, an attacker cannot provide arbitrary files in response to download requests.  
	**monero**: Hashes of monero binaries are written in TXT record. Client verifys the hashes before use the binaries.  

2. Endless data attacks. An attacker cannot respond to client requests with huge amounts of data (extremely large files) that interfere with the client's system.  
	**monero**: vulnerable to this attack as size of binaries are NOT written in TXT record.  

3. Extraneous dependencies attacks. An attacker cannot cause clients to download or install software dependencies that are not the intended dependencies.  
	**monero**: there is no software dependency, binaries are statically linked.  

4. Fast-forward attacks. An attacker cannot arbitrarily increase the version numbers of metadata files, listed in the snapshot metadata, well beyond the current value and thus tricking a software update system into thinking any subsequent updates are trying to rollback the package to a previous, out-of-date version. In some situations, such as those where there is a maximum possible version number, the perpetrator cannot use a number so high that the system would never be able to match it with the one in the snapshot metadata, and thus new updates could never be downloaded.  

5. Indefinite freeze attacks. An attacker cannot respond to client requests with the same, outdateda metadata without the client being aware of the problem.  
	**monero**: vulnerable to this attack as expire date are NOT written in TXT record.  

6. Malicious mirrors preventing updates. A repository mirror cannot prevent updates from good mirrors.  

7. Mix-and-match attacks. An attacker cannot trick clients into using a combination of metadata that never existed together on the repository at the same time.  
	**monero**: TXT records are groupped and then the group is signed not individual record.  

8. Rollback attacks. An attacker cannot trick clients into installing software that is older than that which the client previously knew to be available.  
	**monero**: Version number of binaries are written in TXT record. Client checks the version number before downloading files.  

9. Slow retrieval attacks. An attacker cannot prevent clients from being aware of interference with receiving updates by responding to client requests so slowly that automated updates never complete.  

10. Vulnerability to key compromises. An attacker, who is able to compromise a single key or less than a given threshold of keys, cannot compromise clients. This includes compromising a single online key (such as only being protected by SSL) or a single offline key (such as most software update systems use to sign files).  
	**monero**: vulnerable to this attack as all moneropulse domains are using the same set of Zone Signing Key.  

11. Wrong software installation. An attacker cannot provide a file (trusted or untrusted) that is not the one the client wanted.  
	**monero**: Hashes of monero binaries are written in TXT record. Client verify the hashes before use the binaries.  


### Suggestions:  

- To protect against attack 2: add size of binaries into TXT records. Client verifys length of HTTP content wiht GET RANGE before downloading.   

- To protect against attack 5: add expiry date into TXT record. Client download the data specified by the expiry date. moneropulse domains must be updated periodically.   

- To protect against attack 10: each moneropulse domain use a different ZSK to sign the same set of TXT records. Client get TXT record sets from all moneropulse domains and use the set that exist on > 50% of domains.  

Any comments?  

# Discussion History
## moneromooo-monero | 2018-12-08T15:49:03+00:00
Thanks for going through this.

For 2, adding file size seems like a good idea.

For 5 (indefinite freeze), it's enough for an ISP level attacker to just filter out DNSSEC. Do you know if DNSSEC records are dated ?


## hyc | 2018-12-08T15:52:17+00:00
Every time anything in a DNS zone is updated the zone serial number should be incremented. Typically serial numbers are YYYYMMDDxx.  Individual records have no datestamps, but DNS updates are per-zone, not per-record.

## fluffypony | 2018-12-08T16:51:28+00:00
> For 5 (indefinite freeze), it's enough for an ISP level attacker to just filter out DNSSEC. Do you know if DNSSEC records are dated ?

Not true - nobody can lie about a DNSSEC-signed zone or record existing (ie. pretend it doesn't exist), see the NSEC3 record type. And with DoH (rapidly becoming the standard) your ISP doesn't even know the queries you're making to the DNS server, so they can't freeze you out any more than they can freeze you out of all Internet access.

A good reference to learn how DNSSEC works [is provided by CloudFlare here](https://www.cloudflare.com/dns/dnssec/how-dnssec-works/).

## moneromooo-monero | 2018-12-08T17:43:11+00:00
They don't have to lie, just drop DNSSEC traffic, since it's distinguishable. And their own DNS server just happens to not support DNSSEC, so monero will not do anything.
About the ISP being unable to distinguish, citation needed. Pretty much everywhere I've seen, this is cleartext.

## fluffypony | 2018-12-10T13:54:08+00:00
@moneromooo-monero the push for DoH to be the standard is recent, only really went through in August 2018, but there is a BIG BIG push from pretty much everyone in the industry to move to it. It's still going to be a couple of years before it becomes the de facto standard on routers and operating systems and so on, but in the meantime the quick hack is to run ```knot-resolver``` with something like ```policy.add(policy.all(policy.TLS_FORWARD({{'1.1.1.1', hostname='1.1.1.1'}})))``` in ```kresd/config``` on macOS / Linux / BSD and then do resolution locally.

## fluffypony | 2018-12-10T13:57:35+00:00
In fact, we can just do our own DoH lookups via 1.1.1.1 / 8.8.8.8 / 8.8.4.4 / 9.9.9.9 in the Monero software *if* the ISP doesn't come back with DNSSEC-signed records, all it requires is an HTTP client library that can do TLS.

## moneromooo-monero | 2018-12-10T16:57:02+00:00
Since we do have one (might need some work to make it work well with third party servers thoughy), and provided it's not super complicated, maybe we could do that all the time ?
We get privacy from ISPs and passive snoopers. The DNS server knows who requests what either way. We don't really care about performance here so UDP vs TCP/TLS is no issue. Does UDP have any advantage other than that ? Maybe that it can work everywhere, even through fascist firewalls ? Anything else ?

## Jasonhcwong | 2018-12-16T23:00:18+00:00
> In fact, we can just do our own DoH lookups via 1.1.1.1 / 8.8.8.8 / 8.8.4.4 / 9.9.9.9 in the Monero software _if_ the ISP doesn't come back with DNSSEC-signed records, all it requires is an HTTP client library that can do TLS.

If we use HTTP client or "curl" to do TLS, do we need to  verify the result by manually going through the chain of trust of DNSSEC?

## fluffypony | 2018-12-20T09:56:17+00:00
@moneromooo-monero yes we should do it all the time. UDP has no performance benefit, since we're mostly doing TXT lookups and they're coming back with data larger than a UDP packet, so it has to either upgrade to DNS-over-TCP or send the response in multiple UDP roundtrips which is horrible.

@Jasonhcwong yes absolutely - we're just doing the DNS lookup over HTTPS, and we don't want to rely on the DNS server to do the checking for us. We have the DNSSEC key for the root zone hardcoded in the software, so it's just a matter of stepping through it (which I'm not sure we do right now).

## Jasonhcwong | 2018-12-21T16:51:01+00:00
currently, menero use unbound library to do the verification of us.   
To do DOH we need:  
1. get TXT of updates.moenro.se  
2. get DNSKEY of moneropulse.se to verify TXT of updates.monero.se  
3. get DS of moneropulse.se to verify DNSKEY of moneropulse.se  
4. get DNSKEY of se to verify DS of moneropulse.se  
5. get DS of se to verify DNSKEY of se  
6. get DNSKEY of "." to verify DS of se  
7. use DS of "." to verify DNSKEY of "." andDS of "." is hardcoded in monero  

Cloudflare provides a HTTPS endpoint that support DNS query with JSON format:
```
# get TXT of updates.moenro.se
jason@jason-home:~$ curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=updates.moneropulse.se&do=true&type=TXT'|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1692  100  1692    0     0  10916      0 --:--:-- --:--:-- --:--:-- 10916
{
  "Status": 0,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": true,
  "CD": false,
  "Question": [
    {
      "name": "updates.moneropulse.se.",
      "type": 16
    }
  ],
  "Answer": [
    {
      "name": "updates.moneropulse.se.",
      "type": 16,
      "TTL": 300,
      "data": "\"monero:source:0.13.0.4:d1efa366caa5dc041a35d08b9e49058a57a5639cd233a675ff8ca8f30513b4bb\""
    },
    {
      "name": "updates.moneropulse.se.",
      "type": 16,
      "TTL": 300,
      "data": "\"monero:mac-x64:0.13.0.4:dd859659bf46a11f4bb2de5bddca7c19038758024e32eb7979bc6bf29ef72e56\""
    },
    {
      "name": "updates.moneropulse.se.",
      "type": 16,
      "TTL": 300,
      "data": "\"monero:win-x64:0.13.0.4:d809acd1ed688a4567716cf199c75b51e696a022e6953df3642a8922a48a734a\""
    },
    {
      "name": "updates.moneropulse.se.",
      "type": 16,
      "TTL": 300,
      "data": "\"monero:win-x86:0.13.0.4:f2034f3dc125097c3ae50dff5b0a46798863fab60da8e4f35e4cb8d7d2202741\""
    },
    {
      "name": "updates.moneropulse.se.",
      "type": 16,
      "TTL": 300,
      "data": "\"monero:linux-x64:0.13.0.4:693e1a0210201f65138ace679d1ab1928aca06bb6e679c20d8b4d2d8717e50d6\""
    },
    {
      "name": "updates.moneropulse.se.",
      "type": 16,
      "TTL": 300,
      "data": "\"monero:linux-x86:0.13.0.4:3f02b0de407f944e524afc9d53d7e9ce92bf17ac6e6ef92cd3c22346afc2cb6c\""
    },
    {
      "name": "updates.moneropulse.se.",
      "type": 16,
      "TTL": 300,
      "data": "\"monero:freebsd-x64:0.13.0.4:95bbf57dcae4810077012835a8d369cf3ecac6e1be7b484d0d518c09868a0377\""
    },
    {
      "name": "updates.moneropulse.se.",
      "type": 16,
      "TTL": 300,
      "data": "\"monero:linux-armv7:0.13.0.4:65e2ce5d0abf80ed3b4ecef5babc37445dc4f032457811aafa8a221af78f554a\""
    },
    {
      "name": "updates.moneropulse.se.",
      "type": 46,
      "TTL": 300,
      "data": "TXT 13 3 300 20181221203525 20181219183525 34505 moneropulse.se. uLGLiK7VjWjpwPZLvYnwdzjM0mn6DT4EnpxBoUAFvEiL6dmtwT1SFanv7Up99j9DB29qy9N5XHq17X0ybHa3Bg=="
    }
  ]
}

# get DNSKEY of moneropulse.se to verify TXT of updates.monero.se
jason@jason-home:~$ curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=moneropulse.se&do=true&type=DNSKEY'|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   681  100   681    0     0   5870      0 --:--:-- --:--:-- --:--:--  5870
{
  "Status": 0,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": true,
  "CD": false,
  "Question": [
    {
      "name": "moneropulse.se.",
      "type": 48
    }
  ],
  "Answer": [
    {
      "name": "moneropulse.se.",
      "type": 48,
      "TTL": 2753,
      "data": "256 3 13 oJMRESz5E4gYzS/q6XDrvU1qMPYIjCWzJaOau8XNEZeqCYKD5ar0IRd8KqXXFJkqmVfRvMGPmM1x8fGAa2XhSA=="
    },
    {
      "name": "moneropulse.se.",
      "type": 48,
      "TTL": 2753,
      "data": "257 3 13 mdsswUyr3DPW132mOi8V9xESWE8jTo0dxCjjnopKl+GqJxpVXckHAeF+KkxLbxILfDLUT0rAK9iUzy1L53eKGQ=="
    },
    {
      "name": "moneropulse.se.",
      "type": 46,
      "TTL": 2753,
      "data": "DNSKEY 13 2 3600 20190119181426 20181120181426 2371 moneropulse.se. MyfLjosOlLutssubuVydHOMNBfj2iXqcLmTQO0OXorsitL0/fg2EL84zfuzSVxQDGGgRlmjAHWAm47/EKxRwQw=="
    }
  ]
}

# get DS of moneropulse.se to verify DNSKEY of moneropulse.se
jason@jason-home:~$ curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=moneropulse.se&do=true&type=DS'|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   736  100   736    0     0   6943      0 --:--:-- --:--:-- --:--:--  6943
{
  "Status": 0,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": true,
  "CD": false,
  "Question": [
    {
      "name": "moneropulse.se.",
      "type": 43
    }
  ],
  "Answer": [
    {
      "name": "moneropulse.se.",
      "type": 43,
      "TTL": 2694,
      "data": "2371 13 2 842FC50EB203197BE86A9D23141ADBADA7112D94486D029C75BA8C1BC405B833"
    },
    {
      "name": "moneropulse.se.",
      "type": 46,
      "TTL": 2694,
      "data": "DS 8 2 3600 20190102110024 20181220041039 38244 se. SJjFSLIMFu68tN0PGRDSwzWW/EslEtcFA/pRN0cs9Lp7z5PHc9WhwXN6zC/X60S/qRuxntRj81Mf0YVHkmhrqG1bhRe+dou805gtPbx6MwCzpchyyvofOAQSe3Uv6Y0rKi5gwBVXvPf8C9QHd/+3QktIWxYe3Iay6KgdaN43mJ18OvpV4cm/1g6TCOKT3yxQ8u0klf3L3rVdviQBMXqubUmgKxZIHoTJY7UlqbtLGWeO1QhCqMfZ2GI+lRFXSQpYvMd1VvInOCXeiWQAQZNSfmTmwsYHxjoFRri0rVJTTc9nXi8bvZ3mZ3CoV7Mc9LhdoW7+OJwJdy49qoOC44YZ5Q=="
    }
  ]
}

# get DNSKEY of se to verify DS of moneropulse.se
jason@jason-home:~$ curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=se&do=true&type=DNSKEY'|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1392  100  1392    0     0  12888      0 --:--:-- --:--:-- --:--:-- 12888
{
  "Status": 0,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": true,
  "CD": false,
  "Question": [
    {
      "name": "se.",
      "type": 48
    }
  ],
  "Answer": [
    {
      "name": "se.",
      "type": 48,
      "TTL": 111,
      "data": "256 3 8 AwEAAbAO7Kdld5BUSrea9BRLGHwvHl2O5Nfi4chnIgaiX4R2vL5wRYov4s0DFhnEqnwGlWbzU93sgPUbhf8oo77Hiw53FX4Rwnpxix14zIBm4b+C37FDWA83f2thY8B+nTsWcvgfv6qFQz4cvsmNEUgXSpI/mOFbEbx+bh1UQXuwFfQS//FlaPiqkrq492GD3N2mHg9ozeTE0ZdPOctBceJq+oY2Ff7JGcdhRMGOlJAG9powY6FdiCiVgyaW/OCIsRbLkDrS4sAiaWanTW6VM7hz/fL5R/ICcze+Sadt4qktYhENPm04WVQR5RmakmOqueee/NghC2TsVf+Xn2MrBQHiyHE="
    },
    {
      "name": "se.",
      "type": 48,
      "TTL": 111,
      "data": "257 3 8 AwEAAccqQMsh1rhvB3IWXmWZpCrug9MEGCKGteLIvwppyHeHgeBBm3M0p5FV9ImquvxFCnBd6Eey3Vf8SzoTodZ3YrGF9WFve7bmie2MIBhFDoCep16v9lon0ZsKrOvoCkPbTT0iFCdrbdyikYcCfvvh303anvQeTCf3jy+bHOTleaqVaNRJiGv5NBsPKpfnnqBpqqKyZymSpwQXHtTeyv7iWwGl3cfP3U6sp711WvKkXy7Y2DJnC5T5owHWUy1ZPl4s+9DtuC2A9AWhOpDicguHYRfmyscjCbPOB8/tO5j+uECo67i7JjsiLjQTRyHuigUUBRag3Z3FaTXZBg/myaoUL0U="
    },
    {
      "name": "se.",
      "type": 46,
      "TTL": 111,
      "data": "DNSKEY 8 1 3600 20190102082439 20181220191039 59407 se. pmbo885hkPUYBjB2KFw5nMvp+gsuVaNY+l5oyrFpjx/daDDD/r3ADrFpf53+CFyzNQG+refKb1BM8KVmTw8shoe9v6+km3t/iXvT4XWupMyNVdUuO38Q2+ayjR6ixqm+fkzrtxjYT+IpqyWbTPBXHwPgkpuiDhMOLSH4OjqfvwPXnQi7Mp8/y4aNBKNpkprN0Yoyev7KqH1Hg5rTTbvWWFgYCjGclEj9Z/efB6ECRidra7yT4aGt9DdoFGriH6fvmUHLngQ6YlcQKiq5FgYfmKQ4WHy4MYm9I3aCjcZqxju/B6xJKlON4hmIdVFAaZHpZcJ25BDerVW0hc5aQvMYuQ=="
    }
  ]
}

# get DS of se to verify DNSKEY of se
jason@jason-home:~$ curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=se&do=true&type=DS'|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   698  100   698    0     0   6176      0 --:--:-- --:--:-- --:--:--  6176
{
  "Status": 0,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": true,
  "CD": false,
  "Question": [
    {
      "name": "se.",
      "type": 43
    }
  ],
  "Answer": [
    {
      "name": "se.",
      "type": 43,
      "TTL": 9517,
      "data": "59407 8 2 67A8E06FCEFDD9397F77F26C41ADE4EC142F299BCFA1827F0EF8FD87F2F63022"
    },
    {
      "name": "se.",
      "type": 46,
      "TTL": 9517,
      "data": "DS 8 1 86400 20190103050000 20181221040000 2134 . SLYOH7RVQCY41prYoljlPrEcRS3bHQurm11fgdP2qQ32t0SQQfCl7GCYl9xYSH3iAyW1hRj5TAhc87ojNcQrg/dXObdk5E81xxPDxDn9LtxIBcDzdrXpd4eI7tM+ji6Q30vhKy3ikc5Vvcr8zi4/vpywO7xG8366w7z8jyfJIywX/Ca7K9mn+liLk4AqUNbkJ43fOBAjxNb+W+bZlE8mnc5exeP83MVrVLOuuUwj90LzIgl1oZ2MXZEQGxSw4+0tDlWoCZ530pv6C/7kZkcsNK9Z42Qo1Iz5cLOY1sor4VVo6k95R+TsaultEnHXBHG5MIufo64n9fyIkqPyELKz2g=="
    }
  ]
}

# get DNSKEY of . to verify DS of se
jason@jason-home:~$ curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-query?name=.&do=true&type=DNSKEY'|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2201  100  2201    0     0  21163      0 --:--:-- --:--:-- --:--:-- 21163
{
  "Status": 0,
  "TC": false,
  "RD": true,
  "RA": true,
  "AD": true,
  "CD": false,
  "Question": [
    {
      "name": ".",
      "type": 48
    }
  ],
  "Answer": [
    {
      "name": ".",
      "type": 48,
      "TTL": 9447,
      "data": "256 3 8 AwEAAcH+axCdUOsTc9o+jmyVq5rsGTh1EcatSumPqEfsPBT+whyj0/UhD7cWeixV9Wqzj/cnqs8iWELqhdzGX41ZtaNQUfWNfOriASnWmX2D9m/EunplHu8nMSlDnDcT7+llE9tjk5HI1Sr7d9N16ZTIrbVALf65VB2ABbBG39dyAb7tz21PICJbSp2cd77UF7NFqEVkqohl/LkDw+7Apalmp0qAQT1Mgwi2cVxZMKUiciA6EqS+KNajf0A6olO2oEhZnGGY6b1LTg34/YfHdiIIZQqAfqbieruCGHRiSscC2ZE7iNreL/76f4JyIEUNkt6bQA29JsegxorLzQkpF7NKqZc="
    },
    {
      "name": ".",
      "type": 48,
      "TTL": 9447,
      "data": "256 3 8 AwEAAdp440E6Mz7c+Vl4sPd0lTv2Qnc85dTW64j0RDD7sS/zwxWDJ3QRES2VKDO0OXLMqVJSs2YCCSDKuZXpDPuf++YfAu0j7lzYYdWTGwyNZhEaXtMQJIKYB96pW6cRkiG2Dn8S2vvo/PxW9PKQsyLbtd8PcwWglHgReBVp7kEv/Dd+3b3YMukt4jnWgDUddAySg558Zld+c9eGWkgWoOiuhg4rQRkFstMX1pRyOSHcZuH38o1WcsT4y3eT0U/SR6TOSLIB/8Ftirux/h297oS7tCcwSPt0wwry5OFNTlfMo8v7WGurogfk8hPipf7TTKHIi20LWen5RCsvYsQBkYGpF78="
    },
    {
      "name": ".",
      "type": 48,
      "TTL": 9447,
      "data": "257 3 8 AwEAAagAIKlVZrpC6Ia7gEzahOR+9W29euxhJhVVLOyQbSEW0O8gcCjFFVQUTf6v58fLjwBd0YI0EzrAcQqBGCzh/RStIoO8g0NfnfL2MTJRkxoXbfDaUeVPQuYEhg37NZWAJQ9VnMVDxP/VHL496M/QZxkjf5/Efucp2gaDX6RS6CXpoY68LsvPVjR0ZSwzz1apAzvN9dlzEheX7ICJBBtuA6G3LQpzW5hOA2hzCTMjJPJ8LbqF6dsV6DoBQzgul0sGIcGOYl7OyQdXfZ57relSQageu+ipAdTTJ25AsRTAoub8ONGcLmqrAmRLKBP1dfwhYB4N7knNnulqQxA+Uk1ihz0="
    },
    {
      "name": ".",
      "type": 48,
      "TTL": 9447,
      "data": "257 3 8 AwEAAaz/tAm8yTn4Mfeh5eyI96WSVexTBAvkMgJzkKTOiW1vkIbzxeF3+/4RgWOq7HrxRixHlFlExOLAJr5emLvN7SWXgnLh4+B5xQlNVz8Og8kvArMtNROxVQuCaSnIDdD5LKyWbRd2n9WGe2R8PzgCmr3EgVLrjyBxWezF0jLHwVN8efS3rCj/EWgvIWgb9tarpVUDK/b58Da+sqqls3eNbuv7pr+eoZG+SrDK6nWeL3c6H5Apxz7LjVc1uTIdsIXxuOLYA4/ilBmSVIzuDWfdRUfhHdY6+cn8HFRm+2hM8AnXGXws9555KrUB5qihylGa8subX2Nn6UwNR1AkUTV74bU="
    },
    {
      "name": ".",
      "type": 46,
      "TTL": 9447,
      "data": "DNSKEY 8 0 172800 20190110000000 20181220000000 20326 . TL1fudz2XHfZ3FS7io96k3VQPJaPO+vpVdIvv2+zsYmjri2QChevm1RnfjA0t4rBBnmYzz3xNnM46Gtyr2hiLW6vGPyNLpkpev2dBOHQSsOu5j5pOXq76c8SHrS65j2V15GFEeLduOOr/yVrhdZJVUpfPGvbWI8CJw4xE6FV88GrMe1bR3YvbogC/nUWdC5/tZvH3vnpnFyY8zp0DoIAMoPs3eO7iDEo/L4YExgv4Mw5To2/2Eml/JG2c8KMwXe8a5KpwDKYnJOcfwvo4CZPXlnHHhrsTGzEQY1naz3UunWZZzgyVF8OYCbGuHPR3gEs5HbiFCxwVWRMDO9pwzJeqA=="
    }
  ]
}
```

http://dnsviz.net/d/updates.moneropulse.se/dnssec/ provides a visualization of the verification.

## moneromooo-monero | 2018-12-21T20:29:32+00:00
You'd want to get unbound to do the verification for you, it's horrendously complex otherwise AFAICT.

# Action History
- Created by: Jasonhcwong | 2018-12-08T14:34:07+00:00
