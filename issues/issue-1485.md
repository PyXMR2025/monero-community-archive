---
title: Revise "hangouts" page
source_url: https://github.com/monero-project/monero-site/issues/1485
author: SamsungGalaxyPlayer
assignees: []
labels:
- 💬 discussion
- enhancement
created_at: '2021-02-27T01:15:48+00:00'
updated_at: '2024-06-20T22:47:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The current Hangouts page is unattractive and predominantly contains links to IRC channels only. This is not very user friendly and misses out on quite a huge part of the Monero community.

This revision adds much larger "quick links" at the top to the primary channels and platforms. It adds a link to the Workgroups page. It retains the mailing list link. It also breaks out 4 major community groups that visitors will be commonly drawn to. It removes the resources section, which largely are already in the footer or are no longer used.

### Current

![image](https://user-images.githubusercontent.com/12520755/109370635-bc88a080-7866-11eb-8d5d-9e2bba5162cb.png)


### Proposed

![image](https://user-images.githubusercontent.com/12520755/109370619-ad095780-7866-11eb-8cef-64d233be331f.png)

Related to #1483 #1484 #1486

# Discussion History
## robby-d | 2021-02-27T03:41:32+00:00
I'm personally ambivalent to the big "Monero is its community" text at the top of the redesign. We could shrink that up some or (in my opinion, @SamsungGalaxyPlayer may feel differently) remove it. IMO what is most important is the overall simpler organization of the page that is more useful to the majority of site visitors

## ghost | 2021-02-27T23:09:48+00:00
I could be wrong, but in my opinion it would make more sense to organize by the type of platform rather than the categories shown above. For example, 'Forums' could list the Stack Exchange and subreddits, 'Social' could list the Facebook/Twitter, 'IRC' could list the channels, etc. 

## erciccione | 2021-02-28T08:45:39+00:00
i think what we displayed can be improved, but i don't think such a radical change is necessary. I would add a link to the Workgroup page  and add the other platforms like Discord, etc, but in their own box, where we specify that this are not self-hosted or open source platforms like the others (Taiga, Matrix, Weblate, etc). The way we display the IRC/matrix channels could also be improved.

## tallest-man | 2021-03-01T16:56:46+00:00
I personally like the organization by category (Support, Trading, Mining, Development). But I can see how others might prefer Platform Types as headers. I am of the opinion that the re-design with strong calls to action (Quick Join, Join a Work Group) is preferable from the perspective of the experience of new users / new members of the Monero community. Less text to read and digest on the page, and less "clutter", may result in less mental overload when someone is trying to get involved. 

## robby-d | 2021-03-01T23:33:10+00:00
Here's a potential middle ground:

1. Change icons at the top to larger versions, with the text of what it is (Matrix, Reddit, Discord) under it. With things like reddit, every one knows that logo, but I am unsure what the orange chat box logo is, and most users won't know what the "m" matrix logo is, so having text under I think would help.
2. Add a button for Discord (I really don't think it should be off as a "non-open source" thing... 99% of people don't care, but it is seemingly the most popular chat option by the crypto community at-large right now)
3. Potentially remove the "The Monero community is diverse and varied..." text. It will be skipped by most users and takes up real estate before what users really care about (the icons).
4. Really, really consider swapping that IRC section out for the format that @SamsungGalaxyPlayer has for the 2nd half of the page. Reason being: there are two ways people can think about things when they get to this page: either by medium first, or by category first. With the icons on the top of this page, we take care of the first one (e.g. user thinking "I need a link to the Monero reddit or the Monero discord chat"). But if the user is thinking more like "I'm interested in mining Monero and want to see what community resources are available with that" then the second half of the page will cover that (without forcing them to an IRC chat, when they really would favor the subreddit name). The format that @SamsungGalaxyPlayer has I think is simple and effective, but I would probably reduce the text size some (fonts don't need to be that big). As it is, I think people just see "IRC Channels" and skip it, as virtually no one uses IRC anymore.

## SamsungGalaxyPlayer | 2021-03-02T00:12:15+00:00
The most important thing to me is making common links front and center (and large), like Discord and Reddit.

## erciccione | 2021-03-02T09:13:01+00:00
> I really don't think it should be off as a "non-open source" thing... 99% of people don't care

This is not a valid reason. If we adapt to only what most people care about, this website would be full of moon memes and nothing else. Most of the people don't care about privacy either, but here we are.

I agree the IRC channels section has to go. I'm ok with adding closed source platforms like discord to this page (which at the moment is hosting only open source and/or core hosted platforms), but only if the closed source platforms are labelled as such and in a lower position compared to the open source/self-hosted tools. We spend time and resources to make open source platform available to the public for a reason, it's important to prioritize these tools.

> virtually no one uses IRC anymore

This might be correct in general, but the vast majority of our developers (including all active core members) are on IRC, some are even exclusively there. There is definitely a use for it, so i wouldn't remove it completely.

## robby-d | 2021-03-02T14:17:15+00:00
> I agree the IRC channels section has to go. I'm ok with adding closed source platforms like discord to this page (which at the moment is hosting only open source and/or core hosted platforms), but only if the closed source platforms are labelled as such and in a lower position compared to the open source/self-hosted tools. We spend time and resources to make open source platform available to the public for a reason, it's important to prioritize these tools.

What do you think about using a CSS fieldset to delineate open source from closed source? 
I whipped up a quick hack here: https://jsfiddle.net/3wp8f4ro/1/

This way, we can maintain all of the icons on a single line (preserving usability) while accomplishing your goal of denoting open source/closed source.


## erciccione | 2021-03-03T15:12:04+00:00
That looks nice. I think would be better to add a third box "self-hosted", that would be displayed first. Also, i would also add few words for clarifications, but that's a good starting point!

## robby-d | 2021-03-03T16:41:16+00:00
Sounds good. I'll whip up a PR for this and the home page panel proposed changes and submit within about a week.

## erciccione | 2021-05-26T07:35:20+00:00
@robby-dermody any update on this?

## robby-d | 2021-05-26T11:54:38+00:00
sorry about this, I had started but unfortunately I haven't had any time (moving, new kid, etc). you're of course welcome to take a crack at it off of that jsfiddle code, or you can close this ticket

## apertamono | 2021-09-30T13:57:36+00:00
I agree that we should remove the IRC channel descriptions and make space for more links to different platforms. Sorting by themes rather than platforms is not a bad idea.

But I don't like the focus on icons in both the original, sgp's proposal and robby's sketch. It's unfriendly for new users and visually impaired people. I have some familiarity with cryptocurrencies, but I don't recognize the [m] logo, the orange folder and the speech bubble with blue stripes.

And we shouldn't be so impartial that we're confusing new members of the community. We should make clear which are the most widely used hangouts: /r/Monero and the #monero IRC channel.

The "Join a Workgroup" and "Join the Mailing List" buttons are not directly about hangouts and should be placed lower on the page.

Btw, I considered redesigning the Hangouts page to include links to local meetups, but this wasn't a priority in 2020.

When linking to twitter, we should also include the [Moneristoj](https://twitter.com/i/lists/923503135238311936) list, to represent the whole community.

## HardenedSteel | 2024-06-20T22:47:42+00:00
@SamsungGalaxyPlayer do you have the template for the proposed changes?

# Action History
- Created by: SamsungGalaxyPlayer | 2021-02-27T01:15:48+00:00
