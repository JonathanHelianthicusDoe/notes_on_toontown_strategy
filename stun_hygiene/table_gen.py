#!/usr/bin/env python

HEAD = """\
| level | gag  |  95% |  90% |  85% |
| ----: | :--- | ---: | ---: | ---: |
"""
HEAD_ABBR = """\
| level |  95% |  90% |  85% |
| ----: | ---: | ---: | ---: |
"""
GAGS = ["magnet", "hypno", "org hypno", "throw", "drop"]
PROP_ACC = {
    "magnet": 60,
    "hypno": 70,
    "org hypno": 80,
    "throw": 75,
    "drop": 50,
}
EMOJI = {
    "magnet": 0x1F9F2,
    "hypno": 0x1F453,
    "org hypno": 0x1F97D,
    "throw": 0x1F967,
    "drop": 0x1F3B9,
}


def tgtDef(level):
    if level < 2:
        return -2
    return -5 * (level - 1)


def printTable(gags):
    out = HEAD if len(gags) > 1 else HEAD_ABBR

    for level in range(14, 6, -1):
        for gag in gags:
            stunlessHitChance = PROP_ACC[gag] + 60 + tgtDef(level)
            if stunlessHitChance >= 95:
                continue
            hitChances = [stunlessHitChance + 20 * n for n in range(0, 4)]

            out += f"| {level} |"
            if len(gags) > 1:
                out += f" &#x{hex(EMOJI[gag])[2:]};&nbsp;{gag} |"
            for hitChanceTarget in [95, 90, 85]:
                stuns = -1
                for i, hitChance in enumerate(hitChances):
                    if hitChance >= hitChanceTarget:
                        stuns = i
                        break

                out += f" {stuns} |"
            out += "\n"

    print(out, end="")


print("#### &#x1f4b8;&nbsp;Lure\n")
printTable(["magnet", "hypno", "org hypno"])
print("\n#### &#x1f3b9;&nbsp;Drop\n")
printTable(["drop"])
print("\n#### &#x1f967;&nbsp;Throw\n")
printTable(["throw"])
