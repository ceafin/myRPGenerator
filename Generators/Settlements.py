from random import choice, choices
from random import randint


class generator:
    def version(self):
        return 1.0

    def start(self):
        result = "Settlement of _____\n"
        result += "Race Relations: " + self.raceRelations() + "\n"
        result += "Ruler's Status: " + self.rulersStatus() + "\n"
        result += "Notable Trait(s): " + self.notableTraits() + "\n"
        result += "Known for its: " + self.knownForIts() + "\n"
        result += "Current calamity: " + self.currentCalamity() + "\n"

        return result

    def raceRelations(self):
        elements = [
            "Harmony",
            "Tension or rivalry",
            "Racial majority are conquerors",
            "Racial minority are rulers",
            "Racial minority are refugees",
            "Racial majority oppresses minority",
            "Racial minority oppresses majority",
        ]
        weights = [10, 4, 2, 1, 1, 1, 1]
        return choices(elements, weights, k=1)[0]
    
    def rulersStatus(self):
        elements = [
            "Respected, fair, and just",
            "Feared tyrant",
            "Weakling manipulated by others",
            "Illegitimate ruler, simmering civil war",
            "Ruled or controlled by a powerful monster",
            "Mysterious, anonymous cabal",
            "Contested leadership, open fighting",
            "Cabal seized power openly",
            "Doltish lout",
            "On deathbed, claimants compete for power",
            "Iron-willed but respected",
            "Religious leader"
        ]
        weights = [5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
        return choices(elements, weights, k=1)[0]

    def notableTraits(self):
        elements = [
            "Canals in place of streets",
            "Massive statue of manument",
            "Grand temple",
            "Large fortess",
            "Verdent parks and orchards",
            "River divides town",
            "Major trade center",
            "Headquarters to a power family or guild",
            "Population mostly wealthy",
            "Destitude, rundown",
            "Awful smell (tanneries, open sewers)",
            "Center of trader for one specific good",
            "Site of many battles",
            "Site of mythic or magical event",
            "Important library or archive",
            "Worship of all gods banned",
            "Sinister reputation",
            "Notable library or academy",
            "Site of important tomb or graveyard",
            "Built atop ancient ruins"
        ]
        if randint(1, 20) == 20:
            fst = choice(elements)
            scnd = choice(elements)
            while fst == scnd:
                scnd = choice(elements)
            return "1) " + fst + ", and 2) " + scnd
        else:
            return choice(elements)

    def knownForIts(self):
        elements =[
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20"
        ]

        return choice(elements)

    def currentCalamity(self):
        elements =[
            "1",
            "2",
            "3",
            "4",
            "Plague or famine (sparks riots)",
            "7",
            "Marauding monsters",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20"
        ]
        weights=[1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        return choices(elements,weights,k=1)[0]

# x = generator()
# print x.start()
