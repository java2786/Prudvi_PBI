def isPrime(num):
    # num = 7
    is_prime = True 

    for d in range(2,1+num//2):
        if num % d == 0:
            is_prime = False
            break

    # if is_prime:
    #     print(f"{num} is prime")
    # else:
    #     print(f"{num} is not prime")
    return is_prime
        
        
# call / execute function
# isPrime(53)

for n in range(2, 101):
    response = isPrime(n)
    if response:
        print(f"{n} is prime number")