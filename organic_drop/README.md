# Notes on organic drop

[![CC BY-SA 4.0+](https://i.creativecommons.org/l/by-sa/4.0/88x31.png
"CC BY-SA 4.0+")](https://creativecommons.org/licenses/by-sa/4.0/)

TTR only allows for a single gag track to be organic, so one part of every
toon&rsquo;s loadout (besides which gag track(s) they actually have access to)
is what track they choose to plant. Typically the choice is between sound and
throw. [I talk about planting squirt in another
document](../organic_squirt/README.md) mirroring this one. Lure is a common
choice for those training lure and for those who rely heavily on lure when
playing with others who they don&rsquo;t know (and thus cannot trust to
properly stun for the lure). Trap is also fairly useful and is occasionally
seen, but its usefulness is marginal within &ldquo;normal&rdquo; play; most
organic trap users that I have met say that they mostly just wanted their
railroad to one-shot level 12s (although there are at least three other
regularly useful combos involving organic trap). Organic toonup is vastly
underpowered in normal play, and is thus *exceedingly* rare.

These notes focus on one of the underdogs of the bunch: organic drop. The focus
of this document is *not* to convince the reader to use organic drop, and when
using organic drop, your mileage may vary wildly depending on which gag tracks
you have access to, who you play with, and what cogs in the game you fight the
most. Instead, these are notes (maybe even a kind of guide) based on *my
personal experience* (with all the associated arithmetic included, of course)
using organic drop on soundless toons (one being a two-track uber, and the
other being a four-track nonuber). This is not an exhaustive list of every
possible way of defeating any given level of cog using at least one organic
drop gag; this is a practical guide that does deal with discrete strategies,
but only ones that *make practical sense* within playstyles that I have
personally encountered. Plenty of possibly viable strategies are indeed
*intentionally omitted* here.

These notes are split into two parts: a short preliminary/introduction,
followed by a collection of notes on strategies that can be used with organic
drop. Unlike the [notes on organic squirt](../organic_squirt/README.md), I
won&rsquo;t duplicate the &ldquo;Why organic squirt?&rdquo; essay here with all
occurences of &ldquo;squirt&rdquo; changed to &ldquo;drop&rdquo;. Go [read
that](../organic_squirt/README.md#why-organic-squirt) instead.

The strategies covered here are roughly divided up into three kinds: pure,
mixed, and situational. &ldquo;Pure&rdquo; strategies are straightforward and
only involve drop gags. &ldquo;Mixed&rdquo; strategies are only slightly less
straightforward, and involve at least one gag track that isn&rsquo;t drop.
&ldquo;Situational&rdquo; strategies are not quite so straightforward, and are
situational in the sense that they generally span multiple rounds (thus only
making sense within certain cog fights, not just against certain individual
cogs) and/or require special preparation. Within each of the three kinds,
strategies are not in order of &ldquo;usefulness&rdquo; or anything like that,
but are merely ordered by the following, in descending order of priority:

1. Strategies that involve one or more v2.0 cogs are ordered first;
2. Strategies are ordered by the highest level of cog that is involved,
   descending;
3. Strategies that do not involve lure are ordered first;
4. Strategies that involve fewer organic gags are ordered first.

Tie-breaking after this is arbitrary. This ordering is supposed to reflect
something like (very roughly) &ldquo;higher raw gag damage comes first&rdquo;.

## Preliminary

### Key

The percentage in square brackets to the right of each strategy name is the
probability of every part of the strategy hitting (and thus defeating) the cog.
This probability assumes that the lure has already hit (and thus effectively
has 100% accuracy), unless the strategy involves trap, in which case it is
assumed that the lure is as accurate as a non-organic Hypno Goggles
(equivalently, non-organic $10 Bill, organic Blue Magnet, or organic $5 Bill).

One or more of the following indicators appear to the right of the accuracy
percentage:

* &#x2693;, &#x2693;&#x2693;, &#x2693;&#x2693;&#x2693;,
  &#x2693;&#x2693;&#x2693;&#x2693; : Requires 1, 2, 3, or 4 toons with organic
  drop, respectively.
* &#x1f9f2; : Requires lure.
* &#x1f333; : Requires one or more organic gag(s) that are not drop.
* &#x1f35e; : Particularly commonly used (in my personal experience).

### Basic drop knowledge

The damage values of drop gags (and their organic versions) are listed below:

| Level | Name        | Damage | Damage (organic) |
| ----: | :---------- | -----: | ---------------: |
| 1     | Flowerpot   | 10     | 11               |
| 2     | Sandbag     | 18     | 19               |
| 3     | Anvil       | 30     | 33               |
| 4     | Big Weight  | 45     | 49               |
| 5     | Safe        | 60     | 66               |
| 6     | Grand Piano | 170    | 187              |
| 7     | Toontanic   | 180    | 198              |

Drop gags have `propAcc` values of 50 each, meaning that they are effectively
the least accurate gags in the game. Assuming max drop, drop gags have 95%
(i.e. maximum) accuracy on the following cogs (note that the &ldquo;\# of
stuns&rdquo; on the cog is internally represented &mdash; after being
multiplied by 20 &mdash; as `prevHits`, which is a misleading name):

| Cog level                                                  | \# of stuns |
| ---------------------------------------------------------: | ----------: |
| 1&nbsp;&le;&nbsp;`lvl`&nbsp;&le;&nbsp;4                    | &ge;0       |
| 5<sup>&dagger;</sup>&nbsp;&le;&nbsp;`lvl`&nbsp;&le;&nbsp;8 | &ge;1       |
| 9&nbsp;&le;&nbsp;`lvl`&nbsp;&le;&nbsp;12                   | &ge;2       |

&dagger;: This does not apply to level 5 cogs that are tier 1 (Cold Callers,
Short Changes, Bottom Feeders, and Flunkies); drop has 95% accuracy on these
cogs regardless of the number of stuns.

Mentioning stunning here is particularly crucial, as the misunderstanding of
how stunning works is probably the main reason that organic drop (and drop in
general!) is so often neglected. Each stun adds 20 percentage points (up to a
maximum of 95 such points) to the accuracy (hit probability) of any gag that is
used later in the same round and on the same cog(s), but that is not of the
same track as the gag doing the stunning. Gags (and doodles) that fail (read:
miss) are incapable of stunning. Contrary to popular belief, all of the
following gag tracks **do** stun:

* Toonup stuns for gags that are used by the beneficiaries of the healing,
  *regardless of whether or not any given beneficiary had all of their laff
  before the toonup was attempted*. This is with the caveat that, in order for
  a toonup gag to stun for another gag, the toonup gag **and/or** the gag being
  stunned for must be multi-target. This means that Bamboo Canes, in
  particular, are very valuable for stunning.
* Trap. Most players know that trap stuns for lure (so long as they are used in
  the same round, and overlap in the set of cogs that they target, of course).
  But it also stuns for sound, throw, squirt, and drop, as well (although
  stunning for sound and/or squirt is not useful, assuming that all gag tracks
  are maxed).
* Lure. This is really only relevant for drop gags: in the case that a cog is
  lured, knocked back (via trap, sound, throw, or squirt), and dropped on, all
  in the same round, the drop can benefit from the stun that the lure provides.
* Sound. This seems to be well-known.
* Throw. This also seems to be well-known, albeit less so than when it comes to
  sound and squirt.
* Squirt. This seems to be well-known.

Also note that doodles stun similarly to the way that toonup gags stun, and
fires (pink slips) stun for all multi-target gags (but fires cannot stun for
any single-target gags, for obvious reasons).

## Pure strategies

Note that pure strategies are typically used in conjunction with one or more
stuns (and in these cases are thus, in some sense, actually mixed). For this
reason, the accuracy values here can be a bit misleading.

### P0 [55%] &#x2693;

**1 organic Big Weight** and **2 non-organic Safes** takes out an **unlured
level 12** cog.

#### The math

```python
  49 + 60 + 60 + ceil((49 + 60 + 60) / 5)
= 169          + ceil(169            / 5)
= 169          + 34
= 203
```

#### When

In a lureless context where you just want to toonup and take out a level 12.

#### Comments

Assuming that you do stun with toonup, this has an effective accuracy of 74%.
Not quite 75%, since the toonup only has a 95% chance of success.

### P1 [60%] &#x2693;&#x2693; &#x1f35e;

**2 organic Safes** takes out an **unlured level 11** cog.

#### The math

```python
  66 + 66 + ceil((66 + 66) / 5)
= 132     + ceil(132       / 5)
= 132     + 27
= 159
```

#### When

This is a pretty bread-and-butter combo any time that there are two or more
toons with organic drop in your fight. Here are some slight variations:

* **1 non-organic Cream Pie**, **1 non-organic Birthday Cake** (or the
  equivalent of these two gags, like 1 non-organic Fruit Pie and 1 organic
  Birthday Cake), and **2 organic Safes** takes out an **unlured level 11
  v2.0** cog.
* **1 non-organic TNT** (or equivalent, like 1 organic Birthday Cake, or 1
  non-organic Storm Cloud and 1 non-organic Squirtgun) and **2 organic Safes**
  takes out a **lured level 11 v2.0** cog.

### P2 [65%] &#x2693; &#x1f35e;

**1 non-organic Big Weight** and **1 organic Safe** takes out an **unlured
level 10** cog.

#### The math

```python
  45 + 66 + ceil((45 + 66) / 5)
= 111     + ceil(111       / 5)
= 111     + 23
= 134
```

#### When

This is essentially a variation on P1, but for level 10 cogs &mdash; and also,
requiring only one organic gag. As a result this is also pretty
bread-and-butter and can be used in many of the same situations. Here are some
slight variations:

* **1 non-organic Fire Hose**, **1 non-organic Storm Cloud**, **1 non-organic
  Big Weight**, and **1 organic Safe** takes out an **unlured level 10 v2.0**
  cog.
* **1 non-organic Birthday Cake** (or equivalent, like [1 organic Storm
  Cloud](../organic_squirt/README.md#p5-100---), or 2 non-organic Cream Pies),
  **1 non-organic Big Weight**, and **1 organic Safe** takes out a **lured
  level 10 v2.0** cog.

### P3 [70%] &#x2693;

**1 non-organic Big Weight** and **1 organic Big Weight** takes out an
**unlured level 9** cog.

#### The math

```python
  45 + 49 + ceil((45 + 49) / 5)
= 94      + ceil(94        / 5)
= 94      + 19
= 113
```

#### When

This is essentially a variation on P2, but for level 9 cogs. Useful in similar
situations. Here are some slight variations:

* **1 organic Birthday Cake** (or equivalent, like 1 non-organic Squirtgun and
  1 non-organic Storm Cloud), **1 non-organic Big Weight**, and **1 organic Big
  Weight** takes out an **unlured level 9 v2.0** cog.
* **1 non-organic Storm Cloud** (or equivalent, like 1 non-organic Fruit Pie
  and 1 non-organic Cream Pie, or [2 organic Fire
  Hoses](../organic_squirt/README.md#p7-100---)), **1 non-organic Big Weight**,
  and **1 organic Big Weight** takes out a **lured level 9 v2.0** cog.

## Mixed strategies

### X0 [95%] &#x2693; &#x1f9f2;

**2 non-organic Cream Pies**, **1 organic Safe**, and **1 non-organic Grand
Piano** takes out a **lured level 12 v2.0** cog.

#### The math

```python
# First shell
  40 + 40 + ceil((40 + 40) / 5) + ceil((40 + 40) / 2) + 66
= 80      + ceil(80        / 5) + ceil(80        / 2) + 66
= 80      + 16                  + 40                  + 66
= 202

# Second shell
  170 + ceil((66 + 170) / 5)
= 170 + ceil(236        / 5)
= 170 + 48
= 218
```

#### When

In CEO. Note that this is essentially a variation on X3 that makes clever use
of &ldquo;yellow damage&rdquo; to completely defeat a lured level 12 v2.0 cog
in a single round as efficiently as possible.

#### Comments

Like X3, this is alternatively an organic throw strategy (although the organic
throw version is arguably slightly less efficient): **1 non-organic Cream
Pie**, **1 organic Cream Pie**, **1 non-organic Safe**, and **1 non-organic
Grand Piano** takes out a **lured level 12 v2.0** cog.

### X1 [80%] &#x2693; &#x1f9f2;

**1 non-organic Storm Cloud**, **1 non-organic Big Weight**, **1 non-organic
Safe**, and **1 organic Safe** takes out a **lured level 11 v2.0** cog.

#### The math

```python
# First shell
  80 + ceil(80 / 2) + 45
= 80 + 40           + 45
= 165

# Second shell
  60 + 66 + ceil((45 + 60 + 66) / 5)
= 60 + 66 + ceil(171            / 5)
= 60 + 66 + 35
= 161
```

#### When

This strategy is &mdash; if you&rsquo;re willing to stomach the 80% accuracy
&mdash; optimal in basically any situation in which you can reasonably use it.
This is a variant on the more familiar: **1 non-organic Storm Cloud** and **3
non-organic Safes** takes out a **lured level 11 v2.0** cog. The improvement of
this minor variant is that it saves 1 Safe.

### X2 [90.25%] &#x2693; &#x1f9f2;

**1 non-organic Trapdoor**, **1 organic Big Weight**, and **1 non-organic
Safe** takes out a **lured level 12** cog.

#### The math

```python
  70 + 49 + 60 + ceil((49 + 60) / 5)
= 70 + 49 + 60 + ceil(109       / 5)
= 70 + 49 + 60 + 22
= 201
```

#### When

Because this is just a minor variant on the more familiar: **1 non-organic
Trapdoor** and **2 non-organic Safes** takes out a **lured level 12** cog, this
is useful any time that you would use the no-organic-gags variant. In
particular, this strategy allows stunning for lure when there are level 12
cog(s) present (very important) while still taking out a level 12 cog as
efficiently as possible.

#### Comments

This also doubles as a (ever-so-slightly less efficient) organic trap strategy:
**1 organic Trapdoor**, **1 non-organic Big Weight**, and **1 non-organic
Safe** takes out a **lured level 12** cog.

### X3 [95%] &#x2693; &#x1f9f2;

**2 non-organic Cream Pies** and **1 organic Safe** takes out a **lured level
12** cog.

#### The math

```python
  40 + 40 + ceil((40 + 40) / 5) + ceil((40 + 40) / 2) + 66
= 40 + 40 + ceil(80        / 5) + ceil(80        / 2) + 66
= 40 + 40 + 16                  + 40                  + 66
= 202
```

#### When

The purpose of this strategy is to save a Cream Pie. It does so at the expense
of 5 percentage points of accuracy, which is pretty good, so long as no ubers
are present.

#### Comments

This doubles as an (arguably slightly less efficient) organic throw combo: **1
non-organic Cream Pie**, **1 organic Cream Pie**, and **1 non-organic Safe**
takes out a **lured level 12** cog.

### X4a [75%] &#x2693;&#x2693; &#x1f9f2;

**1 non-organic Fruit Pie** and **2 organic Safes** takes out a **lured level
12** cog.

#### The math

```python
  27 + ceil(27 / 2) + 66 + 66 + ceil((66 + 66) / 5)
= 27 + ceil(27 / 2) + 66 + 66 + ceil(132       / 5)
= 27 + 14           + 66 + 66 + 27
= 200
```

#### When

Depending on the situation, this saves anywhere from 1 to 3 Cream Pies. This is
pretty nice, although you have to be willing to stomach the 75% accuracy
(although it is effectively 94% accuracy, if using a multi-target toonup gag).

Here is a slight variation: **1 non-organic Fire Hose** and **2 organic Safes**
takes out a **lured level 12** cog.

### X4b [75%] &#x2693; &#x1f9f2; &#x1f333;

**1 organic Cream Pie**, **1 non-organic Big Weight**, and **1 organic Safe**
takes out a **lured level 12** cog.

#### The math

```python
  44 + ceil(44 / 2) + 45 + 66 + ceil((45 + 66) / 5)
= 44 + ceil(44 / 2) + 45 + 66 + ceil(111       / 5)
= 44 + 22           + 45 + 66 + 23
= 200
```

#### When

This is a variation on X4a, for cases where you only have one organic drop, but
have at least one organic throw.

### X5 [71.25%] &#x2693; &#x1f35e;

**1 non-organic Aoogah** and **1 organic Grand Piano** takes out an **unlured
level 12** cog.

#### The math

```python
  16 + 187
= 203
```

#### When

Normally, when doing a strategy with one sound gag used to stun (and soften up)
cogs for drop (and possibly also throw and/or squirt) gags, a Foghorn is
necessary in the presence of one or more level 12 cogs. Organic drop fixes this
problem. This is particularly common in CFOs, as well as in other bosses.

### X6 [76%] &#x2693;

**1 non-organic Fruit Pie**, **1 non-organic Birthday Cake**, and **1 organic
Big Weight** takes out an **unlured level 12** cog.

#### The math

```python
  27 + 100 + ceil((27 + 100) / 5) + 49
= 27 + 100 + ceil(127        / 5) + 49
= 27 + 100 + 26                   + 49
= 202
```

#### When

In cases where 3 toons are attacking an unlured level 12 cog, but P0 is not a
great idea (no multi-target toonup is being used), and you have no organic
squirt.

Another possibility here is: **1 non-organic Storm Cloud**, **1 non-organic Big
Weight**, and **1 non-organic Safe**. However, this possibility is a bit less
accurate (71.25% accuracy) and also doesn&rsquo;t help when you are running low
on Storm Clouds. It is, however, a bit more efficient in terms of raw power.

There&rsquo;s also the tried and true **1 non-organic Fruit Pie**, **1
non-organic Cream Pie**, and **1 non-organic Birthday Cake** takes out an
**unlured level 12** cog, but it depends on whether or not the marginally
higher accuracy (80% accuracy) is worth the Cream Pie. Plus, using drop means
that the probability that *anything* hits is higher: 91% &gt; 80%.

### X7 [90.25%] &#x2693;

**2 non-organic Elephant Trunks**, **1 non-organic Safe**, and **1 organic
Safe** takes out an **unlured level 12** cog.

#### The math

```python
  21 + 21 + ceil((21 + 21) / 5) + 60 + 66 + ceil((60 + 66) / 5)
= 21 + 21 + ceil(42        / 5) + 60 + 66 + ceil(126       / 5)
= 21 + 21 + 9                   + 60 + 66 + 26
= 203
```

#### When

Any time that the only cog that you really care about doing considerable damage
to, is a fresh level 12 cog. The canonical example here is the first round of
the first phase of VP.

Here is a very marginal variation that requires two organic drop gags: **1
non-organic Aoogah**, **1 non-organic Elephant Trunk**, and **2 organic Safes**
takes out an **unlured level 12** cog.

### X8 [90.25%] &#x2693; &#x1f333; &#x1f35e;

**1 organic Fire Hose**, **1 non-organic Storm Cloud**, and **1 organic Safe**
takes out an **unlured level 12** cog.

#### The math

```python
  33 + 80 + ceil((33 + 80) / 5) + 66
= 33 + 80 + ceil(113       / 5) + 66
= 33 + 80 + 23                  + 66
= 202
```

#### When

This is typically the optimal way for 3 toons to take out an unlured level 12
cog, given that P0 is a bad option (i.e. no multi-target toonup is being used).
Of course, it does require one organic squirt gag as well as one organic drop
gag.

Another reasonable possibility is **1 non-organic Storm Cloud**, **1
non-organic Big Weight**, and **1 non-organic Safe**. However, this possibility
is significantly less accurate (71.25% accuracy), and doesn&rsquo;t save *all
that much* by saving an organic Fire Hose and using a Big Weight instead.

#### Comments

See [strategy X0b in the notes on organic
squirt](../organic_squirt/README.md#x0b-9025---).

### X9a [80%] &#x2693; &#x1f9f2;

**1 non-organic Fire Hose**, **1 non-organic Big Weight**, and **1 organic Big
Weight** takes out a **lured level 11** cog.

#### The math

```python
  30 + ceil(30 / 2) + 45 + 49 + ceil((45 + 49) / 5)
= 30 + ceil(30 / 2) + 45 + 49 + ceil(94        / 5)
= 30 + 15           + 45 + 49 + 19
= 158
```

#### When

This is just a minor variation of the more mundane: **1 non-organic Seltzer
Bottle**, **1 non-organic Big Weight**, and **1 non-organic Safe** takes out a
**lured level 11** cog. The benefit here is saving a Safe.

Here is a slight variation that is more efficient if you have the organic throw
for it: **1 organic Fruit Pie**, **1 non-organic Big Weight**, and **1 organic
Big Weight** takes out a **lured level 11** cog.

### X9b [80%] &#x2693;&#x2693; &#x1f9f2;

**1 non-organic Fruit Pie** and **2 organic Big Weights** takes out a **lured
level 11** cog.

#### The math

```python
  27 + ceil(27 / 2) + 49 + 49 + ceil((49 + 49) / 5)
= 27 + ceil(27 / 2) + 49 + 49 + ceil(98        / 5)
= 27 + 14           + 49 + 49 + 20
= 159
```

#### When

This is just a variation on X9a that is slightly more efficient, but makes use
of two organic drop gags instead of one.

### X10 [90.25%] &#x2693; &#x1f9f2; &#x1f35e;

**1 non-organic Trapdoor** and **1 organic Safe** takes out a **lured level
10** cog.

#### The math

```python
  70 + 66
= 136
```

#### When

This strategy is quite useful for stunning for lure while also very efficiently
taking out a level 10 cog.

#### Comments

This strategy also doubles as an organic trap strategy: **1 organic Trapdoor**
and **1 non-organic Safe** takes out a **lured level 10** cog.

### X11 [85%] &#x2693; &#x1f9f2; &#x1f333;

**1 organic Cream Pie** and **1 organic Safe** takes out a **lured level 10**
cog.

#### The math

```python
  44 + ceil(44 / 2) + 66
= 44 + 22           + 66
= 132
```

#### When

This saves a cream pie over the usual: **2 non-organic Cream Pies** takes out a
**lured level 10** cog. The caveat is the accuracy, although the accuracy is
typically a non-issue in cases where you are luring the level 10 in the same
round that you use this strategy.

### X12 [85.5%] &#x2693; &#x1f333; &#x1f35e;

**1 organic Cream Pie** and **1 organic Safe** takes out an **unlured level 9**
cog.

#### The math

```python
  44 + 66
= 110
```

#### When

Although this is marginally less efficient w.r.t. raw power in comparison to
P3, this is a great strategy to use in preference to P3 whenever the accuracy
ends up making it more favorable.

### X13 [90%] &#x2693; &#x1f9f2;

**1 non-organic Fire Hose** and **1 organic Safe** takes out a **lured level
9** cog.

#### The math

```python
  30 + ceil(30 / 2) + 66
= 30 + 15           + 66
= 111
```

#### When

The purpose of this strategy is to save a Cream Pie, in preference to the
usual: **1 non-organic Fruit Pie** and **1 non-organic Cream Pie** takes out a
**lured level 9** cog. This strategy has the disadvantage of its accuracy, but
this is basically irrelevant in the case that you are luring the level 9 cog in
the same round that you use this strategy on it.

With organic throw, you get a more efficient (only uses a single level &ge;5
gag) slight variation on this strategy: **1 organic Fruit Pie** and **1 organic
Safe** takes out a **lured level 9** cog.

Also, this strategy doubles as an organic squirt strategy: [**1 organic Fire
Hose** and **1 non-organic Safe** takes out a **lured level 9**
cog](../organic_squirt/README.md#x5-90--). The organic squirt version, however,
unfortunately does not work, [due to a bug in
TTR](../ttr_quirks/README.md#cogs-with-less-than-one-hp-do-not-die).

## Situational strategies

### S0 [60%] &#x2693;&#x2693;

**2 organic Big Weights** and **1 non-organic Safe** leaves an **unlured level
11 v2.0** cog with **124 HP**.

#### The math

```python
# First shell
  49 + 49 + 60
= 158

# Second shell
  ceil((49 + 49 + 60) / 5)
= ceil(158            / 5)
= 32

  156 - 32
= 124
```

#### When

This is just a minor (and rather marginal) variant on: **1 non-organic Big
Weight** and **2 non-organic Safes** leaves an **unlured level 11 v2.0** cog
with **123 HP**. The advantage here is saving a Safe, which is really only an
issue in CEOs (rather than in CGCs, as CGCs give gag restocks).

### S1 [65%] &#x2693;&#x2693; &#x1f35e;

**2 organic Safes** leaves an **unlured level 10 v2.0** cog with **105 HP**.

#### The math

```python
# First shell
  66 + 66
= 132

# Second shell
  ceil((66 + 66) / 5)
= ceil(132       / 5)
= 27

  132 - 27
= 105
```

#### When

This is indeed a variant of S0 that is for level 10 cogs instead of level 11
cogs, but this one is considerably more useful; still, two organic drop gags
are required, but only two gags in total. Here are a few useful variants:

* **2 organic Safes** followed by (in the next round) **2 organic Cream Pies**
  takes out an **unlured level 10 v2.0** cog.
* **2 organic Safes** followed by (in the next round) **1 non-organic Cream
  Pie** and **1 organic Safe** takes out an **unlured level 10 v2.0** cog.
* **2 organic Safes** and **1 non-organic Grand Piano** takes out an **unlured
  level 10 v2.0** cog.
* A humourous variant (<i>caveat emptor</i>: 65% accuracy): **4 organic Safes**
  takes out an **unlured level 10 v2.0** cog.

### S2 [70%] &#x2693;

**1 non-organic Big Weight** and **1 organic Safe** leaves an **unlured level 9
v2.0** cog with **87 HP**.

#### The math

```python
# First shell
  45 + 66
= 111

# Second shell
  ceil((45 + 66) / 5)
= ceil(111       / 5)
= 23

  110 - 23
= 87
```

#### When

This is a variant of S1 for level 9 v2.0 cogs. This one has the advantage of
only needing one organic drop gag, and two gags in total. With just 87 HP
remaining, you can imagine plenty of variants to finish off the second shell of
the cog.
