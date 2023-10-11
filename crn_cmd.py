import ChemicalReactionNetwork as crn

def CRNCreator():
    print("Welcome to the CRN creator!\n")

    n = crn.ChemicalReactionNetwork()

    running = True
    while running:
        print('What do you want to do?\n(A)dd new species or rules.\n(D)elete species or rules.\n(V)iew the CRN.\n(R)un a configuration.\n(E)xit the creator.')
        option = input('>')

        if option == 'A' or option == 'a':
            adding = True
            while adding:
                print('Add a rule or species?\n(S)pecies.\n(R)ule.\n(E)xit.')
                option = input('>')

                if option == 'S' or option == 's':
                    print('Add as many species as you like. Use spaces to distinguish each species.')
                    species = input('>').split()

                    n.AddSpecies(species)
                elif option == 'R' or option == 'r':
                    print('Add the reactants of this rule. Use spaces to distinguish each reactant.')
                    reactants = input('>').split()

                    print('Add the products of this rule. Use spaces to distinguish each product.')
                    products = input('>').split()

                    n.AddRule([reactants, products])
                elif option == 'E' or option == 'e':
                    adding = False
                else:
                    print('Input not recognized!')

        elif option == 'D' or option == 'd':
            deleting = True
            while deleting:
                print('Delete a rule or species?\n(S)pecies.\n(R)ule.\n(E)xit.')
                option = input('>')

                if option == 'S' or option == 's':
                    print('Delete as many species as you like. Use spaces to distinguish each species.')
                    species = input('>').split()

                    n.DeleteSpecies(species)
                elif option == 'R' or option == 'r':
                    print('Add the reactants of the rule to delete. Use spaces to distinguish each reactant.')
                    reactants = input('>').split()

                    print('Add the products of the rule to delete. Use spaces to distinguish each product.')
                    products = input('>').split()

                    n.DeleteRule([reactants, products])
                elif option == 'E' or option == 'e':
                    deleting = False
                else:
                    print('Input not recognized!')
        elif option == 'V' or option == 'v':

            species_list = n.GetSpecies()

            if not species_list:
                print('No species listed!')
            else:
                print('The species of the CRN are: ')

                for count, species in enumerate(species_list):
                    print('{}. {}'.format(count + 1, species))

            rules_list = n.GetRuleset()

            if not rules_list:
                print('No rules listed!')
            else:
                print('The rules of the CRN are: ')

                for count, rule in enumerate(rules_list):
                    print('{}. {}'.format(count + 1, rule))
        elif option == 'R' or option == 'r':
            config = dict()

            if len(n.GetSpecies()) == 0 or len(n.GetRuleset()) == 0:
                print('The CRN is not properly created yet! Make some species or rules!')
                continue

            for i in n.GetSpecies():
                print('How much of species {} do you want in the configuration?'.format(i))

                amount = ' '.join(input('>').split())

                while not amount.isdigit():
                    print('Input must be a digit!')
                    amount = ' '.join(input('>').split())
                
                config[i] = int(amount)

            print(n.RunConfiguration(config))

        elif option == 'E' or option == 'e':
            print('We hope you enjoyed your time here!')
            running = False
        else:
            print("Input not recognized!\n")

    return

if __name__ == '__main__':
    print('Welcome to the CRN Simulator!\n')

    running = True
    while running:
        print('What do you want to do?\n(C)reate a new CRN.\n(E)xit the simulator.')
        option = input('>')

        if option == 'C' or option == 'c':
            CRNCreator()
        elif option == 'E' or option == 'e':
            print('We hope you enjoyed your time here!')
            running = False
        else:
            print("Input not recognized!\n")