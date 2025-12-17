# Find if given num is prime

num = 29
is_prime = True 

for d in range(2,1+num//2):
    if num % d == 0:
        # print(f"{d}: {num} is divisible by {d}, thus {num} is not prime")
        is_prime = False
        break
    # else:
    #     print(f"{num} not divided by {d}")
    
    

if is_prime:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")