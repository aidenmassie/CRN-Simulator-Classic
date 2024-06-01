from regular_crn import ChemicalReactionNetwork
import random


class StepChemicalReactionNetwork(ChemicalReactionNetwork):
    def __init__(self):
        super().__init__()
        self.STEPS = []


    def GetSteps(self):
        return self.STEPS


    def AddStep(self, step):
        self.STEPS.append(step)
        return True


    def RunConfiguration(self, config):
        if len(config) == len(self.SPECIES):
            ruleset_temp = self.RULES.copy()
            steps_temp = self.STEPS.copy()

            while len(steps_temp) > 0 or len(ruleset_temp) > 0:
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

                if len(ruleset_temp) == 0 and len(steps_temp) > 0:
                    config = [species_c + species_s for species_c, species_s in zip(config, steps_temp[0])]
                    steps_temp.pop(0)
                    ruleset_temp = self.RULES.copy()

            return config

        return None