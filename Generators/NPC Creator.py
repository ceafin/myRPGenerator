from random import choice
from random import randint


class generator:
    def version(self):
        return 1.0

    def start(self):
        result = ""
        sex = "she" if randint(1, 2) == 1 else "he"

        result += "[Name] stands before you. "
        result += sex.capitalize() + " "
        result += self.appearance() + ".\n"
        result += "Abilities: " + self.abilities() + "\n"
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
        elements = ["", "", ""]
        return choice(elements)

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


# x = generator()
# print x.start()
