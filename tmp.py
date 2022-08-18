from math import log2


def entropy(p):
    return -p * log2(p)

print(entropy(4/5) + entropy(1/5))