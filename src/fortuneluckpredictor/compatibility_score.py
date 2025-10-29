import random

def compatibility_score(name1: str, name2: str) -> str:
    # number of vowels per name
    v1 = 0
    v2 = 0
    vowels = ["a","e","i","o","u"]
    for v in vowels:
        c1 = name1.lower().count(v)
        c2 = name2.lower().count(v)
        if c1 > c2:
            v1 += (c1 - c2)
        else:
            v2 += (c2 - c1)

    score = v1 + v2
    return 