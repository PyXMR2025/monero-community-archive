---
title: Monero Research Lab Meeting - Wed 15 September 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/610
author: Rucknium
assignees: []
labels: []
created_at: '2021-09-13T06:11:23+00:00'
updated_at: '2021-09-22T18:44:55+00:00'
type: issue
status: closed
closed_at: '2021-09-22T17:57:11+00:00'
---

# Original Description
Time: Wed 15 September 2021 @ 17:00 UTC

Location: #monero-research-lab (IRC/Matrix)

Main discussion topics:

- Triptych vs. alternatives
- Improvements to the mixin selection algorithm ( https://github.com/monero-project/research-lab/issues/86  ) @j-berman @Rucknium 
- Removing/fixing/encrypting unlock time (https://github.com/monero-project/research-lab/issues/78) (it also affects binning)
- Analysis of July-Aug 2021 tx volume anomaly (?) ( isthmus? { @Mitchellpkt } )
- [Active recruitment of technical talent](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)  @Rucknium & others
- MRL structure (why aren't things getting done?).


# Discussion History
## rbrunner7 | 2021-09-13T16:35:11+00:00
Wow, that's one epic topic list. You could easily do 5 meetings for these 5 points, IMHO, and maybe there really should be more than one.

## Rucknium | 2021-09-13T16:37:39+00:00
@rbrunner7 I suppose we could triage the need for further meetings at this meeting itself.

## zkao | 2021-09-14T10:51:13+00:00
there was a related discussion on the recruitment/maintenance of talent [on reddit](https://www.reddit.com/r/Monero/comments/n2njsk/how_to_increase_the_number_of_cryptographers_and/)




## Rucknium | 2021-09-14T13:56:04+00:00
> there was a related discussion on the recruitment/maintenance of talent [on reddit](https://www.reddit.com/r/Monero/comments/n2njsk/how_to_increase_the_number_of_cryptographers_and/)

Interesting. Thanks. The top reply there is about scholarships, though, which is not the way to go IMHO.

## carrington1859 | 2021-09-15T18:15:09+00:00
17:01:05 _UkoeHB> let the meeting commence. Logs will be posted on the issue: https://github.com/monero-project/meta/issues/610
17:01:18 _UkoeHB> 1. greetings
17:01:22 _UkoeHB> hello everyone
17:01:26 _Rucknium[m]> Isn't carrington  running one of the Monero Community meetings soon? carrington  , could you run this one too? I don't know if you are busy though carringtonn
17:01:30 _ArticMine> Hi
17:01:40 _neptune> Hello
17:01:41 _sgp_[m]> hello
17:01:41 _rbrunner> Hoi zäme
17:01:47 _coinstudent2048[> Hello
17:01:49 _Rucknium[m]> Hi.
17:01:50 _one-horse-wagon[> hello
17:01:52 _sgp_[m]> I'm cool with koe running for now
17:01:54 _crypto_grampy[m]> Hi all
17:01:56 _d3neon[m]> hi
17:02:01 _jberman[m]> Hello!
17:02:07 _sgp_[m]> sarang and brandon ran most of the previous ones and they always had agenda items
17:02:13 _carrington[m]> Hello. A researcher should run the MRL meetings, not me
17:02:14 _janowitz> Hi
17:02:33 _wfaressuissia> Hello
17:02:34 _UkoeHB> 2. updates. People working on stuff, a brief summary of what you have been up to.
17:02:42 _ErCiccione> hi
17:02:49 _woodser[m]> hello
17:03:40 _Halver[m]> hi
17:05:16 _Rucknium[m]> My main thing is working on a roadmap to improve the mixin selection algorithm. Within 12 hours I will submit the roadmap to the Vulnerability Response Process in part so that moneromooo and luigi1111w can redact any sensitive parts before release. jberman and isthmus  have seen a draft of it.
17:05:33 _Rucknium[m]> The I sill submit a CCS proposal to execute it
17:05:44 _Rucknium[m]> * will submit
17:06:08 _UkoeHB> Lots of people here :). My summary: The past couple weeks I have been working on PoC for Seraphis. Right now I have working performance mock-ups of RingCT with CLSAG and Triptych on my branch (https://github.com/UkoeHB/monero/tree/seraphis_perf), and have a good plan for building out the Seraphis PoC. There are a lot of variations to perf test, so it is taking me a while to design things properly.
17:06:26 _coinstudent2048[> So Lelantus Spark is out with security proofs. I am working on Seraphis's security proofs. Need verification of security properties I wrote here: https://github.com/UkoeHB/Seraphis/issues/2#issuecomment-918639450
17:07:30 _UkoeHB> Lelantus Spark: https://eprint.iacr.org/2021/1173
17:08:25 _coinstudent2048[> But since Lelantus Spark is "somewhat" of an instance of Seraphis, I guess I'll just "align" my security analysis...
17:08:43 _UkoeHB> I will give about 3-5mins more for summaries then we can move to discussion :)
17:08:46 _sgp_[m]> Here's a good casual discussion on Lelantus Spark https://www.youtube.com/watch?v=vEZC1fTYRZk
17:09:04 _UkoeHB> jberman[m]: would you like to update us?
17:09:24 _jberman> My summary: recommended patching integer truncation in the wallet & reducing the "recent spend window" (https://github.com/monero-project/monero/pull/7798#issuecomment-917495021), did a bit more research into the decoy selection algorithm adding the effect of MyMonero+Monero-LWS & openmonero to the mix in response to some of vtnerd's feedback and
17:09:25 _jberman> criticisms (https://github.com/monero-project/research-lab/issues/86#issuecomment-915806414), worked on other non-research related tasks, and hoping to talk about binning in today's meeting
17:11:18 _UkoeHB> Re: binning, my binning proposal was updated a while back (final draft kind of form) https://github.com/monero-project/research-lab/issues/84
17:12:17 _UkoeHB> Also research related:
17:12:17 _UkoeHB> - fee updates have been PRd and I have comments: https://github.com/monero-project/monero/pull/7819
17:12:17 _UkoeHB> - multisig address generation fixes have been PRd: https://github.com/monero-project/monero/pull/7877
17:12:34 _UkoeHB> Anyone else?
17:13:22 _sgp_[m]> ty for reviewing the fee changes
17:13:49 _UkoeHB> 3. discussion. Ok I think we can move on. The remainder of the meeting is open ended.
17:14:03 _sgp_[m]> are we accepting ArticMine's growth parameters then? am I the only one who is concerned with them?
17:14:29 _UkoeHB> I don't have a strong opinion
17:14:34 _moneromooo> Ping me when you comment on PRs, I seldom check the repo nowadays.
17:14:44 _Rucknium[m]> sgp_:  I suppose I could look at them.
17:14:44 _UkoeHB> ah gotcha
17:15:28 _gingeropolous> sgp_[m], can u briefly summarize ure concerns?
17:15:36 _Rucknium[m]> I am an economist after all. Maybe I have something to say about fees.
17:15:51 _ArticMine> I responded to the growth parameters in MRL issue 70 and the pr
17:16:06 _gingeropolous> ok
17:16:42 _sgp_[m]> gingeropolous: it's just a generous growth rate allowed
17:16:58 _sgp_[m]> we don't need to talk about this here among all the other important stuff, but I am worried it is too generous
17:17:08 _UkoeHB> sgp_[m]: It may be good to circle back to that issue after the fee PR is ready to merge.
17:17:49 _sgp_[m]> ok
17:17:55 _gingeropolous> i think Rucknium[m]'s input will be valuable, because it is effectively monetary policy
17:18:01 _ArticMine> Just a note if you change the grwoth parameters on has to change the whole fee calulation
17:18:28 _ArticMine> So I would suggest this not be left to the last minute
17:19:15 _gingeropolous> so whats all the other important stuff? :)
17:19:35 _Rucknium[m]> Triptych vs. alternatives... (full message at https://libera.ems.host/_matrix/media/r0/download/libera.chat/ae5111e8ad7cef1dddd03a40c2a19fde0eed447c)
17:19:38 _UkoeHB> It sounds like there isn't anything new to add in this meeting, just a call to action: please take a look if you can (MRL issue 70 and PR 7819).
17:20:19 _gingeropolous> for those that can't do links
17:20:21 _gingeropolous> Triptych vs. alternatives
17:20:21 _gingeropolous> Improvements to the mixin selection algorithm (
17:20:21 _gingeropolous> Decoy Selection Algorithm - Areas to Improve research-lab#86 ) @j-berman @Rucknium
17:20:21 _gingeropolous> Removing/fixing/encrypting unlock time (
17:20:22 _gingeropolous> Removing/Fixing/Encrypting monero's timelocks research-lab#78) (it also affects binning)
17:20:23 _gingeropolous> Analysis of July-Aug 2021 tx volume anomaly (?) ( isthmus? { @Mitchellpkt } )
17:20:24 _gingeropolous> Active recruitment of technical talent @Rucknium & others
17:20:26 _gingeropolous> MRL structure (why aren't things getting done?).
17:20:38 _gingeropolous> (from Rucknium[m] 's matrix post)
17:21:24 _Rucknium[m]> Oh, long Matrix posts don't come through nicely on IRC?
17:21:49 _UkoeHB> These are the items from https://github.com/monero-project/meta/issues/610
17:21:59 _UkoeHB> - does anyone have comments/questions about Triptych vs alternatives?
17:22:44 _ArticMine> Do we have some concise figures on verification time / tx size for comparison?
17:22:47 _sgp_[m]> I have one question because we haven't really discussed this during a meeting specifically as far as I understand, but it has been discussed elsewhere:
17:22:57 _wfaressuissia> questions: Triptych isn't competitive even with ideal multisig or multisig is the only blocker ?
17:23:00 _UkoeHB> ArticMine: I am working on perf tests for that.
17:23:07 _one-horse-wagon[> Has anyone looked at RingCT 3.0 as an alternative to Triptych?
17:23:10 _sethsimmons> UkoeHB: My continued preference is explore Seraphis/Lelantus Spark and move to a hard-fork with ring-size change in the meantime.
17:23:14 _ArticMine> Thanks
17:23:21 _sethsimmons> Due to improved view keys and multi-sig simplicity, mainly.
17:23:24 _rbrunner> Well, I have the comment that I can't comment because I am not able to read Sarang's paper and decide how the UX and UI for multisig would change.
17:23:37 _sgp_[m]> Which of the following is more important: 1) easy transition with compatible address format, or 2) easy multisig
17:23:46 _rbrunner> I.e. how much more complicated to transact?
17:23:48 _sgp_[m]> I vote 2
17:23:49 _sethsimmons> wfaressuissia[m]: Multisig is the main blocker, but there are other advantages to Seraphis/Lelantus Spark.
17:25:00 _ArticMine> I have to agree with sethsimmons after speaking with sarang at DefCon after his talk. The Multisig simplicity is very significant in my view
17:25:17 _ErCiccione> I would prioritise whatever gives us a good and usable multisig.
17:25:27 _rbrunner> Quite some unknown how we would fare with an address format change I guess
17:25:34 _rbrunner> Sounds quite radical
17:25:36 _ct[m]> sgp_[m]: I assume the new sofware would prevent users from using old addresses?
17:25:44 _UkoeHB> wfaressuissia: Seraphis in general has several other benefits over Triptych.
17:25:44 _UkoeHB> 1. possibly more efficient (TBD)
17:25:44 _UkoeHB> 2. new features: membership proof delegation (allows tx chaining, offloading membership proofs to third parties, reduces timing analysis of slow tx like multisig), collaborative funding (multiple funders for a tx without big crypto design effort), better address schemes (several variations)
17:25:45 _ct[m]> s/sofware/software/
17:25:58 _Rucknium[m]> BCH more or less did an address format change. Could query them on how to do it right
17:26:24 _rbrunner> Interesting
17:26:28 _x3nu[m]> Could address size decrease?
17:26:51 _ErCiccione> The new format address not be backward compatible?
17:26:55 _gingeropolous> i imagine with a hardfork, it would be easy to protect users re: address change. 
17:27:00 _UkoeHB> x3nu[m]: there are two sets of address scheme variations, one set is larger
17:27:09 _sgp_[m]> proper view keys that show the whole balance (while also allowing view keys as we know them today) is a large win
17:27:13 _UkoeHB> ErCiccione: backward compatible?
17:27:19 _Rucknium[m]> UkoeHB: "collaborative funding (multiple funders for a tx without big crypto design effort)"  Does that mean that a BCH Flipstarter-like crowdfunding system would be easy to put together?
17:27:30 _sgp_[m]> exporting key images is frankly terrible
17:27:35 _UkoeHB> hypothetically - depends on various design decisions
17:27:45 _rbrunner> This new feature list looks so fantastic, somewhat hard to believe for laypeople
17:28:04 _gingeropolous> sgp_[m], smooth would have disagreed, or at least they expressed pause in the past. for reasons i don't fully remember or understand
17:28:25 _sgp_[m]> ErCiccione: people would get new Lelantus Spark/Seraphis addresses
17:28:44 _gingeropolous> re: proper view keys that show whole balance.
17:28:52 _rbrunner> I mean, if we really get all that for an address change, well then ...
17:28:53 _sethsimmons> The biggest issue with the address format change is static addresses used in the past would not be valid/usable.
17:29:06 _sethsimmons> i.e. static donations, saved addresses for friends in address book, etc.
17:29:11 _rbrunner> static = widely published?
17:29:20 _sgp_[m]> haha yeah exactly rbrunner , MANY benefits as I see it
17:29:24 _sethsimmons> As new wallet software after HF would only use the new format, new address generation wouldn't be an issue.
17:29:34 _UkoeHB> gingeropolous: there is an address scheme variant where view-only identifies owned and spent outputs, but can't read amounts. I like this one personally.
17:29:35 _ErCiccione> sgp_: my question was if the precedent format will be still accepted, otherwise would impact ux quite a lot
17:29:41 _sethsimmons> As it's coupled with a HF I don't think it's a huge deal, but it's certainly a bit more headache.
17:29:41 _wfaressuissia> if the base point of comparison is the best non-reviewed and unproven DAP designs, then Triptych isn't competitive even with multisig. If the base point of comparison is current ring signatures with 10 decoys then even Triptych with a bit more complex multisig is an improvement which was expected to deployed soon.
17:29:51 _sgp_[m]> Seth: critically funds sent to those addresses would not be unspendable however
17:29:55 _Rucknium[m]> Zcash is trying to merge t- and z-address formats, I believe. Just another example of another coin doing it.
17:30:00 _sethsimmons> It would not lead to lost funds with a HF, FWIW, just pain for users when merchants/donation acceptance does not update static addresses.
17:30:12 _UkoeHB> ErCiccione: the existing format would have to be rejected
17:30:13 _sgp_[m]> but I assume LS/S funds couldn't be sent to old addresses
17:30:24 _sethsimmons> sgp_[m]: No, wallet software should just reject the address as invalid and prompt that it's old format
17:30:45 _sethsimmons> UkoeHB: Woah, thats cool
17:30:52 _UkoeHB> wfaressuissia: 'soon' is only 'soon' if you find someone to implement that complex multisig
17:31:14 _sethsimmons> Rucknium[m]: This is different, they all still exist and are usable they just basically use a new URI format that can choose among multiple options.
17:31:20 _rbrunner> If I see something as good-looking as this I unvolentarily start to look for the catch :)
17:31:21 _sethsimmons> They aren't phasing out any address format or changing it.
17:31:22 _gingeropolous> i don't think the change in address format is a cause for concern
17:31:29 _sethsimmons> It's just a wallet SDK change.
17:31:42 _d3neon[m]> Would it be possible to convert an old address to a seraphis address?
17:32:07 _sgp_[m]> Triptych is a year + out even if we were fully on board with running with it, which I think is inadvisable at this point
17:32:13 _UkoeHB> d3neon[m]: your private keys would stay the same (or at least your base entropy/mnemonic, depending on design choices)
17:32:20 _ArticMine> One can allow a transition phase afte which sending funds to legacy addresses would not be allowed 6 months would be reasonable
17:32:22 _wfaressuissia> UkoeHB: 2 people were agree to help with implementation: hyc and vtnerd, but that's for the case when design is ready
17:32:25 _sethsimmons> d3neon[m]: New wallet software would just provide new addresses, no conversion needed etc.
17:32:41 _wfaressuissia> Regarding fees. These fees are being used as protection against unlimited blockchain growth (problem with cheap storage and network), unlimited number of malicious txs (problem due to small number of decoys for ring signature) and reward for miners (not very important, since ther is fixed tail emission).  How is it possible to justify decrease or increase of fees without any knowledege of hardware available to miners ?
17:32:45 _d3neon[m]> If you could convert it, that would solve the static address issue
17:33:18 _sethsimmons> d3neon[m]: You just post a new one, don't need to convert.
17:33:27 _sethsimmons> The sender couldn't convert it, FWIW.
17:33:34 _d3neon[m]> alright
17:33:51 _rbrunner> Yeah, a fully automatic conversion tool, based only on the info in the address, would be surprising
17:33:51 _sethsimmons> ArticMine: Yes, that is an option to implement both address formats, but obviously added complexity and code.
17:34:02 _UkoeHB> rbrunner: "I unvolentarily start to look for the catch" The protocol is still experimental and not implemented anywhere - of course there might be a catch no one has seen yet. The more eyes the better.
17:34:04 _gingeropolous> _sgp_[m]> Triptych is a year + out >>> how far out will seraphis / lelantus / superdooper be?
17:34:25 _sgp_[m]> Also Year +
17:34:33 _gingeropolous> or is it 3 +
17:34:45 _x3nu[m]> So a ring decoy increase should be reconsidered then?
17:35:01 _x3nu[m]> As a holdover
17:35:12 _gingeropolous> imo its theater
17:35:12 _UkoeHB> ArticMine: I also think a big transition period would be good.
17:35:26 _sgp_[m]> Firo is planning on Q3 2022 for adoption of Lelantus Spark
17:35:29 _sgp_[m]> just to give a rough idea
17:35:42 _sethsimmons> x3nu[m]: Yes, IMO.
17:35:53 _sgp_[m]> sorry, Q2 2022
17:35:59 _sethsimmons> I think there is pretty broad consensus for a ring-size + BP+ HF with ring-size of 15-17.
17:36:23 _sgp_[m]> Seth: yup
17:36:41 _sethsimmons> But the larger improvements to privacy are likely coming via the decoy selection/binning work being done, TBH.
17:36:53 _merope> wfaressuissia[m]  Fees increase/decrease based on number of transactions being sent. They have nothing to do with mining hardware
17:36:59 _sethsimmons> But ring size bump does help with those in theory, but that's more jbermanRucknium territory
17:37:21 _coinstudent2048[> Hi! I made an attempt to elucidate Seraphis here. Highly incomplete hahaha. UkoeHB please correct mistakes: https://raw.githubusercontent.com/coinstudent2048/writeups/main/seraphis.pdf
17:37:43 _UkoeHB> wfaressuissia: "How is it possible to justify decrease or increase of fees without any knowledege of hardware available to miners ?" The fee PR has two parts. 1) improve the algorithm design to avoid problematic edge cases. 2) increase the minimum fee. Parameter choice is very difficult and somewhat arbitrary, so yes 'how is it possible' is kind of engineering voodoo (which is seen in other engineering fields too).
17:37:58 _gingeropolous> ok, so lelantus spark will be ready Q3 2022 ?
17:38:06 _UkoeHB> coinstudent2048[: cool! I will take a look :)
17:38:08 _rbrunner> We could turn things on the head and ask whether currently anything still speaks *pro* Triptych
17:38:21 _rbrunner> Except an existing but non-multisig implementation
17:38:50 _sethsimmons> gingeropolous: That's their plan, yes, but that's for Firo -- would require implementation for Monero specifically on top of that, but not sure on complexity.
17:39:20 _sgp_[m]> nice coinstudent2048 !
17:40:25 _sethsimmons> There is also a PoC implementation of Lelantus Spark: https://github.com/cypherstack/spark
17:40:26 _ErCiccione> sethsimmons: I'm not sure it worth to make a hard fork now if there are more consensus changes being worked on (assuming they are consensus-related)
17:40:41 _gingeropolous> so i guess, as mentioned before, a key piece of data is compare and contrast lelantus spark / seraphis / triptych re: size and speed etc
17:40:42 _UkoeHB> rbrunner: If Seraphis/etc. turn out to be flops, Triptych is the best known protocol.
17:41:01 _sethsimmons> ErCiccione: Ah, forgot to include fee changes, which should also be included.
17:41:12 _sethsimmons> Past that there are no other consensus changes near-ready that I know of.
17:41:15 _rbrunner> I see, yes
17:41:27 _ErCiccione> I think we should prepare a list of what consensus changes would be included in the next hard fork and then have a dedicated meeting about it
17:41:29 _sethsimmons> And as mentioned a new protocol is still 1y+ out.
17:41:32 _UkoeHB> That being said, Seraphis/etc. don't introduce any crazy new crypto, so it is unlikely.
17:41:54 _coinstudent2048[> UkoeHB: I second this.
17:42:00 _jberman> Agreee with ErCiccione on dedicated meeting about HF
17:42:02 _sethsimmons> ErCiccione: Agreed.
17:42:03 _ErCiccione> UkoeHB: but we need it to support multisig in case
17:42:20 _ErCiccione> meeting again in two weeks then?
17:42:31 _UkoeHB> yes seems appropriate
17:42:38 _ErCiccione> there is enough stuff to talk about in any case i would say, beside the hard fork
17:42:42 _rbrunner> Does Lelantus Spark support multisig then in a reasonable form? Does Firo aim to support multisig?
17:43:01 _sgp_[m]> HF process falls outside of MRL scope mostly and is more of a -dev thing, but yes very important
17:43:22 _sethsimmons> rbrunner: Yes, very simple AFAICT.
17:43:23 _UkoeHB> rbrunner: afaik yes, the Chaum-Pedersen proofs they use can be multisig-d
17:43:30 _sgp_[m]> rbrunner: yes, Lelantus Spark multisig is a dream compared to Triptych
17:43:44 _ErCiccione> meeting in monero-dev sunday 3th 17:00 UTC?
17:43:49 _rbrunner> Nice, one more arrow in the back of Triptych ... ?
17:43:50 _sethsimmons> Pre-print: https://eprint.iacr.org/2021/1173.pdf
17:43:50 _sethsimmons> Github: https://github.com/firoorg/spark-paper
17:43:50 _sethsimmons> PoC: https://github.com/cypherstack/spark
17:44:25 _sgp_[m]> ErCiccione: I'm not aware of any meeting but there should definitely be one imo
17:44:27 _jberman> sounds good to me ErCiccione
17:44:31 _UkoeHB> we should move to another topic, this one took a surprising amount of time
17:44:31 _UkoeHB> - Improvements to the mixin selection algorithm 
17:44:47 _sgp_[m]> rbrunner: that's the main reason not to use Triptych
17:44:50 _jberman> 4 areas to improve decoy selection algo:
17:44:51 _jberman> 1. Integer truncation in the wallet (e.g.: `3 / 2 = 1`)
17:44:51 _jberman> 2. Binning
17:44:52 _jberman> 3. Modifying the distribution estimator (@Rucknium spearheading this)
17:44:52 _ErCiccione> sgp_: yeah, will post in -dev about it if there is consensus here
17:44:52 _jberman> 4. Validating correct algo used at consenus
17:45:11 _sgp_[m]> ErCiccione: yes please do
17:45:45 _jberman> 1. Patching integer truncation
17:45:46 _jberman> Refresher: the decoy selection algo selects *older* outputs than it otherwise would because it truncates an integer (e.g. 3 / 2 = 1, instead of 1.5)
17:45:46 _jberman> I recommended patching integer truncation in the official wallet: https://github.com/monero-project/monero/pull/7798#issuecomment-917495021 (and downsizing the "recent spend window" where the wallet re-selects a young output if the algo suggests a locked output).
17:45:47 _jberman> Summary: patching truncation seems safe on grounds of tx uniformity to me, and I think it's reasonable to assume it would correctly select a decoys that more closely mirror spending patterns.
17:45:58 _jberman> don't think there is much to talk about on that^
17:46:01 _coinstudent2048[> rbrunner: I try to post about Sarang's Triptych multisig paper in MRL/Lounge, but not now.
17:46:15 _rbrunner> TIA!
17:47:17 _UkoeHB> jberman: +1
17:47:43 _jberman> Will give 30 more seconds then moving on to binning
17:47:47 _sgp_[m]> yeah safe to patch
17:48:01 _rbrunner> Lol, bug killed in 30 seconds :)
17:48:23 _jberman> :] 
17:48:34 _jberman> I think binning is blocked by the decision on what to do with unlock times
17:48:35 _jberman> Unlock times have privacy issues (they break tx uniformity & can enable unknowing links), and make binning implementations more vulnerable to particular attacks. So bringing the topic of unlock times back up to try and move toward a decision on what to do with them.
17:48:58 _jberman> Encrypting unlock times is possible at cost of doubling verification time and increasing tx size. Which seems overkill for a feature barely anyone uses today
17:49:10 _jberman> Thoughts on how to reach consensus? Seems no one really loves the feature, so no one cares much about it to go one way or another. Is there precedence for deprecating a feature like this?
17:49:20 _gingeropolous> imo, they seem a novelty 
17:49:40 _sgp_[m]> tbh I'm happy to simply write off binning right now
17:49:41 _selsta> yea, I don't think they are much used
17:49:53 _ErCiccione> maybe a dedicated issue could help? So we can see points in favor and points agains? unless there is already one
17:50:10 _selsta> I don't know any important use cases for them
17:50:28 _merope> wait, I thought atomic swaps relied on lock times?
17:50:31 _gingeropolous> precedence? perhaps axing of the clear format tx id or whatever it was.
17:50:32 _sgp_[m]> ErCiccione: binning has been suggested countless times over many years
17:50:39 _UkoeHB> merope: no on the Monero side
17:50:51 _jberman> ErCiccione dedicated issue for handling the unlock time: https://github.com/monero-project/research-lab/issues/78#issue-726924520
17:50:52 _sgp_[m]> in practice, ringsizes are too small, and it involves many complexities
17:50:57 _merope> (or at least, one of the proposed implementations? comit maybe?)
17:50:57 _Halver[m]> shouldn't a feature like unlock time be treated elsewhere as in the official wallets ?
17:51:00 _rbrunner> Would existing locks honored if we decide to ax them e.g. in our next-gen protocol?
17:51:05 _ErCiccione> jberman: nice. Thanks
17:51:12 _gingeropolous> paymentID. that was deprecated because it didn't do many useful things, but it was replaced with something better.
17:51:21 _gingeropolous> well it did useful things, but poorly
17:51:48 _gingeropolous> perhaps thats something to throw into the lelantus / seraphis thing - can these new protocols do some kind of timelock thinger?
17:51:56 _gingeropolous> in a better way
17:52:19 _isthmus> @rbrunner interesting question, I would lean towards yes
17:52:28 _isthmus> (should honor previous timelocks)
17:52:35 _UkoeHB> rbrunner: yes, since old outputs would be spent using CLSAG
17:52:40 _UkoeHB> so there is no issue
17:52:49 _rbrunner> Ok then, good to know
17:53:13 _sgp_[m]> yup  no issue with past compatibility there :)
17:53:28 _UkoeHB> gingeropolous: not that I know of
17:53:55 _jberman> Will confirm no swap protocol has plans to use the feature
17:54:10 _carrington[m]> A consideration for the next gen transaction protocol should also be whether payment channels are possible
17:54:11 _jberman> Are there any proponents of keeping the lock time assuming not?
17:55:12 _UkoeHB> carrington[m]: I think someone would need to study that specifically.
17:55:17 _sgp_[m]> Well, I'm for keeping the lock time as-is for this hardfork, and I'm cautiously for removing it for the next hardfork (but there's a lot of TBD there)
17:55:31 _gingeropolous> i would vote to deprecate them due to their privacy breaking nature and lack of utility
17:55:59 _rbrunner> I would vote for retiring them with the HF to the next-gen protocol, for a clean cut
17:56:09 _sgp_[m]> gingeropolous: are you suggesting that for this immediate update? way too soon imo
17:56:09 _gingeropolous> i mean they are really only used for 1 purpose currently - im not gonna spend my monero until 2099 ... right?
17:56:19 _isthmus> hahah
17:56:32 _gingeropolous> well no we're not talking what goes into the next hf. thats for the dev discussion :)
17:57:25 _jberman> I figure as soon as someone presents a fleshed out compelling use case that actually needs to use lock times, like payment channels, then there would be no resistance to bringing them back
17:57:32 _UkoeHB> It seems 1hr was not long enough for this meeting, there are still 3 items on the agenda. How about we schedule another meeting for 1wk from now at the same time (1700 UTC), so all agenda items get proper attention?
17:57:41 _sgp_[m]> okay, just good to attack rough timelines to these discussions I think
17:57:41 _Rucknium[m]> Ok I will talk about (3). (Let me know if this doesn't go through to IRC correctly.) I will repost my "update" from above:
17:58:15 _Rucknium[m]> My main thing is working on a roadmap to improve the mixin selection algorithm. Within 12 hours I will submit the roadmap to the Vulnerability Response Process in part so that moneromooo and luigi1111w can redact any sensitive parts before release. jberman and isthmus have seen a draft of it.
17:58:15 _Rucknium[m]> Then I will submit a CCS proposal to execute it
17:58:23 _wfaressuissia> why not to finish right now ? there are a lot of important things and 1 hr / 2 weeks is too small quota to discuss something
17:58:32 _wfaressuissia> s/finish/continue/
17:58:34 _UkoeHB> I am gone in 2mins
17:58:40 _UkoeHB> but the meeting can continue without me if you want
17:59:10 _rbrunner> Seems good to me to adjourn. We are not in such a hurry to do everything today, seems to me
17:59:11 _Rucknium[m]> It's a two-stage execution plan. First, what I have termed Optimal Static Parametric Estimation of Arbitrary Distributions (OSPEAD). It's a medium-term solution to stop the bleeding.
17:59:12 _ArticMine> We can have a meeting in 1 week
17:59:22 _isthmus> I also have to head out
17:59:27 _isthmus> +1 ArticMine
17:59:35 _isthmus> Would be good to reconvene next week
17:59:38 _gingeropolous> weekly ftw
17:59:48 _rbrunner> Older people are also a bit exhousted after one such hour :)
17:59:59 _jberman> In for meeting next week
18:00:01 _Rucknium[m]> I would be OK with weekly. 
18:00:19 _rbrunner> The Return Of The MRL Meetings.
18:00:28 _ArticMine> I am fine with weekly
18:00:43 _carrington[m]> Can someone change the channel description to have the next weeks meeting agenda? Once one is created
18:00:50 _rbrunner> Yeah, at least until the backlog is cleared.
18:01:19 _isthmus> For next week I'll have a postmortem of the transaction volume anomaly from a few weeks ago
18:01:36 _rbrunner> Ah, a cliffhanger
18:01:46 _rbrunner> Clever
18:01:49 _isthmus> ;- )
18:01:50 _isthmus> Tune in next week
18:01:54 _isthmus> Same bat time, same bat channel
18:02:34 _UkoeHB> Can someone grab logs?
18:02:51 _carrington[m]> rucknium[m]: Do you have a write up that can be linked here for people to find in the meeting logs?
18:03:10 _wfaressuissia> "https://libera.monerologs.net/monero-research-lab/20210915/raw" grab or grab&post ?
18:03:39 _Rucknium[m]> carrington: Yes I have a write-up. No, I cannot share it until it has been sanitized by the Vulnerability Response Process.
18:04:39 _sethsimmons> carrington[m]: I can change topic, just ping me once created

## UkoeHB | 2021-09-22T17:56:38+00:00
@Rucknium can you close this issue?

## Rucknium | 2021-09-22T18:44:55+00:00
Thanks, @selsta 

# Action History
- Created by: Rucknium | 2021-09-13T06:11:23+00:00
- Closed at: 2021-09-22T17:57:11+00:00
