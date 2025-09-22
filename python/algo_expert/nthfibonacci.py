# recursive solution (bad)
# Time = O(2^n) 👎
# Space = O(n) 🤏

# def getNthFib(n):
#     if n == 2:
#         return 1
#     if n == 1:
#         return 0
#     return getNthFib(n-1) + getNthFib(n-2)

# recursive solution memoization (better)
# Time = O(n) 👍
# Space = O(n) 🤏


# def getNthFib(n, memoize={1: 0, 2: 1}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n - 1) + getNthFib(n - 2)
#         return memoize[n]


# iterative solution (best)
# Time = O(n) 👍
# Space = O(1) 👍

def getNthFib(n):
    if n <= 1:
        return 0
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

print(getNthFib(6))
