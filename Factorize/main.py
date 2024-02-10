"""
This is a programme that will generate a list of prime factors of a given
number.

We need to:

1. Ask the user to enter a number, which must be an integer, or "Q" to quit.
2. Compute & print the list of prime factors of this number
"""
#####################################
# Import libraries here, if necessary

#####################################
# Helper functions for this programme

# A "global" list of prime numbers known by this programme
primes = list()


def is_prime(number: int) -> bool:
    """
    To check whether a number of prime, we attempt to divide it by all known
    prime numbers. If none of them divide into our number, then it must be
    prime.

    NOTE: We need to use the modulo operator: %
          where a%b gives the remainer for a divided by b.
    """
    # Is `number` a prime number we already know?
    if number in primes:
        return True

    # We loop through the global list called `primes`...
    for prime in primes:
        # ... checking if they divide into `number` with no remainder...
        if number%prime == 0:
            # ... and if they do, `number` is not prime...
            return False
    # ... if we have got this far, then our number is NOT divisible by any
    # known prime, so it must be a new prime number. We add it to the list
    # and return True to say that this is indeed a prime number.
    primes.append(number)
    return True


def factors(number: int) -> list:
    """
    A function that works out prime factors of a given number
    """
    factors = list()
    prime = 1

    while number > 1:
        prime = prime + 1
        while not is_prime(prime):
            prime = prime + 1

        # loop until `prime` no longer divides in our number
        while number%prime == 0:
            # add `prime` to the list of factors
            factors.append(prime)
            # divide our number by this factor because we now need to find the
            # remaining factors (branching the prime factor tree):
            number = number / prime
    
    return factors


def group_factors(factors: list) -> dict:
    """
    We are taking a list of prime factors, e.g. [2, 2, 2, 5, 5, 5] and turning
    this into a dictionary that counts how many of each number there are.

    So, each unique prime factor will be the KEY in the dictionary, and the
    count of how many there are will be the VALUE for that key. In this example
    we expect to show that there are three 2s and three 5s like this:
    {
        2: 3,
        5: 3
    }
    """
    count = dict()

    # Loop through each entry in the list of factors:
    for factor in factors:
        # Have we seen this factor before?
        if factor in count.keys():
            count[factor] = count[factor] + 1
        else:
            count[factor] = 1
    
    return count


def format_powers(factors: list) -> str:
    """
    Takes a dictionary where the keys are prime factors of a number
    and the keys are the exponents of that factor, i.e. how many times
    that factor divides into that number.
    """
    formatted = ""

    # Get the factors grouped in a dictionary
    powers_of = group_factors(factors)

    # Loop through each key in the dictionary
    for factor in powers_of:
        # ... adding to the formatted string
        formatted += f"{factor}^{powers_of[factor]}, "

    # Remvoing the final ", " from the end of the string
    return formatted.strip(", ")


###################################
# The main programme starts here

while True:
    number = input("Please enter a number or 'q' to exit: ") # returns a string
    if number.lower() == "q":
        break

    # input() returns a string, which we need to turn into an integer
    integer = int(number)

    # We will use a function to generate the prime factors of this integer.
    print(f"The prime factors of {integer} are: {factors(integer)}")

    # Turning a LIST into a SET removes any duplicates:
    print(f"The list of unique prime factors is: {set(factors(integer))}")

    # Simplify the prime factors by grouping together with exponents
    print(f"The unique factors with their exponents is: {format_powers(factors(integer))}")