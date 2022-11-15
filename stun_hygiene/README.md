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
gags can meaningfully be the beneficiaries of stunning:

- Lure gags.
- \*Sound gags.
- Throw gags.
- \*Squirt gags.
- Drop gags.

\*These asterisked gags can only benefit from stunning if they are targeting
one or more level &ge;14 cogs.<sup>\[1\]</sup>

If we want to stun for one of the gags above, we must pick a gag (more
generally, pick an _action_, which may or may not be a gag, as we shall see)
that can stun for it. The action that we use to provide the stunning effect
must satisfy **all** of the following&hellip;:

<details>
<summary>Gory details</summary>

- The stunning action must be picked in the same round as the beneficiary.
- The stunning action must take effect **strictly** prior to the beneficiary.
  This just means that the stunning action must take effect prior to the
  beneficiary, and the two actions must not be from the same gag track (e\.g.
  they cannot both be drop gags).
- The stunning action and the beneficiary must overlap; that is:
  - If the stunning action heals<sup>\[2\]</sup> toons (e\.g. a toon-up gag):
    The toon performing the beneficiary action must be affected by the stunning
    action.
  - Otherwise: The [set] of the stunning action&rsquo;s targets (e\.g. in the
    case of a sound gag, this is just &ldquo;the set of all cogs that are
    currently in the battle&rdquo;), and the set of the beneficiary&rsquo;s
    targets, must overlap; that is, their [intersection][intsc] must not be
    [empty](https://en.wikipedia.org/wiki/Empty_set).
- The stunning action must not miss.
  - This applies to toon-up gags as well, despite the fact that toon-up gags
    still have an effect (albeit a greatly reduced one) when they miss.
- If the stunning action heals<sup>\[2\]</sup> toons, then the stunning action
  and the beneficiary action must not both be single-target. In other words,
  one or both of the two actions must be multi-target.

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

### What can I stun with?

- <b>Fires</b>. This might seem a little weird because a fire removes the cog
  from battle, but it _does_ stun for multi-target gags.
- <b>Toons hit</b> SOS. TTR changed toons hit SOS mechanics in v3\.0\.0, so
  that they now operate basically like stuns, except that they add **75**
  percentage points, not 20, as per the in-game description. Naturally, these
  don&rsquo;t work _quite_ like stuns; instead, they are buffs that apply to
  toons and persist for multiple rounds. An active toons hit buff is worth
  effectively 75&nbsp;&div;&nbsp;20&nbsp;=&nbsp;3\.75 stuns (still subject to
  the 95% hit-chance cap, of course&hellip;).
- <b>Doodles</b>. Works similarly to a multi-target toon-up gag.
- <b>Toon-up</b> gags (including SOSes). Note that **the toon-up does not have
  to give any laff**; it merely has to &ldquo;hit&rdquo; (rather than miss).
  Thus, in some situations &mdash; indeed, in _many_ more situations than you
  likely realize &mdash; it makes _very_ good sense to toon-up even when
  everyone else is already at full laff.
- <b>Trap</b> gags (including SOSes<sup>\[3\]</sup>). Trap gags are unique in
  that they do not have to be activated (by lure) to stun; rather, the simple
  act of placing a trap gag counts as an attack on that cog(s) for the purpose
  of stunning. Although placed trap gags do persist for multiple rounds when
  not otherwise disposed of, I don&rsquo;t believe(?) that they provide a stun
  on rounds within which they weren&rsquo;t actively placed.
- <b>Lure</b> gags (including SOSes).
- <b>Sound</b> gags (including SOSes).
- <b>Throw</b> gags (including SOSes).
- <b>Squirt</b> gags (including SOSes).

<sup>\[4\]</sup>

Gag restock SOSes do _not_ stun, and neither do cogs miss SOSes.

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

It&rsquo;s worth noting that stunning is not the only factor here; other
aspects of gag choice, _particularly backup (&ldquo;insurance&rdquo;) gags_,
are also prominent. However, this is not a PSA about insurance gags (although
maybe it should be&hellip;).

### Handy-dandy chart

You _could_ memorise all of the relevant numbers and do accuracy computations
on the fly whilst battling cogs. However, _I_ certainly don&rsquo;t want to do
that, and I doubt that you do either. Instead, it&rsquo;s better to think in
terms of &ldquo;gag combos&rdquo;, as many Toontown players are accustomed to
doing already.

For this reason, I&rsquo;ve compiled a handy-dandy chart that you can read
below, for your cog-fighting needs. Although of course it makes sense to
reference such a chart in the midst of battle, you&rsquo;ll likely find that
you can memorise (or almost-memorise) many of the important bits that you find
particularly useful in your day-to-day Toontowning.

When consulting the chart, you should have in mind both the highest level of
cog that you&rsquo;re targeting, and also the desired threshold of certainty
that the gag will hit.

<details>
<summary>Legend for the chart below</summary>

Cogs above level 14 are not included, both for brevity, and also because they
don&rsquo;t show up very often &mdash; and when they do, you are usually at the
Boiler fight, where you&rsquo;re probably using remotes and fires and so
on&hellip; Sound &amp; squirt are also omitted because you only need to know
that they can be stunned for if the cog is level 14 or higher.

This chart **assumes that any relevant gag track is maxed**, i\.e. that the
toon using the gag has access to the level 7 gag of the respective gag
track.<sup>\[5\]</sup>

- <b>Level:</b> The **highest** level of all cogs targeted by the gag whose
  accuracy you&rsquo;re concerned about.
- <b>&#x1d45b;%:</b> The number of stuns required to make the hit-chance of the
  gag be at least &#x1d45b;%.
- <b>Magnet:</b> An inorganic big magnet or inorganic $5 bill.
- <b>Hypno:</b> An inorganic hypno-goggles, inorganic $10 bill, organic big
  magnet, or organic $5 bill.
- <b>Org hypno:</b> An organic hypno-goggles or organic $10 bill.

</details>

#### &#x1f4b8;&nbsp;Lure

| level | gag                      | 95% | 90% | 85% |
| ----: | :----------------------- | --: | --: | --: |
|    14 | &#x1f9f2;&nbsp;magnet    |   2 |   2 |   2 |
|    14 | &#x1f453;&nbsp;hypno     |   2 |   2 |   1 |
|    14 | &#x1f97d;&nbsp;org hypno |   1 |   1 |   1 |
|    13 | &#x1f9f2;&nbsp;magnet    |   2 |   2 |   2 |
|    13 | &#x1f453;&nbsp;hypno     |   2 |   1 |   1 |
|    13 | &#x1f97d;&nbsp;org hypno |   1 |   1 |   1 |
|    12 | &#x1f9f2;&nbsp;magnet    |   2 |   2 |   1 |
|    12 | &#x1f453;&nbsp;hypno     |   1 |   1 |   1 |
|    12 | &#x1f97d;&nbsp;org hypno |   1 |   1 |   0 |
|    11 | &#x1f9f2;&nbsp;magnet    |   2 |   1 |   1 |
|    11 | &#x1f453;&nbsp;hypno     |   1 |   1 |   1 |
|    11 | &#x1f97d;&nbsp;org hypno |   1 |   0 |   0 |
|    10 | &#x1f9f2;&nbsp;magnet    |   1 |   1 |   1 |
|    10 | &#x1f453;&nbsp;hypno     |   1 |   1 |   0 |
|     9 | &#x1f9f2;&nbsp;magnet    |   1 |   1 |   1 |
|     9 | &#x1f453;&nbsp;hypno     |   1 |   0 |   0 |
|     8 | &#x1f9f2;&nbsp;magnet    |   1 |   1 |   0 |
|     7 | &#x1f9f2;&nbsp;magnet    |   1 |   0 |   0 |

#### &#x1f3b9;&nbsp;Drop

| level | 95% | 90% | 85% |
| ----: | --: | --: | --: |
|    14 |   3 |   3 |   2 |
|    13 |   3 |   2 |   2 |
|    12 |   2 |   2 |   2 |
|    11 |   2 |   2 |   2 |
|    10 |   2 |   2 |   1 |
|     9 |   2 |   1 |   1 |
|     8 |   1 |   1 |   1 |
|     7 |   1 |   1 |   1 |

#### &#x1f967;&nbsp;Throw

| level | 95% | 90% | 85% |
| ----: | --: | --: | --: |
|    14 |   2 |   1 |   1 |
|    13 |   1 |   1 |   1 |
|    12 |   1 |   1 |   1 |
|    11 |   1 |   1 |   0 |
|    10 |   1 |   0 |   0 |

## Why do I care?

If you have this question, you will probably benefit from re-reading the
&ldquo;What is &lsquo;stun hygiene&rsquo;?&rdquo; section above. Nevertheless,
if you are _still_ curious, it&rsquo;s worth doing a brief dive into the
mathematics at play here.

The reality is that the probability of just a single gag hitting isn&rsquo;t
all that we&rsquo;re concerned about. This should be obvious: over the course
of a cog fight, a cog building, a cog facility, a boss run, a field office, or
what have you, you &amp; your teammates will be using _many_ gags in your
efforts to succeed. We can conceptually treat these many gags (or more
generally, many disposable resources) as lying along two dimensions:

- <b>Intra-temporal:</b> The gags that are used within a _single_ round of
  battle.
- <b>Inter-temporal:</b> Gags as they are used across _many_ rounds of battle
  &mdash; usually, the gags that are used in the interval between two
  consecutive trips to the gag shoppe (read: a single facility).

In the intra-temporal case, we have the strategy of gag-picking. You know the
drill: there are (probably) four of you, and you have roughly half a minute to
all pick what gags you&rsquo;re gonna use this round. Assuming that you
collectively decide on something appealing, it now remains to be seen whether
or not
[RNG](https://en.wikipedia.org/wiki/Pseudorandom_number_generator)[sus](https://en.wikipedia.org/wiki/Portmanteau)
will let you have your way. Frequently, you need all (or almost all) of the
gags that can _possibly_ miss, to hit, in order for your strategy to actually
play out as intended.

This brings us to our good friend, the
[binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution).
Of course the binomial distribution is only illustrative here &mdash; a decent
approximation at best &mdash; because the various gags may have various
different hit-chances, whereas there is only one value of &#x1d45d; in a given
binomial distribution. Nevertheless, it&rsquo;s illustrative to note that in
the extreme case, wherein all &#x1d45b; of your trials succeed, the probability
of such an extreme outcome becomes simply &#x1d45d;<sup>&#x1d458;</sup>, where
&#x1d458; is the number of successes (in this extreme case,
&#x1d458;&nbsp;=&nbsp;&#x1d45b;). This value (&#x1d45d;<sup>&#x1d458;</sup>)
naturally goes sour (read: towards zero) _very quickly_ as &#x1d458; gets much
higher than&hellip; well&hellip; 1, basically. This is because
[exponentials](https://en.wikipedia.org/wiki/Exponentiation) are
[scary](https://en.wikipedia.org/wiki/Cobham%27s_thesis). Although one way to
stave off this scariness is certainly to make &#x1d458; small, there are
inevitably many, many times where &#x1d458;&nbsp;\>&nbsp;1, and you just have
to deal with that. In this case, keeping &#x1d45d; as close to 1 as you
possibly can helps _quite a bit_, especially for relatively small values of
&#x1d458; &mdash; and we&rsquo;re only dealing with small &#x1d458; here. To
see what I mean, just try some examples yourself. Consider a modest &#x1d458;
value of &#x1d458;&nbsp;=&nbsp;2, and contrast &#x1d45d;&nbsp;=&nbsp;95% with
&#x1d45d;&nbsp;=&nbsp;90%. Although you might think the difference between 95%
and 90% is not so big &mdash; after all, what&rsquo;s five percentage points
here or there? &mdash; we see something significantly more drastic for just
&#x1d458;&nbsp;=&nbsp;2:

- (95%)<sup>2</sup>&nbsp;=&nbsp;90\.25%.
- (90%)<sup>2</sup>&nbsp;=&nbsp;81%.

Oops! That&rsquo;s not a difference of five percentage points, that&rsquo;s
more like a difference of _nine or ten_!

And in the _inter_-temporal case, I want to invoke not the binomial
distribution, but rather, the notion of
[relative risk (RR)](https://en.wikipedia.org/wiki/Relative_risk). In the
&ldquo;What is &lsquo;stun hygiene&rsquo;?&rdquo; section above, I
note&hellip;:

> When, in a given round of battle, a chosen strategy more or less fails due to
> random chance \[&hellip;\], that is a massive loss of _all_ of the following:
> \[&hellip;\]

&hellip;With the conclusion that we must minimize, to the extent practically
possible, the occurrence of such massive losses. With this framing, RR is
exactly what we want to look at. Consider a similar example to the one above,
where we want to compare a usual success rate of &#x1d45d;&nbsp;=&nbsp;95% with
&#x1d45d;&nbsp;=&nbsp;90%. If
&#x1d45e;&nbsp;&#x225d;&nbsp;1&nbsp;&minus;&nbsp;&#x1d45d; is the probability
of failure, then we are comparing &#x1d45e;&nbsp;=&nbsp;5% with
&#x1d45e;&nbsp;=&nbsp;10%. That is a relative risk of
RR&nbsp;=&nbsp;10%&nbsp;&div;&nbsp;5%&nbsp;=&nbsp;2. That&rsquo;s right:
&#x1d45d;&nbsp;=&nbsp;90% sees _twice as many failures_ as
&#x1d45d;&nbsp;=&nbsp;95%. This effectively means paying twice the cost, and
that is a huge difference no matter how you slice it. Because we are couching
this in terms of a single source of &ldquo;cost&rdquo;, the RR doesn&rsquo;t
suffer from some of its misleading properties that you might be familiar with
from&hellip; less-than-reputable medical/ecological/sociological
[science-journalistic](https://en.wikipedia.org/wiki/Science_journalism)
headlines.

## Where are you getting all of this from?

- [<i>Toontown Resources</i>](https://github.com/QED1224/Toontown-Resources/blob/4ddfbd1f4e2e17858ee22b512533f3187c310cd7/README.md)
  ([archived](https://web.archive.org/web/20221115112356/https://github.com/QED1224/Toontown-Resources/blob/4ddfbd1f4e2e17858ee22b512533f3187c310cd7/README.md)),
  which accurately explains TTO mechanics.
- [<i>The Accuracy Problem</i>](https://old.reddit.com/r/toontownrewritten/comments/rol1j7/the_accuracy_problem/)
  ([archived](https://web.archive.org/web/20221115112257/https://old.reddit.com/r/toontownrewritten/comments/rol1j7/the_accuracy_problem/)),
  which confirms that the relevant TTO mechanics persist into post-v3\.0\.0
  TTR.

---

<details>
<summary>Footnotes</summary>

1. Or _possibly_ if toons are using gags from gag tracks that they
   haven&rsquo;t maxed out, but within this document, we&rsquo;re going to
   assume that all gag tracks that are used are maxed.
2. In this context, saying that the action &ldquo;heals&rdquo; doesn&rsquo;t
   necessarily mean that it actually gives anyone laff; rather, only the
   _intent_ has to be healing, even if the potential beneficiaries of the
   healing are all already full laff and thus cannot be effectively healed.
3. I don&rsquo;t know whether a trap SOS counts as a single multi-target
   attack, or as multiple single-target attacks. Using an ordinary level &le;6
   trap gag in tandem with a trap SOS causes just the one trap gag from the
   trap SOS to get canceled, and any remaining ones do damage normally, which
   suggests &ldquo;multiple single-target attacks&rdquo;. However, I
   can&rsquo;t be certain. If you do happen to know, please tell me!
4. I&rsquo;m unsure about whether or not remotes stun, which is why they are
   not in the above list. If you do happen to know, please tell me!
5. Yes, how close you are to maxing a track affects your accuracy with the gags
   in that track! One more reason to max your dang gags!

</details>

[set]: https://en.wikipedia.org/wiki/Set_(mathematics)
[intsc]: https://en.wikipedia.org/wiki/Intersection_(set_theory)
[tempo]: https://en.wikipedia.org/wiki/Tempo_(chess)
