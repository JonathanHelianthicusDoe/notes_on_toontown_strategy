# PSA: Stun hygiene, or, &ldquo;why does lure keep missing in my FO?&rdquo;

Sometimes gags hit, and sometimes they do not. Most Toontown players already
know that this dynamic has an element of
[randomness](https://en.wikipedia.org/wiki/Pseudorandom_number_generator) to
it; many will be dimly aware of their own ability to influence these random
events; and only very few will understand that &ldquo;stunning&rdquo; &mdash; a
method by which toons may increase their gags&rsquo;
[probability](https://en.wikipedia.org/wiki/Probability) of hitting &mdash; is
a full-fledged [game mechanic](https://en.wikipedia.org/wiki/Game_mechanics)
that can be carefully utilized to optimise for successful cog battles.

## How do I stun?

First, we must consider what kinds of gags we can even &ldquo;stun for&rdquo;
(i\.e. increase the hit-chance of) in the first place. The following kinds of
gags may meaningfully<sup>\[1\]</sup> be the beneficiaries of stunning:

- Lure gags.
- Throw gags.
- Drop gags.

If we want to stun for one of the gags above, we must pick a gag (more
generally, pick an _action_, which may or may not be a gag, as we shall see)
that can stun for it. The action that we use to provide the stunning effect
must satisfy **all** of the following&hellip;:

<details>
<summary>Gory details</summary>

- The stunning action must be picked in the same round as the beneficiary.
- The stunning action must take effect **strictly** prior to the beneficiary. This just means that the stunning action must take effect prior to the beneficiary, and the two actions must not be from the same gag track (e\.g. they cannot both be drop gags/SOSes).
- The stunning action and the beneficiary must overlap; that is:
  - If the stunning action heals toons (e\.g. a toon-up gag): The toon
    performing the beneficiary action must be affected by the stunning action.
  - Otherwise: The [set] of the stunning action&rsquo;s targets (e\.g. in the
    case of a sound gag, this is just &ldquo;the set of all cogs that are
    currently in the battle&rdquo;), and the set of the beneficiary&rsquo;s
    targets, must overlap; that is, their [intersection][intsc] must not be
    [empty](https://en.wikipedia.org/wiki/Empty_set).
- The stunning action must not miss.
  - This applies to toon-up gags as well, despite the fact that toon-up gags
    still have an effect (albeit a greatly reduced one) when they miss.
- If the stunning action heals toons, then the stunning action and the
  beneficiary action must not both be single-target. In other words, one or
  both of the two actions must be multi-target.

</details>

&hellip;TL;DR:

- Stuns don&rsquo;t persist across rounds.
- The stun has to happen before the thing that you&rsquo;re stunning for.
- The stun and the thing that you&rsquo;re stunning for have to overlap
  somehow. Hitting one cog with a fire hose won&rsquo;t stun for a safe
  that&rsquo;s about to be dropped on a different cog, and tooning up Alice
  with a pixie dust won&rsquo;t stun for the big magnet that Bob is about to
  use.
- Gags that miss don&rsquo;t provide any stun. This applies to toon-up gags.
- You can&rsquo;t use a single-target toon-up gag to stun for a single-target
  gag.

## What does a stun do, exactly?

In some cases, a gag is guaranteed to hit (its hit-chance is 100% by
definition); for example, a trap gag, or a throw gag that is used on a lured
cog. In some other cases, a gag is guaranteed to miss (its hit-chance is 0% by
definition); for example, a drop gag that is used on a lured cog.

In all other cases, however, the hit-chance is always **95% at most**, and can
be as low as 0%. Each stun **adds 20 percentage points to the hit-chance**, up
to the 95% limit. For example, a gag that would otherwise have a hit-chance of
50% has a hit-chance of 70% with 1 stun, 90% with 2 stuns, and 95% with 3 or
more stuns.

Notice that the effects of stunning are cumulative (although still subject to
the 95% limit, of course). For example, if you hit a cog with a fire hose
before dropping a grand piano on it, that&rsquo;s 1 stun for the grand piano.
Add another fire hose into the mix, and that&rsquo;s 2 stuns. Add an aoogah on
top, and now you have 3 stuns total. More than 3 stuns for a single gag is not
possible, for the obvious reason that 4 is the maximum number of toons in a
single cog battle.

## What is &ldquo;stun hygiene&rdquo;?

&ldquo;Stun hygiene&rdquo; is a term that I made up to describe the habits of
toons who are aware of how stunning affects their gameplay. If you have good
stun hygiene, this tends to mean the following:

&#x1f4a1; When stunning would increase the hit-chance of a gag (i\.e. it can be
stunned for, and isn&rsquo;t already at 95% hit-chance), **and** you can stun
for that gag whilst losing little or no [tempi][tempo] &mdash; or even whilst
gaining tempi, as is often the case &mdash; then you intentionally stun for
that gag.

A corollary of this would be:

&#x1f4a1; You do not rely on gag choices (especially lure) that have subpar
accuracy, when a change of strategy would give a significantly higher
probability of the strategy actually playing out (i\.e. working as hoped).

If this all sounds a bit nebulous, or perhaps a bit obvious, consider the
following pair of observations:

- When, in a given round of battle, a chosen strategy more or less fails due to
  random chance (i\.e. most or all of the crucial gags miss, e\.g. a lure
  miss), that is a massive loss of _all_ of the following:
  - Tempi; at worst, you lose an entire tempo, and at best you
    &ldquo;only&rdquo; lose the majority of it.
  - Gags (and possibly other disposable resources as well).
  - Laff.
- When a gag has an uncomfortably low hit-chance (which may just mean that it
  has a hit-chance below 95%, or the threshold may be looser), it is high
  likely &mdash; even in general &mdash; that you can do something to fix it.

This seems to imply that we have no choice but to pay close attention to
hit-chances, and use our ability to stun wisely, to avoid &mdash; to the extent
possible &mdash; unnecessary loss. This is what I mean by &ldquo;optimise for
successful cog battles&rdquo;.

### Handy-dandy chart

You _could_ memorise all of the relevant numbers and do accuracy computations
on the fly whilst battling cogs. However, _I_ certainly don&rsquo;t want to do
that, and I doubt that you do either. Instead, it&rsquo;s better to think in
terms of &ldquo;gag combos&rdquo;, as many Toontown players are accustomed to
doing already.

For this reason, I&rsquo;ve compiled a handy-dandy chart that you can read
below, for your cog-fighting needs. Although of course it makes sense to
reference such a chart in the midst of battle, you&rsquo;ll likely find that
you can memorise (or almost-memorise) the important bits that you find
particularly useful in your day-to-day Toontowning.

<details>
<summary>Legend for the chart below</summary>

This chart **assumes that any relevant gag track is maxed**, i\.e. that the
toon using the gag has access to the level 7 gag of the respective gag
track.<sup>\[2\]</sup>

- <b>Level:</b> The **highest** level of all cogs targeted by the gag whose
  accuracy you&rsquo;re concerned about.
- <b>&#x1d45b;%:</b> The number of stuns required to make the hit-chance of the
  gag be at least &#x1d45b;%.
- <b>Magnet:</b> An inorganic big magnet or inorganic $5 bill.
- <b>Hypno:</b> An inorganic hypno-goggles, inorganic $10 bill, organic big
  magnet, or organic $5 bill.
- <b>Org hypno:</b> An organic hypno-goggles or organic $10 bill.

</details>

| level | gag                      | 95% | 90% | 85% |
| ----: | :----------------------- | --: | --: | --: |
|    12 | &#x1f9f2;&nbsp;magnet    |   2 |   2 |   1 |
|    12 | &#x1f453;&nbsp;hypno     |   1 |   1 |   1 |
|    12 | &#x1f97d;&nbsp;org hypno |   1 |   1 |   0 |
|    12 | &#x1f967;&nbsp;throw     |   1 |   1 |   1 |
|    12 | &#x1f3b9;&nbsp;drop      |   2 |   2 |   2 |
|    11 | &#x1f9f2;&nbsp;magnet    |   2 |   1 |   1 |
|    11 | &#x1f453;&nbsp;hypno     |   1 |   1 |   1 |
|    11 | &#x1f97d;&nbsp;org hypno |   1 |   0 |   0 |
|    11 | &#x1f967;&nbsp;throw     |   1 |   1 |   0 |
|    11 | &#x1f3b9;&nbsp;drop      |   2 |   2 |   2 |
|    10 | &#x1f9f2;&nbsp;magnet    |   1 |   1 |   1 |
|    10 | &#x1f453;&nbsp;hypno     |   1 |   1 |   0 |
|    10 | &#x1f967;&nbsp;throw     |   1 |   0 |   0 |
|    10 | &#x1f3b9;&nbsp;drop      |   2 |   2 |   1 |
|     9 | &#x1f9f2;&nbsp;magnet    |   1 |   1 |   1 |
|     9 | &#x1f453;&nbsp;hypno     |   1 |   0 |   0 |
|     9 | &#x1f3b9;&nbsp;drop      |   2 |   1 |   1 |
|     8 | &#x1f9f2;&nbsp;magnet    |   1 |   1 |   0 |
|     8 | &#x1f3b9;&nbsp;drop      |   1 |   1 |   1 |
|     7 | &#x1f9f2;&nbsp;magnet    |   1 |   0 |   0 |
|     7 | &#x1f3b9;&nbsp;drop      |   1 |   1 |   1 |

## Why do I care?

Because the binomial distribution

---

<details>
<summary>Footnotes</summary>

1. Sound &amp; squirt should _theoretically_ be on this list, but their base
   accuracies (`propAcc` values) are too high for it to matter. Thus, this is
   simplified for convenience.
2. Yes, how close you are to maxing a track affects your accuracy with the gags
   in that track! One more reason to max your dang gags!

</details>

[set]: https://en.wikipedia.org/wiki/Set_(mathematics)
[intsc]: https://en.wikipedia.org/wiki/Intersection_(set_theory)
[tempo]: https://en.wikipedia.org/wiki/Tempo_(chess)
