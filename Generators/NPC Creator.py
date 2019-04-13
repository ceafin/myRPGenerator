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
        sex = "she" if randint(1, 2) == 1 else "he"

        result += self.npcName() + " stands before you. "
        result += sex.capitalize() + " "
        result += self.appearance() + ".\n"
        result += sex.capitalize() + " " + self.abilities() + "\n"
        result += "Talents: " + self.talents() + "\n"
        result += "Mannerisms: " + self.mannerisms() + "\n"
        result += "Interaction Traits: " + self.interactionTraits() + "\n"
        result += "Ideals: " + self.ideals() + "\n"
        result += "Bonds: " + self.bonds() + "\n"
        result += "Flaws and Secrets: " + self.flawsSecrets() + "\n"

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
            result += "seems " + choice(highAbil) + "."
        elif fork == 2:
            result += "seems " + choice(lowAbil) + "."
        elif fork == 3:
            result += "seems " + choice(highAbil) + ", while also being " + choice(lowAbil) + "."

        return result

    def talents(self):
        elements = ["", "", ""]
        return choice(elements)

    def mannerisms(self):
        elements = ["", "", ""]
        return choice(elements)

    def interactionTraits(self):
        elements = ["", "", ""]
        return choice(elements)

    def ideals(self):
        elements = ["", "", ""]
        return choice(elements)

    def bonds(self):
        elements = ["", "", ""]
        return choice(elements)

    def flawsSecrets(self):
        elements = ["", "", ""]
        return choice(elements)

    def npcName(self):
        genFile = "./Generators/Names - Celtic.py"

        ex = imp.load_source("generator", genFile)
        zed = ex.generator()

        return zed.start()


# x = generator()
# print x.start()
