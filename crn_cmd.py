import regular_crn
import step_crn


def CRNCreator():
    print('Welcome to the CRN creator!\n')
    crn = None
    print('First, chose your CRN type:\n(R)egular CRN\n(S)tep CRN\n')
    crn_type = input('>')

    if crn_type == 'S' or crn_type == 's':
        crn = step_crn.StepChemicalReactionNetwork()
    else:
        crn = regular_crn.ChemicalReactionNetwork()

    print('Now let\'s add the species of your CRN.\n')
    SpeciesAdder(crn)
    print('Next, let\'s add the ruleset of your CRN.\n')
    RuleAdder(crn)

    if isinstance(crn, step_crn.StepChemicalReactionNetwork):
        print('Time to add the steps of your CRN.\n')
        StepAdder(crn)

    print('Finally, let\'s create a configuration for your system to run on.\n')
    ConfigRunner(crn)

    return


def SpeciesAdder(crn):
    while True:
        species_list = crn.GetSpecies()
        print('Your current species alphabet:')

        if not species_list:
            print('0')
        else:
            for count, species in enumerate(species_list):
                if count:
                    print(',')
                print('{}. {}'.format(count + 1, species), end='')
            print()

        print('To stop adding species, enter a blank input.')
        species = input('>').split()

        if not species:
            return
        else:
            species_added = []
            for s in species:
                if crn.AddSpecies(s):
                    species_added.append(s)

            if not species_added:
                print('No new species were successfully added.')
            else:
                print('The following new species were added:')
                for count, species in enumerate(species_added):
                    if count:
                        print(', ', end='')
                    print('{}'.format(species), end='')

            print()


def RuleAdder(crn):
    while True:
        ruleset = crn.GetRules()
        species_list = crn.GetSpecies()
        print('Your current ruleset:')

        if not ruleset:
            print('0')
        else:
            for count, rule in enumerate(ruleset):
                if count:
                    print(',')
                print('{}. {}'.format(count + 1, RuleNotation(rule, species_list)), end='')
            print()

        print('To stop adding rules, enter a blank input for both reactants and products.')
        print('You are adding reactants.')
        reactants = input('>').split()
        print('You are adding products.')
        products = input('>').split()

        if not reactants and not products:
            return
        else:
            reactants_config = [0] * len(species_list)
            products_config = [0] * len(species_list)

            for r in reactants:
                try:
                    idx = species_list.index(r)
                    reactants_config[idx] += 1
                except ValueError:
                    continue

            for p in products:
                try:
                    idx = species_list.index(p)
                    products_config[idx] += 1
                except ValueError:
                    continue
                
            rule_added = []

            if crn.AddRule([reactants_config, products_config]):
                rule_added = [reactants_config, products_config]

            if not rule_added:
                print('No new rule was successfully added.')
            else:
                print('Added the following new rule:')
                print(RuleNotation(rule_added, species_list))       
                print()


def StepAdder(crn):
    while True:
        steps = crn.GetSteps()
        species_list = crn.GetSpecies()
        print('Your current steps:')

        if not steps:
            print('0')
        else:
            for count, step in enumerate(steps):
                if count:
                    print(',')
                print('Add: ' + ConfigNotation(step, species_list), end='')
            print()

        print('To stop adding steps, enter a blank input.')
        step_species = input('>').split()

        if not step_species:
            return
        else:
            steps_config = [0] * len(species_list)

            for s in step_species:
                try:
                    idx = species_list.index(s)
                    steps_config[idx] += 1
                except ValueError:
                    continue

            step_added = []

            if crn.AddStep(steps_config):
                step_added = steps_config

            if not step_added:
                print('No new step was successfully added.')
            else:
                print('Added the following new step:')
                print('Add: ' + ConfigNotation(step_added, species_list))    
                print()


def ConfigRunner(crn):
    print("Welcome to the CRN configuration runner!\n")

    while True:
        species_list = crn.GetSpecies()
        print('Enter the initial configuration of your CRN system.')
        config_species = input('>').split()
        initial_config = [0] * len(species_list)

        for s in config_species:
            try:
                idx = species_list.index(s)
                initial_config[idx] += 1
            except:
                break

        terminal_config = crn.RunConfiguration(initial_config)
        print('Your initial configuration was:')
        print(ConfigNotation(initial_config, species_list))
        print('And your terminal configuration is:')
        print(ConfigNotation(terminal_config, species_list))
        print('Want to re-run with a new configuration? Type in (Y)es if so.')
        option = input('>')

        if option != 'Y' and option != 'y':
            return


def RuleNotation(rule, species_list):
    notation = ''

    for i in [0, 1]:
        first_species = True
        void_set = True

        for index, species in enumerate(rule[i]):
            if species:
                if index and not first_species:
                    notation += ' + '

                notation += '{}{}'.format(str(species) if species > 1 else '', str(species_list[index]))

                if first_species:
                    first_species = False
                    void_set = False

        if void_set:
            notation += '0'

        if not i:
            notation += ' -> '

    return notation


def ConfigNotation(config, species_list):
    notation = ''

    first_species = True
    void_set = True

    for index, species in enumerate(config):
        if species:
            if index and not first_species:
                notation += ', '

            notation += '{}{}'.format(str(species) if species > 1 else '', str(species_list[index]))

            if first_species:
                first_species = False
                void_set = False

    if void_set:
        notation += '0'

    return notation


if __name__ == '__main__':
    print('Welcome to the CRN Simulator!\n')

    while True:
        print('What do you want to do?\n(C)reate a new CRN.\n(E)xit the simulator.')
        option = input('>')

        if option == 'C' or option == 'c':
            CRNCreator()
        elif option == 'E' or option == 'e':
            print('We hope you enjoyed your time here!')
            break
        else:
            print("Input not recognized!\n")