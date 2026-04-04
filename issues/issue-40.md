---
title: Collision-resistant address visualization
source_url: https://github.com/monero-project/research-lab/issues/40
author: b-g-goodell
assignees: []
labels: []
created_at: '2018-10-02T03:37:18+00:00'
updated_at: '2018-10-22T16:51:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For easy checking of recipient addresses before sending, a utility for visualizing an address as a unique seashell can be found [here](https://github.com/b-g-goodell/research-lab/tree/master/source-code/iseeseashells); when displaying a public key for receiving Monero, a recipient should also display the corresponding seashell, and a sender ought to be able to generate that seashell locally on their own device (or several) to verify that the recipient address is correct. 

Simple utility, can save a lot of headaches, but requires some nontrivial security precautions to avoid a MITM attack, requires the attention of a designer or someone good with 3d rendering, and so on. Lots of work to be done; the math part is easy (and mostly finished, color and texture maps notwithstanding).

# Discussion History
## stoffu | 2018-10-15T06:38:44+00:00
Since the concept seems general, I got curious if any related attempts have been made before, and arrived at a term [identicon](https://en.wikipedia.org/wiki/Identicon) which is used by [GitHub to generate random user icons](https://blog.github.com/2013-08-14-identicons/). Searching the web with keywords "wallet address identicon" gave me quite some instances of usage in cryptocurrency.

Could we simply adapt these similar solutions, or does the seashell method have some unique advantages?


## b-g-goodell | 2018-10-18T22:06:07+00:00
Short answer: [visual fingerprints](https://tylercipriani.com/blog/2017/09/26/ssh-key-fingerprints-identicons-and-ascii-art/) have a history of [at least 20 years in the literature](https://azrael.digipen.edu/~mmead/www/Courses/CS180/HashVisualization.pdf), especially textual ones in ascii, but they are susceptible to [pre-image attacks](https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_dechand.pdf) (sort of like trying to mimic the first N characters of a vanity address). 

Visualizations like these seashells could be generated with enough parameter choices that it is as hard to find a pre-image for a shell as it is to find a pre-image of a hash. Essentially: boosting the uniqueness/entropy of the shells to match the entropy of the address is an easy mathematical trick under the random oracle model.

Similar solutions that could enjoy similar levels of collision resistance could start from the identicon angle and work outward from there. One idea I had awhile ago would be a randomly generated "galaxy" that uses periodic functions to make something pretty, random, and unique. Another idea is modeling the human iris like an eyeballprint.

Models of succulents would be fun too. The inherent 3d nature of these seashells aren't necessary to enjoy the same levels of collision resistance, perhaps, but 2d images will always be... well... two-dimensional.

One example of how to boost entropy using colors (which is tricky because we will want to ensure that colorblind people aren't more likely to be tricked): to generate a random triple of periodic bivariate functions whose codomains/images are subsets of (-1,1) and whose domain is the unit square (x,y) for 0 < x < 1 and 0 < y < 1, call these three functions R, G, and B, using the following method to pick them, and then pick the color of the point (s,t) on the parameterized surface (or whatever I called those parameters) as R(s,t), G(s,t), B(s,t). We'll pick each from a 90 bit space, totalling a 270 bit selection space for this one colormap (keeping in mind anything above 256 bits can be assumed to be limited by the strength of our hash function).

But how to generate a random periodic function on (-1,1) from a 90 bit space? One way: define R(s,t) as a linear combination of 9 different functions, each of the form a*sin(x/n) + b*cos(y/n) + c for some n from  1 <= n <= 9 and such that sqrt(a^2 + b^2) + c <= 1. this choice of function needs to have at least 10 bits of entropy... so we map from a 10-bit space to (a,b,c) and select from this space at random with replacement 9 times. We sum the results together and we get a random function chosen from a 90-bit function space. Details of how to select (a,b,c) in a way that results in a uniform choice requires a little bit of delicacy, but selecting a at random from (-1, 1), selecting b at random from -sqrt(1-a^2) to +sqrt(1-a^2), and selecting c at random from -1+sqrt(a^2 + b^2) to 1 - sqrt(a^2 + b^2)... but I would need to run some numbers to verify that this yields a uniform distribution on all (a,b,c) choices for each function.

## stoffu | 2018-10-19T07:54:44+00:00
Ah, there's a whole body of prior art, of course. Thanks for sharing these interesting materials. So stuff like [this](https://github.com/ethereum/blockies) would be deemed insecure, I suppose.

I wonder if there exist any other serious/rigorous effort in the whole cryptocurrency space, or even in the academic context. If this is such a sensitive security issue, doesn't it slightly belong to the realm of "don't roll your own crypto"?


## b-g-goodell | 2018-10-22T16:51:14+00:00
Regarding the ethereum identicons: I dunno, I'd have to look at their code. I know colorblind people will not find it as useful as everyone else, and I have no idea how much entropy they are actually cramming into their identicons.

Not rolling your own crypto is a good rule. The risk here is that a collision-non-resistant version gets posted someplace and becomes popular. In this case, people are trusting these identicons or shells or faces even though they are susceptible to collisions, which leads back to the original problem... people having to visually and carefully inspect a sequence of digits or an image before sending. 

I don't think MRL should necessarily do more work in this regard, but I think some wallet project somewhere that picks it up could be better off for it.

# Action History
- Created by: b-g-goodell | 2018-10-02T03:37:18+00:00
