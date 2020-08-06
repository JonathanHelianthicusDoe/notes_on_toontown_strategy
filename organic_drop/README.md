# Notes on organic drop

![CC BY-SA 4.0+](https://i.creativecommons.org/l/by-sa/4.0/88x31.png
"CC BY-SA 4.0+")

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

## Pure strategies

## Mixed strategies

## Situational strategies
