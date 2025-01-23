# region imports
from Die import rollFairDie as rfd
from Die import rollUnFairDie as rud
# endregion

# region functions
def rollDice(N=1):
    """
    This function simulates rolling N dice simultaneously by using a loop that rolls
    a single die N times and totaling the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    scores = 0
    for i in range(N): # Rolls die N amount of times
        score = rfd() # score = 1 to 6
        scores += score  # Increment score position 0 by the value rolled(score)
    return scores

    #end region


def rollUnFairDice(N=1):
    """
    This function simulates rolling N, UnFair dice simultaneously by using a loop that rolls
    a single die N times and totals the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    scores = 0
    for i in range(N):  # Rolls die N amount of times
        score = rud()  # score = 1 to 6
        scores += score  # Increment score position 0 by the value rolled(score)
    return scores

    #end region


# endregion

if __name__ == "__main__":
    x = rollDice()
    print(x)
    y = rollUnFairDice()
    print (y)