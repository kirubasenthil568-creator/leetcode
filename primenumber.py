n = int(input("Enter the number: "))
primes = []

if n < 2:
    print("No prime numbers less than 2")
else:
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print("The prime numbers up to", n, "are:", primes)