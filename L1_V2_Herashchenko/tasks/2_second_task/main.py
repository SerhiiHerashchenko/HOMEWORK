def primes_detector(bound):
    primes = [2]
    start = 1

    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    for i in range(3, bound):
        if is_prime(i):
            primes.append(i)

    return primes

def answer(list):
    ans_list = []
    
    for i in range(len(list) - 1):
            if list[i + 1] - list[i] == 2:
                ans_list.append((list[i], list[i + 1]))

    return ans_list

print(answer(primes_detector(100)))