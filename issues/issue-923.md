---
title: 'CCS Wallet Incident Response. Forensics and Attribution '
source_url: https://github.com/monero-project/meta/issues/923
author: Monero-HackerIndustrial
assignees: []
labels: []
created_at: '2023-11-08T05:12:51+00:00'
updated_at: '2024-07-04T16:49:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Per incident: [CCS Wallet Incident](https://github.com/monero-project/meta/issues/916) 

After the disclosure of the stolen funds there has been a lot of questions of what exactly happened and how an attacker could have gotten access to the funds. I am creating this issue so we can gather the evidence/logs needed to properly investigate the incident and hopefully get some attribution for the attack. 

### Incident Response Plan

#### Preparation

- Timeline creation (Including actions that could potentially be related to incident)
- Inventory of known devices affected
- Create Image of affected devices for forensics. 
  - Create full disk image using DD. 
  - Dump active memory
      -  Windows - [WinPmem](https://github.com/Velocidex/WinPmem)
    -  Linux - [LinPmem](https://github.com/Velocidex/Linpmem)
    - Good primer on mem dump and analyzing [link](https://cyberhacktics.com/memory-forensics-on-windows-10-with-volatility/) 
- Inventory of events from users 

#### Forensics

##### Static Analysis
- 
- Identify IOCs (Indicators of compromise) in the following
    -  Access logs
    - Backdoored accounts / auth keys 
    - Binaries/scripts 
- Identify persistence 
- Memory dump analysis (TBA)

##### Dynamic Analysis (TBA)

- Identify network traffic from host to potential c2 infra 

#### Identify known groups 
There are some known groups who target players in the crypto space. Those actors reuse a lot of TTPs. Identifying the lists of known actors can help give us a starting place for easy IOCs. This is just basic homework and don't expect it to be our main path forward. 


#### Containment and clean up  
If an attacker has persistent access on a machine then we need to contain and eradicate their access. Cleanup can be as simple as removing scheduled tasks to full OS reinstall (which is usually recommended in case anything was missed). 

Other cleanup such as rotating keys, passwords and overall account hardening. (Malware can steal cookies and saved passwords from browsers). This means adding mfa and hardware keys when applicable. 


#### Post Mortem and lessons learned

Any findings are used to complete the description of the attack killchain and provide any context missing from the timeline. 
Any identified threats can then be used to give recommendations for improving the security posture of devs in the future. **This is not a time to place blame but a time to learn and improve.** 



#### Threat modeling 

Monero devs are operating in hostile environment full of bad actors looking to steal funds or potentially target the code base. I can help create processes to mitigate those threats and those processes can be translated to easy to use workbooks for developers to use. 



# Discussion History
## Monero-HackerIndustrial | 2023-11-10T03:05:37+00:00
The plan is after thanksgiving I can walk @luigi1111  through dumping memory, manually saving some logs and configs and then DD for full disk image for anything else that might have missed. 

I intend to do a proper write up on my investigation and any findings that might come of it. 

## dan-is-not-the-man | 2023-12-18T07:50:35+00:00
Any news on this, cause if its a doxxing there is a bigger issue at hand since luigi is continuing to be ccs wallet holder

## Monero-HackerIndustrial | 2023-12-19T02:55:09+00:00
Updating for visibility. Today:
Luigi provided the disk image for the drive and the memory dump for the ubuntu server. 
I transferred both the disk image and the memory image to my lab. 
I now have everything I need to start doing my forensics work. My schedule permitting, I plan on starting before the weekend. 

To recap some previous conversations (@luigi1111 please correct me if I got any of the details wrong):

The ubuntu memory dump was taken before a reboot. 
The full disk image was taken from a live boot environment.  

## mehrexe | 2024-01-25T15:18:35+00:00
Both here and in https://github.com/monero-project/meta/issues/916 there just seems to be not that much of a priority over the fact that project leaders lost **half a million** dollars of community money. 

It's sad we forgot about this so quickly, and it's even more sad that it was hardly discussed in the working group or there isn't any sense of urgency. 

Why does no one care that a life changing amount of money that would've advanced Monero significant disappeared, or the subpar care of its handling, or even worse the lukewarm and minimal response to the situation by the people whose fault it is? 

I get that there's a consensus of having so much faith in XMR that finding whoever did it is more unlikely than likely, but this matter was handled too lightly and forgotten about too quickly. This whole situation bugs me. Either there's complacency, incompetence, or a lot more to the story.

## nahuhh | 2024-01-25T15:23:24+00:00
I moved thr priority from talking in circles > paying devs

we haven't forgotten about anything. Were working against a schedule

## dan-is-not-the-man | 2024-05-28T08:49:41+00:00
Soon :tm: 

## rottenwheel | 2024-06-27T08:33:09+00:00
@c0mmando would you be down to receiving the system image and memory dump @luigi1111 had provided to @Monero-HackerIndustrial and analyzing it? For context, HackerIndustrial never came through with anything and has been MIA for several months. Considering you offered to help in a previous comment... Cc. @plowsof.

## luigi1111 | 2024-07-04T16:49:32+00:00
@c0mmando Please contact me on IRC, and we can work out how to proceed.

# Action History
- Created by: Monero-HackerIndustrial | 2023-11-08T05:12:51+00:00
