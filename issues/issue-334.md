---
title: 'Vulnerability Report (1): Misconfigured spf, Protection not used, I can hijack
  your email server'
source_url: https://github.com/monero-project/meta/issues/334
author: raza5402
assignees: []
labels: []
created_at: '2019-04-23T05:54:23+00:00'
updated_at: '2019-04-23T19:59:50+00:00'
type: issue
status: closed
closed_at: '2019-04-23T19:58:56+00:00'
---

# Original Description
Hi Team,

I am a security researcher and I found this vulnerability in https://ww.getmonero.org/
Vulnerability Type: Misconfigured SPF

Description :

this report is about misconfigured spf record flag , which can be use to abuse the organization by posing the identity , which allowing to fake mailing on behalf of respected organization .

About the Issue :

as i seen the SPF and TXT record for the     getmonero.org      which  is

Found v=spf1 record for getmonero.org: 
v=spf1 mx ptr a:mail.getmonero.org ip4:74.220.215.227 ip4:74.220.200.165 include:_spf.google.com ~all 

as u can see the symbol at last which (~all) is the issue , which should be replace by 
(-all) symbol. So valid record will be

Found v=spf1 record for getmonero.org: 
v=spf1 mx ptr a:mail.getmonero.org ip4:74.220.215.227 ip4:74.220.200.165 include:_spf.google.com -all 
  
Whats the issue :

as u can see in the article difference between softmail and fail you should be using fail as Softmail allows anyone to send spoofed emails from your domains.

in current SPF record you should replace  ~ with - at last before all , ~ is strict which prevents all spoofed emails except if you are sending .

Attack Scenario :

an attacker will send phishing mail or anything malicious mail to the victim via mail  example@example.com , even if the victim is aware of phishing attack , he will check the Origin email which will be example@example.com, so he will be sure that its not fake mail and get trapped by attacker !

This can be done using any php mailer tool like this ,

<?php

$to = "VICTIM@example.com";

$subject = "Password Change";

$txt = "Change your password by visiting here - [VIRUS LINK HERE]l";

$headers = "From:    example@example.com  ";

mail($to,$subject,$txt,$headers);

?>

u can check your SPF record form here : http://www.kitterman.com/spf/validate.html !

Reference : https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability

have a look on the digitalocean article for the better understanding !


Please let me know if you need more information.

Looking forward to hear from you.

Sincerely,
Ali Raza


# Discussion History
## fluffypony | 2019-04-23T19:58:56+00:00
Thanks, we're aware of this. It's by design. Nobody should trust unsigned emails anyway.

# Action History
- Created by: raza5402 | 2019-04-23T05:54:23+00:00
- Closed at: 2019-04-23T19:58:56+00:00
