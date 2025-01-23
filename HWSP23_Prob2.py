#region imports
from Dice import rollDice as rfdi
from Dice import rollUnFairDice as rudi
#endregion

print()

#region functions
def main():  # main function to roll nDice fair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: The probability of rolling each score after rolling nDice fair dice nRolls times.
    """
    print('Fair Dice Program')
    print()

    nDice = 2

        #int(input("How many dice to be rolled? "))) # number of dice
    #print('You entered: ',nDice)
    #print()

    nMinScore = nDice * 1  # total score if each die scores 1
    nMaxScore = nDice * 6  # total score if each die scores 6
    nNumScores = nMaxScore-nMinScore+1 # number of possible scores
    nTally = [0] * (nMaxScore-nMinScore+1)  # create a list with (nMaxScore-nMinScore+1) elements/items

    nRolls = 1000

        #int(input('How many times to roll the dice? '))  # how many times to roll the dice
    #print('You entered: ',nRolls)
    #print()

    for i in range(nRolls):  # each loop rolls dice and increments a score
        score = rfdi(N=nDice)  # call with N=nDice
        nTally[score-nMinScore] += 1 # increment score-nMinScore item b/c 0 indexing start

    print('After rolling the {} fair die/dice {} times, '
          'the number of times each value from {} to {} was rolled is: '
          .format(nDice, nRolls, nMinScore, nMaxScore))

    for item in nTally:
        print(item)
    print()

    print('The total number of possible scores for', nDice, 'dice is:', nNumScores)

    print()

    for i in range(nNumScores):  # print the fraction of rolls for each score
        prob = nTally[i]/nRolls
        print(f'The probability of rolling a {i + nMinScore}: {prob: .4f}')

    #print()
    #print('The probability of each score for ' + str(nMinScore) + ' to ' + str(nMaxScore) + ' is: ')
    
    #for i in range(nNumScores):  # print the fraction of rolls for each score
    #    prob = [x / nRolls for x in nTally]
    
    #for item in prob:
    #    print(item)

    #end region


def main2():  # main function to roll nDice unfair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: The probability of rolling each score after rolling nDice unfair dice nRolls times.
    """
    print()
    print('Unfair Dice Program')
    print()

    nDice = 5

    # int(input("How many dice to be rolled? "))) # number of dice
    # print('You entered: ',nDice)
    # print()

    nMinScore = nDice * 1  # total score if each die scores 1
    nMaxScore = nDice * 6  # total score if each die scores 6
    nNumScores = nMaxScore-nMinScore+1  # number of possible scores
    nTally = [0] * (nMaxScore - nMinScore + 1)  # create a list with (nMaxScore-nMinScore+1) elements/items

    nRolls = 1000

    # int(input('How many times to roll the dice? ')))  # how many times to roll the dice
    # print('You entered: ',nRolls)
    # print()

    for i in range(nRolls):  # each loop rolls dice and increments a score
        score = rudi(N=nDice)  # call with N=nDice
        nTally[score - nMinScore] += 1  # increment score-nMinScore item b/c 0 indexing start

    print('After rolling the {} unfair die/dice {} times, '
          'the number of times each value from {} to {} was rolled is: '
          .format(nDice, nRolls, nMinScore, nMaxScore))

    for item in nTally:
        print(item)
    print()


    print('The total number of possible scores for', nDice, 'dice is:', nNumScores)
    print()

    for i in range(nNumScores):  # print the fraction of rolls for each score
         prob = nTally[i]/nRolls
         print(f'The probability of rolling a {i + nMinScore}: {prob: .4f}')

    #print()
    #print('The probability of each score for ' + str(nMinScore) + ' to ' + str(nMaxScore) + ' is: ')

    #prob = [x / nRolls for x in nTally]

    #for item in prob:
    #    print(item)

#endregion


#this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()