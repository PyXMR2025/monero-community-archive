---
title: Would like choice of Esperanto language for mnemonic seed
source_url: https://github.com/monero-project/monero/issues/1738
author: Engelberg
assignees: []
labels: []
created_at: '2017-02-16T05:59:12+00:00'
updated_at: '2017-08-18T13:48:14+00:00'
type: issue
status: closed
closed_at: '2017-08-18T13:48:14+00:00'
---

# Original Description
Given the name of the project, when I installed the official Monero wallet and ran it for the first time, I was rather surprised me when it prompted me for a language and Esperanto wasn't on the list.

# Discussion History
## moneromooo-monero | 2017-02-16T14:03:48+00:00
Feel free to contribute a word list for Esperanto, with unique 4 letter or 3 letter prefixes.

## Engelberg | 2017-02-17T00:09:53+00:00
I can do that.  How many words?

## moneromooo-monero | 2017-02-17T09:21:58+00:00
1626 words. The intent is that they have a unique prefix, typically 3 letter (ie, you can't have duplicate and duped, for example). Also no proper names, words that hopefully are not too esoteric (to the target population). See for example src/mnemonics/italian.h in the monero tree. Supplying a list of words is enough, and I can turn it into a header and plug it wherever it needs to be plugged.


## Engelberg | 2017-02-19T01:23:35+00:00
What's more important: unique 3-letter prefixes (as opposed to 4) or avoiding accented characters?  If I remove all the words that have accented characters, I'm not sure I can make a long enough list with unique 3-letter prefixes.

## moneromooo-monero | 2017-02-19T09:25:26+00:00
Probably avoiding accents I'd say, given this is an international language so we'd want to be able to input it with a wide selection of keyboards. But that's my subjective opinion only.

## apertamono | 2017-02-20T00:51:24+00:00
This should be possible. As a test, I created a list of Esperanto words starting with M, unique for the first 3 letters, avoiding diacritics, names and uncommon words. The result was 70 words. This is slightly below the target of 1626/22=74 words, but there will be more unique words starting with a vowel. 

(There's no Q, W, X and Y in Esperanto. Only Z is uncommon as an initial. I'm not a fluent speaker, but I'm a linguist and I think I can guess which words are common.)

Source: http://www.reta-vortaro.de/revo/ 
My list: http://pastebin.com/WPvTuFVN

## dnaleor | 2017-02-20T09:24:12+00:00
@ProkhorZ we could add Zamenhof just as an exception to the "name rule" ;)

Will try to do some word lists later today for other letters. Will post them here. I'll start with Z, V, U, T, S, ...

edit: Here is a list for Z: http://pastebin.com/TiVHDtYH (20 words)

## apertamono | 2017-02-20T15:54:01+00:00
@dnaleor Great! In that case, I'll work backwards from M to L, K, etc. But I'll be busy this week.

@moneromooo-monero I could also create the header file, I'm looking for easy coding tasks. It would be helpful if you'd add the references to esperanto.h elsewhere. 

## Engelberg | 2017-02-21T07:44:41+00:00
@ProkhorZ @dnaleor I don't want to dissuade you from trying, but I did a quick sanity check by counting _all_ the unique three-letter prefixes among all the unaccented words from the Baza Radikaro, which is one popular wordlist of "common words" by some definition of common.  I even included the rarer groups 6-9, and the "group X".  There are only 948, and that's before removing the proper nouns like continent names (which aren't usually capitalized in Esperanto, but I'm assuming are not desirable in this wordlist), the grammar words (like "adjektivo"), the negative or bodily function words like "vomi" (to vomit), a couple stray abbreviations and punctuated exclamations ("t.e." and "ve!"), etc.
https://gist.github.com/Engelberg/9f117e931d1589fb381c8666a7ee33d5

Going to 4-letter prefixes, I got to 1838, which gave me some room to trim the worst options and still get 1626.

## moneromooo-monero | 2017-02-21T08:36:44+00:00
OK about the header file, I can plug wherever is needed afterwards, thanks.

## apertamono | 2017-02-21T11:08:47+00:00
@Engelberg The Baza Radikaro is a list of about 2500 words, useful for language learners, but of course that wont be enough for our purposes. There are more sources, for instance this page links to a list of 10,000 words: https://eo.wikipedia.org/wiki/Esperantaj_vortaroj_en_la_reto

## dnaleor | 2017-02-21T14:40:57+00:00
so what do we do, stick to 3 or go to 4 letter uniqueness ? 
Was planning to do some letters this week...

edit: by the way, maybe a good idea to also have a more standardized approach to which type of words we choose. I prefer substantives over verbs and verbs over adjectives. 

edit 2: and why aren't we discussing this in esperanto ? ;) 

## apertamono | 2017-02-21T20:17:55+00:00
I still prefer 3-letter unique prefixes. We could always go from 3 to 4 if necessary. 

And I actually prefer a mix of word types, just like the lists for the other languages. Every word ending in -o would be boring!

## dnaleor | 2017-02-22T13:35:18+00:00
ok, I'll continue with 3-letter uniqueness. We'll see what the total will be and if needed we redo a few letters and expand the list. Dan, Esperanto, why is the language so simple? We need more words ;)



## apertamono | 2017-03-07T00:17:52+00:00
Progress update: I've done A to M by now, resulting in a running total of 1241 words, not counting 3-letter words. Thanks for your list, @Engelberg, I'm using it as a base, adding words from 2 online dictonaries.
@dnaleor Did you do some more letters after Z?

BTW, I've been thinking about a list of Dutch words for mnemonics. That will be much easier, because linguists have created lists of frequent words and huge corpora of words labeled and sorted by frequency.

## dnaleor | 2017-03-07T01:31:02+00:00
I've done S-T-U-V-Z Don't know total. Was planning to finish this week with N-O-P-R, but you can do N-O if you want ;)



## apertamono | 2017-03-16T17:17:12+00:00
OK, I did the letters N and O. Did you finish the rest, @dnaleor? 
Then I could create the full list and the header file this Sunday. I'm afraid it'll have to be a 4 letter prefix after all. But this way, it'll be as distinctive as possible.

FYI, here's what I came up with so far.
[running list.txt](https://github.com/monero-project/monero/files/848403/running.list.txt)


## dnaleor | 2017-03-24T23:19:58+00:00
I was busy, only did R-S-T-U-V-Z at this point. Will compile full list tomorrow, after I double checked, @ProkhorZ 

edit: so we are almost finished, P left, then count and try to reach target amount of words. 

edit2: maybe already create some file on github so I can add my list tomorrow :)

## moneromooo-monero | 2017-08-08T11:44:03+00:00
Seems it's almost finished. Is the list ready ? If it is, it can be included in the coming release.

## apertamono | 2017-08-09T15:36:43+00:00
It seems we were waiting on each other and got distracted. What I have is the running list of 1302 words posted above. I have some free time, I can finish the list this week.

In the meantime, I have been thinking about mnemonics in general, after the [How I stole your Siacoins](https://mtlynch.io/stole-siacoins/) blog, where a user wrote down *tonic* instead of *ionic*. I think we should prioritize distinctive words rather than recognizable words. E.g. *tubo, tufo, tuko* are easily confused, so I'd rather use *tubisto, tufgrebo, tuja, tukano*. What do you think?

## moneromooo-monero | 2017-08-10T10:55:52+00:00
That seems like a good thing to aim for, assuming those words aren't obscure. I don't think there's any current rule which prevents disctinctive words at all. Indeed, I remember a guideline saying similar words should be avoided.


## apertamono | 2017-08-12T21:10:24+00:00
*Jes, ĝi estas finita!* I did reach 1626 words with a 3 letter prefix after all, still without diacritics. I ran the list through an online spelling checker and I checked that no prefixes are repeated. For the last update, I used a [bigger online dictionary](http://www.denisowski.org/Esperanto/ESPDIC/espdic.txt); I added some words for languages/peoples that are written in lower case, like *azteca* and *maorio*, as well as some animal and plant names that not everybody might know (*egreto, ibekso*). But most Esperanto speakers will probably have a limited vocabulary anyway.
[fina listo.txt](https://github.com/monero-project/monero/files/1220012/fina.listo.txt)

@moneromooo-monero Could you create the pull request to add this, please?

Credits for compling the list: dnaleor, Engelberg, ProkhorZ.
Sources:
- Baza Radikaro Oficiala
- [Reta Vortaro](http://www.reta-vortaro.de/revo/)
- [Esperanto Panorama](http://www.esperanto-panorama.net/vortaro/eoen.htm) - Esperanto-English Dictionary
- [ESPDIC](http://www.denisowski.org/Esperanto/ESPDIC/espdic.txt) - Paul Denisowski

## moneromooo-monero | 2017-08-13T10:17:08+00:00
Great! Can you put that file on fpaste.org or pastebin.mozilla.org please ? For some reason I always get signature errors when loading from an amazon server via github.
Also, what is the exact spelling/translation of the name "Esperanto" in Esperanto, if not itself ?

## apertamono | 2017-08-13T11:11:48+00:00
OK, that's weird, but I uploaded the list here: https://pastebin.mozilla.org/9029590

The name of the language in Esperanto is simply Esperanto. (Originally, it didn't have a name; it was described as *internacia lingvo* by Doktero Esperanto, but *esperantistoj* have been calling the language Esperanto for over a century.)

## moneromooo-monero | 2017-08-13T15:18:10+00:00
https://github.com/monero-project/monero/pull/2292

If any of the word list authors want a change in attribution, let me know and I'll update.

## dnaleor | 2017-08-13T15:42:24+00:00
Hey @ProkhorZ  ... I indeed forgot to finish my part of the task, meanwhile I switched computers and it would have been hard to get the part of the work I did from the old drive. So thank you very much for doing the task on your own and sorry for my lack of communication. I kinda forgot :/

## dnaleor | 2017-08-13T16:22:51+00:00
yeah @moneromooo-monero , don't put me as an author

## apertamono | 2017-08-13T18:11:33+00:00
OK, no problem, I love collecting words! @dnaleor 
Buy some Siacoin for backups :)

## moneromooo-monero | 2017-08-14T12:44:33+00:00
OK, done

## moneromooo-monero | 2017-08-14T12:57:53+00:00
anonimal's asking whether we could have monero in the list (instead of monda, where the 3-prefix matches). Does that sound OK ?

## apertamono | 2017-08-14T13:27:18+00:00
Yeah, monero is a word, of course. I didn't think of that. I did use bitmonero.

## moneromooo-monero | 2017-08-14T14:18:31+00:00
er, is that actually a word ?

## apertamono | 2017-08-14T14:46:36+00:00
Yeah, it was in the ESPDIC dictionary. Bit- is used as a prefix independently of bitcoin, e.g. in *bitlibro* for 'e-book'.

## moneromooo-monero | 2017-08-14T15:46:46+00:00
OK, so that's a good reason not to use monero, as those words are similar (unless another one replaces bit),

## apertamono | 2017-08-14T16:43:12+00:00
Well, if you want to be extra cautious, i'd use *bitlibro* and *monero*. 

## moneromooo-monero | 2017-08-14T16:47:03+00:00
Sounds good, thanks :)

## moneromooo-monero | 2017-08-18T13:42:28+00:00
+resolved


# Action History
- Created by: Engelberg | 2017-02-16T05:59:12+00:00
- Closed at: 2017-08-18T13:48:14+00:00
