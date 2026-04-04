---
title: Remove Google Analytics
source_url: https://github.com/monero-project/monero-site/issues/558
author: leonklingele
assignees: []
labels: []
created_at: '2018-01-17T01:20:18+00:00'
updated_at: '2018-04-14T13:30:13+00:00'
type: issue
status: closed
closed_at: '2018-04-14T13:30:13+00:00'
---

# Original Description
.. for obvious reasons. Not that mostly everyone isn't already using a proper adblocker, it should be done for the sake of our ideology, to give a statement.

Here are some examples of what _could_ be done by a 3rd party on your website (if the script is not src'ed via [SRI — Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)):

- Modify content (e.g. adjust / add donation addresses)
- Censorship
- Tracking. You're feeding the biggest tracking company with even more data and help them to create a fine-grained user profile
- Redirect to other websites
- Execute arbitrary JavaScript to e.g. enable the camera (ask for permissions first), use geolocation, run crypto miners
- .. complete takeover

Also see https://github.com/mymonero/mymonero-app-js/issues/143 which nobody did reply to nor remove the spyware so far.

I guess this is @fluffypony 

There are some self-hosted, open source analytic services available. I'm not an expert but a lot of people are using Piwik (now known under the name »Matomo«).

__EDIT__:
Forgot to mention the most obvious reason: Tracking.

__EDIT 2__:
Why does there even have to be any kind of tracking? What do you currently do with the analytics data? How does it help you / the project?

# Discussion History
## erciccione | 2018-01-18T12:38:39+00:00
Hi we already agreed all referral should be removed from the website, you can find the discussion in #546 

+in progress

## rehrar | 2018-02-12T21:45:26+00:00
I too think Piwik/Matomo would be a better alternative, although some might argue this gives the Core Team control over a large amount of data on users.

## mattcode55 | 2018-02-13T08:51:17+00:00
Could the data from Piwik/Matomo be made public?


On 12/02/18 21:45, rehrar wrote:
>
> I too think Piwik/Matomo would be a better alternative, although some 
> might argue this gives the Core Team control over a large amount of 
> data on users.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub 
> <https://github.com/monero-project/monero-site/issues/558#issuecomment-365072836>, 
> or mute the thread 
> <https://github.com/notifications/unsubscribe-auth/AcREKqA0N9qAaeI15qgIg0BZozHhLuqEks5tULD3gaJpZM4Rgq0Z>.
>



## philiparthurmoore | 2018-04-02T03:19:21+00:00
Coming in on this a little late, but I'm here because I also was curious why tracking is on your site. Question: is the only official Monero site https://getmonero.org/ or do you also own https://monero.org/? The tracking on both sites bothers me for somewhat obvious reasons. :-)

## rehrar | 2018-04-03T01:23:00+00:00
monero.org is not stewarded by the core team. It's a squatter trying to get hundreds of thousands of dollars for the domain name. I cannot answer as to why tracking is on the site, we can ask the core team like @luigi1111 @fluffypony why that is.

what I can say though is we are working on moving away from Google Analytics and moving toward Piwik/Matomo (which is an open-source, self-hosted version.

## philiparthurmoore | 2018-04-03T10:08:20+00:00
@rehrar Thank you very much for the heads up about monero.org, as well as the tracking issue.

## rehrar | 2018-04-09T23:42:31+00:00
@leonklingele @philiparthurmoore @mattcode55 @erciccione 

#680 is ready for review and merge

## erciccione | 2018-04-14T13:24:10+00:00
#680 Was merged

+resolved

# Action History
- Created by: leonklingele | 2018-01-17T01:20:18+00:00
- Closed at: 2018-04-14T13:30:13+00:00
