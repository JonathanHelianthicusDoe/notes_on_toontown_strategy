#!/usr/bin/env python3

"""
Key
===

exp: expectation/expected
max: maximum
lvl: level
mod: modifier
dmg: damage
per: per toon
atk: attack
ty:  type
"""

import json, pprint


TABLE_HEADER = """\
| Species | Level | Type | Damage |
| :------ | ----: | :--- | -----: |
"""


def readable_type(ty):
    if ty == "sell":
        # Could use &#x1f4f6; instead, but that _means_ something different.
        return "&#x1f4c8; sell"
    elif ty == "cash":
        return "&#x1f4b2; cash"
    elif ty == "law":
        # &#x1f528; is also possible, but is usually depicted as a nailhammer
        # rather than a gavel. You also could use
        # &#x1f9d1;&#x200d;&#x2696;&#xfe0f;, but this 4-codepoint EGC is fairly
        # new (2019?) and thus has poor support across various platforms.
        return "&#x2696; law"
    elif ty == "boss":
        return "&#x1f454; boss"
    else:
        raise ty


with open("cog_arsenals.json", "r", encoding="UTF-8") as f:
    suits = json.loads(f.read())["suits"]

# Index `n` corresponds to `n + 1` toons in the battle.
all_toons_exp = [[] for _ in range(0, 4)]
all_toons_max = [[] for _ in range(0, 4)]
single_toon_exp = [[] for _ in range(0, 4)]
single_toon_max = []

for suit in suits:
    for lvl_mod in range(0, 5):
        info = (suit["name"], suit["type"], suit["base_lv"] + lvl_mod)

        lvl_exp_dmg_per = 0
        # Index `n` corresponds to `n + 2` toons in the battle.
        lvl_exp_dmg_all = [0] * 3
        lvl_max_dmg_per = 0
        lvl_max_dmg_all = [0] * 3
        lvl_exp_dmg_single = [0] * 3
        for atk in suit["arsenal"]:
            atk_max_dmg_per = atk["dmg"][lvl_mod]
            atk_exp_dmg_per = atk_max_dmg_per * atk["acc"][lvl_mod] / 100

            lvl_exp_dmg_per += atk_exp_dmg_per * atk["use"][lvl_mod] / 100
            for toon_count in range(2, 5):
                lvl_exp_dmg_all[toon_count - 2] += (
                    atk_exp_dmg_per
                    * atk["use"][lvl_mod]
                    / 100
                    * (1 if atk["single"] else toon_count)
                )

            lvl_max_dmg_per = max(lvl_max_dmg_per, atk_max_dmg_per)
            for toon_count in range(2, 5):
                lvl_max_dmg_all[toon_count - 2] = max(
                    lvl_max_dmg_all[toon_count - 2],
                    (atk_max_dmg_per * (1 if atk["single"] else toon_count)),
                )

            for toon_count in range(2, 5):
                lvl_exp_dmg_single[toon_count - 2] += (
                    atk_exp_dmg_per
                    * atk["use"][lvl_mod]
                    / (100 * (toon_count if atk["single"] else 1))
                )

        all_toons_exp[0].append((info, lvl_exp_dmg_per))
        for i, d in enumerate(lvl_exp_dmg_all):
            all_toons_exp[i + 1].append((info, d))

        all_toons_max[0].append((info, lvl_max_dmg_per))
        for i, d in enumerate(lvl_max_dmg_all):
            all_toons_max[i + 1].append((info, d))

        single_toon_exp[0].append((info, lvl_exp_dmg_per))
        for i, d in enumerate(lvl_exp_dmg_single):
            single_toon_exp[i + 1].append((info, d))

        single_toon_max.append((info, lvl_max_dmg_per))

# Sort cogs by how much damage they do, from most to least:
for l in all_toons_exp:
    l.sort(key=lambda x: x[1], reverse=True)
for l in all_toons_max:
    l.sort(key=lambda x: x[1], reverse=True)
for l in single_toon_exp:
    l.sort(key=lambda x: x[1], reverse=True)
single_toon_max.sort(key=lambda x: x[1], reverse=True)

# Output Markdown tables; these don't have to be nicely formatted, since we can
# just post-process with an auto-formatter.
out = """\
## Aggregate damage

### Expected aggregate damage

"""

for n, l in enumerate(all_toons_exp):
    out += (
        f"#### {n + 1} toon{'s' if n > 0 else ''}, expected aggregate "
        + "damage\n\n"
        + TABLE_HEADER
    )

    for (name, ty, lvl), d in l:
        out += f"| {name} | {lvl} | {readable_type(ty)} | {d:0.3f} |\n"

    out += "\n"

out += "### Maximum aggregate damage\n\n"

for n, l in enumerate(all_toons_max):
    out += (
        f"#### {n + 1} toon{'s' if n > 0 else ''}, maximum aggregate "
        + "damage\n\n"
        + TABLE_HEADER
    )

    for (name, ty, lvl), d in l:
        out += f"| {name} | {lvl} | {readable_type(ty)} | {d:0.3f} |\n"

    out += "\n"

out += """\
## Damage to given single toon

### Expected damage to given single toon

"""

for n, l in enumerate(single_toon_exp):
    out += (
        f"#### {n + 1} toon{'s' if n > 0 else ''}, expected damage to given "
        + "single toon\n\n"
        + TABLE_HEADER
    )

    for (name, ty, lvl), d in l:
        out += f"| {name} | {lvl} | {readable_type(ty)} | {d:0.3f} |\n"

    out += "\n"

out += "### Maximum damage to given single toon\n\n" + TABLE_HEADER

for (name, ty, lvl), d in single_toon_max:
    out += f"| {name} | {lvl} | {readable_type(ty)} | {d:0.3f} |\n"

print(out, end="")
