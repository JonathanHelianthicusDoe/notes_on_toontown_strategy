# Notes on cog damage

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

For each cog, we have basically 3 dimensions along which the statistics that
I&rsquo;m considering &ldquo;relevant&rdquo; lie. One is the type of statistic:
either [expected value](https://en.wikipedia.org/wiki/Expected_value) or
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

[discrete]: https://en.wikipedia.org/wiki/Discrete_probability_distribution#Discrete_probability_distribution
[outcome]: https://en.wikipedia.org/wiki/Outcome_(probability)
[continuous]: https://en.wikipedia.org/wiki/Discrete_probability_distribution#Continuous_probability_distribution
[ring]: https://en.wikipedia.org/wiki/Ring_(mathematics)
