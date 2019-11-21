# Notes on organic squirt

TTR only allows for a single gag track to be organic, so one part of every
toon&rsquo;s loadout (besides what gag tracks they actually have access to) is
what track they choose to plant. Typically the choice is between sound and
throw. Lure is a common choice for those training lure and for those who rely
heavily on lure when playing with others they don&rsquo;t know (and thus cannot
trust to properly stun for the lure). Trap and drop are also fairly useful and
are occasionally seen, but their usefulness is marginal within
&rdquo;normal&ldquo; play; most organic trap users that I have met say that
they mostly just wanted their railroad to one-shot level 12s. Organic toonup is
vastly underpowered in normal play, and is thus **exceedingly** rare.

These notes focus on the (in my opinion) severely underestimated underdog of
the bunch: organic squirt. No attempt is here made to convince the reader to
use organic squirt, and your mileage may vary wildly depending on which gag
tracks you have access to, who you play with, and what cogs in the game you
fight the most. Instead, these are notes (maybe even a kind of guide) based on
**my personal experience** (with all the associated arithmetic included, of
course) using organic squirt on soundless toons (with variously 1, 3, 4, 5, or
6 gag tracks on each toon). This is not an exhaustive list of every possible
way of defeating any given level of cog using at least one organic squirt gag;
this is a practical guide that does deal with discrete strategies, but only
ones that **make practical sense** within playstyles that I have personally
encountered. Plenty of possibly viable strategies are indeed **intentionally
omitted** here.

These notes are split into two parts: a short preliminary/introduction,
followed by a collection of notes on strategies that can be used with organic
squirt. If you already feel pretty comfortable with the game&rsquo;s mechanics
and the jargon that toons tend to use surrounding said mechanics, you can
probably skip the preliminary.

The strategies covered here are roughly divided up into three kinds: pure,
mixed, and situational. &ldquo;Pure&rdquo; strategies are straightforward and
only involve squirt gags (although they may deal with cogs that are lured or
unlured). &ldquo;Mixed&rdquo; strategies are only slightly less
straightforward, and involve at least one gag track that isn&rsquo;t squirt.
&ldquo;Situational&rdquo; strategies are not quite so straightforward, and are
situational in the sense that they generally span multiple rounds (thus only
making sense within certain cog fights, not just against certain individual
cogs) and/or require special preparation.

## Preliminary

The damage values of squirt gags (and their organic versions) are listed below:

| Level | Name             | Damage | Damage (Organic) |
| ----- | ---------------- | ------ | ---------------- |
| 1     | Squirting Flower | 4      | 5                |
| 2     | Glass Of Water   | 8      | 9                |
| 3     | Squirtgun        | 12     | 13               |
| 4     | Seltzer Bottle   | 21     | 23               |
| 5     | Fire Hose        | 30     | 33               |
| 6     | Storm Cloud      | 80     | 88               |
| 7     | Geyser           | 105    | 115              |

Squirt gags are effectively as accurate as sound gags (slightly complicated by
the fact that sound gags hit all cogs, and squirt gags hit one cog at a time
with the exception of the Geyser). Toons with max squirt have a 95% chance of
hitting any unlured cog with their squirt gags, and all toons have a 100%
chance of hitting any lured cog with their squirt gags.

## Pure strategies

### P0

**1 organic Storm Cloud** and **1 non-organic Fire Hose** takes out a **lured
level 12** cog.

#### The math

```python
  88 + 30 + ceil((88 + 30) / 5) + ceil((88 + 30) / 2)
= 118     + ceil(118       / 5) + ceil(118       / 2)
= 118     + ceil(23.6)          + ceil(59)
= 118     + 24                  + 59
= 201
```

### P1

**1 organic Storm Cloud** and **1 non-organic Storm Cloud** takes out an
**unlured level 12** cog.

#### The math

```python
  88 + 80 + ceil((88 + 80) / 5)
= 168     + ceil(168       / 5)
= 168     + ceil(33.6)
= 168     + 34
= 202
```

#### When

Like most non-situational strategies, this one is pretty general, but it tends
to be more useful in lureless situations for the obvious reason that it
doesn&rsquo;t require the cog to be lured.

### P2

**1 organic Fire Hose** and **2 non-organic Fire Hoses** takes out a **lured
level 11** cog.

#### The math

```python
  33 + 30 + 30 + ceil((33 + 30 + 30) / 5) + ceil((33 + 30 + 30) / 2)
= 93           + ceil(93             / 5) + ceil(93             / 2)
= 93           + ceil(18.6)               + ceil(46.5)
= 93           + 19                       + 47
= 159
```

#### When

The main purpose of this strategy is to conserve a single Cream Pie (which does
anywhere from 7 to 14 more damage than a Fire Hose, albeit less accurately),
although obviously it is also quite useful when one or more toon(s) are
throwless.

### P3a

**4 organic Seltzer Bottles** takes out a **lured level 11** cog.

#### The math

```python
  23 * 4 + ceil(23 * 4 / 5) + ceil(23 * 4 / 2)
= 92     + ceil(92     / 5) + ceil(92     / 2)
= 92     + ceil(18.4)       + ceil(46)
= 92     + 19               + 46
= 157
```

#### When

Despite being a pure strategy, this one is pretty highly situational: it
requires that all 4 toons have organic squirt, and is a hyper-conservative
strategy that is mostly useful in situations where gags are scarce. That being
said, in these situations it is incredibly powerful, so it deserves a place in
this document.

### P3b

**4 organic Fire Hoses** takes out an **unlured level 11** cog.

#### The math

```python
  33 * 4 + ceil(33 * 4 / 5)
= 132    + ceil(132    / 5)
= 132    + ceil(26.4)
= 132    + 27
= 159
```

#### When

This is the lureless version of P3a, so the comments that apply to P3a apply
here as well.

### P4

**1 organic Storm Cloud** takes out a **lured level 10** cog.

#### The math

```python
  88 + ceil(88 / 2)
= 88 + ceil(44)
= 88 + 44
= 132
```

#### Comments

This is what people usually think of when they think of organic squirt, because
it is simple, effective, and &mdash; most importantly &mdash; requires no
coordination/teamwork.

### P5

**1 organic Fire Hose** and **2 non-organic Fire Hoses** takes out an **unlured
level 9** cog.

#### The math

```python
  33 + 30 + 30 + ceil((33 + 30 + 30) / 5)
= 93           + ceil(93             / 5)
= 93           + ceil(18.6)
= 93           + 19
= 112
```

#### When

This strategy is similar to P2, as the main purpose of this strategy is to
conserve a single Cream Pie, and it is also quite useful when one or more
toon(s) are throwless. But this strategy differs in that it is mostly *only
useful in a lureless context*.

### P6

**2 organic Fire Hoses** takes out a **lured level 9** cog.

#### The math

```python
  33 + 33 + ceil((33 + 33) / 5) + ceil((33 + 33) / 2)
= 66      + ceil(66        / 5) + ceil(66        / 2)
= 66      + ceil(13.2)          + ceil(33)
= 66      + 14                  + 33
= 113
```

#### When

This strategy is similar to P2, as the main purpose of this strategy is to
conserve a single Cream Pie, and it is also quite useful when one or more
toon(s) are throwless.

### P7

**1 organic Seltzer Bottle** and **2 non-organic Seltzer Bottles** takes out a
**lured level 9** cog.

#### The math

```python
  23 + 21 + 21 + ceil((23 + 21 + 21) / 5) + ceil((23 + 21 + 21) / 2)
= 65           + ceil(65             / 5) + ceil(65             / 2)
= 65           + ceil(13)                 + ceil(32.5)
= 65           + 13                       + 33
= 111
```

#### When

This is a kind of hyper-conservative strategy that is mostly useful in
situations where gags are scarce. Effectively, this strategy can save you up to
3 Fruit Pies by replacing them with Seltzer Bottles, which do anywhere from 4
to 8 less damage (albeit more accurately). Also obviously useful with one or
more throwless toon(s).
