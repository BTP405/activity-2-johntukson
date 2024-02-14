def checkPrime(num):
    if (num == 1):
        return False
    else:
        return True

def getPrimeNumbers(n):

    """
    Check if the parameter is a prime number. 
    Set a variable called "Prime" to True.
    If n is not 1, loop through number range from 2 - n
    If a factor is found, prime is set to false
    If a factor is not found, Prime is equal to true so the number is printed 
    """

    if checkPrime(n):
        for num in range(2,n):
            prime = True
            for i in range(2,num):
                if (num % i == 0):
                    prime = False
            if prime:
                print(num)
    else:
        print('Number is not Prime')

getPrimeNumbers(10)