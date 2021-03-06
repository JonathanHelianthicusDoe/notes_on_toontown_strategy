# TTR bugs (that I know of) seriously affecting the game&rsquo;s core mechanic

[![CC BY-SA 4.0+](https://i.creativecommons.org/l/by-sa/4.0/88x31.png
"CC BY-SA 4.0+")](https://creativecommons.org/licenses/by-sa/4.0/)

These are ordered &mdash; roughly speaking &mdash; from most critical to least
critical. These are oriented towards Toontown Rewritten (TTR) specifically,
although some or all of them may (or may not) be present in other Toontowns.

## Cogs with less than one HP do not die

**Preface:** Apparently, TTR has not only inherited this bug from TTO (which I
expected anyways), but this bug has also had a consistent server-side
implementation stretching as far back as is known (presumably even earlier than
2003). The semantics of said server-side implementation are that the
&ldquo;knockback&rdquo;/&ldquo;orange&rdquo; damage is equal to the raw damage
divided by two, and then rounded towards zero (in [C][c]:
`int kbBonus = totalDamage / 2;`, with `totalDamage` being an `int`). The
client, however, has always rounded towards positive infinity (rather than
towards zero), resulting in clients seeing completely incorrect numbers. The
natural approach here is to observe that the server side has always rounded
towards zero and call that the one-and-final truth; in this case, this bug is
simply a visual one (albeit an extremely serious visual bug that happens to
affect the core mechanic of the game). This is a perfectly good interpretation,
and I am sympathetic to it, but I am also somewhat sympathetic to my original
interpretation, which is that rounding towards positive infinity are the
intended semantics. The main reasons that one might believe this are (here we
assume a Python 2 implementation):

1. Yellow damage (combo damage) **is rounded towards positive infinity
   already**, and has no known issues. This is essentially guaranteed to be
   intentional (i.e. the semantics intended by the original developers of TTO),
   since there are no known bugs in this respect, and rounding towards positive
   infinity is &mdash; as mentioned below &mdash; not generally something that
   you can do *accidentally*. In this case, particularly, the division is by
   five (rather than two), so we know that the rounding *really is* towards
   positive infinity (or away from zero, which is the same for positive
   numbers anyways) by testing cases in which the pre-rounded result is not an
   integer nor a [half-integer](https://en.wikipedia.org/wiki/Half-integer).
   This eliminates the possibility that any implementation of `round` (i.e.
   rounding to the nearest integer, with some way of breaking ties) is being
   used. If the intended semantics of orange damage is to round towards zero,
   then this creates an inconsistency/incongruency where there apparently was
   none before.
2. If rounding towards zero was the intended semantics, then Toontown
   (including both TTO and TTR) has always displayed the incorrect numbers to
   the players, even though the damage numbers are supposedly the One True
   &amp; Precise Source&trade; of information (as opposed to imprecise sources
   of information, like the color of cog lights) w.r.t. how much damage you are
   dealing to cogs. Because of this, declaring the intended semantics to be
   &ldquo;rounding towards zero&rdquo; &mdash; and thus fixing the bug by
   changing the numbers that are displayed &mdash; is arguably *more* of a
   [retcon](https://en.wikipedia.org/wiki/Retroactive_continuity) from the
   player&rsquo; perspective than declaring the intended semantics to be
   &ldquo;rounding towards positive infinity&rdquo; and changing the
   server-side behavior.
3. How do you even make the mistake in this way? Assuming that rounding towards
   zero is the intended semantics, the server is correctly rounding towards
   zero, and the client is erroneously rounding towards positive infinity. How
   does one *accidentally* round towards positive infinity, exactly? It is
   much, much easier to accidentally round towards zero, because that is the
   default behavior of integer division in *any* programming language, because
   that is how *all* hardware implements it. On the other hand, if you were to
   accidentally round towards positive infinity, you would either have to
   *accidentally* do some convoluted integer arithmetic (e.g.
   `kbBonus = (totalDamage - 1) / 2 + 1`, again assuming an integral value for
   `totalDamage`), or *accidentally* use a `ceil` (ceiling) or `round` function
   call when really you meant to use `floor` or even simply `int` function
   call. The latter is a more understandable mistake, but still begs the
   question of why you would use `ceil` when the semantics are clearly the
   opposite (rounding towards positive infinity) or use `round` when no
   implementation of `round` is going to actually have the semantics that you
   intend (even if it does work in some cases). It also begs the question of
   why you are using unnecessarily inefficient [floating point
   division][fdiv]\(!\) when all you want is to divide an integer by two, and
   possibly round up (again, e.g. `kbBonus = (totalDamage - 1) / 2 + 1`).

Naturally, this is a slippery question to ask, since ultimately it is either
asking for the original intent of TTO&rsquo;s developers &mdash; intent which
is almost certainly lost to time &mdash; or asking for a normative judgement.
Either way, though, this is a serious bug (visual or otherwise), and so is left
here at the top of the list.

---

This is, perhaps, the most shocking one, since it violates one of the most core
principles of cog-fighting: cogs with their HP lowered to zero &mdash; or less
&mdash; explode, thus being removed from the battle entirely. An quirk of this
bug is that something (perhaps just on the client side, but not on the server
side) is actually doing this calculation *correctly*, because cogs that have
had their HP lowered below one, but that do not explode, *still have blinking
red lights*. Specifically, the light blinks at the normal frequency that you
would expect for a cog that is about to start blowing up: faster than a
&ldquo;slow blink&rdquo; (indicating very low &mdash; but more than zero
&mdash; HP), and slower than a &ldquo;rapid blink&rdquo; (a very fast blinking
only produced by a certain bug that is listed below in this document). However,
this correct blinking only seems(?) to last for one round, and in future
rounds, the very rapid blinking observed in other bugs occurs instead.

This bug appears (as far as I know) to only occur in the presence of so-called
&ldquo;orange damage&rdquo;: the extra damage equal to half of the damage dealt
to a cog (only applies to throw and squirt gags) while it is lured, rounded
towards positive infinity &mdash; this &ldquo;rounded towards positive
infinity&rdquo; bit is *crucial* here. I have not (as of yet) gone out to
search for instances of this bug, so all cases that I have here are ones that I
found organically during normal play. The fact that there are, in spite of
this, still *four* completely distinct cases, speaks to how much breakage this
bug can cause:

1. Use an organic Squirtgun on a lured level 3 v1.0 cog. This deals
   `13 + ceil(13 / 2) = 13 + 7 = 20` damage, which is exactly the HP of a level
   3 cog. Thus, the cog has 0 HP &mdash; but it does not die, and can still
   attack toons as if it had more than 0 HP remaining.
2. Use an organic Firehose on a lured level 9 v1.0 cog, immediately followed by
   an inorganic<sup>&dagger;</sup> Safe. This deals
   `33 + ceil(33 / 2) + 60 = 33 + 17 + 60 = 110` damage, which is exactly the HP
   of a level 9 cog.
3. Use an inorganic Birthday Cake on an unlured level 10 v1.0 cog. Lure the
   cog, and hit it with an inorganic Seltzer Bottle. This deals
   `100 + 21 + ceil(21 / 2) = 100 + 21 + 11 = 132` damage, which is exactly the
   HP of a level 10 cog.
4. Use an inorganic and unmaxed Cream Pie that does exactly 37 damage on a
   lured level 6 v1.0 cog. This deals `37 + ceil(37 / 2) = 37 + 19 = 56`
   damage, which is exactly the HP of a level 6 cog.

I suspected that this bug might be a result of TTR&rsquo;s servers (but not
necessarily its clients) using integer division when calculating &ldquo;orange
damage&rdquo;. This would make a lot of sense, since all of the cases seem to
be off by one, and to happen when calculating orange damage for an *odd* amount
of raw damage (odd numbers being the numbers where integer division &mdash;
a.k.a. rounding towards zero &mdash; and rounding towards positive infinity can
actually diverge in their results). Furthermore, similar cases where the
dividend is *even* end up working properly: an organic Stormcloud used on a
lured level 10 v1.0 cog does actually kill it, as expected:
`88 + ceil(88 / 2) = 88 + 44 = 132`. And furthermore, since TTR&rsquo;s
codebase is still on Python 2, it is much easier for them to confuse integer
division with floating-point division (floating-point division and then using
`math.ceil` is one way of implementing &ldquo;rounding towards positive
infinity&rdquo; in Python, even if it is needlessly inefficient&hellip;)
because the `/` operator is used for *both* of these operations in Python 2.
This is a quirk of Python 2 that was fixed in Python 3 via the addition of an
entirely new operator dedicated to integer division: `//`.

&dagger;: I was able to reproduce this bug long ago with an organic Firehose and
an ***organic*** Safe on a lured level 9 v1.0 cog. However, now that I get back
around to it, it appears to have been anecdotal, and therefore possibly
indeterministic, as I have had trouble reproducing it again. It&rsquo;s also
possible that this particular instance of the bug has been patched since then,
which would not be surprising given that it&rsquo;s so egregious. If you can
reproduce this version of the bug, please do send me a screen-recording of it,
and/or at least a more reliable and exact sequence of steps for reproducing it.

## Unused gags are sometimes stolen from toons&rsquo; inventories for no apparent reason

This is another particularly critical bug, because having your gags stolen from
your inventory during battle is quite&hellip; disturbing, and even punishes the
use of some gag-picking strategies that would otherwise be smart to use. This
bug is also accompanied by a (still concerning, albeit much less concerning)
audiovisual bug.

When a toon chooses a gag to be used on a cog, and the cog dies before it gets
around to be that gag track&rsquo;s turn to be used, the expected behavior is
that the gag is simply not used at all. For example, if a level 1 v1.0 cog is
killed by a Cupcake, but another toon also used a Squirting Flower on it in
that same round, the expectation is that the Squirting Flower is simply not
used at all. However, if there are at least one other cog(s) in the fight which
have *also* been targeted with one or more squirt gag(s) in that same round,
and at least one of those gag(s) can actually be used (because those cog(s)
have not died yet, regardless of whether or not these other squirt gag(s) hit
or miss), then there is some chance that the Squirting Flower on the level 1
v1.0 cog will still be used. This bug *appears* (as far as I know) to be
somewhat indeterministic, so there is no guarantee of whether or not it will
occur. But if it does, the Squirting Flower will erroneously be animated as if
the cog were still alive (thus hitting nothing in particular, and often &mdash;
in the case of squirt gags particularly &mdash; just shooting off into a random
direction). The dead cog then erroneously &ldquo;explodes&rdquo; again
(although it is largely invisible, you can hear the sounds, see the explosion
and flying gears, and the toons in the battle will do the usual ducking
animation), and most importantly, the toon that chose that Squirting Flower
***has had it removed from their inventory***. Of course, in the case of a
Squirting Flower this is typically not a big deal, but usually this bug occurs
with level 4, 5, and 6 gags.

## Cog lights on v2.0 cogs are completely broken

This one doesn&rsquo;t need too much description; anyone who has spent any
significant amount of time fighting v2.0 cogs is uncomfortably familiar with
this particular bug. Strictly speaking, this is exclusively a visual bug
&mdash; if you know how so-called &ldquo;carryover&rdquo; damage works and how
to calculate it (and other forms of damage, of course), you can simply ignore
cog lights in general (on v2.0 and v1.0 cogs alike) and use the math
instead&hellip; although, see the first bug on this list for an exception to
this rule!

This typically manifests as (typically, rapidly) blinking red lights on the
second shell (skelecog shell) of a v2.0 cog, or as a green light on the second
shell of a v2.0 cog. It seems that the rapidly blinking red light is caused by
a v2.0 cog taking damage to its second shell in the same round as &mdash; but
strictly after (due to certain gag tracks getting to go earlier than others)
&mdash; losing its first shell via exploding. And it seems that the erroneous
green light is caused by a v2.0 cog taking damage to its second shell *at the
same time as* (meaning within a single gag track, not *just* within the same
round) it losing its first shell via exploding.

All of that being said, this is still a fairly critical bug, since it asks the
question of why Toontown&rsquo;s designers gave the cogs any lights at all, if
they were just going to be totally useless &mdash; indeed, worse than useless,
since they are *actively misleading* to the vast majority of players. The
reality is that while the calculation of damage against cogs &mdash; and cog
HP, and so on &mdash; are public knowledge, the actual game itself does exactly
*nothing* to teach players any of this information whatsoever. As a result, the
natural way that players form habits and internal knowledge about cog-fighting
is by three main mechanisms:

- Trial and error: you can just keep hitting the cogs, and eventually they will
  die! You can use this to gauge the relative power of certain levels of cogs
  and of certain gags against said cogs.
- Memorizing combinations that work on particular levels of cog: usually these
  combinations are themselves found via trial and error.
- Cog lights: the only hints that the game *explicitly* gives to you are via
  cog lights, which tell you an approximate proportion of the cog&rsquo;s
  starting HP that it has left, thus giving a hint as to how much force is
  needed to completely kill the cog.

One of these three mechanisms is wiped out in the presence of v2.0 cogs, and
indeed, only serves to mislead players by lying to them and saying that cogs
have less &mdash; or more &mdash; HP than they actually do.

## The rescindment of a gag pick is not communicated by the servers

Toontown has always had the extremely crucial feature that allows toons to take
back their gag picks after having already made them (or having partially made
them, in the case of selecting a single-target gag but not selecting its
target). However, in many (most&#x203d;) cases, doing this will cause all toons
in the battle to still see your gag pick as being the already-rescinded pick.
This is a fairly critical bug because, in reality, the vast majority (and in
most cases, all) of the communication that occurs when picking gags in the heat
of battle is *through these pick indicators*, which supposedly display whatever
gag (or SOS, or&hellip;) each toon in the battle has picked (or not yet picked)
so far. Thus, this bug significantly hampers coordination/teamwork.

## Attempting to pick an SOS card during battle can cause the toon to be unable to pick anything at all (other than passing)

This is a bizarre and seemingly indeterministic bug; it seems(?) to happen more
often when the toon navigates to their &ldquo;SOS&rdquo; GUI and then tries to
go back to the normal gag-picking GUI. In whatever case it may be, making any
attempt to even *look* at one&rsquo;s own SOS cards (and/or doodle, &amp;c.) is
risking the possibility that you may be stuck in an endless loop of attempting
to pick literally anything (SOS cards, ordinary gags, &amp;c.), only to have
the game pick &ldquo;pass&rdquo; for you instead of whatever you picked. The
actual &ldquo;pass&rdquo; symbol (a red circle with a red diagonal slash
through it, on a white background) does show up for all toons in the battle,
despite the toon of course not choosing to pass at all, and the end result is
indeed that the toon does absolutely nothing in that round.

Because SOS cards are so powerful when used, and because they are often used as
a kind of &ldquo;get out of jail free card&rdquo;, I have personally gone sad
on multiple occasions due to this particular bug.

## Toons are often unnecessarily forced to wait very long to get into a battle, occasionally not being able to join even after waiting

This one is mostly an unnecessary inconvenience, although in certain very
severe cases it can actually be a critical bug. Typically, this happens when
four toons all join a battle at roughly the same time, and three of them get
&ldquo;into&rdquo; the battle, thus being able to see their gag-picking GUI and
the battle timer (rather than standing just outside of the battle&rsquo;s
circumference, waiting). Then, the fourth one that has yet to properly join the
battle is forced to wait nearly the entire 20 seconds of the battle timer
before they are finally allowed into the battle. This is, obviously, just a
waste of roughly 20 seconds, and it happens very often.

In certain rarer cases (the only cases that I know of seem to have all been in
sellbot factories, although this may just be some bias or a fluke), the toon
can actually be forced to wait *more* than the 20 seconds on the battle timer,
thus typically resulting in the three toons in battle all picking nothing
(expecting the fourth toon to be allowed into battle at any moment), and thus
getting attacked by all of the cogs for no reason. Alternatively, this can just
result in them picking gags and fighting the cogs without the participation (at
least, in the first round, if there are more rounds) of the fourth toon.

## SOS trap gags stick around longer than expected, preventing the use of ordinary trap gags

This is a familiar bug for anyone who has used (or has been in a battle where
someone else has used) an SOS trap card &mdash; regardless of its number of
stars. This bug has two components: a visual one, and a
gameplay/game-mechanical one. The visual issue is that these SOS trap gags tend
to visually stick around wherever they were placed, even after they have been
activated and have done the usual damage to the cog(s). Mechanically, these SOS
trap gags that seem to &ldquo;stick around&rdquo; also *behave* like actual
trap gags, albeit only in some ways. These gags will *not* be able to deal
damage again, and presumably (although I cannot confirm this) do *not* stun the
cogs to give extra accuracy to other gags (lure, throw, and drop in
particular); however, they *do* behave like actual trap gags in that they
prevent toons from placing ordinary trap gags down wherever they are.

## The damage instances that a lured cog takes in a given round, as the result of a given gag track, are displayed in an incorrect order

In particular, this only applies to throw and to squirt, since those are the
only gag tracks that benefit from &ldquo;orange damage&rdquo; (knockback
damage). When a lured cog is hit by two or more throw gags (or two or more
squirt gags, as the case may be) in a given round, it takes the raw damage of
the throw gags, as well as the &ldquo;yellow damage&rdquo; (combo damage) due
to there being more than one throw gag hitting that cog, as well as the orange
damage due to the cog being hit with throw while it is lured. Semantically,
this is the correct ordering, as anyone who is familiar with so-called
&ldquo;carryover damage&rdquo; can tell you. Raw damage is applied first,
followed by yellow damage, followed by orange damage. But in-game, the orange
damage is displayed before the yellow damage (although the raw damage is
correctly shown before both of them).

---

## Addendum: bugs that could, possibly, be explained as &ldquo;fully intentional&rdquo; and thus not be bugs at all

### Two (or more) sound gags used in the same round can differ in whether or not they hit

This sometimes happens in the presence of sound SOS cards. SOS cards that use
gags are guaranteed to hit all of their targets, because they calculate their
[outcomes](https://en.wikipedia.org/wiki/Bernoulli_trial) differently than the
corresponding ordinary gags. Ordinary sound gags, on the other hand, have 95%
accuracy at best (and also 95% accuracy at worst, if we assume maxed sound), so
it is possible for the SOS card sound gag(s) to hit while the ordinary sound
gag(s) miss.

This is a more odd behavior and is conceptually distinct from the similar
&ldquo;bug&rdquo; listed further down, because in this case, only gags that
target all cogs are involved. Therefore, it is more shocking that the gags can
differ in whether or not they hit; they are of the same track, used in the same
round, and have actually **identical** targets (not just **overlapping**
targets). Furthermore, this particular behavior can no longer be explained away
by analogy with lure gags: even with lure gags, two lure gags that have
**identical** targets *never* differ in whether or not they hit. This is,
however, still classified as &ldquo;possibly explained as &lsquo;fully
intentional&rsquo;&rdquo; because internally, it is intentional that SOS card
gags and ordinary gags have their
[outcomes](https://en.wikipedia.org/wiki/Bernoulli_trial) calculated in
different ways.

Note that in principle, this can also occur due to the combination of one or
more drop SOS cards with one or more Toontanics.

### Squirt, throw, and sound gags sometimes miss lured cogs

This happens in cases where the squirt/throw/sound gag in question is one that
targets all cogs, and some &mdash; but not all &mdash; cogs in the battle are
lured. This one is probably(?) intentional, I suspect, but is nevertheless a
violation of one of the rules that players learn very early on when it comes to
lure gags. This has led many to speculate about whether or not it is possible
for sound gags and/or Wedding Cake and/or Geyser to miss when *all* cogs are
lured (spoiler: they cannot miss in that case&hellip; or [can
they](https://en.wikipedia.org/wiki/Proprietary_software)?).

The [main &ldquo;Toontown Resources&rdquo;
document](https://github.com/QED1224/Toontown-Resources#equation-) suggests
that there is something called `luredRatio` that is calculated based on the
proportion of the cogs in the battle that are currently lured. One quirk of
this `luredRatio` (at least, as presented in said document) is that it actually
affects the accuracy of single-target throw and squirt gags that are targeting
unlured cogs. For squirt, this isn&rsquo;t that big of a deal, since assuming
max squirt, all squirt gags have maximum accuracy (95%) on all unlured cogs,
regardless of cog level (although it can make a difference for toons with
unmaxed squirt). But for throw, just *one* cog being lured in a row of 4 cogs
will boost the accuracy of a throw gag targeting an unlured level 12 cog from
80% (the usual value, assuming max throw) to maximum accuracy (95%). This is,
needless to say, a bizarre mechanic, such that I doubt that it is really
implemented this way in TTR&hellip; but [who
knows](https://en.wikipedia.org/wiki/Proprietary_software)? Clearly, the intent
of this `luredRatio` mechanic, as written, is to improve the accuracy of
certain multi-target gags (particularly sound gags, but also Wedding Cake and
Geyser) whenever some &mdash; but not all &mdash; of its targets are lured. Of
course, for all sound gags, as well as for Geyser, this is mostly pointless,
since (assuming max sound) they already have &mdash; at worst &mdash; maximum
accuracy (95%). For Wedding Cake, as already mentioned for other throw gags,
this can actually be a boon. But doesn&rsquo;t it feel weird for level 7 gags
to have anything less than 95% accuracy anyways? They are, after all, a sort of
disposable &ldquo;reward&rdquo;, like SOS cards, unites, and pink slips.

The point of mentioning `luredRatio` here at all is that `luredRatio` would
seem to be the justification for allowing squirt, throw, and sound gags to
sometimes miss lured cogs: in these seemingly bizarre cases, sure, there is a
non-zero chance of the gag(s) missing, but that doesn&rsquo;t mean that the one
or more cog(s) being lured is *totally useless*; `luredRatio` ensures that
these cog(s) being lured does at least increase accuracy! &hellip;Except that,
as discussed, that&rsquo;s not really how `luredRatio` works anywhere other
than in *theory*, due to accuracy being capped at 95%.

### Two (or more) throw, squirt, or drop gags of the same track that are used in the same round on the same cog can differ in whether or not they hit

This &ldquo;bug&rdquo; (again, likely not a &ldquo;bug&rdquo; <i>per se</i>,
since it is likely intentional) is similar to and related to the one above.
This can occur in the presence of Wedding Cakes, Geysers, Toontanics, and drop
SOS cards, whenever at least one cog is not lured and at least one
single-target gag of the same track (throw, squirt, or drop, respectively) is
used in the same round. This is, similarly to the previously listed
&ldquo;bug&rdquo;, a violation of one of the rules that players learn very
early on when it comes to multiple gags of the same track targeting the same
cog in the same round. However, it is likely intentional (or at least a simple
byproduct of something intentional), given that lure gags work similarly. In
the case of throw, squirt, and drop, however, it comes as more shocking because
gags of these tracks are inherently single-target &mdash; the only exceptions
being the level seven gags of said tracks.

[c]: https://en.wikipedia.org/wiki/C_%28programming_language%29
[fdiv]: https://en.wikipedia.org/wiki/Floating-point_arithmetic#Multiplication_and_division
