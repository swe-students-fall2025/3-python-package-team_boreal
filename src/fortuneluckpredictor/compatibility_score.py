def compatibility_score(name1: str, name2: str) -> str:
    score = 0
    vowels = "aeiou"
    c = [] # each vowel's count
    n1 = name1.lower()
    n2 = name2.lower()
    for v in vowels:
        c1 = n1.count(v)
        c2 = n2.count(v)
        n = abs(c1 - c2)
        c.append(n)

    # Add vowel counts next to each other together until one digit remains
    while(len(c) > 1):
        new_c = []
        for i in range(len(c) - 1):
            new_c.append((c[i] + c[i+1]) % 10)
        c = new_c

    score = c[0]
    # compatibility message based on final score
    if score <= 2:
        message = "Perfect match — pure harmony! 💞"
    elif score <= 4:
        message = "You two vibe really well! ❤️"
    elif score <= 7:
        message = "There's potential — stay open and see where it goes! 🌈"
    else:
        message = "You'll meet someone wonderful who complements you perfectly! 💫"

    return f"Compatibility score: {score}. {message}"