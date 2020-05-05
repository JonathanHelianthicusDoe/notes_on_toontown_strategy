# Notes on cog damage

![CC BY-SA 4.0+](https://i.creativecommons.org/l/by-sa/4.0/88x31.png
"CC BY-SA 4.0+")

<!-- TOC depthFrom:2 -->

- [Relevant statistics](#relevant-statistics)
- [The Big Cheese](#the-big-cheese)
- [Notes on tabular data](#notes-on-tabular-data)
- [Aggregate damage](#aggregate-damage)
    - [Expected aggregate damage](#expected-aggregate-damage)
        - [1 toon, expected aggregate damage](#1-toon-expected-aggregate-damage)
        - [2 toons, expected aggregate damage](#2-toons-expected-aggregate-damage)
        - [3 toons, expected aggregate damage](#3-toons-expected-aggregate-damage)
        - [4 toons, expected aggregate damage](#4-toons-expected-aggregate-damage)
    - [Maximum aggregate damage](#maximum-aggregate-damage)
        - [1 toon, maximum aggregate damage](#1-toon-maximum-aggregate-damage)
        - [2 toons, maximum aggregate damage](#2-toons-maximum-aggregate-damage)
        - [3 toons, maximum aggregate damage](#3-toons-maximum-aggregate-damage)
        - [4 toons, maximum aggregate damage](#4-toons-maximum-aggregate-damage)
- [Damage to given single toon](#damage-to-given-single-toon)
    - [Expected damage to given single toon](#expected-damage-to-given-single-toon)
        - [1 toon, expected damage to given single toon](#1-toon-expected-damage-to-given-single-toon)
        - [2 toons, expected damage to given single toon](#2-toons-expected-damage-to-given-single-toon)
        - [3 toons, expected damage to given single toon](#3-toons-expected-damage-to-given-single-toon)
        - [4 toons, expected damage to given single toon](#4-toons-expected-damage-to-given-single-toon)
    - [Maximum damage to given single toon](#maximum-damage-to-given-single-toon)

<!-- /TOC -->

One of the most neglected aspects of cog-fighting strategy in Toontown is
taking into account the attacks that cogs have in their arsenals. Of course,
this comes as no surprise, because in &ldquo;normal&rdquo; gameplay, cogs
realistically do not get much opportunity to attack (because of the existence
of the lure and sound gag tracks); and, if they do attack, the damage that they
can do pales in comparison to the max laff capacities and toonup abilities of
the toons in the fight.

Nevertheless, here I want to consider what statistics might be relevant when
gauging the threat posed by particular cog(s). Reasons you might care include
things like the existence of challenge-type toons (semis, ubers, uber semis,
&amp;c.), the possibility of challenge runs (e.g. running bosses with groups
that have significantly less than 8 toons), and also the possibility of judging
[game balance](https://en.wikipedia.org/wiki/Game_balance).

## Relevant statistics

For each cog (meaning a cog of a given species and a given level), we have
basically 3 dimensions along which the statistics that I&rsquo;m considering
&ldquo;relevant&rdquo; lie. One is the type of statistic: either [expected
value](https://en.wikipedia.org/wiki/Expected_value) or
[maximum](https://en.wikipedia.org/wiki/Maxima_and_minima). Another is the
particular situation/aspect that we care about: either the combined damage
dealt to all toons, or the damage dealt to a given single toon in the battle.
And the last dimension is how many toons are in the battle: 1, 2, 3, or 4.

Note that, importantly, the two types of statistic, [expected
value](https://en.wikipedia.org/wiki/Expected_value) and
[maximum](https://en.wikipedia.org/wiki/Maxima_and_minima),
[compose](https://en.wikipedia.org/wiki/Function_composition) well. That is to
say, if we want to know what threat is posed by *more* than 1 cog, we can get
the [expected value](https://en.wikipedia.org/wiki/Expected_value) of their
combined damage-dealings by simply adding the [expected
values](https://en.wikipedia.org/wiki/Expected_value) from all the invidual
cogs; this follows from the
[linearity](https://en.wikipedia.org/wiki/Linear_map) (and thus, <i>a
fortiori</i>, [additivity](https://en.wikipedia.org/wiki/Additive_map)) of
[expectation](https://en.wikipedia.org/wiki/Expected_value). Likewise, if we
want to do the same with the
[maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) damage-dealing, we
can simply add the [maxima](https://en.wikipedia.org/wiki/Maxima_and_minima)
from all the individual cogs; this follows from
(&#x211d;&nbsp;&#x222a;&nbsp;{&minus;&infin;},&nbsp;max,&nbsp;+) [being a
semiring](https://en.wikipedia.org/wiki/Tropical_semiring).<sup>\[1\]</sup>
Also important is the fact that we can get an idea for how much damage we
[expect](https://en.wikipedia.org/wiki/Expected_value) a single toon *with
aggro* from the particular cog in question to take, even if the toon is in a
full &ldquo;party&rdquo; of 4. That expectation is just slightly higher than
the [midpoint](https://en.wikipedia.org/wiki/Midpoint) of the
[expectations](https://en.wikipedia.org/wiki/Expected_value) that we list here
with 4 toons and with 1 toon, since there is a &frac14; chance each round that
a given cog ignores any aggro that it has, and
[randomly picks](https://en.wikipedia.org/wiki/Discrete_uniform_distribution) a
toon to attack.

The chosen types of statistic are [expected
value](https://en.wikipedia.org/wiki/Expected_value) and
[maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) because, in the
first case, we want to know roughly how much lost laff we will have to make up
for in the group, relative to the amount of toonup power available and to how
much laff (current laff, or max laff) the toons have combined; in the second
case, we want to know whether the worst-case scenario can be
[sustained](https://en.wikipedia.org/wiki/Life), which is useful in the
presence of ubers (and, more generally, toons that have low laff at the moment,
even if their max laff is [arbitrarily
large](https://en.wikipedia.org/wiki/Arbitrarily_large)). Also, knowing both
the [expected value](https://en.wikipedia.org/wiki/Expected_value) *and* the
[maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) gives a *vague*
impression of how the cog&rsquo;s damage output is
[distributed](https://en.wikipedia.org/wiki/Probability_distribution) above the
[expected value](https://en.wikipedia.org/wiki/Expected_value). Knowing the
[minimum](https://en.wikipedia.org/wiki/Maxima_and_minima) is not very
strategically useful, since it only represents the best-case scenario &mdash;
not usually something you want to be *planning* for. We could go further: other
[measures of central tendency](https://en.wikipedia.org/wiki/Central_tendency)
exist that could be used, and also we could include [measure(s) of
dispersion](https://en.wikipedia.org/wiki/Statistical_dispersion) like e.g.
[standard deviation](https://en.wikipedia.org/wiki/Standard_deviation). But
[measures of central tendency](https://en.wikipedia.org/wiki/Central_tendency)
other than [expected value](https://en.wikipedia.org/wiki/Expected_value) will
be a bit awkward, since we are working with [discrete probabilities][discrete]
directly associated with particular [outcomes][outcome], rather than a [finite
set of data](https://en.wikipedia.org/wiki/Data_set) or a [continuous
distribution][continuous]. And [measures of
dispersion](https://en.wikipedia.org/wiki/Statistical_dispersion) don&rsquo;t
help much as we only actually care about the
[distribution](https://en.wikipedia.org/wiki/Probability_distribution) above
the [expected value](https://en.wikipedia.org/wiki/Expected_value) and really
just want to know how likely the
[maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) is to occur.

---

<details>
<summary>Footnotes for &ldquo;Relevant statistics&rdquo;</summary>

1. This one is just slightly less obvious, but you can prove this yourself
   pretty easily: basically what you want to prove is a slight generalization
   of
   max{a,&nbsp;b}&nbsp;+&nbsp;max{c,&nbsp;d}&nbsp;=&nbsp;max{a&nbsp;+&nbsp;c,&nbsp;a&nbsp;+&nbsp;d,&nbsp;b&nbsp;+&nbsp;c,&nbsp;b&nbsp;+&nbsp;d}.
   In terms of &ldquo;max&rdquo; as a [binary
   operation](https://en.wikipedia.org/wiki/Binary_operation), this is:
   max{a,&nbsp;b}&nbsp;+&nbsp;max{c,&nbsp;d}&nbsp;=&nbsp;max{max{max{a&nbsp;+&nbsp;c,&nbsp;a&nbsp;+&nbsp;d},&nbsp;b&nbsp;+&nbsp;c},&nbsp;b&nbsp;+&nbsp;d}.
   Rewriting this exact same thing in more familiar [(semi-)ring][ring] syntax:
   (a&nbsp;+&nbsp;b)(c&nbsp;+&nbsp;d)&nbsp;=&nbsp;(((ac&nbsp;+&nbsp;ad)&nbsp;+&nbsp;bc)&nbsp;+&nbsp;bd).
   Since this is a [semiring](https://en.wikipedia.org/wiki/Semiring), both
   operations [associate](https://en.wikipedia.org/wiki/Associative_property),
   so we can get rid of the parentheses on the right-hand side:
   (a&nbsp;+&nbsp;b)(c&nbsp;+&nbsp;d)&nbsp;=&nbsp;ac&nbsp;+&nbsp;ad&nbsp;+&nbsp;bc&nbsp;+&nbsp;bd.
   Again, since this is a semiring, multiplication
   [distributes](https://en.wikipedia.org/wiki/Distributive_property) over
   addition, so we can rewrite the left-hand side by
   [left-distribution](https://en.wikipedia.org/wiki/Distributive_property#Definition):
   (a&nbsp;+&nbsp;b)c&nbsp;+&nbsp;(a&nbsp;+&nbsp;b)d. Repeating this process,
   but with
   [right-distribution](https://en.wikipedia.org/wiki/Distributive_property#Definition),
   we get: (ac&nbsp;+&nbsp;bc)&nbsp;+&nbsp;(ad&nbsp;+&nbsp;bd). Then,
   rearranging this using the fact that addition in a
   [semiring](https://en.wikipedia.org/wiki/Semiring) is an
   [abelian](https://en.wikipedia.org/wiki/Commutative_property)
   [monoid](https://en.wikipedia.org/wiki/Monoid) and thus
   [associates](https://en.wikipedia.org/wiki/Associative_property) and
   [commutes](https://en.wikipedia.org/wiki/Commutative_property), we can get
   the same expression as was on the right-hand side of the equals sign:
   ac&nbsp;+&nbsp;ad&nbsp;+&nbsp;bc&nbsp;+&nbsp;bd.

</details>

## The Big Cheese

The odd cog out here is [The Big
Cheese](https://toontownrewritten.fandom.com/wiki/The_Big_Cheese), although
this is actually just cosmetic. In-game, it appears as if The Big Cheese has 2
attacks: &ldquo;Tee Off&rdquo; and &ldquo;Glower Power&rdquo;. In reality
(internally), The Big Cheese has 4 attacks: `TeeOff`, `CigarSmoke`,
`FloodTheMarket`, and `SongAndDance`. The latter 3 of these attacks have no
animations; however, The Big Cheese has a default animation built in:
&ldquo;Glower Power&rdquo;. As a result, any time that The Big Cheese uses one
of the latter 3 attacks, it visually appears to use a mysterious (actually
non-existent) fifth attack, &ldquo;Glower Power&rdquo;. These 3 attacks do,
however, differ in the damages that they deal, their probabilities of being
chosen, as well as their accuracy values. These values can be obtained from
[SuitBattleGlobals.py][suitbattleglobals] and are represented in the
[cog_arsenals.json](./cog_arsenals.json).

## Notes on tabular data

The tables are organized hierarchically (with [headings][headings]), with the
top level being the dimension that separates aggregate (read: all toons)
statistics from any-given-single-toon statistics, the next level down being the
dimension that separates [expected
values](https://en.wikipedia.org/wiki/Expected_value) from
[maximum](https://en.wikipedia.org/wiki/Maxima_and_minima) values, and the most
deeply nested and final level being the dimension of how many toons are in the
battle. The &ldquo;Maximum damage to given single toon&rdquo; section has no
subsections for number of toons since this statistic does not change based on
the number of toons in the battle.

It also seems useful to have this information in a more searchable and
on-demand form, like a
[command](https://en.wikipedia.org/wiki/Command-line_interpreter) that allows
querying particular cogs, cog levels, particular statistics, particular types
of cogs, &c., and any combination of those things. I haven&rsquo;t yet created
this (and to my knowledge it does not exist), but if you would find it useful,
this paragraph is still here, and there is no such program in this directory,
perhaps file an [issue][defect-tracker] or [pull request][pull-request] with
what you&rsquo;d like to see.

## Aggregate damage

### Expected aggregate damage

#### 1 toon, expected aggregate damage

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 19.000 |
| Legal Eagle      |    11 | &#x2696; law   | 18.157 |
| Big Cheese       |    12 | &#x1f454; boss | 17.090 |
| Big Wig          |    12 | &#x2696; law   | 17.050 |
| Loan Shark       |    11 | &#x1f4b2; cash | 16.725 |
| The Mingler      |    11 | &#x1f4c8; sell | 16.140 |
| Corporate Raider |    11 | &#x1f454; boss | 15.765 |
| Robber Baron     |    12 | &#x1f4b2; cash | 15.600 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 15.300 |
| Big Wig          |    11 | &#x2696; law   | 14.825 |
| Spin Doctor      |    10 | &#x2696; law   | 14.800 |
| Legal Eagle      |    10 | &#x2696; law   | 14.607 |
| Head Hunter      |    10 | &#x1f454; boss | 14.303 |
| Big Cheese       |    11 | &#x1f454; boss | 14.085 |
| Robber Baron     |    11 | &#x1f4b2; cash | 13.550 |
| Loan Shark       |    10 | &#x1f4b2; cash | 13.445 |
| Glad Hander      |     8 | &#x1f4c8; sell | 13.295 |
| The Mingler      |    10 | &#x1f4c8; sell | 13.197 |
| Money Bags       |    10 | &#x1f4b2; cash | 12.870 |
| Corporate Raider |    10 | &#x1f454; boss | 12.825 |
| Bean Counter     |     8 | &#x1f4b2; cash | 12.750 |
| Big Wig          |    10 | &#x2696; law   | 12.750 |
| Two-Face         |    10 | &#x1f4c8; sell | 12.705 |
| Spin Doctor      |     9 | &#x2696; law   | 12.683 |
| Back Stabber     |     9 | &#x2696; law   | 11.925 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 11.800 |
| Legal Eagle      |     9 | &#x2696; law   | 11.598 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 11.575 |
| Head Hunter      |     9 | &#x1f454; boss | 11.325 |
| Big Cheese       |    10 | &#x1f454; boss | 11.060 |
| Robber Baron     |    10 | &#x1f4b2; cash | 10.850 |
| Loan Shark       |     9 | &#x1f4b2; cash | 10.845 |
| Big Wig          |     9 | &#x2696; law   | 10.775 |
| Money Bags       |     9 | &#x1f4b2; cash | 10.717 |
| Two-Face         |     9 | &#x1f4c8; sell | 10.582 |
| Tightwad         |     7 | &#x1f4b2; cash | 10.582 |
| Micromanager     |     8 | &#x1f454; boss | 10.448 |
| The Mingler      |     9 | &#x1f4c8; sell | 10.425 |
| Corporate Raider |     9 | &#x1f454; boss | 10.205 |
| Bean Counter     |     7 | &#x1f4b2; cash | 10.200 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 10.103 |
| Double Talker    |     7 | &#x2696; law   | 10.080 |
| Name Dropper     |     7 | &#x1f4c8; sell |  9.925 |
| Spin Doctor      |     8 | &#x2696; law   |  9.900 |
| Mover & Shaker   |     8 | &#x1f4c8; sell |  9.455 |
| Downsizer        |     9 | &#x1f454; boss |  9.275 |
| Back Stabber     |     8 | &#x2696; law   |  9.262 |
| Big Wig          |     8 | &#x2696; law   |  8.950 |
| Legal Eagle      |     8 | &#x2696; law   |  8.928 |
| Head Hunter      |     8 | &#x1f454; boss |  8.800 |
| Tightwad         |     6 | &#x1f4b2; cash |  8.662 |
| Money Bags       |     8 | &#x1f4b2; cash |  8.640 |
| Ambulance Chaser |     8 | &#x2696; law   |  8.588 |
| Loan Shark       |     8 | &#x1f4b2; cash |  8.480 |
| Robber Baron     |     9 | &#x1f4b2; cash |  8.450 |
| Two-Face         |     8 | &#x1f4c8; sell |  8.430 |
| Big Cheese       |     9 | &#x1f454; boss |  8.285 |
| Number Cruncher  |     8 | &#x1f4b2; cash |  8.190 |
| Glad Hander      |     7 | &#x1f4c8; sell |  8.080 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell |  8.025 |
| The Mingler      |     8 | &#x1f4c8; sell |  7.778 |
| Bean Counter     |     6 | &#x1f4b2; cash |  7.650 |
| Corporate Raider |     8 | &#x1f454; boss |  7.635 |
| Micromanager     |     7 | &#x1f454; boss |  7.590 |
| Downsizer        |     8 | &#x1f454; boss |  7.537 |
| Mover & Shaker   |     7 | &#x1f4c8; sell |  7.450 |
| Spin Doctor      |     7 | &#x2696; law   |  7.382 |
| Bloodsucker      |     6 | &#x2696; law   |  7.330 |
| Back Stabber     |     7 | &#x2696; law   |  7.328 |
| Name Dropper     |     6 | &#x1f4c8; sell |  7.190 |
| Ambulance Chaser |     7 | &#x2696; law   |  6.938 |
| Telemarketer     |     6 | &#x1f4c8; sell |  6.922 |
| Pencil Pusher    |     6 | &#x1f454; boss |  6.900 |
| Money Bags       |     7 | &#x1f4b2; cash |  6.763 |
| Double Talker    |     6 | &#x2696; law   |  6.720 |
| Head Hunter      |     7 | &#x1f454; boss |  6.540 |
| Two-Face         |     7 | &#x1f4c8; sell |  6.508 |
| Legal Eagle      |     7 | &#x2696; law   |  6.468 |
| Penny Pincher    |     6 | &#x1f4b2; cash |  6.450 |
| Number Cruncher  |     7 | &#x1f4b2; cash |  6.438 |
| Robber Baron     |     8 | &#x1f4b2; cash |  6.300 |
| Big Cheese       |     8 | &#x1f454; boss |  5.960 |
| Downsizer        |     7 | &#x1f454; boss |  5.945 |
| Loan Shark       |     7 | &#x1f4b2; cash |  5.940 |
| The Mingler      |     7 | &#x1f4c8; sell |  5.615 |
| Back Stabber     |     6 | &#x2696; law   |  5.593 |
| Spin Doctor      |     6 | &#x2696; law   |  5.570 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell |  5.550 |
| Ambulance Chaser |     6 | &#x2696; law   |  5.513 |
| Mover & Shaker   |     6 | &#x1f4c8; sell |  5.505 |
| Corporate Raider |     7 | &#x1f454; boss |  5.475 |
| Micromanager     |     6 | &#x1f454; boss |  5.152 |
| Bean Counter     |     5 | &#x1f4b2; cash |  5.100 |
| Telemarketer     |     5 | &#x1f4c8; sell |  5.040 |
| Pencil Pusher    |     5 | &#x1f454; boss |  4.950 |
| Name Dropper     |     5 | &#x1f4c8; sell |  4.925 |
| Bloodsucker      |     5 | &#x2696; law   |  4.890 |
| Money Bags       |     6 | &#x1f4b2; cash |  4.860 |
| Short Change     |     5 | &#x1f4b2; cash |  4.822 |
| Head Hunter      |     6 | &#x1f454; boss |  4.745 |
| Tightwad         |     5 | &#x1f4b2; cash |  4.740 |
| Flunky           |     5 | &#x1f454; boss |  4.740 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  4.688 |
| Two-Face         |     6 | &#x1f4c8; sell |  4.665 |
| Yesman           |     7 | &#x1f454; boss |  4.450 |
| Downsizer        |     6 | &#x1f454; boss |  4.435 |
| Glad Hander      |     6 | &#x1f4c8; sell |  4.325 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  4.300 |
| Name Dropper     |     4 | &#x1f4c8; sell |  4.065 |
| Cold Caller      |     5 | &#x1f4c8; sell |  4.062 |
| Double Talker    |     5 | &#x2696; law   |  3.955 |
| Telemarketer     |     4 | &#x1f4c8; sell |  3.880 |
| Bottom Feeder    |     5 | &#x2696; law   |  3.880 |
| Ambulance Chaser |     5 | &#x2696; law   |  3.863 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  3.680 |
| Back Stabber     |     5 | &#x2696; law   |  3.545 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  3.530 |
| Pencil Pusher    |     4 | &#x1f454; boss |  3.525 |
| Bloodsucker      |     4 | &#x2696; law   |  3.400 |
| Bean Counter     |     4 | &#x1f4b2; cash |  3.400 |
| Short Change     |     4 | &#x1f4b2; cash |  3.385 |
| Name Dropper     |     3 | &#x1f4c8; sell |  3.310 |
| Cold Caller      |     4 | &#x1f4c8; sell |  3.255 |
| Telemarketer     |     3 | &#x1f4c8; sell |  3.157 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  3.150 |
| Downsizer        |     5 | &#x1f454; boss |  3.125 |
| Yesman           |     6 | &#x1f454; boss |  3.078 |
| Flunky           |     4 | &#x1f454; boss |  2.955 |
| Micromanager     |     5 | &#x1f454; boss |  2.955 |
| Bottom Feeder    |     4 | &#x2696; law   |  2.910 |
| Ambulance Chaser |     4 | &#x2696; law   |  2.775 |
| Pencil Pusher    |     3 | &#x1f454; boss |  2.700 |
| Glad Hander      |     4 | &#x1f4c8; sell |  2.675 |
| Tightwad         |     4 | &#x1f4b2; cash |  2.670 |
| Short Change     |     3 | &#x1f4b2; cash |  2.582 |
| Glad Hander      |     5 | &#x1f4c8; sell |  2.560 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  2.488 |
| Yesman           |     5 | &#x1f454; boss |  2.473 |
| Cold Caller      |     3 | &#x1f4c8; sell |  2.423 |
| Bloodsucker      |     3 | &#x2696; law   |  2.410 |
| Tightwad         |     3 | &#x1f4b2; cash |  2.385 |
| Double Talker    |     4 | &#x2696; law   |  2.280 |
| Flunky           |     3 | &#x1f454; boss |  2.240 |
| Bottom Feeder    |     3 | &#x2696; law   |  2.225 |
| Telemarketer     |     2 | &#x1f4c8; sell |  2.138 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  1.825 |
| Micromanager     |     4 | &#x1f454; boss |  1.775 |
| Pencil Pusher    |     2 | &#x1f454; boss |  1.762 |
| Cold Caller      |     2 | &#x1f4c8; sell |  1.703 |
| Short Change     |     2 | &#x1f4b2; cash |  1.685 |
| Double Talker    |     3 | &#x2696; law   |  1.575 |
| Yesman           |     4 | &#x1f454; boss |  1.555 |
| Bloodsucker      |     2 | &#x2696; law   |  1.520 |
| Bottom Feeder    |     2 | &#x2696; law   |  1.450 |
| Short Change     |     1 | &#x1f4b2; cash |  1.423 |
| Cold Caller      |     1 | &#x1f4c8; sell |  1.345 |
| Yesman           |     3 | &#x1f454; boss |  1.275 |
| Flunky           |     2 | &#x1f454; boss |  1.255 |
| Flunky           |     1 | &#x1f454; boss |  1.050 |
| Bottom Feeder    |     1 | &#x2696; law   |  0.910 |

#### 2 toons, expected aggregate damage

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 28.500 |
| Big Wig          |    12 | &#x2696; law   | 24.650 |
| Robber Baron     |    12 | &#x1f4b2; cash | 24.000 |
| The Mingler      |    11 | &#x1f4c8; sell | 23.700 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 22.950 |
| Spin Doctor      |    10 | &#x2696; law   | 21.950 |
| Big Wig          |    11 | &#x2696; law   | 21.575 |
| Robber Baron     |    11 | &#x1f4b2; cash | 20.300 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 19.420 |
| The Mingler      |    10 | &#x1f4c8; sell | 19.085 |
| Spin Doctor      |     9 | &#x2696; law   | 18.863 |
| Back Stabber     |     9 | &#x2696; law   | 18.405 |
| Big Wig          |    10 | &#x2696; law   | 18.275 |
| Legal Eagle      |    11 | &#x2696; law   | 18.157 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 17.200 |
| Big Cheese       |    12 | &#x1f454; boss | 17.090 |
| Loan Shark       |    11 | &#x1f4b2; cash | 16.725 |
| Robber Baron     |    10 | &#x1f4b2; cash | 16.450 |
| Corporate Raider |    11 | &#x1f454; boss | 15.765 |
| Mover & Shaker   |     8 | &#x1f4c8; sell | 15.685 |
| The Mingler      |     9 | &#x1f4c8; sell | 15.270 |
| Big Wig          |     9 | &#x2696; law   | 15.175 |
| Spin Doctor      |     8 | &#x2696; law   | 14.700 |
| Legal Eagle      |    10 | &#x2696; law   | 14.607 |
| Back Stabber     |     8 | &#x2696; law   | 14.362 |
| Head Hunter      |    10 | &#x1f454; boss | 14.303 |
| Big Cheese       |    11 | &#x1f454; boss | 14.085 |
| Loan Shark       |    10 | &#x1f4b2; cash | 13.445 |
| Glad Hander      |     8 | &#x1f4c8; sell | 13.295 |
| Robber Baron     |     9 | &#x1f4b2; cash | 13.000 |
| Money Bags       |    10 | &#x1f4b2; cash | 12.870 |
| Corporate Raider |    10 | &#x1f454; boss | 12.825 |
| Bean Counter     |     8 | &#x1f4b2; cash | 12.750 |
| Two-Face         |    10 | &#x1f4c8; sell | 12.705 |
| Big Wig          |     8 | &#x2696; law   | 12.700 |
| Mover & Shaker   |     7 | &#x1f4c8; sell | 12.400 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell | 11.925 |
| The Mingler      |     8 | &#x1f4c8; sell | 11.670 |
| Legal Eagle      |     9 | &#x2696; law   | 11.598 |
| Back Stabber     |     7 | &#x2696; law   | 11.487 |
| Head Hunter      |     9 | &#x1f454; boss | 11.325 |
| Big Cheese       |    10 | &#x1f454; boss | 11.060 |
| Spin Doctor      |     7 | &#x2696; law   | 10.932 |
| Loan Shark       |     9 | &#x1f4b2; cash | 10.845 |
| Name Dropper     |     7 | &#x1f4c8; sell | 10.825 |
| Money Bags       |     9 | &#x1f4b2; cash | 10.717 |
| Two-Face         |     9 | &#x1f4c8; sell | 10.582 |
| Tightwad         |     7 | &#x1f4b2; cash | 10.582 |
| Micromanager     |     8 | &#x1f454; boss | 10.448 |
| Ambulance Chaser |     8 | &#x2696; law   | 10.275 |
| Corporate Raider |     9 | &#x1f454; boss | 10.205 |
| Bean Counter     |     7 | &#x1f4b2; cash | 10.200 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 10.103 |
| Double Talker    |     7 | &#x2696; law   | 10.080 |
| Robber Baron     |     8 | &#x1f4b2; cash |  9.600 |
| Downsizer        |     9 | &#x1f454; boss |  9.275 |
| Mover & Shaker   |     6 | &#x1f4c8; sell |  9.165 |
| Legal Eagle      |     8 | &#x2696; law   |  8.928 |
| Back Stabber     |     6 | &#x2696; law   |  8.893 |
| Head Hunter      |     8 | &#x1f454; boss |  8.800 |
| Tightwad         |     6 | &#x1f4b2; cash |  8.662 |
| Money Bags       |     8 | &#x1f4b2; cash |  8.640 |
| Loan Shark       |     8 | &#x1f4b2; cash |  8.480 |
| Two-Face         |     8 | &#x1f4c8; sell |  8.430 |
| The Mingler      |     7 | &#x1f4c8; sell |  8.315 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell |  8.300 |
| Ambulance Chaser |     7 | &#x2696; law   |  8.288 |
| Big Cheese       |     9 | &#x1f454; boss |  8.285 |
| Number Cruncher  |     8 | &#x1f4b2; cash |  8.190 |
| Spin Doctor      |     6 | &#x2696; law   |  8.150 |
| Glad Hander      |     7 | &#x1f4c8; sell |  8.080 |
| Name Dropper     |     6 | &#x1f4c8; sell |  7.865 |
| Bean Counter     |     6 | &#x1f4b2; cash |  7.650 |
| Corporate Raider |     8 | &#x1f454; boss |  7.635 |
| Micromanager     |     7 | &#x1f454; boss |  7.590 |
| Downsizer        |     8 | &#x1f454; boss |  7.537 |
| Bloodsucker      |     6 | &#x2696; law   |  7.330 |
| Telemarketer     |     6 | &#x1f4c8; sell |  6.922 |
| Pencil Pusher    |     6 | &#x1f454; boss |  6.900 |
| Money Bags       |     7 | &#x1f4b2; cash |  6.763 |
| Double Talker    |     6 | &#x2696; law   |  6.720 |
| Head Hunter      |     7 | &#x1f454; boss |  6.540 |
| Ambulance Chaser |     6 | &#x2696; law   |  6.525 |
| Two-Face         |     7 | &#x1f4c8; sell |  6.508 |
| Legal Eagle      |     7 | &#x2696; law   |  6.468 |
| Penny Pincher    |     6 | &#x1f4b2; cash |  6.450 |
| Number Cruncher  |     7 | &#x1f4b2; cash |  6.438 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  6.310 |
| Yesman           |     7 | &#x1f454; boss |  6.250 |
| Big Cheese       |     8 | &#x1f454; boss |  5.960 |
| Downsizer        |     7 | &#x1f454; boss |  5.945 |
| Loan Shark       |     7 | &#x1f4b2; cash |  5.940 |
| Corporate Raider |     7 | &#x1f454; boss |  5.475 |
| Back Stabber     |     5 | &#x2696; law   |  5.465 |
| Name Dropper     |     5 | &#x1f4c8; sell |  5.375 |
| Micromanager     |     6 | &#x1f454; boss |  5.152 |
| Bean Counter     |     5 | &#x1f4b2; cash |  5.100 |
| Telemarketer     |     5 | &#x1f4c8; sell |  5.040 |
| Pencil Pusher    |     5 | &#x1f454; boss |  4.950 |
| Bloodsucker      |     5 | &#x2696; law   |  4.890 |
| Money Bags       |     6 | &#x1f4b2; cash |  4.860 |
| Short Change     |     5 | &#x1f4b2; cash |  4.822 |
| Head Hunter      |     6 | &#x1f454; boss |  4.745 |
| Tightwad         |     5 | &#x1f4b2; cash |  4.740 |
| Flunky           |     5 | &#x1f454; boss |  4.740 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  4.688 |
| Two-Face         |     6 | &#x1f4c8; sell |  4.665 |
| Ambulance Chaser |     5 | &#x2696; law   |  4.538 |
| Downsizer        |     6 | &#x1f454; boss |  4.435 |
| Name Dropper     |     4 | &#x1f4c8; sell |  4.365 |
| Glad Hander      |     6 | &#x1f4c8; sell |  4.325 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  4.300 |
| Yesman           |     6 | &#x1f454; boss |  4.197 |
| Cold Caller      |     5 | &#x1f4c8; sell |  4.062 |
| Double Talker    |     5 | &#x2696; law   |  3.955 |
| Telemarketer     |     4 | &#x1f4c8; sell |  3.880 |
| Bottom Feeder    |     5 | &#x2696; law   |  3.880 |
| Name Dropper     |     3 | &#x1f4c8; sell |  3.535 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  3.530 |
| Pencil Pusher    |     4 | &#x1f454; boss |  3.525 |
| Bloodsucker      |     4 | &#x2696; law   |  3.400 |
| Bean Counter     |     4 | &#x1f4b2; cash |  3.400 |
| Short Change     |     4 | &#x1f4b2; cash |  3.385 |
| Cold Caller      |     4 | &#x1f4c8; sell |  3.255 |
| Ambulance Chaser |     4 | &#x2696; law   |  3.225 |
| Telemarketer     |     3 | &#x1f4c8; sell |  3.157 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  3.150 |
| Downsizer        |     5 | &#x1f454; boss |  3.125 |
| Yesman           |     5 | &#x1f454; boss |  3.103 |
| Flunky           |     4 | &#x1f454; boss |  2.955 |
| Micromanager     |     5 | &#x1f454; boss |  2.955 |
| Bottom Feeder    |     4 | &#x2696; law   |  2.910 |
| Pencil Pusher    |     3 | &#x1f454; boss |  2.700 |
| Glad Hander      |     4 | &#x1f4c8; sell |  2.675 |
| Tightwad         |     4 | &#x1f4b2; cash |  2.670 |
| Short Change     |     3 | &#x1f4b2; cash |  2.582 |
| Glad Hander      |     5 | &#x1f4c8; sell |  2.560 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  2.488 |
| Cold Caller      |     3 | &#x1f4c8; sell |  2.423 |
| Bloodsucker      |     3 | &#x2696; law   |  2.410 |
| Tightwad         |     3 | &#x1f4b2; cash |  2.385 |
| Double Talker    |     4 | &#x2696; law   |  2.280 |
| Flunky           |     3 | &#x1f454; boss |  2.240 |
| Bottom Feeder    |     3 | &#x2696; law   |  2.225 |
| Telemarketer     |     2 | &#x1f4c8; sell |  2.138 |
| Yesman           |     4 | &#x1f454; boss |  1.855 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  1.825 |
| Micromanager     |     4 | &#x1f454; boss |  1.775 |
| Pencil Pusher    |     2 | &#x1f454; boss |  1.762 |
| Cold Caller      |     2 | &#x1f4c8; sell |  1.703 |
| Short Change     |     2 | &#x1f4b2; cash |  1.685 |
| Double Talker    |     3 | &#x2696; law   |  1.575 |
| Bloodsucker      |     2 | &#x2696; law   |  1.520 |
| Bottom Feeder    |     2 | &#x2696; law   |  1.450 |
| Short Change     |     1 | &#x1f4b2; cash |  1.423 |
| Yesman           |     3 | &#x1f454; boss |  1.375 |
| Cold Caller      |     1 | &#x1f4c8; sell |  1.345 |
| Flunky           |     2 | &#x1f454; boss |  1.255 |
| Flunky           |     1 | &#x1f454; boss |  1.050 |
| Bottom Feeder    |     1 | &#x2696; law   |  0.910 |

#### 3 toons, expected aggregate damage

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 38.000 |
| Robber Baron     |    12 | &#x1f4b2; cash | 32.400 |
| Big Wig          |    12 | &#x2696; law   | 32.250 |
| The Mingler      |    11 | &#x1f4c8; sell | 31.260 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 30.600 |
| Spin Doctor      |    10 | &#x2696; law   | 29.100 |
| Big Wig          |    11 | &#x2696; law   | 28.325 |
| Robber Baron     |    11 | &#x1f4b2; cash | 27.050 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 27.040 |
| Spin Doctor      |     9 | &#x2696; law   | 25.043 |
| The Mingler      |    10 | &#x1f4c8; sell | 24.973 |
| Back Stabber     |     9 | &#x2696; law   | 24.885 |
| Big Wig          |    10 | &#x2696; law   | 23.800 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 22.825 |
| Robber Baron     |    10 | &#x1f4b2; cash | 22.050 |
| Mover & Shaker   |     8 | &#x1f4c8; sell | 21.915 |
| The Mingler      |     9 | &#x1f4c8; sell | 20.115 |
| Big Wig          |     9 | &#x2696; law   | 19.575 |
| Spin Doctor      |     8 | &#x2696; law   | 19.500 |
| Back Stabber     |     8 | &#x2696; law   | 19.462 |
| Legal Eagle      |    11 | &#x2696; law   | 18.157 |
| Robber Baron     |     9 | &#x1f4b2; cash | 17.550 |
| Mover & Shaker   |     7 | &#x1f4c8; sell | 17.350 |
| Big Cheese       |    12 | &#x1f454; boss | 17.090 |
| Loan Shark       |    11 | &#x1f4b2; cash | 16.725 |
| Big Wig          |     8 | &#x2696; law   | 16.450 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell | 15.825 |
| Corporate Raider |    11 | &#x1f454; boss | 15.765 |
| Back Stabber     |     7 | &#x2696; law   | 15.647 |
| The Mingler      |     8 | &#x1f4c8; sell | 15.563 |
| Legal Eagle      |    10 | &#x2696; law   | 14.607 |
| Spin Doctor      |     7 | &#x2696; law   | 14.482 |
| Head Hunter      |    10 | &#x1f454; boss | 14.303 |
| Big Cheese       |    11 | &#x1f454; boss | 14.085 |
| Loan Shark       |    10 | &#x1f4b2; cash | 13.445 |
| Glad Hander      |     8 | &#x1f4c8; sell | 13.295 |
| Robber Baron     |     8 | &#x1f4b2; cash | 12.900 |
| Money Bags       |    10 | &#x1f4b2; cash | 12.870 |
| Mover & Shaker   |     6 | &#x1f4c8; sell | 12.825 |
| Corporate Raider |    10 | &#x1f454; boss | 12.825 |
| Bean Counter     |     8 | &#x1f4b2; cash | 12.750 |
| Two-Face         |    10 | &#x1f4c8; sell | 12.705 |
| Back Stabber     |     6 | &#x2696; law   | 12.192 |
| Ambulance Chaser |     8 | &#x2696; law   | 11.963 |
| Name Dropper     |     7 | &#x1f4c8; sell | 11.725 |
| Legal Eagle      |     9 | &#x2696; law   | 11.598 |
| Head Hunter      |     9 | &#x1f454; boss | 11.325 |
| Big Cheese       |    10 | &#x1f454; boss | 11.060 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell | 11.050 |
| The Mingler      |     7 | &#x1f4c8; sell | 11.015 |
| Loan Shark       |     9 | &#x1f4b2; cash | 10.845 |
| Spin Doctor      |     6 | &#x2696; law   | 10.730 |
| Money Bags       |     9 | &#x1f4b2; cash | 10.717 |
| Two-Face         |     9 | &#x1f4c8; sell | 10.582 |
| Tightwad         |     7 | &#x1f4b2; cash | 10.582 |
| Micromanager     |     8 | &#x1f454; boss | 10.448 |
| Corporate Raider |     9 | &#x1f454; boss | 10.205 |
| Bean Counter     |     7 | &#x1f4b2; cash | 10.200 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 10.103 |
| Double Talker    |     7 | &#x2696; law   | 10.080 |
| Ambulance Chaser |     7 | &#x2696; law   |  9.638 |
| Downsizer        |     9 | &#x1f454; boss |  9.275 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  8.940 |
| Legal Eagle      |     8 | &#x2696; law   |  8.928 |
| Head Hunter      |     8 | &#x1f454; boss |  8.800 |
| Tightwad         |     6 | &#x1f4b2; cash |  8.662 |
| Money Bags       |     8 | &#x1f4b2; cash |  8.640 |
| Name Dropper     |     6 | &#x1f4c8; sell |  8.540 |
| Loan Shark       |     8 | &#x1f4b2; cash |  8.480 |
| Two-Face         |     8 | &#x1f4c8; sell |  8.430 |
| Big Cheese       |     9 | &#x1f454; boss |  8.285 |
| Number Cruncher  |     8 | &#x1f4b2; cash |  8.190 |
| Glad Hander      |     7 | &#x1f4c8; sell |  8.080 |
| Yesman           |     7 | &#x1f454; boss |  8.050 |
| Bean Counter     |     6 | &#x1f4b2; cash |  7.650 |
| Corporate Raider |     8 | &#x1f454; boss |  7.635 |
| Micromanager     |     7 | &#x1f454; boss |  7.590 |
| Ambulance Chaser |     6 | &#x2696; law   |  7.537 |
| Downsizer        |     8 | &#x1f454; boss |  7.537 |
| Back Stabber     |     5 | &#x2696; law   |  7.385 |
| Bloodsucker      |     6 | &#x2696; law   |  7.330 |
| Telemarketer     |     6 | &#x1f4c8; sell |  6.922 |
| Pencil Pusher    |     6 | &#x1f454; boss |  6.900 |
| Money Bags       |     7 | &#x1f4b2; cash |  6.763 |
| Double Talker    |     6 | &#x2696; law   |  6.720 |
| Head Hunter      |     7 | &#x1f454; boss |  6.540 |
| Two-Face         |     7 | &#x1f4c8; sell |  6.508 |
| Legal Eagle      |     7 | &#x2696; law   |  6.468 |
| Penny Pincher    |     6 | &#x1f4b2; cash |  6.450 |
| Number Cruncher  |     7 | &#x1f4b2; cash |  6.438 |
| Big Cheese       |     8 | &#x1f454; boss |  5.960 |
| Downsizer        |     7 | &#x1f454; boss |  5.945 |
| Loan Shark       |     7 | &#x1f4b2; cash |  5.940 |
| Name Dropper     |     5 | &#x1f4c8; sell |  5.825 |
| Corporate Raider |     7 | &#x1f454; boss |  5.475 |
| Yesman           |     6 | &#x1f454; boss |  5.318 |
| Ambulance Chaser |     5 | &#x2696; law   |  5.212 |
| Micromanager     |     6 | &#x1f454; boss |  5.152 |
| Bean Counter     |     5 | &#x1f4b2; cash |  5.100 |
| Telemarketer     |     5 | &#x1f4c8; sell |  5.040 |
| Pencil Pusher    |     5 | &#x1f454; boss |  4.950 |
| Bloodsucker      |     5 | &#x2696; law   |  4.890 |
| Money Bags       |     6 | &#x1f4b2; cash |  4.860 |
| Short Change     |     5 | &#x1f4b2; cash |  4.822 |
| Head Hunter      |     6 | &#x1f454; boss |  4.745 |
| Tightwad         |     5 | &#x1f4b2; cash |  4.740 |
| Flunky           |     5 | &#x1f454; boss |  4.740 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  4.688 |
| Two-Face         |     6 | &#x1f4c8; sell |  4.665 |
| Name Dropper     |     4 | &#x1f4c8; sell |  4.665 |
| Downsizer        |     6 | &#x1f454; boss |  4.435 |
| Glad Hander      |     6 | &#x1f4c8; sell |  4.325 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  4.300 |
| Cold Caller      |     5 | &#x1f4c8; sell |  4.062 |
| Double Talker    |     5 | &#x2696; law   |  3.955 |
| Telemarketer     |     4 | &#x1f4c8; sell |  3.880 |
| Bottom Feeder    |     5 | &#x2696; law   |  3.880 |
| Name Dropper     |     3 | &#x1f4c8; sell |  3.760 |
| Yesman           |     5 | &#x1f454; boss |  3.732 |
| Ambulance Chaser |     4 | &#x2696; law   |  3.675 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  3.530 |
| Pencil Pusher    |     4 | &#x1f454; boss |  3.525 |
| Bloodsucker      |     4 | &#x2696; law   |  3.400 |
| Bean Counter     |     4 | &#x1f4b2; cash |  3.400 |
| Short Change     |     4 | &#x1f4b2; cash |  3.385 |
| Cold Caller      |     4 | &#x1f4c8; sell |  3.255 |
| Telemarketer     |     3 | &#x1f4c8; sell |  3.157 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  3.150 |
| Downsizer        |     5 | &#x1f454; boss |  3.125 |
| Flunky           |     4 | &#x1f454; boss |  2.955 |
| Micromanager     |     5 | &#x1f454; boss |  2.955 |
| Bottom Feeder    |     4 | &#x2696; law   |  2.910 |
| Pencil Pusher    |     3 | &#x1f454; boss |  2.700 |
| Glad Hander      |     4 | &#x1f4c8; sell |  2.675 |
| Tightwad         |     4 | &#x1f4b2; cash |  2.670 |
| Short Change     |     3 | &#x1f4b2; cash |  2.582 |
| Glad Hander      |     5 | &#x1f4c8; sell |  2.560 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  2.488 |
| Cold Caller      |     3 | &#x1f4c8; sell |  2.423 |
| Bloodsucker      |     3 | &#x2696; law   |  2.410 |
| Tightwad         |     3 | &#x1f4b2; cash |  2.385 |
| Double Talker    |     4 | &#x2696; law   |  2.280 |
| Flunky           |     3 | &#x1f454; boss |  2.240 |
| Bottom Feeder    |     3 | &#x2696; law   |  2.225 |
| Yesman           |     4 | &#x1f454; boss |  2.155 |
| Telemarketer     |     2 | &#x1f4c8; sell |  2.138 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  1.825 |
| Micromanager     |     4 | &#x1f454; boss |  1.775 |
| Pencil Pusher    |     2 | &#x1f454; boss |  1.762 |
| Cold Caller      |     2 | &#x1f4c8; sell |  1.703 |
| Short Change     |     2 | &#x1f4b2; cash |  1.685 |
| Double Talker    |     3 | &#x2696; law   |  1.575 |
| Bloodsucker      |     2 | &#x2696; law   |  1.520 |
| Yesman           |     3 | &#x1f454; boss |  1.475 |
| Bottom Feeder    |     2 | &#x2696; law   |  1.450 |
| Short Change     |     1 | &#x1f4b2; cash |  1.423 |
| Cold Caller      |     1 | &#x1f4c8; sell |  1.345 |
| Flunky           |     2 | &#x1f454; boss |  1.255 |
| Flunky           |     1 | &#x1f454; boss |  1.050 |
| Bottom Feeder    |     1 | &#x2696; law   |  0.910 |

#### 4 toons, expected aggregate damage

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 47.500 |
| Robber Baron     |    12 | &#x1f4b2; cash | 40.800 |
| Big Wig          |    12 | &#x2696; law   | 39.850 |
| The Mingler      |    11 | &#x1f4c8; sell | 38.820 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 38.250 |
| Spin Doctor      |    10 | &#x2696; law   | 36.250 |
| Big Wig          |    11 | &#x2696; law   | 35.075 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 34.660 |
| Robber Baron     |    11 | &#x1f4b2; cash | 33.800 |
| Back Stabber     |     9 | &#x2696; law   | 31.365 |
| Spin Doctor      |     9 | &#x2696; law   | 31.223 |
| The Mingler      |    10 | &#x1f4c8; sell | 30.860 |
| Big Wig          |    10 | &#x2696; law   | 29.325 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 28.450 |
| Mover & Shaker   |     8 | &#x1f4c8; sell | 28.145 |
| Robber Baron     |    10 | &#x1f4b2; cash | 27.650 |
| The Mingler      |     9 | &#x1f4c8; sell | 24.960 |
| Back Stabber     |     8 | &#x2696; law   | 24.562 |
| Spin Doctor      |     8 | &#x2696; law   | 24.300 |
| Big Wig          |     9 | &#x2696; law   | 23.975 |
| Mover & Shaker   |     7 | &#x1f4c8; sell | 22.300 |
| Robber Baron     |     9 | &#x1f4b2; cash | 22.100 |
| Big Wig          |     8 | &#x2696; law   | 20.200 |
| Back Stabber     |     7 | &#x2696; law   | 19.808 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell | 19.725 |
| The Mingler      |     8 | &#x1f4c8; sell | 19.455 |
| Legal Eagle      |    11 | &#x2696; law   | 18.157 |
| Spin Doctor      |     7 | &#x2696; law   | 18.032 |
| Big Cheese       |    12 | &#x1f454; boss | 17.090 |
| Loan Shark       |    11 | &#x1f4b2; cash | 16.725 |
| Mover & Shaker   |     6 | &#x1f4c8; sell | 16.485 |
| Robber Baron     |     8 | &#x1f4b2; cash | 16.200 |
| Corporate Raider |    11 | &#x1f454; boss | 15.765 |
| Back Stabber     |     6 | &#x2696; law   | 15.492 |
| Legal Eagle      |    10 | &#x2696; law   | 14.607 |
| Head Hunter      |    10 | &#x1f454; boss | 14.303 |
| Big Cheese       |    11 | &#x1f454; boss | 14.085 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell | 13.800 |
| The Mingler      |     7 | &#x1f4c8; sell | 13.715 |
| Ambulance Chaser |     8 | &#x2696; law   | 13.650 |
| Loan Shark       |    10 | &#x1f4b2; cash | 13.445 |
| Spin Doctor      |     6 | &#x2696; law   | 13.310 |
| Glad Hander      |     8 | &#x1f4c8; sell | 13.295 |
| Money Bags       |    10 | &#x1f4b2; cash | 12.870 |
| Corporate Raider |    10 | &#x1f454; boss | 12.825 |
| Bean Counter     |     8 | &#x1f4b2; cash | 12.750 |
| Two-Face         |    10 | &#x1f4c8; sell | 12.705 |
| Name Dropper     |     7 | &#x1f4c8; sell | 12.625 |
| Legal Eagle      |     9 | &#x2696; law   | 11.598 |
| Mover & Shaker   |     5 | &#x1f4c8; sell | 11.570 |
| Head Hunter      |     9 | &#x1f454; boss | 11.325 |
| Big Cheese       |    10 | &#x1f454; boss | 11.060 |
| Ambulance Chaser |     7 | &#x2696; law   | 10.988 |
| Loan Shark       |     9 | &#x1f4b2; cash | 10.845 |
| Money Bags       |     9 | &#x1f4b2; cash | 10.717 |
| Two-Face         |     9 | &#x1f4c8; sell | 10.582 |
| Tightwad         |     7 | &#x1f4b2; cash | 10.582 |
| Micromanager     |     8 | &#x1f454; boss | 10.448 |
| Corporate Raider |     9 | &#x1f454; boss | 10.205 |
| Bean Counter     |     7 | &#x1f4b2; cash | 10.200 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 10.103 |
| Double Talker    |     7 | &#x2696; law   | 10.080 |
| Yesman           |     7 | &#x1f454; boss |  9.850 |
| Back Stabber     |     5 | &#x2696; law   |  9.305 |
| Downsizer        |     9 | &#x1f454; boss |  9.275 |
| Name Dropper     |     6 | &#x1f4c8; sell |  9.215 |
| Legal Eagle      |     8 | &#x2696; law   |  8.928 |
| Head Hunter      |     8 | &#x1f454; boss |  8.800 |
| Tightwad         |     6 | &#x1f4b2; cash |  8.662 |
| Money Bags       |     8 | &#x1f4b2; cash |  8.640 |
| Ambulance Chaser |     6 | &#x2696; law   |  8.550 |
| Loan Shark       |     8 | &#x1f4b2; cash |  8.480 |
| Two-Face         |     8 | &#x1f4c8; sell |  8.430 |
| Big Cheese       |     9 | &#x1f454; boss |  8.285 |
| Number Cruncher  |     8 | &#x1f4b2; cash |  8.190 |
| Glad Hander      |     7 | &#x1f4c8; sell |  8.080 |
| Bean Counter     |     6 | &#x1f4b2; cash |  7.650 |
| Corporate Raider |     8 | &#x1f454; boss |  7.635 |
| Micromanager     |     7 | &#x1f454; boss |  7.590 |
| Downsizer        |     8 | &#x1f454; boss |  7.537 |
| Bloodsucker      |     6 | &#x2696; law   |  7.330 |
| Telemarketer     |     6 | &#x1f4c8; sell |  6.922 |
| Pencil Pusher    |     6 | &#x1f454; boss |  6.900 |
| Money Bags       |     7 | &#x1f4b2; cash |  6.763 |
| Double Talker    |     6 | &#x2696; law   |  6.720 |
| Head Hunter      |     7 | &#x1f454; boss |  6.540 |
| Two-Face         |     7 | &#x1f4c8; sell |  6.508 |
| Legal Eagle      |     7 | &#x2696; law   |  6.468 |
| Penny Pincher    |     6 | &#x1f4b2; cash |  6.450 |
| Yesman           |     6 | &#x1f454; boss |  6.438 |
| Number Cruncher  |     7 | &#x1f4b2; cash |  6.438 |
| Name Dropper     |     5 | &#x1f4c8; sell |  6.275 |
| Big Cheese       |     8 | &#x1f454; boss |  5.960 |
| Downsizer        |     7 | &#x1f454; boss |  5.945 |
| Loan Shark       |     7 | &#x1f4b2; cash |  5.940 |
| Ambulance Chaser |     5 | &#x2696; law   |  5.887 |
| Corporate Raider |     7 | &#x1f454; boss |  5.475 |
| Micromanager     |     6 | &#x1f454; boss |  5.152 |
| Bean Counter     |     5 | &#x1f4b2; cash |  5.100 |
| Telemarketer     |     5 | &#x1f4c8; sell |  5.040 |
| Name Dropper     |     4 | &#x1f4c8; sell |  4.965 |
| Pencil Pusher    |     5 | &#x1f454; boss |  4.950 |
| Bloodsucker      |     5 | &#x2696; law   |  4.890 |
| Money Bags       |     6 | &#x1f4b2; cash |  4.860 |
| Short Change     |     5 | &#x1f4b2; cash |  4.822 |
| Head Hunter      |     6 | &#x1f454; boss |  4.745 |
| Tightwad         |     5 | &#x1f4b2; cash |  4.740 |
| Flunky           |     5 | &#x1f454; boss |  4.740 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  4.688 |
| Two-Face         |     6 | &#x1f4c8; sell |  4.665 |
| Downsizer        |     6 | &#x1f454; boss |  4.435 |
| Yesman           |     5 | &#x1f454; boss |  4.362 |
| Glad Hander      |     6 | &#x1f4c8; sell |  4.325 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  4.300 |
| Ambulance Chaser |     4 | &#x2696; law   |  4.125 |
| Cold Caller      |     5 | &#x1f4c8; sell |  4.062 |
| Name Dropper     |     3 | &#x1f4c8; sell |  3.985 |
| Double Talker    |     5 | &#x2696; law   |  3.955 |
| Telemarketer     |     4 | &#x1f4c8; sell |  3.880 |
| Bottom Feeder    |     5 | &#x2696; law   |  3.880 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  3.530 |
| Pencil Pusher    |     4 | &#x1f454; boss |  3.525 |
| Bloodsucker      |     4 | &#x2696; law   |  3.400 |
| Bean Counter     |     4 | &#x1f4b2; cash |  3.400 |
| Short Change     |     4 | &#x1f4b2; cash |  3.385 |
| Cold Caller      |     4 | &#x1f4c8; sell |  3.255 |
| Telemarketer     |     3 | &#x1f4c8; sell |  3.157 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  3.150 |
| Downsizer        |     5 | &#x1f454; boss |  3.125 |
| Flunky           |     4 | &#x1f454; boss |  2.955 |
| Micromanager     |     5 | &#x1f454; boss |  2.955 |
| Bottom Feeder    |     4 | &#x2696; law   |  2.910 |
| Pencil Pusher    |     3 | &#x1f454; boss |  2.700 |
| Glad Hander      |     4 | &#x1f4c8; sell |  2.675 |
| Tightwad         |     4 | &#x1f4b2; cash |  2.670 |
| Short Change     |     3 | &#x1f4b2; cash |  2.582 |
| Glad Hander      |     5 | &#x1f4c8; sell |  2.560 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  2.488 |
| Yesman           |     4 | &#x1f454; boss |  2.455 |
| Cold Caller      |     3 | &#x1f4c8; sell |  2.423 |
| Bloodsucker      |     3 | &#x2696; law   |  2.410 |
| Tightwad         |     3 | &#x1f4b2; cash |  2.385 |
| Double Talker    |     4 | &#x2696; law   |  2.280 |
| Flunky           |     3 | &#x1f454; boss |  2.240 |
| Bottom Feeder    |     3 | &#x2696; law   |  2.225 |
| Telemarketer     |     2 | &#x1f4c8; sell |  2.138 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  1.825 |
| Micromanager     |     4 | &#x1f454; boss |  1.775 |
| Pencil Pusher    |     2 | &#x1f454; boss |  1.762 |
| Cold Caller      |     2 | &#x1f4c8; sell |  1.703 |
| Short Change     |     2 | &#x1f4b2; cash |  1.685 |
| Yesman           |     3 | &#x1f454; boss |  1.575 |
| Double Talker    |     3 | &#x2696; law   |  1.575 |
| Bloodsucker      |     2 | &#x2696; law   |  1.520 |
| Bottom Feeder    |     2 | &#x2696; law   |  1.450 |
| Short Change     |     1 | &#x1f4b2; cash |  1.423 |
| Cold Caller      |     1 | &#x1f4c8; sell |  1.345 |
| Flunky           |     2 | &#x1f454; boss |  1.255 |
| Flunky           |     1 | &#x1f454; boss |  1.050 |
| Bottom Feeder    |     1 | &#x2696; law   |  0.910 |

### Maximum aggregate damage

#### 1 toon, maximum aggregate damage

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| The Mingler      |    11 | &#x1f4c8; sell | 24.000 |
| Loan Shark       |    11 | &#x1f4b2; cash | 24.000 |
| Corporate Raider |    11 | &#x1f454; boss | 24.000 |
| Legal Eagle      |    11 | &#x2696; law   | 22.000 |
| Big Cheese       |    12 | &#x1f454; boss | 22.000 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 21.000 |
| The Mingler      |    10 | &#x1f4c8; sell | 21.000 |
| Loan Shark       |    10 | &#x1f4b2; cash | 21.000 |
| Robber Baron     |    12 | &#x1f4b2; cash | 21.000 |
| Big Wig          |    12 | &#x2696; law   | 21.000 |
| Head Hunter      |    10 | &#x1f454; boss | 21.000 |
| Corporate Raider |    10 | &#x1f454; boss | 21.000 |
| Glad Hander      |     8 | &#x1f4c8; sell | 20.000 |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 20.000 |
| Spin Doctor      |    10 | &#x2696; law   | 20.000 |
| Big Cheese       |    11 | &#x1f454; boss | 20.000 |
| Ambulance Chaser |     8 | &#x2696; law   | 19.000 |
| Legal Eagle      |    10 | &#x2696; law   | 19.000 |
| Big Wig          |    11 | &#x2696; law   | 19.000 |
| Mover & Shaker   |     8 | &#x1f4c8; sell | 18.000 |
| Two-Face         |    10 | &#x1f4c8; sell | 18.000 |
| The Mingler      |     9 | &#x1f4c8; sell | 18.000 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 18.000 |
| Tightwad         |     7 | &#x1f4b2; cash | 18.000 |
| Money Bags       |    10 | &#x1f4b2; cash | 18.000 |
| Loan Shark       |     9 | &#x1f4b2; cash | 18.000 |
| Robber Baron     |    11 | &#x1f4b2; cash | 18.000 |
| Double Talker    |     7 | &#x2696; law   | 18.000 |
| Back Stabber     |     9 | &#x2696; law   | 18.000 |
| Spin Doctor      |     9 | &#x2696; law   | 18.000 |
| Micromanager     |     8 | &#x1f454; boss | 18.000 |
| Head Hunter      |     9 | &#x1f454; boss | 18.000 |
| Corporate Raider |     9 | &#x1f454; boss | 18.000 |
| Big Cheese       |    10 | &#x1f454; boss | 18.000 |
| Legal Eagle      |     9 | &#x2696; law   | 17.000 |
| Big Wig          |    10 | &#x2696; law   | 17.000 |
| Two-Face         |     9 | &#x1f4c8; sell | 16.000 |
| Money Bags       |     9 | &#x1f4b2; cash | 16.000 |
| Robber Baron     |    10 | &#x1f4b2; cash | 16.000 |
| Big Cheese       |     9 | &#x1f454; boss | 16.000 |
| Glad Hander      |     7 | &#x1f4c8; sell | 15.000 |
| Mover & Shaker   |     7 | &#x1f4c8; sell | 15.000 |
| The Mingler      |     8 | &#x1f4c8; sell | 15.000 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 15.000 |
| Bean Counter     |     8 | &#x1f4b2; cash | 15.000 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 15.000 |
| Loan Shark       |     8 | &#x1f4b2; cash | 15.000 |
| Ambulance Chaser |     7 | &#x2696; law   | 15.000 |
| Back Stabber     |     8 | &#x2696; law   | 15.000 |
| Spin Doctor      |     8 | &#x2696; law   | 15.000 |
| Legal Eagle      |     8 | &#x2696; law   | 15.000 |
| Big Wig          |     9 | &#x2696; law   | 15.000 |
| Micromanager     |     7 | &#x1f454; boss | 15.000 |
| Downsizer        |     9 | &#x1f454; boss | 15.000 |
| Head Hunter      |     8 | &#x1f454; boss | 15.000 |
| Corporate Raider |     8 | &#x1f454; boss | 15.000 |
| Name Dropper     |     7 | &#x1f4c8; sell | 14.000 |
| Two-Face         |     8 | &#x1f4c8; sell | 14.000 |
| Money Bags       |     8 | &#x1f4b2; cash | 14.000 |
| Robber Baron     |     9 | &#x1f4b2; cash | 14.000 |
| Bloodsucker      |     6 | &#x2696; law   | 14.000 |
| Big Cheese       |     8 | &#x1f454; boss | 14.000 |
| Tightwad         |     6 | &#x1f4b2; cash | 13.000 |
| Number Cruncher  |     8 | &#x1f4b2; cash | 13.000 |
| Double Talker    |     6 | &#x2696; law   | 13.000 |
| Back Stabber     |     7 | &#x2696; law   | 13.000 |
| Big Wig          |     8 | &#x2696; law   | 13.000 |
| Downsizer        |     8 | &#x1f454; boss | 13.000 |
| Telemarketer     |     6 | &#x1f4c8; sell | 12.000 |
| Mover & Shaker   |     6 | &#x1f4c8; sell | 12.000 |
| Two-Face         |     7 | &#x1f4c8; sell | 12.000 |
| The Mingler      |     7 | &#x1f4c8; sell | 12.000 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell | 12.000 |
| Penny Pincher    |     6 | &#x1f4b2; cash | 12.000 |
| Bean Counter     |     7 | &#x1f4b2; cash | 12.000 |
| Money Bags       |     7 | &#x1f4b2; cash | 12.000 |
| Loan Shark       |     7 | &#x1f4b2; cash | 12.000 |
| Bloodsucker      |     5 | &#x2696; law   | 12.000 |
| Ambulance Chaser |     6 | &#x2696; law   | 12.000 |
| Spin Doctor      |     7 | &#x2696; law   | 12.000 |
| Legal Eagle      |     7 | &#x2696; law   | 12.000 |
| Pencil Pusher    |     6 | &#x1f454; boss | 12.000 |
| Micromanager     |     6 | &#x1f454; boss | 12.000 |
| Head Hunter      |     7 | &#x1f454; boss | 12.000 |
| Corporate Raider |     7 | &#x1f454; boss | 12.000 |
| Glad Hander      |     6 | &#x1f4c8; sell | 11.000 |
| Short Change     |     5 | &#x1f4b2; cash | 11.000 |
| Number Cruncher  |     7 | &#x1f4b2; cash | 11.000 |
| Robber Baron     |     8 | &#x1f4b2; cash | 11.000 |
| Back Stabber     |     6 | &#x2696; law   | 11.000 |
| Downsizer        |     7 | &#x1f454; boss | 11.000 |
| Cold Caller      |     5 | &#x1f4c8; sell | 10.000 |
| Name Dropper     |     6 | &#x1f4c8; sell | 10.000 |
| Two-Face         |     6 | &#x1f4c8; sell | 10.000 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell | 10.000 |
| Money Bags       |     6 | &#x1f4b2; cash | 10.000 |
| Bottom Feeder    |     5 | &#x2696; law   | 10.000 |
| Bloodsucker      |     4 | &#x2696; law   | 10.000 |
| Spin Doctor      |     6 | &#x2696; law   | 10.000 |
| Pencil Pusher    |     5 | &#x1f454; boss | 10.000 |
| Head Hunter      |     6 | &#x1f454; boss | 10.000 |
| Telemarketer     |     5 | &#x1f4c8; sell |  9.000 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  9.000 |
| Short Change     |     4 | &#x1f4b2; cash |  9.000 |
| Tightwad         |     5 | &#x1f4b2; cash |  9.000 |
| Bean Counter     |     6 | &#x1f4b2; cash |  9.000 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  9.000 |
| Double Talker    |     5 | &#x2696; law   |  9.000 |
| Downsizer        |     6 | &#x1f454; boss |  9.000 |
| Cold Caller      |     4 | &#x1f4c8; sell |  8.000 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  8.000 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  8.000 |
| Bottom Feeder    |     4 | &#x2696; law   |  8.000 |
| Bloodsucker      |     3 | &#x2696; law   |  8.000 |
| Ambulance Chaser |     5 | &#x2696; law   |  8.000 |
| Back Stabber     |     5 | &#x2696; law   |  8.000 |
| Pencil Pusher    |     4 | &#x1f454; boss |  8.000 |
| Yesman           |     7 | &#x1f454; boss |  8.000 |
| Micromanager     |     5 | &#x1f454; boss |  8.000 |
| Downsizer        |     5 | &#x1f454; boss |  8.000 |
| Telemarketer     |     4 | &#x1f4c8; sell |  7.000 |
| Name Dropper     |     5 | &#x1f4c8; sell |  7.000 |
| Glad Hander      |     5 | &#x1f4c8; sell |  7.000 |
| Short Change     |     3 | &#x1f4b2; cash |  7.000 |
| Flunky           |     5 | &#x1f454; boss |  7.000 |
| Yesman           |     6 | &#x1f454; boss |  7.000 |
| Cold Caller      |     3 | &#x1f4c8; sell |  6.000 |
| Telemarketer     |     3 | &#x1f4c8; sell |  6.000 |
| Name Dropper     |     4 | &#x1f4c8; sell |  6.000 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  6.000 |
| Tightwad         |     4 | &#x1f4b2; cash |  6.000 |
| Bean Counter     |     5 | &#x1f4b2; cash |  6.000 |
| Bottom Feeder    |     3 | &#x2696; law   |  6.000 |
| Bloodsucker      |     2 | &#x2696; law   |  6.000 |
| Double Talker    |     3 | &#x2696; law   |  6.000 |
| Double Talker    |     4 | &#x2696; law   |  6.000 |
| Ambulance Chaser |     4 | &#x2696; law   |  6.000 |
| Flunky           |     4 | &#x1f454; boss |  6.000 |
| Pencil Pusher    |     3 | &#x1f454; boss |  6.000 |
| Yesman           |     5 | &#x1f454; boss |  6.000 |
| Micromanager     |     4 | &#x1f454; boss |  6.000 |
| Name Dropper     |     3 | &#x1f4c8; sell |  5.000 |
| Glad Hander      |     4 | &#x1f4c8; sell |  5.000 |
| Short Change     |     2 | &#x1f4b2; cash |  5.000 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  5.000 |
| Tightwad         |     3 | &#x1f4b2; cash |  5.000 |
| Flunky           |     3 | &#x1f454; boss |  5.000 |
| Yesman           |     4 | &#x1f454; boss |  5.000 |
| Cold Caller      |     2 | &#x1f4c8; sell |  4.000 |
| Telemarketer     |     2 | &#x1f4c8; sell |  4.000 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  4.000 |
| Bean Counter     |     4 | &#x1f4b2; cash |  4.000 |
| Bottom Feeder    |     2 | &#x2696; law   |  4.000 |
| Flunky           |     2 | &#x1f454; boss |  4.000 |
| Pencil Pusher    |     2 | &#x1f454; boss |  4.000 |
| Yesman           |     3 | &#x1f454; boss |  4.000 |
| Cold Caller      |     1 | &#x1f4c8; sell |  3.000 |
| Short Change     |     1 | &#x1f4b2; cash |  3.000 |
| Bottom Feeder    |     1 | &#x2696; law   |  3.000 |
| Flunky           |     1 | &#x1f454; boss |  3.000 |

#### 2 toons, maximum aggregate damage

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| The Mingler      |    11 | &#x1f4c8; sell | 48.000 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 42.000 |
| The Mingler      |    10 | &#x1f4c8; sell | 42.000 |
| Robber Baron     |    12 | &#x1f4b2; cash | 42.000 |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 40.000 |
| Mover & Shaker   |     8 | &#x1f4c8; sell | 36.000 |
| The Mingler      |     9 | &#x1f4c8; sell | 36.000 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 36.000 |
| Robber Baron     |    11 | &#x1f4b2; cash | 36.000 |
| Back Stabber     |     9 | &#x2696; law   | 36.000 |
| Spin Doctor      |    10 | &#x2696; law   | 34.000 |
| Robber Baron     |    10 | &#x1f4b2; cash | 32.000 |
| Spin Doctor      |     9 | &#x2696; law   | 32.000 |
| Big Wig          |    12 | &#x2696; law   | 32.000 |
| Mover & Shaker   |     7 | &#x1f4c8; sell | 30.000 |
| The Mingler      |     8 | &#x1f4c8; sell | 30.000 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 30.000 |
| Ambulance Chaser |     8 | &#x2696; law   | 30.000 |
| Back Stabber     |     8 | &#x2696; law   | 30.000 |
| Big Wig          |    11 | &#x2696; law   | 30.000 |
| Robber Baron     |     9 | &#x1f4b2; cash | 28.000 |
| Back Stabber     |     7 | &#x2696; law   | 26.000 |
| Spin Doctor      |     8 | &#x2696; law   | 26.000 |
| Big Wig          |    10 | &#x2696; law   | 26.000 |
| Name Dropper     |     7 | &#x1f4c8; sell | 24.000 |
| Mover & Shaker   |     6 | &#x1f4c8; sell | 24.000 |
| The Mingler      |     7 | &#x1f4c8; sell | 24.000 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell | 24.000 |
| Loan Shark       |    11 | &#x1f4b2; cash | 24.000 |
| Ambulance Chaser |     7 | &#x2696; law   | 24.000 |
| Corporate Raider |    11 | &#x1f454; boss | 24.000 |
| Robber Baron     |     8 | &#x1f4b2; cash | 22.000 |
| Back Stabber     |     6 | &#x2696; law   | 22.000 |
| Legal Eagle      |    11 | &#x2696; law   | 22.000 |
| Big Wig          |     9 | &#x2696; law   | 22.000 |
| Big Cheese       |    12 | &#x1f454; boss | 22.000 |
| Loan Shark       |    10 | &#x1f4b2; cash | 21.000 |
| Head Hunter      |    10 | &#x1f454; boss | 21.000 |
| Corporate Raider |    10 | &#x1f454; boss | 21.000 |
| Glad Hander      |     8 | &#x1f4c8; sell | 20.000 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell | 20.000 |
| Spin Doctor      |     7 | &#x2696; law   | 20.000 |
| Big Wig          |     8 | &#x2696; law   | 20.000 |
| Big Cheese       |    11 | &#x1f454; boss | 20.000 |
| Legal Eagle      |    10 | &#x2696; law   | 19.000 |
| Name Dropper     |     6 | &#x1f4c8; sell | 18.000 |
| Mover & Shaker   |     5 | &#x1f4c8; sell | 18.000 |
| Two-Face         |    10 | &#x1f4c8; sell | 18.000 |
| Tightwad         |     7 | &#x1f4b2; cash | 18.000 |
| Money Bags       |    10 | &#x1f4b2; cash | 18.000 |
| Loan Shark       |     9 | &#x1f4b2; cash | 18.000 |
| Double Talker    |     7 | &#x2696; law   | 18.000 |
| Ambulance Chaser |     6 | &#x2696; law   | 18.000 |
| Spin Doctor      |     6 | &#x2696; law   | 18.000 |
| Micromanager     |     8 | &#x1f454; boss | 18.000 |
| Head Hunter      |     9 | &#x1f454; boss | 18.000 |
| Corporate Raider |     9 | &#x1f454; boss | 18.000 |
| Big Cheese       |    10 | &#x1f454; boss | 18.000 |
| Legal Eagle      |     9 | &#x2696; law   | 17.000 |
| Two-Face         |     9 | &#x1f4c8; sell | 16.000 |
| Money Bags       |     9 | &#x1f4b2; cash | 16.000 |
| Back Stabber     |     5 | &#x2696; law   | 16.000 |
| Yesman           |     7 | &#x1f454; boss | 16.000 |
| Big Cheese       |     9 | &#x1f454; boss | 16.000 |
| Glad Hander      |     7 | &#x1f4c8; sell | 15.000 |
| Bean Counter     |     8 | &#x1f4b2; cash | 15.000 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 15.000 |
| Loan Shark       |     8 | &#x1f4b2; cash | 15.000 |
| Legal Eagle      |     8 | &#x2696; law   | 15.000 |
| Micromanager     |     7 | &#x1f454; boss | 15.000 |
| Downsizer        |     9 | &#x1f454; boss | 15.000 |
| Head Hunter      |     8 | &#x1f454; boss | 15.000 |
| Corporate Raider |     8 | &#x1f454; boss | 15.000 |
| Two-Face         |     8 | &#x1f4c8; sell | 14.000 |
| Money Bags       |     8 | &#x1f4b2; cash | 14.000 |
| Bloodsucker      |     6 | &#x2696; law   | 14.000 |
| Yesman           |     6 | &#x1f454; boss | 14.000 |
| Big Cheese       |     8 | &#x1f454; boss | 14.000 |
| Tightwad         |     6 | &#x1f4b2; cash | 13.000 |
| Number Cruncher  |     8 | &#x1f4b2; cash | 13.000 |
| Double Talker    |     6 | &#x2696; law   | 13.000 |
| Downsizer        |     8 | &#x1f454; boss | 13.000 |
| Telemarketer     |     6 | &#x1f4c8; sell | 12.000 |
| Name Dropper     |     5 | &#x1f4c8; sell | 12.000 |
| Two-Face         |     7 | &#x1f4c8; sell | 12.000 |
| Penny Pincher    |     6 | &#x1f4b2; cash | 12.000 |
| Bean Counter     |     7 | &#x1f4b2; cash | 12.000 |
| Money Bags       |     7 | &#x1f4b2; cash | 12.000 |
| Loan Shark       |     7 | &#x1f4b2; cash | 12.000 |
| Bloodsucker      |     5 | &#x2696; law   | 12.000 |
| Ambulance Chaser |     5 | &#x2696; law   | 12.000 |
| Legal Eagle      |     7 | &#x2696; law   | 12.000 |
| Pencil Pusher    |     6 | &#x1f454; boss | 12.000 |
| Yesman           |     5 | &#x1f454; boss | 12.000 |
| Micromanager     |     6 | &#x1f454; boss | 12.000 |
| Head Hunter      |     7 | &#x1f454; boss | 12.000 |
| Corporate Raider |     7 | &#x1f454; boss | 12.000 |
| Glad Hander      |     6 | &#x1f4c8; sell | 11.000 |
| Short Change     |     5 | &#x1f4b2; cash | 11.000 |
| Number Cruncher  |     7 | &#x1f4b2; cash | 11.000 |
| Downsizer        |     7 | &#x1f454; boss | 11.000 |
| Cold Caller      |     5 | &#x1f4c8; sell | 10.000 |
| Two-Face         |     6 | &#x1f4c8; sell | 10.000 |
| Money Bags       |     6 | &#x1f4b2; cash | 10.000 |
| Bottom Feeder    |     5 | &#x2696; law   | 10.000 |
| Bloodsucker      |     4 | &#x2696; law   | 10.000 |
| Pencil Pusher    |     5 | &#x1f454; boss | 10.000 |
| Yesman           |     4 | &#x1f454; boss | 10.000 |
| Head Hunter      |     6 | &#x1f454; boss | 10.000 |
| Telemarketer     |     5 | &#x1f4c8; sell |  9.000 |
| Short Change     |     4 | &#x1f4b2; cash |  9.000 |
| Tightwad         |     5 | &#x1f4b2; cash |  9.000 |
| Bean Counter     |     6 | &#x1f4b2; cash |  9.000 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  9.000 |
| Double Talker    |     5 | &#x2696; law   |  9.000 |
| Downsizer        |     6 | &#x1f454; boss |  9.000 |
| Cold Caller      |     4 | &#x1f4c8; sell |  8.000 |
| Name Dropper     |     4 | &#x1f4c8; sell |  8.000 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  8.000 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  8.000 |
| Bottom Feeder    |     4 | &#x2696; law   |  8.000 |
| Bloodsucker      |     3 | &#x2696; law   |  8.000 |
| Ambulance Chaser |     4 | &#x2696; law   |  8.000 |
| Pencil Pusher    |     4 | &#x1f454; boss |  8.000 |
| Yesman           |     3 | &#x1f454; boss |  8.000 |
| Micromanager     |     5 | &#x1f454; boss |  8.000 |
| Downsizer        |     5 | &#x1f454; boss |  8.000 |
| Telemarketer     |     4 | &#x1f4c8; sell |  7.000 |
| Glad Hander      |     5 | &#x1f4c8; sell |  7.000 |
| Short Change     |     3 | &#x1f4b2; cash |  7.000 |
| Flunky           |     5 | &#x1f454; boss |  7.000 |
| Cold Caller      |     3 | &#x1f4c8; sell |  6.000 |
| Telemarketer     |     3 | &#x1f4c8; sell |  6.000 |
| Name Dropper     |     3 | &#x1f4c8; sell |  6.000 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  6.000 |
| Tightwad         |     4 | &#x1f4b2; cash |  6.000 |
| Bean Counter     |     5 | &#x1f4b2; cash |  6.000 |
| Bottom Feeder    |     3 | &#x2696; law   |  6.000 |
| Bloodsucker      |     2 | &#x2696; law   |  6.000 |
| Double Talker    |     3 | &#x2696; law   |  6.000 |
| Double Talker    |     4 | &#x2696; law   |  6.000 |
| Flunky           |     4 | &#x1f454; boss |  6.000 |
| Pencil Pusher    |     3 | &#x1f454; boss |  6.000 |
| Micromanager     |     4 | &#x1f454; boss |  6.000 |
| Glad Hander      |     4 | &#x1f4c8; sell |  5.000 |
| Short Change     |     2 | &#x1f4b2; cash |  5.000 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  5.000 |
| Tightwad         |     3 | &#x1f4b2; cash |  5.000 |
| Flunky           |     3 | &#x1f454; boss |  5.000 |
| Cold Caller      |     2 | &#x1f4c8; sell |  4.000 |
| Telemarketer     |     2 | &#x1f4c8; sell |  4.000 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  4.000 |
| Bean Counter     |     4 | &#x1f4b2; cash |  4.000 |
| Bottom Feeder    |     2 | &#x2696; law   |  4.000 |
| Flunky           |     2 | &#x1f454; boss |  4.000 |
| Pencil Pusher    |     2 | &#x1f454; boss |  4.000 |
| Cold Caller      |     1 | &#x1f4c8; sell |  3.000 |
| Short Change     |     1 | &#x1f4b2; cash |  3.000 |
| Bottom Feeder    |     1 | &#x2696; law   |  3.000 |
| Flunky           |     1 | &#x1f454; boss |  3.000 |

#### 3 toons, maximum aggregate damage

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| The Mingler      |    11 | &#x1f4c8; sell | 72.000 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 63.000 |
| The Mingler      |    10 | &#x1f4c8; sell | 63.000 |
| Robber Baron     |    12 | &#x1f4b2; cash | 63.000 |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 60.000 |
| Mover & Shaker   |     8 | &#x1f4c8; sell | 54.000 |
| The Mingler      |     9 | &#x1f4c8; sell | 54.000 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 54.000 |
| Robber Baron     |    11 | &#x1f4b2; cash | 54.000 |
| Back Stabber     |     9 | &#x2696; law   | 54.000 |
| Spin Doctor      |    10 | &#x2696; law   | 51.000 |
| Robber Baron     |    10 | &#x1f4b2; cash | 48.000 |
| Spin Doctor      |     9 | &#x2696; law   | 48.000 |
| Big Wig          |    12 | &#x2696; law   | 48.000 |
| Mover & Shaker   |     7 | &#x1f4c8; sell | 45.000 |
| The Mingler      |     8 | &#x1f4c8; sell | 45.000 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 45.000 |
| Ambulance Chaser |     8 | &#x2696; law   | 45.000 |
| Back Stabber     |     8 | &#x2696; law   | 45.000 |
| Big Wig          |    11 | &#x2696; law   | 45.000 |
| Robber Baron     |     9 | &#x1f4b2; cash | 42.000 |
| Back Stabber     |     7 | &#x2696; law   | 39.000 |
| Spin Doctor      |     8 | &#x2696; law   | 39.000 |
| Big Wig          |    10 | &#x2696; law   | 39.000 |
| Name Dropper     |     7 | &#x1f4c8; sell | 36.000 |
| Mover & Shaker   |     6 | &#x1f4c8; sell | 36.000 |
| The Mingler      |     7 | &#x1f4c8; sell | 36.000 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell | 36.000 |
| Ambulance Chaser |     7 | &#x2696; law   | 36.000 |
| Robber Baron     |     8 | &#x1f4b2; cash | 33.000 |
| Back Stabber     |     6 | &#x2696; law   | 33.000 |
| Big Wig          |     9 | &#x2696; law   | 33.000 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell | 30.000 |
| Spin Doctor      |     7 | &#x2696; law   | 30.000 |
| Big Wig          |     8 | &#x2696; law   | 30.000 |
| Name Dropper     |     6 | &#x1f4c8; sell | 27.000 |
| Mover & Shaker   |     5 | &#x1f4c8; sell | 27.000 |
| Ambulance Chaser |     6 | &#x2696; law   | 27.000 |
| Spin Doctor      |     6 | &#x2696; law   | 27.000 |
| Loan Shark       |    11 | &#x1f4b2; cash | 24.000 |
| Back Stabber     |     5 | &#x2696; law   | 24.000 |
| Yesman           |     7 | &#x1f454; boss | 24.000 |
| Corporate Raider |    11 | &#x1f454; boss | 24.000 |
| Legal Eagle      |    11 | &#x2696; law   | 22.000 |
| Big Cheese       |    12 | &#x1f454; boss | 22.000 |
| Loan Shark       |    10 | &#x1f4b2; cash | 21.000 |
| Yesman           |     6 | &#x1f454; boss | 21.000 |
| Head Hunter      |    10 | &#x1f454; boss | 21.000 |
| Corporate Raider |    10 | &#x1f454; boss | 21.000 |
| Glad Hander      |     8 | &#x1f4c8; sell | 20.000 |
| Big Cheese       |    11 | &#x1f454; boss | 20.000 |
| Legal Eagle      |    10 | &#x2696; law   | 19.000 |
| Name Dropper     |     5 | &#x1f4c8; sell | 18.000 |
| Two-Face         |    10 | &#x1f4c8; sell | 18.000 |
| Tightwad         |     7 | &#x1f4b2; cash | 18.000 |
| Money Bags       |    10 | &#x1f4b2; cash | 18.000 |
| Loan Shark       |     9 | &#x1f4b2; cash | 18.000 |
| Double Talker    |     7 | &#x2696; law   | 18.000 |
| Ambulance Chaser |     5 | &#x2696; law   | 18.000 |
| Yesman           |     5 | &#x1f454; boss | 18.000 |
| Micromanager     |     8 | &#x1f454; boss | 18.000 |
| Head Hunter      |     9 | &#x1f454; boss | 18.000 |
| Corporate Raider |     9 | &#x1f454; boss | 18.000 |
| Big Cheese       |    10 | &#x1f454; boss | 18.000 |
| Legal Eagle      |     9 | &#x2696; law   | 17.000 |
| Two-Face         |     9 | &#x1f4c8; sell | 16.000 |
| Money Bags       |     9 | &#x1f4b2; cash | 16.000 |
| Big Cheese       |     9 | &#x1f454; boss | 16.000 |
| Glad Hander      |     7 | &#x1f4c8; sell | 15.000 |
| Bean Counter     |     8 | &#x1f4b2; cash | 15.000 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 15.000 |
| Loan Shark       |     8 | &#x1f4b2; cash | 15.000 |
| Legal Eagle      |     8 | &#x2696; law   | 15.000 |
| Yesman           |     4 | &#x1f454; boss | 15.000 |
| Micromanager     |     7 | &#x1f454; boss | 15.000 |
| Downsizer        |     9 | &#x1f454; boss | 15.000 |
| Head Hunter      |     8 | &#x1f454; boss | 15.000 |
| Corporate Raider |     8 | &#x1f454; boss | 15.000 |
| Two-Face         |     8 | &#x1f4c8; sell | 14.000 |
| Money Bags       |     8 | &#x1f4b2; cash | 14.000 |
| Bloodsucker      |     6 | &#x2696; law   | 14.000 |
| Big Cheese       |     8 | &#x1f454; boss | 14.000 |
| Tightwad         |     6 | &#x1f4b2; cash | 13.000 |
| Number Cruncher  |     8 | &#x1f4b2; cash | 13.000 |
| Double Talker    |     6 | &#x2696; law   | 13.000 |
| Downsizer        |     8 | &#x1f454; boss | 13.000 |
| Telemarketer     |     6 | &#x1f4c8; sell | 12.000 |
| Name Dropper     |     4 | &#x1f4c8; sell | 12.000 |
| Two-Face         |     7 | &#x1f4c8; sell | 12.000 |
| Penny Pincher    |     6 | &#x1f4b2; cash | 12.000 |
| Bean Counter     |     7 | &#x1f4b2; cash | 12.000 |
| Money Bags       |     7 | &#x1f4b2; cash | 12.000 |
| Loan Shark       |     7 | &#x1f4b2; cash | 12.000 |
| Bloodsucker      |     5 | &#x2696; law   | 12.000 |
| Ambulance Chaser |     4 | &#x2696; law   | 12.000 |
| Legal Eagle      |     7 | &#x2696; law   | 12.000 |
| Pencil Pusher    |     6 | &#x1f454; boss | 12.000 |
| Yesman           |     3 | &#x1f454; boss | 12.000 |
| Micromanager     |     6 | &#x1f454; boss | 12.000 |
| Head Hunter      |     7 | &#x1f454; boss | 12.000 |
| Corporate Raider |     7 | &#x1f454; boss | 12.000 |
| Glad Hander      |     6 | &#x1f4c8; sell | 11.000 |
| Short Change     |     5 | &#x1f4b2; cash | 11.000 |
| Number Cruncher  |     7 | &#x1f4b2; cash | 11.000 |
| Downsizer        |     7 | &#x1f454; boss | 11.000 |
| Cold Caller      |     5 | &#x1f4c8; sell | 10.000 |
| Two-Face         |     6 | &#x1f4c8; sell | 10.000 |
| Money Bags       |     6 | &#x1f4b2; cash | 10.000 |
| Bottom Feeder    |     5 | &#x2696; law   | 10.000 |
| Bloodsucker      |     4 | &#x2696; law   | 10.000 |
| Pencil Pusher    |     5 | &#x1f454; boss | 10.000 |
| Head Hunter      |     6 | &#x1f454; boss | 10.000 |
| Telemarketer     |     5 | &#x1f4c8; sell |  9.000 |
| Name Dropper     |     3 | &#x1f4c8; sell |  9.000 |
| Short Change     |     4 | &#x1f4b2; cash |  9.000 |
| Tightwad         |     5 | &#x1f4b2; cash |  9.000 |
| Bean Counter     |     6 | &#x1f4b2; cash |  9.000 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  9.000 |
| Double Talker    |     5 | &#x2696; law   |  9.000 |
| Downsizer        |     6 | &#x1f454; boss |  9.000 |
| Cold Caller      |     4 | &#x1f4c8; sell |  8.000 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  8.000 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  8.000 |
| Bottom Feeder    |     4 | &#x2696; law   |  8.000 |
| Bloodsucker      |     3 | &#x2696; law   |  8.000 |
| Pencil Pusher    |     4 | &#x1f454; boss |  8.000 |
| Micromanager     |     5 | &#x1f454; boss |  8.000 |
| Downsizer        |     5 | &#x1f454; boss |  8.000 |
| Telemarketer     |     4 | &#x1f4c8; sell |  7.000 |
| Glad Hander      |     5 | &#x1f4c8; sell |  7.000 |
| Short Change     |     3 | &#x1f4b2; cash |  7.000 |
| Flunky           |     5 | &#x1f454; boss |  7.000 |
| Cold Caller      |     3 | &#x1f4c8; sell |  6.000 |
| Telemarketer     |     3 | &#x1f4c8; sell |  6.000 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  6.000 |
| Tightwad         |     4 | &#x1f4b2; cash |  6.000 |
| Bean Counter     |     5 | &#x1f4b2; cash |  6.000 |
| Bottom Feeder    |     3 | &#x2696; law   |  6.000 |
| Bloodsucker      |     2 | &#x2696; law   |  6.000 |
| Double Talker    |     3 | &#x2696; law   |  6.000 |
| Double Talker    |     4 | &#x2696; law   |  6.000 |
| Flunky           |     4 | &#x1f454; boss |  6.000 |
| Pencil Pusher    |     3 | &#x1f454; boss |  6.000 |
| Micromanager     |     4 | &#x1f454; boss |  6.000 |
| Glad Hander      |     4 | &#x1f4c8; sell |  5.000 |
| Short Change     |     2 | &#x1f4b2; cash |  5.000 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  5.000 |
| Tightwad         |     3 | &#x1f4b2; cash |  5.000 |
| Flunky           |     3 | &#x1f454; boss |  5.000 |
| Cold Caller      |     2 | &#x1f4c8; sell |  4.000 |
| Telemarketer     |     2 | &#x1f4c8; sell |  4.000 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  4.000 |
| Bean Counter     |     4 | &#x1f4b2; cash |  4.000 |
| Bottom Feeder    |     2 | &#x2696; law   |  4.000 |
| Flunky           |     2 | &#x1f454; boss |  4.000 |
| Pencil Pusher    |     2 | &#x1f454; boss |  4.000 |
| Cold Caller      |     1 | &#x1f4c8; sell |  3.000 |
| Short Change     |     1 | &#x1f4b2; cash |  3.000 |
| Bottom Feeder    |     1 | &#x2696; law   |  3.000 |
| Flunky           |     1 | &#x1f454; boss |  3.000 |

#### 4 toons, maximum aggregate damage

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| The Mingler      |    11 | &#x1f4c8; sell | 96.000 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 84.000 |
| The Mingler      |    10 | &#x1f4c8; sell | 84.000 |
| Robber Baron     |    12 | &#x1f4b2; cash | 84.000 |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 80.000 |
| Mover & Shaker   |     8 | &#x1f4c8; sell | 72.000 |
| The Mingler      |     9 | &#x1f4c8; sell | 72.000 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 72.000 |
| Robber Baron     |    11 | &#x1f4b2; cash | 72.000 |
| Back Stabber     |     9 | &#x2696; law   | 72.000 |
| Spin Doctor      |    10 | &#x2696; law   | 68.000 |
| Robber Baron     |    10 | &#x1f4b2; cash | 64.000 |
| Spin Doctor      |     9 | &#x2696; law   | 64.000 |
| Big Wig          |    12 | &#x2696; law   | 64.000 |
| Mover & Shaker   |     7 | &#x1f4c8; sell | 60.000 |
| The Mingler      |     8 | &#x1f4c8; sell | 60.000 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 60.000 |
| Ambulance Chaser |     8 | &#x2696; law   | 60.000 |
| Back Stabber     |     8 | &#x2696; law   | 60.000 |
| Big Wig          |    11 | &#x2696; law   | 60.000 |
| Robber Baron     |     9 | &#x1f4b2; cash | 56.000 |
| Back Stabber     |     7 | &#x2696; law   | 52.000 |
| Spin Doctor      |     8 | &#x2696; law   | 52.000 |
| Big Wig          |    10 | &#x2696; law   | 52.000 |
| Name Dropper     |     7 | &#x1f4c8; sell | 48.000 |
| Mover & Shaker   |     6 | &#x1f4c8; sell | 48.000 |
| The Mingler      |     7 | &#x1f4c8; sell | 48.000 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell | 48.000 |
| Ambulance Chaser |     7 | &#x2696; law   | 48.000 |
| Robber Baron     |     8 | &#x1f4b2; cash | 44.000 |
| Back Stabber     |     6 | &#x2696; law   | 44.000 |
| Big Wig          |     9 | &#x2696; law   | 44.000 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell | 40.000 |
| Spin Doctor      |     7 | &#x2696; law   | 40.000 |
| Big Wig          |     8 | &#x2696; law   | 40.000 |
| Name Dropper     |     6 | &#x1f4c8; sell | 36.000 |
| Mover & Shaker   |     5 | &#x1f4c8; sell | 36.000 |
| Ambulance Chaser |     6 | &#x2696; law   | 36.000 |
| Spin Doctor      |     6 | &#x2696; law   | 36.000 |
| Back Stabber     |     5 | &#x2696; law   | 32.000 |
| Yesman           |     7 | &#x1f454; boss | 32.000 |
| Yesman           |     6 | &#x1f454; boss | 28.000 |
| Name Dropper     |     5 | &#x1f4c8; sell | 24.000 |
| Loan Shark       |    11 | &#x1f4b2; cash | 24.000 |
| Ambulance Chaser |     5 | &#x2696; law   | 24.000 |
| Yesman           |     5 | &#x1f454; boss | 24.000 |
| Corporate Raider |    11 | &#x1f454; boss | 24.000 |
| Legal Eagle      |    11 | &#x2696; law   | 22.000 |
| Big Cheese       |    12 | &#x1f454; boss | 22.000 |
| Loan Shark       |    10 | &#x1f4b2; cash | 21.000 |
| Head Hunter      |    10 | &#x1f454; boss | 21.000 |
| Corporate Raider |    10 | &#x1f454; boss | 21.000 |
| Glad Hander      |     8 | &#x1f4c8; sell | 20.000 |
| Yesman           |     4 | &#x1f454; boss | 20.000 |
| Big Cheese       |    11 | &#x1f454; boss | 20.000 |
| Legal Eagle      |    10 | &#x2696; law   | 19.000 |
| Two-Face         |    10 | &#x1f4c8; sell | 18.000 |
| Tightwad         |     7 | &#x1f4b2; cash | 18.000 |
| Money Bags       |    10 | &#x1f4b2; cash | 18.000 |
| Loan Shark       |     9 | &#x1f4b2; cash | 18.000 |
| Double Talker    |     7 | &#x2696; law   | 18.000 |
| Micromanager     |     8 | &#x1f454; boss | 18.000 |
| Head Hunter      |     9 | &#x1f454; boss | 18.000 |
| Corporate Raider |     9 | &#x1f454; boss | 18.000 |
| Big Cheese       |    10 | &#x1f454; boss | 18.000 |
| Legal Eagle      |     9 | &#x2696; law   | 17.000 |
| Name Dropper     |     4 | &#x1f4c8; sell | 16.000 |
| Two-Face         |     9 | &#x1f4c8; sell | 16.000 |
| Money Bags       |     9 | &#x1f4b2; cash | 16.000 |
| Ambulance Chaser |     4 | &#x2696; law   | 16.000 |
| Yesman           |     3 | &#x1f454; boss | 16.000 |
| Big Cheese       |     9 | &#x1f454; boss | 16.000 |
| Glad Hander      |     7 | &#x1f4c8; sell | 15.000 |
| Bean Counter     |     8 | &#x1f4b2; cash | 15.000 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 15.000 |
| Loan Shark       |     8 | &#x1f4b2; cash | 15.000 |
| Legal Eagle      |     8 | &#x2696; law   | 15.000 |
| Micromanager     |     7 | &#x1f454; boss | 15.000 |
| Downsizer        |     9 | &#x1f454; boss | 15.000 |
| Head Hunter      |     8 | &#x1f454; boss | 15.000 |
| Corporate Raider |     8 | &#x1f454; boss | 15.000 |
| Two-Face         |     8 | &#x1f4c8; sell | 14.000 |
| Money Bags       |     8 | &#x1f4b2; cash | 14.000 |
| Bloodsucker      |     6 | &#x2696; law   | 14.000 |
| Big Cheese       |     8 | &#x1f454; boss | 14.000 |
| Tightwad         |     6 | &#x1f4b2; cash | 13.000 |
| Number Cruncher  |     8 | &#x1f4b2; cash | 13.000 |
| Double Talker    |     6 | &#x2696; law   | 13.000 |
| Downsizer        |     8 | &#x1f454; boss | 13.000 |
| Telemarketer     |     6 | &#x1f4c8; sell | 12.000 |
| Name Dropper     |     3 | &#x1f4c8; sell | 12.000 |
| Two-Face         |     7 | &#x1f4c8; sell | 12.000 |
| Penny Pincher    |     6 | &#x1f4b2; cash | 12.000 |
| Bean Counter     |     7 | &#x1f4b2; cash | 12.000 |
| Money Bags       |     7 | &#x1f4b2; cash | 12.000 |
| Loan Shark       |     7 | &#x1f4b2; cash | 12.000 |
| Bloodsucker      |     5 | &#x2696; law   | 12.000 |
| Legal Eagle      |     7 | &#x2696; law   | 12.000 |
| Pencil Pusher    |     6 | &#x1f454; boss | 12.000 |
| Micromanager     |     6 | &#x1f454; boss | 12.000 |
| Head Hunter      |     7 | &#x1f454; boss | 12.000 |
| Corporate Raider |     7 | &#x1f454; boss | 12.000 |
| Glad Hander      |     6 | &#x1f4c8; sell | 11.000 |
| Short Change     |     5 | &#x1f4b2; cash | 11.000 |
| Number Cruncher  |     7 | &#x1f4b2; cash | 11.000 |
| Downsizer        |     7 | &#x1f454; boss | 11.000 |
| Cold Caller      |     5 | &#x1f4c8; sell | 10.000 |
| Two-Face         |     6 | &#x1f4c8; sell | 10.000 |
| Money Bags       |     6 | &#x1f4b2; cash | 10.000 |
| Bottom Feeder    |     5 | &#x2696; law   | 10.000 |
| Bloodsucker      |     4 | &#x2696; law   | 10.000 |
| Pencil Pusher    |     5 | &#x1f454; boss | 10.000 |
| Head Hunter      |     6 | &#x1f454; boss | 10.000 |
| Telemarketer     |     5 | &#x1f4c8; sell |  9.000 |
| Short Change     |     4 | &#x1f4b2; cash |  9.000 |
| Tightwad         |     5 | &#x1f4b2; cash |  9.000 |
| Bean Counter     |     6 | &#x1f4b2; cash |  9.000 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  9.000 |
| Double Talker    |     5 | &#x2696; law   |  9.000 |
| Downsizer        |     6 | &#x1f454; boss |  9.000 |
| Cold Caller      |     4 | &#x1f4c8; sell |  8.000 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  8.000 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  8.000 |
| Bottom Feeder    |     4 | &#x2696; law   |  8.000 |
| Bloodsucker      |     3 | &#x2696; law   |  8.000 |
| Pencil Pusher    |     4 | &#x1f454; boss |  8.000 |
| Micromanager     |     5 | &#x1f454; boss |  8.000 |
| Downsizer        |     5 | &#x1f454; boss |  8.000 |
| Telemarketer     |     4 | &#x1f4c8; sell |  7.000 |
| Glad Hander      |     5 | &#x1f4c8; sell |  7.000 |
| Short Change     |     3 | &#x1f4b2; cash |  7.000 |
| Flunky           |     5 | &#x1f454; boss |  7.000 |
| Cold Caller      |     3 | &#x1f4c8; sell |  6.000 |
| Telemarketer     |     3 | &#x1f4c8; sell |  6.000 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  6.000 |
| Tightwad         |     4 | &#x1f4b2; cash |  6.000 |
| Bean Counter     |     5 | &#x1f4b2; cash |  6.000 |
| Bottom Feeder    |     3 | &#x2696; law   |  6.000 |
| Bloodsucker      |     2 | &#x2696; law   |  6.000 |
| Double Talker    |     3 | &#x2696; law   |  6.000 |
| Double Talker    |     4 | &#x2696; law   |  6.000 |
| Flunky           |     4 | &#x1f454; boss |  6.000 |
| Pencil Pusher    |     3 | &#x1f454; boss |  6.000 |
| Micromanager     |     4 | &#x1f454; boss |  6.000 |
| Glad Hander      |     4 | &#x1f4c8; sell |  5.000 |
| Short Change     |     2 | &#x1f4b2; cash |  5.000 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  5.000 |
| Tightwad         |     3 | &#x1f4b2; cash |  5.000 |
| Flunky           |     3 | &#x1f454; boss |  5.000 |
| Cold Caller      |     2 | &#x1f4c8; sell |  4.000 |
| Telemarketer     |     2 | &#x1f4c8; sell |  4.000 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  4.000 |
| Bean Counter     |     4 | &#x1f4b2; cash |  4.000 |
| Bottom Feeder    |     2 | &#x2696; law   |  4.000 |
| Flunky           |     2 | &#x1f454; boss |  4.000 |
| Pencil Pusher    |     2 | &#x1f454; boss |  4.000 |
| Cold Caller      |     1 | &#x1f4c8; sell |  3.000 |
| Short Change     |     1 | &#x1f4b2; cash |  3.000 |
| Bottom Feeder    |     1 | &#x2696; law   |  3.000 |
| Flunky           |     1 | &#x1f454; boss |  3.000 |

## Damage to given single toon

### Expected damage to given single toon

#### 1 toon, expected damage to given single toon

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 19.000 |
| Legal Eagle      |    11 | &#x2696; law   | 18.157 |
| Big Cheese       |    12 | &#x1f454; boss | 17.090 |
| Big Wig          |    12 | &#x2696; law   | 17.050 |
| Loan Shark       |    11 | &#x1f4b2; cash | 16.725 |
| The Mingler      |    11 | &#x1f4c8; sell | 16.140 |
| Corporate Raider |    11 | &#x1f454; boss | 15.765 |
| Robber Baron     |    12 | &#x1f4b2; cash | 15.600 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 15.300 |
| Big Wig          |    11 | &#x2696; law   | 14.825 |
| Spin Doctor      |    10 | &#x2696; law   | 14.800 |
| Legal Eagle      |    10 | &#x2696; law   | 14.607 |
| Head Hunter      |    10 | &#x1f454; boss | 14.303 |
| Big Cheese       |    11 | &#x1f454; boss | 14.085 |
| Robber Baron     |    11 | &#x1f4b2; cash | 13.550 |
| Loan Shark       |    10 | &#x1f4b2; cash | 13.445 |
| Glad Hander      |     8 | &#x1f4c8; sell | 13.295 |
| The Mingler      |    10 | &#x1f4c8; sell | 13.197 |
| Money Bags       |    10 | &#x1f4b2; cash | 12.870 |
| Corporate Raider |    10 | &#x1f454; boss | 12.825 |
| Bean Counter     |     8 | &#x1f4b2; cash | 12.750 |
| Big Wig          |    10 | &#x2696; law   | 12.750 |
| Two-Face         |    10 | &#x1f4c8; sell | 12.705 |
| Spin Doctor      |     9 | &#x2696; law   | 12.683 |
| Back Stabber     |     9 | &#x2696; law   | 11.925 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 11.800 |
| Legal Eagle      |     9 | &#x2696; law   | 11.598 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 11.575 |
| Head Hunter      |     9 | &#x1f454; boss | 11.325 |
| Big Cheese       |    10 | &#x1f454; boss | 11.060 |
| Robber Baron     |    10 | &#x1f4b2; cash | 10.850 |
| Loan Shark       |     9 | &#x1f4b2; cash | 10.845 |
| Big Wig          |     9 | &#x2696; law   | 10.775 |
| Money Bags       |     9 | &#x1f4b2; cash | 10.717 |
| Two-Face         |     9 | &#x1f4c8; sell | 10.582 |
| Tightwad         |     7 | &#x1f4b2; cash | 10.582 |
| Micromanager     |     8 | &#x1f454; boss | 10.448 |
| The Mingler      |     9 | &#x1f4c8; sell | 10.425 |
| Corporate Raider |     9 | &#x1f454; boss | 10.205 |
| Bean Counter     |     7 | &#x1f4b2; cash | 10.200 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 10.103 |
| Double Talker    |     7 | &#x2696; law   | 10.080 |
| Name Dropper     |     7 | &#x1f4c8; sell |  9.925 |
| Spin Doctor      |     8 | &#x2696; law   |  9.900 |
| Mover & Shaker   |     8 | &#x1f4c8; sell |  9.455 |
| Downsizer        |     9 | &#x1f454; boss |  9.275 |
| Back Stabber     |     8 | &#x2696; law   |  9.262 |
| Big Wig          |     8 | &#x2696; law   |  8.950 |
| Legal Eagle      |     8 | &#x2696; law   |  8.928 |
| Head Hunter      |     8 | &#x1f454; boss |  8.800 |
| Tightwad         |     6 | &#x1f4b2; cash |  8.662 |
| Money Bags       |     8 | &#x1f4b2; cash |  8.640 |
| Ambulance Chaser |     8 | &#x2696; law   |  8.588 |
| Loan Shark       |     8 | &#x1f4b2; cash |  8.480 |
| Robber Baron     |     9 | &#x1f4b2; cash |  8.450 |
| Two-Face         |     8 | &#x1f4c8; sell |  8.430 |
| Big Cheese       |     9 | &#x1f454; boss |  8.285 |
| Number Cruncher  |     8 | &#x1f4b2; cash |  8.190 |
| Glad Hander      |     7 | &#x1f4c8; sell |  8.080 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell |  8.025 |
| The Mingler      |     8 | &#x1f4c8; sell |  7.778 |
| Bean Counter     |     6 | &#x1f4b2; cash |  7.650 |
| Corporate Raider |     8 | &#x1f454; boss |  7.635 |
| Micromanager     |     7 | &#x1f454; boss |  7.590 |
| Downsizer        |     8 | &#x1f454; boss |  7.537 |
| Mover & Shaker   |     7 | &#x1f4c8; sell |  7.450 |
| Spin Doctor      |     7 | &#x2696; law   |  7.382 |
| Bloodsucker      |     6 | &#x2696; law   |  7.330 |
| Back Stabber     |     7 | &#x2696; law   |  7.328 |
| Name Dropper     |     6 | &#x1f4c8; sell |  7.190 |
| Ambulance Chaser |     7 | &#x2696; law   |  6.938 |
| Telemarketer     |     6 | &#x1f4c8; sell |  6.922 |
| Pencil Pusher    |     6 | &#x1f454; boss |  6.900 |
| Money Bags       |     7 | &#x1f4b2; cash |  6.763 |
| Double Talker    |     6 | &#x2696; law   |  6.720 |
| Head Hunter      |     7 | &#x1f454; boss |  6.540 |
| Two-Face         |     7 | &#x1f4c8; sell |  6.508 |
| Legal Eagle      |     7 | &#x2696; law   |  6.468 |
| Penny Pincher    |     6 | &#x1f4b2; cash |  6.450 |
| Number Cruncher  |     7 | &#x1f4b2; cash |  6.438 |
| Robber Baron     |     8 | &#x1f4b2; cash |  6.300 |
| Big Cheese       |     8 | &#x1f454; boss |  5.960 |
| Downsizer        |     7 | &#x1f454; boss |  5.945 |
| Loan Shark       |     7 | &#x1f4b2; cash |  5.940 |
| The Mingler      |     7 | &#x1f4c8; sell |  5.615 |
| Back Stabber     |     6 | &#x2696; law   |  5.593 |
| Spin Doctor      |     6 | &#x2696; law   |  5.570 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell |  5.550 |
| Ambulance Chaser |     6 | &#x2696; law   |  5.513 |
| Mover & Shaker   |     6 | &#x1f4c8; sell |  5.505 |
| Corporate Raider |     7 | &#x1f454; boss |  5.475 |
| Micromanager     |     6 | &#x1f454; boss |  5.152 |
| Bean Counter     |     5 | &#x1f4b2; cash |  5.100 |
| Telemarketer     |     5 | &#x1f4c8; sell |  5.040 |
| Pencil Pusher    |     5 | &#x1f454; boss |  4.950 |
| Name Dropper     |     5 | &#x1f4c8; sell |  4.925 |
| Bloodsucker      |     5 | &#x2696; law   |  4.890 |
| Money Bags       |     6 | &#x1f4b2; cash |  4.860 |
| Short Change     |     5 | &#x1f4b2; cash |  4.822 |
| Head Hunter      |     6 | &#x1f454; boss |  4.745 |
| Tightwad         |     5 | &#x1f4b2; cash |  4.740 |
| Flunky           |     5 | &#x1f454; boss |  4.740 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  4.688 |
| Two-Face         |     6 | &#x1f4c8; sell |  4.665 |
| Yesman           |     7 | &#x1f454; boss |  4.450 |
| Downsizer        |     6 | &#x1f454; boss |  4.435 |
| Glad Hander      |     6 | &#x1f4c8; sell |  4.325 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  4.300 |
| Name Dropper     |     4 | &#x1f4c8; sell |  4.065 |
| Cold Caller      |     5 | &#x1f4c8; sell |  4.062 |
| Double Talker    |     5 | &#x2696; law   |  3.955 |
| Telemarketer     |     4 | &#x1f4c8; sell |  3.880 |
| Bottom Feeder    |     5 | &#x2696; law   |  3.880 |
| Ambulance Chaser |     5 | &#x2696; law   |  3.863 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  3.680 |
| Back Stabber     |     5 | &#x2696; law   |  3.545 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  3.530 |
| Pencil Pusher    |     4 | &#x1f454; boss |  3.525 |
| Bloodsucker      |     4 | &#x2696; law   |  3.400 |
| Bean Counter     |     4 | &#x1f4b2; cash |  3.400 |
| Short Change     |     4 | &#x1f4b2; cash |  3.385 |
| Name Dropper     |     3 | &#x1f4c8; sell |  3.310 |
| Cold Caller      |     4 | &#x1f4c8; sell |  3.255 |
| Telemarketer     |     3 | &#x1f4c8; sell |  3.157 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  3.150 |
| Downsizer        |     5 | &#x1f454; boss |  3.125 |
| Yesman           |     6 | &#x1f454; boss |  3.078 |
| Flunky           |     4 | &#x1f454; boss |  2.955 |
| Micromanager     |     5 | &#x1f454; boss |  2.955 |
| Bottom Feeder    |     4 | &#x2696; law   |  2.910 |
| Ambulance Chaser |     4 | &#x2696; law   |  2.775 |
| Pencil Pusher    |     3 | &#x1f454; boss |  2.700 |
| Glad Hander      |     4 | &#x1f4c8; sell |  2.675 |
| Tightwad         |     4 | &#x1f4b2; cash |  2.670 |
| Short Change     |     3 | &#x1f4b2; cash |  2.582 |
| Glad Hander      |     5 | &#x1f4c8; sell |  2.560 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  2.488 |
| Yesman           |     5 | &#x1f454; boss |  2.473 |
| Cold Caller      |     3 | &#x1f4c8; sell |  2.423 |
| Bloodsucker      |     3 | &#x2696; law   |  2.410 |
| Tightwad         |     3 | &#x1f4b2; cash |  2.385 |
| Double Talker    |     4 | &#x2696; law   |  2.280 |
| Flunky           |     3 | &#x1f454; boss |  2.240 |
| Bottom Feeder    |     3 | &#x2696; law   |  2.225 |
| Telemarketer     |     2 | &#x1f4c8; sell |  2.138 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  1.825 |
| Micromanager     |     4 | &#x1f454; boss |  1.775 |
| Pencil Pusher    |     2 | &#x1f454; boss |  1.762 |
| Cold Caller      |     2 | &#x1f4c8; sell |  1.703 |
| Short Change     |     2 | &#x1f4b2; cash |  1.685 |
| Double Talker    |     3 | &#x2696; law   |  1.575 |
| Yesman           |     4 | &#x1f454; boss |  1.555 |
| Bloodsucker      |     2 | &#x2696; law   |  1.520 |
| Bottom Feeder    |     2 | &#x2696; law   |  1.450 |
| Short Change     |     1 | &#x1f4b2; cash |  1.423 |
| Cold Caller      |     1 | &#x1f4c8; sell |  1.345 |
| Yesman           |     3 | &#x1f454; boss |  1.275 |
| Flunky           |     2 | &#x1f454; boss |  1.255 |
| Flunky           |     1 | &#x1f454; boss |  1.050 |
| Bottom Feeder    |     1 | &#x2696; law   |  0.910 |

#### 2 toons, expected damage to given single toon

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 14.250 |
| Big Wig          |    12 | &#x2696; law   | 12.325 |
| Robber Baron     |    12 | &#x1f4b2; cash | 12.000 |
| The Mingler      |    11 | &#x1f4c8; sell | 11.850 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 11.475 |
| Spin Doctor      |    10 | &#x2696; law   | 10.975 |
| Big Wig          |    11 | &#x2696; law   | 10.787 |
| Robber Baron     |    11 | &#x1f4b2; cash | 10.150 |
| Mover & Shaker   |     9 | &#x1f4c8; sell |  9.710 |
| The Mingler      |    10 | &#x1f4c8; sell |  9.542 |
| Spin Doctor      |     9 | &#x2696; law   |  9.431 |
| Back Stabber     |     9 | &#x2696; law   |  9.203 |
| Big Wig          |    10 | &#x2696; law   |  9.137 |
| Legal Eagle      |    11 | &#x2696; law   |  9.079 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell |  8.600 |
| Big Cheese       |    12 | &#x1f454; boss |  8.545 |
| Loan Shark       |    11 | &#x1f4b2; cash |  8.362 |
| Robber Baron     |    10 | &#x1f4b2; cash |  8.225 |
| Corporate Raider |    11 | &#x1f454; boss |  7.882 |
| Mover & Shaker   |     8 | &#x1f4c8; sell |  7.842 |
| The Mingler      |     9 | &#x1f4c8; sell |  7.635 |
| Big Wig          |     9 | &#x2696; law   |  7.588 |
| Spin Doctor      |     8 | &#x2696; law   |  7.350 |
| Legal Eagle      |    10 | &#x2696; law   |  7.304 |
| Back Stabber     |     8 | &#x2696; law   |  7.181 |
| Head Hunter      |    10 | &#x1f454; boss |  7.151 |
| Big Cheese       |    11 | &#x1f454; boss |  7.043 |
| Loan Shark       |    10 | &#x1f4b2; cash |  6.722 |
| Glad Hander      |     8 | &#x1f4c8; sell |  6.647 |
| Robber Baron     |     9 | &#x1f4b2; cash |  6.500 |
| Money Bags       |    10 | &#x1f4b2; cash |  6.435 |
| Corporate Raider |    10 | &#x1f454; boss |  6.412 |
| Bean Counter     |     8 | &#x1f4b2; cash |  6.375 |
| Two-Face         |    10 | &#x1f4c8; sell |  6.353 |
| Big Wig          |     8 | &#x2696; law   |  6.350 |
| Mover & Shaker   |     7 | &#x1f4c8; sell |  6.200 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell |  5.963 |
| The Mingler      |     8 | &#x1f4c8; sell |  5.835 |
| Legal Eagle      |     9 | &#x2696; law   |  5.799 |
| Back Stabber     |     7 | &#x2696; law   |  5.744 |
| Head Hunter      |     9 | &#x1f454; boss |  5.663 |
| Big Cheese       |    10 | &#x1f454; boss |  5.530 |
| Spin Doctor      |     7 | &#x2696; law   |  5.466 |
| Loan Shark       |     9 | &#x1f4b2; cash |  5.422 |
| Name Dropper     |     7 | &#x1f4c8; sell |  5.413 |
| Money Bags       |     9 | &#x1f4b2; cash |  5.359 |
| Two-Face         |     9 | &#x1f4c8; sell |  5.291 |
| Tightwad         |     7 | &#x1f4b2; cash |  5.291 |
| Micromanager     |     8 | &#x1f454; boss |  5.224 |
| Ambulance Chaser |     8 | &#x2696; law   |  5.138 |
| Corporate Raider |     9 | &#x1f454; boss |  5.103 |
| Bean Counter     |     7 | &#x1f4b2; cash |  5.100 |
| Number Cruncher  |     9 | &#x1f4b2; cash |  5.051 |
| Double Talker    |     7 | &#x2696; law   |  5.040 |
| Robber Baron     |     8 | &#x1f4b2; cash |  4.800 |
| Downsizer        |     9 | &#x1f454; boss |  4.638 |
| Mover & Shaker   |     6 | &#x1f4c8; sell |  4.582 |
| Legal Eagle      |     8 | &#x2696; law   |  4.464 |
| Back Stabber     |     6 | &#x2696; law   |  4.446 |
| Head Hunter      |     8 | &#x1f454; boss |  4.400 |
| Tightwad         |     6 | &#x1f4b2; cash |  4.331 |
| Money Bags       |     8 | &#x1f4b2; cash |  4.320 |
| Loan Shark       |     8 | &#x1f4b2; cash |  4.240 |
| Two-Face         |     8 | &#x1f4c8; sell |  4.215 |
| The Mingler      |     7 | &#x1f4c8; sell |  4.157 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell |  4.150 |
| Ambulance Chaser |     7 | &#x2696; law   |  4.144 |
| Big Cheese       |     9 | &#x1f454; boss |  4.143 |
| Number Cruncher  |     8 | &#x1f4b2; cash |  4.095 |
| Spin Doctor      |     6 | &#x2696; law   |  4.075 |
| Glad Hander      |     7 | &#x1f4c8; sell |  4.040 |
| Name Dropper     |     6 | &#x1f4c8; sell |  3.933 |
| Bean Counter     |     6 | &#x1f4b2; cash |  3.825 |
| Corporate Raider |     8 | &#x1f454; boss |  3.817 |
| Micromanager     |     7 | &#x1f454; boss |  3.795 |
| Downsizer        |     8 | &#x1f454; boss |  3.769 |
| Bloodsucker      |     6 | &#x2696; law   |  3.665 |
| Telemarketer     |     6 | &#x1f4c8; sell |  3.461 |
| Pencil Pusher    |     6 | &#x1f454; boss |  3.450 |
| Money Bags       |     7 | &#x1f4b2; cash |  3.381 |
| Double Talker    |     6 | &#x2696; law   |  3.360 |
| Head Hunter      |     7 | &#x1f454; boss |  3.270 |
| Ambulance Chaser |     6 | &#x2696; law   |  3.262 |
| Two-Face         |     7 | &#x1f4c8; sell |  3.254 |
| Legal Eagle      |     7 | &#x2696; law   |  3.234 |
| Penny Pincher    |     6 | &#x1f4b2; cash |  3.225 |
| Number Cruncher  |     7 | &#x1f4b2; cash |  3.219 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  3.155 |
| Yesman           |     7 | &#x1f454; boss |  3.125 |
| Big Cheese       |     8 | &#x1f454; boss |  2.980 |
| Downsizer        |     7 | &#x1f454; boss |  2.973 |
| Loan Shark       |     7 | &#x1f4b2; cash |  2.970 |
| Corporate Raider |     7 | &#x1f454; boss |  2.737 |
| Back Stabber     |     5 | &#x2696; law   |  2.732 |
| Name Dropper     |     5 | &#x1f4c8; sell |  2.688 |
| Micromanager     |     6 | &#x1f454; boss |  2.576 |
| Bean Counter     |     5 | &#x1f4b2; cash |  2.550 |
| Telemarketer     |     5 | &#x1f4c8; sell |  2.520 |
| Pencil Pusher    |     5 | &#x1f454; boss |  2.475 |
| Bloodsucker      |     5 | &#x2696; law   |  2.445 |
| Money Bags       |     6 | &#x1f4b2; cash |  2.430 |
| Short Change     |     5 | &#x1f4b2; cash |  2.411 |
| Head Hunter      |     6 | &#x1f454; boss |  2.373 |
| Tightwad         |     5 | &#x1f4b2; cash |  2.370 |
| Flunky           |     5 | &#x1f454; boss |  2.370 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  2.344 |
| Two-Face         |     6 | &#x1f4c8; sell |  2.333 |
| Ambulance Chaser |     5 | &#x2696; law   |  2.269 |
| Downsizer        |     6 | &#x1f454; boss |  2.217 |
| Name Dropper     |     4 | &#x1f4c8; sell |  2.182 |
| Glad Hander      |     6 | &#x1f4c8; sell |  2.163 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  2.150 |
| Yesman           |     6 | &#x1f454; boss |  2.099 |
| Cold Caller      |     5 | &#x1f4c8; sell |  2.031 |
| Double Talker    |     5 | &#x2696; law   |  1.978 |
| Telemarketer     |     4 | &#x1f4c8; sell |  1.940 |
| Bottom Feeder    |     5 | &#x2696; law   |  1.940 |
| Name Dropper     |     3 | &#x1f4c8; sell |  1.768 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  1.765 |
| Pencil Pusher    |     4 | &#x1f454; boss |  1.762 |
| Bloodsucker      |     4 | &#x2696; law   |  1.700 |
| Bean Counter     |     4 | &#x1f4b2; cash |  1.700 |
| Short Change     |     4 | &#x1f4b2; cash |  1.693 |
| Cold Caller      |     4 | &#x1f4c8; sell |  1.627 |
| Ambulance Chaser |     4 | &#x2696; law   |  1.613 |
| Telemarketer     |     3 | &#x1f4c8; sell |  1.579 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  1.575 |
| Downsizer        |     5 | &#x1f454; boss |  1.562 |
| Yesman           |     5 | &#x1f454; boss |  1.551 |
| Flunky           |     4 | &#x1f454; boss |  1.478 |
| Micromanager     |     5 | &#x1f454; boss |  1.478 |
| Bottom Feeder    |     4 | &#x2696; law   |  1.455 |
| Pencil Pusher    |     3 | &#x1f454; boss |  1.350 |
| Glad Hander      |     4 | &#x1f4c8; sell |  1.337 |
| Tightwad         |     4 | &#x1f4b2; cash |  1.335 |
| Short Change     |     3 | &#x1f4b2; cash |  1.291 |
| Glad Hander      |     5 | &#x1f4c8; sell |  1.280 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  1.244 |
| Cold Caller      |     3 | &#x1f4c8; sell |  1.211 |
| Bloodsucker      |     3 | &#x2696; law   |  1.205 |
| Tightwad         |     3 | &#x1f4b2; cash |  1.192 |
| Double Talker    |     4 | &#x2696; law   |  1.140 |
| Flunky           |     3 | &#x1f454; boss |  1.120 |
| Bottom Feeder    |     3 | &#x2696; law   |  1.113 |
| Telemarketer     |     2 | &#x1f4c8; sell |  1.069 |
| Yesman           |     4 | &#x1f454; boss |  0.927 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  0.913 |
| Micromanager     |     4 | &#x1f454; boss |  0.888 |
| Pencil Pusher    |     2 | &#x1f454; boss |  0.881 |
| Cold Caller      |     2 | &#x1f4c8; sell |  0.851 |
| Short Change     |     2 | &#x1f4b2; cash |  0.843 |
| Double Talker    |     3 | &#x2696; law   |  0.787 |
| Bloodsucker      |     2 | &#x2696; law   |  0.760 |
| Bottom Feeder    |     2 | &#x2696; law   |  0.725 |
| Short Change     |     1 | &#x1f4b2; cash |  0.711 |
| Yesman           |     3 | &#x1f454; boss |  0.688 |
| Cold Caller      |     1 | &#x1f4c8; sell |  0.672 |
| Flunky           |     2 | &#x1f454; boss |  0.627 |
| Flunky           |     1 | &#x1f454; boss |  0.525 |
| Bottom Feeder    |     1 | &#x2696; law   |  0.455 |

#### 3 toons, expected damage to given single toon

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 12.667 |
| Robber Baron     |    12 | &#x1f4b2; cash | 10.800 |
| Big Wig          |    12 | &#x2696; law   | 10.750 |
| The Mingler      |    11 | &#x1f4c8; sell | 10.420 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 10.200 |
| Spin Doctor      |    10 | &#x2696; law   |  9.700 |
| Big Wig          |    11 | &#x2696; law   |  9.442 |
| Robber Baron     |    11 | &#x1f4b2; cash |  9.017 |
| Mover & Shaker   |     9 | &#x1f4c8; sell |  9.013 |
| Spin Doctor      |     9 | &#x2696; law   |  8.348 |
| The Mingler      |    10 | &#x1f4c8; sell |  8.324 |
| Back Stabber     |     9 | &#x2696; law   |  8.295 |
| Big Wig          |    10 | &#x2696; law   |  7.933 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell |  7.608 |
| Robber Baron     |    10 | &#x1f4b2; cash |  7.350 |
| Mover & Shaker   |     8 | &#x1f4c8; sell |  7.305 |
| The Mingler      |     9 | &#x1f4c8; sell |  6.705 |
| Big Wig          |     9 | &#x2696; law   |  6.525 |
| Spin Doctor      |     8 | &#x2696; law   |  6.500 |
| Back Stabber     |     8 | &#x2696; law   |  6.487 |
| Legal Eagle      |    11 | &#x2696; law   |  6.053 |
| Robber Baron     |     9 | &#x1f4b2; cash |  5.850 |
| Mover & Shaker   |     7 | &#x1f4c8; sell |  5.783 |
| Big Cheese       |    12 | &#x1f454; boss |  5.697 |
| Loan Shark       |    11 | &#x1f4b2; cash |  5.575 |
| Big Wig          |     8 | &#x2696; law   |  5.483 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell |  5.275 |
| Corporate Raider |    11 | &#x1f454; boss |  5.255 |
| Back Stabber     |     7 | &#x2696; law   |  5.216 |
| The Mingler      |     8 | &#x1f4c8; sell |  5.188 |
| Legal Eagle      |    10 | &#x2696; law   |  4.869 |
| Spin Doctor      |     7 | &#x2696; law   |  4.827 |
| Head Hunter      |    10 | &#x1f454; boss |  4.768 |
| Big Cheese       |    11 | &#x1f454; boss |  4.695 |
| Loan Shark       |    10 | &#x1f4b2; cash |  4.482 |
| Glad Hander      |     8 | &#x1f4c8; sell |  4.432 |
| Robber Baron     |     8 | &#x1f4b2; cash |  4.300 |
| Money Bags       |    10 | &#x1f4b2; cash |  4.290 |
| Mover & Shaker   |     6 | &#x1f4c8; sell |  4.275 |
| Corporate Raider |    10 | &#x1f454; boss |  4.275 |
| Bean Counter     |     8 | &#x1f4b2; cash |  4.250 |
| Two-Face         |    10 | &#x1f4c8; sell |  4.235 |
| Back Stabber     |     6 | &#x2696; law   |  4.064 |
| Ambulance Chaser |     8 | &#x2696; law   |  3.987 |
| Name Dropper     |     7 | &#x1f4c8; sell |  3.908 |
| Legal Eagle      |     9 | &#x2696; law   |  3.866 |
| Head Hunter      |     9 | &#x1f454; boss |  3.775 |
| Big Cheese       |    10 | &#x1f454; boss |  3.687 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell |  3.683 |
| The Mingler      |     7 | &#x1f4c8; sell |  3.672 |
| Loan Shark       |     9 | &#x1f4b2; cash |  3.615 |
| Spin Doctor      |     6 | &#x2696; law   |  3.577 |
| Money Bags       |     9 | &#x1f4b2; cash |  3.572 |
| Two-Face         |     9 | &#x1f4c8; sell |  3.527 |
| Tightwad         |     7 | &#x1f4b2; cash |  3.527 |
| Micromanager     |     8 | &#x1f454; boss |  3.483 |
| Corporate Raider |     9 | &#x1f454; boss |  3.402 |
| Bean Counter     |     7 | &#x1f4b2; cash |  3.400 |
| Number Cruncher  |     9 | &#x1f4b2; cash |  3.367 |
| Double Talker    |     7 | &#x2696; law   |  3.360 |
| Ambulance Chaser |     7 | &#x2696; law   |  3.212 |
| Downsizer        |     9 | &#x1f454; boss |  3.092 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  2.980 |
| Legal Eagle      |     8 | &#x2696; law   |  2.976 |
| Head Hunter      |     8 | &#x1f454; boss |  2.933 |
| Tightwad         |     6 | &#x1f4b2; cash |  2.888 |
| Money Bags       |     8 | &#x1f4b2; cash |  2.880 |
| Name Dropper     |     6 | &#x1f4c8; sell |  2.847 |
| Loan Shark       |     8 | &#x1f4b2; cash |  2.827 |
| Two-Face         |     8 | &#x1f4c8; sell |  2.810 |
| Big Cheese       |     9 | &#x1f454; boss |  2.762 |
| Number Cruncher  |     8 | &#x1f4b2; cash |  2.730 |
| Glad Hander      |     7 | &#x1f4c8; sell |  2.693 |
| Yesman           |     7 | &#x1f454; boss |  2.683 |
| Bean Counter     |     6 | &#x1f4b2; cash |  2.550 |
| Corporate Raider |     8 | &#x1f454; boss |  2.545 |
| Micromanager     |     7 | &#x1f454; boss |  2.530 |
| Ambulance Chaser |     6 | &#x2696; law   |  2.513 |
| Downsizer        |     8 | &#x1f454; boss |  2.513 |
| Back Stabber     |     5 | &#x2696; law   |  2.462 |
| Bloodsucker      |     6 | &#x2696; law   |  2.443 |
| Telemarketer     |     6 | &#x1f4c8; sell |  2.308 |
| Pencil Pusher    |     6 | &#x1f454; boss |  2.300 |
| Money Bags       |     7 | &#x1f4b2; cash |  2.254 |
| Double Talker    |     6 | &#x2696; law   |  2.240 |
| Head Hunter      |     7 | &#x1f454; boss |  2.180 |
| Two-Face         |     7 | &#x1f4c8; sell |  2.169 |
| Legal Eagle      |     7 | &#x2696; law   |  2.156 |
| Penny Pincher    |     6 | &#x1f4b2; cash |  2.150 |
| Number Cruncher  |     7 | &#x1f4b2; cash |  2.146 |
| Big Cheese       |     8 | &#x1f454; boss |  1.987 |
| Downsizer        |     7 | &#x1f454; boss |  1.982 |
| Loan Shark       |     7 | &#x1f4b2; cash |  1.980 |
| Name Dropper     |     5 | &#x1f4c8; sell |  1.942 |
| Corporate Raider |     7 | &#x1f454; boss |  1.825 |
| Yesman           |     6 | &#x1f454; boss |  1.773 |
| Ambulance Chaser |     5 | &#x2696; law   |  1.737 |
| Micromanager     |     6 | &#x1f454; boss |  1.718 |
| Bean Counter     |     5 | &#x1f4b2; cash |  1.700 |
| Telemarketer     |     5 | &#x1f4c8; sell |  1.680 |
| Pencil Pusher    |     5 | &#x1f454; boss |  1.650 |
| Bloodsucker      |     5 | &#x2696; law   |  1.630 |
| Money Bags       |     6 | &#x1f4b2; cash |  1.620 |
| Short Change     |     5 | &#x1f4b2; cash |  1.607 |
| Head Hunter      |     6 | &#x1f454; boss |  1.582 |
| Tightwad         |     5 | &#x1f4b2; cash |  1.580 |
| Flunky           |     5 | &#x1f454; boss |  1.580 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  1.562 |
| Name Dropper     |     4 | &#x1f4c8; sell |  1.555 |
| Two-Face         |     6 | &#x1f4c8; sell |  1.555 |
| Downsizer        |     6 | &#x1f454; boss |  1.478 |
| Glad Hander      |     6 | &#x1f4c8; sell |  1.442 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  1.433 |
| Cold Caller      |     5 | &#x1f4c8; sell |  1.354 |
| Double Talker    |     5 | &#x2696; law   |  1.318 |
| Telemarketer     |     4 | &#x1f4c8; sell |  1.293 |
| Bottom Feeder    |     5 | &#x2696; law   |  1.293 |
| Name Dropper     |     3 | &#x1f4c8; sell |  1.253 |
| Yesman           |     5 | &#x1f454; boss |  1.244 |
| Ambulance Chaser |     4 | &#x2696; law   |  1.225 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  1.177 |
| Pencil Pusher    |     4 | &#x1f454; boss |  1.175 |
| Bean Counter     |     4 | &#x1f4b2; cash |  1.133 |
| Bloodsucker      |     4 | &#x2696; law   |  1.133 |
| Short Change     |     4 | &#x1f4b2; cash |  1.128 |
| Cold Caller      |     4 | &#x1f4c8; sell |  1.085 |
| Telemarketer     |     3 | &#x1f4c8; sell |  1.052 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  1.050 |
| Downsizer        |     5 | &#x1f454; boss |  1.042 |
| Micromanager     |     5 | &#x1f454; boss |  0.985 |
| Flunky           |     4 | &#x1f454; boss |  0.985 |
| Bottom Feeder    |     4 | &#x2696; law   |  0.970 |
| Pencil Pusher    |     3 | &#x1f454; boss |  0.900 |
| Glad Hander      |     4 | &#x1f4c8; sell |  0.892 |
| Tightwad         |     4 | &#x1f4b2; cash |  0.890 |
| Short Change     |     3 | &#x1f4b2; cash |  0.861 |
| Glad Hander      |     5 | &#x1f4c8; sell |  0.853 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  0.829 |
| Cold Caller      |     3 | &#x1f4c8; sell |  0.807 |
| Bloodsucker      |     3 | &#x2696; law   |  0.803 |
| Tightwad         |     3 | &#x1f4b2; cash |  0.795 |
| Double Talker    |     4 | &#x2696; law   |  0.760 |
| Flunky           |     3 | &#x1f454; boss |  0.747 |
| Bottom Feeder    |     3 | &#x2696; law   |  0.742 |
| Yesman           |     4 | &#x1f454; boss |  0.718 |
| Telemarketer     |     2 | &#x1f4c8; sell |  0.713 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  0.608 |
| Micromanager     |     4 | &#x1f454; boss |  0.592 |
| Pencil Pusher    |     2 | &#x1f454; boss |  0.588 |
| Cold Caller      |     2 | &#x1f4c8; sell |  0.568 |
| Short Change     |     2 | &#x1f4b2; cash |  0.562 |
| Double Talker    |     3 | &#x2696; law   |  0.525 |
| Bloodsucker      |     2 | &#x2696; law   |  0.507 |
| Yesman           |     3 | &#x1f454; boss |  0.492 |
| Bottom Feeder    |     2 | &#x2696; law   |  0.483 |
| Short Change     |     1 | &#x1f4b2; cash |  0.474 |
| Cold Caller      |     1 | &#x1f4c8; sell |  0.448 |
| Flunky           |     2 | &#x1f454; boss |  0.418 |
| Flunky           |     1 | &#x1f454; boss |  0.350 |
| Bottom Feeder    |     1 | &#x2696; law   |  0.303 |

#### 4 toons, expected damage to given single toon

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 11.875 |
| Robber Baron     |    12 | &#x1f4b2; cash | 10.200 |
| Big Wig          |    12 | &#x2696; law   |  9.962 |
| The Mingler      |    11 | &#x1f4c8; sell |  9.705 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell |  9.562 |
| Spin Doctor      |    10 | &#x2696; law   |  9.062 |
| Big Wig          |    11 | &#x2696; law   |  8.769 |
| Mover & Shaker   |     9 | &#x1f4c8; sell |  8.665 |
| Robber Baron     |    11 | &#x1f4b2; cash |  8.450 |
| Back Stabber     |     9 | &#x2696; law   |  7.841 |
| Spin Doctor      |     9 | &#x2696; law   |  7.806 |
| The Mingler      |    10 | &#x1f4c8; sell |  7.715 |
| Big Wig          |    10 | &#x2696; law   |  7.331 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell |  7.112 |
| Mover & Shaker   |     8 | &#x1f4c8; sell |  7.036 |
| Robber Baron     |    10 | &#x1f4b2; cash |  6.912 |
| The Mingler      |     9 | &#x1f4c8; sell |  6.240 |
| Back Stabber     |     8 | &#x2696; law   |  6.141 |
| Spin Doctor      |     8 | &#x2696; law   |  6.075 |
| Big Wig          |     9 | &#x2696; law   |  5.994 |
| Mover & Shaker   |     7 | &#x1f4c8; sell |  5.575 |
| Robber Baron     |     9 | &#x1f4b2; cash |  5.525 |
| Big Wig          |     8 | &#x2696; law   |  5.050 |
| Back Stabber     |     7 | &#x2696; law   |  4.952 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell |  4.931 |
| The Mingler      |     8 | &#x1f4c8; sell |  4.864 |
| Legal Eagle      |    11 | &#x2696; law   |  4.539 |
| Spin Doctor      |     7 | &#x2696; law   |  4.508 |
| Big Cheese       |    12 | &#x1f454; boss |  4.272 |
| Loan Shark       |    11 | &#x1f4b2; cash |  4.181 |
| Mover & Shaker   |     6 | &#x1f4c8; sell |  4.121 |
| Robber Baron     |     8 | &#x1f4b2; cash |  4.050 |
| Corporate Raider |    11 | &#x1f454; boss |  3.941 |
| Back Stabber     |     6 | &#x2696; law   |  3.873 |
| Legal Eagle      |    10 | &#x2696; law   |  3.652 |
| Head Hunter      |    10 | &#x1f454; boss |  3.576 |
| Big Cheese       |    11 | &#x1f454; boss |  3.521 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell |  3.450 |
| The Mingler      |     7 | &#x1f4c8; sell |  3.429 |
| Ambulance Chaser |     8 | &#x2696; law   |  3.413 |
| Loan Shark       |    10 | &#x1f4b2; cash |  3.361 |
| Spin Doctor      |     6 | &#x2696; law   |  3.327 |
| Glad Hander      |     8 | &#x1f4c8; sell |  3.324 |
| Money Bags       |    10 | &#x1f4b2; cash |  3.218 |
| Corporate Raider |    10 | &#x1f454; boss |  3.206 |
| Bean Counter     |     8 | &#x1f4b2; cash |  3.188 |
| Two-Face         |    10 | &#x1f4c8; sell |  3.176 |
| Name Dropper     |     7 | &#x1f4c8; sell |  3.156 |
| Legal Eagle      |     9 | &#x2696; law   |  2.899 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  2.893 |
| Head Hunter      |     9 | &#x1f454; boss |  2.831 |
| Big Cheese       |    10 | &#x1f454; boss |  2.765 |
| Ambulance Chaser |     7 | &#x2696; law   |  2.747 |
| Loan Shark       |     9 | &#x1f4b2; cash |  2.711 |
| Money Bags       |     9 | &#x1f4b2; cash |  2.679 |
| Two-Face         |     9 | &#x1f4c8; sell |  2.646 |
| Tightwad         |     7 | &#x1f4b2; cash |  2.646 |
| Micromanager     |     8 | &#x1f454; boss |  2.612 |
| Corporate Raider |     9 | &#x1f454; boss |  2.551 |
| Bean Counter     |     7 | &#x1f4b2; cash |  2.550 |
| Number Cruncher  |     9 | &#x1f4b2; cash |  2.526 |
| Double Talker    |     7 | &#x2696; law   |  2.520 |
| Yesman           |     7 | &#x1f454; boss |  2.462 |
| Back Stabber     |     5 | &#x2696; law   |  2.326 |
| Downsizer        |     9 | &#x1f454; boss |  2.319 |
| Name Dropper     |     6 | &#x1f4c8; sell |  2.304 |
| Legal Eagle      |     8 | &#x2696; law   |  2.232 |
| Head Hunter      |     8 | &#x1f454; boss |  2.200 |
| Tightwad         |     6 | &#x1f4b2; cash |  2.166 |
| Money Bags       |     8 | &#x1f4b2; cash |  2.160 |
| Ambulance Chaser |     6 | &#x2696; law   |  2.138 |
| Loan Shark       |     8 | &#x1f4b2; cash |  2.120 |
| Two-Face         |     8 | &#x1f4c8; sell |  2.107 |
| Big Cheese       |     9 | &#x1f454; boss |  2.071 |
| Number Cruncher  |     8 | &#x1f4b2; cash |  2.048 |
| Glad Hander      |     7 | &#x1f4c8; sell |  2.020 |
| Bean Counter     |     6 | &#x1f4b2; cash |  1.913 |
| Corporate Raider |     8 | &#x1f454; boss |  1.909 |
| Micromanager     |     7 | &#x1f454; boss |  1.898 |
| Downsizer        |     8 | &#x1f454; boss |  1.884 |
| Bloodsucker      |     6 | &#x2696; law   |  1.833 |
| Telemarketer     |     6 | &#x1f4c8; sell |  1.731 |
| Pencil Pusher    |     6 | &#x1f454; boss |  1.725 |
| Money Bags       |     7 | &#x1f4b2; cash |  1.691 |
| Double Talker    |     6 | &#x2696; law   |  1.680 |
| Head Hunter      |     7 | &#x1f454; boss |  1.635 |
| Two-Face         |     7 | &#x1f4c8; sell |  1.627 |
| Legal Eagle      |     7 | &#x2696; law   |  1.617 |
| Penny Pincher    |     6 | &#x1f4b2; cash |  1.613 |
| Yesman           |     6 | &#x1f454; boss |  1.609 |
| Number Cruncher  |     7 | &#x1f4b2; cash |  1.609 |
| Name Dropper     |     5 | &#x1f4c8; sell |  1.569 |
| Big Cheese       |     8 | &#x1f454; boss |  1.490 |
| Downsizer        |     7 | &#x1f454; boss |  1.486 |
| Loan Shark       |     7 | &#x1f4b2; cash |  1.485 |
| Ambulance Chaser |     5 | &#x2696; law   |  1.472 |
| Corporate Raider |     7 | &#x1f454; boss |  1.369 |
| Micromanager     |     6 | &#x1f454; boss |  1.288 |
| Bean Counter     |     5 | &#x1f4b2; cash |  1.275 |
| Telemarketer     |     5 | &#x1f4c8; sell |  1.260 |
| Name Dropper     |     4 | &#x1f4c8; sell |  1.241 |
| Pencil Pusher    |     5 | &#x1f454; boss |  1.238 |
| Bloodsucker      |     5 | &#x2696; law   |  1.223 |
| Money Bags       |     6 | &#x1f4b2; cash |  1.215 |
| Short Change     |     5 | &#x1f4b2; cash |  1.206 |
| Head Hunter      |     6 | &#x1f454; boss |  1.186 |
| Tightwad         |     5 | &#x1f4b2; cash |  1.185 |
| Flunky           |     5 | &#x1f454; boss |  1.185 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  1.172 |
| Two-Face         |     6 | &#x1f4c8; sell |  1.166 |
| Downsizer        |     6 | &#x1f454; boss |  1.109 |
| Yesman           |     5 | &#x1f454; boss |  1.091 |
| Glad Hander      |     6 | &#x1f4c8; sell |  1.081 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  1.075 |
| Ambulance Chaser |     4 | &#x2696; law   |  1.031 |
| Cold Caller      |     5 | &#x1f4c8; sell |  1.016 |
| Name Dropper     |     3 | &#x1f4c8; sell |  0.996 |
| Double Talker    |     5 | &#x2696; law   |  0.989 |
| Telemarketer     |     4 | &#x1f4c8; sell |  0.970 |
| Bottom Feeder    |     5 | &#x2696; law   |  0.970 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  0.883 |
| Pencil Pusher    |     4 | &#x1f454; boss |  0.881 |
| Bloodsucker      |     4 | &#x2696; law   |  0.850 |
| Bean Counter     |     4 | &#x1f4b2; cash |  0.850 |
| Short Change     |     4 | &#x1f4b2; cash |  0.846 |
| Cold Caller      |     4 | &#x1f4c8; sell |  0.814 |
| Telemarketer     |     3 | &#x1f4c8; sell |  0.789 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  0.787 |
| Downsizer        |     5 | &#x1f454; boss |  0.781 |
| Flunky           |     4 | &#x1f454; boss |  0.739 |
| Micromanager     |     5 | &#x1f454; boss |  0.739 |
| Bottom Feeder    |     4 | &#x2696; law   |  0.727 |
| Pencil Pusher    |     3 | &#x1f454; boss |  0.675 |
| Glad Hander      |     4 | &#x1f4c8; sell |  0.669 |
| Tightwad         |     4 | &#x1f4b2; cash |  0.667 |
| Short Change     |     3 | &#x1f4b2; cash |  0.646 |
| Glad Hander      |     5 | &#x1f4c8; sell |  0.640 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  0.622 |
| Yesman           |     4 | &#x1f454; boss |  0.614 |
| Cold Caller      |     3 | &#x1f4c8; sell |  0.606 |
| Bloodsucker      |     3 | &#x2696; law   |  0.603 |
| Tightwad         |     3 | &#x1f4b2; cash |  0.596 |
| Double Talker    |     4 | &#x2696; law   |  0.570 |
| Flunky           |     3 | &#x1f454; boss |  0.560 |
| Bottom Feeder    |     3 | &#x2696; law   |  0.556 |
| Telemarketer     |     2 | &#x1f4c8; sell |  0.534 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  0.456 |
| Micromanager     |     4 | &#x1f454; boss |  0.444 |
| Pencil Pusher    |     2 | &#x1f454; boss |  0.441 |
| Cold Caller      |     2 | &#x1f4c8; sell |  0.426 |
| Short Change     |     2 | &#x1f4b2; cash |  0.421 |
| Yesman           |     3 | &#x1f454; boss |  0.394 |
| Double Talker    |     3 | &#x2696; law   |  0.394 |
| Bloodsucker      |     2 | &#x2696; law   |  0.380 |
| Bottom Feeder    |     2 | &#x2696; law   |  0.362 |
| Short Change     |     1 | &#x1f4b2; cash |  0.356 |
| Cold Caller      |     1 | &#x1f4c8; sell |  0.336 |
| Flunky           |     2 | &#x1f454; boss |  0.314 |
| Flunky           |     1 | &#x1f454; boss |  0.263 |
| Bottom Feeder    |     1 | &#x2696; law   |  0.227 |

### Maximum damage to given single toon

| Species          | Level | Type           | Damage |
| :--------------- | ----: | :------------- | -----: |
| The Mingler      |    11 | &#x1f4c8; sell | 24.000 |
| Loan Shark       |    11 | &#x1f4b2; cash | 24.000 |
| Corporate Raider |    11 | &#x1f454; boss | 24.000 |
| Legal Eagle      |    11 | &#x2696; law   | 22.000 |
| Big Cheese       |    12 | &#x1f454; boss | 22.000 |
| Mover & Shaker   |     9 | &#x1f4c8; sell | 21.000 |
| The Mingler      |    10 | &#x1f4c8; sell | 21.000 |
| Loan Shark       |    10 | &#x1f4b2; cash | 21.000 |
| Robber Baron     |    12 | &#x1f4b2; cash | 21.000 |
| Big Wig          |    12 | &#x2696; law   | 21.000 |
| Head Hunter      |    10 | &#x1f454; boss | 21.000 |
| Corporate Raider |    10 | &#x1f454; boss | 21.000 |
| Glad Hander      |     8 | &#x1f4c8; sell | 20.000 |
| Mr. Hollywood    |    12 | &#x1f4c8; sell | 20.000 |
| Spin Doctor      |    10 | &#x2696; law   | 20.000 |
| Big Cheese       |    11 | &#x1f454; boss | 20.000 |
| Ambulance Chaser |     8 | &#x2696; law   | 19.000 |
| Legal Eagle      |    10 | &#x2696; law   | 19.000 |
| Big Wig          |    11 | &#x2696; law   | 19.000 |
| Mover & Shaker   |     8 | &#x1f4c8; sell | 18.000 |
| Two-Face         |    10 | &#x1f4c8; sell | 18.000 |
| The Mingler      |     9 | &#x1f4c8; sell | 18.000 |
| Mr. Hollywood    |    11 | &#x1f4c8; sell | 18.000 |
| Tightwad         |     7 | &#x1f4b2; cash | 18.000 |
| Money Bags       |    10 | &#x1f4b2; cash | 18.000 |
| Loan Shark       |     9 | &#x1f4b2; cash | 18.000 |
| Robber Baron     |    11 | &#x1f4b2; cash | 18.000 |
| Double Talker    |     7 | &#x2696; law   | 18.000 |
| Back Stabber     |     9 | &#x2696; law   | 18.000 |
| Spin Doctor      |     9 | &#x2696; law   | 18.000 |
| Micromanager     |     8 | &#x1f454; boss | 18.000 |
| Head Hunter      |     9 | &#x1f454; boss | 18.000 |
| Corporate Raider |     9 | &#x1f454; boss | 18.000 |
| Big Cheese       |    10 | &#x1f454; boss | 18.000 |
| Legal Eagle      |     9 | &#x2696; law   | 17.000 |
| Big Wig          |    10 | &#x2696; law   | 17.000 |
| Two-Face         |     9 | &#x1f4c8; sell | 16.000 |
| Money Bags       |     9 | &#x1f4b2; cash | 16.000 |
| Robber Baron     |    10 | &#x1f4b2; cash | 16.000 |
| Big Cheese       |     9 | &#x1f454; boss | 16.000 |
| Glad Hander      |     7 | &#x1f4c8; sell | 15.000 |
| Mover & Shaker   |     7 | &#x1f4c8; sell | 15.000 |
| The Mingler      |     8 | &#x1f4c8; sell | 15.000 |
| Mr. Hollywood    |    10 | &#x1f4c8; sell | 15.000 |
| Bean Counter     |     8 | &#x1f4b2; cash | 15.000 |
| Number Cruncher  |     9 | &#x1f4b2; cash | 15.000 |
| Loan Shark       |     8 | &#x1f4b2; cash | 15.000 |
| Ambulance Chaser |     7 | &#x2696; law   | 15.000 |
| Back Stabber     |     8 | &#x2696; law   | 15.000 |
| Spin Doctor      |     8 | &#x2696; law   | 15.000 |
| Legal Eagle      |     8 | &#x2696; law   | 15.000 |
| Big Wig          |     9 | &#x2696; law   | 15.000 |
| Micromanager     |     7 | &#x1f454; boss | 15.000 |
| Downsizer        |     9 | &#x1f454; boss | 15.000 |
| Head Hunter      |     8 | &#x1f454; boss | 15.000 |
| Corporate Raider |     8 | &#x1f454; boss | 15.000 |
| Name Dropper     |     7 | &#x1f4c8; sell | 14.000 |
| Two-Face         |     8 | &#x1f4c8; sell | 14.000 |
| Money Bags       |     8 | &#x1f4b2; cash | 14.000 |
| Robber Baron     |     9 | &#x1f4b2; cash | 14.000 |
| Bloodsucker      |     6 | &#x2696; law   | 14.000 |
| Big Cheese       |     8 | &#x1f454; boss | 14.000 |
| Tightwad         |     6 | &#x1f4b2; cash | 13.000 |
| Number Cruncher  |     8 | &#x1f4b2; cash | 13.000 |
| Double Talker    |     6 | &#x2696; law   | 13.000 |
| Back Stabber     |     7 | &#x2696; law   | 13.000 |
| Big Wig          |     8 | &#x2696; law   | 13.000 |
| Downsizer        |     8 | &#x1f454; boss | 13.000 |
| Telemarketer     |     6 | &#x1f4c8; sell | 12.000 |
| Mover & Shaker   |     6 | &#x1f4c8; sell | 12.000 |
| Two-Face         |     7 | &#x1f4c8; sell | 12.000 |
| The Mingler      |     7 | &#x1f4c8; sell | 12.000 |
| Mr. Hollywood    |     9 | &#x1f4c8; sell | 12.000 |
| Penny Pincher    |     6 | &#x1f4b2; cash | 12.000 |
| Bean Counter     |     7 | &#x1f4b2; cash | 12.000 |
| Money Bags       |     7 | &#x1f4b2; cash | 12.000 |
| Loan Shark       |     7 | &#x1f4b2; cash | 12.000 |
| Bloodsucker      |     5 | &#x2696; law   | 12.000 |
| Ambulance Chaser |     6 | &#x2696; law   | 12.000 |
| Spin Doctor      |     7 | &#x2696; law   | 12.000 |
| Legal Eagle      |     7 | &#x2696; law   | 12.000 |
| Pencil Pusher    |     6 | &#x1f454; boss | 12.000 |
| Micromanager     |     6 | &#x1f454; boss | 12.000 |
| Head Hunter      |     7 | &#x1f454; boss | 12.000 |
| Corporate Raider |     7 | &#x1f454; boss | 12.000 |
| Glad Hander      |     6 | &#x1f4c8; sell | 11.000 |
| Short Change     |     5 | &#x1f4b2; cash | 11.000 |
| Number Cruncher  |     7 | &#x1f4b2; cash | 11.000 |
| Robber Baron     |     8 | &#x1f4b2; cash | 11.000 |
| Back Stabber     |     6 | &#x2696; law   | 11.000 |
| Downsizer        |     7 | &#x1f454; boss | 11.000 |
| Cold Caller      |     5 | &#x1f4c8; sell | 10.000 |
| Name Dropper     |     6 | &#x1f4c8; sell | 10.000 |
| Two-Face         |     6 | &#x1f4c8; sell | 10.000 |
| Mr. Hollywood    |     8 | &#x1f4c8; sell | 10.000 |
| Money Bags       |     6 | &#x1f4b2; cash | 10.000 |
| Bottom Feeder    |     5 | &#x2696; law   | 10.000 |
| Bloodsucker      |     4 | &#x2696; law   | 10.000 |
| Spin Doctor      |     6 | &#x2696; law   | 10.000 |
| Pencil Pusher    |     5 | &#x1f454; boss | 10.000 |
| Head Hunter      |     6 | &#x1f454; boss | 10.000 |
| Telemarketer     |     5 | &#x1f4c8; sell |  9.000 |
| Mover & Shaker   |     5 | &#x1f4c8; sell |  9.000 |
| Short Change     |     4 | &#x1f4b2; cash |  9.000 |
| Tightwad         |     5 | &#x1f4b2; cash |  9.000 |
| Bean Counter     |     6 | &#x1f4b2; cash |  9.000 |
| Number Cruncher  |     6 | &#x1f4b2; cash |  9.000 |
| Double Talker    |     5 | &#x2696; law   |  9.000 |
| Downsizer        |     6 | &#x1f454; boss |  9.000 |
| Cold Caller      |     4 | &#x1f4c8; sell |  8.000 |
| Penny Pincher    |     5 | &#x1f4b2; cash |  8.000 |
| Number Cruncher  |     5 | &#x1f4b2; cash |  8.000 |
| Bottom Feeder    |     4 | &#x2696; law   |  8.000 |
| Bloodsucker      |     3 | &#x2696; law   |  8.000 |
| Ambulance Chaser |     5 | &#x2696; law   |  8.000 |
| Back Stabber     |     5 | &#x2696; law   |  8.000 |
| Pencil Pusher    |     4 | &#x1f454; boss |  8.000 |
| Yesman           |     7 | &#x1f454; boss |  8.000 |
| Micromanager     |     5 | &#x1f454; boss |  8.000 |
| Downsizer        |     5 | &#x1f454; boss |  8.000 |
| Telemarketer     |     4 | &#x1f4c8; sell |  7.000 |
| Name Dropper     |     5 | &#x1f4c8; sell |  7.000 |
| Glad Hander      |     5 | &#x1f4c8; sell |  7.000 |
| Short Change     |     3 | &#x1f4b2; cash |  7.000 |
| Flunky           |     5 | &#x1f454; boss |  7.000 |
| Yesman           |     6 | &#x1f454; boss |  7.000 |
| Cold Caller      |     3 | &#x1f4c8; sell |  6.000 |
| Telemarketer     |     3 | &#x1f4c8; sell |  6.000 |
| Name Dropper     |     4 | &#x1f4c8; sell |  6.000 |
| Penny Pincher    |     4 | &#x1f4b2; cash |  6.000 |
| Tightwad         |     4 | &#x1f4b2; cash |  6.000 |
| Bean Counter     |     5 | &#x1f4b2; cash |  6.000 |
| Bottom Feeder    |     3 | &#x2696; law   |  6.000 |
| Bloodsucker      |     2 | &#x2696; law   |  6.000 |
| Double Talker    |     3 | &#x2696; law   |  6.000 |
| Double Talker    |     4 | &#x2696; law   |  6.000 |
| Ambulance Chaser |     4 | &#x2696; law   |  6.000 |
| Flunky           |     4 | &#x1f454; boss |  6.000 |
| Pencil Pusher    |     3 | &#x1f454; boss |  6.000 |
| Yesman           |     5 | &#x1f454; boss |  6.000 |
| Micromanager     |     4 | &#x1f454; boss |  6.000 |
| Name Dropper     |     3 | &#x1f4c8; sell |  5.000 |
| Glad Hander      |     4 | &#x1f4c8; sell |  5.000 |
| Short Change     |     2 | &#x1f4b2; cash |  5.000 |
| Penny Pincher    |     3 | &#x1f4b2; cash |  5.000 |
| Tightwad         |     3 | &#x1f4b2; cash |  5.000 |
| Flunky           |     3 | &#x1f454; boss |  5.000 |
| Yesman           |     4 | &#x1f454; boss |  5.000 |
| Cold Caller      |     2 | &#x1f4c8; sell |  4.000 |
| Telemarketer     |     2 | &#x1f4c8; sell |  4.000 |
| Penny Pincher    |     2 | &#x1f4b2; cash |  4.000 |
| Bean Counter     |     4 | &#x1f4b2; cash |  4.000 |
| Bottom Feeder    |     2 | &#x2696; law   |  4.000 |
| Flunky           |     2 | &#x1f454; boss |  4.000 |
| Pencil Pusher    |     2 | &#x1f454; boss |  4.000 |
| Yesman           |     3 | &#x1f454; boss |  4.000 |
| Cold Caller      |     1 | &#x1f4c8; sell |  3.000 |
| Short Change     |     1 | &#x1f4b2; cash |  3.000 |
| Bottom Feeder    |     1 | &#x2696; law   |  3.000 |
| Flunky           |     1 | &#x1f454; boss |  3.000 |

[discrete]: https://en.wikipedia.org/wiki/Discrete_probability_distribution#Discrete_probability_distribution
[outcome]: https://en.wikipedia.org/wiki/Outcome_(probability)
[continuous]: https://en.wikipedia.org/wiki/Discrete_probability_distribution#Continuous_probability_distribution
[ring]: https://en.wikipedia.org/wiki/Ring_(mathematics)
[headings]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements
[pull-request]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests
[defect-tracker]: https://en.wikipedia.org/wiki/Bug_tracking_system
[suitbattleglobals]: https://github.com/open-toontown/open-toontown/blob/develop/toontown/battle/SuitBattleGlobals.py
