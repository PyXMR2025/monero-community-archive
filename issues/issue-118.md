---
title: based monero address decentralized IP address, Abolish ipv4 and ipv6
source_url: https://github.com/monero-project/research-lab/issues/118
author: Pantyhose-X
assignees: []
labels: []
created_at: '2024-02-29T08:45:47+00:00'
updated_at: '2024-05-20T16:38:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
THE IDEAL PATH
What if we replace the controlled and surveilled IP addresses with new internet addresses that are based on monero address? These addresses will inherit all monero address features, i.e., they will be purely decentralized, secure, future-proof, robust, anonymous, unhackable, controlled by no single authority and many more.

Is it just a dream? For now. If this could be true we would be changing the internet as we know it.

* monero address + monero DNS, access to monero domain

win10 network adapters : Enter the monero address
Wi-Fi  DHCP Static : Enter the monero address


---
IPv4 and IPv6 are centralized. They are controlled by national companies, etc. 
![](https://www.apnic.net/wp-content/uploads/policy-environment_obsolete/images/ipv4_hierarchy.png)

Try to Google “Who controls IP addresses?” You’ll promptly get “IANA: the Internet Assigned Numbers Authority.” IANA is the top authority behind IP address allocation and assignment. There are five different regional internet registries (RIR) with jurisdiction under the IANA.

As a matter of fact, as an individual or a normal internet user you cannot request IP addresses directly from IANA or one of the five RIRs, but only from internet service providers, such as the services offered by mobile or telecom operators.


* True decentralization, no official singular Foundation, Committee, Corporation, or entities in permanent unitary control of the protocol.

# Discussion History
## SyntheticBird45 | 2024-03-10T10:48:35+00:00
So your proposal is to essentially implement namecoin into monero ? Also the title is off-topic. You can't ban IPv4 or IPv6. These are the instrinsics of the internet, that's why its called Internet Protocol. DNS is giving out IP address to connect to. Or do you refer to an overlay network on top of monero daemon ??

I don't want to sound harsh but you don't understand what you're talking about...

## SorenEricMent | 2024-03-22T07:18:38+00:00
No, it doesn't work that way. Also I think you need to learn what is BGP and RPKI

## ghost | 2024-05-20T01:59:51+00:00
Using Monero's hash address system to replace IPv4 and IPv6 would involve significant changes to internet infrastructure. Here are some potential features and considerations:

1. **Anonymity**: Similar to Monero transactions, users' identities could be obfuscated through cryptographic hashing, enhancing privacy and security online.

2. **Decentralization**: A decentralized network of nodes could manage the assignment and resolution of hash addresses, reducing reliance on centralized authorities.

3. **Scalability**: Hash addresses could potentially offer improved scalability compared to IPv4 and IPv6, allowing for more efficient routing and management of internet traffic.

4. **Resistance to censorship**: Decentralized hash addressing could make it more difficult for governments or other entities to censor or control internet access.

5. **Compatibility**: Transitioning away from IPv4 and IPv6 would require extensive compatibility measures to ensure that existing devices and services can still communicate effectively.

Overall, while using Monero's hash address system to replace IPv4 and IPv6 could offer benefits in terms of privacy, decentralization, and scalability, it would also present significant technical and logistical challenges.

## SorenEricMent | 2024-05-20T05:56:23+00:00
> Using Monero's hash address system to replace IPv4 and IPv6 would involve significant changes to internet infrastructure. Here are some potential features and considerations:
> 
> 1. **Anonymity**: Similar to Monero transactions, users' identities could be obfuscated through cryptographic hashing, enhancing privacy and security online.
> 2. **Decentralization**: A decentralized network of nodes could manage the assignment and resolution of hash addresses, reducing reliance on centralized authorities.
> 3. **Scalability**: Hash addresses could potentially offer improved scalability compared to IPv4 and IPv6, allowing for more efficient routing and management of internet traffic.
> 4. **Resistance to censorship**: Decentralized hash addressing could make it more difficult for governments or other entities to censor or control internet access.
> 5. **Compatibility**: Transitioning away from IPv4 and IPv6 would require extensive compatibility measures to ensure that existing devices and services can still communicate effectively.
> 
> Overall, while using Monero's hash address system to replace IPv4 and IPv6 could offer benefits in terms of privacy, decentralization, and scalability, it would also present significant technical and logistical challenges.

Can you please not put that through ChatGPT and call it a contribution to the discussion 

## molangning | 2024-05-20T06:02:20+00:00
This wouldn’t work at all. The only way I can think of it working is by building it on top of existing protocols (ipv4/ipv6)

## SyntheticBird45 | 2024-05-20T10:45:03+00:00
> This wouldn’t work at all. The only way I can think of it working is by building it on top of existing protocols (ipv4/ipv6)

Yes. That's why I say this make no sense.

> No, it doesn't work that way. Also I think you need to learn what is BGP and RPKI

So you want monero nodes to become autonomous systems? wtf? You do realize AS are meant to be setup at high hierarchical nodes in the tree, everyday users becoming one would make absolutely no fucking sense. Closest you can get from such idea would be Yggdrasil network. Also, AS are all meant to patents and are proprietary, there are no way in the world you can become one if you are not a corporation. Can you at least realize that BGP is two layers upper than IP? meaning BGP requires TCP/UDP which requires IP.

## SorenEricMent | 2024-05-20T15:01:16+00:00
> > This wouldn’t work at all. The only way I can think of it working is by building it on top of existing protocols (ipv4/ipv6)
> 
> Yes. That's why I say this make no sense.
> 
> > No, it doesn't work that way. Also I think you need to learn what is BGP and RPKI
> 
> So you want monero nodes to become autonomous systems? wtf? You do realize AS are meant to be setup at high hierarchical nodes in the tree, everyday users becoming one would make absolutely no fucking sense. Closest you can get from such idea would be Yggdrasil network. Also, AS are all meant to patents and are proprietary, there are no way in the world you can become one if you are not a corporation. Can you at least realize that BGP is two layers upper than IP? meaning BGP requires TCP/UDP which requires IP.

I was replying to OP about BGP and RPKI to tell them the point you just explained in detail but okay

However your explaination is also wrong anyways, individuals can run AS and the ASN will be their name, I have several friends running their own ipv6 AS, also check out DN42.

## SorenEricMent | 2024-05-20T15:04:06+00:00
> So your proposal is to essentially implement namecoin into monero ? Also the title is off-topic. You can't ban IPv4 or IPv6. These are the instrinsics of the internet, that's why its called Internet Protocol. DNS is giving out IP address to connect to. Or do you refer to an overlay network on top of monero daemon ??
> 
> I don't want to sound harsh but you don't understand what you're talking about...

Eh I get it, I was replying to OP, not you

## SyntheticBird45 | 2024-05-20T16:38:26+00:00
I'm confused, somehow I thought you were the OP

# Action History
- Created by: Pantyhose-X | 2024-02-29T08:45:47+00:00
