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
