"""weird_algorithm
"""


def even(n: int):
    return n % 2 == 0


def weird_algorithm(n: int):
    print(n, end=" ")
    if n == 1:
        print()
        return
    if even(n):
        weird_algorithm(round(n / 2))
    elif not even(n):
        weird_algorithm(n * 3 + 1)


if __name__ == "__main__":
    n = int(input())
    weird_algorithm(n)
