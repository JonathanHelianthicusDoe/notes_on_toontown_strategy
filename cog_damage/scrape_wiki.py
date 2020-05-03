#!/usr/bin/env python3

"""
I just ran this script like this:

./scrape_wiki.py https://toontownrewritten.fandom.com/wiki/Cold_Caller \
                 https://toontownrewritten.fandom.com/wiki/Telemarketer \
                 https://toontownrewritten.fandom.com/wiki/Name_Dropper \
                 https://toontownrewritten.fandom.com/wiki/Glad_Hander \
                 'https://toontownrewritten.fandom.com/wiki/Mover_%26_Shaker' \
                 https://toontownrewritten.fandom.com/wiki/Two-Face \
                 https://toontownrewritten.fandom.com/wiki/The_Mingler \
                 https://toontownrewritten.fandom.com/wiki/Mr._Hollywood \
                 https://toontownrewritten.fandom.com/wiki/Short_Change \
                 https://toontownrewritten.fandom.com/wiki/Penny_Pincher \
                 https://toontownrewritten.fandom.com/wiki/Tightwad \
                 https://toontownrewritten.fandom.com/wiki/Bean_Counter \
                 https://toontownrewritten.fandom.com/wiki/Number_Cruncher \
                 https://toontownrewritten.fandom.com/wiki/Money_Bags \
                 https://toontownrewritten.fandom.com/wiki/Loan_Shark \
                 https://toontownrewritten.fandom.com/wiki/Robber_Baron \
                 https://toontownrewritten.fandom.com/wiki/Bottom_Feeder \
                 https://toontownrewritten.fandom.com/wiki/Bloodsucker \
                 https://toontownrewritten.fandom.com/wiki/Double_Talker \
                 https://toontownrewritten.fandom.com/wiki/Ambulance_Chaser \
                 https://toontownrewritten.fandom.com/wiki/Back_Stabber \
                 https://toontownrewritten.fandom.com/wiki/Spin_Doctor \
                 https://toontownrewritten.fandom.com/wiki/Legal_Eagle \
                 https://toontownrewritten.fandom.com/wiki/Big_Wig \
                 https://toontownrewritten.fandom.com/wiki/Flunky \
                 https://toontownrewritten.fandom.com/wiki/Pencil_Pusher \
                 https://toontownrewritten.fandom.com/wiki/Yesman \
                 https://toontownrewritten.fandom.com/wiki/Micromanager \
                 https://toontownrewritten.fandom.com/wiki/Downsizer \
                 https://toontownrewritten.fandom.com/wiki/Head_Hunter \
                 https://toontownrewritten.fandom.com/wiki/Corporate_Raider \
                 > cog_arsenals.json

Notice that Big Cheese (and only Big Cheese) is missing; this is because it's
~*~sPeCiAl~*~ and has attacks that do a random amount of damage(?)

This script picks up a small amount of garbage that I had to clean up but oh
well... The wikia is not consistent in how it formats things.
"""

import html.parser, json, sys, urllib.request


class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()

        self.data = {
            "name": "",
            "type": "",
            "base_lv": 0,
            "arsenal": [],
        }
        self.in_main_table = False
        self.in_table = False
        self.tr_ix = -1
        self.td_ix = -1
        self.in_font = False

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            for name, val in attrs:
                if name == "class" and "article-table" in val:
                    self.in_table = True
                    break
            if not self.in_table:
                self.in_main_table = True

        elif tag == "tr":
            self.tr_ix += 1

        elif tag == "td":
            self.td_ix += 1

        elif tag == "font":
            self.in_font = True

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_main_table = False
            self.in_table = False
            self.tr_ix = -1

        if tag == "tr":
            self.td_ix = -1

        elif tag == "font":
            self.in_font = False

    def handle_data(self, data):
        stripped = data.strip()
        if len(stripped) == 0:
            return

        if self.in_main_table:
            if self.tr_ix == 1 and self.in_font:
                self.data["name"] = stripped
            elif self.tr_ix == 3 and self.td_ix == 1:
                if stripped[-1] == "s":
                    self.data["type"] = stripped[:-4].lower()
                else:
                    self.data["type"] = stripped[:-3].lower()
            elif self.tr_ix == 4 and self.td_ix == 1:
                self.data["base_lv"] = int(stripped)
        elif self.in_table:
            if self.tr_ix == 0:
                self.data["arsenal"].append(
                    {
                        "name": stripped,
                        "single": False,
                        "dmg": [],
                        "acc": [],
                        "use": [],
                    }
                )
            elif self.tr_ix == 1 and self.td_ix == 1:
                self.data["arsenal"][-1]["single"] = (
                    stripped.split()[0].lower() == "single"
                )
            elif self.tr_ix == 3 and self.td_ix > 0:
                self.data["arsenal"][-1]["dmg"].append(int(stripped))
            elif self.tr_ix == 4 and self.td_ix > 0:
                self.data["arsenal"][-1]["acc"].append(int(stripped))
            elif self.tr_ix == 5 and self.td_ix > 0:
                self.data["arsenal"][-1]["use"].append(int(stripped))


def scrape_page(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("UTF-8")
            parser = Parser()
            parser.feed(html)

            return parser.data
    except Exception as e:
        print(f"{url}\n", file=sys.stderr)

        raise e


suits = []
for arg in sys.argv[1:]:
    suits.append(scrape_page(arg))
print(json.dumps({"suits": suits}))
