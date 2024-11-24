"""missing_number
"""


def missing_number(n: int, numbers) -> int:
    nset = set(numbers)
    all = set(range(1, n + 1))
    missing = all.difference(nset)
    return missing.pop() or 1


if __name__ == "__main__":
    n = int(input())
    numbers = [int(x) for x in input().split(" ")]
    print(missing_number(n, numbers))
