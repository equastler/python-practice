def locate_card(cards, query):
    lo = 0
    hi = len(cards) - 1
    while lo <= hi:
        guess = cards[(lo + hi) // 2]
        if guess < query:
            hi = ((lo + hi)//2) - 1
        elif guess > query:
            lo = ((lo + hi)//2) + 1
        elif guess == query:
            return (lo + hi) // 2

#above = binary search alg for dec order time complexity O(logN) -- linear search would be O(N)
