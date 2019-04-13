from random import choice
from random import randint


class generator: 
    def version(self):
        return 1.0

    def start(self):
        result = ""
        sex = "she" if randint(1, 2) == 1 else "he"

        result = "[Name] stands before you.\n"
        result + sex.capitalize() + " has "
        if self.appearance()[0].lower() == ("a" or "i" or "o" or "u" or "e" or "y"):
            result = "an " + self.appearance() + "\n"
        else:
            result = "a " + self.appearance() + "\n"
        result = result + "Abilities: " + self.abilities() + "\n"
        result = result + "Talents: " + self.talents() + "\n"
        result = result + "Mannerisms: " + self.mannerisms() + "\n"
        result = result + "Interaction Traits: " + self.interactionTraits() + "\n"
        result = result + "Ideals: " + self.ideals() + "\n"
        result = result + "Bonds: " + self.bonds() + "\n"
        result = result + "Flaws and Secrets: " + self.flawsSecrets() + "\n"

        return result

    def appearance(self):
        elements = [
            "distinctive jewelery: earrings, necklace, circlet, bracelets",
            "piercings",
            "flamboyant or outlandish clothes",
            "formal, clean clothes",
            "ragged, dirty clothes",
            "pronounced scar",
            "missing teeth",
            "missing finger(s)",
            "unusual eye color, or unmatched colors",
            "tattoos",
            "birthmark",
            "unusual skin color",
            "bald",
            "braided beard or hair",
            "unusual hair color",
            "nervous eye twitch",
            "distinctive nose",
            "distinctive posture (crooked or rigid)",
            "execptionally beautiful",
            "execptionally ugly",
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
