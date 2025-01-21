def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
            return False
    return True


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

prime_numbers = [num for num in numbers if is_prime(num)]

if prime_numbers:
    print(f"Prime numbers in the given list: {prime_numbers}")
else:
    print("No prime numbers found in the given list.")