import random
import timeit
import functools

def sum_digits(numbers):
    if numbers not in sum_digits.my_cache:
        sum_digits.my_cache[numbers] = sum(
            int(digit) for number in numbers for digit in str(number)
        )
    return sum_digits.my_cache[numbers]
sum_digits.my_cache = {}

numbers = tuple(random.randint(1, 1000) for _ in range(1_000_000))

print(
    timeit.timeit(
        "sum_digits(numbers)",
        globals=globals(),
        number=1
    )
)

print(
    timeit.timeit(
        "sum_digits(numbers)",
        globals=globals(),
        number=1
    )


sum = functools.cache(sum)

print(
    timeit.timeit(
        "sum(range(100_000_001))",
        globals=globals(),
        number=1,
    )
)

print(
    timeit.timeit(
        "sum(range(100_000_001))",
        globals=globals(),
        number=1,
    )
)