import random

class ChemicalReactionNetwork:
    def __init__(self):
        self.SPECIES = []
        self.RULESET = []

    def AddSpecies(self, species):
        for s in species:
            if not s in self.SPECIES:
                self.SPECIES.append(s)
    
    def AddRule(self, rule):
        if rule in self.RULESET:
            print('ERROR: Rule was already found in the CRN\'s ruleset!')
        elif rule[0] == rule[1]:
            print('ERROR: Rule with the same count of reactants and products not allowed!')
        else:
            reactants = dict()
            products = dict()

            for r in rule[0]:
                if not r in self.SPECIES:
                    print('ERROR: Species {} was not found in the CRN\'s species list!'.format(r))
                    return
                if r in reactants:
                    reactants[r] += 1
                else:
                    reactants[r] = 1
            
            for p in rule[1]:
                if not p in self.SPECIES:
                    print('ERROR: Species {} was not found in the CRN\'s species list!'.format(p))
                    return
                if p in products:
                    products[p] += 1
                else:
                    products[p] = 1

            self.RULESET.append([reactants, products])
    
    def DeleteSpecies(self, species):
        for s in species:
            if s in self.SPECIES:
                self.SPECIES.remove(s)
    
    def DeleteRule(self, rule):
        # This is ugly.
        reactants = dict()
        products = dict()

        for r in rule[0]:
            if not r in self.SPECIES:
                print('ERROR: Species {} was not found in the CRN\'s species list!'.format(r))
                return
            if r in reactants:
                reactants[r] += 1
            else:
                reactants[r] = 1
            
        for p in rule[1]:
            if not p in self.SPECIES:
                print('ERROR: Species {} was not found in the CRN\'s species list!'.format(p))
                return
            if p in products:
                products[p] += 1
            else:
                products[p] = 1

        if(not [reactants, products] in self.RULESET):
            print('ERROR: Rule was not found in the CRN\'s ruleset!')
        else:
            self.RULESET.remove([reactants, products])

    def GetSpecies(self):
        return self.SPECIES

    def GetRuleset(self):
        return self.RULESET

    def RunConfiguration(self, config):
        if len(config) == len(self.SPECIES):

            temp = self.RULESET.copy()

            running = True
            canContinue = False

            while(running):
                while(len(temp) > 0):

                    index = random.randint(0, len(temp) - 1)

                    reactionCanOccur = True

                    for reactant in temp[index][0]:
                        if config[reactant] < temp[index][0][reactant]:
                            reactionCanOccur = False

                    if reactionCanOccur:
                        canContinue = True
                        for reactant in temp[index][0]:
                            config[reactant] -= temp[index][0][reactant]
                        for product in temp[index][1]:
                            config[product] += temp[index][1][product] 
                
                    temp.pop(index)
                
                if canContinue:
                    temp = self.RULESET.copy()
                    canContinue = False
                else:
                    running = False
        
            return config