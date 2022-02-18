def getGreatestFamilyNum(num):

    """Return the greated number in a family of the given number"""

    number = int(''.join((sorted(str(num), reverse=True))))
    newNum = -1 if number > 100000000 else number 
    print('Greatest non-negative number in {0} family is {1}'.format(num, newNum))


getGreatestFamilyNum(553)
print(type (getGreatestFamilyNum(312)))

def convertIntToBinary(num1, num2):

    """Return sum of 1s in binary of an integer"""

    num = num1 * num2
    print('Using bin(), Binary of {0} = {1}'.format(num, bin(num1 * num2)))
    print('Using format(), Binary of {0} = {1}'.format(num, format(num1 * num2, 'b')))
    print('Using str.format(), Binary of {0} = {1}'.format(num, '{0:b}'.format(num1 * num2)))
    print('Count of 1s in binary is {}'.format(format(num1 * num2, 'b').count('1')))
    print(type(bin(num1 * num2)))
    print(type(format(num1 * num2, 'b')))
convertIntToBinary(3, 5)


#Quiz: A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded 
# by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 
# and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of 
# length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary 
# representation 100000 and has no binary gaps.

# Write a function:
# def solution(N)
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 
# if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and s
# o its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary 
# representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..2,147,483,647].
def split(word):
    return [char for char in word]

def solution(N):
    # write your code in Python 3.6
    binary = '{0:b}'.format(N) 

    res = len(split(binary)) - 1 - split(binary)[::-1].index('1') # index of last '1'
    binary = binary[binary.index('1'):res+1] # Slice the string to exclude trailing 0s
    zeroList = binary.split('1')

    maxmumz = 0
    for w in zeroList:
        if res == split(binary).index('1'):
            maxmumz = 0
            break
        if len(w) > maxmumz:
            maxmumz = len(w)
    
    return 0 if maxmumz == 0 else maxmumz


print(solution(529))
