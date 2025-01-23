# region imports
import random as rnd
import statistics as stats

#Collaborated with Kaleb Clyma and Brayden Taylor
# endregion

# region functions
def between(num, low, high, inclusivelow=True, inclusivehigh=True):
    """
    I wrote this function to return a boolean to indicate if num is in a range
    :param num: the number to check
    :param low: the low end of the range
    :param high: the high end of the range
    :param inclusivelow: bool to include the low end
    :param inclusivehigh: bool to include the high end
    :return: bool indicating if between low and high limits
    """
    if inclusivelow and inclusivehigh:
        return low <= num <= high
    elif inclusivelow and not inclusivehigh:
        return low <= num < high
    elif not inclusivelow and inclusivehigh:
        return low < num <= high
    else:
        return low < num < high
    pass


def main():
    """
    This function produces an array of numbers from a normally distributed population

    To check if the numbers generated are normally distributed, I can count
    the percentage within 1,2 and 3 standard deviations of the mean and see
    if they match the theoretical values.  I'll create 3 bins into which the
    numbers in my array will fit.  Note:  a number in bin 1 will also be in bins
    2 & 3.  A number in bin3 will not necessarily be in 1 or 2.
    :return: nothing
    """
    N = 1000  # size of array I want
    arr = []  # array for storing the numbers
    mean = 50  # the mean I want
    stdev = 10  # the standard deviation

    bin1=0  # normal dist should contain 68% within +/-1stdev
    bin2=0  # normal dist should contain 95.5% within +/-2stdev
    bin3=0  # normal dist should contain 99.7% within +/-3stdev

    for i in range(N):  # this loop generates the numbers
        num = rnd.normalvariate(mean, stdev) #Return random numbers from given mean and standard deviation
        arr.append(num)

    sample_mean = stats.mean(arr) #Returns the mean of set of numbers or specified array
    sample_stdev = stats.stdev(arr) #Returns the standard deviation of set of numbers or specified array

    # find edges of the limits for the various bins
    bin1low = sample_mean - sample_stdev
    bin1high = sample_mean + sample_stdev

    bin2low = sample_mean - 2*sample_stdev
    bin2high = sample_mean + 2*sample_stdev

    bin3low = sample_mean - 3*sample_stdev
    bin3high = sample_mean + 3* sample_stdev

    for num in arr: # this checks which bin(s) the current number is in.

        if bin1low <= num <= bin1high:
            bin1 += 1
        if bin2low <= num <= bin2high:
            bin2 += 1
        if bin3low <= num <= bin3high:
            bin3 += 1

    print(f'Generated Numbers (first 10 values): {arr[:10]}')

    print()

    print(f'Sample mean: {sample_mean: .2f}')
    print(f'Sample standard deviation: {sample_stdev: .2f}')

    print()

    #print(arr)  # If I want to see the actual array, uncomment this.
    print("{:.1f}% of data within +/-1 StDev of mean.".format(100*bin1/N))
    print("{:.1f}% of data within +/-2 StDev of mean.".format(100*bin2/N))
    print("{:.1f}% of data within +/-3 StDev of mean.".format(100*bin3/N))
# endregion

if __name__ == "__main__":
    main()  # calls the function main
