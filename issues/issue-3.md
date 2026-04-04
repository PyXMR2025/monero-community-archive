---
title: Pick up difficulty research
source_url: https://github.com/monero-project/research-lab/issues/3
author: fluffypony
assignees: []
labels: []
created_at: '2016-09-04T14:00:24+00:00'
updated_at: '2018-11-17T22:23:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
The difficulty research that Surae was working on is quite extensive, but incomplete.

Someone would have to pick it up and run with it, as Surae is basically burnt out on difficulty and has moved on to other challenges:)


# Discussion History
## fluffypony | 2016-09-04T14:03:39+00:00
@zawy12 would you be interested in doing some research on difficulty algorithms, the Monero difficulty algorithm in particular, and possibly presenting your ideal algorithm as a suitable replacement? The current state of the research is here: https://github.com/monero-project/research-lab/tree/master/publications/MRL-0006%20-%20Difficulty%20Adjustment%20Algorithms%20in%20Cryptocurrency%20Protocols

If you'd be interested in committing a large portion of time to it we could use the Forum Funding System to crowdfund you on a per-milestone or per-month basis.


## zawy12 | 2016-09-05T11:08:15+00:00
I may work on trying to get it implemented in Monero after I get a finalized version after testing it on the Zcash testnet. The testnet is ideal because it has an occasional attack for testing, but there is not a moment-by-moment competition for blocks.  So it's mostly a real-world Poisson process.  Once an algo works perfectly on that, it can be adjusted to protect against attacks.  And once protected against attacks, it needs to be checked to make sure it has not lost quality when there are no attacks.   I doubt anyone will buy the rights for it so in a few days it will be under creative commons as "zawy difficulty algorithm v1.0".


## zawy12 | 2016-09-09T16:33:21+00:00
I've come to the conclusion that the best difficulty will be a simple rolling average:

next Diff = avg past N Diff \* TargetInterval / Avg past N solve times.

The shorter the window average, the more protection against attacks, but there is  more variation in solve times. This is unavoidable.  There is a law written in stone: if difficulty is allowed to go down, you can have good protection or good solve times with a low standard deviation, but you can't have both.  You have to choose how many blocks you want to "give away" by choosing the max time for say 10% of the block solves.   Low block window averaging is higher protecting but wider swings in solve times.  You could use N=5 for great protection if it is OK to have time to solve > 5x your target for 5% of the blocks. Once manipulators come in, you need to be prepared for 5x target 10% of the time.   But such a short averaging window requires an accurate timestamp on blocks instead of miner generated times.  Without that I would copy what Zcash is doing (N=17 window average with a median instead of mean for the solve times), except be sure not to use the 8% up and 16% down limits they are using, which I hope and suspect they drop before release.  There is something weird with their method of getting the median that works better than the way I get the median, so us eit, which I guess comes from Digishield v3.  But if you get  an accurate timestamp, use the mean.  

And low N averages have accidental spikes in difficulty and solve times.  Miners can choose to come in immediately after those which makes the next difficulty and solve time spike even higher.  so they can put it into oscillation for profit.  But this might be a problem for all windows of even larger N.  

The biggest protection against attacks might be to discover the methods and encourage and enable everyone to use them.  That tends to block the profits of cheaters by actually leveling out the swings, helpig the constant-on miners.   For example, in time warp attack is less and less useful if you initiate it and 10 people come in to take it away, splitting the profit.  So maybe you shoulld give the code to enable everyone to do it. It might then become useless to everyone.   Of you try to pick a bottom, but then someone comes in earlier so your bottom does not occur, and so on, until there is no bottom.

The only way I have found to get **perfect protection** against attackers (and fairness) and to have a  **perfect release schedule**  is to never let the difficulty drop but follow a slow steady rise, use a valid timestamp on solved blocks, and pay miners inversely proportional (Tim Olson's idea) to their solve time relative to the average time that is expected for the current difficulty setting.  If a miner solves fast, he gets paid proportionally less.  If he solves slow, he gets paid more. The coin release schedule stays as perfect as your clock, and there's zero profit from manipulations.  The problem with a clock is that it is a third party.  But it is not a problem if you're already using a subtle 3rd party going under the name of "trusted peers" who will set to a universal time clock.   (The trusted timestamp also prevents timewarp attacks.  ETH uses one.)

This has very important stable, real value implications. For example, miners are paid PER BLOCK for the amount of electricity needed, getting closer to the ideal of value=joules, not merely based on the average electricity expense per block expected.    This requires abandoning the idea that blocks must be solved within a certain time frame.  If the coin can survive post-mining on fees, then it should survive solve delays in the exact same manner to prove it can survive on fees ahead of time.  But it may not result in substantial delays as everything is done so well. 

This probably changes too much in bitcoin's core, and there are likely good reasons Satoshi did not do it.  But it's best by starting with a known ideal and work backwards.  In this case it means every time you let difficulty fall, you are harming constant-on miners relative to other types of miners. 


## zawy12 | 2017-06-19T11:59:09+00:00
Sumokoin and cryptonote have been guided in their difficulty algos by the first part of my comment above and got me to thinking about difficulty again.  I've better formulated exactly what a difficulty algorithm needs to do, and posted it to the [cryptonote thread](https://github.com/seredat/karbowanec/commit/231db5270acb2e673a641a1800be910ce345668a#commitcomment-22615860) 

I'm backtracking in my comment above and going against the median Zcash had told me they are using, and sticking with average.

## fluffypony | 2017-06-19T12:40:23+00:00
@b-g-goodell ^^

## zawy12 | 2017-06-21T04:11:18+00:00
I was able to finish an implementation of the difficulty algorithm that has a dynamic averaging window to protect against 10x attacks while also being smooth at constant hashrates.  It is not yet hardened against timestamp errors.  The charts below compare it to a good simple averaging window of N=18.  Details (my verbosity and errors) and vetting are at [sumokoin](https://github.com/sumoprojects/sumokoin/pull/10)  Cryptonote link above will remain my place for an "executive summary" (it has links to the precise pseudocode for this tentative Zawy v2 (dynamic averagnig window).   I'll post again here if it gets hardened against timestamp errors or implemented in a real coin.

The 10x short attacks are only 15 blocks wide.

![difficulty_zawy_v1](https://user-images.githubusercontent.com/18004719/27366720-e4ca455c-5615-11e7-80f4-74358c7eb598.gif)
![difficulty_zawy_v2](https://user-images.githubusercontent.com/18004719/27366721-e4cbf4f6-5615-11e7-8547-1bb422c8eb43.gif)



## zawy12 | 2017-11-20T05:12:38+00:00
@fluffypony  

It's been a year since my first post above.  As a result of people trying to help BCH's problems, they requested my input and showed me two difficulty algorithms that are better than the simple average I have been proselytizing.  

<strike>BCH messed up again and jumped in with a large N=144. Now they have daily oscillations. Not catastrophic, but not good.  </strike> [Live data from BCH, BTG, ZEC, Hush, Masari, Sumokoin and Karbowanek](https://github.com/zawy12/difficulty-algorithms/issues/6) <strike> indicates using N=30 is the most important step in having an optimal difficulty algorithm.</strike>  BTG avoided Zcash's oscillations by using my recommended N=30 and deleting Zcash's tempering equation.  Zcash is N=17, but they "temper" it, so it acts like N=63.

[Karbowanek will be the first coin](https://github.com/seredat/karbowanec/issues/11#issue-275228023) to employ one of them.

Both of the following algos are substantially better than the simple rolling average.  Apparently Tom and Jacob spent an afternoon thinking about it and came up with something better.  Every coin should use one of these, without modification.     I prefer the 2nd one.

[WHM algorithm](https://github.com/zawy12/difficulty-algorithms/issues/3)

[EMA algorithm](https://github.com/zawy12/difficulty-algorithms/issues/4)


[Tom, Jacob, and others are using python code for testing.](https://github.com/kyuupichan/difficulty)

![excel](https://user-images.githubusercontent.com/18004719/33560871-02d98bf6-d8df-11e7-821a-147c0ae04165.gif)


## jacob-eliosoff | 2017-11-20T05:38:19+00:00
For anyone struggling to grok my admittedly dense EMA algo above, see eg [this explanation](https://github.com/kyuupichan/difficulty/pull/26#issuecomment-342290398).

Big thanks to @zawy12 for making the effort to understand many proposed algorithms, test & compare them, and spread the knowledge around!

## zawy12 | 2017-12-19T00:38:05+00:00
I'm keeping the newest versions of the best algorithms [here](https://github.com/zawy12/difficulty-algorithms/issues/1).

I'm keeping a list of the results of various algorithms [here](https://github.com/zawy12/difficulty-algorithms/issues/6).   It shows how awesome Masari (Monero clone with a lot of difficulty problems) is doing with the WHM N=60. I'm getting them to switch to EMA in next fork.



## zawy12 | 2018-01-06T22:44:18+00:00
We've developed a new algorithm that's the best of the best and allows integer math on the target.

https://github.com/zawy12/difficulty-algorithms/issues/17

## zawy12 | 2018-11-17T22:23:01+00:00
Monero needs to play it safe, but in case it's ever interested, I have a way to change difficulty during the block to make solvetimes a much tighter Poisson.  No more delays.

https://github.com/zawy12/difficulty-algorithms/issues/36

![image](https://user-images.githubusercontent.com/18004719/48666333-6de7db80-ea8d-11e8-9074-45b9114f64ec.png)


# Action History
- Created by: fluffypony | 2016-09-04T14:00:24+00:00
