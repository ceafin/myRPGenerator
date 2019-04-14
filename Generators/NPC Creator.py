import os
import glob
import imp


from random import choice
from random import randint


class generator:
    def version(self):
        return 1.0

    def start(self):

        result = ""
        npcName = self.npcName()
        sex = "she" if randint(1, 2) == 1 else "he"

        result += npcName + " stands before you. "
        result += sex.capitalize() + " " + self.appearance() + ". "
        result += npcName + " " + self.abilities() + ". "
        result += sex.capitalize() + " " + self.talents() + ". "
        result += npcName + " " + self.mannerisms() + ". "
        result += "When interacting with others " + sex + " " + self.interactionTraits() + ". "
        result += npcName + " " + self.ideals() + ". "
        result += sex.capitalize() + " " + self.bonds() + ". "
        result += "Something that could potentially undermine" + npcName + " " + self.flawsSecrets() + ".\n\n"

        return result

    def appearance(self):
        elements = [
            "is wearing distinctive jewelery: earrings, necklace, circlet, bracelets",
            "has many piercings",
            "has flamboyant or outlandish clothes",
            "is wearing formal, clean clothes",
            "is wearing ragged, dirty clothes",
            "has a pronounced scar",
            "is missing teeth",
            "is missing finger(s)",
            "has an unusual eye color, or unmatched colors",
            "has several visible tattoos",
            "has a noticable birthmark",
            "has unusual skin color",
            "is bald",
            "has a braided beard or braided hair",
            "has unusual hair color",
            "has a nervous eye twitch",
            "has a distinctive nose",
            "has distinctive posture (crooked or rigid)",
            "is execptionally beautiful",
            "is execptionally ugly",
        ]
        return choice(elements)

    def abilities(self):

        fork = randint(1, 3)
        result = ""

        highAbil = [
            "powerful, brawny, strong as an ox (high STR)",
            "lithe, agile, graceful (high DEX)",
            "hardy, hale, healthy (high CON)",
            "studious, learned, inquisitive (high INT)",
            "perceptive, spiritual, insightful (high WIS)",
            "persuasive, forceful, born leader (high CHA)",
        ]
        lowAbil = [
            "feeble, scrawny (low STR)",
            "crumsy, fumbling (low DEX)",
            "sickly, pale (low CON)",
            "dim-witted, slow (low INT)",
            "oblivious, absentminded (low WIS)",
            "dull, boring (low CHA)",
        ]

        if fork == 1:
            result += "seems " + choice(highAbil)
        elif fork == 2:
            result += "seems " + choice(lowAbil)
        elif fork == 3:
            result += "seems " + choice(highAbil) + ", while also being " + choice(lowAbil)

        return result

    def talents(self):
        elements = [
            "can play a musical instrument",
            "can speak several languages fluently",
            "is unbelievably lucky",
            "has perfect memory",
            "is great with animals",
            "is great with children",
            "is great at solving puzzles",
            "is great a [some game]",
            "is great at impersonations",
            "draws beautifully",
            "paints beautifully",
            "sings beautifully",
            "can drink everyone under the table",
            "is an expert carpenter",
            "is an expert cook",
            "is an expert dart thrower and rock skipper",
            "is an expert juggler",
            "is a skilled actor and master of disguise",
            "is a skilled dancer",
            "knows Thieves' Cant",
        ]
        return choice(elements)

    def mannerisms(self):
        elements = [
            "is prone to singing, whistling, or humming quietly",
            "speaks in rhyme of some other peculiar way",
            "has a particularly high/low voice",
            "slurs their words, lisps, or stutters",
            "enunciates overly clearly",
            "speaks louder than necessary for the situation",
            "whispers regardless of the situation",
            "uses flowery speech and long words",
            "frequently uses the wrong word or colloquialism",
            "uses colorful oaths and exclamations",
            "makes constant jokes or puns when possible",
            "is prone to (unbased) predictions of doom",
            "fidgets",
            "squints more than necessary",
            "often stares into the distance",
            "always seems to be chewing on something",
            "often paces",
            "unconsciously taps fingers",
            "unconsciously bites their fingernails",
            "often is tugging their beard or twirling their hair",
        ]
        return choice(elements)

    def interactionTraits(self):
        elements = [
            "stubbornly argumentative",
            "awfully arrogant",
            "blustering",
            "quite rude",
            "very curious",
            "open and friendly",
            "honest",
            "easily hot-tempered",
            "easily irritable",
            "ponderous",
            "very quiet",
            "noticably suspicious",
        ]
        if randint(1, 6) == 6:
            fst = choice(elements)
            scnd = choice(elements)
            while fst == scnd:
                scnd = choice(elements)
            return "is " + fst + " while also " + scnd
        else:
            return "is " + choice(elements)

    def ideals(self):
        alignment = randint(1, 6)

        alignEnum = {1: "good", 2: "lawful", 3: "evil", 4: "chaotic", 5: "neutral", 6: "neuter"}
        ideals = {
            1: ["beauty", "charity", "the greater good", "life", "respect", "self-sacrifice"],
            2: ["community", "fairness", "honor", "logic", "responsibility", "tradition"],
            3: ["dominion", "greed", "might", "pain", "retribution", "slaughter"],
            4: ["change", "creativity", "freedom", "indepenence", "no limits", "whimsy"],
            5: ["balance", "knowledge", "live and let live", "moderation", "neutrality", "people"],
            6: ["aspiration", "discovery", "glory", "nation", "redemption", "self-knowledge"],
        }

        if randint(1, 6) == 6:
            fst = choice(ideals[alignment])
            scnd = choice(ideals[alignment])
            while fst == scnd:
                scnd = choice(ideals[alignment])
            return (
                "holds to the "
                + alignEnum[alignment]
                + " ideals of "
                + fst
                + " and "
                + scnd
                + " in high regard"
            )
        else:
            return (
                "holds the "
                + alignEnum[alignment]
                + " ideal of "
                + choice(ideals[alignment])
                + " in high regard"
            )

    def bonds(self):
        elements = [
            "considers dedication to fulfilling a personal life goal as important",
            "believes being protective of family members as especially important",
            "thinks being protective of colleages or compatriots as very important",
            "recognizes being loyal to one's benefactor, patron, or employer",
            "is captivated by a romantic interest",
            "is drawn to a special place of interest",
            "is very protective of a sentimental keepsake",
            "strives to protect a valuable prossession",
            "is out for revenge",
        ]

        if randint(1, 10) == 10:
            fst = choice(elements)
            scnd = choice(elements)
            while fst == scnd:
                scnd = choice(elements)
            return fst + " and " + scnd
        else:
            return choice(elements)

    def flawsSecrets(self):
        elements = [
            "is their forbidden love or suseptibility to romance",
            "is that they enjoy decadent pleasures",
            "is their arrogance",
            "is that they envy another person's possessions or station",
            "is overpowering greed",
            "is prone to rage",
            "is that they have a powerful enemy",
            "is the specific phobia of _____",
            "is their shameful or scanalous history",
            "is a secret crime or misdeed",
            "is possession of forbidden lore",
            "is fool-hardy bravery",
        ]
        return choice(elements)

    def npcName(self):
        genFile = "./Generators/Names - Celtic.py"

        ex = imp.load_source("generator", genFile)
        zed = ex.generator()

        return zed.start()


# x = generator()
# print x.start()
