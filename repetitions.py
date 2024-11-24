"""repetitions
"""


def repetitions(seq: str) -> int:
    max = 0
    current = 1
    for idx, char in enumerate(seq):
        if idx > 0:
            if char == seq[idx - 1]:
                current += 1
            else:
                max = current + 1 if current > max else max
                current = 0

    max = current if current > max else max
    return max


if __name__ == "__main__":
    seq = input()
    print(repetitions(seq))
