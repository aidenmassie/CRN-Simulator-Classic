import random


class ChemicalReactionNetwork:
    def __init__(self):
        self.SPECIES = []
        self.RULES = []


    def GetSpecies(self):
        return self.SPECIES


    def GetRules(self):
        return self.RULES


    def AddSpecies(self, species):
        if not species in self.SPECIES:
            self.SPECIES.append(species)
            return True

        return False


    def AddRule(self, rule):
        if not rule in self.RULES and rule[0] != rule[1]:
            self.RULES.append(rule)
            return True
        return False


    def RunConfiguration(self, config):
        if len(config) == len(self.SPECIES):
            ruleset_temp = self.RULES.copy()

            while len(ruleset_temp) > 0:
                index = random.randint(0, len(ruleset_temp) - 1)
                isApplicable = True

                for i, species in enumerate(config):
                    if species < ruleset_temp[index][0][i]:
                        isApplicable = False
                        break

                if isApplicable:
                    application = [product - reactant for product, reactant in zip(ruleset_temp[index][1], ruleset_temp[index][0])]
                    config = [species_c + species_a for species_c, species_a in zip(config, application)]
                    ruleset_temp = self.RULES.copy()
                else:
                    ruleset_temp.pop(index)

            return config
        
        return None