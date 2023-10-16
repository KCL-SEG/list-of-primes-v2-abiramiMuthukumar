"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if(number_of_primes > 0):
        list = []

        current_number = 2

        while(len(list) < number_of_primes):
            prime = True
            for i in range(2,current_number):
                if current_number%i == 0:
                    prime=False
                    break
                i+=1

            if prime == True:
                list.append(current_number)

            current_number+=1

        return list
    else:
        raise ValueError
